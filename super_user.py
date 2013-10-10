#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
User functions that are excluded from Flash client but needed by server.
'''
__author__ = 'Ethan Kennerly'

import user_as
from intersection_mc import *
from remote_control import address, note
# from user_as import MouseEvent, mouseDown, setup_echo, echo_protocol_class
from user_as import *

def _parent_goto_mc_name_news(mouse_event):
    target = mouse_event.currentTarget.parent
    mouse_mc = mouse_event.currentTarget
    return _target_goto_mc_name_news(target, mouse_mc)

def _target_goto_mc_name_news(target, mouse_mc):
    mc_name = mouse_mc.name
    label = rstrip_string(mc_name, '_mc')
    target_news = note(target, 
        'currentLabel', label)
    mc_news = note(mouse_mc, 
        'currentLabel', 'none')
    news = upgrade(mc_news, target_news)
    return news
        
def adjust_level_balance_news(black, white):
    '''Get and show level balance.
    >>> code_unit.doctest_unit(user_class.adjust_level_balance, log = False)
    '''
    from super_users import get_effective_level, get_prize_arguments
    arguments = get_prize_arguments(black, white, True)
    black_level = get_effective_level(arguments[0], *arguments[2:])
    white_level = arguments[1]
    level_news = {
        'game_over_mc': {
            'balance_mc': {
                'black_level_txt': {
                    'text': str(black_level),
                },
                'white_level_txt': {
                    'text': str(white_level),
                },
            },
        },
    }
    return level_news



def sequence_stone(news, events, time, intersection_names):
    '''Convert untimed build bunker event to 1-second event.
    >>> moonhyoung = user_class()
    >>> moonhyoung.create()

    After question black, client goes to question_black_repeat on fixed interval.
    >>> news = note(moonhyoung.root._3_3_mc, 'currentLabel', 'question_black')
    >>> news['_3_3_mc']['currentLabel']
    'question_black'
    >>> names = get_intersection_names(moonhyoung.intersection_mc_array)
    >>> events, time, name = sequence_stone(news, [], 1000, names)
    >>> events[0]['time_txt']['text']
    '2000'
    >>> events[0]['_3_3_mc']['currentLabel']
    'question_black'
    >>> news.get('_3_3_mc')
    >>> name
    '_3_3_mc'
    
    >>> news = note(moonhyoung.root._3_3_mc, 'currentLabel', 'black')
    >>> news['_3_3_mc']['currentLabel']
    'black'
    >>> names = get_intersection_names(moonhyoung.intersection_mc_array)
    >>> events, time, name = sequence_stone(news, [], 1000, names)
    >>> events[0]['time_txt']['text']
    '2000'
    >>> events[0]['_3_3_mc']['currentLabel']
    'black'
    >>> news.get('_3_3_mc')
    >>> name
    '_3_3_mc'

    sequence white.
    >>> news = note(moonhyoung.root._4_4_mc, 'currentLabel', 'white')
    >>> news['_4_4_mc']['currentLabel']
    'white'
    >>> names = get_intersection_names(moonhyoung.intersection_mc_array)
    >>> events, time, name = sequence_stone(news, [], 1000, names)
    >>> events[0]['time_txt']['text']
    '2000'
    >>> events[0]['_4_4_mc']['currentLabel']
    'white'
    >>> news.get('_4_4_mc')
    >>> name
    '_4_4_mc'

    sequence hide_black
    >>> marije = moonhyoung
    >>> news = note(marije.root._4_4_mc, 'currentLabel', 'question_hide_black')
    >>> news['_4_4_mc']['currentLabel']
    'question_hide_black'
    >>> names = get_intersection_names(marije.intersection_mc_array)
    >>> events, time, name = sequence_stone(news, [], 1000, names)
    >>> events[0]['time_txt']['text']
    '2000'
    >>> events[0]['_4_4_mc']['currentLabel']
    'question_hide_black'
    >>> news.get('_4_4_mc')
    >>> name
    '_4_4_mc'

    Ignore unsequenced events.
    >>> news = note(moonhyoung.root.menu_mc, 'currentLabel', 'none')
    >>> events, time, name = sequence_stone(news, [], 1000, names)
    >>> news.get('sequence')
    >>> news
    {'menu_mc': {'currentLabel': 'none'}}

    Ignore unsequenced intersection events.
    >>> news = note(moonhyoung.root._3_3_mc, 'currentLabel', 'question_black')
    >>> news = upgrade(news, note(moonhyoung.root._3_3_mc.black_shape_mc, 'currentLabel', '_0001') )
    >>> news = upgrade(news, note(moonhyoung.root._0_0_mc.black_shape_mc, 'currentLabel', '_0000') )
    >>> news['_3_3_mc']['currentLabel']
    'question_black'
    >>> events, time, name = sequence_stone(news, [], 1000, names)
    >>> events[0]['time_txt']['text']
    '2000'
    >>> events[0]['_3_3_mc']['currentLabel']
    'question_black'
    >>> events[0]['_3_3_mc'].get('black_shape_mc')
    >>> events[0].get('_0_0_mc')
    >>> news.get('_3_3_mc').get('currentLabel')
    >>> news['_3_3_mc']['black_shape_mc']['currentLabel']
    '_0001'
    >>> news['_0_0_mc']['black_shape_mc']['currentLabel']
    '_0000'
    '''
    found = ''
    for intersection_name in intersection_names:
        new_intersection = news.get(intersection_name)
        if new_intersection:
            label = news[intersection_name].get('currentLabel')
            labels = ['question_black', 'question_hide_black', 'black', 'white']
            if label and label in labels:
                found = intersection_name
                event = {intersection_name: {'currentLabel': label}}
                time += 1000
                event = upgrade(event, {'time_txt': {'text': str(time)}})
                events.append(event)
                del news[intersection_name]['currentLabel']
                if not news[intersection_name]:
                    del news[intersection_name]
    return events, time, found


def sequence_progress(news, events, time, intersection_names, suffix):
    '''start progress appears after stone
    >>> rene = user_class()
    >>> rene.create()
    >>> intersection_names = get_intersection_names(rene.intersection_mc_array)
    >>> events = []
    >>> time = 1000
    >>> news = {}
    >>> suffix = ''
    >>> events, time = sequence_progress(news, events, time, intersection_names, suffix)
    >>> events
    []
    >>> time
    1000
    >>> news
    {}
    >>> news = {'_1_1_mc': {'currentLabel': 'black', 'progress_mc': {'currentLabel':  'black_start'}}}
    >>> suffix = '_start'
    >>> events, time = sequence_progress(news, events, time, intersection_names, suffix)
    >>> events[0]['time_txt']['text']
    '1000'
    >>> events[0]['_1_1_mc']['progress_mc']['currentLabel']
    'black_start'
    >>> time
    1000
    >>> news
    {'_1_1_mc': {'currentLabel': 'black'}}

    sequence complete progress at same time as your turn begins
    >>> events = []
    >>> news = {'_1_1_mc': {'progress_mc': {'currentLabel':  'black_complete'}}}
    >>> suffix = '_complete'
    >>> events, time = sequence_progress(news, events, time, intersection_names, suffix)
    >>> events[0]['time_txt']['text']
    '1000'
    >>> events[0]['_1_1_mc']['progress_mc']['currentLabel']
    'black_complete'
    >>> time
    1000
    >>> news
    {}
    '''
    for intersection_name in intersection_names:
        new_intersection = news.get(intersection_name)
        if new_intersection:
            label = ''
            progress = news[intersection_name].get('progress_mc')
            if progress:
                label = progress.get('currentLabel')
            labels = ['black%s' % suffix, 'white%s' % suffix]
            if label and label in labels:
                event = {intersection_name: {'progress_mc': {
                    'currentLabel': label}}}
                event = upgrade(event, {'time_txt': {'text': str(time)}})
                events.append(event)
                del news[intersection_name]['progress_mc']
                if not news[intersection_name]:
                    del news[intersection_name]
    return events, time


def get_kyung_first_move_unsequenced_news(): 
    return \
    {'_1_1_mc': {'decoration_mc': {'currentLabel': 'black_defend'}},
     '_1_2_mc': {'decoration_mc': {'currentLabel': 'black_attack'}},
     '_1_3_mc': {'decoration_mc': {'currentLabel': 'black_attack'}},
     '_1_4_mc': {'decoration_mc': {'currentLabel': 'black_attack'}},
     '_1_5_mc': {'decoration_mc': {'currentLabel': 'black_defend'}},
     '_2_1_mc': {'decoration_mc': {'currentLabel': 'black_attack'}},
     '_2_2_mc': {'decoration_mc': {'currentLabel': 'black_attack'}},
     '_2_3_mc': {'decoration_mc': {'currentLabel': 'black_attack'}},
     '_2_4_mc': {'decoration_mc': {'currentLabel': 'black_attack'}},
     '_2_5_mc': {'decoration_mc': {'currentLabel': 'black_attack'}},
     '_2_6_mc': {'top_move_mc': {'currentLabel': 'white'}},
     '_3_1_mc': {'decoration_mc': {'currentLabel': 'black_attack'}},
     '_3_2_mc': {'decoration_mc': {'currentLabel': 'black_attack'}},
     '_3_3_mc': {'black_shape_mc': {'attack_mc': {'currentLabel': '_0000',
                                    'defend_mc': {'currentLabel': 'show'}},
                                'defend_mc': {'currentLabel': 'show'}},
                 'formation_mc': {'currentLabel': 'black_attack_defend'}},
     '_3_4_mc': {'decoration_mc': {'currentLabel': 'black_attack'}},
     '_3_5_mc': {'decoration_mc': {'currentLabel': 'black_attack'}},
     '_4_1_mc': {'decoration_mc': {'currentLabel': 'black_attack'}},
     '_4_2_mc': {'decoration_mc': {'currentLabel': 'black_attack'}},
     '_4_3_mc': {'decoration_mc': {'currentLabel': 'black_attack'}},
     '_4_4_mc': {'decoration_mc': {'currentLabel': 'black_attack'}},
     '_4_5_mc': {'decoration_mc': {'currentLabel': 'black_attack'}},
     '_5_1_mc': {'decoration_mc': {'currentLabel': 'black_defend'}},
     '_5_2_mc': {'decoration_mc': {'currentLabel': 'black_attack'}},
     '_5_3_mc': {'decoration_mc': {'currentLabel': 'black_attack'}},
     '_5_4_mc': {'decoration_mc': {'currentLabel': 'black_attack'}},
     '_5_5_mc': {'decoration_mc': {'currentLabel': 'black_defend'}},
     'cursor_mc': {'act_mc': {'currentLabel': 'preview'}},
     'score_mc': {'bar_mc': {'currentLabel': '_0',
                             'marker_mc': {'change_txt': {'text': '0'},
                                           'currentLabel': 'neutral'},
                             'territory_txt': {'text': '0'}}}}


def get_laurens_profit_unsequenced_news():
    return \
    {'_0_0_mc': {'territory_mc': {'currentLabel': 'black'}},
     '_0_1_mc': {'territory_mc': {'currentLabel': 'black'}},
     '_0_2_mc': {'territory_mc': {'currentLabel': 'black'}},
     '_0_3_mc': {'territory_mc': {'currentLabel': 'black'}},
     '_0_4_mc': {'territory_mc': {'currentLabel': 'black'}},
     '_1_0_mc': {'territory_mc': {'currentLabel': 'black'}},
     '_1_1_mc': {'territory_mc': {'currentLabel': 'black'}},
     '_1_2_mc': {'territory_mc': {'currentLabel': 'black'}},
     '_1_3_mc': {'territory_mc': {'currentLabel': 'black'}},
     '_1_4_mc': {'territory_mc': {'currentLabel': 'black'}},
     '_2_0_mc': {'territory_mc': {'currentLabel': 'black'}},
     '_2_1_mc': {'territory_mc': {'currentLabel': 'black'}},
     '_2_2_mc': {'black_shape_mc': {'defend_mc': {'profit_mc': {'currentLabel': 'show'}}},
                 'currentLabel': 'question_black'},
     '_2_3_mc': {'territory_mc': {'currentLabel': 'black'}},
     '_3_0_mc': {'territory_mc': {'currentLabel': 'black'}},
     '_3_1_mc': {'territory_mc': {'currentLabel': 'black'}},
     '_3_2_mc': {'territory_mc': {'currentLabel': 'black'},
                 'top_move_mc': {'currentLabel': 'white'}},
     '_3_3_mc': {'territory_mc': {'currentLabel': 'black'}},
     '_3_4_mc': {'territory_mc': {'currentLabel': 'black'}},
     '_4_0_mc': {'territory_mc': {'currentLabel': 'black'}},
     '_4_1_mc': {'territory_mc': {'currentLabel': 'black'}},
     '_4_2_mc': {'territory_mc': {'currentLabel': 'black'}},
     '_4_3_mc': {'territory_mc': {'currentLabel': 'black'}},
     '_4_4_mc': {'territory_mc': {'currentLabel': 'black'}},
     'cursor_mc': {'act_mc': {'currentLabel': 'preview'}},
     'score_mc': {'bar_mc': {'currentLabel': '_23',
                             'marker_mc': {'change_txt': {'text': '+23'},
                                           'currentLabel': 'positive'},
                             'territory_txt': {'text': '23'}}},
     'tutor_mc': {'currentLabel': 'question'}}


def get_distance(i0, i1):
    '''
    >>> get_distance('_3_3_mc', '_3_2_mc')
    1
    >>> get_distance('_3_3_mc', '_1_3_mc')
    2
    >>> get_distance('_3_3_mc', '_4_4_mc')
    2
    >>> get_distance('', '_4_4_mc')
    2
    '''
    r0, c0 = get_row_column(i0)
    r1, c1 = get_row_column(i1)
    dr = abs(r1 - r0)
    dc = abs(c1 - c0)
    return dr + dc

def sequence_wave(property_name, news, events, time, intersection_names, 
        origin_name, step = 125, label_name = None):
    '''Knights build in order from castle.
    >>> moonhyoung = user_class()
    >>> moonhyoung.create()
    
    >>> news = get_kyung_first_move_unsequenced_news()
    >>> news['_3_2_mc']['decoration_mc']['currentLabel']
    'black_attack'
    >>> names = get_intersection_names(moonhyoung.intersection_mc_array)
    >>> events, time = sequence_wave('decoration_mc', news, [0], 5000, names, '_3_3_mc', step = 250)
     
    Append to events.
    >>> events[0]
    0
    >>> events[1]['time_txt']['text']
    '5250'
    >>> events[1]['_3_2_mc']['decoration_mc']['currentLabel']
    'black_attack'
    >>> news.get('_3_2_mc')
    >>> events[2]['time_txt']['text']
    '5500'
    >>> events[2]['_3_1_mc']['decoration_mc']['currentLabel']
    'black_attack'
    >>> events[4]['_1_1_mc']['decoration_mc']['currentLabel']
    'black_defend'
    >>> len(events)
    5
    >>> news.get('_3_1_mc')

    Return time of last event
    >>> events[4]['time_txt']['text']
    '6000'
    >>> time
    6000
     
    Ignore unsequenced events.
    >>> news = note(moonhyoung.root.menu_mc, 'currentLabel', 'none')
    >>> events, time = sequence_wave('decoration_mc', news, [], 5000, names, '_3_3_mc', step = 250)
    >>> news.get('sequence')
    >>> news
    {'menu_mc': {'currentLabel': 'none'}}
     
    Ignore unsequenced intersection events.
    >>> news = get_kyung_first_move_unsequenced_news()
    >>> news = upgrade(news, note(moonhyoung.root._3_3_mc.black_shape_mc, 'currentLabel', '_0001') )
    >>> events, time = sequence_wave('decoration_mc', news, [], 5000, names, '_3_3_mc', step = 125)
    >>> events[0]['time_txt']['text']
    '5125'
    >>> events[0]['_3_2_mc']['decoration_mc']['currentLabel']
    'black_attack'
    >>> events[0].get('_3_3_mc')
    >>> events[0].get('_0_0_mc')
    >>> news.get('_3_3_mc').get('currentLabel')
    >>> news['_3_3_mc']['black_shape_mc']['currentLabel']
    '_0001'

    Sequence none events and white labels.
    >>> news = note(moonhyoung.root._3_4_mc.decoration_mc, 'currentLabel', 'none')
    >>> news = upgrade(news, note(moonhyoung.root._3_5_mc.decoration_mc, 'currentLabel', 'white_defend') )
    >>> events, time = sequence_wave('decoration_mc', news, [], 5000, names, '_3_3_mc', step = 250)
    >>> events[0]['time_txt']['text']
    '5250'
    >>> events[0]['_3_4_mc']['decoration_mc']['currentLabel']
    'none'
    >>> events[1]['time_txt']['text']
    '5500'
    >>> events[1]['_3_5_mc']['decoration_mc']['currentLabel']
    'white_defend'

    Sequence territory
    >>> news = note(moonhyoung.root._3_4_mc.territory_mc, 'currentLabel', 'none')
    >>> news = upgrade(news, note(moonhyoung.root._3_5_mc.territory_mc, 'currentLabel', 'white') )
    >>> events, time = sequence_wave('territory_mc', news, [], 5000, names, '_3_3_mc', step = 250)
    >>> events[0]['time_txt']['text']
    '5250'
    >>> events[0]['_3_4_mc']['territory_mc']['currentLabel']
    'none'
    >>> events[1]['time_txt']['text']
    '5500'
    >>> events[1]['_3_5_mc']['territory_mc']['currentLabel']
    'white'

    Sequence critical
    >>> news = {'_4_2_mc': {'dragon_status_mc': {'currentLabel': 'black_attack'}}}
    >>> events, time = sequence_wave('dragon_status_mc', news, [], 6000, names, '_4_3_mc', step = 125)
    >>> events[0]['time_txt']['text']
    '6125'
    >>> events[0]['_4_2_mc']['dragon_status_mc']['currentLabel']
    'black_attack'

    If specified, only sequence the label.
    >>> news = {'_0_1_mc': {'top_move_mc': {'currentLabel': 'black'}},
    ...     '_1_1_mc': {'top_move_mc': {'currentLabel': 'white'}}}
    >>> events, time = sequence_wave('top_move_mc', news, [], 6000, names, '_4_3_mc', step = 125, label_name = 'white')
    >>> len(events)
    1
    >>> events[0]['_1_1_mc']['top_move_mc']['currentLabel']
    'white'
    >>> events[0].get('_0_1_mc')
    >>> events, time = sequence_wave('top_move_mc', news, [], 6000, names, '_4_3_mc', step = 125, label_name = 'black')
    >>> events[0]['_0_1_mc']['top_move_mc']['currentLabel']
    'black'
    >>> events[0].get('_1_1_mc')
    
    >>> news = {'_0_1_mc': {'square_mc': {'currentLabel': 'show'}},
    ...     '_1_1_mc': {'square_mc': {'currentLabel': 'none'}}}
    >>> events, time = sequence_wave('square_mc', news, events, 0, 
    ...     names, '_4_3_mc', label_name = 'show')
    >>> news['_1_1_mc']
    {'square_mc': {'currentLabel': 'none'}}
    >>> news.get('_0_1_mc')
    '''
    #step = 250
    distances = {}
    for intersection_name in intersection_names:
        new_intersection = news.get(intersection_name)
        if new_intersection:
            decoration = news[intersection_name].get(property_name)
            if decoration:
                label = news[intersection_name][property_name].get('currentLabel')
                if label:
                    if label_name is None or label_name == label: 
                        event = {intersection_name: {property_name: {
                            'currentLabel': label}}}
                        distance = get_distance(origin_name, intersection_name)
                        arrival = time + distance * step
                        event = upgrade(event, {'time_txt': {'text': str(arrival)}})
                        distances = upgrade(distances, {distance: event})
                        del news[intersection_name][property_name]['currentLabel']
                        if not news[intersection_name][property_name]:
                            del news[intersection_name][property_name]
                        if not news[intersection_name]:
                            del news[intersection_name]
    if distances:
        distances_events = distances.items()
        distances_events.sort()
        for distance, event in distances_events:
            events.append(event)
        time = int(events[-1]['time_txt']['text'])
    return events, time

def sequence_strike(news, events, time, intersection_names, origin_name):
    '''Bunker soldier strikes or retaliates.  In order of distance.
    >>> moonhyoung = user_class()
    >>> moonhyoung.create()
    
    >>> news = note(moonhyoung.root._4_4_strike_mc.west_mc, 
    ...     'currentLabel', 'white_notice')
    >>> news = upgrade(news, note(moonhyoung.root._3_4_strike_mc.north_mc, 
    ...     'currentLabel', 'white_notice') )
    >>> news['_4_4_strike_mc']['west_mc']['currentLabel']
    'white_notice'
    >>> names = get_intersection_names(moonhyoung.intersection_mc_array)
    >>> events, time = sequence_strike(news, [0], 5000, names, '_4_4_mc')
     
    Append to events.
    >>> events[0]
    0
    >>> events[1]['time_txt']['text']
    '5250'
    >>> events[1]['_4_4_strike_mc']['west_mc']['currentLabel']
    'white_notice'
    >>> events[1]['time_txt']['text']
    '5250'
    >>> events[2]['_3_4_strike_mc']['north_mc']['currentLabel']
    'white_notice'
    >>> len(events)
    3
    >>> news.get('_4_4_strike_mc')

    Return time of last event
    >>> events[2]['time_txt']['text']
    '5500'
    >>> time
    5500

    Ignore unsequenced events.
    >>> news = note(moonhyoung.root.menu_mc, 'currentLabel', 'none')
    >>> events, time = sequence_strike(news, [], 5000, names, '_3_3_mc')
    >>> news.get('sequence')
    >>> news
    {'menu_mc': {'currentLabel': 'none'}}
     
    Ignore unsequenced intersection events.
    >>> news = note(moonhyoung.root._4_4_strike_mc.west_mc, 
    ...     'currentLabel', 'white_notice')
    >>> news = upgrade(news, note(moonhyoung.root._4_4_mc.black_shape_mc, 'currentLabel', '_0001') )
    >>> events, time = sequence_strike(news, [], 5000, names, '_4_4_mc')
    >>> events[0]['time_txt']['text']
    '5250'
    >>> events[0]['_4_4_strike_mc']['west_mc']['currentLabel']
    'white_notice'
    >>> events[0].get('_4_4_mc')
    >>> news.get('_4_4_strike_mc')
    >>> news['_4_4_mc']['black_shape_mc']['currentLabel']
    '_0001'
    '''
    return sequence_direction(news, events, time, intersection_names, 
            origin_name, '_strike_mc', step = 250)


def sequence_direction(news, events, time, intersection_names, origin_name,
        suffix = '_mc', child_prefix = '', step = 125):
    '''Bunker soldier strikes or retaliates.  In order of distance.
    Or block.
    >>> moonhyoung = user_class()
    >>> moonhyoung.create()
    
    >>> news = note(moonhyoung.root._4_4_strike_mc.west_mc, 
    ...     'currentLabel', 'white_notice')
    >>> news = upgrade(news, note(moonhyoung.root._3_4_strike_mc.north_mc, 
    ...     'currentLabel', 'white_notice') )
    >>> news['_4_4_strike_mc']['west_mc']['currentLabel']
    'white_notice'
    >>> names = get_intersection_names(moonhyoung.intersection_mc_array)
    >>> events, time = sequence_direction(news, [0], 5000, names, '_4_4_mc',
    ...     '_strike_mc', step = 250)
     
    Append to events.
    >>> events[0]
    0
    >>> events[1]['time_txt']['text']
    '5250'
    >>> events[1]['_4_4_strike_mc']['west_mc']['currentLabel']
    'white_notice'
    >>> events[1]['time_txt']['text']
    '5250'
    >>> events[2]['_3_4_strike_mc']['north_mc']['currentLabel']
    'white_notice'
    >>> len(events)
    3
    >>> news.get('_4_4_strike_mc')

    Return time of last event
    >>> events[2]['time_txt']['text']
    '5500'
    >>> time
    5500

    block
    >>> news = note(moonhyoung.root._4_4_mc.block_west_mc, 
    ...     'currentLabel', 'white_notice')
    >>> news = upgrade(news, note(moonhyoung.root._3_4_mc.block_north_mc, 
    ...     'currentLabel', 'white_notice') )
    >>> news['_4_4_mc']['block_west_mc']['currentLabel']
    'white_notice'
    >>> names = get_intersection_names(moonhyoung.intersection_mc_array)
    >>> events, time = sequence_direction(news, [0], 5000, names, '_4_4_mc',
    ...     '_mc', 'block_', step = 250)
     
    Append to events.
    >>> events[0]
    0
    >>> events[1]['time_txt']['text']
    '5250'
    >>> events[1]['_4_4_mc']['block_west_mc']['currentLabel']
    'white_notice'
    >>> events[1]['time_txt']['text']
    '5250'
    >>> events[2]['_3_4_mc']['block_north_mc']['currentLabel']
    'white_notice'
    >>> len(events)
    3
    >>> news.get('_4_4_mc')

    Ignore unsequenced events.
    >>> news = note(moonhyoung.root.menu_mc, 'currentLabel', 'none')
    >>> events, time = sequence_direction(news, [], 5000, names, '_3_3_mc', step = 250)
    >>> news.get('sequence')
    >>> news
    {'menu_mc': {'currentLabel': 'none'}}
     
    Ignore unsequenced intersection events.
    >>> news = note(moonhyoung.root._4_4_strike_mc.west_mc, 
    ...     'currentLabel', 'white_notice')
    >>> news = upgrade(news, note(moonhyoung.root._4_4_mc.black_shape_mc, 'currentLabel', '_0001') )
    >>> events, time = sequence_direction(news, [], 5000, names, '_4_4_mc',
    ...     '_strike_mc', step = 125)
    >>> events[0]['time_txt']['text']
    '5125'
    >>> events[0]['_4_4_strike_mc']['west_mc']['currentLabel']
    'white_notice'
    >>> events[0].get('_4_4_mc')
    >>> news.get('_4_4_strike_mc')
    >>> news['_4_4_mc']['black_shape_mc']['currentLabel']
    '_0001'
    '''
    if '_mc' == suffix:
        strike_names = intersection_names
    else:
        strike_names = [rstrip_string(i, '_mc') + suffix
            for i in intersection_names]
    distances = {}
    for strike_name in strike_names:
        new_strike = news.get(strike_name)
        if new_strike:
            directions = ['north_mc', 'east_mc', 'south_mc', 'west_mc']
            for direction in directions:
                direction = child_prefix + direction
                if new_strike.get(direction):
                    label = news[strike_name][direction].get('currentLabel')
                    if label:
                        event = {strike_name: {direction: {
                            'currentLabel': label}}}
                        distance = get_distance(origin_name, strike_name)
                        arrival = time + (1 + distance) * step
                        event = upgrade(event, {'time_txt': {
                            'text': str(arrival)}})
                        distances = upgrade(distances, {distance: event})
                        del news[strike_name][direction]['currentLabel']
                        if not news[strike_name][direction]:
                            del news[strike_name][direction]
                        if not news[strike_name]:
                            del news[strike_name]
    if distances:
        distances_events = distances.items()
        distances_events.sort()
        for distance, event in distances_events:
            events.append(event)
        time = int(events[-1]['time_txt']['text'])
    return events, time


def sequence_profit(news, events, time, origin_name, step = 750):
    '''sequence profit but not score.
    >>> news = get_laurens_profit_unsequenced_news()
    >>> events, time = sequence_profit(news, [], 1000, '_2_2_mc', step = 500)
    >>> events[0].get('score_mc')
    >>> if not news.has_key('score_mc'):  news
    >>> shape = events[0]['_2_2_mc']['black_shape_mc']
    >>> shape['defend_mc']['profit_mc']['currentLabel']
    'show'
    >>> news['_2_2_mc'].get('black_shape_mc')
    >>> len(events)
    1

    Time
    >>> events[0]['time_txt']['text']
    '1500'
    >>> time
    1500

    Only checks profit at origin.
    >>> news = get_laurens_profit_unsequenced_news()
    >>> events, time = sequence_profit(news, [], 1000, '_2_3_mc')
    >>> events
    []
    >>> time
    1000
    '''
    #score = news.get('score_mc')
    #if score:
    #    event = {}
    #    event['score_mc'] = news.pop('score_mc')
    #    event = upgrade(event, {'time_txt': {'text': str(time + step)}})
    #    events.append(event)
    #    time = int(events[-1]['time_txt']['text'])
    # TODO:  extract and share find subdictionary
    origin = news.get(origin_name)
    if origin:
        shape = origin.get('black_shape_mc')
        if shape:
            defend = shape.get('defend_mc')
            if defend:
                profit = defend.get('profit_mc')
                if profit:
                    label = profit.get('currentLabel')
                    if label:
                        event = {origin_name: {'black_shape_mc': {
                            'defend_mc': {'profit_mc': {
                                'currentLabel': label}}}}}
                        event = upgrade(event, {'time_txt': {
                            'text': str(time + step)}})
                        events.append(event)
                        time = int(events[-1]['time_txt']['text'])
                        # TODO:  extract and share tidy function
                        del news[origin_name]['black_shape_mc']['defend_mc']['profit_mc']['currentLabel']
                        if not news[origin_name]['black_shape_mc']['defend_mc']['profit_mc']:
                            del news[origin_name]['black_shape_mc']['defend_mc']['profit_mc']
                        if not news[origin_name]['black_shape_mc']['defend_mc']:
                            del news[origin_name]['black_shape_mc']['defend_mc']
                        if not news[origin_name]['black_shape_mc']:
                            del news[origin_name]['black_shape_mc']
                        if not news[origin_name]:
                            del news[origin_name]
    return events, time


def sequence_child(child_name, news, events, time, step = 250, needs_label = False):
    '''Child of root.
    sequence cursor.
    >>> news = get_laurens_profit_unsequenced_news()
    >>> events, time = sequence_child('cursor_mc', news, [], 1000, step = 250)
    >>> event = events[-1]
    >>> event['cursor_mc']['act_mc']['currentLabel']
    'preview'
    >>> event['time_txt']['text']
    '1250'
    >>> time
    1250

    tutor
    >>> events, time = sequence_child('tutor_mc', news, [], 1000, step = 500)
    >>> event = events[-1]
    >>> event['tutor_mc']['currentLabel']
    'question'
    >>> event['time_txt']['text']
    '1500'
    >>> time
    1500

    extra stone or hide gift
    >>> news = {'extra_stone_gift_mc': {'currentLabel': '_1'}}
    >>> events, time = sequence_child('extra_stone_gift_mc', news, [], 1000)
    >>> events[-1]['extra_stone_gift_mc']['currentLabel']
    '_1'
    >>> news = {'hide_gift_mc': {'currentLabel': '_0'}}
    >>> events, time = sequence_child('hide_gift_mc', news, [], 1000)
    >>> events[-1]['hide_gift_mc']['currentLabel']
    '_0'

    needs a label to sequence.
    >>> news = {'turn_mc': {'white_username_txt': 'WHITE'}}
    >>> events, time = sequence_child('turn_mc', news, [], 1000, needs_label = True)
    >>> events
    []
    '''
    child = news.get(child_name)
    if child:
        if not needs_label or child.get('currentLabel'):
            event = {}
            event[child_name] = news.pop(child_name)
            event = upgrade(event, {'time_txt': {'text': str(time + step)}})
            events.append(event)
            time = int(events[-1]['time_txt']['text'])
            ## time += step
    return events, time


import copy
def sequence_score(child_name, news, events, time, step = 125, 
        needs_label = False, old_value = 0):
    '''Expand difference to a range.
    >>> news = {}
    >>> events, time = sequence_score('score_mc', news, [], 1000, step = 125)
    >>> events
    []
    >>> time
    1000

    Score up.
    >>> news = {'score_mc': {'bar_mc': {'currentLabel': '_4', 'marker_mc': {'change_txt': {'text': '4'}}}}}
    >>> events, time = sequence_score('score_mc', news, [], 1000, step = 125)
    >>> from pprint import pprint
    >>> ## pprint(events)
    >>> events[-1]['time_txt']['text']
    '1625'
    >>> events[-1]['score_mc']['bar_mc']['currentLabel']
    '_4'
    >>> events[-1]['score_mc']['bar_mc']['marker_mc']['change_txt']['text']
    '4'
    >>> events[-2]['time_txt']['text']
    '1500'
    >>> events[-2]['score_mc']['bar_mc']['currentLabel']
    '_3'
    >>> events[-2]['score_mc']['bar_mc']['marker_mc']['change_txt']['text']
    '3'
    >>> events[-3]['time_txt']['text']
    '1375'
    >>> events[-3]['score_mc']['bar_mc']['currentLabel']
    '_2'
    >>> events[-3]['score_mc']['bar_mc']['marker_mc']['change_txt']['text']
    '2'

    Score down.  From old value.
    Corrupts '+' change prefix for marker intermediate values.
    >>> news = {'score_mc': {'bar_mc': {'currentLabel': '_-2', 'marker_mc': {'change_txt': {'text': '-2'}}}}}
    >>> events, time = sequence_score('score_mc', news, [], 1000, step = 125, old_value = 2)
    >>> ## pprint(events)
    >>> events[-1]['score_mc']['bar_mc']['currentLabel']
    '_-2'
    >>> events[-1]['score_mc']['bar_mc']['marker_mc']['change_txt']['text']
    '-2'
    >>> events[-2]['score_mc']['bar_mc']['currentLabel']
    '_-1'
    >>> events[-2]['score_mc']['bar_mc']['marker_mc']['change_txt']['text']
    '-1'
    >>> events[-3]['score_mc']['bar_mc']['currentLabel']
    '_0'
    >>> events[-3]['score_mc']['bar_mc']['marker_mc']['change_txt']['text']
    '0'

    Might be no marker.
    >>> news = {'score_mc': {'bar_mc': {'currentLabel': '_-2'}}}
    >>> events, time = sequence_score('score_mc', news, [], 1000, step = 125, old_value = 2)
    >>> ## pprint(events)
    >>> events[-1]['score_mc']['bar_mc']['currentLabel']
    '_-2'
    >>> events[-1]['score_mc']['bar_mc'].get('marker_mc')
    >>> events[-2]['score_mc']['bar_mc']['currentLabel']
    '_-1'
    >>> events[-2]['score_mc']['bar_mc'].get('marker_mc')

    Might be marker without change.
    >>> news = {'score_mc': {'bar_mc': {'currentLabel': '_-2', 'marker_mc': {'currentLabel': 'neutral'}}}}
    >>> events, time = sequence_score('score_mc', news, [], 1000, step = 125, old_value = 2)
    >>> ## pprint(events)
    >>> events[-1]['score_mc']['bar_mc']['currentLabel']
    '_-2'
    >>> events[-1]['score_mc']['bar_mc']['marker_mc']
    {'currentLabel': 'neutral'}
    >>> events[-2]['score_mc']['bar_mc']['currentLabel']
    '_-1'
    >>> events[-2]['score_mc']['bar_mc']['marker_mc']
    {'currentLabel': 'neutral'}
    '''
    child = news.get(child_name)
    if child:
        bar = child.get('bar_mc')
        if bar:
            new_value_label = bar.get('currentLabel')
            if not needs_label or new_value_label:
                if not new_value_label:
                    new_value_label = '_0'
                new_value = int(new_value_label[1:])
                value_log = 'sequence_score: old_value %s, new_value %s' \
                        % (old_value, new_value)
                logging.warn(value_log)
                event = {}
                event[child_name] = news.pop(child_name)
                if old_value < new_value:
                    backwards = 1
                else:
                    backwards = -1
                next_time = time
                final_event = copy.deepcopy(event)
                bar_mc = final_event[child_name]['bar_mc']
                marker_mc = bar_mc.get('marker_mc')
                if marker_mc:
                    change_txt = marker_mc.get('change_txt')
                    if change_txt:
                        final_change = change_txt['text'].strip('+')
                        final_change = int(final_change)
                for intermediate_value in range(old_value, new_value, backwards):
                    intermediate_event = copy.deepcopy(event)
                    next_time += step
                    intermediate_event = upgrade(intermediate_event, 
                            {'time_txt': {'text': str(next_time)}})
                    intermediate_label = '_%i' % intermediate_value
                    bar_mc = intermediate_event[child_name]['bar_mc']
                    bar_mc['currentLabel'] = intermediate_label
                    until = intermediate_value - new_value
                    if marker_mc and change_txt and final_change:
                        difference = final_change + until
                        bar_mc['marker_mc']['change_txt']['text'] \
                                = str(difference)
                    events.append(intermediate_event)
                final_event = copy.deepcopy(event)
                next_time += step
                final_event = upgrade(final_event, 
                        {'time_txt': {'text': str(next_time)}})
                events.append(final_event)
                time = int(events[-1]['time_txt']['text'])
                ## time += step
    return events, time

def sequence_label(origin_name, events, time, step = 250, 
        label = 'black_question_repeat'):
    '''Black stone prompts question.
    >>> news = get_laurens_profit_unsequenced_news()
    >>> events, time = sequence_label('_2_2_mc', [], 1000, step = 250)
    >>> event = events[-1]
    >>> event['_2_2_mc']['currentLabel']
    'black_question_repeat'
    >>> event['time_txt']['text']
    '1250'
    >>> time
    1250

    >>> events, time = sequence_label('_2_2_mc', [], 1000, step = 500,
    ...     label = 'question_hide_black_repeat')
    >>> event = events[-1]
    >>> event['_2_2_mc']['currentLabel']
    'question_hide_black_repeat'
    >>> event['time_txt']['text']
    '1500'
    >>> time
    1500
    '''
    event = {}
    event[origin_name] = {'currentLabel': label}
    event = upgrade(event, {'time_txt': {'text': str(time + step)}})
    events.append(event)
    time = int(events[-1]['time_txt']['text'])
    return events, time


def sequence_cursor(news, events, time):
    '''sequence profit.
        sequence cursor and tutor.
    >>> news = get_laurens_profit_unsequenced_news()
    >>> events, time = sequence_cursor(news, [], 1000)
    >>> event = events[-1]
    >>> event['cursor_mc']['act_mc']['currentLabel']
    'preview'
    '''
    step = 250
    cursor = news.get('cursor_mc')
    if cursor:
        event = {}
        event['cursor_mc'] = news.pop('cursor_mc')
        event = upgrade(event, {'time_txt': {'text': str(time + step)}})
        events.append(event)
        time = int(events[-1]['time_txt']['text'])
    return events, time


def get_laurens_remove_table_news():  
    return \
    {'_0_0_mc': {'block_east_mc': {'currentLabel': 'none'},
                 'block_north_mc': {'currentLabel': 'none'},
                 'block_west_mc': {'currentLabel': 'none'},
                 'currentLabel': 'empty_black',
                 'empty_block_east_mc': {'currentLabel': 'none'},
                 'empty_block_north_mc': {'currentLabel': 'none'},
                 'empty_block_south_mc': {'currentLabel': 'none'},
                 'empty_block_west_mc': {'currentLabel': 'none'}},
     '_0_1_mc': {'block_north_mc': {'currentLabel': 'none'},
                 'block_west_mc': {'currentLabel': 'none'},
                 'currentLabel': 'empty_black',
                 'empty_block_east_mc': {'currentLabel': 'none'},
                 'empty_block_north_mc': {'currentLabel': 'none'},
                 'empty_block_south_mc': {'currentLabel': 'none'},
                 'empty_block_west_mc': {'currentLabel': 'none'}},
     '_0_2_mc': {'empty_block_east_mc': {'currentLabel': 'none'},
                 'empty_block_north_mc': {'currentLabel': 'none'},
                 'empty_block_south_mc': {'currentLabel': 'none'},
                 'empty_block_west_mc': {'currentLabel': 'none'}},
     '_1_0_mc': {'empty_block_east_mc': {'currentLabel': 'none'},
                 'empty_block_north_mc': {'currentLabel': 'none'},
                 'empty_block_south_mc': {'currentLabel': 'none'},
                 'empty_block_west_mc': {'currentLabel': 'none'}},
     '_1_1_mc': {'empty_block_east_mc': {'currentLabel': 'none'},
                 'empty_block_north_mc': {'currentLabel': 'none'},
                 'empty_block_south_mc': {'currentLabel': 'none'},
                 'empty_block_west_mc': {'currentLabel': 'none'}},
     '_1_2_mc': {'empty_block_east_mc': {'currentLabel': 'none'},
                 'empty_block_north_mc': {'currentLabel': 'none'},
                 'empty_block_south_mc': {'currentLabel': 'none'},
                 'empty_block_west_mc': {'currentLabel': 'none'}},
     '_2_0_mc': {'empty_block_east_mc': {'currentLabel': 'none'},
                 'empty_block_north_mc': {'currentLabel': 'none'},
                 'empty_block_south_mc': {'currentLabel': 'none'},
                 'empty_block_west_mc': {'currentLabel': 'none'}},
     '_2_1_mc': {'empty_block_east_mc': {'currentLabel': 'none'},
                 'empty_block_north_mc': {'currentLabel': 'none'},
                 'empty_block_south_mc': {'currentLabel': 'none'},
                 'empty_block_west_mc': {'currentLabel': 'none'}},
     '_2_2_mc': {'empty_block_east_mc': {'currentLabel': 'none'},
                 'empty_block_north_mc': {'currentLabel': 'none'},
                 'empty_block_south_mc': {'currentLabel': 'none'},
                 'empty_block_west_mc': {'currentLabel': 'none'}},
     'currentLabel': 'lobby',
     'game_over_mc': {'_9_9_mc': {'confirm_mc': {'dispatchEvent': 'mouseDown'}},
                      'currentLabel': 'none',
                      'mission_mc': {'currentLabel': 'none'},
                      'white_computer_mc': {'currentLabel': 'none'}},
     'lobby_mc': {'enter_mc': {'currentLabel': 'none'},
                  'join_mc': {'currentLabel': 'none', 'join_txt': {'text': ''}}},
     'menu_mc': {'currentLabel': 'none', 'lobby_mc': {'currentLabel': 'none'}},
     'option_mc': {'block_mc': {'currentLabel': 'none'},
                   'first_capture_mc': {'currentLabel': 'none'},
                   'gibs_mc': {'currentLabel': 'none'},
                   'prohibit_danger_mc': {'currentLabel': 'none'}},
     'sgf_file_txt': {'text': ''},
     'turn_mc': {'black_user_txt': {'text': 'BLACK'},
                 'white_user_txt': {'text': 'WHITE'}},
     'tutor_mc': {'currentLabel': 'none'}}

def validate_pass(news):
    '''Upgrade news to revert pass, if false.
    >>> code_unit.doctest_unit(user_class.do_pass, log = False, verbose = False)
    '''
    if news.has_key('bad_move_mc'):
        bad_move = news.get('bad_move_mc')
        if bad_move:
            if 'show' == bad_move.get('currentLabel'):
                not_pass = {
                    'pass_mc': {'currentLabel': 'none'}
                }
                news = upgrade(news, not_pass)
                return False
    return True


class user_class(user_as.globe_class):
    '''Server-side model of ActionScript client.
    '''
    def __init__(globe):
        '''
        >>> u = user_class()
        >>> u.users
        '''
        user_as.globe_class.__init__(globe)
        # XXX HACK.  object on stage?
        globe.reverted = {}
        globe.news_ok = False
        globe.users = None
        globe.last_send_time = None

    def setup_events(globe):
        user_as.globe_class.setup_events(globe)
        globe.root.option_mc.score_mc.enter_mc.addEventListener(
                MouseEvent.MOUSE_DOWN, globe.toggle_score_mc)

    def toggle_option(globe, mouse_event):
        '''Publish to client a single option switched on or off.
        >>> emmet = setup_echo(user_class)
        >>> emmet.root.suicide_mc.currentLabel
        u'none'
        >>> emmet.root.suicide_mc.enter_mc.currentLabel
        u'none'
        >>> emmet.news_ok
        False
        >>> emmet.root.suicide_mc.enter_mc.dispatchEvent(mouseDown)
        >>> emmet.news_ok
        True
        >>> emmet.root.suicide_mc.currentLabel
        'show'
        >>> emmet.root.suicide_mc.enter_mc.currentLabel
        'none'
        >>> emmet.root.suicide_mc.enter_mc.dispatchEvent(mouseDown)
        >>> emmet.root.suicide_mc.currentLabel
        'none'
        >>> emmet.root.suicide_mc.enter_mc.currentLabel
        'none'

        Toggle score option.
        >>> emmet.root.option_mc.score_mc.currentLabel
        u'none'
        >>> emmet.root.score_mc.currentLabel
        u'none'
        >>> emmet.root.option_mc.score_mc.enter_mc.dispatchEvent(mouseDown)
        >>> emmet.root.option_mc.score_mc.currentLabel
        'show'
        >>> emmet.root.score_mc.currentLabel
        'show'
        >>> emmet.root.option_mc.score_mc.enter_mc.dispatchEvent(mouseDown)
        >>> emmet.root.option_mc.score_mc.currentLabel
        'none'
        '''
        news = globe._toggle_news(mouse_event)
        return globe.publish(news)

    def toggle_menu(globe, mouse_event):
        '''Publish to client a single option switched on or off.
        >>> jade = setup_echo(user_class)
        >>> wait = 0.125 / jade._speed
        >>> jade.news_ok
        False

        Jade toggles menu between open <--> close.
        >>> jade.root.menu_mc.toggle_mc.dispatchEvent(mouseDown)
        >>> time.sleep(wait)
        >>> jade.root.menu_mc.currentLabel
        'show'
        >>> jade.news_ok
        True
        >>> jade.root.menu_mc.toggle_mc.dispatchEvent(mouseDown)
        >>> time.sleep(wait)
        >>> jade.root.menu_mc.currentLabel
        'none'
        >>> jade.root.menu_mc.toggle_mc.dispatchEvent(mouseDown)
        >>> time.sleep(wait)
        >>> jade.root.menu_mc.currentLabel
        'show'
        '''
        return globe.toggle_option(mouse_event)

    def _toggle_news(globe, mouse_event):
        logging.info('toggle_news:  starting')
        option = mouse_event.currentTarget.parent
        news = note(mouse_event.currentTarget, 'currentLabel', 'none')
        toggles = {'none': 'show', 'show': 'none'}
        if option.currentLabel in toggles:
            next = toggles[option.currentLabel]
            toggle_news = note(option, 'currentLabel', next)
            news = upgrade(news, toggle_news)
            globe.news_ok = True
        else:
            what_is_this_label = 'toggle_news: i did not expect %s' \
                    % option.currentLabel
            logging.error(what_is_this_label)
        return news

    def toggle_score_mc(globe, mouse_event):
        news = globe._toggle_news(mouse_event)
        label = news.get('option_mc').get('score_mc').get('currentLabel')
        score_news = {'score_mc': {'currentLabel': label}}
        news = upgrade(news, score_news)
        return globe.publish(news)

    #def problem(globe, mouse_event):
    #    '''DEPRECATED?
    #    >>> from super_users import setup_users
    #    >>> from mock_client import echo_protocol_class
    #    >>> users = setup_users(8.0)
    #    >>> yuji = users.get('yuji')
    #    >>> yuji.ambassador = echo_protocol_class()
    #    >>> yuji.root.lobby_mc._00_mc.capture_3_3_mc.dispatchEvent(mouseDown)
    #    >>> yuji.root.currentLabel
    #    '_3_3'
    #    '''
    #    problem_name = mouse_event.currentTarget.parent.name
    #    from lesson import get_start_problem_file_news 
    #    reply = get_start_problem_file_news(globe.users, globe, problem_name)
    #    globe.news_ok = True
    #    return globe.publish(reply)

    def problem_name(globe, mouse_event):
        r'''Setup the problem.
        >>> from super_users import setup_users
        >>> from mock_client import echo_protocol_class
        >>> users = setup_users(8.0)
        >>> yuji = users.get('yuji')
        >>> yuji.ambassador = echo_protocol_class()
        >>> yuji.root.lobby_mc._00_mc.capture_5_5_mc.dispatchEvent(mouseDown)
        >>> yuji.root.currentLabel
        '_5_5'
        >>> yuji.root.sgf_file_txt.text
        'sgf/beginner/capture_5_5.sgf'

        '''
        ## import pdb; pdb.set_trace();
        problem_mc = mouse_event.currentTarget
        from lesson import get_start_problem_name_news 
        reply = get_start_problem_name_news(globe.users, globe, problem_mc)
        globe.news_ok = True
        return globe.publish(reply)

    def do_pass(globe, mouse_event):
        r'''
        #>>> users = setup_users(8, setup_events = False)
        #>>> h1 = users.get('h1')
        >>> from super_users import setup_users_white_black
        >>> users, h2, h1 = setup_users_white_black('h2', 'h1')
        
        >>> h1.root.sgf_file_txt.text = 'sgf/test_capture_3_3.sgf'
        >>> h1.play_history = [{'size': 3}]
        
        >>> h1.root.bad_move_mc.currentLabel
        'none'
        >>> h1.root.pass_white_mc.currentLabel
        'none'
        >>> h1.root.pass_mc.currentLabel
        'none'
        >>> h1.root.pass_mc.dispatchEvent(mouseDown)
        >>> h1.root.bad_move_mc.currentLabel
        'show'
        >>> h1.root.pass_white_mc.currentLabel
        'none'
        >>> h1.root.pass_mc.currentLabel
        'none'
        >>> from pprint import pprint
        >>> ## pprint(h1.ambassador.sends[-1])

        >>> h1.play_history = [{'size': 3}, {'black': (1, 1)}]
        >>> h1.root.bad_move_mc.currentLabel
        'show'
        >>> h1.root.pass_mc.dispatchEvent(mouseDown)
        >>> h1.root.bad_move_mc.currentLabel
        'none'
        
        '''
        pass_mc = mouse_event.currentTarget
        # follow sgf.  see emmet* yuji_capture_3_3_example:  first move
        pass_dict = {get_color(globe): 'pass'}
        # HACK:  complains if import at global.
        from lesson import update_path
        from super_users import get_author
        author = get_author(globe.users, globe)
        news = update_path(author, None, pass_dict)
        #- partner_news = upgrade(partner_news, path_news)
        # prohibit bad_move
        if not validate_pass(news):
            globe.news_ok = True
            globe.publish(news)
        else:
            if 'show' == globe.root.bad_move_mc.currentLabel:
                globe.root.bad_move_mc.gotoAndPlay('none')
        #reply = _pass_reply(users, user)


    def parent_goto_mc_name(globe, mouse_event):
        '''In lobby, goto single player or multiplayer.
        >>> code_unit.inline_examples(
        ...     globe_class.parent_goto_mc_name.__doc__, 
        ...     locals(), globals(), 
        ...     verify_examples = False)
        >>> jade_user = user_class()
        >>> jade_user.create()
        >>> jade_user.setup_events()
        >>> jade_user.ambassador = echo_protocol_class()
        >>> jade_user.news_ok
        False

        >>> jade_user.revise(multiplayer_news)
        >>> jade_user.root.lobby_mc.currentLabel
        'multiplayer'
        >>> jade_user.root.lobby_mc.multiplayer_mc.currentLabel
        'none'
        >>> multiplayer_reply = jade_user.ambassador.sends[-1]
        >>> pprint(multiplayer_reply.get('lobby_mc'))
        {'currentLabel': 'multiplayer', 'multiplayer_mc': {'currentLabel': 'none'}}
        >>> jade_user.news_ok
        True

        >>> jade_user.revise(single_player_news)
        >>> jade_user.root.lobby_mc.currentLabel
        'single_player'
        >>> jade_user.root.lobby_mc.single_player_mc.currentLabel
        'none'
        >>> single_player_reply = jade_user.ambassador.sends[-1]
        >>> pprint(single_player_reply.get('lobby_mc'))
        {'currentLabel': 'single_player', 'single_player_mc': {'currentLabel': 'none'}}

        grandparent
        >>> jade_user.root.lobby_mc.currentLabel
        'single_player'
        >>> jade_user.root.lobby_mc.main_mc._00_mc.dispatchEvent(mouseDown)
        >>> jade_user.root.lobby_mc.currentLabel
        '_00'

        great grandparent
        >>> jade_user.root.gotoAndPlay('lobby')
        >>> jade_user.root.currentLabel
        'lobby'
        >>> jade_user.root.lobby_mc.main_mc.login_mc.dispatchEvent(mouseDown)
        >>> jade_user.root.currentLabel
        'login'
        '''
        news = _parent_goto_mc_name_news(mouse_event)
        globe.news_ok = True
        globe.publish(news)

    def grandparent_goto_mc_name(globe, mouse_event):
        target = mouse_event.currentTarget.parent.parent
        mouse_mc = mouse_event.currentTarget
        news = _target_goto_mc_name_news(target, mouse_mc)
        globe.news_ok = True
        globe.publish(news)

    def great_grandparent_goto_mc_name(globe, mouse_event):
        target = mouse_event.currentTarget.parent.parent.parent
        mouse_mc = mouse_event.currentTarget
        news = _target_goto_mc_name_news(target, mouse_mc)
        globe.news_ok = True
        globe.publish(news)

    def author_parent_goto_mc_name(globe, mouse_event):
        '''Tell partner same news.
        >>> from super_users import setup_users_white_black
        >>> users, ethan, jade = setup_users_white_black('ethan', 'jade')
        >>> ethan.root.game_over_mc.extra_stone_available_mc._4_mc.dispatchEvent(mouseDown)

        Jade has four extra stones.
        >>> jade.root.game_over_mc.extra_stone_available_mc.currentLabel
        '_4'
        '''
        news = _parent_goto_mc_name_news(mouse_event)
        globe.news_ok = True
        from super_users import get_partner, tell
        partner = get_partner(globe.users, globe)
        tell(partner, news)
        globe.publish(news)

    def adjust_level_balance(globe, mouse_event):
        '''Adjust level balance. 
        >>> from super_users import setup_users_white_black
        >>> users, steven, ethan = setup_users_white_black('steven', 'ethan')
        >>> ethan.root.game_over_mc.balance_mc.black_level_txt.text
        '0'
        >>> steven.root.game_over_mc.balance_mc.black_level_txt.text
        '0'
        >>> ethan.root.game_over_mc.balance_mc.white_level_txt.text
        '0'
        >>> steven.root.game_over_mc.balance_mc.white_level_txt.text
        '0'
        >>> ethan.root.game_over_mc.extra_stone_available_mc.currentLabel
        '_0'
        >>> ethan.root.level_mc._txt.text
        '40'
        >>> steven.root.level_mc._txt.text
        '50'
        >>> ethan.root.option_mc.computer_pass_mc.gotoAndPlay('show')
        >>> ethan.root.option_mc.first_capture_mc.gotoAndPlay('none')

        >>> ethan.root.game_over_mc.hide_available_mc._2_mc.dispatchEvent(mouseDown)

        Both see Ethan has two hide available.
        >>> ethan.root.game_over_mc.hide_available_mc.currentLabel
        '_2'
        >>> steven.root.game_over_mc.hide_available_mc.currentLabel
        '_2'

        Both see level balance.
        >>> ethan.root.game_over_mc.balance_mc.black_level_txt.text
        '53'
        >>> steven.root.game_over_mc.balance_mc.black_level_txt.text
        '53'
        >>> ethan.root.game_over_mc.balance_mc.white_level_txt.text
        '50'
        >>> steven.root.game_over_mc.balance_mc.white_level_txt.text
        '50'
        
        >>> ethan.root.game_over_mc.hide_available_mc._3_mc.dispatchEvent(mouseDown)
        >>> ethan.root.game_over_mc.hide_available_mc.currentLabel
        '_3'
        >>> steven.root.game_over_mc.hide_available_mc.currentLabel
        '_3'

        Both see level balance.
        >>> ethan.root.game_over_mc.balance_mc.black_level_txt.text
        '55'
        >>> steven.root.game_over_mc.balance_mc.black_level_txt.text
        '55'
        >>> ethan.root.game_over_mc.balance_mc.white_level_txt.text
        '50'
        >>> steven.root.game_over_mc.balance_mc.white_level_txt.text
        '50'

        Lower
        >>> ethan.root.game_over_mc.hide_available_mc._1_mc.dispatchEvent(mouseDown)
        >>> ethan.root.game_over_mc.hide_available_mc.currentLabel
        '_1'
        >>> steven.root.game_over_mc.hide_available_mc.currentLabel
        '_1'

        Both see level balance.
        >>> ethan.root.game_over_mc.balance_mc.black_level_txt.text
        '51'
        >>> steven.root.game_over_mc.balance_mc.black_level_txt.text
        '51'
        >>> ethan.root.game_over_mc.balance_mc.white_level_txt.text
        '50'
        >>> steven.root.game_over_mc.balance_mc.white_level_txt.text
        '50'
        '''
        from super_users import get_author, get_partner, tell
        news = _parent_goto_mc_name_news(mouse_event)
        olds = imitate_news(globe.root, news)
        partner = get_partner(globe.users, globe)
        olds = imitate_news(partner.root, news)
        black = get_author(globe.users, globe)
        white = get_partner(globe.users, black)
        level_news = adjust_level_balance_news(black, white)
        news = upgrade(news, level_news)
        globe.news_ok = True
        partner = get_partner(globe.users, globe)
        tell(partner, news)
        globe.publish(news)
        #- return globe.author_parent_goto_mc_name(mouse_event)

    def remove_table(globe, mouse_event):
        '''Root go to name of button.  Reset menu and button.  
        Clear table.
        >>> from super_users import setup_users_white_black
        >>> users, ethan, jade = setup_users_white_black('ethan', 'jade')

        Pretend Jade is at table with menu open.
        >>> jade.root._0_0_mc.gotoAndPlay('black')
        >>> jade.root.gotoAndPlay('_3_3')
        >>> jade.root.menu_mc.gotoAndPlay('show')

        From menu, Jade goes to lobby.
        >>> jade.root.menu_mc.lobby_mc.dispatchEvent(mouseDown)
        >>> jade.root.menu_mc.currentLabel
        'none'
        >>> jade.root.currentLabel
        'lobby'
        >>> jade.root.menu_mc.lobby_mc.currentLabel
        'none'

        Table is clear.
        >>> jade.root._0_0_mc.currentLabel
        'empty_black'
        >>> jade.play_history
        []
        >>> jade.board_history
        []

        Pretend marije is at table with menu open.
        >>> marije = jade
        >>> marije.root._0_0_mc.gotoAndPlay('black')
        >>> marije.root.gotoAndPlay('_3_3')
        >>> marije.root.menu_mc.gotoAndPlay('show')

        From menu, marije goes to lobby.
        >>> marije.root.game_over_mc.score_mc.lobby_mc.dispatchEvent(mouseDown)
        >>> marije.root.menu_mc.currentLabel
        'none'
        >>> marije.root.currentLabel
        'lobby'
        >>> marije.root.menu_mc.lobby_mc.currentLabel
        'none'

        Table is clear.
        >>> marije.root._0_0_mc.currentLabel
        'empty_black'
        >>> marije.play_history
        []
        >>> marije.board_history
        []
        '''
        button = mouse_event.currentTarget
        news = _target_goto_mc_name_news(button.root, button)
        #grandparent = button.parent.parent
        #news = _target_goto_mc_name_news(grandparent, button)
        globe.news_ok = True
        from super_users import _remove_table
        remove_news = _remove_table(globe.users, globe)
        news = upgrade(news, remove_news)
        #partner = get_partner(globe.users, globe)
        #tell(partner, news)
        globe.publish(news)

    def chat_input(globe, mouse_event):
        '''Broadcast user name and chat text to users logged in.
        >>> from super_users import setup_users_white_black, set_partner
        >>> users, ethan, jade = setup_users_white_black('ethan', 'jade')
        >>> lukasz = users.get('lukasz')
        >>> lukasz.ambassador = echo_protocol_class()
        >>> jade.news_ok
        False

        Input may be updated out of order, so current state must include news.
        >>> jade.current['chat_input_txt'] = {'text': 'hello'}
        >>> jade.current['chat_input_mc'] = {'currentLabel': 'enter', 'dispatchEvent': 'mouseDown'}
        >>> jade.root.chat_input_txt.text = 'hello'
        >>> jade.root.chat_input_mc.dispatchEvent(mouseDown)
        >>> jade.root.comment_mc.currentLabel
        'comment'
        >>> jade.root.comment_mc._txt.text
        'jade: hello'
        >>> jade.root.chat_input_txt.text
        ''
        >>> ethan.root.comment_mc.currentLabel
        'comment'
        >>> ethan.root.comment_mc._txt.text
        'jade: hello'
        >>> jade.root.chat_input_mc.currentLabel
        'none'

        Do not ask client to repeat input.
        >>> jade.ambassador.sends[-1]['chat_input_mc'].get('dispatchEvent')
        >>> jade.news_ok
        True

        Processing may occur out of order.
        >>> jade.news_ok = False
        >>> jade.current['chat_input_txt'] = {'text': 'hello'}
        >>> jade.current['chat_input_mc'] = {'currentLabel': 'enter', 'dispatchEvent': 'mouseDown'}
        >>> jade.root.chat_input_mc.dispatchEvent(mouseDown)
        >>> jade.root.chat_input_txt.text = 'hello'
        >>> jade.root.comment_mc.currentLabel
        'comment'
        >>> jade.root.comment_mc._txt.text
        'jade: hello'
        >>> jade.news_ok
        True

        When out of order, server input differs from client input.
        >>> jade.root.chat_input_txt.text
        'hello'
        
        >>> jade.root.chat_input_mc.currentLabel
        'none'
        >>> ethan.root.comment_mc.currentLabel
        'comment'
        >>> ethan.root.comment_mc._txt.text
        'jade: hello'
        >>> lukasz.root.comment_mc.currentLabel
        'comment'
        >>> lukasz.root.comment_mc._txt.text
        'jade: hello'
        '''
        #chat_message = globe.ambassador.receives[-1]['chat_input_txt']['text']
        chat_message = globe.current['chat_input_txt']['text']
        username = globe.root.title_mc.username_txt.text
        chat_text = '%s: %s' % (username, chat_message)
        chat_news = {
            'comment_mc': {
                'currentLabel': 'comment',
                '_txt': {
                    'text': chat_text
                }
            }
        }
        from super_users import tell, get_partner
        # partner = get_partner(globe.users, globe)
        # tell(partner, chat_news)
        tolds = []
        for other in globe.users.values():
            if other.ambassador and other != globe and other not in tolds:
                tell(other, chat_news)
                tolds.append(other)
        chat_news['chat_input_txt'] = {'text': ''}
        chat_news['chat_input_mc'] = {'currentLabel': 'none'}
        globe.news_ok = True
        globe.publish(chat_news)

    def publish(globe, news, reverted = {}):
        '''publish and sequence events
        Optionally revert, after the sequence.
        server publish news and reverted
            if any reverted:
                clear sequence
                    send sequence []
            instead of upgrade reverted before sequence, 
            update reverted after sequence.
        client push news
            if receive sequence []:
                remove all sequenced events.
        >>> moonhyoung = user_class()
        >>> moonhyoung.create()
        >>> moonhyoung.ambassador = echo_protocol_class()
        >>> reverted = note(moonhyoung.root._1_1_mc.decoration_mc, 
        ...     'currentLabel', 'none')
        >>> reverted = upgrade(reverted, note(moonhyoung.root._2_2_mc.decoration_mc, 
        ...     'currentLabel', 'none'))
        >>> reverted = upgrade(reverted, note(moonhyoung.root._3_3_mc.black_shape_mc, 
        ...     'currentLabel', '_0000'))
        >>> news = note(moonhyoung.root._3_3_mc, 
        ...     'currentLabel', 'question_black')
        >>> news = upgrade(news, note(moonhyoung.root._2_2_mc.decoration_mc, 
        ...     'currentLabel', 'black_defend'))
        >>> news = upgrade(news, note(moonhyoung.root._3_3_mc.black_shape_mc, 
        ...     'currentLabel', '_0001'))
        >>> moonhyoung.root.title_mc.time_txt.text
        '0'
        >>> previous = {'title_mc': {'time_txt': {'text': '250'}}}
        >>> reverted = upgrade(reverted, previous)
        >>> moonhyoung.publish(news, reverted = reverted)
        >>> sent = moonhyoung.ambassador.sends[-1]
        >>> sequence = sent['sequence']

        Upon receiving first event with sequence key, 
        client clears the preceding sequence.
        When I revert the client, I also clear the old sequence.
        >>> sequence[0]['sequence']
        []
        >>> sequence[1].get('sequence')
        >>> sequence[1]['_3_3_mc']['currentLabel']
        'question_black'
        >>> ## sequence

        The reverted portion also goes directly into the news,
        >>> sent['_2_2_mc']['decoration_mc']['currentLabel']
        'none'

        Reverted may later be overwritten by the sequence.
        >>> sequence[2]['_2_2_mc']['decoration_mc']['currentLabel']
        'black_defend'

        Even if reverting, timestamp advances until after sequence.
        >>> moonhyoung.root.title_mc.time_txt.text
        '2000'

        Unsequenced news overwrites reverted immediately.
        >>> sent['_3_3_mc']['black_shape_mc']['currentLabel']
        '_0001'

        If no sequence, revert still clears.
        >>> moonhyoung.root.currentLabel
        'setup'
        >>> moonhyoung.publish({}, reverted = {'currentLabel': 'lobby'})
        >>> sent = moonhyoung.ambassador.sends[-1]
        >>> sequence = sent['sequence']
        >>> moonhyoung.root.currentLabel
        'lobby'
        >>> moonhyoung.olds_list[-1]['currentLabel']
        'setup'

        If entering lobby, update disabled.
        >>> laurens = moonhyoung
        >>> laurens.root.lobby_mc._20_mc.hide_9_9_mc.disabled_mc.currentLabel
        'show'
        >>> laurens.ambassador.sends[-1]['lobby_mc']['_20_mc']['hide_9_9_mc']['disabled_mc']['currentLabel']
        'show'

        If reverted not specified, but user has reverted, 
        revert that and clear user reverted.
        >>> moonhyoung.reverted = {'currentLabel': 'table'} 
        >>> moonhyoung.publish({})
        >>> sent = moonhyoung.ambassador.sends[-1]
        >>> sent['currentLabel']
        'table'
        >>> moonhyoung.reverted
        {}
        >>> moonhyoung.root.currentLabel
        'table'
        >>> moonhyoung.olds_list[-1]
        {'currentLabel': 'lobby'}

        If reverting and reverted state already exists, do no save reverted.
        Thus, preview mode is not prematurely halted while reverting.
        >>> marije = moonhyoung
        >>> marije.root.cursor_mc.act_mc.gotoAndPlay('preview')
        >>> marije.reverted = {'_1_1_mc': {'currentLabel': 'preview_black'}, 'cursor_mc': {'act_mc': {'currentLabel': 'preview'}}}
    
        To avoid packet collision between server and Flash client's socket:
        Before send, wait 0.25 second
        >>> import time
        >>> before = time.clock()
        >>> marije.publish({})
        >>> marije.olds_list[-1]
        {'_1_1_mc': {'currentLabel': 'empty_black'}}
        >>> marije.publish({})

        Before send, wait 0.25 second
        Yet while testing without network, speed up.
        >>> duration = time.clock() - before
        >>> import config
        >>> defaults = config.setup_defaults()
        >>> configuration = config.borg(defaults)
        >>> delay = 0.25 / configuration.mock_speed
        >>> if not delay <= duration:  print delay, round(duration, 4)

        Sequence refers to old value.
        >>> moonhyoung.root.score_mc.bar_mc.gotoAndPlay('_-21')
        >>> news = {'score_mc': {'bar_mc': {'currentLabel': '_4', 'marker_mc': {'change_txt': {'text': '+25'}}}}}
        >>> moonhyoung.publish(news)
        >>> sent = moonhyoung.ambassador.sends[-1]
        >>> sent['sequence'][-1]['score_mc']['bar_mc']['currentLabel']
        '_4'
        >>> sent['sequence'][-1]['score_mc']['bar_mc']['marker_mc']['change_txt']['text']
        '+25'
        >>> sent['sequence'][-2]['score_mc']['bar_mc']['currentLabel']
        '_3'
        >>> sent['sequence'][-2]['score_mc']['bar_mc']['marker_mc']['change_txt']['text']
        '24'
     
        '''
        if not reverted:
            if globe.reverted:
                reverted = globe.reverted
                globe.reverted = {}
        #if reverted:
        #    globe.revise(reverted)
        if 'lobby' == news.get('currentLabel') or 'lobby' == reverted.get('currentLabel'):
            from super_users import update_disable_menu_news
            black_level = int(globe.root.level_mc._txt.text)
            news = upgrade(news, 
                update_disable_menu_news(black_level, globe.root.lobby_mc) )
        server_reverted = copy.deepcopy(reverted)
        server_news = copy.deepcopy(news)
        server_news = upgrade(server_reverted, server_news)
        sequence_time_news = globe.sequence_events(news)
        server_news = upgrade(server_news, sequence_time_news)
        globe.revise(server_news)
        #- olds = imitate_news(globe.root, reverted) #-
        #- globe.revise(news) #-
        if reverted:
            news = upgrade(reverted, news)
            if not news.has_key('sequence'):
                news['sequence'] = []
            news['sequence'].insert(0, {'sequence': []})
        my_news = globe.insert_credentials(news)
        now = time.time()
        if globe.last_send_time:
            interval = now - globe.last_send_time
            import config
            defaults = config.setup_defaults()
            configuration = config.borg(defaults)
            nap = (0.25 / configuration.mock_speed) - interval
            if 0 < nap:
                nap_log = 'publish:  sleep %s' % nap
                logging.warn(nap_log)
                ## print nap_log
                time.sleep(nap)
        globe.last_send_time = time.time()
        ## globe.last_send_time = now
        # debug = False
        debug = False
        if debug:
            from pprint import pformat
            pp_news = pformat(my_news)
            news_log = '%s.publish:  %s' % (globe.root.title_mc.username_txt.text,
                    pp_news)
            logging.warn(news_log)
        globe.ambassador.send(my_news)
   
    def sequence_events(globe, news):
        '''Convert untimed build bunker event to timed event.
        >>> moonhyoung = user_class()
        >>> moonhyoung.create()
        >>> moonhyoung.root.title_mc.time_txt.text = '1000'
        
        >>> news = note(moonhyoung.root._3_3_mc, 'currentLabel', 'question_black')
        >>> news['_3_3_mc']['currentLabel']
        'question_black'
        >>> moonhyoung.sequence_events(news)
        {'title_mc': {'time_txt': {'text': '2750'}}}
        >>> news['sequence'][0]['time_txt']['text']
        '2000'
        >>> news['sequence'][0]['_3_3_mc']['currentLabel']
        'question_black'
        >>> news.get('_3_3_mc')
        
        After scheduling, set time to 1 second after last event.
        >>> news['sequence'][-1]['time_txt']['text']
        '2250'
        >>> moonhyoung.root.title_mc.time_txt.text
        '2750'

        Ignore no events to sequence.
        >>> news = {}
        >>> moonhyoung.sequence_events(news)
        {}
        >>> news
        {}
        >>> news = get_laurens_remove_table_news()
        >>> moonhyoung.sequence_events(news)
        {'title_mc': {'time_txt': {'text': '4500'}}}
        >>> news.get('sequence')[0]['tutor_mc']
        {'currentLabel': 'none'}

        Ignore unsequenced events.
        >>> news = note(moonhyoung.root.menu_mc, 'currentLabel', 'none')
        >>> moonhyoung.sequence_events(news)
        {}
        >>> news.get('sequence')
        >>> news
        {'menu_mc': {'currentLabel': 'none'}}
        
        Ignore unsequenced intersection events.
        >>> moonhyoung.root.title_mc.time_txt.text = '4000'
        >>> news = note(moonhyoung.root._3_3_mc, 'currentLabel', 'question_black')
        >>> news = upgrade(news, note(moonhyoung.root._3_3_mc.black_shape_mc, 'currentLabel', '_0001') )
        >>> news = upgrade(news, note(moonhyoung.root._0_0_mc.black_shape_mc, 'currentLabel', '_0000') )
        >>> news['_3_3_mc']['currentLabel']
        'question_black'
        >>> moonhyoung.sequence_events(news)
        {'title_mc': {'time_txt': {'text': '5750'}}}

        After scheduling, set time to half second after last event.
        >>> news['sequence'][-1]['time_txt']['text']
        '5250'
        >>> ## news['sequence'][-1]
        >>> ## news['sequence']
        >>> moonhyoung.root.title_mc.time_txt.text
        '5750'
        >>> news['sequence'][0]['_3_3_mc']['currentLabel']
        'question_black'
        >>> news['sequence'][0]['_3_3_mc'].get('black_shape_mc')
        >>> news['sequence'][0].get('_0_0_mc')
        >>> news.get('_3_3_mc').get('currentLabel')
        >>> news['_3_3_mc']['black_shape_mc']['currentLabel']
        '_0001'
        >>> news['_0_0_mc']['black_shape_mc']['currentLabel']
        '_0000'

        Repeat question
        >>> news['sequence'][-1]['_3_3_mc']['currentLabel']
        'question_black_repeat'

        sequence profit.
        >>> laurens = user_class()
        >>> laurens.create()
        >>> laurens.root.title_mc.time_txt.text = '1000'
        >>> news = get_laurens_profit_unsequenced_news()
        >>> laurens.sequence_events(news)
        {'title_mc': {'time_txt': {'text': '6992'}}}
        >>> event = news['sequence'][7]
        >>> from pprint import pprint
        >>> # pprint(news['sequence'])
        >>> ## pprint(event)
        >>> shape = event['_2_2_mc']['black_shape_mc']
        >>> shape['defend_mc']['profit_mc']['currentLabel']
        'show'

        sequence cursor after stone and progress.
        >>> event = news['sequence'][1]
        >>> event['cursor_mc']['act_mc']['currentLabel']
        'preview'
        >>> ## pprint(news['sequence'])

        after the above is question_black_repeat
        with some preceding animation.
        expect long delay until after preceding.
        without.
        expect short delay.
        >>> news['sequence'][8]['_2_2_mc']['currentLabel']
        'question_black_repeat'

        sequence tutor.
        >>> last_event = news['sequence'][-1]
        >>> ## pprint(last_event)
        >>> last_event['tutor_mc']['currentLabel']
        'question'

        question_hide_black
        >>> news = get_laurens_profit_unsequenced_news()
        >>> news['_2_2_mc']['currentLabel'] = 'question_hide_black'
        >>> from pprint import pprint
        >>> ## pprint(news)
        >>> laurens.sequence_events(news)
        {'title_mc': {'time_txt': {'text': '12984'}}}
        >>> # pprint(news['sequence'])
        >>> event = news['sequence'][8]
        >>> ## pprint(event)
        >>> event['_2_2_mc']['currentLabel']
        'question_hide_black_repeat'
        
        TODO:  after the above is comment.   
        >>> news = get_laurens_profit_unsequenced_news()
        >>> news['comment_mc'] = {'currentLabel': 'comment'}
        >>> laurens.sequence_events(news)
        {'title_mc': {'time_txt': {'text': '19476'}}}
        >>> event = news['sequence'][-1]
        >>> event['comment_mc']['currentLabel']
        'comment'
        >>> ## pprint(news['sequence'])

        Sequence empty_block.  do not sequence black question repeat.
        >>> news = {'_3_2_mc': {'currentLabel': 'white'}, '_2_2_mc': {'empty_block_south_mc': {'currentLabel': 'white'}}}
        >>> laurens.sequence_events(news)
        {'title_mc': {'time_txt': {'text': '21226'}}}
        >>> ## news['sequence']
        >>> intersection = news['sequence'][1]['_2_2_mc']
        >>> intersection['empty_block_south_mc']['currentLabel']
        'white'

        Sequence turn veil.  Then sequence score, and so on.
        >>> news = {'turn_mc': {'currentLabel': 'black'}, 'turn_veil_mc': {'currentLabel': 'you'}}
        >>> score_news = {'score_mc': {'bar_mc': {'currentLabel': '_4', 'marker_mc': {'change_txt': {'text': '4'}}}}}
        >>> news = upgrade(news, score_news)
        >>> time_news = laurens.sequence_events(news)
        >>> news['sequence'][0]['turn_veil_mc']['currentLabel']
        'you'
        >>> news['sequence'][1]['turn_mc']['currentLabel']
        'black'
        >>> news['sequence'][-1]['score_mc']['bar_mc']['currentLabel']
        '_4'
        >>> ## pprint(news['sequence'])
        
        HACK:  Does later square 'show' overwrites 'none'?

        If clear sequence, retain that in first place.
        >>> news = {'turn_mc': {'currentLabel': 'black'}, 'turn_veil_mc': {'currentLabel': 'you'}}
        >>> news['sequence'] = [{'sequence': []}]
        >>> time_new = laurens.sequence_events(news)
        >>> news['sequence'][0]
        {'sequence': []}
        >>> news['sequence'][-1]['turn_mc']['currentLabel']
        'black'

        If False sequence in news, do not sequence.
        >>> robby = laurens
        >>> news = {'turn_mc': {'currentLabel': 'black'}, 'turn_veil_mc': {'currentLabel': 'you'}}
        >>> news['sequence'] = False
        >>> robby.sequence_events(news)
        {}
        >>> news.get('sequence')

        Careful, False sequence is removed.
        If sequence twice, sequence appears.
        >>> time_news = robby.sequence_events(news)
        >>> news['sequence'][-1]['turn_mc']['currentLabel']
        'black'

        Sequence score, one point at a time.
        Removes '+' prefix from intermediate values.
        >>> moonhyoung = laurens
        >>> moonhyoung.root.score_mc.bar_mc.gotoAndPlay('_-21')
        >>> news = {'score_mc': {'bar_mc': {'currentLabel': '_4', 'marker_mc': {'change_txt': {'text': '+25'}}}}}
        >>> time_news = moonhyoung.sequence_events(news)
        >>> ## pprint(news['sequence'])
        >>> news['sequence'][-1]['score_mc']['bar_mc']['currentLabel']
        '_4'
        >>> news['sequence'][-1]['score_mc']['bar_mc']['marker_mc']['change_txt']['text']
        '+25'
        >>> news['sequence'][-2]['score_mc']['bar_mc']['currentLabel']
        '_3'
        >>> news['sequence'][-2]['score_mc']['bar_mc']['marker_mc']['change_txt']['text']
        '24'
        >>> news['sequence'][-6]['score_mc']['bar_mc']['currentLabel']
        '_-1'
        >>> news['sequence'][-6]['score_mc']['bar_mc']['marker_mc']['change_txt']['text']
        '20'

        Warning:  for large score, makes a long list and so makes large data
        >>> len(news['sequence'])
        26
        >>> if not 1000 < len(str(news['sequence'])):
        ...     len(str(news['sequence']))

        start progress appears after stone
        >>> rene = user_class()
        >>> rene.create()
        >>> rene.root.title_mc.time_txt.text = '1000'
        >>> news = {'_1_1_mc': {'currentLabel': 'black', 'progress_mc': {'currentLabel':  'black_start'}}}
        >>> time_news = rene.sequence_events(news)
        >>> news['sequence'][0]['time_txt']['text']
        '2000'
        >>> news['sequence'][0]['_1_1_mc']['currentLabel']
        'black'
        >>> news['sequence'][1]['time_txt']['text']
        '2000'
        >>> news['sequence'][1]['_1_1_mc']['progress_mc']['currentLabel']
        'black_start'

        sequence complete progress after your turn begins
        >>> news = {'_1_1_mc': {'progress_mc': {'currentLabel':  'black_complete'}}, 'turn_mc': {'currentLabel': 'black'}}
        >>> rene.root.title_mc.time_txt.text = '2000'
        >>> time_news = rene.sequence_events(news)
        >>> news['sequence'][0]['time_txt']['text']
        '2125'
        >>> news['sequence'][0]['turn_mc']['currentLabel']
        'black'
        >>> news['sequence'][1]['time_txt']['text']
        '2125'
        >>> news['sequence'][1]['_1_1_mc']['progress_mc']['currentLabel']
        'black_complete'
        >>> ## pprint(news['sequence'])
        
        '''
        time = int(globe.root.title_mc.time_txt.text)
        if 'sequence' in news:
            if False is news['sequence']:
                news.pop('sequence')
                return {}
            else:
                events = news['sequence']
        else:
            events = []
        intersection_names = get_intersection_names(
                globe.intersection_mc_array)
        events, time, origin_name = sequence_stone(
                news, events, time, intersection_names)
        if origin_name:
            origin_event = events[-1]
        events, time = sequence_progress(news, events, time, 
                intersection_names, '_start')
        # XXX UNTESTED: if next message is unsequenced 
        # it may play before previous message.
        events, time = sequence_child('cursor_mc', news, events, time, 
                step = 62)
                # step = 125) # too slow?
                # step = 250) too slow?
        events, time = sequence_child('turn_veil_mc', news, events, time, 
                step = 62, needs_label = True)
                # step = 500, needs_label = True) # too slow?
                # step = 1000, needs_label = True) # too slow?
        events, time = sequence_child('turn_mc', news, events, time, 
                step = 62, needs_label = True)
                # step = 125, needs_label = True) # too slow?
        events, time = sequence_progress(news, events, time, 
                intersection_names, '_complete') 
        if origin_name:
            origin_label = origin_event[origin_name]['currentLabel']
            events, time = sequence_wave('square_mc', news, events, time, 
                intersection_names, origin_name, label_name = 'none')
            events, time = sequence_wave('top_move_mc', news, events, time, 
                intersection_names, origin_name, label_name = 'none')
            events, time = sequence_direction(news, events, time, 
                intersection_names, origin_name, '_mc', 'empty_block_')
            events, time = sequence_wave('decoration_mc', news, events, time, 
                intersection_names, origin_name)
            events, time = sequence_direction(news, events, time, 
                intersection_names, origin_name, '_strike_mc', 
                step = 125)
                # step = 250) # too slow?
            events, time = sequence_direction(news, events, time, 
                intersection_names, origin_name, '_mc', 'block_', 
                step = 125)
                # step = 250) # too slow?
            events, time = sequence_wave('gibs_mc', news, events, time, 
                intersection_names, origin_name)
            events, time = sequence_wave('dragon_status_mc', news, events, 
                    time, intersection_names, origin_name)
            events, time = sequence_wave('top_move_mc', news, events, time, 
                intersection_names, origin_name, label_name = 'white')
            events, time = sequence_wave('territory_mc', news, events, time, 
                intersection_names, origin_name)
            # time += 500
            events, time = sequence_profit(news, events, time, origin_name)
            events, time = sequence_child('extra_stone_gift_mc', news, events, time)
            events, time = sequence_child('hide_gift_mc', news, events, time)
            repeats = {'question_black': 'question_black_repeat',
                 'question_hide_black': 'question_hide_black_repeat'}
            if origin_label in repeats:
                events, time = sequence_label(origin_name, events, time, 
                    label = repeats[origin_label])
            events, time = sequence_wave('top_move_mc', news, events, time, 
                intersection_names, origin_name, label_name = 'black')
            #events, time = sequence_wave('square_mc', news, events, time, 
            #    intersection_names, origin_name)
            events, time = sequence_wave('square_mc', news, events, time, 
                intersection_names, origin_name, label_name = 'show')
            # HACK:  Does later square 'show' overwrites 'none'?
            #events, time = sequence_wave('square_mc', news, events, time, 
            #    intersection_names, origin_name, label_name = 'show')
            events, time = sequence_wave('last_move_mc', news, events, time, 
                    intersection_names, origin_name)
        old_score = int(globe.root.score_mc.bar_mc.currentLabel[1:])
        events, time = sequence_score('score_mc', news, events, time, 
                step = 1000/24, old_value = old_score) # too slow?
                # step = 1000/12, old_value = old_score) # too slow?
        ## XXX UNTESTED: if next message is unsequenced 
        ## it may play before previous message.
        #events, time = sequence_child('cursor_mc', news, events, time, 
        #        step = 125)
        #        # step = 250) too slow?
        #events, time = sequence_child('turn_veil_mc', news, events, time, 
        #        step = 500, needs_label = True)
        #        # step = 1000, needs_label = True) # too slow?
        #events, time = sequence_child('turn_mc', news, events, time, 
        #        step = 125, needs_label = True)
        #events, time = sequence_progress(news, events, time, 
        #        intersection_names, '_complete') 
        if 'tutor_mc' in news or 'comment_mc' in news:
            time += 125
            # time += 250 # too slow?
            # time += 500 # too slow?
            events, time = sequence_child('tutor_mc', news, events, time, 
                    step = 125)
                    # step = 500) # too slow?
            events, time = sequence_child('comment_mc', news, events, time, 
                    step = 125)
                    # step = 500) # too slow?
        events, time = sequence_child('game_over_mc', news, events, time, 
                step = 500)
        events, time = sequence_child('level_mc', news, events, time, 
                step = 500)
        if events:
            news['sequence'] = events
            time += 125
            # time += 500 # too slow?
            globe.root.title_mc.time_txt.text = str(time)
            return {'title_mc': {'time_txt': {'text': str(time)}}}
        else:
            return {}

# Single user algorithms



# See overlays and get gifts.
def get_observant_news():
    '''copy dictionary so as not to corrupt during upgrade.'''
    return {
        'option_mc': {
            'empty_block_mc': {'currentLabel': 'none'},
            'first_capture_mc': {'currentLabel': 'none'},
            'prohibit_danger_mc': {'currentLabel': 'none'},
            'block_mc': {'currentLabel': 'show'},
            'gibs_mc': {'currentLabel': 'show'},
            'score_mc': {'currentLabel': 'show'},
            'computer_pass_mc': {'currentLabel': 'show'},
            },
        # 'liberty_mc': {'currentLabel': 'show'},
        'territory_mc': {'currentLabel': 'show'},
        'suicide_mc': {'currentLabel': 'show'},
        'strike_mc': {'currentLabel': 'show'},
        'profit_mc': {'currentLabel': 'show'},
        'dead_mc': {'currentLabel': 'show'},
        'defend_mc': {'currentLabel': 'show'},
        'attack_mc': {'currentLabel': 'show'},
        'top_move_mc': {'currentLabel': 'show'},
        'decoration_mc': {'currentLabel': 'show'},
        'critical_mc': {'currentLabel': 'show'},
        'unconditional_status_mc': {'currentLabel': 'none'},
        'connected_mc': {'currentLabel': 'show'},
        'extra_stone_mc': {'currentLabel': 'gift'},
        'hide_mc': {'currentLabel': 'gift'},
    }

def become_observant(joris):
    '''See overlays and get gifts.
    '''
    olds = imitate_news(joris.root, get_observant_news())

def get_aware_news():
    return {
        'option_mc': {
            'empty_block_mc': {'currentLabel': 'none'},
            'prohibit_danger_mc': {'currentLabel': 'none'},
            'block_mc': {'currentLabel': 'show'},
            'gibs_mc': {'currentLabel': 'show'},
            },
        'liberty_mc': {'currentLabel': 'none'},
    }


def get_expert_news():
    return {
        'option_mc': {
            'empty_block_mc': {'currentLabel': 'none'},
            'first_capture_mc': {'currentLabel': 'none'},
            'prohibit_danger_mc': {'currentLabel': 'none'},
            'block_mc': {'currentLabel': 'none'},
            'gibs_mc': {'currentLabel': 'none'},
            'score_mc': {'currentLabel': 'none'},
            'computer_pass_mc': {'currentLabel': 'show'},
            },
        # 'liberty_mc': {'currentLabel': 'none'},
        'territory_mc': {'currentLabel': 'none'},
        'suicide_mc': {'currentLabel': 'none'},
        'strike_mc': {'currentLabel': 'none'},
        'profit_mc': {'currentLabel': 'none'},
        'dead_mc': {'currentLabel': 'none'},
        'defend_mc': {'currentLabel': 'none'},
        'attack_mc': {'currentLabel': 'none'},
        'top_move_mc': {'currentLabel': 'none'},
        'decoration_mc': {'currentLabel': 'none'},
        'critical_mc': {'currentLabel': 'none'},
        'unconditional_status_mc': {'currentLabel': 'none'},
        'connected_mc': {'currentLabel': 'none'},
        'extra_stone_mc': {'currentLabel': 'none'},
        'hide_mc': {'currentLabel': 'none'},
    }
    




def get_white_computer_news(user):
    '''computer plays white.  or turn off.
    >>> emmet = user_class()
    >>> emmet.create(1)
    >>> news = get_white_computer_news(emmet)
    >>> news.get('game_over_mc').get('white_computer_mc').get('currentLabel')
    'computer'
    >>> emmet.root.game_over_mc.white_computer_mc.gotoAndPlay('computer')
    >>> news = get_white_computer_news(emmet)
    >>> news.get('game_over_mc').get('white_computer_mc').get('currentLabel')
    'none'

    reset button.
    >>> news['game_over_mc']['white_computer_mc']['enter_mc']['currentLabel']
    'none'
    
    '''
    current = user.root.game_over_mc.white_computer_mc.currentLabel
    toggles = {'none': 'computer', 'computer': 'none'}
    reply = {
        'game_over_mc': {
            'white_computer_mc': {
                'currentLabel': toggles[current],
                'enter_mc': {
                    'currentLabel': 'none'
                }
            }
        }
    }
    return reply

def is_previewing(user):
    '''cursor or intersection is preview
    >>> user = user_as.globe_class()
    >>> user.create(1)
    >>> is_previewing(user)
    False
    >>> user.root.cursor_mc.act_mc.gotoAndPlay('preview')
    >>> is_previewing(user)
    False
    >>> user.root.cursor_mc.act_mc.gotoAndPlay('none')

    Update olds_list to enable reverting
    >>> news = {'cursor_mc': {'act_mc': {'currentLabel': 'start_preview'}}, '_0_0_mc': {'currentLabel': 'preview_black'}}
    >>> user.revise(news) 
    >>> is_previewing(user)
    False
    >>> news = {'cursor_mc': {'act_mc': {'currentLabel': 'preview'}}}
    >>> user.revise(news) 
    >>> is_previewing(user)
    True
    '''
    if not user.olds_list:
        return False
    if 'preview' == user.root.cursor_mc.act_mc.currentLabel:
        return True
    #- if any_label_equals(user.intersection_mc_array, 
    #-         'question_black'):
    #-     return True
    #- if any_label_equals(user.intersection_mc_array, 
    #-         'preview_black'):
    #-     return True
    return False

def clear_preview(user, exclude_list = ['eat_mc', 'title_mc']):
    '''after reverting, reapply the latest news.
    >>> user = user_class()
    >>> user.create(1)

    Update olds_list to enable reverting
    >>> user.root.cursor_mc.act_mc.gotoAndPlay('play')
    >>> news = {'_0_8_mc': {'currentLabel': 'preview_black'}, 'cursor_mc': {'act_mc': {'currentLabel': 'preview'}}}
    >>> user.revise(news) 
    >>> revert_news = clear_preview(user, exclude_list = ['eat_mc', 'title_mc'])
    >>> user.root._0_8_mc.currentLabel
    'empty_black'
    >>> if not revert_news == {'_0_8_mc': {'currentLabel': 'empty_black'}, 'cursor_mc': {'act_mc': {'currentLabel': 'play'}}}:
    ...     revert_news

    User does not refers to reverted news 
    Assign user to refer reverted for convenient publishing.
    >>> if user.reverted == revert_news:
    ...     from pprint import pprint
    ...     pprint(user.reverted)
    ...     pprint(revert_news)

    Since the state was reverted, the preview state has been removed.

    Reverting the timestamp of the client's last transmission
    causes the server to believe the client has gone back in time.
    Thus, the server would date in the past.  
    The client transmission timestamp is in title_mc, so exclude title_mc.
    >>> user.root.title_mc.time_txt.text = '1000'
    >>> news = {'_0_8_mc': {'currentLabel': 'preview_black'}, 'cursor_mc': {'act_mc': {'currentLabel': 'preview'}}}
    >>> news = upgrade(news, {'title_mc': {'time_txt': {'text': '2000'}}})
    >>> user.revise(news) 
    >>> revert_news = clear_preview(user, exclude_list = ['eat_mc', 'title_mc'])
    >>> user.root.title_mc.time_txt.text
    '2000'
    >>> user.root._0_8_mc.currentLabel
    'empty_black'
    >>> if not revert_news == {'_0_8_mc': {'currentLabel': 'empty_black'}, 'cursor_mc': {'act_mc': {'currentLabel': 'play'}}}:
    ...     revert_news
    
    eat_mc represents real-time timer, so reverting that is equivalent
    to reseting the clock, which can cost a player a move.  
    So during clear preview, before reverting, remove eat_mc.
    >>> news = {'_0_7_mc': {'currentLabel': 'preview_black'}, 'eat_mc': {'act_mc': {'currentLabel': 'eat'}}, 'cursor_mc': {'act_mc': {'currentLabel': 'preview'}}}
    >>> user.revise(news) 
    >>> revert_news = clear_preview(user, exclude_list = ['eat_mc', 'title_mc'])
    >>> user.root._0_7_mc.currentLabel
    'empty_black'
    >>> user.root.eat_mc.act_mc.currentLabel
    'eat'
    >>> if not revert_news == {'_0_7_mc': {'currentLabel': 'empty_black'}, 'cursor_mc': {'act_mc': {'currentLabel': 'play'}}}:
    ...     revert_news
    '''
    news = {}
    while is_previewing(user):
        olds = user.olds_list.pop()
        for exclude in exclude_list:
            if exclude in olds.keys():
                olds.pop(exclude)
        cleared = user_as.imitate_news(user.root, olds)
        news = upgrade(news, olds)
    return news

def get_clear_formation_news(root):
    '''clear formations that have a response.'''
    news = {}
    for r in range(root.numChildren):
        child_mc = root.getChildAt(r)
        if child_mc.name.startswith('formation_'):
            formation_mc = child_mc
            for c in range(formation_mc.numChildren):
               rotate_mc = formation_mc.getChildAt(c)
               if 'none' != rotate_mc.response_mc.currentLabel:
                   reset = {formation_mc.name: 
                           {rotate_mc.name: 
                               {'response_mc': {'currentLabel': 'none'}}
                            }
                        }
                   news = upgrade(news, reset)
    return news


def may_get_formation_news(new_board, user, intersection_mc_array, 
        intersection_mc, dead = False):
    '''If enabled, revise user and return active formations.
    XXX see client.white_formation_example
    XXX see client.extra_stone_limit_example
    XXX see user_interface.py:preview_formation_example
    Formations auto expire, and reverting would replay response,
    so do not store response state in old list, such as by revise.
   
    >>> user = globe_class()
    >>> user.create(1)
    >>> user.root.defend_mc.gotoAndPlay('show')

    #>>> user.root.formation_field_mc.rotate_0_mc.response_mc.gotoAndPlay('response')
    #>>> user.root.formation_jump_mc.rotate_90_mc.response_mc.gotoAndPlay('response')
    #>>> user.olds_list
    []
    #>>> intersection_mc = user.intersection_mc_array[2][2]
    #>>> intersection_mc.gotoAndPlay('black')
    #>>> board_text = flash_to_text(user.intersection_mc_array)
    #>>> new_board = referee.text_to_array(board_text)
    #>>> news = may_get_formation_news(new_board, user, user.intersection_mc_array, intersection_mc, dead = False)
    #>>> news.get('formation_field_mc').get('rotate_0_mc')
    {'response_mc': {'currentLabel': 'response'}}
    #>>> user.olds_list
    []

    #Clear previous formations and notify client to also clear previous formations.
    #>>> user.revise(news)
    #>>> user.root.formation_field_mc.rotate_0_mc.response_mc.currentLabel
    'response'
    #>>> intersection_mc = user.intersection_mc_array[0][0]
    #>>> intersection_mc.gotoAndPlay('black')
    #>>> board_text = flash_to_text(user.intersection_mc_array)
    #>>> new_board = referee.text_to_array(board_text)
    #>>> news = may_get_formation_news(new_board, user, user.intersection_mc_array, intersection_mc, dead = False)
    #>>> user.root.formation_field_mc.rotate_0_mc.response_mc.currentLabel
    'none'
    #>>> news.get('formation_field_mc').get('rotate_0_mc')
    {'response_mc': {'currentLabel': 'none'}}

    May show defend decoration.
    >>> user.root._2_2_mc.gotoAndPlay('black')
    >>> user.root._2_4_mc.gotoAndPlay('black')
    >>> user.root._0_0_mc.gotoAndPlay('empty_black')
    >>> intersection_mc = user.intersection_mc_array[2][4]
    >>> user.root.decoration_mc.gotoAndPlay('none')
    >>> board_text = flash_to_text(user.intersection_mc_array)
    >>> new_board = referee.text_to_array(board_text)
    >>> news = may_get_formation_news(new_board, user, user.intersection_mc_array, intersection_mc, dead = False)
    >>> news.get('_2_3_mc')
    >>> user.root.decoration_mc.gotoAndPlay('show')
    >>> board_text = flash_to_text(user.intersection_mc_array)
    >>> new_board = referee.text_to_array(board_text)
    >>> user.root.defend_mc.gotoAndPlay('none')
    >>> news = may_get_formation_news(new_board, user, user.intersection_mc_array, intersection_mc, dead = False)
    >>> news.get('_2_3_mc')
    >>> user.root.defend_mc.gotoAndPlay('show')
    >>> user.root.attack_mc.gotoAndPlay('show')
    >>> user.root._4_4_mc.gotoAndPlay('white')
    >>> user.pb()
    ,,,,,,,,,
    ,,,,,,,,,
    ,,X,X,,,,
    ,,,,,,,,,
    ,,,,O,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    >>> board_text = flash_to_text(user.intersection_mc_array)
    >>> new_board = referee.text_to_array(board_text)
    >>> news = may_get_formation_news(new_board, user, user.intersection_mc_array, intersection_mc, dead = False)
    >>> if not news.get('_2_3_mc'):
    ...     from pprint import pprint; pprint(news)
    >>> if not 'black_attack' == news.get('_2_3_mc').get('decoration_mc').get('currentLabel'):  
    ...     from pprint import pprint; pprint(news)
    >>> news['_2_4_mc']['formation_mc']['currentLabel']
    'black_attack_defend'

    Remove previous decorations.
    >>> user.root.decoration_mc.gotoAndPlay('show')
    >>> user.root._8_8_mc.decoration_mc.gotoAndPlay('black_attack')
    >>> news = may_get_formation_news(new_board, user, user.intersection_mc_array, intersection_mc, dead = False)
    >>> news.get('_8_8_mc').get('decoration_mc')
    {'currentLabel': 'none'}

    If GnuGo expects stone will die, do not show positive formation.
    >>> news = may_get_formation_news(new_board, user, 
    ...     user.intersection_mc_array, intersection_mc, dead = True)
    >>> from pprint import pprint
    >>> news.get('_2_3_mc')

    Yet do show bad formation and curse the stone.
    >>> news = may_get_formation_news(new_board, user, 
    ...     user.intersection_mc_array, intersection_mc, dead = True)
    >>> from pprint import pprint
    >>> news.get('_2_3_mc')
    >>> news['_3_4_mc']['decoration_mc']['currentLabel']
    'white_attack'
    >>> news['_2_4_mc']['formation_mc']['currentLabel']
    'white_attack_curse'
    '''
    formation_news = {}
    if not dead:
        show_profit = user.root.profit_mc.currentLabel == 'show'
        show_defend = user.root.defend_mc.currentLabel == 'show'
        show_attack = user.root.attack_mc.currentLabel == 'show'
        if show_profit or show_defend or show_attack:
            clear_formation_news = get_clear_formation_news(user.root)
            olds = imitate_news(user.root, clear_formation_news)
            formation_news = upgrade(formation_news, clear_formation_news)
            show_decoration = user.root.decoration_mc.currentLabel == 'show'
            if show_decoration:
                remove_decoration_news = get_remove_decoration_news(
                        user.intersection_mc_array)
                formation_news = upgrade(formation_news, remove_decoration_news)
            news = get_formation_news(new_board, user.intersection_mc_array, 
                    intersection_mc, show_profit, show_defend, show_attack,
                    show_decoration)
            formation_news = upgrade(formation_news, news)
    if not formation_news:
        show_attack = user.root.attack_mc.currentLabel == 'show'
        row, column = get_row_column(intersection_mc.name)
        mark = new_board[row][column]
        if show_attack:
            attack = get_match_news(referee.get_nearest_enemy_matches,
                    referee.attack_pattern_dictionary, 'attack', 
                    intersection_mc_array, new_board, row, column)
            if attack:
                formation_news = upgrade(formation_news, attack)
                color = referee.get_color(mark)
                partner_color = referee.opposite(color)
                label = partner_color + '_' + 'attack_curse'
                curse_news = get_intersection_news(
                    row, column, 'formation_mc', label)
                formation_news = upgrade(formation_news, curse_news)
    return formation_news



def may_get_gift_news(user):
    '''If option on, no extra stone now, and one available, take one.
    >>> user = globe_class()
    >>> user.create(1)
    >>> from pprint import pprint
    >>> pprint(may_get_gift_news(user))
    {}

    If already have extra stone gift, and have hide option:  get hide gift.
    >>> user.root.option_mc.hide_available_mc.gotoAndPlay('_2')
    >>> user.root.hide_mc.gotoAndPlay('gift')
    >>> user.root.extra_stone_gift_mc.gotoAndPlay('_1')
    >>> pprint(may_get_gift_news(user))
    {'hide_gift_mc': {'currentLabel': '_1'},
     'option_mc': {'hide_available_mc': {'currentLabel': '_1'}}}

    If extra stone not available, and have hide option:  get hide gift.
    >>> user.root.option_mc.hide_available_mc.gotoAndPlay('_1')
    >>> user.root.extra_stone_mc.gotoAndPlay('gift')
    >>> user.root.hide_mc.gotoAndPlay('gift')
    >>> user.root.extra_stone_gift_mc.gotoAndPlay('_0')
    >>> user.root.option_mc.extra_stone_available_mc.gotoAndPlay('_0')
    >>> pprint(may_get_gift_news(user))
    {'hide_gift_mc': {'currentLabel': '_1'},
     'option_mc': {'hide_available_mc': {'currentLabel': '_0'}}}

    If hide not available, do not take it.
    >>> user.root.option_mc.hide_available_mc.gotoAndPlay('_0')
    >>> user.root.hide_mc.gotoAndPlay('gift')
    >>> user.root.extra_stone_gift_mc.gotoAndPlay('_0')
    >>> user.root.option_mc.extra_stone_available_mc.gotoAndPlay('_0')
    >>> pprint(may_get_gift_news(user))
    {}

    If extra stone available, take one.  If not, do not.
    >>> user = globe_class()
    >>> user.create(1)
    >>> user.root.extra_stone_mc.gotoAndPlay('gift')
    >>> user.root.hide_mc.gotoAndPlay('none')
    >>> user.root.option_mc.extra_stone_available_mc.gotoAndPlay('_2')
    >>> pprint(may_get_gift_news(user))
    {'extra_stone_gift_mc': {'currentLabel': '_1'},
     'option_mc': {'extra_stone_available_mc': {'currentLabel': '_1'}}}
    >>> user.root.option_mc.extra_stone_available_mc.gotoAndPlay('_1')
    >>> pprint(may_get_gift_news(user))
    {'extra_stone_gift_mc': {'currentLabel': '_1'},
     'option_mc': {'extra_stone_available_mc': {'currentLabel': '_0'}}}
    >>> user.root.option_mc.extra_stone_available_mc.gotoAndPlay('_0')
    >>> pprint(may_get_gift_news(user))
    {}
    '''
    news = {}
    if '_0' == user.root.cursor_mc.extra_stone_mc.currentLabel:
        if 'gift' == user.root.extra_stone_mc.currentLabel:
            extra_stone_gift = user.root.extra_stone_gift_mc.currentLabel
            if '_0' == extra_stone_gift:
                extra_stone_available = user.root.option_mc.extra_stone_available_mc.currentLabel
                extra_stone_available = int(extra_stone_available[1:])
                if 1 <= extra_stone_available:
                    extra_stone_available -= 1
                    extra_stone_available_text = '_%i' % extra_stone_available
                    news = {
                        'option_mc': {
                                 'extra_stone_available_mc': {
                                     'currentLabel': extra_stone_available_text}},
                        'extra_stone_gift_mc': {'currentLabel':  '_1'}}
                    return news
        if 'gift' == user.root.hide_mc.currentLabel:
            hide_gift = user.root.hide_gift_mc.currentLabel
            if '_0' == hide_gift:
                # XXX redundant form as extra_stone_available
                hide_available = user.root.option_mc.hide_available_mc.currentLabel
                hide_available = int(hide_available[1:])
                if 1 <= hide_available:
                    hide_available -= 1
                    hide_available_text = '_%i' % hide_available
                    news = {
                        'option_mc': {
                                 'hide_available_mc': {
                                     'currentLabel': hide_available_text}},
                        'hide_gift_mc': {'currentLabel':  '_1'}}
                    return news
    return news


def write_mouse_down(user, intersection_mc):
    '''Conveniently log a move as an example of mouse down.
    Must have defined 'wait', which is usually 1.0 to 4.0
    >>> user = globe_class()
    >>> user.create(1)
    >>> set_color(user, 'white')
    >>> intersection_mc = user.root._0_1_mc
    >>> write_mouse_down(user, intersection_mc)
    '>>> mouse_down_and_sleep(ethan, ethan.root._0_1_mc, wait)'
    >>> write_mouse_down(user, user.root.hide_gift_mc.use_mc)
    '>>> mouse_down_and_sleep(ethan, ethan.root.hide_gift_mc.use_mc, wait)'
    '''
    user_name = user.root.title_mc.username_txt.text
    color = get_color(user)
    input_log = '>>> mouse_down_and_sleep(%s, %s.%s, wait)' \
                    % (user_name, user_name, address(intersection_mc))
    return input_log




def add_black_capture_news(user, add_black_capture):
    '''Add (or subtract) to count of black's captures.
    >>> laurens = user_as.globe_class()
    >>> laurens.create(1)
    >>> laurens.root.score_mc.bar_mc.marker_mc.capture_mc.gotoAndPlay('_0')
    >>> news, total = add_black_capture_news(laurens, -1)
    >>> total
    -1
    >>> laurens.revise(news)
    >>> laurens.root.score_mc.bar_mc.marker_mc.capture_mc.currentLabel
    '_-1'
    >>> news, total = add_black_capture_news(laurens, 3)
    >>> total
    2
    >>> laurens.revise(news)
    >>> laurens.root.score_mc.bar_mc.marker_mc.capture_mc.currentLabel
    '_2'
    '''
    old_label = user.root.score_mc.bar_mc.marker_mc.capture_mc.currentLabel
    old_capture = int(old_label.strip('_'))
    capture = old_capture + add_black_capture
    capture_label = '_%i' % capture
    news = {
        'score_mc': {
            'bar_mc': {
                'marker_mc': {
                    'capture_mc': {
                        'currentLabel': capture_label
                    }
                }
            }
        }
    }
    return news, capture


def add_black_capture_to_score_news(user):
    '''Add count of black's captures to the score.
    >>> laurens = user_as.globe_class()
    >>> laurens.create(1)
    >>> laurens.root.score_mc.bar_mc.marker_mc.capture_mc.gotoAndPlay('_-1')
    >>> laurens.root.score_mc.bar_mc.gotoAndPlay('_0')
    >>> news = add_black_capture_to_score_news(laurens)
    >>> laurens.revise(news)
    >>> laurens.root.score_mc.bar_mc.currentLabel
    '_-1'
    >>> laurens.root.score_mc.bar_mc.marker_mc.capture_mc.gotoAndPlay('_3')
    >>> news = add_black_capture_to_score_news(laurens)
    >>> laurens.revise(news)
    >>> laurens.root.score_mc.bar_mc.currentLabel
    '_2'

    Careful!  It adds everytime.
    >>> news = add_black_capture_to_score_news(laurens)
    >>> laurens.revise(news)
    >>> laurens.root.score_mc.bar_mc.currentLabel
    '_5'
    '''
    black_capture_label = user.root.score_mc.bar_mc.marker_mc.capture_mc.currentLabel
    black_capture = int(black_capture_label.strip('_'))
    old_label = user.root.score_mc.bar_mc.currentLabel
    old_score = int(old_label.strip('_'))
    score = old_score + black_capture
    score_label = '_%i' % score
    return {
        'score_mc': {
            'bar_mc': {
                'currentLabel': score_label
            }
        }
    }

def get_color(user):
    '''
    >>> get_color(None)
    >>> get_color('')
    '''
    if not user:
        return
    user_name = user.root.title_mc.username_txt.text
    black_name = user.root.turn_mc.black_user_txt.text
    if black_name == user_name:
        return 'black'
    white_name = user.root.turn_mc.white_user_txt.text
    if white_name == user_name:
        return 'white'

def set_color(user, color):
    '''
    >>> user = user_as.globe_class()
    >>> user.create(1)
    >>> set_color(user, 'white'); get_color(user)
    'white'
    >>> set_color(user, 'black'); get_color(user)
    'black'
    >>> old_log_level = logging.getLogger().level
    >>> logging.getLogger().setLevel(logging.CRITICAL)
    >>> set_color(user, 'x'); get_color(user)
    'black'
    >>> logging.getLogger().setLevel(old_log_level)
    '''    
    user_name = user.root.title_mc.username_txt.text
    black_name = user.root.turn_mc.black_user_txt.text
    white_name = user.root.turn_mc.white_user_txt.text
    if 'black' == color:
        user.root.turn_mc.black_user_txt.text = user_name
        if white_name == user_name:
            user.root.turn_mc.white_user_txt.text = 'WHITE'
    elif 'white' == color:
        user.root.turn_mc.white_user_txt.text = user_name
        if black_name == user_name:
            user.root.turn_mc.black_user_txt.text = 'BLACK'
    else:
        logging.error('set_color:  what color is this?  %s' % color)


def get_board(user):
    '''referee text array board.
    >>> emmet = globe_class()
    >>> emmet.create(1)
    >>> board = get_board(emmet)
    >>> len(board)
    9
    '''
    intersection_mc_array = user.intersection_mc_array
    pre_board_text = flash_to_text(intersection_mc_array)
    pre_board = referee.text_to_array(pre_board_text)
    return pre_board

    
def get_empty_color_news(user, color):
    news = {}
    for row in user.intersection_mc_array:
        for intersection_mc in row:
            empty_color = 'empty_' + color
            if intersection_mc.currentLabel.startswith('empty') \
                    and empty_color != intersection_mc.currentLabel:
                news[intersection_mc.name] = {'currentLabel': empty_color}
    return news


def wait_your_turn(user, color, intersection_mc):
    '''If not your turn, say intersection is empty and give help.
    >>> user = user_as.globe_class()
    >>> user.create(1)
    >>> wait_your_turn(user, 'black', user.root._5_5_mc)
    >>> wait_your_turn(user, 'white', user.root._5_5_mc)
    {'_5_5_mc': {'currentLabel': 'empty_white'}, 'help_mc': {'currentLabel': 'wait_your_turn'}}
    '''
    if not color == user.root.turn_mc.currentLabel:
        empty = 'empty_' + color
        sorry = {intersection_mc.name: {'currentLabel': empty},
            'help_mc': {'currentLabel': 'wait_your_turn'}}
        return sorry

def get_your_turn_news(color):
    return {
        'turn_mc':  {'currentLabel': color}, 
        'cursor_mc': {
            'currentLabel': color,
            'act_mc': {'currentLabel': 'play'}
        },
        'turn_veil_mc':  {'currentLabel': 'you'}
    }

def is_your_turn(user):
    '''
    >>> andre = user_as.globe_class()
    >>> andre.create(1)
    >>> if not is_your_turn(andre):  andre.root.turn_veil_mc.currentLabel
    >>> your_turn_news = {'turn_veil_mc':  {'currentLabel': 'you'}}
    >>> olds = imitate_news(andre.root, your_turn_news)
    >>> if not is_your_turn(andre):  andre.root.turn_veil_mc.currentLabel
    >>> other_turn_news = {'turn_veil_mc':  {'currentLabel': 'other'}}
    >>> olds = imitate_news(andre.root, other_turn_news)
    >>> if is_your_turn(andre):  andre.root.turn_veil_mc.currentLabel
    '''
    return 'you' == user.root.turn_veil_mc.currentLabel
    
def update_turn(user, color, news, partner_news):
    '''turn unless extra stone
    >>> user = user_class()
    >>> user.create(1)
    >>> user.users = {}
    >>> user_name = user.root.title_mc.username_txt.text
    >>> user.root.turn_mc.black_user_txt.text = user_name
    >>> news, partner_news = update_turn(user, 'white', {}, {})
    >>> news['turn_veil_mc']['currentLabel']
    'you'
    >>> partner_news['turn_veil_mc']['currentLabel']
    'other'
    >>> partner_news['turn_veil_mc']['currentLabel']
    'other'

    White took a turn, do not reset white's pass.
    >>> partner_news.get('pass_mc')
    >>> partner_news.get('pass_white_mc')

    You see you may play.
    >>> news['cursor_mc']['currentLabel']
    'black'
    >>> news['cursor_mc']['act_mc']['currentLabel']
    'play'
    >>> partner_news['cursor_mc']['currentLabel']
    'none'
    >>> partner_news['cursor_mc']['act_mc']['currentLabel']
    'busy'
    >>> news, partner_news = update_turn(user, 'black', {}, {})
    >>> news['turn_veil_mc']['currentLabel']
    'other'
    >>> partner_news['turn_veil_mc']['currentLabel']
    'you'

    Black took a turn, do not reset white's pass.
    >>> partner_news.get('pass_mc')
    >>> partner_news.get('pass_white_mc')

    #>>> partner_news['pass_mc']['currentLabel']
    #'none'
    #>>> partner_news['pass_white_mc']['currentLabel']
    #'none'

    With extra stone, take another turn.
    >>> user.root.cursor_mc.extra_stone_mc.gotoAndPlay('_1')
    >>> news, partner_news = update_turn(user, 'black', {}, {})
    >>> news['turn_veil_mc']['currentLabel']
    'you'
    >>> partner_news['turn_veil_mc']['currentLabel']
    'other'
    >>> news['cursor_mc']['extra_stone_mc']['currentLabel']
    '_0'

    when turn updates, even if to pass, update progress
    >>> play_news = {'_0_0_mc': {'currentLabel': 'black'}, 'turn_mc': {'currentLabel': 'black'}}
    >>> import pprint
    >>> news, partner_news = update_turn(user, 'black', play_news, {})
    >>> news['_0_0_mc']['progress_mc']['currentLabel']
    'black_complete'
    '''
    if '_1' == user.root.cursor_mc.extra_stone_mc.currentLabel:
        lose_extra_stone = {'cursor_mc':  {'extra_stone_mc': 
            {'currentLabel':  '_0'}}}
        news = upgrade(news, lose_extra_stone)
        next_color = color
    else:
        next_color = referee.next_turn(color)
    your_turn = get_your_turn_news(next_color)
    their_turn = {
            'turn_mc':  {'currentLabel': next_color}, 
            'cursor_mc': {
                'currentLabel': 'none',
                'act_mc': {'currentLabel': 'busy'}
                },
            'turn_veil_mc':  {'currentLabel': 'other'}}
    #reset_pass = {
    #    'pass_mc': {'currentLabel': 'none'},
    #    'pass_white_mc': {'currentLabel': 'none'},
    #}
    if next_color == get_color(user):
        news = upgrade(news, your_turn)
        partner_news = upgrade(partner_news, their_turn)
    else:
        news = upgrade(news, their_turn)
        partner_news = upgrade(partner_news, your_turn)
        #partner_news = upgrade(partner_news, reset_pass)
    news = update_progress_news(user.intersection_mc_array, news)
    from super_users import get_partner
    partner = get_partner(user.users, user)
    if partner:
        partner_news = update_progress_news(partner.intersection_mc_array, 
                partner_news)
    return news, partner_news


def update_empty_block(user, new_board, color, news):
    '''Update your turn and empty blocks.
    >>> yuji = globe_class()
    >>> yuji.create(1)
    >>> from pprint import pprint

    YUJI CAN SEE EMPTY BLOCKS.
    >>> yuji.root.option_mc.empty_block_mc.gotoAndPlay('show')
    >>> new_board_text = flash_to_text(yuji.intersection_mc_array)
    >>> new_board = text_to_array(new_board_text)
    >>> news = update_empty_block(yuji, None, 'black', {})
    >>> if not news.get('_0_0_mc'):
    ...     pprint(news)
    >>> news.get('_0_0_mc').get('empty_block_north_mc')
    {'currentLabel': 'block'}
    >>> news.get('_0_0_mc').get('empty_block_east_mc')
    {'currentLabel': 'liberty'}

    new_board supersedes intersection_mc_array
    >>> new_board_text = flash_to_text(yuji.intersection_mc_array)
    >>> new_board = text_to_array(new_board_text)
    >>> new_board[1][1] = referee.black
    >>> news = update_empty_block(yuji, new_board, 'black', {})
    >>> if not news.get('_0_1_mc'):
    ...     pprint(news)
    >>> if not news.get('_0_1_mc').get('empty_block_south_mc') == {'currentLabel': 'you'}:
    ...     pprint(news.get('0_1_mc'))

    ETHAN CANNOT SEE EMPTY BLOCKS.
    >>> ethan = globe_class()
    >>> ethan.create(1)
    >>> ethan.root.option_mc.empty_block_mc.gotoAndPlay('none')
    >>> ethan.root._1_1_mc.gotoAndPlay('black')
    >>> new_board_text = flash_to_text(ethan.intersection_mc_array)
    >>> new_board = text_to_array(new_board_text)
    >>> new_board[1][1] = referee.black
    >>> news = update_empty_block(ethan, new_board, 'white', {})
    >>> if news.get('_0_1_mc'):
    ...     pprint(news)
    '''
    if not new_board:
        new_board_text = flash_to_text(user.intersection_mc_array)
        new_board = text_to_array(new_board_text)
    if 'show' == user.root.option_mc.empty_block_mc.currentLabel:
        reply = get_empty_block_news(user.intersection_mc_array, 
                new_board, color)
        news = upgrade(news, reply)
    return news


def request_extra_stone(user, news):
    '''If you have gift, use for extra stone.
    >>> user = user_as.globe_class()
    >>> user.create(1)
    >>> news = user_as.get_extra_stone_news()
    >>> reply = request_extra_stone(user, news)
    >>> reply.get('cursor_mc')
    >>> user.root.extra_stone_gift_mc.gotoAndPlay('_1')
    >>> reply = request_extra_stone(user, news)
    >>> reply.get('cursor_mc').get('extra_stone_mc')
    {'currentLabel': '_1'}
    >>> reply.get('extra_stone_gift_mc')
    {'currentLabel': '_0', 'use_mc': {'currentLabel': 'none'}}

    Only works for _1 right now.
    >>> user.root.extra_stone_gift_mc.gotoAndPlay('_2')
    >>> reply = request_extra_stone(user, news)
    >>> reply.get('cursor_mc')
    '''
    reply = {}
    extra_stone_gift_mc = news.get('extra_stone_gift_mc')
    if extra_stone_gift_mc:
        use_mc = extra_stone_gift_mc.get('use_mc')
        if 'enter' == use_mc.get('currentLabel'):
            if '_1' == user.root.extra_stone_gift_mc.currentLabel:
                reply = {'extra_stone_gift_mc': {'currentLabel': '_0',
                            'use_mc':  {'currentLabel': 'none'}},
                        'cursor_mc':  {'extra_stone_mc': {'currentLabel': '_1'}}
                    }
    return reply


def request_hide(user, news):
    '''If you have gift, use for extra stone.
    >>> user = user_as.globe_class()
    >>> user.create(1)
    >>> news = user_as.get_hide_news()
    >>> reply = request_hide(user, news)
    >>> reply.get('cursor_mc')
    >>> user.root.hide_gift_mc.gotoAndPlay('_1')
    >>> reply = request_hide(user, news)
    >>> reply.get('cursor_mc')
    {'currentLabel': 'hide_black'}
    >>> reply.get('hide_gift_mc')
    {'currentLabel': '_0', 'use_mc': {'currentLabel': 'none'}}

    Only works for _1 right now.
    >>> user.root.hide_gift_mc.gotoAndPlay('_2')
    >>> reply = request_hide(user, news)
    >>> reply.get('cursor_mc')
    '''
    reply = {}
    hide_gift_mc = news.get('hide_gift_mc')
    if hide_gift_mc:
        use_mc = hide_gift_mc.get('use_mc')
        if 'enter' == use_mc.get('currentLabel'):
            if '_1' == user.root.hide_gift_mc.currentLabel:
                reply = {'hide_gift_mc': {'currentLabel': '_0',
                            'use_mc':  {'currentLabel': 'none'}},
                        'cursor_mc':  {'currentLabel': 'hide_black'}
                    }
    return reply

# End single user algorithms


snippet = '''
# !start python code_explorer.py --snippet snippet --import super_user.py
import super_user; super_user = reload(super_user); from super_user import *
# code_unit.doctest_unit(may_get_formation_news)
'''
import code_unit
if __name__ == '__main__':
    from optparse import OptionParser
    parser = OptionParser()
    parser.add_option("--unit", default="",
        dest="unit", help="unit to doctest [default: %default]")
    parser.add_option('-v', '--verbose', dest='verbose', default='warning',
                    help="Increase verbosity")
    (options, args) = parser.parse_args()
    log_level = logging_levels[options.verbose]
    logging.basicConfig(level=log_level)
    if options.unit:
        unit = eval(options.unit)
        code_unit.doctest_unit(unit)
    else:
        units = globals().values()
        ## units.remove(setup_example)
        code_unit.doctest_units(units)
    

