#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
Control Flash client or mock client.
'''
__author__ = 'Ethan Kennerly'

from user_as import *

def master_publish(globe, news):
    master = globe.root.title_mc.master_txt.text
    slave = globe.root.title_mc.slave_txt.text
    master_news = {
            'title_mc': {
                'master_txt': {'text': master},
                'slave_txt': {'text': slave}
            }
        }
    news = upgrade(news, master_news)
    globe.ambassador.send(news)

class master_class(globe_class):
    #def create(globe, mock_speed = 1):
    #    '''Set callback to publish to slave.
    #    >>> yuji = master_class()
    #    >>> yuji.create(1)
    #    >>> if not yuji.root._on_set:  False
    #    '''
    #    globe_class.create(globe, mock_speed)
    #    #def publish_my_property(owner, name, value): 
    #    #    publish_property(globe, owner, name, value)
    #    #globe.root._on_set = publish_my_property
    def publish_property(globe, owner, name, value): 
        publish_property(globe, owner, name, value)
    def publish(globe, news):
        master_publish(globe, news)
    def imitate(globe, news):
        '''Turn off _on_set then set stage.  
        >>> yuji = master_class()
        >>> yuji.create(1)
        >>> yuji.setup_events()
        >>> from mock_client import echo_protocol_class
        >>> yuji.ambassador = echo_protocol_class()
        >>> yuji.root._on_set = yuji.publish_property
        >>> yuji.ambassador.sends
        []
        >>> yuji.root.gotoAndPlay('table')
        >>> yuji.ambassador.sends[-1].get('currentLabel')
        'table'
        >>> yuji.root.currentLabel
        'table'
        >>> yuji.imitate({'currentLabel': 'lobby'})
        >>> yuji.ambassador.sends[-1].get('currentLabel')
        'table'
        >>> yuji.root.currentLabel
        'lobby'
        >>> yuji.root.gotoAndPlay('login')
        >>> yuji.ambassador.sends[-1].get('currentLabel')
        'login'
        >>> yuji.root.currentLabel
        'login'
        '''
        enabled = globe.root._on_set
        globe.root._on_set = None
        globe_class.imitate(globe, news)
        globe.root._on_set = enabled
        
def slave_set_property(globe, owner, name, value): 
    news = note(owner, name, value)
    master_publish(globe, news)
    
def slave_dispatch_event(globe, owner, event_type): 
    news = note(owner, 'dispatchEvent', event_type)
    master_publish(globe, news)


import time

def slave_mouse_down_and_sleep(globe, target, second):
    slave_dispatch_event(globe, target, MouseEvent.MOUSE_DOWN)
    time.sleep(second)


def slave_echo_once(globe, intersection_mc, second):
    news = {
        intersection_mc.name: {
            'currentLabel': 'preview_black'},
        'gateway_mc': {
            'ready_time_txt': {
                'text': 'echo_once'}
        }
    }
    master_publish(globe, news)
    time.sleep(second)

def slave_copy(globe, intersection_mc, second):
    '''Small news.  See echo
    '''
    news = {
        intersection_mc.name: {
            'currentLabel': 'preview_black'},
        'gateway_mc': {
            'ready_time_txt': {
                'text': 'copy'}
        }
    }
    master_publish(globe, news)
    time.sleep(second)

import copy

def mouse_down_and_news(globe, intersection_mc, second):
    large_news = load('lifeanddeath.large_news.py')
    news = copy.deepcopy(large_news)
    news[intersection_mc.name] = {'currentLabel': 'preview_black'}
    #event = note(intersection_mc, 'dispatchEvent', MouseEvent.MOUSE_DOWN)
    #news = upgrade(news, event)
    globe.publish(news)
    time.sleep(second)

def slave_mouse_down_and_news(globe, intersection_mc, second):
    '''Large news.  See echo
    '''
    large_news = load('lifeanddeath.large_news.py')
    news = copy.deepcopy(large_news)
    # news[intersection_mc.name] = {'currentLabel': 'preview_black'}
    event = note(intersection_mc, 'dispatchEvent', MouseEvent.MOUSE_DOWN)
    news = upgrade(news, event)
    master_publish(globe, news)
    time.sleep(second)

def slave_copy_large_news(globe, intersection_mc, second):
    '''Large news.  See echo
    '''
    large_news = load('lifeanddeath.large_news.py')
    news = {
        intersection_mc.name: {
            'currentLabel': 'preview_black'},
        'gateway_mc': {
            'ready_time_txt': {
                'text': 'copy'}
        }
    }
    news = upgrade(large_news, news)
    master_publish(globe, news)
    time.sleep(second)


def slave_log_large_news(globe, intersection_mc, second):
    '''Log the news.  See echo
    '''
    large_news = load('lifeanddeath.large_news.py')
    news = {
        intersection_mc.name: {
            'currentLabel': 'preview_black'},
        'gateway_mc': {
            'ready_time_txt': {
                'text': 'log'}
        }
    }
    news = upgrade(large_news, news)
    master_publish(globe, news)
    time.sleep(second)


class slave_counter_borg:
    '''Multiple instances share same state.
    http://code.activestate.com/recipes/66531/'''
    __shared_state = {}
    slave_count = 0
    master_count = 0
    def __init__(self):
        self.__dict__ = self.__shared_state


import amf_socket_client

def _setup_master(globe):
    '''Setup 1 slave then 1 master.'''
    globe.ambassador = amf_socket_client.AmfSocketClient(globe.imitate)
    # globe.ambassador = amf_socket_client.AmfSocketClient(globe.news_list.append)
    globe.ambassador.connect(configuration.amf_host, configuration.amf_port)
    slave_counter = slave_counter_borg()
    globe.root.title_mc.slave_txt.text = str(slave_counter.slave_count 
            + slave_counter.master_count)
    slave_counter.slave_count += 1
    globe.root.title_mc.master_txt.text = str(slave_counter.master_count
            + slave_counter.slave_count)
    slave_counter.master_count += 1
    # publish
    globe.root._on_set = globe.publish_property
    time.sleep(2) # too short with 4.0 lag?
    # time.sleep(6) # ok?
    return globe.ambassador

def setup_master(globe):
    '''Setup 1 client then 1 master (0:1, 2:3).'''
    slave = globe_class()
    slave.setup(configuration.mock_speed, setup_amf_client)
    return _setup_master(globe)

import subprocess
def setup_flash_client():
    '''
    C:\project\lifeanddeath>lifeanddeath.swf
    '''
    import os
    path = os.path.abspath(configuration.client_bat)
    pid = subprocess.Popen([path]).pid
    #- time.sleep(0) # name/password not loaded
    #- time.sleep(1) # ? name/password not loaded
    #- time.sleep(2) # ethan does not load name/password
    # time.sleep(3) # ok?
    # time.sleep(4) # ok
    time.sleep(6) # ok? # too short with simulate_lag 4.0?
    # time.sleep(8) # ok
    # time.sleep(12) # ok?
    return pid


def setup_flash_master(globe):
    '''Setup 1 Flash client then 1 master (0:1, 2:3).'''
    setup_flash_client()
    return _setup_master(globe)
    #globe.ambassador = amf_socket_client.AmfSocketClient(globe.imitate)
    #globe.ambassador.connect(configuration.amf_host, configuration.amf_port)
    #time.sleep(1)
    #slave_counter = slave_counter_borg()
    #globe.root.title_mc.slave_txt.text = str(slave_counter.slave_count 
    #        + slave_counter.master_count)
    #slave_counter.slave_count += 1
    #globe.root.title_mc.master_txt.text = str(slave_counter.master_count
    #        + slave_counter.slave_count)
    #slave_counter.master_count += 1
    #return globe.ambassador


from smart_go_format import sgf_to_history
# from client import mouse_down_and_sleep
from intersection_mc import get_intersection_name
from client import *



def find_in_receives_sequence(receives, parent_label, child_label):
    '''Find the child in the index of the sequence 
    from the list of news received.
    >>> receives = [{}]
    >>> pprint(find_in_receives_sequence(receives, 'a', 'b'))
    []
    >>> pprint(find_in_receives_sequence([{'a': {'b': 'c'}}], 'a', 'b'))
    []
    >>> pprint(find_in_receives_sequence([{'sequence': [{'a': {'b': 'c'}}]}], 'a', 'b'))
    [(0, None, 'c', ['sequence'])]
    '''
    found = []
    for i, r in enumerate(receives):
        sequence = r.get('sequence')
        if sequence:
            for s in sequence:
                if s.get(parent_label):
                    child = s[parent_label].get(child_label)
                    if child:
                        found.append( (i, s.get('time_txt'), child, r.keys()) )
    return found


def reenact_example(history, white_name, black_name, wait):
    '''Set size, play black and white.  Nothing else supported.
    Does not work???
    >>> # from super_users import setup_users_white_black
    >>> # users, white, black = setup_users_white_black('ethan', 'joris')
    >>> mouse_down_and_sleep = slave_mouse_down_and_sleep
    >>> from client import *
    >>> code_unit.inline_examples(
    ...     ethan_joris_start_example.__doc__, 
    ...     locals(), globals(), 
    ...     verify_examples = False)
    >>> history = sgf_to_history('sgf/beginner/count_5_5.sgf')
    >>> example_text = reenact_example(history, 'ethan', 'joris', 4.0)
    '''
    example_text = '>>> white, black = %s, %s' % (white_name, black_name)
    example_text += '\n>>> wait = %s' % wait
    for event in history:
        if event.has_key('size'):
            size = event['size']
            size_name = get_intersection_name(size, size)
            example_text += '\n>>> mouse_down_and_sleep(black, black.root.game_over_mc.%s.enter_mc, wait / black._speed)' % size_name
        if event.has_key('black'):
            row, column = event['black']
            intersection_name = get_intersection_name(row, column)
            example_text += '\n>>> mouse_down_and_sleep(black, black.root.%s, wait / black._speed)' % intersection_name
            example_text += '\n>>> mouse_down_and_sleep(black, black.root.%s, wait / black._speed)' % intersection_name
        if event.has_key('white'):
            row, column = event['white']
            intersection_name = get_intersection_name(row, column)
            example_text += '\n>>> mouse_down_and_sleep(white, white.root.%s, wait / white._speed)' % intersection_name
    return example_text


def get_news(news):
    return news

def get_address(globe, intersection_mc):
    return '%s.%s' % (globe.root.title_mc.username_txt.text, \
            address(intersection_mc))
    
def print_address(globe, intersection_mc, wait):
    '''Mock mouse_down_and_wait
    >>> andre = configuration.globe_class()
    >>> andre.root
    >>> andre.create(16)
    >>> print_address(andre, andre.root._0_0_mc.territory_mc, 1.0)
    ethan.root._0_0_mc.territory_mc
    >>> andre.root.title_mc.username_txt.text = 'andre'
    >>> print_address(andre, andre.root._0_0_mc.territory_mc, 1.0)
    andre.root._0_0_mc.territory_mc
    '''
    print get_address(globe, intersection_mc)

def get_address_and_sleep(globe, intersection_mc, wait):
    address = get_address(globe, intersection_mc)
    time.sleep(wait)
    return address
    
class time_since_class(object):
    '''Time since last time called.
    >>> timer = time_since_class()
    >>> timer.since()
    0.0
    >>> time.sleep(0.125)
    >>> code_unit.round2(timer.since(), 5)
    0.125
    >>> code_unit.round2(timer.since(), 5)
    0.0
    >>> time.sleep(0.125)

    Reset.
    >>> timer.then = None
    >>> timer.since()
    0.0
    '''
    def __init__(self):
        self.then = None
    def since(self):
        if self.then is None:
            self.then = time.time()
        now = time.time()
        since = now - self.then
        self.then = now
        return since

class since_function_class(object):
    '''List approximate time before a function was called.
    >>> def dream(nap_time):
    ...     time.sleep(nap_time)
    ...     return 'dream'
    ...     
    >>> since_function = since_function_class()
    >>> since_dream = since_function.wrap(dream)
    >>> since_dream(0.13); since_dream(0);
    >>> since_function.dreams
    [(0.0, 'dream'), (0.125, 'dream')]
    '''
    def __init__(self):
        self.timer = time_since_class() 
        self.dreams = []
        self.precision = 4
    def wrap(self, function, *args, **kwargs):
        def wrapper(*args, **kwargs):
            sleep = self.timer.since()
            rounded_sleep = code_unit.round2(sleep, self.precision)
            dream = function(*args, **kwargs)
            self.dreams.append( (rounded_sleep, dream) )
        return wrapper


def play_history(history, white, black, mouse_down_and_sleep, wait):
    r'''Set size, play black and white; convert comment and publish news.
    Nothing else supported.
    >>> from super_users import setup_users_white_black
    >>> users, ethan, lukasz = setup_users_white_black('ethan', 'lukasz')
    >>> white_computer_history = sgf_to_history('sgf/beginner/count_5_5_play_black_1.sgf')
    >>> from pprint import pprint
    >>> pprint(white_computer_history[-1].get('news'))
    {'game_over_mc': {'white_computer_mc': {'enter_mc': {'dispatchEvent': 'mouseDown'}}}}
    >>> play_history(white_computer_history, ethan, lukasz, print_address, 0.0625)
    lukasz.root.game_over_mc._5_5_mc.enter_mc
    lukasz.root._1_1_mc
    lukasz.root._1_1_mc
    ethan.root._3_3_mc
    lukasz.root._1_3_mc
    lukasz.root._1_3_mc
    ethan.root._3_1_mc
    lukasz.root._1_2_mc
    lukasz.root._1_2_mc
    ethan.root._3_2_mc
    lukasz.root._1_0_mc
    lukasz.root._1_0_mc
    ethan.root._3_0_mc
    lukasz.root._2_3_mc
    lukasz.root._2_3_mc
    ethan.root._3_4_mc
    >>> lukasz.root.game_over_mc.white_computer_mc.enter_mc.currentLabel
    'enter'
    >>> ethan.root.game_over_mc.white_computer_mc.enter_mc.currentLabel
    u'none'

    >>> comment_in_history = [{'comment': 'LUKASZ:  RED/BLUE GLASSES SHOW WHICH CAKE YOU ARE TAKING', 'news': {'territory_mc': {'currentLabel': 'show'}}, 'size': 5}, {'black': (2, 2)}, {'white': (2, 3)}]
    >>> play_history(comment_in_history, ethan, lukasz, print_address, 0.0625)
    lukasz.root.game_over_mc._5_5_mc.enter_mc
    lukasz.root._2_2_mc
    lukasz.root._2_2_mc
    ethan.root._2_3_mc
    >>> lukasz.root.comment_mc.currentLabel 
    'comment'
    >>> lukasz.root.comment_mc._txt.text
    'LUKASZ:  RED/BLUE GLASSES SHOW WHICH CAKE YOU ARE TAKING'

    Time between calls.
    >>> since = since_function_class()
    >>> since_address_and_sleep = since.wrap(get_address_and_sleep)
    >>> since_news = since.wrap(get_news)
    >>> lukasz.publish = since_news
    >>> since.timer.then = None
    >>> comment_in_event = [{'black': (2, 2)}, {'white': (2, 3), 'comment': '?'}, {'black': (3, 3)}]
    >>> play_history(comment_in_event, ethan, lukasz, since_address_and_sleep, 0.0625)
    >>> from pprint import pprint
    >>> pprint(since.dreams)
    [(0.0, 'lukasz.root._2_2_mc'),
     (0.0625, 'lukasz.root._2_2_mc'),
     (0.0625, 'ethan.root._2_3_mc'),
     (0.0625, {'comment_mc': {'_txt': {'text': '?'}, 'currentLabel': 'comment'}}),
     (0.0625, 'lukasz.root._3_3_mc'),
     (0.0625, 'lukasz.root._3_3_mc')]
    '''
    for event in history:
        news = {}
        if event.has_key('size'):
            size = event['size']
            size_name = get_intersection_name(size, size)
            mouse_down_and_sleep(black, black.root.game_over_mc[size_name].enter_mc, 
                    wait / black._speed)
        if event.has_key('black'):
            row, column = event['black']
            intersection_name = get_intersection_name(row, column)
            mouse_down_and_sleep(black, black.root[intersection_name], 
                    wait / black._speed)
            mouse_down_and_sleep(black, black.root[intersection_name], 
                    wait / black._speed)
        if event.has_key('white'):
            row, column = event['white']
            intersection_name = get_intersection_name(row, column)
            mouse_down_and_sleep(white, white.root[intersection_name], 
                    wait / white._speed)
        if event.has_key('news'):
            news = upgrade(news, event['news'])
        if event.has_key('comment'):
            comment = event['comment']
            comment_news = {
                'comment_mc': {
                    'currentLabel': 'comment',
                    '_txt': {
                        'text': comment
                    }
                }
            }
            news = upgrade(news, comment_news)
        if news:
            black.publish(news)
            time.sleep(wait / black._speed)
            #intersection_name = get_intersection_name(row, column)
            #mouse_down_and_sleep(white, white.root[intersection_name], 
            #        wait / white._speed)
    

def exit_make_and_start(ethan, joris, mouse_down_and_sleep):
    '''Exit the table, make a new table, join the table and start playing.
    >>> code_unit.inline_examples(
    ...     ethan_joris_start_example.__doc__, 
    ...     locals(), globals(), 
    ...     verify_examples = False)
    >>> exit_make_and_start(ethan, joris, mouse_down_and_sleep)
    >>> property_diff(joris, joris.root, 'currentLabel', 'table')
    '''
    mouse_down_and_sleep(joris, joris.root.lobby_mc.enter_mc, 
            1.0 / joris._speed)
    while 'lobby' != ethan.root.currentLabel:
        time.sleep(0.125 / ethan._speed)
    mouse_down_and_sleep(ethan, ethan.root.lobby_mc.create_mc, 
            1.0 / ethan._speed)
    while 'ethan' != joris.root.lobby_mc.join_mc.join_txt.text:
        time.sleep(0.125 / joris._speed)
    mouse_down_and_sleep(joris, joris.root.lobby_mc.join_mc.enter_btn, 
            1.0 / joris._speed)
    while 'ethan' != joris.root.turn_mc.white_user_txt.text:
        time.sleep(0.125 / joris._speed)
    mouse_down_and_sleep(joris, joris.root.game_over_mc.start_mc, 
            1.0 / joris._speed)
    

def exit_and_play_sgf(sgf_file, ethan, joris, mouse_down_and_sleep, wait):
    '''
    >>> code_unit.inline_examples(
    ...     ethan_joris_start_example.__doc__, 
    ...     locals(), globals(), 
    ...     verify_examples = False)
    >>> exit_and_play_sgf('sgf/beginner/count_5_5.sgf', ethan, joris, mouse_down_and_sleep, 1.0)
    >>> property_diff(joris, joris.root, 'currentLabel', '_5_5')
    >>> exit_and_play_sgf('sgf/beginner/count_5_5_white_1.sgf', ethan, joris, mouse_down_and_sleep, 1.0)
    >>> property_diff(joris, joris.root, 'currentLabel', '_5_5')
    '''
    exit_make_and_start(ethan, joris, mouse_down_and_sleep)
    history = sgf_to_history(sgf_file)
    play_history(history, ethan, joris, mouse_down_and_sleep, wait)


def play_sgf(sgf_file, ethan, lukasz, mouse_down_and_sleep, wait):
    history = sgf_to_history(sgf_file)
    play_history(history, ethan, lukasz, mouse_down_and_sleep, wait)




def territory_mark_example():
    '''After play SGF, black, white, and neutral territory is marked.
    >>> code_unit.inline_examples(
    ...     ethan_joris_start_example.__doc__, 
    ...     locals(), globals(), 
    ...     verify_examples = False)
    >>> exit_and_play_sgf('sgf/beginner/count_5_5_even_neutral.sgf', ethan, joris, mouse_down_and_sleep, 1.0)
    >>> joris.pb()
    ,X,,,
    ,XXXX
    XX,OO
    OOOO,
    ,,,O,
    >>> ethan.pb()
    ,X,,,
    ,XXXX
    XX,OO
    OOOO,
    ,,,O,
    >>> property_diff(joris, joris.root._2_2_mc.territory_mc, 'currentLabel', 
    ...     'neutral')
    >>> property_diff(joris, joris.root._0_2_mc.territory_mc, 'currentLabel', 
    ...     'black')
    >>> property_diff(joris, joris.root._4_2_mc.territory_mc, 'currentLabel', 
    ...     'white')
    '''


def before_remote_control_example():
    '''If no master, slave does not match master.  If master, match the master.
    setup slave
    >>> gateway_process = configuration.subprocess_gateway(configuration.amf_host, 'embassy.py', configuration.verbose)
    >>> slave = configuration.globe_class()
    >>> slave.setup(configuration.mock_speed, configuration.setup_client)
    >>> property_diff(slave, slave.root.title_mc.username_txt, 'text', 
    ...     'ethan')

    doctest an example
    >>> code_unit.inline_examples(
    ...     login_example.__doc__, 
    ...     locals(), globals(), 
    ...     verify_examples = False)

    slave still at login as ethan.
    >>> property_diff(joris, joris.root, 'currentLabel', 'lobby')
    >>> property_diff(joris, joris.root.title_mc.username_txt, 'text', 
    ...     'joris')
    >>> property_diff(slave, slave.root, 'currentLabel', 'login')
    >>> property_diff(slave, slave.root.title_mc.username_txt, 'text', 
    ...     'ethan')
    '''

def after_remote_control_example():
    '''If no master, slave does not match master.  If master, match the master.
    setup slave
    >>> gateway_process = configuration.subprocess_gateway(configuration.amf_host, 'embassy.py', configuration.verbose)
    >>> slave = configuration.globe_class()
    >>> slave.setup(configuration.mock_speed, configuration.setup_client)
    >>> property_diff(slave, slave.root.title_mc.username_txt, 'text', 
    ...     'ethan')

    configure remote control
    >>> configuration.setup_client = setup_master
    >>> set_property = slave_set_property
    >>> dispatch_event = slave_dispatch_event
    >>> mouse_down_and_sleep = slave_mouse_down_and_sleep

    doctest an example
    >>> code_unit.inline_examples(
    ...     login_example.__doc__, 
    ...     locals(), globals(), 
    ...     verify_examples = False)

    slave and master have gone to lobby and are joris.
    >>> property_diff(joris, joris.root, 'currentLabel', 'lobby')
    >>> property_diff(joris, joris.root.title_mc.username_txt, 'text', 
    ...     'joris')
    >>> property_diff(slave, slave.root, 'currentLabel', 'lobby')
    >>> property_diff(slave, slave.root.title_mc.username_txt, 'text', 
    ...     'joris')
    '''

def after_master_class_example():
    '''If no master, slave does not match master.  If master, match the master.
    setup slave
    >>> gateway_process = configuration.subprocess_gateway(configuration.amf_host, 'embassy.py', configuration.verbose)
    >>> slave = configuration.globe_class()
    >>> slave.setup(configuration.mock_speed, configuration.setup_client)
    >>> property_diff(slave, slave.root.title_mc.username_txt, 'text', 
    ...     'ethan')

    configure remote control
    >>> configuration.setup_client = setup_master
    >>> # set_property = slave_set_property
    >>> # dispatch_event = slave_dispatch_event
    >>> # mouse_down_and_sleep = slave_mouse_down_and_sleep
    >>> configuration.globe_class = master_class

    doctest an example
    >>> code_unit.inline_examples(
    ...     login_example.__doc__, 
    ...     locals(), globals(), 
    ...     verify_examples = False)

    slave and master have gone to lobby and are joris.
    >>> property_diff(joris, joris.root, 'currentLabel', 'lobby')
    >>> property_diff(joris, joris.root.title_mc.username_txt, 'text', 
    ...     'joris')
    >>> property_diff(slave, slave.root, 'currentLabel', 'lobby')
    >>> property_diff(slave, slave.root.title_mc.username_txt, 'text', 
    ...     'joris')
    '''


def master_login_example():
    r'''Joris fails and then succeeds to login.
    >>> gateway_process = configuration.subprocess_gateway(configuration.amf_host, 'embassy.py', configuration.verbose)
    >>> joris = configuration.globe_class()
    >>> wait = 4.0 / joris._speed
    >>> joris.setup(configuration.mock_speed, configuration.setup_client)
    >>> time.sleep(wait)
    >>> if not joris.root._on_set:  False
    >>> joris #doctest: +ELLIPSIS
    <master.master_class object at 0x...>
 
    EXT. LOGIN

    At user name text field, Joris mistypes in his name.
    At password, Joris types in his password.
    He clicks the button to start.

    >>> joris.root.currentLabel
    'login'
    >>> joris.root['gateway_mc'].currentLabel
    'connect'
    >>> joris.ambassador.sends
    []
    >>> joris.root.title_mc.username_txt.text = 'Joris'
    
    Master delegates the change to the slave.
    >>> joris.ambassador.sends[-1].get('title_mc').get('username_txt').get('text')
    'Joris'
    >>> time.sleep(wait)
    >>> joris.root.title_mc.password_txt.text = 'j'
    >>> time.sleep(wait)
    >>> joris.root.title_mc.start_btn.dispatchEvent(mouseDown)

    Thus, master requests to enter and awaits gateway reply.
    >>> joris.ambassador.sends[-1].get('gateway_mc')
    >>> time.sleep(wait)

    Soon, he sees he made a mistake with the name or password.
    >>> joris.root.currentLabel
    'login'
    >>> joris.root['gateway_mc'].currentLabel
    'password'

    Master does not delegate the received news to the slave.
    >>> joris.ambassador.sends[-1].get('gateway_mc')

    At user name text field, Joris types in his name.
    At password, Joris types in his password.
    He clicks the button to start.

    >>> joris.root.title_mc.username_txt.text = 'joris'
    >>> time.sleep(wait)
    >>> joris.root.title_mc.password_txt.text = 'j'
    >>> time.sleep(wait)
    >>> joris.root.title_mc.start_btn.dispatchEvent(mouseDown)
    >>> time.sleep(wait)
    >>> time.sleep(max(wait, 2))

    INT. LOBBY

    Soon, he enters the lobby.
    >>> joris.root.currentLabel
    'lobby'
    >>> joris.root['gateway_mc'].currentLabel
    'none'

    #- Joris closes the application.
    #- >>> joris.root.gateway_mc.gotoAndPlay('exit')
    '''


def enable_remote_control_snippet():
    '''Import defaults to mock.  
    >>> configuration.subprocess_gateway = subprocess_gateway_file
    >>> configuration.setup_client = setup_amf_client
    >>> configuration.mock_speed = 1
    >>> ## if not globals().get('verbose'):  verbose = 'info'
    >>> ## configuration.verbose = 'debug'
    >>> configuration.verbose = 'info'
    >>> configuration.setup_client = setup_flash_master
    >>> set_property = slave_set_property
    >>> dispatch_event = slave_dispatch_event
    >>> mouse_down_and_sleep = slave_mouse_down_and_sleep
    '''

def setup_remote_control_snippet():
    '''Start server, before Flash client
    >>> configuration.subprocess_gateway = subprocess_gateway_file
    >>> configuration.setup_client = setup_amf_client
    >>> configuration.mock_speed = 1
    >>> ## if not globals().get('verbose'):  configuration.verbose = 'info'
    >>> ## configuration.verbose = 'debug'
    >>> configuration.verbose = 'info'
    >>> configuration.setup_client = setup_flash_master
    >>> configuration.globe_class = master_class
    >>> configuration.simulate_lag = 0.0
    >>> ## configuration.simulate_lag = 4.0
    >>> set_property = slave_set_property
    >>> dispatch_event = slave_dispatch_event
    >>> mouse_down_and_sleep = slave_mouse_down_and_sleep
    >>> mouse_down_and_news = slave_mouse_down_and_news
    >>> gateway_process = configuration.subprocess_gateway(configuration.amf_host, 'embassy.py', configuration.verbose)
    '''

def remote_login_snippet():
    '''login as Ethan
    >>> setup_flash_client()
    >>> ethan = configuration.globe_class()
    >>> ethan.setup(configuration.mock_speed, configuration.setup_client)
    >>> property_diff(ethan, ethan.root.title_mc.master_txt, 'text', '1')
    >>> time.sleep(1)
    >>> property_diff(ethan, ethan.root.title_mc.slave_txt, 'text', '0')
    >>> time.sleep(1)
    >>> set_property(ethan, ethan.root.title_mc.username_txt, 'text', 'ethan')
    >>> time.sleep(1)
    >>> set_property(ethan, ethan.root.title_mc.password_txt, 'text', 'kennerly')
    >>> time.sleep(1)
    >>> mouse_down_and_sleep(ethan, ethan.root.title_mc.start_btn, 1.0 / ethan._speed)
    '''


def master_save_stage_example():
    '''In Flash, Ethan has just added or removed or changed scene graph.
    Now, Python stage is out of date.  So Ethan saves stage.

    This only works with master client, which invokes Flash.
    >>> gateway_process = configuration.subprocess_gateway(configuration.amf_host, 'embassy.py', configuration.verbose)
    >>> ethan = configuration.globe_class()
    >>> ethan.setup(configuration.mock_speed, configuration.setup_client)

    Stage is setup.
    >>> if not MovieClip == type(ethan.root):
    ...     MovieClip, type(ethan.root)
    >>> if not isMovieClip(ethan.root):
    ...     MovieClip, type(ethan.root)

    Soon ethan sees connection at login.
    >>> time.sleep(1.0 / ethan._speed)
    >>> property_diff(ethan, ethan.root['gateway_mc'], 'currentLabel', 'connect')
    >>> property_diff(ethan, ethan.root, 'currentLabel', 'login')

    ethan supplies his credentials.
    >>> set_property(ethan, ethan.root.title_mc.username_txt, 'text', 'ethan')
    >>> time.sleep(1.0 / ethan._speed)
    >>> set_property(ethan, ethan.root.title_mc.password_txt, 'text', 'kennerly')
    >>> time.sleep(1.0 / ethan._speed)

    ethan presses button to save.
    ethan sees saving is happening.  This takes a few seconds.
    >>> mouse_down_and_sleep(ethan, ethan.root.save_mc,
    ...     24.0 / ethan._speed)

    After half a minute, save is complete.
    >>> property_diff(ethan, ethan.root['save_mc'], 
    ...     'currentLabel', 'none')

    Currently master client grumbles. Is that because it tries to save too?

    Exception in thread Thread-2:
    Traceback (most recent call last):
      File "C:\Python25\lib\threading.py", line 460, in __bootstrap
        self.run()
      File "C:\project\lifeanddeath\amf_socket_client.py", line 199, in run
        self.client.receive()
      File "C:\project\lifeanddeath\amf_socket_client.py", line 184, in receive
        self.on_receive(news)
      File "C:\project\lifeanddeath\client.py", line 349, in imitate
        globe.save_list = globe.save_one_child(globe.root, globe.save_list)
      File "C:\project\lifeanddeath\client.py", line 264, in save_one_child
        child = child_list.pop(0)
    IndexError: pop from empty list
    '''


def modify_flash_example():
    '''Save new movie clip in Flash to file.

    Before we begin, backup the save file.
    >>> import shutil
    >>> backup = save_file_name + '.doctest.bak'
    >>> shutil.copyfile(save_file_name, backup)

    For example, add 'create_mc' to lobby_mc 
    and remove 'start_btn_click_btn' from title_mc.
    >>> gateway_process = configuration.subprocess_gateway(configuration.amf_host, 'embassy.py', configuration.verbose)
    
    In Flash, Ethan adds 'create_mc' to model.
    Ethan connects.
    >>> globe = configuration.globe_class()
    >>> globe.setup(configuration.mock_speed, configuration.setup_client)
    >>> create_mc = MovieClip()
    >>> create_mc.name = 'create_mc'
    >>> create_mc.gotoAndPlay('none')
    >>> globe.root.lobby_mc.addChild(create_mc)
    >>> start_btn_click_btn = globe.root.title_mc.getChildByName('start_btn_click_btn')
    >>> removed_child = globe.root.title_mc.removeChild(start_btn_click_btn)
    >>> globe.root.title_mc.getChildByName('start_btn_click_btn')

    Stage is setup.
    >>> if not MovieClip == type(globe.root):
    ...     MovieClip, type(globe.root)
    >>> if not isMovieClip(globe.root):
    ...     MovieClip, type(globe.root)

    Soon Ethan sees connection at login.
    >>> time.sleep(1.0 / globe._speed)
    >>> if not globe.root['gateway_mc']['currentLabel'] == 'connect':
    ...     print family_tree(globe.root['gateway_mc'], {})
    ...     globe.root['gateway_mc']['currentLabel']
    >>> if not globe.root['currentLabel'] == 'login':
    ...     globe.root['currentLabel']

    Ethan supplies credentials.
    >>> globe.root['title_mc']['username_txt'].text = 'ethan'
    >>> globe.root['title_mc']['password_txt'].text = 'kennerly'

    Ethan presses button to save.
    Ethan sees saving is happening.  This takes a few seconds.
    >>> globe.root.save_mc.dispatchEvent(
    ...     MouseEvent(MouseEvent.MOUSE_DOWN))

    After a while, save is complete.
    >>> time.sleep(24.0 / globe._speed)
    >>> if not globe.root['save_mc']['currentLabel'] == 'none':
    ...     print family_tree(globe.root['save_mc'], {})
    ...     globe.root['save_mc']['currentLabel']

    Ethan closes the application.
    >>> globe.root.gateway_mc.gotoAndPlay('exit')

    #Ethan changes a message.
    #>>> globe.root.create_mc.gotoAndPlay('enter')

    #Ethan clicks button to load.
    #>>> globe.root.load_mc.dispatchEvent(
    #...     MouseEvent(MouseEvent.MOUSE_DOWN))

    #Ethan sees loading is happening.  This takes a few seconds.
    #>>> time.sleep(16.0 / globe._speed)
    
    #After a while...  the message is reverted.
    #>>> if not globe.root['create_mc']['currentLabel'] == 'none':
    #...     print family_tree(globe.root['create_mc'], {})
    #...     globe.root['create_mc']['currentLabel']

    A new client of joris has create_mc but no first cell.
    >>> joris = configuration.globe_class()
    >>> joris.setup(configuration.mock_speed, configuration.setup_client)
    >>> if joris.root.title_mc.getChildByName('start_btn_click_btn'):
    ...     print joris.root['title_mc'].start_btn_click_btn
    ...     print family_tree(joris.root['title_mc'].start_btn_click_btn, {})
    >>> if not joris.root['lobby_mc']['create_mc']['currentLabel'] == 'none':
    ...     print family_tree(joris.root['lobby_mc']['create_mc'], {})
    ...     joris.root['lobby_mc']['create_mc']['currentLabel']

    Joris closes the application.
    >>> joris.root.gateway_mc.gotoAndPlay('exit')

    Afterward, restore the original save file, so data is not corrupted.
    >>> shutil.copyfile(backup, save_file_name)
    '''


def load_example():
    '''Save and load the stage to and from server file.

    For example, load_stage reverts at least a couple of labels on stage.
    Joris logs in.
    >>> gateway_process = configuration.subprocess_gateway(configuration.amf_host, 'embassy.py', configuration.verbose)
    >>> globe = configuration.globe_class()
    >>> globe.setup(configuration.mock_speed, configuration.setup_client)

    Stage is setup.
    >>> if not MovieClip == type(globe.root):
    ...     MovieClip, type(globe.root)
    >>> if not isMovieClip(globe.root):
    ...     MovieClip, type(globe.root)

    Soon Joris sees connection at login.
    >>> time.sleep(1.0 / globe._speed)
    >>> if not globe.root['gateway_mc']['currentLabel'] == 'connect':
    ...     print family_tree(globe.root['gateway_mc'], {})
    ...     globe.root['gateway_mc']['currentLabel']
    >>> if not globe.root['currentLabel'] == 'login':
    ...     globe.root['currentLabel']

    Joris supplies his credentials.
    >>> globe.root['title_mc']['username_txt'].text = 'joris'
    >>> globe.root['title_mc']['password_txt'].text = 'j'

    Joris presses button to save.
    Joris sees saving is happening.  This takes a few seconds.
    >>> globe.root.save_mc.dispatchEvent(
    ...     MouseEvent(MouseEvent.MOUSE_DOWN))

    After a while, save is complete.
    >>> time.sleep(24.0 / globe._speed)
    >>> if not globe.root['save_mc']['currentLabel'] == 'none':
    ...     print family_tree(globe.root['save_mc'], {})
    ...     globe.root['save_mc']['currentLabel']

    Joris changes a message.
    >>> globe.root.gotoAndPlay('lobby')
    >>> globe.root['gateway_mc'].gotoAndPlay('already_login')

    Joris clicks button to load.
    >>> globe.root.load_mc.dispatchEvent(
    ...     MouseEvent(MouseEvent.MOUSE_DOWN))

    Joris sees loading is happening.  This takes a few seconds.
    After a while...  the message is reverted.
    >>> time.sleep(16.0 / globe._speed)
    >>> if not globe.root['gateway_mc']['currentLabel'] == 'connect':
    ...     print family_tree(globe.root['gateway_mc'], {})
    ...     globe.root['gateway_mc']['currentLabel']
    >>> if not globe.root['currentLabel'] == 'login':
    ...     globe.root['currentLabel']

    Joris closes the application.
    >>> globe.root.gateway_mc.gotoAndPlay('exit')
    '''



snippet = '''
# !start python code_explorer.py --snippet snippet --import master.py
import master; master = reload(master); from master import *
# code_unit.doctest_unit(play_history)
'''
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
    else:
        units = globals().values()
        ## units.remove(setup_example)
        code_unit.doctest_units(units)

