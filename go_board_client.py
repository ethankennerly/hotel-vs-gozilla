#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
Adapted from example text socket using Twisted.

@see: U{Wiki page for this example<http://pyamf.org/wiki/BinarySocket>}

@since: 0.1

Edited for go board by Ethan Kennerly   http://finegamedesign.com
'''
__author__ = 'Ethan Kennerly'
# Socket networking and PyAMF encoding

import socket
import pyamf
from pyamf import remoting
from go_board_configuration import *



class AmfSocketClient(object):
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, 
                socket.SOCK_STREAM)
        self.sends = []
        self.receives = []

    def connect(self, host, port):
        connect_message = "AmfSocketClient connecting to socket server on %s:%d" % (host, port)
        logging.warn(connect_message)
        try:
            self.sock.connect((host, port))
            logging.debug('AmfSocketClient connected to server.')
        except socket.error, e:
            raise Exception("Can't connect: %s" % e[1])

    def send(self, message):
        self.sends.append(message)
        # tell server we started listening
        logging.debug('send:  request: %s' % message.__repr__())
        encoder = pyamf.get_encoder(object_encoding)
        encoder.writeElement(message)
        message = encoder.stream.getvalue()
        encoder.stream.truncate()
        logging.debug('send:  encoded request: %s' % message.__repr__())
        send_log = encoder.stream.tell().__repr__() \
                + encoder.stream.__repr__()
        logging.debug('send; ' + send_log)
        decoder = pyamf.get_decoder(object_encoding, message)
        #if not isinstance(stream, util.BufferedByteStream):
        #    stream = util.BufferedByteStream(stream)
        logging.debug('send: ' 
                + decoder.stream.tell().__repr__() 
                + decoder.stream.__repr__())
        data = decoder.readElement()
        logging.debug('send:  decoded %s' % data.__repr__())
        try:
            #total_sent = 0
            #while total_sent < len(message):
                sent = self.sock.send(message)
                if sent == 0:
                    raise RuntimeError, \
                        "socket connection broken"
            #    total_sent += sent
        except socket.error, e:
            raise Exception("Can't connect: %s" % e[1])


def say(envoy, message):
    r'''Send and receive over socket.
    '''
    logging.debug('send', message)
    # docs.python.org/howto/sockets.html
    message_length = len(gtp_string)
    total_sent = 0
    while total_sent < message_length:
        sent = envoy.send(gtp_string[total_sent:])
        if 0 == sent:
            print 'RuntimeError socket connection broken'
        total_sent += sent


def listen(envoy):
    response = ''
    # http://bytes.com/topic/python/answers/22953-how-catch-socket-timeout
    try:
        chunk = envoy.recv(1024)
        if '' == chunk:
            error_message = 'RuntimeError socket connection broken'
            logging.error('listen', error_message)
        response += chunk
    except socket.timeout:
        logging.error('listen timeout')
        logging.error('listen %s' % response.__repr__())
        return 'timeout'
    except socket.error:
        import sys
        error_number, error_string = sys.exc_info()[:2]
        error_message = 'socket error %i:  "%s"' \
                    % (error_number, error_string)
        logging.error('listen', error_message)
        return error_message
    decoder = pyamf.get_decoder(object_encoding, response)
    #if not isinstance(stream, util.BufferedByteStream):
    #    stream = util.BufferedByteStream(stream)
    logging.debug('listen: response: ' + response.__repr__())
    logging.debug('listen: stream: ' + decoder.stream.__repr__())
    data = decoder.readElement()
    logging.debug('listen decoded %s' % data.__repr__())
    return data


def listen_continuously(envoy, globe, receives,
        listen = listen, delay = lambda: 1.0 / 256):
    # If waiting 1/128 or less, sometimes the message is truncated.
    # I guess there is a variable execution and socket delay.
    while True:
        time.sleep(delay())
        news = listen(envoy)
        if news:
            receives.append(news)
        if globe and globe.root:
            root = imitate_news(news, globe.root)
            if 'exit' == globe.root.gateway_mc.currentLabel:
                logging.info('exit == root.gateway_mc.currentLabel')
                break
        else:
            break


from threading import Thread
class listener_class(Thread):
    '''listen locks Python interpretter.  
    So listener_class.start starts a thread.
    # >>> listener = listener_class(...)
    # >>> listener.start()
    '''
    def __init__(self, envoy, globe, receives, listen = listen, 
            delay = lambda: 1.0 / 256):
        Thread.__init__(self)
        self.envoy = envoy
        self.globe = globe
        self.receives = receives
        self.listen = listen
        self.delay = delay
    def run(self):
        listen_continuously(self.envoy, self.globe,
                self.receives, self.listen, self.delay)
        logging.info('listener shutdown')





import subprocess
@memorably
def _subprocess_gateway(amf_host):
    base_command = 'python'
    base_file = 'embassy.py'
    sub_options = ['--host', options.host, '--verbose', options.verbose]
    import os
    path = os.path.join(os.getcwd(), 
            os.path.dirname(__file__),
            base_file)
    command = [base_command, path] + sub_options
    logging.debug('subprocess_gateway %s' % command.__repr__())
    try:
        process_identity = subprocess.Popen(command).pid
    except:
        logging.warn('subprocess_gateway %s' % command)
        logging.exception('The system cannot find the file specified?')
        time.sleep(1)
        raise
    time.sleep(1)
    return process_identity

def _setup_client(globe):
    client = AmfSocketClient()
    client.connect(amf_host, amf_port)
    listener = listener_class(client.sock, globe, client.receives)
    listener.start()
    globe.ambassador = client
    return client

# Mock network

def sleep(seconds, speed = 1):
    '''Sleep quickly, for mocking time.
    >>> sleep(5, 256)
    '''
    real_time = seconds / float(speed) 
    ## print 'sleep real_time', real_time
    time.sleep(real_time)


@memorably
def mock_gateway(amf_host = None):
    from embassy import go_club_class
    go_club = go_club_class(mock_speed)
    return go_club

import random
def mock_lag(speed = 1):
    '''Randomly generate seconds of network lag.
    >>> lags = [mock_lag() for i in range(1000)]
    >>> if 1 < max(lags):
    ...     max(lags)
    >>> if min(lags) < (1.0 / 64):
    ...     min(lags)

    Speed up for tests.
    >>> speed = 16
    >>> lags = [mock_lag(speed) for i in range(1000)]
    >>> if 1.0 / speed < max(lags):
    ...     max(lags)
    >>> if min(lags) < (1.0 / 64 / speed):
    ...     min(lags)
    '''
    ## logging.debug('mock_lag(%s)' % speed)
    lag = random.paretovariate(20) - 1 + (1.0 / 64)
    return lag / float(speed)

class mock_client_class(object):
    def __init__(self):
        from embassy import go_club_class
        self.go_club = go_club_class(mock_speed)
        self.envoy = []
        self.sends = []
        self.receives = []
    def send(self, message):
        self.sends.append(message)
        response = self.go_club.receive(message)
        self.envoy.append(response)

def laggily_listen(envoy):
    ## lag = mock_lag()
    ## sleep(lag, globe._speed)
    if envoy:
        message = envoy.pop(0)
        return message

def mock_setup_client(globe):
    ## globe._speed = mock_speed
    client = mock_client_class()
    logging.debug('mock_setup_client: globe._speed = %s' % globe._speed)
    listener = listener_class(client.envoy, globe, client.receives,
            listen = laggily_listen, 
            delay = lambda: mock_lag(globe._speed))
    listener.start()
    globe.ambassador = client
    return client

# End networking




import code_unit

# for doctest, which does not enter __main__, mock by default
subprocess_gateway = mock_gateway
setup_client = mock_setup_client
mock_speed = 16

if __name__ == '__main__':
    # Late import, in case this project becomes a library, 
    # never to be run as main again.
    from optparse import OptionParser

    # Populate our options, -h/--help is already there for you.
    parser = OptionParser()
    parser.add_option("-p", "--port", default=amf_port,
        dest="port", help="port number [default: %default]")
    parser.add_option("--host", default=amf_host,
        dest="host", help="host address [default: %default]")
    parser.add_option("--unit", default="",
        dest="unit", help="unit to doctest [default: %default]")
    parser.add_option('-v', '--verbose', dest='verbose', default='warning',
                    help="Increase verbosity")
    parser.add_option("--wait", default="0",
        dest="wait", help="wait afterwards to copy results before shell exits [default: %default]")
    parser.add_option("--mock", default="",
        dest="mock", help="mock networking gateway tests locally and quickly, with PDB trace and exception traceback.  argument is speed of mock network (1 == real-time). [default: %default]")
    # Here would be a good place to check what came in on the command line and
    # call optp.error("Useful message") to exit if all it not well.
    (options, args) = parser.parse_args()

    log_level = logging_levels[options.verbose]

    # Set up basic configuration, out to stderr with a reasonable default format.
    logging.basicConfig(level=log_level)
    

    amf_host = options.host
    amf_port = int(options.port)

    if options.mock:
        subprocess_gateway = mock_gateway
        setup_client = mock_setup_client
        mock_speed = int(options.mock)
    else:
        subprocess_gateway = _subprocess_gateway
        setup_client = _setup_client
        mock_speed = 1
    # Inspect examples
    if options.unit:
        unit = eval(options.unit)
        code_unit.doctest_unit(unit)
    else:
        gateway_process = subprocess_gateway(amf_host)
        units = globals().values()
        code_unit.doctest_units(units)

    if options.wait:
        code_unit.wait(options.wait)

