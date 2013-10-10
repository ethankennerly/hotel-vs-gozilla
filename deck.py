#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
Discard and draw from deck in a dictionary.
'''
__author__ = 'Ethan Kennerly'



def discard(dictionary, key, *items_in_list):
    '''
    >>> discard({'a': [1]}, 'a', 1)
    {}
    >>> discard({'a': [1, 2]}, 'a', 1)
    {'a': [2]}
    >>> discard({'a': []}, 'a', *[])
    {}
    >>> discard({'a': []}, 'a')
    {}
    '''
    for item in items_in_list:
        dictionary[key].remove(item)
    if dictionary.has_key(key) and not dictionary.get(key, []):
        dictionary.pop(key)
    return dictionary



def draw(dictionary, key, *items_in_list):
    '''Do not redraw duplicate.
    >>> draw({'a': [1]}, 'a', 0)
    {'a': [1, 0]}
    >>> draw({}, 'a', 1)
    {'a': [1]}
    >>> draw({'a': [1]}, 'a', 1)
    {'a': [1]}

    Do not add key if nothing to add.
    >>> draw({}, 'a', *[])
    {}
    '''
    if items_in_list:
        if not dictionary.has_key(key):
            dictionary[key] = []
    for item in items_in_list:
        if item not in dictionary[key]:
            dictionary[key].append(item)
    return dictionary

import code_unit

if __name__ == '__main__':
    import sys
    code_unit.test_file_args('./smart_go_format.py', sys.argv,
            locals(), globals())

