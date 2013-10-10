'''Simple stream socket that hides my common problems with sockets.'''
__author__ = 'Ethan Kennerly'

import logging
import socket


def create():
    return socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def connect(stream_socket, host, port):
    try:
        stream_socket.connect((host, port))
    except socket.error, e:
        raise Exception("Can't connect: %s" % e[1])


def send(stream_socket, data):
    r'''Send over socket.
    '''
    logging.debug('say: ' + data)
    try:
        # docs.python.org/howto/sockets.html
        total_sent = 0
        while total_sent < len(data):
            sent = stream_socket.send(data)
            if 0 == sent:
                raise RuntimeError, \
                    "socket connection broken"
            total_sent += sent
    except socket.error, e:
        raise Exception("Can't connect: %s" % e[1])


def recv(stream_socket, bytes = 1024):
    # http://bytes.com/topic/python/answers/22953-how-catch-socket-timeout
    data = ''
    try:
        chunk = stream_socket.recv(bytes)
        if '' == chunk:
            error_message = 'RuntimeError socket connection broken'
            logging.error('listen', error_message)
        data += chunk
    except socket.timeout:
        logging.error('listen timeout')
        logging.error('listen %s' % data.__repr__())
        return 'timeout'
    except socket.error:
        import sys
        error_number, error_string = sys.exc_info()[:2]
        error_message = 'socket error %s:  "%s"' \
                    % (error_number, error_string)
        logging.error('listen', error_message)
        return error_message
    return data


class socket_class(socket.socket):
    '''Hides details of socket.
    >>> s = socket_class()
    '''
    def __init__(self):
        self._socket = create()
    def connect(self, host, port):
        connect(self._socket, host, port)
    def send(self, data):
        send(self._socket, data)
    def recv(self, bytes = 1024):
        return recv(self._socket, bytes)


if __name__ == '__main__':
    print 'Testing...',
    import doctest
    doctest.testmod()
    print 'complete.'

