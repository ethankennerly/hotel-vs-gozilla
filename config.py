#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Auto-generate and default option from configuration file.
Parse configuration file and option value float and int.

Would be nice if...
Comment preceding option populates option help.
'''
__author__ = 'Ethan Kennerly'

import re
def parse_type(string):
    '''return as float, int, or string
    >>> parse_type('-0.5')
    -0.5
    >>> parse_type(' -0.5')
    ' -0.5'
    >>> parse_type('0.0.0')
    '0.0.0'
    >>> parse_type('1.0.0')
    '1.0.0'
    >>> parse_type(0)
    0
    >>> parse_type(1.0)
    1.0
    >>> parse_type('1')
    1
    >>> parse_type('1.0')
    1.0
    >>> parse_type('true')
    True
    >>> parse_type('false')
    False
    '''
    string = str(string)
    float_re = re.compile('^-?\d+\.\d*$')
    if float_re.match(string):
        return float(string)
    int_re = re.compile('^\d+$')
    if int_re.match(string):
        return int(string)
    if 'true' == string:
        return True
    if 'false' == string:
        return False
    return string

from ConfigParser import ConfigParser
from optparse import OptionParser

def get_defaults(config_files):
    configuration = ConfigParser()
    files_found = configuration.read(config_files)
    defaults = configuration.defaults()
    return defaults
    
def default_parser(defaults):
    '''Auto-generate and default option from configuration file.
    >>> config_files = ['internet.cfg', 'localhost.cfg']
    >>> parser = default_parser(get_defaults(config_files))
    >>> if not 2 <= len(parser.option_list):  
    ...     parser.option_list
    '''
    parser = OptionParser()
    for option_name, value_string in defaults.items():
        parser.add_option('--%s' % option_name, default=value_string)
    return parser

def parse_types(options):
    for key, value in options.__dict__.items():
        options.__dict__[key] = parse_type(value)
    return options
    
def parse_args(parser, sys_argv):
    '''
    Parse command line arguments and convert option value float and int.
    '''
    (options, args) = parser.parse_args(args = sys_argv[1:])
    options = parse_types(options)
    return (options, args)

def get_options(config_files, sys_argv):
    '''
    Auto-generate and default option from configuration file.
    Parse command line arguments and convert option value float and int.
    >>> config_files = ['internet.cfg', 'localhost.cfg']
    >>> import sys
    >>> sys.argv = ['client.py', '--simulate_lag', '1.0']
    >>> (options, args) = get_options(config_files, sys.argv)
    >>> options.simulate_lag
    1.0
    >>> options.policy_file
    'socket-policy.xml'
    '''
    defaults = get_defaults(config_files)
    parser = default_parser(defaults)
    return parse_args(parser, sys_argv)

import logging
logging_levels = {'critical': logging.CRITICAL,
              'error': logging.ERROR,
              'warning': logging.WARNING,
              'info': logging.INFO,
              'debug': logging.DEBUG}
def setup_logging(verbose_name = 'warning'):
    '''
    >>> setup_logging()
    '''
    log_level = logging_levels[verbose_name]
    logging.basicConfig(level=log_level)

class borg:
    '''Single reference to data.
    Multiple instances share same state.
    http://code.activestate.com/recipes/66531/'''
    __shared_state = {}
    def __init__(self, default_values_dict):
        '''Set defaults, if not already defined.
        convert numeric strings to numbers.'''
        self.__dict__ = self.__shared_state
        for key, value in default_values_dict.items():
            if not self.__dict__.has_key(key):
                self.__dict__[key] = parse_type(value)
    def set(self, option_values_dict):
        '''Set arbitrary attributes; convert numeric strings to numbers.
        >>> options = borg({'a': '0'})
        >>> options.a
        0
        >>> options.set({'a': 1, 'b': 2})
        >>> options.a
        1
        >>> from pprint import pprint
        >>> pprint(options.__dict__)
        {'a': 1, 'b': 2}
        >>> options = borg({'a': 2, 'c': '3'})
        >>> pprint(options.__dict__)
        {'a': 1, 'b': 2, 'c': 3}
        '''
        for key, value in option_values_dict.items():
            self.__dict__[key] = value


import os
def setup_defaults(config_files = None):
    '''Cascade internet.cfg and localhost.cfg according to operating system.
    >>> defaults = setup_defaults()
    >>> configuration = borg(defaults)
    '''
    if not config_files:
        if 'nt' == os.name:
            config_files = ['internet.cfg', 'localhost.cfg']
        elif 'posix' == os.name:
            config_files = ['localhost.cfg', 'internet.cfg']
    defaults = get_defaults(config_files)
    return defaults

if __name__ == '__main__':
    print __file__, 'starts testing...',
    import doctest
    doctest.testmod()
    print 'complete.'
