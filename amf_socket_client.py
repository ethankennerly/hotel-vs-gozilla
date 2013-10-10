#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
Adapted from example text socket using Twisted.

@see: U{Wiki page for this example<http://pyamf.org/wiki/BinarySocket>}

@since: 0.1

Edited for object by Ethan Kennerly   http://finegamedesign.com
'''
__author__ = 'Ethan Kennerly'
# Socket networking and PyAMF encoding


def greets_example():
    r'''Send a message to server.
    >>> from test_network import subprocess_gateway
    >>> gateway_process = subprocess_gateway(file = 'amf_socket_server_test.py')
    >>> def pass_this(news):
    ...     pass
    >>> client = AmfSocketClient(on_receive = pass_this)
    >>> client.connect('localhost', 5900)

    Soon, the server acknowledges the connection.
    >>> time.sleep(2)
    >>> client.receives[-1]
    {'gateway_mc': {'currentLabel': u'connect'}}

    Only when necessary to debug,
    Test protocol writes raw AMF data it sent, one file per message in /log/#.amf
    Protocol is volatile, so the numbering may restart and overwrite frequently.
    >>> time.sleep(0.25)
    >>> import os
    >>> os.path.exists('./log/0.amf')
    True
    >>> file = open('./log/0.amf', 'rb')
    >>> server_send_0 = file.read()
    >>> client.receives[0]
    {'gateway_mc': {'currentLabel': u'connect'}}
    >>> client_receive_0 = encode_object(client.encoder, client.receives[0]) 
    >>> len(client_receive_0)
    40
    >>> len(server_send_0)
    40
    >>> client_receive_0 == server_send_0
    True
    >>> client_receive_0.__repr__()
    "'\\n\\x0b\\x01\\x15gateway_mc\\n\\x01\\x19currentLabel\\x06\\x0fconnect\\x01\\x01'"
    >>> server_send_0.__repr__()
    "'\\n\\x0b\\x01\\x15gateway_mc\\n\\x01\\x19currentLabel\\x06\\x0fconnect\\x01\\x01'"
    >>> file.close()
    >>> del file

    After connection message, if enabled, send greeting.
    >>> from amf_socket_server_test import greets_protocol
    >>> greets_protocol.on_connect_greets
    ['log/greet/0.amf', 'log/greet/1.amf', 'log/greet/2.amf']

    I used this to test an archived message.
    >>> greets_protocol.combine
    False
    >>> client.send({0: 0})
    >>> time.sleep(1.0 / 4)
    >>> client.send({1: 1})
    >>> time.sleep(1.0 / 4)
    >>> client.send({2: 2})
    >>> time.sleep(1.0 / 4)
    >>> len(client.receives)
    4
    >>> client_receive = client.receives[-1]
    >>> os.path.exists('./log/greet/2.amf')
    True
    >>> file = open('./log/greet/2.amf', 'rb')
    >>> server_send = file.read()
    >>> server_object = decode_object(server_send)
    >>> if not client_receive == server_object:
    ...     print 'client_receive:', client_receive.__repr__()
    ...     print 'server_send:', server_send.__repr__()
    >>> file.close()
    >>> del file

    Soon, the client enters the service.
    >>> time.sleep(1)
    >>> entering = {'gateway_mc': {'currentLabel': u'entering'}}
    >>> client.send(entering)
    >>> if not client.sends[-1] == entering:
    ...     client.sends[-1], entering

    Soon, the default server echoes or broadcasts back the message.
    >>> time.sleep(1)
    >>> client.receives[-1]
    {'gateway_mc': {'currentLabel': u'entering'}}
    >>> if not client.receives[-1] == entering:
    ...     client.receives[-1], entering

    Unlike Flash, during a single server protocol send,
    this AMF client only receives single message from server.
    
    Disconnect, so that listener will go away.
    >>> client.is_alive = False
    '''



def split_example():
    r'''Send a message to server.
    >>> from test_network import subprocess_gateway
    >>> gateway_process = subprocess_gateway(file = 'amf_socket_server_split.py')
    >>> def pass_this(news):
    ...     pass
    >>> client = AmfSocketClient(on_receive = pass_this)
    >>> client.connect('localhost', 5900)

    Soon, the server acknowledges the connection.
    >>> time.sleep(2)
    >>> client.receives[-1]
    {'gateway_mc': {'currentLabel': u'connect'}}

    Only when necessary to debug,
    Test protocol writes raw AMF data it sent, one file per message in /log/#.amf
    Protocol is volatile, so the numbering may restart and overwrite frequently.

    After connection message, if enabled, send greeting.
    >>> from amf_socket_server_split import split_protocol
    >>> split_protocol.on_connect_greets
    ['log/greet/0.amf', 'log/greet/1.amf', 'log/greet/2.amf']

    I used this to test an archived message.
    >>> client.send({0: 0})
    >>> time.sleep(1.0 / 4)
    >>> client.send({1: 1})
    >>> time.sleep(1.0 / 4)
    >>> client.send({2: 2})
    >>> time.sleep(1.0 / 4)
    >>> len(client.receives)
    4
    >>> client.receives[-1]
    >>> client.receives

    Unlike Flash, during a single server protocol send,
    this AMF client only receives single message from server.
    
    Disconnect, so that listener will go away.
    >>> client.is_alive = False
    '''



def as_object_to_dict(as_object):
    '''Recursively copy and convert a pyAMF ActionScript Object 
    into a Python dictionary.
    >>> as_object = ASObject({'a': ASObject({'b': 2})})
    >>> type(as_object)
    <class 'pyamf.ASObject'>
    >>> type(as_object['a'])
    <class 'pyamf.ASObject'>
    >>> type(as_object_to_dict(as_object))
    <type 'dict'>
    >>> type(as_object_to_dict(as_object)['a'])
    <type 'dict'>
    >>> as_object_to_dict(as_object)
    {'a': {'b': 2}}

    Equivalently, could evaluate string representation 
    of the ActionScript object
    >>> as_object = ASObject({'a': ASObject({'b': 2})})
    >>> type(eval(str(as_object)))
    <type 'dict'>
    >>> type(eval(str(as_object))['a'])
    <type 'dict'>
    '''
    duplicate = copy.deepcopy(as_object)
    if not hasattr(duplicate, 'items'):
        return duplicate
    else:
        dictionary = dict(duplicate)
        for key, value in dictionary.items():
            dictionary[key] = as_object_to_dict(value)
        return dictionary


# Socket networking and PyAMF encoding

import logging
import simple_socket
import pyamf
from pyamf import remoting
object_encoding = pyamf.AMF3
# object_encoding = pyamf.AMF0
import time

# ActionScript Messaging Format

def encode_object(encoder, message):
    logging.debug('encode_object:  %s' % represent(message) )
    encoder.writeElement(message)
    amf_data = encoder.stream.getvalue()
    encoder.stream.truncate()
    encoder.context.clear()
    return amf_data

def represent(data, max = 256):
    text = data.__repr__()
    if max < len(text):
        text = text[:max] + '...'
    return text
    
def decode_object(amf_data):
    '''Is the object limited to a size less than about 40 kB to 90 kB?'''
    raw_text = represent(amf_data)
    raw = 'decode_object:  amf_data: %s' % raw_text
    logging.debug(raw)
    decoder = pyamf.get_decoder(object_encoding, amf_data)
    ## logging.debug('decode_object: stream: ' + represent(decoder.stream))
    message = None
    try:
        # XXX Sometimes ASObject whose string representation is 68 kB 
        # returns an IOError.
        message = decoder.readElement()
    except IOError:
        logging.error(raw)
        logging.error('decode_object IOError')
        # XXX Will another dataReceived callback occur?
        return IOError
    except pyamf.EOStream:
        logging.error(raw)
        end_of_stream = 'decode_object:  EOStream'
        logging.error(end_of_stream)
        return IOError
    except pyamf.DecodeError:
        logging.error(raw)
        decode_error = 'decode_object:  DecodeError'
        logging.error(decode_error)
        
        return IOError
    except:
        logging.error(raw)
        error = 'decode_object:  Error'
        logging.error(error)
        raise
    if message is not None:
        decoded = 'decode_object:  decoded %s' % represent(message)
        logging.debug(decoded)
        if pyamf.ASObject != type(message) and dict != type(message):
            not_an_object = 'decode_object:  i was expecting simple object:  %s' \
                    % represent(message)
            logging.error(not_an_object)
            return IOError
    else:
        no_message = 'decode_object:  no message? "%s"' % represent(message)
        logging.warn(no_message)
    return message

def validate(message, amf_data):
    '''validate encoding by decoding.'''
    decoded = decode_object(amf_data)
    if decoded != message:
        mismatch = 'send: message %s does not match decoded %s' \
                % (message, decoded)
        logging.debug(mismatch)
        return False
    return True

minimum_interval = 0.25
class AmfSocketClient(object):
    def __init__(self, on_receive = None, minimum_interval = minimum_interval):
        self.socket = simple_socket.socket_class()
        self.sends = []
        self.receives = []
        self.is_alive = None
        self.encoder = pyamf.get_encoder(object_encoding)
        self.on_receive = on_receive
        self.receive_time = None
        self.minimum_interval = minimum_interval
        ## self.connect(amf_host, amf_port)

    def connect(self, amf_host, amf_port):
        connect_message = "AmfSocketClient connecting to socket server on %s:%d" % (amf_host, amf_port)
        logging.warn(connect_message)
        connected = False
        timeout = 5
        duration = 0
        while (not connected) and duration < timeout:
            try:
                self.socket.connect(amf_host, amf_port)
                connected = True
            except:
                time.sleep(0.5)
                duration += 0.5
        if connected:
            logging.warn('AmfSocketClient connected to server.')
            self.is_alive = True
            listener = listener_class(self)
            listener.start()
        else:
            logging.critical('AmfSocketClient failed to connect')

    def send(self, message):
        self.sends.append(message)
        amf_data = encode_object(self.encoder, message)
        valid = validate(message, amf_data)
        self.socket.send(amf_data)

    def receive(self):
        r'''As in ActionScript, emulate asynchronous listening.
        If waiting 1/64 or less, for message of a few kB there is decode error.
        I guess there is a variable execution and socket delay.
        Messages from server sent too close together.
        mock packet collision
        too close together:  less than 0.25 / mock_speed
        if next packet arrives too close together, then log error 
            and eat old packet.
        record last arrival time
        >>> from test_network import subprocess_gateway
        >>> gateway_process = subprocess_gateway(file = 'amf_socket_server.py')
        >>> def pass_this(news):
        ...     pass
        >>> client = AmfSocketClient(on_receive = pass_this)
        >>> client.connect('localhost', 5900)
        >>> client.receive()
        >>> time.sleep(0.25)
        >>> client.receive()
        >>> time.sleep(0.25)
        >>> client.receive()
        >>> time.sleep(0.125)
        >>> client.receive() #doctest: +ELLIPSIS
        receive:  ERROR:  packet too soon 0.2...
        >>> time.sleep(0.25)
        >>> client.receive()

        TODO mock client: listening interval:
                if two or more messages in receives:
                    log error and eat all except last message
        '''
        now = time.clock()
        if self.receive_time:
            interval = now - self.receive_time
            if interval < self.minimum_interval:
                print 'receive:  ERROR:  packet too soon', round(interval, 3)
        self.receive_time = now
        ## time.sleep(1.0 / 128)
        ## time.sleep(1.0 / 64)
        ## time.sleep(1.0 / 32)
        time.sleep(1.0 / 16)
        ## time.sleep(1.0 / 2)
        data = self.socket.recv(16384)
        ## data = self.socket.recv(8192)
        ## too small for large_news
        ## data = self.socket.recv(4096)
        if data and 'timeout' != data:
            news = decode_object(data)
            if news:
                if IOError is news:
                    ## import pdb; pdb.set_trace(); 
                    logging.warn('receive: IOError')
                    pass
                else:
                    self.receives.append(news)
                    if self.on_receive:
                        self.on_receive(news)


from threading import Thread
class listener_class(Thread):
    '''listen locks Python interpretter.  
    So listener_class.start starts a thread.
    # >>> listener = listener_class(...)
    # >>> listener.start()
    '''
    def __init__(self, client):
        Thread.__init__(self)
        self.client = client
    def run(self):
        while self.client.is_alive:
            self.client.receive()
        logging.info('listener shutdown')


import code_unit
if __name__ == '__main__':
    from optparse import OptionParser
    parser = OptionParser()
    parser.add_option("--unit", default="",
        dest="unit", help="unit to doctest [default: %default]")
    (options, args) = parser.parse_args()

    if options.unit:
        unit = eval(options.unit)
        code_unit.doctest_unit(unit)

