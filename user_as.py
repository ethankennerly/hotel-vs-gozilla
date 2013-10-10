#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
A user of Crazy Cake

                client:  acceptance test, master
                    user:  globe:  client.as.py, stage
                                remote_control ...
                                    actionscript
                embassy
                    users:  super_user
                            user ...

user does not depend on other users.  
so user functions may be tested with performance bottleneck of user.create.
user depends on stage and client-side actionscript.
user is accessed by client and users.

'''
__author__ = 'Ethan Kennerly'


import logging
logging_levels = {'critical': logging.CRITICAL,
              'error': logging.ERROR,
              'warning': logging.WARNING,
              'info': logging.INFO,
              'debug': logging.DEBUG}
log_level = logging_levels['warning']

import copy

# Client animation, resources, and state



# Begin ActionScript compatible Python  client.as.py
# Begin ActionScript to export to client.as

# Control Crazy Cake flash movie
#- save_file_name = 'lifeanddeath.stage.py'
save_file_name = 'lifeanddeath.fla.stage.py'
from remote_control import *

# Convenient to test.
mouseDown = MouseEvent(MouseEvent.MOUSE_DOWN)
mouseOver = MouseEvent(MouseEvent.MOUSE_OVER)
mouseOut = MouseEvent(MouseEvent.MOUSE_OUT)
enterFrame = Event(Event.ENTER_FRAME)

def setup_echo(a_class):
    user = a_class()
    user.create(1)
    user.setup_events()
    from mock_client import echo_protocol_class
    user.ambassador = echo_protocol_class()
    return user


def get_intersection_name(row, column):
    name = '_' + str(row) + '_' + str(column) + '_mc'
    # name = '_%i_%i_mc' % (row, column)
    return name

def get_intersection_array(root, length = 9):
    '''
    >>> user = globe_class()
    >>> user.create(1)
    >>> user.intersection_mc_array = get_intersection_array(
    ...     user.root, length = 9)
    >>> len(user.intersection_mc_array)
    9
    >>> user.intersection_mc_array = get_intersection_array(
    ...     user.root, length = 3)
    >>> len(user.intersection_mc_array)
    3
    '''
    intersections = []
    for row in range(length):
        intersections.append( [] )
        for column in range(length):
            name = get_intersection_name(row, column)
            if root.getChildByName(name):
                # ActionScript gotcha:  a[-1] :: a[a.length - 1]
                intersections[-1].append(root[name])
    return intersections


# from intersection_mc import get_first_intersection





def rstrip_string(string, strip):
    '''Match exact string to strip.
    >>> 'question_black_repeat'.rstrip('_repeat')
    'question_black'
    >>> 'question_black_repeatt'.rstrip('_repeat')
    'question_black'
    >>> rstrip_string('question_black_repeat', '_repeat')
    'question_black'
    >>> rstrip_string('question_black_repeatt', '_repeat')
    'question_black_repeatt'
    >>> rstrip_string('question_black_repeat2', '_repeat')
    'question_black_repeat2'
    '''
    splits = string.split(strip)
    splits_length = len(splits)
    stripped = string
    if 2 <= splits_length:
        if '' == splits[splits_length - 1]:
            splits.pop()
            stripped = ''.join(splits)
    return stripped


def get_play_stone_news(intersection_mc, eat_mc, preview_enabled):
    '''Next state for stone.
    Start preview, which server increments to question.
    >>> joris = globe_class()
    >>> joris.create()
    >>> news = get_play_stone_news(joris.root._0_0_mc, joris.root.eat_mc, True)
    >>> news['cursor_mc']['act_mc'].get('currentLabel')
    'preview'
    >>> news['_0_0_mc'].get('currentLabel')
    'preview_black'

    If no preview, then do not preview.
    >>> news = get_play_stone_news(joris.root._0_0_mc, joris.root.eat_mc, False)
    >>> news.get('cursor_mc')
    >>> news['_0_0_mc'].get('currentLabel')
    'play_black'

    If no preview, then do not preview hide.
    >>> joris.root._0_0_mc.gotoAndPlay('empty_hide_black')
    >>> news = get_play_stone_news(joris.root._0_0_mc, joris.root.eat_mc, False)
    >>> news.get('cursor_mc')
    >>> news['_0_0_mc'].get('currentLabel')
    'play_hide_black'

    If not eating, send that, too.
    >>> if not news['eat_mc'].get('currentLabel') == 'none':  
    ...     news['eat_mc'].get('currentLabel')

    If 'black' or 'white', return nothing.
    >>> joris.root._0_0_mc.gotoAndPlay('black')
    >>> news = get_play_stone_news(joris.root._0_0_mc, joris.root.eat_mc, False)
    >>> news
    {}

    If eating, do not send eating.
    >>> joris.root.eat_mc.act_mc.gotoAndPlay('eat')
    >>> news = get_play_stone_news(joris.root._0_0_mc, joris.root.eat_mc, False)
    >>> news.get('eat_mc')
    >>> joris.root.eat_mc.act_mc.gotoAndPlay('none')

    If looping animation (ending with '_repeat'), then convert to entry label.
    >>> from pprint import pprint
    >>> joris.root._0_0_mc.gotoAndPlay('question_black_repeat')
    >>> news = get_play_stone_news(joris.root._0_0_mc, joris.root.eat_mc, False)
    >>> if not news.get('_0_0_mc').get('currentLabel') == 'play_black':
    ...     pprint(news)

    Do not convert '_repeat' found elsewhere in label.
    >>> old_log_level = logging.getLogger().level
    >>> logging.getLogger().setLevel(logging.CRITICAL)
    >>> joris.root._0_0_mc.gotoAndPlay('question_black_repeat_t')
    >>> news = get_play_stone_news(joris.root._0_0_mc, joris.root.eat_mc, False)
    >>> if news.get('_0_0_mc'):
    ...     pprint(news)
    >>> logging.getLogger().setLevel(old_log_level)

    rene moves black.  rene sees start progress immediately
    >>> rene = globe_class()
    >>> rene.create()
    >>> news = get_play_stone_news(rene.root._0_0_mc, rene.root.eat_mc, False)
    >>> news['_0_0_mc']['progress_mc'].get('currentLabel')
    'black_setup'
    
    rene moves white.  rene sees start progress immediately
    >>> rene.root._0_0_mc.gotoAndPlay('empty_white')
    >>> news = get_play_stone_news(rene.root._0_0_mc, rene.root.eat_mc, False)
    >>> news['_0_0_mc']['progress_mc'].get('currentLabel')
    'white_setup'
    '''
    logging.info('get_play_stone_news:  starting at ' + intersection_mc.name);
    var = label = null;
    var = cursor_label = null;
    var = news = {};
    var = intersection_label = rstrip_string(intersection_mc.currentLabel, '_repeat');
    var = progress_news = {};
    if ('empty_black' == intersection_label):
        if (preview_enabled):
            label = 'preview_black';
            cursor_label = 'preview';
        else:
            label = 'play_black';
            progress_news[intersection_mc.name] = \
                {'progress_mc': {'currentLabel':  'black_setup'}};
            news = upgrade(news, progress_news);
    elif ('question_black' == intersection_label):
        label = 'play_black';
        progress_news[intersection_mc.name] = \
            {'progress_mc': {'currentLabel':  'black_setup'}};
        news = upgrade(news, progress_news);
    elif ('empty_white' == intersection_label):
        label = 'play_white';
        progress_news[intersection_mc.name] = \
            {'progress_mc': {'currentLabel':  'white_setup'}};
        news = upgrade(news, progress_news);
    elif ('empty_hide_black' == intersection_label):
        if (preview_enabled):
            label = 'preview_hide_black';
            cursor_label = 'preview';
        else:
            label = 'play_hide_black';
            progress_news[intersection_mc.name] = \
                {'progress_mc': {'currentLabel':  'black_setup'}};
            news = upgrade(news, progress_news);
    elif ('question_hide_black' == intersection_label):
        label = 'play_hide_black';
        progress_news[intersection_mc.name] = \
            {'progress_mc': {'currentLabel':  'black_setup'}};
        news = upgrade(news, progress_news);
    elif ('black' == intersection_label \
            or 'white' == intersection_label):
        # label = intersection_label;
        var = a = 0;
    else:
        logging.error('get_play_stone_news:  what do i do? ' + intersection_mc.name \
                + ' : ' + intersection_label);
    if (label):
        var = label_news = {};
        label_news[intersection_mc.name] = {'currentLabel':  label};
        if ('none' == eat_mc.act_mc.currentLabel):
            label_news['eat_mc'] = {};
            label_news['eat_mc']['act_mc'] = {'currentLabel':  eat_mc.act_mc.currentLabel};
        news = upgrade(news, label_news);
    if (cursor_label):
        news = upgrade(news,
                {'cursor_mc':  {'act_mc': {'currentLabel':  cursor_label}}} );
    return news;


def get_busy_news(root):
    '''If not preview, once click, become busy.
    >>> robby = globe_class()
    >>> robby.create()
    >>> ok, news = get_busy_news(robby.root)
    >>> ok
    True
    >>> news['cursor_mc']['act_mc']['currentLabel']
    'busy'
    >>> news.get('help_mc')

    If busy, notify that we are busy.
    >>> olds = imitate_news(robby.root, news)
    >>> ok, news = get_busy_news(robby.root)
    >>> ok
    False
    >>> news.get('cursor_mc')
    >>> news['help_mc']['currentLabel']
    'busy'

    Until server says we are no longer busy.  Then reset.
    >>> reply = {'cursor_mc': {'act_mc': {'currentLabel': 'none'}}}
    >>> olds = imitate_news(robby.root, reply)
    >>> ok, news = get_busy_news(robby.root)
    >>> ok
    True
    >>> news['cursor_mc']['act_mc']['currentLabel']
    'busy'
    >>> news.get('help_mc')
    '''
    if 'busy' == root.cursor_mc.act_mc.currentLabel:
        return False, {'help_mc': {'currentLabel': 'busy'}}
    else:
        return True, {'cursor_mc': {'act_mc': {'currentLabel': 'busy'}}}

def count_item(container):
    '''How many items are in the container?
    ActionScript does not respond like Python to:  {} != object
    >>> count_item({'a': 0})
    1
    >>> count_item(2)
    Traceback (most recent call last):
      ...
    TypeError: 'int' object is not iterable
    >>> count_item(null)
    0
    '''
    var = count = 0;
    if (null != container):
        for key in container:
            count += 1;
    return count;



def remove_preview_news(intersection_mc_array, intersection_mc):
    '''
    press an intersection, moving into a preview.  
    look for intersections that may be in preview.  revert these.
    >>> laurens = globe_class()
    >>> laurens.create(1)
    >>> laurens.setup_events()
    >>> laurens.root._0_0_mc.gotoAndPlay('preview_black')
    >>> remove_news = remove_preview_news(laurens.intersection_mc_array, 
    ...     laurens.root._0_1_mc)
    >>> from pprint import pprint
    >>> if not remove_news.get('_0_0_mc'):
    ...     pprint(remove_news)
    >>> remove_news.get('_0_0_mc').get('currentLabel')
    'empty_black'
    >>> laurens.root._0_1_mc.gotoAndPlay('question_black')
    >>> remove_news = remove_preview_news(laurens.intersection_mc_array,
    ...     laurens.root._0_1_mc)
    >>> from pprint import pprint
    >>> if remove_news.get('_0_1_mc'):
    ...     pprint(remove_news)
    >>> remove_news.get('_0_1_mc')
    '''
    var = news = {};
    for row in range(len(intersection_mc_array)):
        for column in range(len(intersection_mc_array[row])):
            var = remove_intersection_mc = intersection_mc_array[row][column];
            if (intersection_mc != remove_intersection_mc):
                if ('preview_black' == remove_intersection_mc.currentLabel \
                        or 'question_black' == remove_intersection_mc.currentLabel):
                    var = empty = note(remove_intersection_mc, 
                            'currentLabel', 'empty_black');
                    news = upgrade(news, empty);
    return news;

def get_extra_stone_news():
    '''see embassy.request_extra_stone'''
    return {'extra_stone_gift_mc':  {
        'use_mc': {'currentLabel':  'enter'}
        }
    }

def get_hide_news():
    '''see embassy.request_hide'''
    return {'hide_gift_mc':  {
        'use_mc': {'currentLabel':  'enter'}
        }
    }

def get_mouse_shield_news(root):
    '''Activate and place mouse shield at mouse.  Auto-expires.
    >>> laurens = globe_class()
    >>> laurens.create()
    >>> hasattr(laurens.root, 'mouseX')
    True
    >>> hasattr(laurens.root, 'mouseY')
    True
    >>> laurens.root.mouseX = 100
    >>> laurens.root.mouseY = 200

    Flash shield animation auto-expires.
    Mock client must deactivate explicitly.
    >>> laurens.root.mouse_shield_mc.gotoAndPlay('none')
    >>> import pprint
    >>> news = get_mouse_shield_news(laurens.root)

    Mouse down marks last press (or whatever event when getting news).
    >>> pprint.pprint(news.get('mouse_down_mc'))
    {'currentLabel': 'shield', 'x': 100, 'y': 200}
    
    Flash has shield follow mouse every frame.
    >>> pprint.pprint(news.get('mouse_shield_mc'))
    {'currentLabel': 'shield'}

    User may be clicking sporadically or accidentally touching screen.
    Does not move mouse down if already activated, yet restarts shield.
    >>> olds = imitate_news(laurens.root, news)
    >>> laurens.root.mouseX = 300
    >>> laurens.root.mouseY = 400
    >>> news = get_mouse_shield_news(laurens.root)
    >>> pprint.pprint(news.get('mouse_down_mc'))
    {'currentLabel': 'shield'}
    >>> pprint.pprint(news.get('mouse_shield_mc'))
    {'currentLabel': 'shield'}
    
    Flash shield animation auto-expires.
    Mock client must deactivate explicitly.
    >>> laurens.root.mouse_shield_mc.gotoAndPlay('none')
    >>> news = get_mouse_shield_news(laurens.root)
    >>> pprint.pprint(news.get('mouse_down_mc'))
    {'currentLabel': 'shield', 'x': 300, 'y': 400}
    >>> pprint.pprint(news.get('mouse_shield_mc'))
    {'currentLabel': 'shield'}
    '''
    if 'shield' != root.mouse_shield_mc.currentLabel:
        return {
            'mouse_down_mc': {
                    'currentLabel': 'shield', 
                    'x': root.mouseX, 
                    'y': root.mouseY},
            'mouse_shield_mc': {
                    'currentLabel': 'shield'}
            }
    else:
        return {
            'mouse_down_mc': {
                    'currentLabel': 'shield'},
            'mouse_shield_mc': {
                    'currentLabel': 'shield'}
            }


def get_problem_news(problem_name):
    news = {
        'lobby_mc': {}
    }
    news['lobby_mc'][problem_name] = { 
                'enter_mc': {'currentLabel': 'enter'}
            }
    return news


def get_hide_info_news():
    return {'info_mc': {
        'currentLabel': 'none',
        'stone_mc': {'currentLabel': 'none'},
        'decoration_mc': {'currentLabel': 'none'},
        'territory_mc': {'currentLabel': 'none'},
        'top_move_mc': {'currentLabel': 'none'},
        'profit_mc': {'currentLabel': 'none'},
        'block_mc': {'currentLabel': 'none'},
        'dragon_status_mc': {'currentLabel': 'none'},
        '_txt': {'text': ''}
        }
    };


    


def get_test_sequence(black, label, time):
    '''
    >>> moonhyoung = globe_class()
    >>> moonhyoung.create()
    >>> news = get_test_sequence(moonhyoung, 'question_black', 1000)
    '''
    moonhyoung = black
    event = note(moonhyoung.root._3_3_mc, 'currentLabel', label)
    timed_event = upgrade(event, {'time_txt': {'text': str(time)}})
    sequence = [timed_event]
    news = {'sequence': sequence}
    # moonhyoung.publish(news)
    return news


def get_children(parent_mc, exclude_name):
    '''
    >>> joris = globe_class()
    >>> joris.create()
    >>> joris.setup_events()
    >>> joris.ambassador = echo_protocol_class()
    >>> from pprint import pprint
    >>> unnamed_mc = MovieClip()
    >>> unnamed_mc.name = 'instance1443'
    >>> joris.root.lobby_mc._20_mc.addChild(unnamed_mc)
    >>> children = get_children(joris.root.lobby_mc._20_mc, 'main_mc')
    >>> if not 5 <= len(children):  children
    >>> if unnamed_mc in children:  children
    >>> [c.name for c in children if c.name == 'main_mc']
    []
    '''
    var = children = [];
    var = child_count = parent_mc.numChildren;
    for c in range(child_count):
        var = child_mc = parent_mc.getChildAt(c);
        if (isMovieClip(child_mc) and hasName(child_mc)):
            if (exclude_name != child_mc.name):
                children.append(child_mc);
    return children;

def children_listen_to_mouse(parent_mc, event, respond, exclude_name):
    '''All children except the excluded listen to mouse down.
    >>> joris = globe_class()
    >>> joris.create()
    >>> joris.setup_events()
    >>> joris.ambassador = echo_protocol_class()
    >>> from pprint import pprint
    >>> unnamed_mc = MovieClip()
    >>> unnamed_mc.name = 'instance1443'
    >>> joris.root.lobby_mc._20_mc.addChild(unnamed_mc)
    >>> children_listen_to_mouse(joris.root.lobby_mc._20_mc, 
    ...     MouseEvent.MOUSE_DOWN, joris.problem_name, 'main_mc')
    >>> old_log_level = logging.getLogger().level
    >>> logging.getLogger().setLevel(logging.CRITICAL)
    >>> unnamed_mc.dispatchEvent(mouseDown)
    >>> logging.getLogger().setLevel(old_log_level)
    >>> if joris.ambassador.sends:
    ...     joris.ambassador.sends[-1].get('lobby_mc')

    Link all menu items in stage except back to main.
    >>> joris.root.lobby_mc._20_mc.hide_7_7_mc.dispatchEvent(mouseDown)
    >>> joris.root.lobby_mc._20_mc.extra_hide_7_7_mc.dispatchEvent(mouseDown)
    >>> single_player_news = joris.ambassador.sends[-1]
    >>> pprint(single_player_news.get('lobby_mc'))
    {'_20_mc': {'extra_hide_7_7_mc': {'currentLabel': 'enter',
                                      'dispatchEvent': 'mouseDown'}}}

    May also listen to mouseOver or mouseOut.
    >>> marije = joris
    >>> children_listen_to_mouse(marije.root.lobby_mc._00_mc, 
    ...     MouseEvent.MOUSE_OVER, marije.show_menu_info, 'main_mc')
    >>> target = marije.root.lobby_mc._00_mc.capture_3_3_mc
    >>> target.info_txt.text = 'Surround a fire.'
    >>> marije.root.info_mc.currentLabel
    'none'
    >>> target.dispatchEvent(mouseOver)
    >>> marije.root.info_mc.currentLabel
    'show'
    >>> children_listen_to_mouse(marije.root.lobby_mc._00_mc, 
    ...     MouseEvent.MOUSE_OUT, marije.hide_info, 'main_mc')
    >>> marije.root.info_mc.currentLabel
    'show'
    >>> target.dispatchEvent(mouseOut)
    >>> marije.root.info_mc.currentLabel
    'none'
    '''
    var = children = get_children(parent_mc, exclude_name);
    for c in range(len(children)):
        var = child_mc = children[c];
        child_mc.addEventListener(event, respond);




def get_laurens_question_black_sequenced_news():
    return \
    {'_2_2_mc': {'black_shape_mc': {'defend_mc': {'profit_mc': {'currentLabel': 'show'}}}},
     'cursor_mc': {'act_mc': {'currentLabel': 'preview'}},
     'sequence': [{'_2_2_mc': {'currentLabel': 'question_black'},
                   'time_txt': {'text': '190951'}},
                  {'_3_2_mc': {'top_move_mc': {'currentLabel': 'white'}},
                   'time_txt': {'text': '191201'}},
                  {'_1_2_mc': {'territory_mc': {'currentLabel': 'black'}},
                   '_2_1_mc': {'territory_mc': {'currentLabel': 'black'}},
                   '_2_3_mc': {'territory_mc': {'currentLabel': 'black'}},
                   '_3_2_mc': {'territory_mc': {'currentLabel': 'black'}},
                   'time_txt': {'text': '191451'}},
                  {'_0_2_mc': {'territory_mc': {'currentLabel': 'black'}},
                   '_1_1_mc': {'territory_mc': {'currentLabel': 'black'}},
                   '_1_3_mc': {'territory_mc': {'currentLabel': 'black'}},
                   '_2_0_mc': {'territory_mc': {'currentLabel': 'black'}},
                   '_3_1_mc': {'territory_mc': {'currentLabel': 'black'}},
                   '_3_3_mc': {'territory_mc': {'currentLabel': 'black'}},
                   '_4_2_mc': {'territory_mc': {'currentLabel': 'black'}},
                   'time_txt': {'text': '191701'}},
                  {'_0_1_mc': {'territory_mc': {'currentLabel': 'black'}},
                   '_0_3_mc': {'territory_mc': {'currentLabel': 'black'}},
                   '_1_0_mc': {'territory_mc': {'currentLabel': 'black'}},
                   '_1_4_mc': {'territory_mc': {'currentLabel': 'black'}},
                   '_3_0_mc': {'territory_mc': {'currentLabel': 'black'}},
                   '_3_4_mc': {'territory_mc': {'currentLabel': 'black'}},
                   '_4_1_mc': {'territory_mc': {'currentLabel': 'black'}},
                   '_4_3_mc': {'territory_mc': {'currentLabel': 'black'}},
                   'time_txt': {'text': '191951'}},
                  {'_0_0_mc': {'territory_mc': {'currentLabel': 'black'}},
                   '_0_4_mc': {'territory_mc': {'currentLabel': 'black'}},
                   '_4_0_mc': {'territory_mc': {'currentLabel': 'black'}},
                   '_4_4_mc': {'territory_mc': {'currentLabel': 'black'}},
                   'time_txt': {'text': '192201'}}],
     'score_mc': {'bar_mc': {'currentLabel': '_23',
                             'marker_mc': {'change_txt': {'text': '+23'},
                                           'currentLabel': 'positive'},
                             'territory_txt': {'text': '23'}}},
     'tutor_mc': {'currentLabel': 'question'}}
            

class globe_class(object):
    '''Global variables get out of sync between local function and doctest example.  This class stores the global variables that ActionScript needs.
    And methods that are inconvenient to write without implicit reference to globe, such as event listeners.
    embassy needs to import non-shared globe that is isomorphic to client.
    '''
    def __init__(globe):
        '''
        >>> laurens = globe_class()
        >>> laurens.instant
        True
        >>> import config
        >>> defaults = config.setup_defaults()
        >>> configuration = config.borg(defaults)
        >>> configuration.instant = True
        >>> moonhyoung = globe_class()
        >>> moonhyoung.instant
        True
        '''
        globe.root = None
        globe.intersection_mc_array = None
        globe.ambassador = None
        globe.news_list = []
        globe.olds_list = []
        globe.sequence_list = []
        globe.original_stage = {}
        globe._speed = 1
        globe._save_file_name = save_file_name
        globe.save_list = []
        globe.info = {}
        globe.info_olds = {}
        globe.info_sequence = [];
        # below is not used in actionscript client
        globe.play_history = []
        globe.board_history = []
        globe.current = {}
        import config
        defaults = config.setup_defaults()
        configuration = config.borg(defaults)
        globe.instant = configuration.instant

    def __del__(globe):
        if hasattr(globe, 'root') and globe.root:
            globe.root.gateway_mc.gotoAndPlay('exit')

    def create(globe, speed = 1):
        '''Flash demands root (and its parent, the stage) be read-only.
        '''
        # XXX intersection_mc.news_to_board.__doc__ lost: refer_to_stage
        from remote_control import refer_to_stage
        globe._speed = speed
        #- globe.root = create_stage(save_file_name) # slow
        globe.root = refer_to_stage(save_file_name)
        globe.intersection_mc_array = get_intersection_array(globe.root) 
        globe.credentials = globe.root['title_mc']

    def setup_formations(globe):
        '''Formations get in the way of mouse click so they are turned off.
        >>> laurens = globe_class()
        >>> laurens.create()
        >>> laurens.setup_formations()

        #disable formations
        #>>> laurens.root.formation_connect_mc.mouseEnabled
        #False
        #>>> laurens.root.formation_connect_mc.mouseChildren
        #False
        #>>> laurens.root.formation_perch_mc.mouseEnabled
        #False
        #>>> laurens.root.formation_perch_mc.mouseChildren
        #False
        '''
        var = child_count = globe.root.numChildren;
        for c in range(child_count):
            var = child = globe.root.getChildAt(c);
            # py:find === as:indexOf
            if (0 == child.name.find('formation')):
                child.mouseEnabled = false;
                child.mouseChildren = false;
        #globe.root.formation_connect_mc.mouseEnabled = false
        #globe.root.formation_connect_mc.mouseChildren = false
        #globe.root.formation_diagonal_attack_mc.mouseEnabled = false
        #globe.root.formation_diagonal_attack_mc.mouseChildren = false
        #globe.root.formation_diagonal_connect_mc.mouseEnabled = false
        #globe.root.formation_diagonal_connect_mc.mouseChildren = false
        #globe.root.formation_diagonal_cut_half_mc.mouseEnabled = false
        #globe.root.formation_diagonal_cut_half_mc.mouseChildren = false
        #globe.root.formation_diagonal_mc.mouseEnabled = false
        #globe.root.formation_diagonal_mc.mouseChildren = false
        #globe.root.formation_field_mc.mouseEnabled = false
        #globe.root.formation_field_mc.mouseChildren = false
        #globe.root.formation_jump_attack_mc.mouseEnabled = false
        #globe.root.formation_jump_attack_mc.mouseChildren = false
        #globe.root.formation_jump_mc.mouseEnabled = false
        #globe.root.formation_jump_mc.mouseChildren = false
        #globe.root.formation_knight_attack_mc.mouseEnabled = false
        #globe.root.formation_knight_attack_mc.mouseChildren = false
        #globe.root.formation_knight_cut_half_mc.mouseEnabled = false
        #globe.root.formation_knight_cut_half_mc.mouseChildren = false
        #globe.root.formation_knight_mc.mouseEnabled = false
        #globe.root.formation_knight_mc.mouseChildren = false
        #globe.root.formation_leap_attack_mc.mouseEnabled = false
        #globe.root.formation_leap_attack_mc.mouseChildren = false
        #globe.root.formation_leap_mc.mouseEnabled = false
        #globe.root.formation_leap_mc.mouseChildren = false
        #globe.root.formation_peep_diagonal_mc.mouseEnabled = false
        #globe.root.formation_peep_diagonal_mc.mouseChildren = false
        #globe.root.formation_peep_knight_mc.mouseEnabled = false
        #globe.root.formation_peep_knight_mc.mouseChildren = false
        #globe.root.formation_peep_mc.mouseEnabled = false
        #globe.root.formation_peep_mc.mouseChildren = false
        #globe.root.formation_quarter_field_mc.mouseEnabled = false
        #globe.root.formation_quarter_field_mc.mouseChildren = false
        #globe.root.formation_tiger_jaw_mc.mouseEnabled = false
        #globe.root.formation_tiger_jaw_mc.mouseChildren = false
        #globe.root.formation_tiger_mouth_mc.mouseEnabled = false
        #globe.root.formation_tiger_mouth_mc.mouseChildren = false

    def setup_events(globe):
        '''
        Archive original stage.
        >>> code_unit.doctest_unit(globe_class.save_one_child, log = false);
        '''
        globe.original_stage = compose_root(insert_label_and_position,
                globe.root['title_mc']);
        del globe.original_stage['title_mc']['username_txt'];
        del globe.original_stage['title_mc']['password_txt'];
        globe.root.log_txt.text = 'log'
        var = news_log = compose_root(insert_label_and_position,
                globe.root['log_txt']);
        globe.original_stage = upgrade(globe.original_stage, news_log);
        globe.root.gotoAndPlay('login');
        globe.root.score_mc.bar_mc.gotoAndPlay('_0');
        globe.root.score_mc.bar_mc.marker_mc.capture_mc.gotoAndPlay('_0');
        globe.root.score_mc.bar_mc.marker_mc.change_txt.text = '0'
        globe.root.gateway_mc.none_mc.addEventListener(
                MouseEvent.MOUSE_DOWN, globe.parent_goto_mc_name);
        globe.root.comment_mc.none_mc.addEventListener(
                MouseEvent.MOUSE_DOWN, globe.parent_goto_mc_name);
        globe.root.chat_input_mc.addEventListener(
                MouseEvent.MOUSE_DOWN, globe.chat_input);
        globe.root.title_mc.start_btn.addEventListener(
                MouseEvent.MOUSE_DOWN, globe.login);
        globe.root.lobby_mc.level_1_mc.enter_btn.addEventListener(
                MouseEvent.MOUSE_DOWN, globe.enter_level_1);
        globe.root.lobby_mc.create_mc.addEventListener(
                MouseEvent.MOUSE_DOWN, globe.create_table);
        globe.root.lobby_mc.join_mc.enter_btn.addEventListener(
                MouseEvent.MOUSE_DOWN, globe.join_table);
        globe.root.game_over_mc.start_mc.addEventListener(
                MouseEvent.MOUSE_DOWN, globe.start_game);
        globe.root.game_over_mc.score_mc.lobby_mc.addEventListener(
                MouseEvent.MOUSE_DOWN, globe.remove_table);
        globe.root.save_mc.addEventListener(
                MouseEvent.MOUSE_DOWN, globe.save_stage);
        globe.root.load_mc.addEventListener(
                MouseEvent.MOUSE_DOWN, globe.load_stage);
        #- globe.root.turn_mc.white_mc.enter_btn.addEventListener(
        #-         MouseEvent.MOUSE_DOWN, globe.become_white);
        globe.root.extra_stone_gift_mc.use_mc.addEventListener(
                MouseEvent.MOUSE_DOWN, globe.extra_stone);
        globe.root.hide_gift_mc.use_mc.addEventListener(
                MouseEvent.MOUSE_DOWN, globe.hide);
        globe.root.pass_mc.addEventListener(
                MouseEvent.MOUSE_DOWN, globe.do_pass);
        globe.root.suicide_mc.enter_mc.addEventListener(
                MouseEvent.MOUSE_DOWN, globe.toggle_option);
        globe.root.option_mc.score_mc.enter_mc.addEventListener(
                MouseEvent.MOUSE_DOWN, globe.toggle_option);
        globe.root.option_mc.computer_pass_mc.enter_mc.addEventListener(
                MouseEvent.MOUSE_DOWN, globe.toggle_option);
        globe.root.option_mc.first_capture_mc.enter_mc.addEventListener(
                MouseEvent.MOUSE_DOWN, globe.toggle_option);
        globe.root.clock_mc.enter_mc.enter_btn.addEventListener(
                MouseEvent.MOUSE_DOWN, globe.activate_clock);
        globe.root.level_mc.none_mc.addEventListener(
                MouseEvent.MOUSE_DOWN, globe.parent_goto_mc_name);
        globe.root.theme_txt.addEventListener(
                TextEvent.TEXT_INPUT, globe.set_theme_txt);
        globe.root.cursor_mc.mouseEnabled = false;
        globe.root.cursor_mc.mouseChildren = false;
        #- globe.root.black_last_move_mc.mouseEnabled = false;
        #- globe.root.black_last_move_mc.mouseChildren = false;
        #- globe.root.white_last_move_mc.mouseEnabled = false;
        #- globe.root.white_last_move_mc.mouseChildren = false;
        globe.root.eat_mc.mouseEnabled = false;
        globe.root.eat_mc.mouseChildren = false;
        globe.root.addEventListener(MouseEvent.MOUSE_MOVE, globe.follow);
        globe.root.addEventListener(MouseEvent.MOUSE_DOWN, globe.mouse_shield);
        globe.setup_formations();
        globe.board_listens_to_mouse(globe.intersection_mc_array);
        globe.listen_to_game_over();
        globe.listen_to_lobby();
        globe._finish_flash_setup();
        globe.root.addEventListener(Event.ENTER_FRAME, globe.update);

    def listen_to_parent(globe, parent_name):
        '''May also listen to mouseOver or mouseOut.
            on mouse over:
                if opening note and length greater than or equal to 2:
                    copy opening note from info_txt.text to info_mc._txt.text
                    show info
            on mouse out:
                if show info:
                    hide info
        >>> marije = globe_class()
        >>> marije.create()
        >>> marije.setup_events()
        >>> marije.ambassador = echo_protocol_class()
        >>> target = marije.root.lobby_mc._00_mc.capture_3_3_mc
        >>> target.info_txt.text = 'Surround a fire.'
        >>> marije.root.info_mc.currentLabel
        'none'
        >>> target.dispatchEvent(mouseOver)
        >>> marije.root.info_mc.currentLabel
        'show'
        >>> marije.root.info_mc.currentLabel
        'show'
        >>> target.dispatchEvent(mouseOut)
        >>> marije.root.info_mc.currentLabel
        'none'

        On click lobby, notify server.
        >>> marije.root.lobby_mc.main_mc._00_mc.dispatchEvent(mouseDown)
        >>> marije.ambassador.sends[-1]['lobby_mc']['main_mc']['_00_mc']['dispatchEvent']
        'mouseDown'
        >>> marije.root.lobby_mc._00_mc.main_mc.dispatchEvent(mouseDown)
        >>> marije.ambassador.sends[-1]['lobby_mc']['_00_mc']['main_mc']['dispatchEvent']
        'mouseDown'
        '''
        globe.root.lobby_mc.main_mc[parent_name].addEventListener(
                MouseEvent.MOUSE_DOWN, globe.grandparent_goto_mc_name);
        globe.root.lobby_mc[parent_name].main_mc.addEventListener(
                MouseEvent.MOUSE_DOWN, globe.grandparent_goto_mc_name);
        children_listen_to_mouse(globe.root.lobby_mc[parent_name], 
                MouseEvent.MOUSE_DOWN, globe.problem_name, 'main_mc');
        children_listen_to_mouse(globe.root.lobby_mc[parent_name], 
                MouseEvent.MOUSE_OVER, globe.show_menu_info, 'main_mc');
        children_listen_to_mouse(globe.root.lobby_mc[parent_name], 
                MouseEvent.MOUSE_OUT, globe.hide_info, 'main_mc');

    def listen_to_lobby(globe):
        globe.listen_to_parent('_00_mc');
        globe.listen_to_parent('_04_mc');
        globe.listen_to_parent('_07_mc');
        globe.listen_to_parent('_10_mc');
        globe.listen_to_parent('_14_mc');
        globe.listen_to_parent('_20_mc');
        globe.root.lobby_mc.main_mc.multiplayer_mc.addEventListener(
                MouseEvent.MOUSE_DOWN, globe.grandparent_goto_mc_name);
        globe.root.lobby_mc._main_mc.addEventListener(
                MouseEvent.MOUSE_DOWN, globe.parent_goto_mc_name);
        globe.root.lobby_mc.main_mc.login_mc.addEventListener(
                MouseEvent.MOUSE_DOWN, globe.great_grandparent_goto_mc_name);
        globe.root.lobby_mc.enter_mc.addEventListener(
                MouseEvent.MOUSE_DOWN, globe.enter_lobby);
        globe.root.menu_mc.toggle_mc.addEventListener(
                MouseEvent.MOUSE_DOWN, globe.toggle_menu);
        globe.root.menu_mc.lobby_mc.addEventListener(
                MouseEvent.MOUSE_DOWN, globe.remove_table);
        #globe.root.lobby_mc._00_mc.capture_5_5_mc.addEventListener(
        #        MouseEvent.MOUSE_DOWN, globe.problem_name);
        #globe.root.lobby_mc._00_mc.capture_3_3_mc.addEventListener(
        #        MouseEvent.MOUSE_DOWN, globe.problem_name);
        #globe.root.lobby_mc._00_mc.dominate_3_3_mc.addEventListener(
        #        MouseEvent.MOUSE_DOWN, globe.problem_name);
        #globe.root.lobby_mc._00_mc.dominate_5_5_mc.addEventListener(
        #        MouseEvent.MOUSE_DOWN, globe.problem_name);
        #globe.root.lobby_mc._00_mc.score_5_5_mc.addEventListener(
        #        MouseEvent.MOUSE_DOWN, globe.problem_name);
        #globe.root.lobby_mc._10_mc.extra_stone_5_5_mc.addEventListener(
        #        MouseEvent.MOUSE_DOWN, globe.problem_name);
        #globe.root.lobby_mc._10_mc.extra_stone_5_5_2_mc.addEventListener(
        #        MouseEvent.MOUSE_DOWN, globe.problem_name);
        #globe.root.lobby_mc._10_mc.extra_stone_7_7_mc.addEventListener(
        #        MouseEvent.MOUSE_DOWN, globe.problem_name);
        #globe.root.lobby_mc._10_mc.extra_stone_7_7_2_mc.addEventListener(
        #        MouseEvent.MOUSE_DOWN, globe.problem_name);
        #globe.root.lobby_mc._10_mc.extra_stone_7_7_3_mc.addEventListener(
        #        MouseEvent.MOUSE_DOWN, globe.problem_name);
        #globe.root.lobby_mc._10_mc.extra_stone_7_7_4_mc.addEventListener(
        #        MouseEvent.MOUSE_DOWN, globe.problem_name);
        #globe.root.lobby_mc._10_mc.extra_stone_9_9_mc.addEventListener(
        #        MouseEvent.MOUSE_DOWN, globe.problem_name);
        #globe.root.lobby_mc._10_mc.extra_stone_9_9_2_mc.addEventListener(
        #        MouseEvent.MOUSE_DOWN, globe.problem_name);
        #globe.root.lobby_mc._10_mc.extra_stone_9_9_3_mc.addEventListener(
        #        MouseEvent.MOUSE_DOWN, globe.problem_name);
        #globe.root.lobby_mc._20_mc.hide_5_5_mc.addEventListener(
        #        MouseEvent.MOUSE_DOWN, globe.problem_name);
        #globe.root.lobby_mc._20_mc.hide_7_7_mc.addEventListener(
        #        MouseEvent.MOUSE_DOWN, globe.problem_name);
        #globe.root.lobby_mc._00_mc.capture_3_3_mc.addEventListener(
        #        MouseEvent.MOUSE_DOWN, globe.problem);
        #globe.root.lobby_mc._00_mc.capture_5_5_mc.addEventListener(
        #        MouseEvent.MOUSE_DOWN, globe.problem);
        #globe.root.lobby_mc._00_mc.dominate_3_3_mc.addEventListener(
        #        MouseEvent.MOUSE_DOWN, globe.problem);
        #globe.root.lobby_mc._00_mc.dominate_5_5_mc.addEventListener(
        #        MouseEvent.MOUSE_DOWN, globe.problem);
        #globe.root.lobby_mc._00_mc.score_5_5_mc.addEventListener(
        #        MouseEvent.MOUSE_DOWN, globe.problem);
        #globe.root.lobby_mc._00_mc.extra_stone_7_7_mc.addEventListener(
        #        MouseEvent.MOUSE_DOWN, globe.problem);
        #globe.root.lobby_mc._00_mc.extra_stone_7_7_2_mc.addEventListener(
        #        MouseEvent.MOUSE_DOWN, globe.problem);
        #globe.root.lobby_mc._00_mc.extra_stone_9_9_mc.addEventListener(
        #        MouseEvent.MOUSE_DOWN, globe.problem);
        #globe.root.lobby_mc._00_mc.hide_5_5_mc.addEventListener(
        #        MouseEvent.MOUSE_DOWN, globe.problem);
        #globe.root.lobby_mc._00_mc.hide_7_7_mc.addEventListener(
        #        MouseEvent.MOUSE_DOWN, globe.problem);
        #- globe.root.lobby_mc.single_player_mc.addEventListener(
        #-         MouseEvent.MOUSE_DOWN, globe.parent_goto_mc_name);

    def listen_to_game_over(globe):
        globe.root.game_over_mc._3_3_mc.enter_mc.addEventListener(
                MouseEvent.MOUSE_DOWN, globe.board_3_3);
        globe.root.game_over_mc._3_3_mc.confirm_mc.addEventListener(
                MouseEvent.MOUSE_DOWN, globe.confirm_board_3_3);
        globe.root.game_over_mc._5_5_mc.enter_mc.addEventListener(
                MouseEvent.MOUSE_DOWN, globe.board_5_5);
        globe.root.game_over_mc._5_5_mc.confirm_mc.addEventListener(
                MouseEvent.MOUSE_DOWN, globe.confirm_board_5_5);
        globe.root.game_over_mc._7_7_mc.enter_mc.addEventListener(
                MouseEvent.MOUSE_DOWN, globe.board_7_7);
        globe.root.game_over_mc._7_7_mc.confirm_mc.addEventListener(
                MouseEvent.MOUSE_DOWN, globe.confirm_board_7_7);
        globe.root.game_over_mc._9_9_mc.enter_mc.addEventListener(
                MouseEvent.MOUSE_DOWN, globe.board_9_9);
        globe.root.game_over_mc._9_9_mc.confirm_mc.addEventListener(
                MouseEvent.MOUSE_DOWN, globe.confirm_board_9_9);
        globe.root.game_over_mc.white_computer_mc.enter_mc.addEventListener(
                MouseEvent.MOUSE_DOWN, globe.white_computer);
        globe.root.game_over_mc.extra_stone_available_mc._0_mc.addEventListener(
                MouseEvent.MOUSE_DOWN, globe.adjust_level_balance);
        globe.root.game_over_mc.extra_stone_available_mc._1_mc.addEventListener(
                MouseEvent.MOUSE_DOWN, globe.adjust_level_balance);
        globe.root.game_over_mc.extra_stone_available_mc._2_mc.addEventListener(
                MouseEvent.MOUSE_DOWN, globe.adjust_level_balance);
        globe.root.game_over_mc.extra_stone_available_mc._3_mc.addEventListener(
                MouseEvent.MOUSE_DOWN, globe.adjust_level_balance);
        globe.root.game_over_mc.extra_stone_available_mc._4_mc.addEventListener(
                MouseEvent.MOUSE_DOWN, globe.adjust_level_balance);
        globe.root.game_over_mc.extra_stone_available_mc._5_mc.addEventListener(
                MouseEvent.MOUSE_DOWN, globe.adjust_level_balance);
        globe.root.game_over_mc.extra_stone_available_mc._6_mc.addEventListener(
                MouseEvent.MOUSE_DOWN, globe.adjust_level_balance);
        globe.root.game_over_mc.extra_stone_available_mc._7_mc.addEventListener(
                MouseEvent.MOUSE_DOWN, globe.adjust_level_balance);
        globe.root.game_over_mc.extra_stone_available_mc._8_mc.addEventListener(
                MouseEvent.MOUSE_DOWN, globe.adjust_level_balance);
        globe.root.game_over_mc.extra_stone_available_mc._9_mc.addEventListener(
                MouseEvent.MOUSE_DOWN, globe.adjust_level_balance);
        globe.root.game_over_mc.hide_available_mc._0_mc.addEventListener(
                MouseEvent.MOUSE_DOWN, globe.adjust_level_balance);
        globe.root.game_over_mc.hide_available_mc._1_mc.addEventListener(
                MouseEvent.MOUSE_DOWN, globe.adjust_level_balance);
        globe.root.game_over_mc.hide_available_mc._2_mc.addEventListener(
                MouseEvent.MOUSE_DOWN, globe.adjust_level_balance);
        globe.root.game_over_mc.hide_available_mc._3_mc.addEventListener(
                MouseEvent.MOUSE_DOWN, globe.adjust_level_balance);
        globe.root.game_over_mc.hide_available_mc._4_mc.addEventListener(
                MouseEvent.MOUSE_DOWN, globe.adjust_level_balance);
        globe.root.game_over_mc.hide_available_mc._5_mc.addEventListener(
                MouseEvent.MOUSE_DOWN, globe.adjust_level_balance);
        globe.root.game_over_mc.hide_available_mc._6_mc.addEventListener(
                MouseEvent.MOUSE_DOWN, globe.adjust_level_balance);
        globe.root.game_over_mc.hide_available_mc._7_mc.addEventListener(
                MouseEvent.MOUSE_DOWN, globe.adjust_level_balance);
        globe.root.game_over_mc.hide_available_mc._8_mc.addEventListener(
                MouseEvent.MOUSE_DOWN, globe.adjust_level_balance);
        globe.root.game_over_mc.hide_available_mc._9_mc.addEventListener(
                MouseEvent.MOUSE_DOWN, globe.adjust_level_balance);
        
    def _finish_flash_setup(globe): 
        '''HACK:  Only in Flash client.  Do not export. see lifeanddeath.as'''
        pass

    def setup(globe, mock_speed, setup_client):
        '''This starts client, so do not setup in embassy 
        if you do not want the client to setup in the embassy.
        '''
        globe.create(mock_speed)  ## mock flash only
        globe.setup_events()
        globe.ambassador = setup_client(globe)  ## flash needs client global.

    def insert_credentials(globe, message):
        username = globe.root.title_mc.username_txt.text
        password = globe.root.title_mc.password_txt.text
        master = globe.root.title_mc.master_txt.text
        slave = globe.root.title_mc.slave_txt.text
        news = {
                'title_mc': {
                    'username_txt': {'text': username},
                    'password_txt': {'text': password},
                    'master_txt': {'text': master},
                    'slave_txt': {'text': slave}
                }
            }
        message = upgrade(message, news)
        return message

    def update_log(globe, message):
        r'''Reverse order line per message.
        >>> laurens = globe_class()
        >>> laurens.create()
        >>> laurens.setup_events() # clear the log.
        >>> laurens.update_log('hoi')
        >>> laurens.root.log_txt.text
        'hoi\nlog'
        >>> laurens.update_log('hoe heet je?')
        >>> print laurens.root.log_txt.text
        hoe heet je?
        hoi
        log
        '''
        logging.info(message)
        globe.root.log_txt.text = message + '\n' + globe.root.log_txt.text

    #def parent_goto_none(globe, mouse_event):
    #    '''
    #    >>> lukasz = globe_class()
    #    >>> lukasz.create()
    #    >>> lukasz.ambassador = echo_protocol_class()
    #    >>> lukasz.root.gateway_mc.gotoAndPlay('connect')
    #    >>> mouse_event = MouseEvent(MouseEvent.MOUSE_DOWN)
    #    >>> mouse_event.currentTarget = lukasz.root.gateway_mc.close_btn
    #    >>> lukasz.parent_goto_none(mouse_event)
    #    >>> lukasz.root.gateway_mc.currentLabel
    #    'none'
    #    '''
    #    display_object = mouse_event.currentTarget
    #    if undefined != display_object.parent:
    #        news = note(display_object.parent, 'currentLabel', 'none')
    #        globe.publish(news)

    def login(globe, mouse_event):
        news = {
            'gateway_mc': {
                'currentLabel': 'enter'
            }
        }
        globe.publish(news)

    def enter_level_1(globe, mouse_event):
        news = {
            'lobby_mc': {
                'level_1_mc': {
                    'currentLabel': 'enter'
                }
            }
        }
        globe.publish(news)

    def create_table(globe, mouse_event):
        news = {
            'lobby_mc': {
                'create_mc': {
                    'currentLabel': 'enter'
                }
            }
        }
        globe.publish(news)

    def join_table(globe, mouse_event):
        news = {
            'lobby_mc': {
                'join_mc': {
                    'currentLabel': 'enter'
                }
            }
        }
        globe.publish(news)

    def start_game(globe, mouse_event):
        news = {
            'game_over_mc': {
                'start_mc': {
                    'currentLabel': 'enter'
                }
            }
        }
        globe.publish(news)

    def extra_stone(globe, mouse_event):
        news = get_extra_stone_news()
        globe.publish(news)

    def hide(globe, mouse_event):
        news = get_hide_news()
        globe.publish(news)

    #def do_pass(globe, mouse_event):
    #    logging.info('do_pass:  starting')
    #    news = note(mouse_event.currentTarget, 'currentLabel', 'enter')
    #    globe.publish(news)

    def toggle_option(globe, mouse_event):
        '''
        >>> emmet = setup_echo(globe_class)
        >>> emmet.root.suicide_mc.currentLabel
        'none'
        >>> emmet.root.suicide_mc.enter_mc.currentLabel
        'none'
        >>> emmet.root.suicide_mc.enter_mc.dispatchEvent(mouseDown)
        >>> emmet.ambassador.sends[-1].get('suicide_mc')
        {'enter_mc': {'currentLabel': 'enter', 'dispatchEvent': 'mouseDown'}}
        >>> emmet.root.suicide_mc.enter_mc.currentLabel
        'enter'
        >>> emmet.root.suicide_mc.currentLabel
        'none'

        Toggle score option
        >>> emmet.root.option_mc.score_mc.enter_mc.dispatchEvent(mouseDown)
        >>> emmet.ambassador.sends[-1].get('option_mc')
        {'score_mc': {'enter_mc': {'currentLabel': 'enter', 'dispatchEvent': 'mouseDown'}}}
        '''
        logging.info('toggle_option:  starting')
        news = {}
        enter_news = note(mouse_event.currentTarget, 'currentLabel', 'enter')
        globe.revise(enter_news)
        news = upgrade(news, enter_news)
        event_news = note(mouse_event.currentTarget, 'dispatchEvent', mouse_event.type)
        news = upgrade(news, event_news)
        my_news = globe.insert_credentials(news)
        globe.ambassador.send(my_news)

    def board_3_3(globe, mouse_event):
        logging.info('board_3_3:  starting')
        news = note(mouse_event.currentTarget, 'currentLabel', 'enter')
        globe.publish(news)

    def confirm_board_3_3(globe, mouse_event):
        globe.confirm_board_size('_3_3')

    def board_5_5(globe, mouse_event):
        logging.info('board_5_5:  starting')
        news = note(mouse_event.currentTarget, 'currentLabel', 'enter')
        globe.publish(news)

    def confirm_board_5_5(globe, mouse_event):
        globe.confirm_board_size('_5_5')

    def board_7_7(globe, mouse_event):
        logging.info('board_7_7:  starting')
        news = note(mouse_event.currentTarget, 'currentLabel', 'enter')
        globe.publish(news)

    def confirm_board_7_7(globe, mouse_event):
        globe.confirm_board_size('_7_7')

    def board_9_9(globe, mouse_event):
        logging.info('board_9_9:  starting')
        news = note(mouse_event.currentTarget, 'currentLabel', 'enter')
        globe.publish(news)

    def confirm_board_9_9(globe, mouse_event):
        globe.confirm_board_size('_9_9')

    def confirm_board_size(globe, size):
        '''Constrain and snap intersections to the board.
        >>> laurens = globe_class()
        >>> laurens.create()
        >>> laurens.setup_events()
        >>> laurens.ambassador = echo_protocol_class()
        >>> laurens.confirm_board_size('_5_5')
        >>> len(laurens.intersection_mc_array)
        5
        >>> laurens.root.currentLabel
        '_5_5'

        Snap intersections.
        >>> laurens.root._0_0_mc.x
        100

        Do not leave lobby.
        >>> laurens.root.gotoAndPlay('lobby')
        >>> laurens.confirm_board_size('_9_9')
        >>> laurens.root.currentLabel
        'lobby'
        '''
        logging.info('confirm_board'+ size +':  starting');
        # ActionScript gotcha [1] --> .charAt(1)
        size = String(size);
        var = length = int(size.charAt(1)); 
        globe.intersection_mc_array = get_intersection_array(
                globe.root, length);
        var = size_news = {};
        # ActionScript gotcha {a: 1} == {'a': 1}
        size_news[size + '_mc'] = {
            'enter_mc': {
                'currentLabel': 'none'
            }
        }
        var = news = {
            'game_over_mc': size_news
        }
        if ('lobby' != globe.root.currentLabel):
            news['currentLabel'] = size;
        globe.revise(news);
        globe.snap_intersections(length);
        #- globe.publish_x_y(globe.intersection_mc_array)

    def snap_intersections(globe, intersection_per_line, stage_pixel = 600,
            original_pixel_per_space = 60, offstage = 1000, 
            max_intersection_per_line = 9):
        '''Snap intersection and strike.  Move excess off-stage.
        >>> moonhyoung = globe_class()
        >>> moonhyoung.create(1)
        >>> moonhyoung.snap_intersections(9, 600)
        >>> moonhyoung.root._0_0_mc.x
        60
        >>> moonhyoung.root._0_0_mc.y
        60
        >>> moonhyoung.root._8_8_mc.x
        540
        >>> moonhyoung.root._8_8_mc.y
        540
        >>> moonhyoung.root._8_8_mc.scaleX
        1.0
        >>> moonhyoung.root._8_8_mc.scaleY
        1.0
        >>> moonhyoung.snap_intersections(3, 600)
        >>> moonhyoung.root._0_0_mc.x
        150
        >>> moonhyoung.root._0_0_mc.y
        150
        >>> moonhyoung.root._8_8_mc.x
        1000
        >>> moonhyoung.root._8_8_mc.y
        1000
        >>> moonhyoung.root._8_8_mc.scaleX
        2.5
        >>> moonhyoung.root._8_8_mc.scaleY
        2.5
        '''
        var = gutters = 1;
        var = pixel_per_space = stage_pixel \
                / (intersection_per_line + gutters);
        var = scale = float(pixel_per_space) / original_pixel_per_space;
        for row in range(max_intersection_per_line):
            var = y = offstage;
            if (row < intersection_per_line):
                y = pixel_per_space + (pixel_per_space * row);
            for column in range(max_intersection_per_line):
                var = x = offstage;
                if (column < intersection_per_line):
                    x = pixel_per_space + (pixel_per_space * column);
                var = name = '_' + str(row) + '_' + str(column) + '_mc';
                var = _mc = globe.root[name];
                _mc.x = x;
                _mc.y = y;
                _mc.scaleX = scale;
                _mc.scaleY = scale;
                var = strike_name = '_' + str(row) \
                        + '_' + str(column) + '_strike_mc';
                var = strike_mc = globe.root[strike_name];
                strike_mc.x = x;
                strike_mc.y = y;
                strike_mc.scaleX = scale;
                strike_mc.scaleY = scale;


    #def problem(globe, mouse_event):
    #    '''DEPRECATED?'''
    #    problem_name = mouse_event.currentTarget.parent.name
    #    news = get_problem_news(problem_name)
    #    # see toggle_option, log_example
    #    globe.revise(news)
    #    event_news = note(mouse_event.currentTarget, 'dispatchEvent', mouse_event.type)
    #    news = upgrade(news, event_news)
    #    my_news = globe.insert_credentials(news)
    #    globe.ambassador.send(my_news)
    #    #- globe.publish(news)

    def _publish_event(globe, mouse_event, news):
        mc_news = note(mouse_event.currentTarget, 
            'currentLabel', 'enter')
        news = upgrade(news, mc_news)
        globe.revise(news)
        event_news = note(mouse_event.currentTarget, 
            'dispatchEvent', mouse_event.type)
        news = upgrade(news, event_news)
        my_news = globe.insert_credentials(news)
        globe.ambassador.send(my_news)
        
    def parent_goto_mc_name(globe, mouse_event):
        '''In lobby, request to goto single player or multiplayer.
        >>> jade = globe_class()
        >>> jade.create()
        >>> jade.setup_events()
        >>> jade.ambassador = echo_protocol_class()
        >>> from pprint import pprint
        >>> jade.root.lobby_mc.gotoAndPlay('single_player')
        >>> jade.root.lobby_mc.main_mc.multiplayer_mc.dispatchEvent(mouseDown)
        >>> multiplayer_news = jade.ambassador.sends[-1]
        >>> pprint(multiplayer_news.get('lobby_mc'))
        {'main_mc': {'multiplayer_mc': {'currentLabel': 'enter',
                                        'dispatchEvent': 'mouseDown'}}}
        >>> jade.root.lobby_mc.gotoAndPlay('multiplayer')
        >>> jade.root.lobby_mc.main_mc._00_mc.dispatchEvent(mouseDown)
        >>> single_player_news = jade.ambassador.sends[-1]
        >>> pprint(single_player_news.get('lobby_mc'))
        {'main_mc': {'_00_mc': {'currentLabel': 'enter',
                                'dispatchEvent': 'mouseDown'}}}
        >>> jade.root.game_over_mc.extra_stone_available_mc._1_mc.dispatchEvent(mouseDown)
        >>> jade.root.game_over_mc.hide_available_mc._2_mc.dispatchEvent(mouseDown)
        >>> jade.root.lobby_mc._00_mc.capture_3_3_mc.dispatchEvent(mouseDown)
        >>> jade.root.lobby_mc.main_mc._00_mc.dispatchEvent(mouseDown)
        >>> jade.root.lobby_mc.main_mc._10_mc.dispatchEvent(mouseDown)
        >>> jade.root.lobby_mc.main_mc._20_mc.dispatchEvent(mouseDown)

        Link all menu items in stage except back to main.
        >>> jade.root.lobby_mc._20_mc.hide_7_7_mc.dispatchEvent(mouseDown)
        >>> jade.root.lobby_mc._20_mc.extra_hide_7_7_mc.dispatchEvent(mouseDown)
        >>> single_player_news = jade.ambassador.sends[-1]
        >>> pprint(single_player_news.get('lobby_mc'))
        {'_20_mc': {'extra_hide_7_7_mc': {'currentLabel': 'enter',
                                          'dispatchEvent': 'mouseDown'}}}
        '''
        globe._publish_event(mouse_event, {})

    var = author_parent_goto_mc_name = parent_goto_mc_name;
    var = remove_table = parent_goto_mc_name;
    var = toggle_menu = parent_goto_mc_name;
    var = problem_name = parent_goto_mc_name;
    var = grandparent_goto_mc_name = parent_goto_mc_name;
    var = great_grandparent_goto_mc_name = parent_goto_mc_name;
    var = adjust_level_balance = author_parent_goto_mc_name;
    var = do_pass = parent_goto_mc_name;

    def chat_input(globe, mouse_event):
        '''Send chat text to server.
        >>> jade = globe_class()
        >>> jade.create()
        >>> jade.setup_events()
        >>> jade.ambassador = echo_protocol_class()
        >>> from pprint import pprint
        >>> jade.root.chat_input_txt.text = 'hello'
        >>> jade.root.chat_input_mc.dispatchEvent(mouseDown)
        >>> jade.ambassador.sends[-1].get('chat_input_txt')
        {'text': 'hello'}
        >>> jade.ambassador.sends[-1].get('chat_input_mc')
        {'currentLabel': 'enter', 'dispatchEvent': 'mouseDown'}
        '''
        chat_news = get_note(globe.root.chat_input_txt, 'text')
        globe._publish_event(mouse_event, chat_news)

    def white_computer(globe, mouse_event):
        news = {
            'game_over_mc': {
                'white_computer_mc': {
                    'enter_mc': {'currentLabel': 'enter'}
                }
            }
        } 
        globe.publish(news)

    def enter_lobby(globe, mouse_event):
        news = {
            'lobby_mc': {
                'enter_mc': {'currentLabel': 'enter'}
            }
        } 
        globe.publish(news)

    def activate_clock(globe, mouse_event):
        logging.info('activate_clock:  starting')
        news = {
            'clock_mc': {
                'enter_mc': {'currentLabel': 'enter'}
            }
        } 
        globe.publish(news)

    def publish(globe, news):
        '''Edits news!
        >>> laurens = globe_class()
        >>> laurens.create()
        >>> laurens.setup_events()
        >>> laurens.root.title_mc.username_txt.text = 'laurens'
        >>> laurens.root.title_mc.password_txt.text = 'l'
        >>> laurens.ambassador = echo_protocol_class()
        >>> news = {'title_mc': {'username_txt': {'text': 'ethan'}}}
        >>> laurens.current
        {}
        >>> laurens.publish(news)
        >>> news['title_mc']['password_txt']['text']
        'l'

        Remembers news to recreate current published state.
        Beware: ignores unpublished password.
        >>> laurens.current['title_mc']['username_txt']['text']
        'ethan'
        >>> news = {'title_mc': {'password_txt': {'text': 'e'}}}
        >>> laurens.publish(news)
        >>> laurens.current['title_mc']['password_txt']['text']
        'e'

        Sends current time.
        >>> now = laurens.ambassador.sends[-1]['title_mc']['time_txt']['text']
        >>> now = int(now)
        >>> if not getTimer() <= now + 50:  now
        '''
        ## print flash_to_text(globe.intersection_mc_array)
        var = now = getTimer();
        var = time_news = {'title_mc': {'time_txt': {'text': str(now)}}};
        news = upgrade(news, time_news);
        globe.revise(news);
        my_news = globe.insert_credentials(news);
        globe.ambassador.send(my_news);

        
    def pb(globe):
        '''conveniently print board'''
        from embassy import flash_to_text
        print flash_to_text(globe.intersection_mc_array)

    def save_one_child(globe, root, child_list):
        '''At end, revert original master, slave, but not username or password.
        >>> laurens = globe_class()
        >>> laurens.create()
        >>> laurens.setup_events()
        >>> laurens.ambassador = print_protocol_class()
        >>> laurens.root.title_mc.username_txt.text = 'laurens'
        >>> laurens.root.title_mc.password_txt.text = 'l'
        >>> laurens.root.title_mc.master_txt.text = '777'
        >>> laurens.root.title_mc.slave_txt.text = '666'

        >>> old_log_level = logging.getLogger().level
        >>> logging.getLogger().setLevel(logging.CRITICAL)

        If nothing, do nothing and return empty list.
        >>> laurens.save_one_child(laurens.root, []) #doctest: +ELLIPSIS
        []

        If nothing, do nothing and return empty list.
        >>> laurens.save_one_child(laurens.root, [None]) #doctest: +ELLIPSIS
        []

        Revert master and return popped list.
        >>> laurens.save_one_child(laurens.root, [MovieClip()]) #doctest: +ELLIPSIS
        {...'master_txt': {'text': 'master'}...
        []

        Do not transmit log_txt and return popped list.
        >>> laurens.save_one_child(laurens.root, [MovieClip()]) #doctest: +ELLIPSIS
        {...'log_txt': {'text': 'log'}...
        []
            
        Do not transmit log_txt, which may be too large or contain indecipherable characters.
        >>> messy_log_txt = TextField()
        >>> messy_log_txt.name = 'log_txt'
        >>> messy_log_txt.text = '161 readResponse:  result = [object Object]\rreadResponse:  status:  \rbytesAvailable = 143; event.bytesLoaded = 143; attempt = 0\rimitate complete\rsend:  [object Object]\r160 readResponse:  result = [object Object]\rreadResponse:  status:  \rbytesAvailable = 143; event.bytesLoaded = 143;'
        
        >>> laurens.save_one_child(laurens.root, [messy_log_txt, MovieClip()]) #doctest: +ELLIPSIS
        {...'log_txt': {'text': 'log'}...
        [<actionscript.MovieClip object at 0x...>]

        >>> logging.getLogger().setLevel(old_log_level)
        '''
        if (0 == count_item(child_list)):
            return [];
        var = news = globe.insert_credentials({});
        var = child = child_list.pop(0); # XXX .as --> child_list.shift()
        var = save_child = {};
        if (null == child):
            globe.update_log('error ' + str(child));
            logging.error('save_one_child: empty ' + str(child));
            return child_list;
        elif ('log_txt' == child.name):
            save_child['log_txt'] = {};
            save_child['log_txt']['text'] = 'log';
        else:
            logging.info('save_one_child: ' + child.name);
            save_child = compose_root(insert_label_and_position, child);
        news = upgrade(news, save_child);
        var = save = {};
        if (1 <= len(child_list)):
            root['save_mc'].gotoAndPlay('entering');
            save = compose_root(insert_label, root['save_mc']);
        else:
            root['save_mc'].gotoAndPlay('enter');
            save = compose_root(insert_label_and_position, 
                root['save_mc']);
            save = insert_label_and_position(root, save);
            save = upgrade(save, globe.original_stage);
        news = upgrade(news, save);
        globe.ambassador.send(news);
        return child_list;

    def set_theme_txt(globe, text_event):
        '''on input text, set theme.
        Only defined in ActionScript?'''
        trace("set_theme_txt:  " + text_event.text)
        set_theme(intersection_mc_array, text_event.text)

    def save_stage(globe, mouse_event):
        '''Because 96 kB leads server to complain of error, save in parts.'''
        logging.info('save_stage:  starting')
        globe.save_list = [ globe.root.getChildAt(c)
                for c in range(globe.root.numChildren) ]
        globe.save_list = globe.save_one_child(globe.root, globe.save_list)

    def load_stage(globe, mouse_event):
        '''Because 96 kB leads server to complain of error, load in parts.'''
        logging.info('load_stage:  starting')
        globe.root['load_mc'].gotoAndPlay('entering')
        message = compose_root(insert_label,
                globe.credentials, globe.root['load_mc'])
        globe.ambassador.send(message)

    def play_stone(globe, mouse_event):
        '''Press an intersection, play.
        If preview enabled, change intersection into a preview.  
        Look for intersections that may be in preview.  revert these.
        >>> laurens = globe_class()
        >>> laurens.create(1)
        >>> laurens.ambassador = echo_protocol_class()
        >>> laurens.setup_events()
        >>> laurens.root.preview_gift_mc.enabled_mc.gotoAndPlay('show')
        >>> mouse_event = MouseEvent(MouseEvent.MOUSE_DOWN)
        >>> mouse_event.currentTarget = laurens.root._0_0_mc
        >>> laurens.play_stone(mouse_event)
        >>> laurens.root._0_0_mc.currentLabel
        'preview_black'

        Until server says not busy.
        >>> laurens.root.cursor_mc.act_mc.gotoAndPlay('none')
        >>> mouse_event.currentTarget = laurens.root._0_1_mc
        >>> laurens.play_stone(mouse_event)
        >>> laurens.root._0_0_mc.currentLabel
        'empty_black'

        Do not send emptied intersection to server.
        >>> laurens.ambassador.sends[-1].get('_0_0_mc')

        Moonhyoung prefers to play immediately.
        >>> moonhyoung = laurens
        >>> moonhyoung.root.preview_gift_mc.enabled_mc.gotoAndPlay('none')
        >>> mouse_event = MouseEvent(MouseEvent.MOUSE_DOWN)

        Until server says not busy.
        >>> moonhyoung.root.cursor_mc.act_mc.gotoAndPlay('none')
        >>> mouse_event.currentTarget = moonhyoung.root._0_0_mc
        >>> moonhyoung.play_stone(mouse_event)
        >>> moonhyoung.root._0_0_mc.currentLabel
        'play_black'

        Do not resend stone in progress.  Do log an error.
        >>> old_log_level = logging.getLogger().level
        >>> logging.getLogger().setLevel(logging.CRITICAL)
        >>> before = len(laurens.ambassador.sends)
        >>> laurens.root._0_1_mc.gotoAndPlay('play_black')
        >>> laurens.play_stone(mouse_event)
        >>> if not before == len(laurens.ambassador.sends):
        ...     laurens.ambassador.sends[-1]
        >>> logging.getLogger().setLevel(old_log_level)

        If busy, do not send click.
        >>> robby = moonhyoung
        >>> robby.root._0_0_mc.gotoAndPlay('empty_black')
        >>> robby.root._0_1_mc.gotoAndPlay('empty_black')
        >>> robby.root.cursor_mc.act_mc.gotoAndPlay('none')
        >>> robby.root.cursor_mc.act_mc.currentLabel
        'none'
        >>> mouse_event.currentTarget = robby.root._0_0_mc
        >>> robby.play_stone(mouse_event)
        >>> robby.root.cursor_mc.act_mc.currentLabel
        'busy'
        >>> robby.root._0_0_mc.currentLabel
        'play_black'
        >>> robby.ambassador.sends[-1]['cursor_mc']['act_mc']['currentLabel']
        'busy'
        >>> mouse_event.currentTarget = robby.root._0_1_mc
        >>> robby.play_stone(mouse_event)
        >>> robby.root.cursor_mc.act_mc.currentLabel
        'busy'
        >>> robby.root._0_0_mc.currentLabel
        'play_black'
        >>> robby.root._0_1_mc.currentLabel
        'empty_black'

        Until server says not busy.
        >>> robby.root.cursor_mc.act_mc.gotoAndPlay('none')
        >>> robby.root._0_0_mc.gotoAndPlay('black')
        >>> mouse_event.currentTarget = robby.root._0_1_mc
        >>> robby.play_stone(mouse_event)
        >>> robby.root.cursor_mc.act_mc.currentLabel
        'busy'
        >>> robby.root._0_0_mc.currentLabel
        'black'
        >>> robby.root._0_1_mc.currentLabel
        'play_black'
        '''
        var = olds = {};
        var = busy = {};
        if ('busy' == globe.root.cursor_mc.act_mc.currentLabel):
            busy = {'help_mc': {'currentLabel': 'busy'}};
            olds = imitate_news(globe.root, busy);
            return;
        busy = {'cursor_mc': {'act_mc': {'currentLabel': 'busy'}}};
        # olds = imitate_news(globe.root, busy);
        var = intersection_mc = mouse_event.currentTarget;
        var = remove_news = remove_preview_news(globe.intersection_mc_array,
                intersection_mc);
        olds = imitate_news(globe.root, remove_news);
        var = preview_enabled = 'show' == globe.root \
                .preview_gift_mc.enabled_mc.currentLabel
        var = play_news = get_play_stone_news(intersection_mc, 
                globe.root.eat_mc, preview_enabled);        
        if (1 <= count_item(play_news)):
            # log_news('play_stone', play_news);
            play_news = upgrade(play_news, busy);
            globe.publish(play_news);

    def show_info(globe, mouse_event):
        '''Show info about the stone at the target intersection.
        >>> robby = globe_class()
        >>> robby.create(1)
        >>> robby.ambassador = echo_protocol_class()
        >>> robby.root._2_6_mc.gotoAndPlay('black')
        >>> robby.root._2_6_mc.black_shape_mc.attack_mc.gotoAndPlay('_0000')
        >>> robby.root._2_6_mc.black_shape_mc.defend_mc.gotoAndPlay('show')
        >>> robby.root._2_6_mc.black_shape_mc.defend_mc.profit_mc.gotoAndPlay('show')
        >>> robby.root._2_6_mc.territory_mc.gotoAndPlay('black_dead')
        >>> robby.root._2_6_mc.dragon_status_mc.gotoAndPlay('black_attack')
        >>> robby.root._2_6_mc.block_south_mc.gotoAndPlay('black_block')
        >>> robby.root.info_mc.currentLabel
        'none'
        >>> robby.root.info_mc.stone_mc.currentLabel
        'none'
        >>> robby.root.info_mc.decoration_mc.currentLabel
        'none'
        >>> robby.root.info_mc.profit_mc.currentLabel
        'none'
        >>> robby.root.info_mc.territory_mc.currentLabel
        'none'
        >>> robby.root.info_mc.block_mc.currentLabel
        'none'
        >>> robby.root.info_mc.dragon_status_mc.currentLabel
        'none'
        >>> mouse_event = MouseEvent(MouseEvent.MOUSE_OVER)
        >>> mouse_event.currentTarget = robby.root._2_6_mc
        >>> robby.show_info(mouse_event)
        >>> robby.root.info_mc.currentLabel
        'show'
        >>> robby.root.info_mc.stone_mc.currentLabel
        'black'
        >>> robby.root.info_mc.decoration_mc.currentLabel
        'black_attack_defend'
        >>> robby.root.info_mc.profit_mc.currentLabel
        'show'
        >>> robby.root.info_mc.territory_mc.currentLabel
        'black_dead'
        >>> robby.root.info_mc.block_mc.currentLabel
        'black_block'
        >>> robby.root.info_mc.dragon_status_mc.currentLabel
        'black_attack'
        >>> mouse_event.currentTarget = robby.root._0_0_mc
        >>> robby.show_info(mouse_event)
        >>> robby.root.info_mc.currentLabel
        'none'
        >>> robby.root.info_mc.stone_mc.currentLabel
        'none'
        >>> robby.root.info_mc.decoration_mc.currentLabel
        'none'
        >>> robby.root.info_mc.profit_mc.currentLabel
        'none'
        >>> robby.root.info_mc.territory_mc.currentLabel
        'neutral'
        >>> robby.root.info_mc.dragon_status_mc.currentLabel
        'none'

        Also hide info.
        >>> mouse_event = MouseEvent(MouseEvent.MOUSE_OVER)
        >>> mouse_event.currentTarget = robby.root._2_6_mc
        >>> robby.show_info(mouse_event)
        >>> robby.root.info_mc.currentLabel
        'show'
        >>> robby.root.info_mc.stone_mc.currentLabel
        'black'
        >>> robby.root.info_mc.decoration_mc.currentLabel
        'black_attack_defend'
        >>> robby.root.info_mc.territory_mc.currentLabel
        'black_dead'
        >>> robby.root.info_mc.block_mc.currentLabel
        'black_block'
        >>> robby.root.info_mc.dragon_status_mc.currentLabel
        'black_attack'
        >>> robby.root.info_mc._txt.text = 'Surround the fire.'
        >>> mouse_event = MouseEvent(MouseEvent.MOUSE_OUT)
        >>> mouse_event.currentTarget = robby.root._2_6_mc
        >>> robby.hide_info(mouse_event)
        >>> robby.root.info_mc.currentLabel
        'none'
        >>> robby.root.info_mc._txt.text
        ''
        >>> robby.root.info_mc.stone_mc.currentLabel
        'none'
        >>> robby.root.info_mc.decoration_mc.currentLabel
        'none'
        >>> robby.root.info_mc.territory_mc.currentLabel
        'none'
        >>> robby.root.info_mc.profit_mc.currentLabel
        'none'
        >>> robby.root.info_mc.block_mc.currentLabel
        'none'
        >>> robby.root.info_mc.dragon_status_mc.currentLabel
        'none'

        Reuse decoration for shape and place on board.
        >>> robby.root._6_2_mc.decoration_mc.gotoAndPlay('white_defend')
        >>> robby.root._6_2_mc.territory_mc.gotoAndPlay('white')
        >>> robby.root._6_2_mc.top_move_mc.gotoAndPlay('white')
        >>> mouse_event = MouseEvent(MouseEvent.MOUSE_OVER)
        >>> mouse_event.currentTarget = robby.root._6_2_mc
        >>> robby.show_info(mouse_event)
        >>> robby.root.info_mc.currentLabel
        'show'
        >>> robby.root.info_mc.stone_mc.currentLabel
        'none'
        >>> robby.root.info_mc.decoration_mc.currentLabel
        'white_defend'
        >>> robby.root.info_mc.territory_mc.currentLabel
        'white'
        >>> robby.root.info_mc.top_move_mc.currentLabel
        'white'
        >>> robby.hide_info(mouse_event)
        >>> robby.root.info_mc.top_move_mc.currentLabel
        'none'
        '''
        var = intersection_mc = mouse_event.currentTarget;
        var = label = intersection_mc.currentLabel;
        var = info_label = 'none';
        var = stone_label = 'none';
        var = decoration_label = 'none';
        var = profit_label = 'none';
        var = territory_label = intersection_mc.territory_mc.currentLabel;
        var = top_move_label = intersection_mc.top_move_mc.currentLabel;
        var = dragon_status_label = intersection_mc.dragon_status_mc.currentLabel;
        var = block_label = 'none';
        if ('black' == label or 'white' == label):
            info_label = 'show';
            stone_label = label;
            if ('black' == label):
                var = tags = '';
                var = shape_mc = intersection_mc[label + '_shape_mc'];
                var = attack_label = shape_mc.attack_mc.currentLabel;
                if ('none' != attack_label):
                    tags = tags + '_attack';
                var = defend_label = shape_mc.defend_mc.currentLabel;
                if ('none' != defend_label):
                    tags = tags + '_defend';
                if ('' != tags):
                    decoration_label = label + tags
                profit_label = shape_mc.defend_mc.profit_mc.currentLabel;
            if ('none' != intersection_mc.block_north_mc.currentLabel):
                block_label = intersection_mc.block_north_mc.currentLabel;
            if ('none' != intersection_mc.block_east_mc.currentLabel):
                block_label = intersection_mc.block_east_mc.currentLabel;
            if ('none' != intersection_mc.block_south_mc.currentLabel):
                block_label = intersection_mc.block_south_mc.currentLabel;
            if ('none' != intersection_mc.block_west_mc.currentLabel):
                block_label = intersection_mc.block_west_mc.currentLabel;
        else:
            if ('none' != territory_label and 'neutral' != territory_label):
                info_label = 'show';
            if ('none' != intersection_mc.decoration_mc.currentLabel):
                info_label = 'show';
                decoration_label = intersection_mc.decoration_mc.currentLabel;
            if ('none' != intersection_mc.top_move_mc.currentLabel):
                info_label = 'show';
        globe.root.info_mc.gotoAndPlay(info_label);
        globe.root.info_mc.stone_mc.gotoAndPlay(stone_label);
        globe.root.info_mc.decoration_mc.gotoAndPlay(decoration_label);
        globe.root.info_mc.territory_mc.gotoAndPlay(territory_label);
        globe.root.info_mc.top_move_mc.gotoAndPlay(top_move_label);
        globe.root.info_mc.profit_mc.gotoAndPlay(profit_label);
        globe.root.info_mc.block_mc.gotoAndPlay(block_label);
        globe.root.info_mc.dragon_status_mc.gotoAndPlay(dragon_status_label);
        globe.show_info_sequence(mouse_event);

    def hide_info(globe, mouse_event):
        '''For example, see show info.
        '''
        globe.imitate( get_hide_info_news() );
        globe.hide_info_sequence(mouse_event);


    def show_info_sequence(globe, mouse_event):
        '''Moonhyoung sees info of intersection.
        >>> moonhyoung = globe_class()
        >>> moonhyoung.create()
        >>> from pattern import get_info_sequence_news_2_2
        >>> news = get_info_sequence_news_2_2()
        >>> ## olds = imitate_news(moonhyoung.root, news)
        >>> ## moonhyoung.info = upgrade(moonhyoung.info, news['info'])

        Upgrade info.   On mouse over 2,2, see mark at 1,2.
        >>> news = get_info_sequence_news_2_2()
        >>> moonhyoung.info.get('info_mc')
        >>> moonhyoung.push_news(news)
        >>> moonhyoung.info['_2_2_mc'][0]['info_mc']['decoration_mc']['pattern_txt']['text']
        'CONNECT'
        >>> moonhyoung.info['_2_2_mc'][0]['_1_2_mc']['mark_mc']['currentLabel']
        'show'

        >>> mouse_event = MouseEvent(MouseEvent.MOUSE_OVER)
        >>> mouse_event.currentTarget = moonhyoung.root._2_2_mc
        >>> moonhyoung.root.info_mc.decoration_mc.pattern_txt.text
        ''
        >>> moonhyoung.root._1_2_mc.mark_mc.currentLabel
        'none'
        >>> moonhyoung.show_info_sequence(mouse_event)
        >>> moonhyoung.update(None)
        >>> moonhyoung.root.info_mc.decoration_mc.pattern_txt.text
        'CONNECT'
        >>> moonhyoung.root._1_2_mc.mark_mc.currentLabel
        'show'

        Upon mouse out, set the mark and info pattern text to nothing.
        >>> moonhyoung.hide_info_sequence(mouse_event)
        >>> moonhyoung.update(None)
        >>> moonhyoung.root.info_mc.decoration_mc.pattern_txt.text
        ''
        >>> moonhyoung.root._1_2_mc.mark_mc.currentLabel
        'none'

        Show info calls show info sequence.  
        >>> moonhyoung.push_news(news)
        >>> moonhyoung.show_info(mouse_event)
        >>> moonhyoung.update(None)
        >>> moonhyoung.root.info_mc.decoration_mc.pattern_txt.text
        'CONNECT'
        >>> moonhyoung.root._1_2_mc.mark_mc.currentLabel
        'show'

        Hide info calls hide info sequence.  
        >>> moonhyoung.ambassador = echo_protocol_class()
        >>> moonhyoung.hide_info(mouse_event)
        >>> moonhyoung.update(None)
        >>> moonhyoung.root.info_mc.decoration_mc.pattern_txt.text
        ''
        >>> moonhyoung.root._1_2_mc.mark_mc.currentLabel
        'none'

        If multiple info, cycle every 2 seconds.
        >>> second_mark = {'_0_2_mc': {'mark_mc': {'currentLabel': 'show'}}}
        >>> moonhyoung.info['_2_2_mc'].append(second_mark)
        >>> moonhyoung.show_info_sequence(mouse_event)
        >>> moonhyoung.update(None)
        >>> moonhyoung.root._1_2_mc.mark_mc.currentLabel
        'show'
        >>> moonhyoung.root._0_2_mc.mark_mc.currentLabel
        'none'
        >>> time.sleep(2)
        >>> # moonhyoung.show_info_sequence(mouse_event)
        >>> moonhyoung.update(None)
        >>> moonhyoung.root._1_2_mc.mark_mc.currentLabel
        'none'
        >>> moonhyoung.root._0_2_mc.mark_mc.currentLabel
        'show'
        >>> time.sleep(2)
        >>> # moonhyoung.show_info_sequence(mouse_event)
        >>> moonhyoung.update(None)
        >>> moonhyoung.root._1_2_mc.mark_mc.currentLabel
        'show'
        >>> moonhyoung.root._0_2_mc.mark_mc.currentLabel
        'none'
        '''
        var = intersection_mc = mouse_event.currentTarget;
        var = sequence = globe.info.get(intersection_mc.name);
        if (sequence and 1 <= len(sequence)):
            globe.info_sequence = sequence;

    def _get_info_sequence(globe, sequence):
        '''For example, see show_info_sequence
        '''
        if (sequence and 1 <= len(sequence)):
            var = index = int(getTimer() / 2000) % len(sequence);
            var = news = sequence[index];
            var = reverted = imitate_news(globe.root, globe.info_olds);
            var = olds = imitate_news(globe.root, news);
            globe.info_olds = olds;

    def hide_info_sequence(globe, mouse_event):
        '''For example, see show_info_sequence
        '''
        if (globe.info_olds):
            var = olds = imitate_news(globe.root, globe.info_olds);
            globe.info_olds = {};
            globe.info_sequence = [];


    def show_menu_info(globe, mouse_event):
        '''Describe the go problem.
        >>> marije = globe_class()
        >>> marije.create(1)
        >>> marije.ambassador = echo_protocol_class()
        >>> target = marije.root.lobby_mc._00_mc.capture_3_3_mc
        >>> target.info_txt.text = ''
        >>> target.info_txt.text = 'Surround a fire.'
        >>> marije.root.info_mc.currentLabel
        'none'
        >>> marije.root.info_mc._txt.text
        ''
        >>> mouse_event = MouseEvent(MouseEvent.MOUSE_OVER)
        >>> mouse_event.currentTarget = target
        >>> marije.show_menu_info(mouse_event)
        >>> marije.root.info_mc.currentLabel
        'show'
        >>> marije.root.info_mc._txt.text
        'Surround a fire.'
        >>> target2 = marije.root.lobby_mc._00_mc.capture_3_3_1_mc
        >>> target2.info_txt.text = ''
        >>> target2.info_txt.text = 'Surround a second fire.'
        >>> mouse_event.currentTarget = target2
        >>> marije.show_menu_info(mouse_event)
        >>> marije.root.info_mc.currentLabel
        'show'
        >>> marije.root.info_mc._txt.text
        'Surround a second fire.'

        Also hide info.
        >>> mouse_event = MouseEvent(MouseEvent.MOUSE_OUT)
        >>> mouse_event.currentTarget = target2
        >>> marije.hide_info(mouse_event)
        >>> marije.root.info_mc.currentLabel
        'none'
        >>> marije.root.info_mc._txt.text
        ''
        '''
        var = target_mc = mouse_event.currentTarget;
        var = info = target_mc.info_txt.text;
        if (info and 2 <= len(info)):
            globe.root.info_mc.gotoAndPlay('show');
            globe.root.info_mc._txt.text = info;


    def board_listens_to_mouse(globe, intersection_mc_array):
        '''
        >>> user = globe_class()
        >>> user.create(1)
        >>> user.root._0_0_mc.mouseEnabled
        True
        >>> user.root._0_0_mc.decoration_mc.mouseEnabled
        True
        >>> user.board_listens_to_mouse(user.intersection_mc_array)
        >>> user.root._0_0_mc.mouseEnabled
        True
        >>> user.root._0_0_mc.decoration_mc.mouseEnabled
        False
        >>> user.root._0_0_mc.decoration_mc.mouseChildren
        False

        XXX HACK TODO update every doctest referring 
        from _0_0_mc to _0_0_mc._btn.
        >>> user.root._0_0_mc.mouseEnabled
        True

        Do not disable mouseChildren of object that does not have that property.
        >>> shape = InteractiveObject()
        >>> shape.name = 'shape'
        >>> hasattr(shape, 'mouseChildren')
        False
        >>> user.root._0_0_mc.addChild(shape)
        >>> user.board_listens_to_mouse(user.intersection_mc_array)
        >>> hasattr(user.root._0_0_mc.shape, 'mouseChildren')
        False
        >>> user.root._0_0_mc.shape.mouseEnabled
        False

        Disable mouseChildren on strikes.
        >>> user.root._0_0_strike_mc.mouseEnabled
        False
        >>> user.root._0_0_strike_mc.mouseChildren
        False
        
        Mouse over intersection triggers show info.
        >>> robby = globe_class()
        >>> robby.create(1)
        >>> robby.ambassador = echo_protocol_class()
        >>> robby.setup_events()
        >>> robby.root._2_6_mc.gotoAndPlay('black')
        >>> robby.root._2_6_mc.black_shape_mc.attack_mc.gotoAndPlay('_0000')
        >>> robby.root._2_6_mc.black_shape_mc.defend_mc.gotoAndPlay('show')
        >>> robby.root._2_6_mc.dispatchEvent(mouseOver)
        >>> robby.root.info_mc.currentLabel
        'show'
        >>> robby.root.info_mc.stone_mc.currentLabel
        'black'
        >>> robby.root.info_mc.decoration_mc.currentLabel
        'black_attack_defend'
        >>> robby.root._0_0_mc.dispatchEvent(mouseOver)
        >>> robby.root.info_mc.currentLabel
        'none'
        >>> robby.root.info_mc.stone_mc.currentLabel
        'none'
        >>> robby.root.info_mc.decoration_mc.currentLabel
        'none'

        Mouse out hides info box.
        >>> robby.root._2_6_mc.dispatchEvent(mouseOver)
        >>> robby.root.info_mc.currentLabel
        'show'
        >>> robby.root.info_mc.stone_mc.currentLabel
        'black'
        >>> robby.root.info_mc.decoration_mc.currentLabel
        'black_attack_defend'
        >>> robby.root._2_6_mc.dispatchEvent(mouseOut)
        >>> robby.root.info_mc.currentLabel
        'none'
        >>> robby.root.info_mc.stone_mc.currentLabel
        'none'
        >>> robby.root.info_mc.decoration_mc.currentLabel
        'none'
        '''
        for row in range(len(intersection_mc_array)):
            for column in range(len(intersection_mc_array[row])):
                #try:
                var = intersection = intersection_mc_array[row][column];
                #except:
                #    import pdb; pdb.set_trace();
                var = child_count = intersection.numChildren;
                for c in range(child_count):
                    var = child = intersection.getChildAt(c);
                    if (isInteractiveObject(child)):
                        child.mouseEnabled = false;
                    if (isMovieClip(child)):
                        child.mouseChildren = false;
                #intersection.territory_mc.mouseEnabled = false
                #intersection.territory_mc.mouseChildren = false
                #intersection.block_north_mc.mouseEnabled = false
                #intersection.block_north_mc.mouseChildren = false
                #intersection.block_east_mc.mouseEnabled = false
                #intersection.block_east_mc.mouseChildren = false
                #intersection.block_south_mc.mouseEnabled = false
                #intersection.block_south_mc.mouseChildren = false
                #intersection.block_west_mc.mouseEnabled = false
                #intersection.block_west_mc.mouseChildren = false
                #intersection.hide_mc.mouseEnabled = false
                #intersection.hide_mc.mouseChildren = false
                #intersection.star_mc.mouseEnabled = false
                #intersection.star_mc.mouseChildren = false
                #intersection.question_mc.mouseEnabled = false
                #intersection.question_mc.mouseChildren = false
                #intersection.overlay_mc.mouseEnabled = false

                intersection.overlay_mc.mouseChildren = true;
                intersection.overlay_mc._btn.mouseEnabled = true;
                # XXX HACK TODO update every doctest referring 
                # from _0_0_mc to _0_0_mc._btn.
                #.as:uncomment: intersection.mouseEnabled = false;  # HACK uncomment in ActionScript only.
                intersection.addEventListener(
                        MouseEvent.MOUSE_DOWN, globe.play_stone);
                intersection.addEventListener(
                        MouseEvent.MOUSE_OVER, globe.show_info);
                intersection.addEventListener(
                        MouseEvent.MOUSE_OUT, globe.hide_info);
                var = strike_name = '_' + str(row) \
                        + '_' + str(column) + '_strike_mc';
                var = strike_mc = globe.root[strike_name];
                strike_mc.mouseEnabled = false;
                strike_mc.mouseChildren = false;
        globe.root.help_mc.mouseEnabled = false;
        globe.root.help_mc.mouseChildren = false;

    def follow(globe, mouse_event):
        '''Cursor and shield follow mouse position.
        >>> laurens = globe_class()
        >>> laurens.create()
        >>> laurens.root.mouseX = 100
        >>> laurens.root.mouseY = 200
        >>> laurens.follow(MouseEvent(MouseEvent.MOUSE_DOWN))
        >>> laurens.root.mouse_shield_mc.x
        100
        >>> laurens.root.cursor_mc.y
        200
        '''
        globe.root.cursor_mc.x = int(globe.root.mouseX)
        globe.root.cursor_mc.y = int(globe.root.mouseY)
        globe.root.mouse_shield_mc.x = int(globe.root.mouseX)
        globe.root.mouse_shield_mc.y = int(globe.root.mouseY)

    def mouse_shield(mouse_event):
        '''double publish may collide with a network message.
        So imitate but do not publish.'''
        news = get_mouse_shield_news(globe.root)
        imitate_news(globe.root, news)

    def revise(globe, news):
        '''
        >>> laurens = globe_class()
        >>> laurens.create()
        >>> laurens.setup_events()
        >>> laurens.root.title_mc.username_txt.text = 'laurens'
        >>> laurens.root.title_mc.password_txt.text = 'l'
        >>> news = {'title_mc': {'username_txt': {'text': 'ethan'}}}
        >>> laurens.current
        {}
        >>> laurens.revise(news)

        Remembers news to recreate current published state.
        Beware: ignores unrevised password.
        >>> laurens.current
        {'title_mc': {'username_txt': {'text': 'ethan'}}}
        >>> news = {'title_mc': {'password_txt': {'text': 'e'}}}
        >>> laurens.revise(news)
        >>> laurens.current
        {'title_mc': {'username_txt': {'text': 'ethan'}, 'password_txt': {'text': 'e'}}}
        '''
        archive = copy.deepcopy(news);
        globe.current = upgrade(globe.current, archive);
        olds = imitate_news(globe.root, news, null);
        globe.olds_list.append(olds);

    def echo_once_or_imitate(globe, news):
        '''If echo trigger, strip echo trigger.
        >>> ## gateway_process = subprocess_gateway(amf_host, 'embassy.py', verbose)
        >>> ethan = globe_class()
        >>> ethan.create()
        >>> ethan.setup_events()
        >>> ethan.ambassador = print_protocol_class()
        >>> ethan.echo_once_or_imitate({'gateway_mc': {'currentLabel': 'enter'}})
        >>> if not ethan.root.gateway_mc.currentLabel == 'enter':  
        ...     ethan.root.gateway_mc.currentLabel
        >>> news = {'gateway_mc': {
        ...    'ready_time_txt': {
        ...        'text': 'echo_once'}
        ...     }
        ... }
        >>> ethan.echo_once_or_imitate(news)
        {'title_mc': {'username_txt': {'text': ''}, 'slave_txt': {'text': 'slave'}, 'password_txt': {'text': ''}, 'master_txt': {'text': 'master'}}}
        >>> if ethan.root.gateway_mc.ready_time_txt.text == 'echo_once':  
        ...     ethan.root.gateway_mc.currentLabel

        Or just log.
        >>> news = {'gateway_mc': {
        ...    'ready_time_txt': {
        ...        'text': 'log'}
        ...     },
        ...     'currentLabel': 'table'
        ... }
        >>> ethan.echo_once_or_imitate(news)
        >>> if ethan.root.currentLabel == 'table':  
        ...     ethan.root.currentLabel
        '''
        if undefined != news.get('gateway_mc'):
            if undefined != news.get('gateway_mc').get('ready_time_txt'):
                if 'log' == news.get('gateway_mc').get('ready_time_txt').get('text'):
                    news.pop('gateway_mc')
                    globe.log_news('log', news)
                    return
                elif 'echo_once' == news.get('gateway_mc').get('ready_time_txt').get('text'):
                    news.pop('gateway_mc')
                    globe.log_news('echo_once', news)
                    news = globe.insert_credentials(news)
                    globe.ambassador.send(news)
                    return
        globe.imitate(news)

    def imitate(globe, news):
        # globe.log_news('imitate', news);
        globe.revise(news);
        var = is_alive = globe.is_alive();
        logging.debug('globe.is_alive ' + str(is_alive));
        logging.debug('globe.ambassador.is_alive ' + str(globe.ambassador.is_alive));
        globe.ambassador.is_alive = globe.is_alive();
        if (is_alive):
            if ('entering' == globe.root['save_mc'].currentLabel):
                globe.save_list = globe.save_one_child(globe.root, globe.save_list);
            elif ('entering' == globe.root['load_mc'].currentLabel):
                # XXX Gotcha ActionScript requires 'new MouseEvent' 
                # but does not bark while compiling
                var = mouse_event = new = MouseEvent(MouseEvent.MOUSE_DOWN);
                globe.load_stage(mouse_event);

    def log_news(globe, cite, news):
        '''In reverse order, append keys in news and their labels to text field.
        >>> ## gateway_process = subprocess_gateway(amf_host, 'embassy.py', verbose)
        >>> laurens = globe_class()
        >>> laurens.create()
        >>> ## laurens.setup(mock_speed, setup_client)
        >>> laurens.setup_events() # clear the log.  XXX redudant with setup?
        >>> laurens.ambassador = print_protocol_class()
        >>> laurens.root.title_mc.username_txt.text = 'laurens'
        >>> laurens.imitate({'_1_0_mc': {'currentLabel': 'black'}, '_0_0_mc': {'currentLabel': 'black'}})
        >>> print laurens.root.log_txt.text
        log

        deprecated:
        imitate_news: laurens: _0_0_mc:black _1_0_mc:black
        '''
        var = keywords = get_keywords(news);
        var = my_keywords = globe.root.title_mc.username_txt.text + ':' + keywords;
        globe.update_log(cite + ': ' + my_keywords);

    def push_news(globe, news):
        '''Route news to reading list or sequence or info.
        >>> import config
        >>> defaults = config.setup_defaults()
        >>> configuration = config.borg(defaults)
        >>> configuration.instant = False
        >>> moonhyoung = globe_class()
        >>> moonhyoung.create()
        >>> moonhyoung.ambassador = print_protocol_class()
        >>> moonhyoung.news_list
        []
        >>> moonhyoung.sequence_list
        []

        Enable sequence.
        >>> ## configuration.instant = False
        >>> moonhyoung.instant
        False

        Ignore empty sequence.
        >>> news = {'sequence': []}
        >>> moonhyoung.push_news(news)
        
        sequence a timed event.
        >>> event = note(moonhyoung.root._3_3_mc, 'currentLabel', 'question_black')
        >>> timed_event = upgrade(event, {'time_txt': {'text': '256000'}})
        >>> sequence = [timed_event]
        >>> news = {'sequence': sequence}
        >>> moonhyoung.push_news(news)
        >>> now = getTimer()
        >>> if not now < 256000:  now
        >>> moonhyoung.news_list
        []
        >>> len(moonhyoung.sequence_list)
        1
        >>> moonhyoung.sequence_list[0][0]['time_txt']['text']
        '256000'
        >>> moonhyoung.sequence_list[0][0]['_3_3_mc']['currentLabel']
        'question_black'
        >>> moonhyoung.root.gotoAndPlay('table')
        >>> moonhyoung.push_news({'currentLabel': 'lobby'})

        Upon push, available news is NOT imitated.
        >>> rene = moonhyoung
        >>> rene.news_list
        [{'currentLabel': 'lobby'}]
        >>> rene.root.currentLabel
        'table'
        >>> len(rene.sequence_list)
        1

        Upon receiving first event with sequence key, 
        client flushes the preceding sequence.
        When I revert the client, I also clear the old sequence.
        >>> from pprint import pprint
        >>> pprint(moonhyoung.sequence_list)
        [[{'_3_3_mc': {'currentLabel': 'question_black'},
           'time_txt': {'text': '256000'}}]]
        >>> moonhyoung.root._3_3_mc.currentLabel
        'empty_black'
        >>> news = {'sequence': [{'sequence': []}, 
        ...     {'currentLabel': 'table', 'time_txt': {'text': '256000'}}]}
        >>> moonhyoung.push_news(news)
        >>> pprint(moonhyoung.sequence_list)
        [[{'_3_3_mc': {'currentLabel': 'question_black'},
           'time_txt': {'text': '256000'}}],
         [{'sequence': []}, {'currentLabel': 'table', 'time_txt': {'text': '256000'}}]]
        >>> moonhyoung.root._3_3_mc.currentLabel
        'empty_black'
        >>> moonhyoung.update(None)
        >>> getTimer() < 256000
        True
        >>> pprint(moonhyoung.sequence_list)
        [[{'currentLabel': 'table', 'time_txt': {'text': '256000'}}]]
        >>> moonhyoung.root._3_3_mc.currentLabel
        'question_black'

        Optionally imitate now.
        >>> configuration.instant = True
        >>> moonhyoung = globe_class()
        >>> moonhyoung.create()
        >>> moonhyoung.ambassador = print_protocol_class()
        >>> event = note(moonhyoung.root._3_3_mc, 'currentLabel', 'question_black')
        >>> timed_event = upgrade(event, {'time_txt': {'text': '256000'}})
        >>> sequence = [timed_event]
        >>> news = {'sequence': sequence}
        >>> moonhyoung.push_news(news)
        >>> now = getTimer()
        >>> if not now < 256000:  now
        >>> moonhyoung.news_list
        []
        >>> moonhyoung.sequence_list
        [[{'_3_3_mc': {'currentLabel': 'question_black'}, 'time_txt': {'text': '256000'}}]]
        >>> moonhyoung.root._3_3_mc.currentLabel
        'empty_black'
        >>> moonhyoung.update(None)
        >>> moonhyoung.sequence_list
        []
        >>> moonhyoung.root._3_3_mc.currentLabel
        'question_black'

        >>> configuration.instant = True
        >>> laurens = globe_class()
        >>> laurens.create()
        >>> laurens.ambassador = print_protocol_class()
        >>> news = get_laurens_question_black_sequenced_news()
        >>> laurens.push_news(news)
        >>> laurens.root._2_2_mc.currentLabel
        'empty_black'
        >>> laurens.update(None)
        >>> laurens.root._2_2_mc.currentLabel
        'question_black'

        >>> code_unit.doctest_unit(globe_class.show_info_sequence, log = False)

        Clear info.
        >>> moonhyoung.info = {'_2_2_mc': []}
        >>> moonhyoung.push_news({'info': {'delete': true}})
        >>> moonhyoung.info
        {}

        >>> print 'To manually test info:  '

        Open room, make two moves near center that show info.
        Mouse over those moves.  See info marks.
        Exit room.  Reenter room.  Mouse over same intersections.  See no marks.
        '''
        # globe.log_news('push_news', news);
        if (type(news) == Object):
            var = old = false;
            if (undefined != news.get('sequence')):
                var = sequence = news['sequence'];
                if (1 <= len(sequence)):
                    globe.sequence_list.append(sequence);
                    old = true;
                del news['sequence'];
            if (1 <= count_item(news)):
                globe.news_list.append(news);
                old = true;
            if (undefined != news.get('info')):
                var = breakpoint = true;
            # ActionScript gotcha:  never {'info': {}} != news.get('info')
            if (undefined != news.get('info')):
                if (true == news.get('info').get('delete')):
                    globe.info = {};
                else:
                    globe.info = upgrade(globe.info, news['info']);
        else:
            trace('push_news: what is this? ' + news);

    def deliver_news(globe, event):
        '''Imitate first news in list.  
        TODO:  Synchronize this ActionScript and Python method.
        >>> ethan = globe_class()
        >>> ethan.create()
        >>> ethan.root.addEventListener(Event.ENTER_FRAME, ethan.deliver_news)
        >>> ethan.ambassador = print_protocol_class()
        >>> news = {'currentLabel': 'table'}
        >>> ethan.news_list.append(news)
        >>> ethan.root.dispatchEvent(enterFrame)
        >>> ethan.root.currentLabel
        'table'
        >>> ethan.news_list
        []
        >>> news = {'currentLabel': 'lobby'}
        >>> news2 = {'gateway_mc': {'currentLabel': 'enter'}}
        >>> ethan.news_list.append(news)
        >>> ethan.news_list.append(news2)
        >>> ethan.root.dispatchEvent(enterFrame)
        >>> ethan.root.currentLabel
        'lobby'
        >>> ethan.root.gateway_mc.currentLabel
        'enter'
        >>> ethan.news_list
        []
        '''
        var = news = {};
        while (globe and globe.news_list and 1 <= len(globe.news_list) \
                and globe.ambassador):
            news = globe.news_list.pop(0);
            globe.imitate(news);

    def follow_sequences(globe, event):
        return globe._follow_sequences(globe.instant);

    def _follow_sequences(globe, instant):
        '''If time for news in sequence, imitate then discard the news.
        Time is client age in milliseconds, as in getTimer.
        >>> import config
        >>> defaults = config.setup_defaults()
        >>> configuration = config.borg(defaults)
        >>> configuration.instant = False
        
        >>> moonhyoung = globe_class()
        >>> moonhyoung.create()
        >>> moonhyoung.root.addEventListener(Event.ENTER_FRAME, moonhyoung.follow_sequences)
        >>> moonhyoung.ambassador = print_protocol_class()
        >>> now = getTimer()
        >>> event = {}
        >>> event = note(moonhyoung.root._3_3_mc, 'currentLabel', 'question_black')
        >>> timed_event = upgrade(event, {'time_txt': {'text': str(now + 250)}})
        >>> sequence = [timed_event]

        Do not upgrade news, as that would recursively reference the sequence.
        >>> ## news = upgrade(event, {'sequence': sequence})
        >>> moonhyoung.sequence_list.append(sequence)
        >>> moonhyoung.root.dispatchEvent(enterFrame)
        >>> moonhyoung.root._3_3_mc.currentLabel
        'empty_black'
        >>> len(moonhyoung.sequence_list)
        1
        >>> time.sleep(0.25)
        >>> moonhyoung.root.dispatchEvent(enterFrame)
        >>> moonhyoung.root._3_3_mc.currentLabel
        'question_black'
        >>> len(moonhyoung.sequence_list)
        0

        If no timestamp, then consume immediately.
        >>> news = {}
        >>> news = upgrade(news, note(moonhyoung.root._3_3_mc, 'currentLabel', 'black') )
        >>> sequence = [news]
        >>> moonhyoung.sequence_list.append(sequence)
        >>> moonhyoung.root.dispatchEvent(enterFrame)
        >>> moonhyoung.root._3_3_mc.currentLabel
        'black'
        >>> len(moonhyoung.sequence_list)
        0
        
        If 0 or any timestamp before age in client, then consume immediately.
        >>> news = {}
        >>> news = upgrade(news, note(moonhyoung.root._3_3_mc, 'currentLabel', 'black') )
        >>> news = upgrade(news, {'time_txt': {'text': str(0)}})
        >>> sequence = [news]
        >>> moonhyoung.sequence_list.append(sequence)
        >>> moonhyoung.root.dispatchEvent(enterFrame)
        >>> moonhyoung.root._3_3_mc.currentLabel
        'black'
        >>> len(moonhyoung.sequence_list)
        0

        If multiple sequenced events are overdue, consume each overdue.
        >>> moonhyoung.root._3_3_mc.gotoAndPlay('none')
        >>> moonhyoung.root._3_2_mc.decoration_mc.gotoAndPlay('none')
        >>> moonhyoung.root._3_1_mc.decoration_mc.gotoAndPlay('none')
        >>> news = {}
        >>> news = upgrade(news, note(moonhyoung.root._3_3_mc, 'currentLabel', 'black') )
        >>> news = upgrade(news, {'time_txt': {'text': str(0)}})
        >>> news2 = note(moonhyoung.root._3_2_mc.decoration_mc, 'currentLabel', 'black_attack')
        >>> news2 = upgrade(news2, {'time_txt': {'text': str(1)}})
        >>> news3 = note(moonhyoung.root._3_1_mc.decoration_mc, 'currentLabel', 'black_attack')
        >>> news3 = upgrade(news3, {'time_txt': {'text': str(900000)}})
        >>> sequence = [news, news2, news3]
        >>> moonhyoung.sequence_list.append(sequence)
        >>> moonhyoung.root.dispatchEvent(enterFrame)
        >>> moonhyoung.root._3_3_mc.currentLabel
        'black'
        >>> moonhyoung.root._3_2_mc.decoration_mc.currentLabel
        'black_attack'
        >>> moonhyoung.root._3_1_mc.decoration_mc.currentLabel
        'none'
        >>> len(moonhyoung.sequence_list)
        1

        Optionally, immediately imitate sequenced events.
        >>> configuration.instant = True
        >>> moonhyoung = globe_class()
        >>> moonhyoung.create()
        >>> moonhyoung.ambassador = print_protocol_class()
        >>> moonhyoung.news_list = []
        >>> moonhyoung.sequence_list = []
        >>> event = note(moonhyoung.root._3_3_mc, 'currentLabel', 'question_black')
        >>> timed_event = upgrade(event, {'time_txt': {'text': '1000'}})
        >>> sequence = [timed_event]
        >>> moonhyoung.sequence_list.append(sequence)
        >>> moonhyoung.follow_sequences(enterFrame)
        >>> moonhyoung.news_list
        []
        >>> moonhyoung.sequence_list
        []
        >>> moonhyoung.root._3_3_mc.currentLabel
        'question_black'

        >>> code_unit.doctest_unit(globe_class.push_news, log = False)
        '''
        if (1 <= len(globe.sequence_list)):
            var = previous = globe.sequence_list[0];
            var = sequence = globe.sequence_list[0];
            var = time = 0;
            var = time_txt = '0';
            var = news = {};
            # ActionScript gotcha:  for..in does not guarantee access in same order.
            # for..in and for each..in
            # http://www.kirupa.com/forum/showpost.php?s=7ec39a65b4a290ca1d6c8b7cd43cf0a1&p=1923917&postcount=137
            for s in range(len(globe.sequence_list)):
                sequence = globe.sequence_list[s];
                time = 0;
                while (1 <= len(sequence) and (instant \
                        or time <= getTimer()) ):
                    if (type(sequence[0].get('sequence')) == Array):
                        sequence.pop(0);
                        for pre in range(s):
                            previous = globe.sequence_list[pre];
                            while (1 <= len(previous)):
                                news = previous.pop(0);
                                globe.imitate(news);
                    time_txt = sequence[0].get('time_txt');
                    if (null != time_txt):
                        time = int(time_txt['text']);
                    if (instant or time <= getTimer()):
                        news = sequence.pop(0);
                        # globe.log_news('_follow_sequence:imitate', news);
                        globe.imitate(news);
            var = new_sequence_list = [];
            for n in range(len(globe.sequence_list)):
                sequence = globe.sequence_list[n];
                if (1 <= len(sequence)):
                    new_sequence_list.append(sequence);
            globe.sequence_list = new_sequence_list;

    def update(globe, event):
        '''deliver news and follow sequences
        >>> moonhyoung = globe_class()
        >>> moonhyoung.create()
        >>> moonhyoung.update(null)
        '''
        globe.deliver_news(event);
        globe.follow_sequences(event);
        globe._get_info_sequence(globe.info_sequence);
    
    def is_alive(globe):
        if (globe and globe.root):
            if ('exit' == globe.root.gateway_mc.currentLabel):
                logging.info('exit == root.gateway_mc.currentLabel');
                return false;
        else:
            return false;
        return true;


# End ActionScript compatible Python that Flash needs
# End ActionScript compatible Python that server needs

# Test
from mock_client import *


import code_unit
snippet = '''
# !start python code_explorer.py --snippet snippet --import user_as.py
import user_as; user_as = reload(user_as); from user_as import *
'''
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
    

