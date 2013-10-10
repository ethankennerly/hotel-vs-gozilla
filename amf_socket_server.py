#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Twisted networking and PyAMF encoding with application hooks.
Adapted from example text socket using Twisted.
Edited for AMF objects by Ethan Kennerly   http://finegamedesign.com
"""


try:
    import twisted
except ImportError:
    print "This server requires the Twisted framework. Download it from http://twistedmatrix.com"
    raise SystemExit

from twisted.internet.protocol import Protocol, Factory
from twisted.internet import reactor

from pyamf import remoting
import pyamf
import logging
import amf_socket_client


class transport_mock:  
    def write(self, message):  
        print 'transport.write(%s)' % len(message)
    def loseConnection(self):  
        print 'transport.loseConnection()'

def protocol_mock(factory):
    protocol = AmfSocketProtocol()
    protocol.factory = factory
    protocol.transport = transport_mock()
    def print_message(message):
        print message
    protocol.on_receive = print_message
    def print_on_error():
        print 'on_error'
    protocol.on_error = print_on_error
    return protocol

def factory_mock(): 
    return AmfSocketFactory('localhost', 8000, 
        'socket-policy.xml', 843)

def write_to_file(amf_data, basename):
    '''Write raw AMF data to file.
    see amf_socket_client.py: example()'''
    if amf_data:
        path = './log/%s.amf' % basename
        logging.warn('write_to_file: path: %s' % path)
        file = open(path, 'wb')
        file.write(amf_data)
        file.close()
        del file


import time
class AmfSocketProtocol(Protocol):
    '''Application server may conveniently subclass and customize reactions.
    Such as on_receive.
    '''
    timeout = 60000
    object_encoding = amf_socket_client.object_encoding

    def __init__(self):
        self.encoder = pyamf.get_encoder(self.object_encoding)
        self.connection_serial = None
        self.sends = []

    def on_connect(self):
        message = {'gateway_mc': {'currentLabel': 'connect'}}
        self.send(message)

    def on_disconnect(self, reason):
        pass

    def on_error(self):
        message = {'gateway_mc': {'currentLabel': 'unclear'}}
        self.send(message)

    def on_receive(self, message):
        self.broadcast(message)

    def connectionLost(self, reason):
        '''Remove connection from list.
        >>> factory = factory_mock() 
        >>> ethan = protocol_mock(factory)

        Even if serial number not connected, gracefully disconnect.
        >>> ethan.factory.connections.has_key(ethan.connection_serial)
        False
        >>> ethan.connectionLost('[closed cleanly]')
        connectionLost:  error None not connected []

        Expect to connect before disconnect.
        >>> ethan.connectionMade()
        transport.write(40)
        >>> ethan.connection_serial
        0
        >>> ethan.factory.connections.has_key(ethan.connection_serial)
        True
        >>> ethan.connectionLost('[closed cleanly]')

        Even if serial number not connected, gracefully disconnect.
        >>> ethan.connectionLost('[closed cleanly]')
        connectionLost:  error 0 not connected [0]
        >>> ethan.factory.connections.has_key(ethan.connection_serial)
        True

        Ethan and Wout connect, and take a number in order.
        >>> ethan = protocol_mock(factory)
        >>> ethan.connectionMade()
        transport.write(40)
        >>> ethan.connection_serial
        1
        >>> wout = protocol_mock(factory)
        >>> wout.connectionMade()
        transport.write(40)
        >>> wout.connection_serial
        2

        Ethan disconnects.  Wout keeps his number.
        >>> ethan.connectionLost('[closed cleanly]')
        >>> wout.connection_serial
        2

        Ethan reconnects on next number.
        >>> ethan = protocol_mock(factory)
        >>> ethan.connectionMade()
        transport.write(40)
        >>> ethan.connection_serial
        3
        >>> wout.connection_serial
        2
        >>> wout.connectionLost('[closed cleanly]')
        >>> ethan.connectionLost('[closed cleanly]')
        '''
        disconnect_note = ' disconnected %s because %s' \
            % (self.connection_serial, reason)
        logging.info(disconnect_note)
        Protocol.connectionLost(self, reason)
        if self.connection_serial in self.factory.connections \
                and self.factory.connections[self.connection_serial]:
            self.factory.connections[self.connection_serial] = None
        else:
            error = 'connectionLost:  error %s not connected %s' \
                    % (self.connection_serial, self.factory.connections.keys())
            logging.error(error)
            print error
        self.on_disconnect(reason)

    def connectionMade(self):
        self.buffer = ''
        if len(self.factory.connections) >= self.factory.max_connections:
            self.transport.write('Too many connections, try again later')
            self.transport.loseConnection()
            return
        self.connection_serial = len(self.factory.connections)
        self.factory.connections[self.connection_serial] = self
        connection_note = ' connected %i' % self.connection_serial
        logging.info(connection_note)
        self.on_connect()
        self.timeout_deferred = reactor.callLater(
                AmfSocketProtocol.timeout, 
                self.transport.loseConnection)

    def dataReceived(self, data):
        r'''Gracefully wait for incomplete data to complete with end of file.
        http://www.gossamer-threads.com/lists/python/python/765105

        >>> factory = factory_mock()
        >>> ethan = protocol_mock(factory)
        >>> ethan.connectionMade()
        transport.write(40)

        Gracefully receive incomplete policy request until complete.
        >>> ethan.dataReceived('<policy-file-request/')
        on_error
        >>> ethan.dataReceived('>\x00')
        transport.write(241)
        transport.loseConnection()
        '''
        raw = 'dataReceived:  raw %s' % amf_socket_client.represent(data)
        logging.debug(raw)
        now = time.time()
        length = len(data)
        packet_log = 'server.dataReceived: %f, %i, %i' \
                % (now, self.connection_serial, length)
        logging.info(packet_log)
        self.buffer += data
        if _serve_policy(self, self.buffer):
            logging.error('policy requested on wrong protocol; transport %s' \
                    % self.transport.__dict__)
        else:
            message = amf_socket_client.decode_object(data)
            if IOError is message:
                logging.error( 'IOError transport: %s' % self.transport.__dict__)
                self.on_error()
            elif message:
                self.on_receive(message)
        if self.timeout_deferred:
            self.timeout_deferred.cancel()
            self.timeout_deferred = reactor.callLater(
                    AmfSocketProtocol.timeout, 
                    self.transport.loseConnection)

    def send(self, message):
        r'''Encode text into ActionScript Messaging Format, and transmit.
        >>> factory = factory_mock()
        >>> ethan = protocol_mock(factory)
        >>> ethan.connectionMade()
        transport.write(40)
        >>> ethan.send("{'currentLabel': 'lobby'}")
        transport.write(27)
        >>> ethan.sends[-1]
        "\x063{'currentLabel': 'lobby'}"
        >>> ethan.send("{'currentLabel': 'login'}")
        transport.write(27)
        >>> ethan.sends[-1]
        "\x063{'currentLabel': 'login'}"
        '''
        message_text = amf_socket_client.represent(message)
        statement = 'server.send: %s: %s' % (self.connection_serial,
                message_text)
        logging.debug(statement)
        amf_data = amf_socket_client.encode_object(self.encoder, message)
        now = time.time()
        length = len(amf_data)
        packet_log = 'server.send: %f, %i, %i' \
                % (now, self.connection_serial, length)
        logging.info(packet_log)
        self.transport.write(amf_data)
        self.on_send(message, amf_data)
        self.sends.append(amf_data)

    def log_send(self, message, amf_data):
        id = '%i_%i' % (self.connection_serial, len(self.sends))
        write_to_file(amf_data, id)

    def on_send(self, message, amf_data):
        ## self.log_send(message, amf_data)
        pass

    def broadcast(self, message): 
        connections = self.factory.connections
        broadcast = 'broadcast:  %s, %s' % (message, connections)
        logging.info(broadcast)
        for serial, connection in connections.items():
            logging.debug(str(serial) + str(connection))
            connection.send(message)


class AmfSocketFactory(Factory):
    protocol = AmfSocketProtocol
    max_connections = 100

    def __init__(self, amf_host, amf_port, 
            policy_file, policy_port):
        self.connections = {}
        self.amf_host = amf_host
        self.amf_port = amf_port
        self.policy_file = policy_file
        self.policy_port = policy_port

    def setup(self):
        reactor.listenTCP(int(self.amf_port), 
                self, interface = self.amf_host)
        reactor.listenTCP(int(self.policy_port), 
                SocketPolicyFactory(self.policy_file),
                          interface = self.amf_host)
        logging.warn("Running Socket AMF gateway on %s:%s" \
                % (self.amf_host, self.amf_port) )
        logging.warn("Running Policy file %s server on %s:%s" \
                % (self.policy_file, self.amf_host, self.policy_port) )
        return reactor


def _serve_policy(protocol, buffer):
    '''Snippet to serve policy from a protocol.  
    >>> factory = factory_mock()
    >>> ethan = protocol_mock(factory)
    >>> _serve_policy(ethan, '<policy-file-request/')

    Need not have null character.
    >>> _serve_policy(ethan, '<policy-file-request/>')
    transport.write(241)
    transport.loseConnection()
    True
    '''
    if buffer.startswith('<policy-file-request/>'):
        policy = open(protocol.factory.policy_file, 'rt').read()
        protocol.transport.write(policy)
        protocol.transport.loseConnection()
        return True
    
class SocketPolicyProtocol(Protocol):
    """
    Serves strict policy file for Flash Player >= 9,0,124.
    
    @see: U{http://adobe.com/go/strict_policy_files}
    """
    def connectionMade(self):
        self.buffer = ''

    def dataReceived(self, data):
        self.buffer += data
        _serve_policy(self, self.buffer)


class SocketPolicyFactory(Factory):
    protocol = SocketPolicyProtocol

    def __init__(self, policy_file):
        """
        @param policy_file: Path to the policy file definition
        """
        self.policy_file = policy_file

    def getPolicyFile(self, protocol):
        return open(self.policy_file, 'rt').read()


def run_server():
    factory = AmfSocketFactory(
            'localhost', 5900, 
            'socket-policy.xml', 843)
    reactor = factory.setup()
    reactor.run()  # Infinite loop blocks execution


import code_unit
if __name__ == '__main__':
    from optparse import OptionParser
    parser = OptionParser()
    parser.add_option("--unit", default="",
        dest="unit", help="unit to doctest [default: %default]")
    parser.add_option("--test", default="",
        help="test all doctests [default: %default]")
    (options, args) = parser.parse_args()

    if options.unit:
        unit = eval(options.unit)
        code_unit.doctest_unit(unit)
    elif options.test:
        units = globals().values()
        code_unit.doctest_units(units)
    else:
        run_server()



