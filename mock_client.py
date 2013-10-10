'''
Test and mock a network.
'''
__author__ = 'Ethan Kennerly'

# Test network

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
    >>> def print_and_return_args(*args, **kwargs):  
    ...     print args, kwargs
    ...     return args, kwargs
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
    >>> print_and_return_args(['a'], ['b'])
    (['a'], ['b'],), {}
    (['a'], ['b'],), {}
    >>> print_and_return_args(['a'], ['b'])
    (['a'], ['b'],), {}
    >>> print_and_return_args(['b'], ['b'])
    (['b'], ['b'],), {}
    (['b'], ['b'],), {}
    >>> print_and_return_args(['a'], ['b'])
    (['a'], ['b'],), {}
    >>> print_and_return_args(['a'], ['b'])
    (['a'], ['b'],), {}
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
def subprocess_gateway_file(amf_host = 'localhost', 
        file = 'amf_socket_server.py', 
        verbose = 'error', **kwargs
        ):
    base_command = 'python'
    # TODO:  Would be nice to relay all command-line options and arguments
    sub_options = ['--amf_host', amf_host, '--verbose', verbose]
    for key, value in kwargs:
        flag = '--%s' % key
        if flag not in sub_options:
            sub_options.append(flag)
            sub_options.append(value)
    import os
    path = os.path.join(os.getcwd(), 
            os.path.dirname(__file__), file)
    command = [base_command, path] + sub_options
    logging.debug('subprocess_gateway_file %s' % command.__repr__())
    try:
        process_identity = subprocess.Popen(command).pid
    except:
        logging.warn('subprocess_gateway_file %s' % command)
        logging.exception('The system cannot find the file specified?')
        time.sleep(1)
        raise
    # allow time for server to setup and its subprocesses to setup.
    # time.sleep(4) # too short?
    # time.sleep(8) # too short?
    # time.sleep(12) # too short 2010-09-19
    time.sleep(16) # too short?
    return process_identity


# Mock network

from configuration import *

def get_out_of_bounds(lags, lower_bound = 1.0 / 16, upper_bound = 4.0):
    '''
    >>> get_out_of_bounds([0, 1], 0, 1)

    Floor too low
    >>> get_out_of_bounds([1, 2], 1.00001, 2)
    1

    Floor too high
    >>> get_out_of_bounds([0.5, 1], 0, 1)
    0.5

    Ceiling too high
    >>> get_out_of_bounds([0, 1], 0, 0.9999)
    1

    Ceiling too low
    Thin tail means upper bound is rarely approached.
    >>> get_out_of_bounds([0, 0.125], 0, 1.1)
    0.125
    >>> get_out_of_bounds([0, 0.25], 0, 1.1)
    0.25
    >>> get_out_of_bounds([0, 0.25], 0, 1)
    >>> get_out_of_bounds([0, 0.5], 0, 1)
    >>> get_out_of_bounds([0, 0.5], 0, 0.9)
    '''
    range = upper_bound - lower_bound
    upper_floor = lower_bound + (range * 0.25)
    lower_ceiling = lower_bound + (range * 0.01)
    if upper_bound < max(lags) or max(lags) < upper_floor:
        return max(lags)
    if min(lags) < lower_bound or lower_ceiling < min(lags):
        return min(lags)

import random
def mock_lag(lower_bound = 1.0 / 16, upper_bound = 4.0):
    '''Randomly generate seconds of network lag.
    >>> lags = [mock_lag() for i in range(1000)]
    >>> get_out_of_bounds(lags)
    >>> lags = [mock_lag() for i in range(1000)]
    >>> get_out_of_bounds(lags)
    >>> lags = [mock_lag() for i in range(1000)]
    >>> get_out_of_bounds(lags)

    Speed up for tests.
    >>> mock_speed = 16
    >>> lo, hi = 0.5 / mock_speed, 1.0 / mock_speed
    >>> lags = [mock_lag(lo, hi) for i in range(1000)]
    >>> out = get_out_of_bounds(lags, lo, hi)
    >>> if out:
    ...     lo, out, hi

    Other values.  Thin tail means upper bound is rarely approached.
    >>> lags = [mock_lag(1.0, 2.0) for i in range(1000)]
    >>> get_out_of_bounds(lags, 1.0, 2.0)
    '''
    lag = random.paretovariate(14) - 1
    range = upper_bound - lower_bound
    unfiltered = lag * range + lower_bound
    high_pass = max(lower_bound, unfiltered)
    bounded = min(upper_bound, high_pass)
    return bounded

class internet_borg:
    '''Multiple instances share same state.
    http://code.activestate.com/recipes/66531/'''
    __shared_state = {}
    servers = {}
    def __init__(self):
        self.__dict__ = self.__shared_state



class echo_protocol_class(object):
    '''Return what was sent.
    >>> echo_protocol = echo_protocol_class()
    >>> echo_protocol.send({'a': 1})
    {'a': 1}
    >>> echo_protocol.sends
    [{'a': 1}]

    #>>> echo_protocol.receive({'b': 2})
    #>>> echo_protocol.receives
    #[{'b': 2}]
    '''
    is_alive = False
    def __init__(self):
        self.sends = []
    #    self.receives = []
    def send(self, message):
        self.sends.append(message)
        return message
    #def receive(self, message):
    #    self.receives.append(message)

class print_protocol_class(object):
    '''Print and return what was sent.
    >>> print_protocol = print_protocol_class()
    >>> result = print_protocol.send({'a': 1})
    {'a': 1}
    >>> result
    {'a': 1}
    >>> print_protocol.sends
    [{'a': 1}]
    '''
    is_alive = False
    def __init__(self):
        self.sends = []
    def send(self, message):
        self.sends.append(message)
        print message.__repr__()
        return message


class mock_protocol_class(echo_protocol_class):
    '''
    >>> m = mock_protocol_class(None)

    #>>> m.receives
    #[]
    '''
    def __init__(self, mock_client):
        echo_protocol_class.__init__(self)
        self.mock_client = mock_client
        #- self.is_alive = True
    def send(self, message):
        self.mock_client.socket.append(message)

class mock_client_class(object):
    def __init__(self, amf_host, amf_port, on_receive = None, mock_speed = 1, 
            simulate_lag = 0):
        self.internet = internet_borg()
        self.socket = []
        self.sends = []
        self.receives = []
        self.is_alive = True
        self.on_receive = on_receive
        self.server = self.internet.servers[amf_host][amf_port]
        self.protocol = mock_protocol_class(self)
        self.mock_speed = mock_speed
        self.simulate_lag = simulate_lag
        self.setup()
    def send(self, message):
        self.sends.append(message)
        response = self.server.receive(self.protocol, message)
        ##- response = self.go_club.receive(self, message)
        self.socket.append(response)
    def receive(self):
        '''HACK migrated mock lag to server instead of modifying flash client.
        Does lag on server interfere with messages?
        Lag on client enables tests of lag-situations without a network.'''
        lag = mock_lag(self.simulate_lag, 4 * self.simulate_lag)
        time.sleep(lag / self.mock_speed)
        while self.socket:
            news = self.socket.pop(0)
            if news:
                self.receives.append(news)
            if news and self.on_receive:
                self.on_receive(news)
            return news
    def setup(self):
        from amf_socket_client import listener_class
        min_lag = self.simulate_lag / self.mock_speed
        logging.debug('mock_client.setup: min_lag = %s' % min_lag)
        listener = listener_class(self)
        listener.start()


def mock_setup_client(globe):
    from client import configuration
    globe.ambassador = mock_client_class(configuration.amf_host, 
            configuration.amf_port, globe.push_news, 
            mock_speed = configuration.mock_speed, 
            simulate_lag = configuration.simulate_lag)
    return globe.ambassador



if __name__ == '__main__':
    print 'Testing...',
    import doctest
    doctest.testmod()
    print 'complete.'

