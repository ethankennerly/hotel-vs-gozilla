'''Sort lesson SGF files to conveniently open the files.
'''
__author__ = 'Ethan Kennerly'
import os
import shutil

def sort_files(file_names):
    r'''
    sort by order counting by tens from 10 to leave room to edit like in BASIC.
    >>> sort_files(['b.txt', 'a.txt'])
    ['10_b.txt', '20_a.txt']
    
    skip unnamed files.
    >>> sort_files(['b.txt', ''])
    ['10_b.txt']

    fill in leading zeroes.
    >>> sort_files([str(a) for a in range(10)])
    ['010_0', '020_1', '030_2', '040_3', '050_4', '060_5', '070_6', '080_7', '090_8', '100_9']
    >>> sort_files([str(a) for a in range(100)])[90:]
    ['0910_90', '0920_91', '0930_92', '0940_93', '0950_94', '0960_95', '0970_96', '0980_97', '0990_98', '1000_99']
    '''
    sorted_file_names = []
    z = len(str(len(file_names))) + 1
    for index, name in enumerate(file_names):
        if name:
            sorted_name = str(index*10+10).zfill(z) + '_' + name
            sorted_file_names.append(sorted_name)
    return sorted_file_names


import text

lesson_path = 'sgf/beginner'
def get_lesson():
    lesson_text = text.load('sgf/beginner/lesson.txt')
    lesson = lesson_text.split('\r\n')
    return lesson

def sort_lesson():
    '''Actually sort the lesson.
    >>> sort_lesson()
    '''
    lesson = get_lesson()
    sorted_path = 'sgf/begin'
    sorted = sort_files(lesson)
    for les, sort in zip(lesson, sorted):
        from_les = os.path.join(lesson_path, les)
        to_sort = os.path.join(sorted_path, sort)
        shutil.copy2(from_les, to_sort)

def pathed_lesson():
    lesson = get_lesson()
    pathed = [os.path.join(lesson_path, name) for name in lesson]
    return pathed



from user_as import get_problem_news

def reset_problem_name_news(problem_name):
    news = {
        'lobby_mc': {
            problem_name: { 
                'currentLabel': 'none'
            }
        }
    }
    return news

def receive_problem_news(problem_name):
    news = {
        'lobby_mc': {}
    }
    news['lobby_mc'][problem_name] = { 
                'enter_mc': {'currentLabel': 'none'}
            }
    return news


def get_problem_file(problem_name):
    '''deprecated for get_problem_name_file
    >>> lesson = pathed_lesson()
    >>> lesson[0] == get_problem_file('_0_mc')
    True
    >>> lesson[9] == get_problem_file('_9_mc')
    True
    '''
    print 'deprecated for get_problem_name_file'
    lesson = pathed_lesson()
    index = int(problem_name[1])
    return lesson[index]

from user_as import rstrip_string
def get_problem_name_file(problem_name):
    r'''
    >>> get_problem_name_file('capture_5_5_mc')
    'sgf/beginner/capture_5_5.sgf'
    >>> get_problem_name_file('dominate_3_3_mc')
    'sgf/beginner/dominate_3_3.sgf'

        Unix file system cannot find '\\' in path:
        (Pdb) os.name
        'posix'
        (Pdb) problem_file
        'sgf/beginner\\capture_3_3.sgf'
        (Pdb) os.path.exists(problem_file)
        False
        (Pdb) os.path.exists('sgf/beginner/capture_3_3.sgf')
        True
    '''
    base_name = rstrip_string(problem_name, '_mc')
    return 'sgf/beginner/%s.sgf' % base_name

import os
def get_problem_name(problem_file):
    '''MovieClip name from file.
    >>> get_problem_name('sgf/beginner/capture_5_5.sgf')
    'capture_5_5_mc'
    '''
    basename = os.path.basename(problem_file)
    base, extension = os.path.splitext(basename)
    return '%s_mc' % base


def get_start_problem(news):
    '''Return file path to problem.
    >>> news = receive_problem_news('_0_mc')
    >>> name, problem = get_start_problem(news)
    >>> lesson = pathed_lesson()
    >>> ('_0_mc', lesson[0]) == get_start_problem(get_problem_news('_0_mc'))
    True
    >>> ('_2_mc', lesson[2]) == get_start_problem(get_problem_news('_2_mc'))
    True
    '''
    lobby_dict = news.get('lobby_mc')
    if lobby_dict:
        lesson = pathed_lesson()
        for index, problem in enumerate(lesson):
            name = '_%i_mc' % index
            problem_dict = lobby_dict.get(name)
            if problem_dict:
                enter_dict = problem_dict.get('enter_mc')
                if enter_dict:
                    if 'enter' == enter_dict.get('currentLabel'):
                        return name, problem
    return None, None

from smart_go_format import sgf_to_history, sgf_file_to_pgf, get_next_events
from remote_control import upgrade, note
from super_user import get_color, set_color, update_turn, get_empty_color_news, update_empty_block
from super_users import to_resize_board, get_partner, tell

def get_start_problem_file_news(users, user, problem_name):
    problem_file = get_problem_file(problem_name)
    return _get_start_problem_news(users, user, problem_name, problem_file)

def get_start_problem_name_news(users, user, problem_mc):
    problem_file = get_problem_name_file(problem_mc.name)
    return _get_start_problem_news(users, user, problem_mc, problem_file)


def add_white_example():
    '''News to add multiple black stones and a white stone.
    >>> from super_users import setup_users_white_black
    >>> users, ethan, moonhyoung = setup_users_white_black('ethan', 'moonhyoung')
    >>> reply = _get_start_problem_news(users, moonhyoung, moonhyoung.root.lobby_mc._00_mc.capture_rule_mc, 'sgf/beginner/capture_rule.sgf')
    >>> ## reply = get_start_problem_name_news(users, moonhyoung, moonhyoung.root.lobby_mc._00_mc.capture_rule_mc)
    >>> from remote_control import imitate_news
    >>> olds = imitate_news(moonhyoung.root, reply)
    >>> moonhyoung.pb()
    ,X,
    XOX
    ,,,
    >>> moonhyoung.play_history[0]['add_black']
    [(0, 1), (1, 0), (1, 2)]
    >>> moonhyoung.play_history[0]['add_white']
    [(1, 1)]
    '''

from user_as import get_children
import re
import time
def parse_every_problem(parent_mc):
    '''TODO:  Parse every problem that a user has access to.
    For speed, parse each instead of starting with event manager.
    >>> from super_user import user_class
    >>> moonhyoung = user_class()
    >>> moonhyoung.create(8.0)
    >>> moonhyoung.setup_events()
    >>> parse_every_problem(moonhyoung.root.lobby_mc)

    TODO (in another example?):  Play out random paths in problem.
    '''
    level_mcs = get_children(parent_mc, 'main_mc')
    level_mc_re = re.compile('^_[0-9][0-9]_mc$')
    for mc in level_mcs:
        if level_mc_re.match(mc.name):
            problem_mcs = get_children(mc, 'main_mc')
            for problem_mc in problem_mcs:
                problem_file = get_problem_name_file(problem_mc.name)
                if problem_file:
                    try:
                        history = sgf_to_history(problem_file)
                    except:
                        print 'parse_every_problem:  bad problem_file %s?' \
                            % problem_file
                        #time.sleep(0.5)
                        #raise
                else:
                    print 'parse_every_problem:  no problem_file %s?' \
                            % problem_file


def start_every_problem_example():
    '''TODO:  Start every problem that a user has access to.
    Slower than parsing.
    >>> from super_user import user_class
    >>> moonhyoung = user_class()
    >>> moonhyoung.create(8.0)
    >>> moonhyoung.setup_events()
    >>> # get_children
    >>> # for each
    >>> # start
    >>> # quit
    '''

def get_start_problem_example(users, user, news):
    r'''Return news for player and partner.
    Precondition:  Board is clear.
    >>> from super_users import setup_users_white_black
    >>> users, ethan, mathijs = setup_users_white_black('ethan', 'mathijs')
    >>> reply = get_start_problem_name_news(users, mathijs, mathijs.root.lobby_mc._00_mc.capture_3_3_1_mc)

    User receives file of problem.
    >>> if not reply.get('sgf_file_txt').get('text') == 'sgf/beginner/capture_3_3_1.sgf':
    ...     reply

    User resets path in problem tree. 
    >>> if not reply.get('sgf_path_txt') == {'text': '[]'}:
    ...     reply.keys()
   
    Assign computer as partner.
    >>> lukasz = users.get('lukasz')
    >>> lukasz.setup_events()
    >>> andre = lukasz
    >>> if not andre:
    ...     print 'expected andre'
    >>> # set_color(andre, 'black')
    >>> reply = _get_start_problem_news(users, andre, andre.root.lobby_mc._00_mc.capture_5_5_mc, 'sgf/test_capture_5_5.sgf')
    >>> ethan == get_partner(users, andre)
    False
    >>> computer_andre = users.get('computer_lukasz')
    >>> if not computer_andre == get_partner(users, andre):
    ...     computer_andre, get_partner(users, andre)
    >>> if not andre == get_partner(computer_andre.users, computer_andre):
    ...     computer_andre, get_partner(users, andre)

    Set user to black.
    >>> reply['turn_mc']['black_user_txt']['text']
    'lukasz'

    It is Andre's turn to play.
    >>> andre.root.turn_mc.currentLabel
    'black'
    >>> get_color(andre)
    'black'
    >>> andre.root._0_0_mc.currentLabel
    'empty_black'

    Andre's partner has white board.
    >>> get_color(computer_andre)
    'white'
    >>> computer_andre.root._0_0_mc.currentLabel
    'empty_white'

    Both will see added stone.  Partner is updated.
    >>> reply['_0_1_mc']['currentLabel']
    'black'
    >>> reply['currentLabel']
    '_5_5'
    >>> computer_andre.root.currentLabel
    '_5_5'
    >>> computer_andre.root['_0_1_mc']['currentLabel']
    'black'

    #>>> computer_andre.pb()
    ,,,,,
    ,,X,,
    ,,,,,
    ,,,,,
    ,,,,,

    So that GnuGo keeps up.  Player history includes added stone in head.
    >>> andre.play_history[0]['add_black']
    [(0, 1)]

    User receives news embedded in SGF, whereas, other user does not.
    >>> reply = _get_start_problem_news(users, andre, andre.root.lobby_mc._00_mc.capture_5_5_mc, 'sgf/test_dominate_3_3.sgf')
    >>> if not reply.get('option_mc').get('block_mc').get('currentLabel') == 'show':
    ...     reply
    >>> computer_andre.root.option_mc.block_mc.currentLabel
    'none'

    Only user receives header comment in SGF.
    >>> reply = get_start_problem_name_news(users, andre, andre.root.lobby_mc._00_mc.capture_5_5_mc)
    >>> if not reply['comment_mc'].get('currentLabel') == 'comment':
    ...     reply
    >>> computer_andre.root.tutor_mc.currentLabel
    'none'

    Computer is level 36.
    >>> computer_andre.root.level_mc._txt.text
    '36'

    Only user, and not partner, receives file path of problem file.
    >>> reply.get('sgf_file_txt').get('text')
    'sgf/beginner/capture_5_5.sgf'
    >>> computer_andre.root.sgf_file_txt.text
    ''

    Always go to label of board.
    >>> from pprint import pprint
    >>> reply = get_start_problem_name_news(users, andre, andre.root.lobby_mc._14_mc.extra_stone_9_9_mc)
    >>> if not reply.get('currentLabel') == '_9_9':
    ...     pprint(reply['currentLabel'])
    >>> computer_andre.root.currentLabel
    '_9_9'

    Create a bot at level 36
    >>> joris = users.get('joris')
    >>> joris.setup_events()
    >>> # set_color(joris, 'black')
    >>> reply = _get_start_problem_news(users, joris, joris.root.lobby_mc._00_mc.capture_5_5_mc, 'sgf/test_dominate_3_3.sgf')
    >>> computer_joris = users.get('computer_joris')
    >>> computer_joris.root.level_mc._txt.text
    '36'
    >>> joris == get_partner(computer_joris.users, computer_joris)
    True

    Set user to black.
    >>> reply['turn_mc']['black_user_txt']['text']
    'joris'

    Opening note
    >>> reply = _get_start_problem_news(users, joris, joris.root.lobby_mc._00_mc.capture_5_5_mc, 'sgf/test_opening_note.sgf')
    >>> reply['game_over_mc']['mission_mc']['currentLabel']
    'opening_note'
    >>> reply['game_over_mc']['mission_mc'].has_key('_txt')
    True

    Do not sequence
    >>> reply['sequence']
    False

    Close info box
    >>> reply['info_mc']['currentLabel']
    'none'
    >>> reply['info_mc']['_txt']['text']
    ''
    '''

def get_start_problem_news_deprecated(users, user, news):
    problem_name, problem_file = get_start_problem(news)
    return _get_start_problem_news(users, user, problem_name, problem_file)

def _add_stone(add_key, positions):
    '''Add black or white.
    >>> _add_stone('add_black', [(1, 2)])
    {'_1_2_mc': {'currentLabel': 'black'}}
    '''
    news = {}
    add_colors = {'add_black': 'black', 'add_white': 'white'}
    if add_key in add_colors:
        color = add_colors[add_key]
        from intersection_mc import get_intersection_name
        for row, column in positions:
            intersection_name = get_intersection_name(row, column)
            news[intersection_name] = {'currentLabel': color}
    return news

def _may_add_stone(event):
    '''May or may not add stone to news
    >>> _may_add_stone({})
    {}
    >>> _may_add_stone({'add_black': [(1, 2)]})
    {'_1_2_mc': {'currentLabel': 'black'}}

    >>> from super_users import setup_users_white_black
    >>> users, ethan, moonhyoung = setup_users_white_black('ethan', 'moonhyoung')
    >>> reply = get_start_problem_name_news(users, moonhyoung, moonhyoung.root.lobby_mc._00_mc.capture_5_5_mc)
    >>> reply['_1_2_mc']['currentLabel']
    'black'
    >>> moonhyoung.play_history[0]['add_black']
    [(1, 2)]
    '''
    news = {}
    for key, value in event.items():
        add = _add_stone(key, value)
        if add:
            news = upgrade(news, add)
    return news



from intersection_mc import get_connected_news, get_block_news, get_empty_block_news, news_to_board
from user_as import get_intersection_array
from super_user import get_color
from remote_control import get_latest
def may_visualize_add_stone(user, intersection_mc_array, history, reply):
    '''According to player options, connect, block, etc.
    >>> from super_user import user_class, become_observant
    >>> moonhyoung = user_class()
    >>> moonhyoung.create(1)
    >>> ## moonhyoung.setup_events()

    Moonhyoung can see help and has a color.
    >>> # become_observant(moonhyoung)
    >>> set_color(moonhyoung, 'black')
    >>> history = sgf_to_history('sgf/test_score_rule_territory.sgf')
    >>> reply, size = get_board_setup(history, {})
    >>> reply = may_visualize_add_stone(moonhyoung, moonhyoung.intersection_mc_array, history, reply) 
    >>> reply['_3_0_mc']['currentLabel']
    'black'
    >>> reply['_3_0_mc']['currentLabel']
    'black'

    Moonhyoung sees connect, block, empty_block, and territory.
    >>> reply['_0_4_mc']['black_shape_mc']['currentLabel']
    '_0011'
    >>> reply['_4_3_mc'].get('block_south_mc')
    >>> reply['_4_2_mc']['empty_block_north_mc']['currentLabel']
    'block'
    >>> reply['_0_1_mc']['empty_block_east_mc']['currentLabel']
    'you'
    
    Territory and score require talking to GnuGo.
    >>> reply['_0_0_mc'].get('territory_mc')
    >>> reply.get('score_mc')

    Add stone to player history is copied from problem, not here.
    >>> marije = moonhyoung
    >>> marije.play_history
    []

    Optionally, SGF sets no empty block.
    >>> andrew = moonhyoung
    >>> history = sgf_to_history('sgf/test_capture.sgf')
    >>> reply, size = get_board_setup(history, {})
    >>> reply = may_visualize_add_stone(andrew, andrew.intersection_mc_array, history, reply) 
    >>> reply.get('_0_2_mc')
    >>> reply.get('_0_2_mc')
    >>> reply.get('_0_2_mc')
    '''
    if history:
        add_stone_news = _may_add_stone(history[0])
        reply = upgrade(reply, add_stone_news)
    news, size = get_board_setup(history, add_stone_news)
    resize_news = to_resize_board(9, size)
    news = upgrade(news, resize_news)
    new_board = news_to_board(news)
    ## from referee import pb
    ## pb(new_board)
    length = int(size[1])
    new_intersection_mc_array = get_intersection_array(user.root, length)
    #connected_enabled = None
    #if reply.get('connected_mc'):
    #    connected_enabled = reply.get('connected_mc').get('currentLabel')
    #if not connected_enabled:
    #    connected_enabled = 'show' == user.root.connected_mc.currentLabel
    connected_label = get_latest(reply, 
            user.root.connected_mc, 'currentLabel')
    if 'show' == connected_label:
        connected_news = get_connected_news(new_intersection_mc_array, 
                new_board)
        reply = upgrade(reply, connected_news)
    #block_enabled = None
    #if reply.get('option_mc'):
    #    option_mc = reply.get('option_mc')
    #    if option_mc.get('block_mc'):
    #        block_enabled = option_mc.get('block_mc').get('currentLabel')
    #if not block_enabled:
    #    block_enabled = 'show' == user.root.option_mc.block_mc.currentLabel
    block_label = get_latest(reply, 
            user.root.option_mc.block_mc, 'currentLabel')
    if 'show' == block_label:
        user_block_news = get_block_news(new_intersection_mc_array,
                new_board)
        reply = upgrade(reply, user_block_news)
    empty_block_label = get_latest(reply, 
            user.root.option_mc.empty_block_mc, 'currentLabel')
    #empty_block_label = None
    #if reply.get('option_mc'):
    #    option_mc = reply.get('option_mc')
    #    if option_mc.get('empty_block_mc'):
    #        empty_block_label = option_mc.get('empty_block_mc').get('currentLabel')
    #if not empty_block_label:
    #    empty_block_label = user.root.option_mc.empty_block_mc.currentLabel
    if 'show' == empty_block_label:
        empty_block_news = get_empty_block_news(new_intersection_mc_array, 
                new_board, get_color(user))
        reply = upgrade(reply, empty_block_news)
    return reply

def get_board_setup(history, reply, size = '_9_9'):
    '''Size, comment, embedded news.
    >>> history = sgf_to_history('sgf/test_score_rule_territory.sgf')
    >>> reply, size = get_board_setup(history, {})
    >>> size
    '_5_5'
    >>> reply['connected_mc']['currentLabel']
    'show'
    '''
    if history:
        event = history[0]
        if event.get('size'):
            length = event.get('size')
            size = '_%i_%i' % (length, length)
        if event.get('news'):
            event_news = event.get('news')
            reply = upgrade(reply, event_news)
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
            reply = upgrade(reply, comment_news)
    return reply, size


def get_opening_note(event):
    '''Extract python game format opening note to mission text field.
    >>> from pprint import pprint
    >>> pprint(get_opening_note({}))
    {}
    >>> note = 'BABY DRAGONS DO NOT KNOW THE CORNER IS DANGEROUS.'
    >>> news = get_opening_note({'opening_note': note})
    >>> pprint(news)
    {'game_over_mc': {'mission_mc': {'_txt': {'text': 'BABY DRAGONS DO NOT KNOW THE CORNER IS DANGEROUS.'},
                                     'currentLabel': 'opening_note'}}}
    '''
    news = {}
    if 'opening_note' in event:
        note = event['opening_note']
        news = {
            'game_over_mc': {
                'mission_mc': {
                    '_txt': {
                        'text': note
                    }, 
                    'currentLabel': 'opening_note'
                }
            }
        }
    return news

def get_preview_problem_news():
    '''
    board size
    opponent
    opening note
    options
    file of problem
    '''

def _get_start_problem_news(users, user, problem_mc, problem_file):
    reply = {}
    if problem_file:
        from super_users import set_partner_news
        sgf_file_news = {
            'sgf_file_txt': {
                'text': problem_file
            },
            'sgf_path_txt': {
                'text': '[]'
            }
        }
        reply = upgrade(reply, sgf_file_news)
        history = sgf_to_history(problem_file)
        get_opening_note_news = get_opening_note(history[0])
        reply = upgrade(reply, get_opening_note_news)
        reply, size = get_board_setup(history, reply)
        set_color(user, 'black')
        reply = may_visualize_add_stone(user, user.intersection_mc_array, 
                history, reply)
        resize_news = to_resize_board(0, size)
        reply = upgrade(reply, resize_news)
        #- old_length = len(user.intersection_mc_array)
        preview_news = {
            'game_over_mc': {
                'currentLabel': 'preview'
            }
        }
        reply = upgrade(reply, preview_news)
        user.play_history = history
        received = note(problem_mc, 'currentLabel', 'none')
        #- received = reset_problem_name_news(problem_name)
        #- received = receive_problem_news(problem_name)
        reply = upgrade(reply, received)
        # TODO:  extract following to function?
        partner = get_partner(users, user)
        partner_news = {}
        if not partner:
            bot_name = 'computer_%s' % user.root.title_mc.username_txt.text
            bot = users.get(bot_name)
            if not bot:
                from super_user import user_class
                bot = user_class()
                bot.create(user._speed)
                bot.setup_events()
                bot.users = users
                bot.root.title_mc.username_txt.text = bot_name
                bot.root.title_mc.password_txt.text = bot_name
                from super_users import gnugo_level
                bot.root.level_mc._txt.text = str(gnugo_level)
                users[bot_name] = bot
            if bot:
                if not bot.ambassador:
                    from mock_client import echo_protocol_class
                    bot.ambassador = echo_protocol_class()
                user_news, partner_news = set_partner_news(users, 
                        user, bot_name)
                partner = get_partner(users, user)
                reply = upgrade(reply, user_news)
            else:
                logging.error('receive:  to start problem, need partner or %s' % bot_name)
        empty_news = get_empty_color_news(user, get_color(user))
        reply = upgrade(reply, empty_news)
        empty_news = get_empty_color_news(partner, get_color(partner))
        partner_news = upgrade(partner_news, empty_news)
        #- partner_news = upgrade(partner_news, resize_news)
        #- partner_news = may_visualize_add_stone(partner, 
        #-         partner.intersection_mc_array, history, partner_news)
        if history:
            add_stone_news = _may_add_stone(history[0])
            partner_news = upgrade(partner_news, add_stone_news)
            partner_news = upgrade(partner_news, resize_news)
        #? partner_news = upgrade(partner_news, reply)
        reply, partner_news = update_turn(user, 'white', reply, partner_news)
        #- reply = update_empty_block(user, None, get_color(user), reply)
        tell(partner, partner_news)
        if history:
            if history[0].get('news'):
                private_event_news = history[0].get('news')
                reply = upgrade(reply, private_event_news)
        if reply:
            from user_as import get_hide_info_news
            reply = upgrade(reply, get_hide_info_news() )
            reply['sequence'] = False
    return reply


def _get_start_problem_news_DEPRECATE(users, user, problem_mc, problem_file):
    reply = {}
    if problem_file:
        from super_users import set_partner_news
        sgf_file_news = {
            'sgf_file_txt': {
                'text': problem_file
            },
            'sgf_path_txt': {
                'text': '[]'
            }
        }
        reply = upgrade(reply, sgf_file_news)
        history = sgf_to_history(problem_file)
        get_opening_note_news = get_opening_note(history[0])
        reply = upgrade(reply, get_opening_note_news)
        reply, size = get_board_setup(history, reply)
        set_color(user, 'black')
        reply = may_visualize_add_stone(user, user.intersection_mc_array, 
                history, reply)
        resize_news = to_resize_board(0, size)
        reply = upgrade(reply, resize_news)
        #- old_length = len(user.intersection_mc_array)
        preview_news = {
            'game_over_mc': {
                'currentLabel': 'preview'
            }
        }
        reply = upgrade(reply, preview_news)
        user.play_history = history
        received = note(problem_mc, 'currentLabel', 'none')
        #- received = reset_problem_name_news(problem_name)
        #- received = receive_problem_news(problem_name)
        reply = upgrade(reply, received)
        # TODO:  extract following to function?
        partner = get_partner(users, user)
        partner_news = {}
        if not partner:
            bot_name = 'computer_%s' % user.root.title_mc.username_txt.text
            bot = users.get(bot_name)
            if not bot:
                from super_user import user_class
                bot = user_class()
                bot.create(user._speed)
                bot.setup_events()
                bot.root.title_mc.username_txt.text = bot_name
                bot.root.title_mc.password_txt.text = bot_name
                from super_users import gnugo_level
                bot.root.level_mc._txt.text = str(gnugo_level)
                users[bot_name] = bot
            if bot:
                if not bot.ambassador:
                    from mock_client import echo_protocol_class
                    bot.ambassador = echo_protocol_class()
                user_news, partner_news = set_partner_news(users, 
                        user, bot_name)
                partner = get_partner(users, user)
                reply = upgrade(reply, user_news)
            else:
                logging.error('receive:  to start problem, need partner or %s' % bot_name)
        empty_news = get_empty_color_news(user, get_color(user))
        reply = upgrade(reply, empty_news)
        empty_news = get_empty_color_news(partner, get_color(partner))
        partner_news = upgrade(partner_news, empty_news)
        #- partner_news = upgrade(partner_news, resize_news)
        #- partner_news = may_visualize_add_stone(partner, 
        #-         partner.intersection_mc_array, history, partner_news)
        if history:
            add_stone_news = _may_add_stone(history[0])
            partner_news = upgrade(partner_news, add_stone_news)
            partner_news = upgrade(partner_news, resize_news)
        #? partner_news = upgrade(partner_news, reply)
        reply, partner_news = update_turn(user, 'white', reply, partner_news)
        #- reply = update_empty_block(user, None, get_color(user), reply)
        tell(partner, partner_news)
        if history:
            if history[0].get('news'):
                private_event_news = history[0].get('news')
                reply = upgrade(reply, private_event_news)
    return reply


def get_branch(path, tree):
    '''Child list or slice of list starting at tail address.
    >>> pgf = sgf_file_to_pgf('sgf/test_capture_3_3.sgf')
    >>> path = [1, 1]
    >>> from pprint import pprint
    >>> pprint(get_branch(path, pgf))
    [{'news': {'tutor_mc': {'currentLabel': 'surround'}}, 'white': 'pass'},
     {'black': 'pass', 'news': {'tutor_mc': {'currentLabel': 'capture'}}},
     {'news': {'tutor_mc': {'currentLabel': 'none'}}, 'white': 'pass'}]
    >>> path = [0, 0]
    >>> tree = [{}]
    >>> get_branch(path, tree)
    >>> path = []
    >>> tree = [{}]
    >>> get_branch(path, tree)
    [{}]

    If after end of list, return nothing.
    >>> path = [1, 1]
    >>> tree = [{}, [10, 20]]
    >>> get_branch(path, tree)
    [20]
    >>> path = [1, 2]
    >>> get_branch(path, tree)
    >>> tree = [{}, [10, 20, 30]]
    >>> get_branch(path, tree)
    [30]
    '''
    here = tree
    if 2 <= len(path):
        for step in path[:-1]:
            here = here[step]
    if 1 <= len(path):
        step = path[-1]
        if len(here) <= step:
            return
        if type([]) == type(here[step]):
            here = here[step]
        else:
            here = here[step:]
    return here


def get_here(path, tree):
    '''Child list or slice of list starting at tail address.
    >>> pgf = sgf_file_to_pgf('sgf/test_capture_3_3.sgf')
    >>> path = [1, 1]
    >>> from pprint import pprint
    >>> pprint(get_here(path, pgf))
    {'news': {'tutor_mc': {'currentLabel': 'surround'}}, 'white': 'pass'}
    >>> path = [0, 0]
    >>> tree = [{}]
    >>> get_here(path, tree)
    Traceback (most recent call last):
      ...
    KeyError: 0
    >>> path = []
    >>> tree = [{}]
    >>> get_here(path, tree)
    [{}]
    >>> path = []
    >>> pgf = sgf_file_to_pgf('sgf/test_node_0.sgf')
    >>> here = get_here(path, pgf)
    >>> path = [1]
    >>> pgf = sgf_file_to_pgf('sgf/test_node_0.sgf')
    >>> here = get_here(path, pgf)
    '''
    here = tree
    for step in path:
        here = here[step]
    return here


def get_sgf_path(user):
    path_text = user.root.sgf_path_txt.text
    path = eval(path_text)
    return path
    
def set_sgf_path(user, path):
    '''Conveniently get and set path within an SGF file.
    >>> from super_user import user_class
    >>> yuji = user_class()
    >>> yuji.create(1)
    >>> yuji.setup_events()
    >>> pgf = sgf_file_to_pgf('sgf/test_capture_3_3.sgf')
    >>> path = [1, 1]
    >>> from pprint import pprint
    >>> pprint(get_branch(path, pgf))
    [{'news': {'tutor_mc': {'currentLabel': 'surround'}}, 'white': 'pass'},
     {'black': 'pass', 'news': {'tutor_mc': {'currentLabel': 'capture'}}},
     {'news': {'tutor_mc': {'currentLabel': 'none'}}, 'white': 'pass'}]
    >>> set_sgf_path(yuji, path)
    >>> path = get_sgf_path(yuji)
    >>> path
    [1, 1]
    >>> pprint(get_branch(path, pgf))
    [{'news': {'tutor_mc': {'currentLabel': 'surround'}}, 'white': 'pass'},
     {'black': 'pass', 'news': {'tutor_mc': {'currentLabel': 'capture'}}},
     {'news': {'tutor_mc': {'currentLabel': 'none'}}, 'white': 'pass'}]
    >>> path = [1]
    >>> set_sgf_path(yuji, path)
    >>> append_sgf_path(yuji, 1)
    >>> path = get_sgf_path(yuji)
    >>> path
    [1, 1]
    >>> pprint(get_branch(path, pgf))
    [{'news': {'tutor_mc': {'currentLabel': 'surround'}}, 'white': 'pass'},
     {'black': 'pass', 'news': {'tutor_mc': {'currentLabel': 'capture'}}},
     {'news': {'tutor_mc': {'currentLabel': 'none'}}, 'white': 'pass'}]
    '''
    path_text = str(path)
    user.root.sgf_path_txt.text = path_text


def append_sgf_path(user, leaf):
    path = get_sgf_path(user)
    set_sgf_path(user, path + [leaf])

def get_current_pgf(user):
    '''Tree from current position
    >>> from super_user import user_class
    >>> yuji = user_class()
    >>> yuji.create(1)
    >>> yuji.setup_events()
    >>> get_current_pgf(yuji)
    []
    >>> yuji.root.sgf_file_txt.text = 'sgf/test_capture_3_3.sgf'
    >>> pgf = get_current_pgf(yuji)
    >>> from pprint import pprint
    >>> if not 100 < len(str(pgf)):
    ...     pprint(pgf)
    >>> set_sgf_path(yuji, [1, 0])
    >>> from pprint import pprint
    >>> pprint(get_current_pgf(yuji))
    [{'black': (1, 1), 'news': {'tutor_mc': {'currentLabel': 'question'}}},
     {'news': {'tutor_mc': {'currentLabel': 'surround'}}, 'white': 'pass'},
     {'black': 'pass', 'news': {'tutor_mc': {'currentLabel': 'capture'}}},
     {'news': {'tutor_mc': {'currentLabel': 'none'}}, 'white': 'pass'}]
    '''
    pgf = []
    problem_file = user.root.sgf_file_txt.text
    if os.path.exists(problem_file):
        path = get_sgf_path(user)
        tree = sgf_file_to_pgf(problem_file)
        pgf = get_branch(path, tree)
    return pgf


def get_pgf(user):
    '''Tree of SGF
    >>> from super_user import user_class
    >>> yuji = user_class()
    >>> yuji.create(1)
    >>> get_current_pgf(yuji)
    []
    >>> yuji.root.sgf_file_txt.text = 'sgf/test_capture_3_3.sgf'
    >>> pgf = get_pgf(yuji)
    >>> from pprint import pprint
    >>> if not 300 < len(str(pgf)):
    ...     pprint(pgf)
    >>> set_sgf_path(yuji, [1, 1])
    >>> pgf1 = get_pgf(yuji)
    >>> if not pgf == pgf1:
    ...     pprint(pgf1)
    '''
    pgf = []
    problem_file = user.root.sgf_file_txt.text
    if os.path.exists(problem_file):
        pgf = sgf_file_to_pgf(problem_file)
    return pgf


from intersection_mc import child_label_from_to, set_coordinate_news
def update_square(intersection_mc_array, event, news):
    '''Clear previous squares.
    Convert python game format squares to remote control news.
    >>> from super_user import user_class
    >>> marije = user_class()
    >>> marije.create(1)
    >>> marije.setup_events()
    >>> update_square(marije.intersection_mc_array, {})
    {}
    >>> marije.root._0_1_mc.square_mc.gotoAndPlay('show')
    >>> news = update_square(marije.intersection_mc_array, {}, {})
    >>> news['_0_1_mc']['square_mc']['currentLabel']
    'none'
    >>> event = {'square': [(0, 0), (1, 0), (0, 1)]}
    >>> news = update_square(marije.intersection_mc_array, event, {})
    >>> news['_0_0_mc']['square_mc']['currentLabel']
    'show'
    >>> news['_0_1_mc']['square_mc']['currentLabel']
    'show'
    >>> news['_1_0_mc']['square_mc']['currentLabel']
    'show'
    >>> event = {'square': [(0, 0), (1, 0)]}
    >>> news = update_square(marije.intersection_mc_array, event, {})
    >>> news['_0_0_mc']['square_mc']['currentLabel']
    'show'
    >>> news['_0_1_mc']['square_mc']['currentLabel']
    'none'
    >>> news['_1_0_mc']['square_mc']['currentLabel']
    'show'
    '''
    none_news = child_label_from_to(intersection_mc_array, 
            'square_mc', 'show', 'none')
    news = upgrade(news, none_news)
    if 'square' in event:
        coordinates = event['square']
        show_news = set_coordinate_news(coordinates, 'square_mc', 'show')
        news = upgrade(news, show_news)
    return news    


import copy
from intersection_mc import get_row_column, get_intersection_color
from smart_go_format import get_node_on_any_path, merge_news
def update_path(user, intersection_mc, pass_dict = {}):
    '''Return the news if any symmetry on path.
    Then clear SGF file.
    >>> from super_user import user_class
    >>> emmet = user_class()
    >>> emmet.create(1)
    >>> emmet.setup_events()
    >>> emmet.root.sgf_file_txt.text = 'sgf/test_capture_3_3.sgf'

    Update intersection before path.
    >>> news = update_path(emmet, emmet.root._0_0_mc)
    >>> news.has_key('comment_mc')
    False

    Pass catches any move not explicitly stated.
    >>> emmet.root._0_1_mc.gotoAndPlay('preview_black')
    >>> emmet.play_history = [{'size': 3}]
    >>> news = update_path(emmet, emmet.root._0_1_mc)
    >>> if not news.has_key('comment_mc'):  news
    >>> if news.has_key('tutor_mc'):  news
    >>> from pprint import pprint
    >>> ## pprint(news)

    If bad move, then clear intersection.

    >>> emmet.root._1_1_mc.gotoAndPlay('play_black')
    >>> news = update_path(emmet, emmet.root._1_1_mc)

    If on path, do not update the current path to the new path.  
    >>> emmet.root.sgf_file_txt.text = 'sgf/test_capture_3_3.sgf'
    >>> emmet.root._1_1_mc.gotoAndPlay('play_black')
    >>> news = update_path(emmet, emmet.root._1_1_mc)
    >>> if not news.has_key('tutor_mc'):  news
    >>> if news.has_key('black'):  news

    If no SGF, then return same as end of SGF.
    >>> emmet.root.sgf_file_txt.text = 'sgf/test_node_0.sgf'
    >>> emmet.play_history = [{'size': 9}]
    >>> emmet.root._1_1_mc.gotoAndPlay('play_black')
    >>> news = update_path(emmet, emmet.root._1_1_mc)
    >>> news
    {}

    Do not clear the SGF file.
    >>> news.get('sgf_file_txt')

    If problem file not found, then on path is None.
    >>> emmet.root.sgf_file_txt.text = 'sgf/beginner/NO_SUCH.sgf'
    >>> emmet.root._1_2_mc.gotoAndPlay('play_black')
    >>> news = update_path(emmet, emmet.root._1_2_mc)
    >>> news
    {}

    If path, then check that branch of the SGF tree.
    >>> yuji = user_class()
    >>> yuji.create(1)
    >>> yuji.setup_events()
    >>> yuji.play_history = [{'size': 3}]
    >>> yuji.root.sgf_file_txt.text = 'sgf/test_capture_3_3.sgf'
    >>> yuji.root._1_1_mc.gotoAndPlay('preview_black')
    >>> news = update_path(yuji, yuji.root._1_1_mc)
    >>> if not news.has_key('tutor_mc'):  news
    >>> if news.has_key('black'):  news
    >>> if news.has_key('white'):  news

    Does not update history.  If move already in history, then not on path.
    After end of path, not 'off path' but same result as if no file.
    >>> yuji.play_history.append({'black': (1, 1)})
    >>> yuji.root._1_1_mc.gotoAndPlay('preview_black')
    >>> news = update_path(yuji, yuji.root._1_1_mc)
    >>> news
    {}

    Actually, is the color of the move compared with the color of the SGF?

    Mark squares.
    >>> marije = user_class()
    >>> marije.create(1)
    >>> marije.setup_events()
    >>> marije.root.sgf_file_txt.text = 'sgf/test_mark_square.sgf'
    >>> marije.play_history = [{'size': 3}, {'black': (1, 1)}, {'white': (0, 1)}]
    >>> marije.root._1_1_mc.gotoAndPlay('black')
    >>> marije.root._0_1_mc.gotoAndPlay('white')
    >>> marije.root._1_0_mc.gotoAndPlay('preview_black')
    >>> news = update_path(marije, marije.root._1_0_mc)
    >>> if not news['_0_0_mc']['square_mc']['currentLabel'] == 'show':  news

    Pass.
    >>> h1 = yuji
    >>> h1.play_history = [{'size': 3}]
    >>> h1.root.sgf_file_txt.text = 'sgf/test_capture_3_3.sgf'
    >>> news = update_path(h1, None, pass_dict = {'black': 'pass'})
    >>> if not news.has_key('bad_move_mc'):  news
    '''
    news = {}
    pgf_tree = get_pgf(user)
    if pgf_tree:
        pgf_history = _branch_history(user.play_history, intersection_mc, 
                pass_dict)
        event = get_node_on_any_path(pgf_history, pgf_tree)
        if event:
            news = merge_news(event)
        update_square(user.intersection_mc_array, event, news)
    return news

def _branch_history(play_history, intersection_mc, pass_dict):
    '''Copy history and append intersection or pass.
    >>> code_unit.doctest_unit(update_path, verbose = False, log = False)
    '''
    pgf_history = copy.deepcopy(play_history)
    pgf_history.append({})
    if pass_dict:
        color = pass_dict.keys()[0]
        pgf_history[-1][color] = pass_dict[color]
    else:
        color = get_intersection_color(intersection_mc)
        if color:
            row, column = get_row_column(intersection_mc.name)
            pgf_history[-1][color] = row, column
    return pgf_history

def update_path_rotated_example():
    '''Match rotated SGF tree.
    >>> from super_user import user_class
    >>> marije = user_class()
    >>> marije.create(1)
    >>> marije.setup_events()
    >>> marije.root.sgf_file_txt.text = 'sgf/test_bottom_square.sgf'
    >>> marije.confirm_board_size('_3_3')
    >>> marije.pb()
    ,,,
    ,,,
    ,,,
    >>> marije.play_history = [{'size': 3, 'add_black': [(1, 1)], 'add_white': [(2, 2)]}]
    >>> marije.root._1_1_mc.gotoAndPlay('black')
    >>> marije.root._2_2_mc.gotoAndPlay('white')
    >>> marije.pb()
    ,,,
    ,X,
    ,,O
    >>> marije.root._2_1_mc.gotoAndPlay('preview_black')
    >>> marije.pb()
    ,,,
    ,X,
    ,$O
    >>> news = update_path(marije, marije.root._2_1_mc)
    >>> if not news['_1_2_mc']['square_mc']['currentLabel'] == 'show':  news
    >>> if news.get('bad_move_mc'):  news
    '''

def on_problem_path(user, intersection_mc):
    '''DEPRECATE.  Use update_path instead.
    Return leaf number, and comment for node 1 of problem SGF.
    Then clear SGF file.
    >>> from super_user import user_class
    >>> emmet = user_class()
    >>> emmet.create(1)
    >>> emmet.setup_events()
    >>> emmet.root.sgf_file_txt.text = 'sgf/test_capture_3_3.sgf'
    >>> on, news = on_problem_path(emmet, emmet.root._0_0_mc)
    >>> on
    False
    >>> news.has_key('comment_mc')
    False
    >>> news.has_key('tutor_mc')
    True
    >>> from pprint import pprint
    >>> ## pprint(news)

    >>> on, news = on_problem_path(emmet, emmet.root._1_1_mc)
    >>> on
    [1, 1]

    If on path, do not update the current path to the new path.  
    >>> get_sgf_path(emmet)
    []
    >>> # set_sgf_path(emmet, [])
    >>> emmet.root.sgf_file_txt.text = 'sgf/test_capture_3_3.sgf'
    >>> on, news = on_problem_path(emmet, emmet.root._1_1_mc)
    >>> on
    [1, 1]
    >>> news.has_key('tutor_mc')
    True

    If no SGF, then return same as end of SGF.
    >>> get_sgf_path(emmet)
    []
    >>> emmet.root.sgf_file_txt.text = 'sgf/test_node_0.sgf'
    >>> on, news = on_problem_path(emmet, emmet.root._1_1_mc)
    >>> on
    >>> news.has_key('tutor_mc')
    False

    Do not clear the SGF file.
    >>> news.get('sgf_file_txt')

    If problem file not found, then on path is None.
    >>> emmet.root.sgf_file_txt.text = 'sgf/beginner/NO_SUCH.sgf'
    >>> on, news = on_problem_path(emmet, emmet.root._1_2_mc)
    >>> on

    If path, then check that branch of the SGF tree.
    >>> code_unit.inline_examples(
    ...     get_current_pgf.__doc__, 
    ...     locals(), globals(), 
    ...     verify_examples = False)
    >>> pgf = get_current_pgf(yuji)
    >>> set_sgf_path(yuji, [])
    >>> on, news = on_problem_path(yuji, yuji.root._1_1_mc)
    >>> on
    [1, 1]
    >>> set_sgf_path(yuji, [0, 0])
    >>> on, news = on_problem_path(yuji, yuji.root._1_1_mc)
    Traceback (most recent call last):
      ...
    KeyError: 0
    >>> set_sgf_path(yuji, [1, 0])
    >>> on, news = on_problem_path(yuji, yuji.root._1_1_mc)
    >>> on
    [1, 1]
    >>> set_sgf_path(yuji, [1, 1])
    >>> on, news = on_problem_path(yuji, yuji.root._1_1_mc)
    >>> on
    [1, 2]

    If not on path, do not update the current path to the new path.  
    >>> get_sgf_path(yuji)
    [1, 1]

    Pass catches any move not explicitly stated.
    >>> set_sgf_path(yuji, [1, 0])
    >>> on, news = on_problem_path(yuji, yuji.root._1_1_mc)
    >>> on
    [1, 1]
    >>> set_sgf_path(yuji, [1, 1])
    >>> on, news = on_problem_path(yuji, yuji.root._0_0_mc)
    >>> on
    [1, 2]

    If on path, do not update the current path to the new path.  
    >>> get_sgf_path(yuji)
    [1, 1]

    After end of path, not 'off path' but same result as if no file.
    >>> set_sgf_path(yuji, [1, 4])
    >>> on, news = on_problem_path(yuji, yuji.root._0_0_mc)
    >>> on
    >>> news
    {}

    Actually, is the color of the move compared with the color of the SGF?

    TODO?  migrate on = None to on = <type 'exceptions.EOFError'>
    Does not support SGF files with sub-branches, such as sgf/test_subbranch_3_3.sgf
    '''
    on, reply = None, {}
    leaf = None
    pass_comment_news = {}
    remaining_pgf = get_current_pgf(user)
    if remaining_pgf:
        pgf = get_pgf(user)
        offset = 0
        path = get_sgf_path(user)
        # SGF has game information in node 0, so skip the header
        if type([]) == type(remaining_pgf) and [] == path:
            #header = remaining_pgf.pop(0)
            header = remaining_pgf[offset]
            offset += 1
            path = [offset]
            remaining_pgf = remaining_pgf[offset:]
        #events = get_next_events(remaining_pgf)
        #for e, event in enumerate(events):
        pushed = []
        if remaining_pgf:
            here = get_here(path, pgf)
            pushed = [0]
            on = False
        #here = get_here(path, pgf)
        #pushed = [0]
        while remaining_pgf and pushed:
            pushed = []
            here = remaining_pgf.pop(0)
            #if type([]) != type(here) and remaining_pgf and path:
            #    path[-1] += 1
            #    here = remaining_pgf.pop(0)
            while type([]) == type(here):
                offset = 0
                here = here.pop(offset)
                # here = here[offset]
                pushed += [offset]
                path += [offset]
            event = here
            if 'black' in event:
                color = 'black'
            elif 'white' in event:
                color = 'white'
            else:
                # SGF has game information in node 0, so skip the header
                continue
            move = event.get(color)
            if 'pass' == move:
                # on = [e + offset]
                on = [p for p in path]
                if on:  on[-1] += 1
                #on = True
                #leaf = e
                if event.has_key('comment'):
                    comment = event['comment']
                    pass_comment_news = {
                        'comment_mc': {
                            'currentLabel': 'comment',
                            '_txt': {
                                'text': comment
                            }
                        }
                    }
                if event.has_key('news'):
                    news = event['news']
                    bad_move = news.get('bad_move_mc')
                    if bad_move:
                        if 'show' == bad_move.get('currentLabel'):
                            on = False
                    reply = upgrade(reply, news)
            elif move:
                r, c = move
                from intersection_mc import get_row_column
                if (r, c) != get_row_column(intersection_mc.name):
                    on = False
                else:
                    on = [p for p in path]
                    if on:  on[-1] += 1
                    # on = [e + offset]
                    #on = True
                    #leaf = e
                    #sgf_file_news = {'sgf_file_txt': {'text': ''}}
                    #reply = upgrade(reply, sgf_file_news)
                    # is the following redundant with pass?
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
                        reply = upgrade(reply, comment_news)
                    if event.has_key('news'):
                        news = event['news']
                        bad_move = news.get('bad_move_mc')
                        if bad_move:
                            if 'show' == bad_move.get('currentLabel'):
                                on = False
                        reply = upgrade(reply, news)
                    #if on and leaf is not None:
                    #    path = get_sgf_path(user)
                    #    set_sgf_path(user, path + [leaf])
                    return on, reply
            path[-1] += 1
            for p in pushed:
                path.pop(-1)
    if pass_comment_news:
        reply = upgrade(reply, pass_comment_news)
    #if on and leaf is not None:
    #    path = get_sgf_path(user)
    #    set_sgf_path(user, path + [leaf])
    return on, reply



import code_unit
snippet = '''
# !start python code_explorer.py --import lesson.py --snippet snippet
import lesson; lesson = reload(lesson); from lesson import *
'''
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

