#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Conveniently host local AMF server from within a client doctest.
'''
__author__ = 'Ethan Kennerly'

import time
import logging

class memo_borg:
    '''Multiple instances share same state.
    http://code.activestate.com/recipes/66531/'''
    __shared_state = {}
    results = {}
    def __init__(self):
        self.__dict__ = self.__shared_state


from decorator import decorator
@decorator
def memorably(function, *args, **kwargs):
    '''Run a function only once.  Thereafter, memoize.
    Useful for calls that are only needed once.
    >>> @memorably
    ... def print_and_return(a):  
    ...     print a
    ...     return a
    >>> print_and_return('a')
    a
    'a'
    >>> print_and_return('a')
    'a'
    >>> print_and_return('b')
    b
    'b'
    >>> print_and_return('a')
    'a'
    >>> print_and_return('b')
    'b'
    '''
    memo = memo_borg()
    kwargs_list = kwargs.items()
    kwargs_tuple = tuple(kwargs_list)
    signature = (function, args, kwargs_tuple)
    logging.debug('signature:  ' + signature.__repr__())
    logging.debug('memo.results:  ' + memo.results.__repr__())
    ## time.sleep(0.5)
    if not signature in memo.results:
        result = function(*args, **kwargs)
        memo.results[signature] = result
    else:
        result = memo.results[signature]
    return result




import subprocess
@memorably
def subprocess_gateway(amf_host = 'localhost', 
        file = 'amf_socket_server.py', verbose = 'error'):
    '''Test simple AMF socket server, without fancy options.
    Waits some seconds until anticipating that server has booted up.'''
    base_command = 'python'
    sub_options = ['--host', amf_host, '--verbose', verbose]
    import os
    path = os.path.join(os.getcwd(), 
            os.path.dirname(__file__), file)
    command = [base_command, path] + sub_options
    logging.debug('subprocess_gateway %s' % command.__repr__())
    try:
        process_identity = subprocess.Popen(command).pid
    except:
        logging.warn('subprocess_gateway %s' % command)
        logging.exception('The system cannot find the file specified?')
        time.sleep(1)
        raise
    # time.sleep(2) # too short?
    # time.sleep(8) # too short?
    # time.sleep(12) # too short?
    time.sleep(16) # too short?
    return process_identity




if __name__ == '__main__':
    print 'Testing...',
    import doctest
    doctest.testmod()
    print 'complete.'

