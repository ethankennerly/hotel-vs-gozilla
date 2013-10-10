#!/usr/bin/python
# -*- coding: utf-8 -*-


'''Simple broadcast of position of stones on board.'''
__author__ = 'Ethan Kennerly'

def finish_move(message):
    '''Transition from getting to get, and putting to put.
    >>> getting = {'black1': {'y': 83, 'x': 684, 'currentLabel': u'getting'}}
    >>> get = finish_move(getting)
    >>> if not get['black1']['currentLabel'] == 'get':
    ...     get
    >>> putting = {'white40': {'y': 121, 'x': 406, 'currentLabel': u'putting'}}
    >>> put = finish_move(putting)
    >>> if not put['white40']['currentLabel'] == 'put':
    ...     put
    '''
    for name, property in message.items():
        label = property.get('currentLabel')
        news = message
        if 'getting' == label:
            news[name]['currentLabel'] = 'get'
        elif 'putting' == label:
            news[name]['currentLabel'] = 'put'
    return news


# Twisted networking and PyAMF encoding

import amf_socket_server
from go_board_configuration import *


class go_board_protocol_class(amf_socket_server.AmfSocketProtocol):
    def on_receive(self, message):
        news = finish_move(message)
        self.broadcast(news)


class go_board_factory_class(amf_socket_server.AmfSocketFactory):
    protocol = go_board_protocol_class


def test(options):
    import doctest
    logging.warn('go_board_server starts doctests.')
    doctest.testmod()
    logging.warn('go_board_server finished doctests.')
    logging.warn('waiting %s' % options.test)
    import time
    time.sleep(float(options.test))


def run_server(options):
    go_board_factory = go_board_factory_class(
        options.amf_host, options.amf_port, 
        options.policy_file, options.policy_port)
    reactor = go_board_factory.setup()
    reactor.run()  # Infinite loop blocks execution


if __name__ == '__main__':
    from optparse import OptionParser

    parser = OptionParser()
    parser.add_option("--host", default=amf_host,
        dest="amf_host", help="host address [default: %default]")
    parser.add_option("-a", "--app-port", default=amf_port,
        dest="amf_port", help="Application port number [default: %default]")
    parser.add_option("-p", "--policy-port", default=policy_port,
        dest="policy_port", help="Socket policy port number [default: %default]")
    parser.add_option("-f", "--policy-file", default=policy_file,
        dest="policy_file", help="Location of socket policy file [default: %default]")
    parser.add_option("--test", 
        help="run all doctests, then wait afterwards to copy results before shell exits [default: %default]")
    parser.add_option('-v', '--verbose', dest='verbose', default='warning',
                    help="Increase verbosity")
    (options, args) = parser.parse_args()

    log_level = logging_levels[options.verbose]

    # Print to stderr
    logging.basicConfig(level=log_level)

    if options.test:
        test(options)
    else:
        run_server(options)


