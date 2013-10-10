#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
Crazy Cake server between two Flash players.
Embassy binds together Flash model super users and PyAMF server.
    gtp:  Go Text Protocol
    amf:  ActionScript Messaging Format
'''
__author__ = 'Ethan Kennerly'

import client
from decorator import decorator
import time

from super_users import *



# User and GTP
# Go Text Protocol and Smart Go Format

import go_text_protocol

def get_top_move_news(gtp_envoy, play_history, intersection_mc_array, 
        clear_color, color, board_size):
    '''see get_critical_news
    emmet_capture_5_5_example'''
    news = {}
    clear_top_move_news = child_label_from_to(intersection_mc_array, 
            'top_move_mc', clear_color, 'none')
    news = upgrade(news, clear_top_move_news)
    if color:
        go_text_protocol.update_gnugo(gtp_envoy, play_history, board_size)
        top_move = go_text_protocol.get_coordinate(gtp_envoy, 
                'top_moves_%s' % color, board_size)
        if top_move:
            top_move_news = set_coordinate_news([top_move],
                'top_move_mc', color)
            news = upgrade(news, top_move_news)
    return news


def edit_top_move(coordinate, intersection_mc_array, clear_color):
    '''Upon playing a stone and hearing from the GnuGo player
    the top move to make, share this with the partner.
    >>> marije = user_class()
    >>> marije.create()
    >>> marije.root._0_0_mc.top_move_mc.gotoAndPlay('white')
    >>> coordinate = (2, 1)
    >>> news = edit_top_move(coordinate, marije.intersection_mc_array, 'white')
    >>> from pprint import pprint
    >>> pprint( news )
    {'_0_0_mc': {'top_move_mc': {'currentLabel': 'none'}},
     '_2_1_mc': {'top_move_mc': {'currentLabel': 'white'}}}
    '''

from smart_go_format import save_sgf
def get_critical_news(gtp_envoy, play_history, board, color, row, column,
        intersection_mc_array):
    '''
    find neighbors beside white's last play.  
    convert history to sgf.  
    for neighbors, show gnugo sgf, and ask gnugo for dragon status.  
    if critical, convert all blocks to danger.  so do this after block news.
    notify black.
    >>> play_history = [{'black': (7, 0)}, {'white': (6, 0)}, {'black': (7, 1)}, {'white': (6, 1)}, {'black': (7, 2)}, {'white': (6, 2)}, {'black': (7, 3)}, {'white': (6, 3)}, {'black': (8, 3)}, {'white': (7, 4)}]
    >>> board = referee.critical_board

    The color, row, and column correspond to the latest in history.
    Show opponent critical attack icon.
    >>> black = user_class()
    >>> black.create(1)
    >>> stephen = black
    >>> from pprint import pprint
    >>> gtp_envoy = go_text_protocol.setup_envoy(configuration.gtp_path, 'localhost', 5903)
    >>> setup_gtp = go_text_protocol.talk(gtp_envoy, 'set_random_seed 0')
    >>> color, row, column = 'white', 7, 4
    >>> news = get_critical_news(gtp_envoy, play_history, board, color, row, column,
    ...     black.intersection_mc_array)
    >>> if not news.get('_8_1_mc') or not news.get('_8_1_mc').get('top_move_mc') == {'currentLabel': 'black'}:
    ...     pprint(news)
    >>> if not news.get('_7_0_mc').get('dragon_status_mc') == {'currentLabel': 'white_attack'}:
    ...     pprint(news)

    #>>> if not news.get('_8_1_mc').get('top_move_mc') == {'currentLabel': 'black'}:
    #...     import pprint
    #...     pprint.pprint(news)

    After black is safe (or if not critical), remove vital and critical.
    >>> olds = imitate_news(black.root, news)
    >>> play_history.append({'black': (8, 1)})
    >>> news = get_critical_news(gtp_envoy, play_history, board, color, row, column,
    ...     black.intersection_mc_array)
    >>> try: 
    ...     news.get('_8_1_mc').get('top_move_mc') == {'currentLabel': 'none'}
    ... except:
    ...     pprint(news)
    True
    >>> try: 
    ...     news.get('_7_0_mc').get('dragon_status_mc') == {'currentLabel': 'none'}
    ... except:
    ...     pprint(news)
    True

    After white is safe, laurens sees critical disappear.
    >>> laurens = black
    >>> black.root._7_0_mc.dragon_status_mc.gotoAndPlay('black_attack')
    >>> news = get_critical_news(gtp_envoy, play_history, board, color, row, column,
    ...     black.intersection_mc_array)
    >>> try: 
    ...     news.get('_8_1_mc').get('top_move_mc') == {'currentLabel': 'none'}
    ... except:
    ...     pprint(news)
    True
    >>> try: 
    ...     news.get('_7_0_mc').get('dragon_status_mc') == {'currentLabel': 'none'}
    ... except:
    ...     pprint(news)
    True

    If critical against white, do not show top move to black.
    >>> play_history = [{'white': (0, 0)}, {'black': (0, 1)}, {'white': (1, 0)}]
    >>> board = referee.clear_board
    >>> board[0][0] = referee.white
    >>> board[0][1] = referee.black
    >>> board[1][0] = referee.white
    >>> news = get_critical_news(gtp_envoy, play_history, board, 'black', 0, 1, black.intersection_mc_array)
    >>> news['_0_0_mc']['dragon_status_mc']['currentLabel']
    'black_attack'
    >>> olds = imitate_news(black.root, news)
    >>> children_label_equals(black.intersection_mc_array, 'top_move_mc', 'black')
    []
    '''
    sgf_file = 'sgf/_dragon_status.sgf'
    # row, column = get_row_column(intersection_mc.name)
    # play_history.append({})
    # play_history[-1][color] = row, column
    board_size = len(board)
    save_sgf(play_history, sgf_file, size = board_size)
    # board_text = flash_to_text(intersection_mc_array)
    # board = referee.text_to_array(board_text)
    attackers = referee.find_attacker(board, row, column)
    dragons, vitals = go_text_protocol.get_attacker_critical_coordinates(
            sgf_file, attackers, size = board_size)
    #- news = set_block_news(coordinates, color + '_' + 'danger')
    dragons_vitals_log = 'dragons=%s; vitals=%s' % (dragons, vitals)
    logging.debug(dragons_vitals_log)
    news = {}
    if dragons and color != 'black':
        top_move_color = 'black'
    else:
        top_move_color = ''
    top_move_news = get_top_move_news(gtp_envoy, play_history, 
            intersection_mc_array, 'black', top_move_color, board_size)
    news = upgrade(news, top_move_news)
    #- clear_vital_point_news = child_label_from_to(intersection_mc_array, 'vital_point_mc', 'white_attack', 'none')
    #- news = upgrade(news, clear_vital_point_news)
    for old_color in ('white', 'black'):
        old_label = '%s_attack' % old_color
        clear_dragon_status_news = child_label_from_to(
                intersection_mc_array, 'dragon_status_mc', 
                old_label, 'none')
        news = upgrade(news, clear_dragon_status_news)
    label = color + '_attack'
    #- dragon_status_news = set_coordinate_news(dragons, 
    #-         'formation_mc', label)
    dragon_status_news = set_coordinate_news(dragons, 
            'dragon_status_mc', label)
            #- 'dragon_status_mc', 'critical')
    news = upgrade(news, dragon_status_news)
    #- vital_point_news = set_coordinate_news(vitals,
    #-         'decoration_mc', label)
    #- vital_point_news = set_coordinate_news(vitals,
    #-         'vital_point_mc', label)
    #-         #- 'vital_point_mc', 'defense_point')
    #- news = upgrade(news, vital_point_news)
    return news


def is_in_tail(file, tail, string):
    '''
    >>> is_in_tail('example.log', 120, 'asdf')
    False
    >>> is_in_tail('example.log', 120, 'asdfasdfasdf')
    False
    '''
    import text
    example_log = text.load(file)
    position = example_log[-tail:].find(string)
    return 0 <= position


def can_genmove_white(users, user):
    '''Is it alright for white to take a turn?
    >>> users, ethan, mathijs = setup_users_partners_ethan_mathijs()
    >>> size = 9
    >>> can_genmove_white(users, mathijs)
    False
    >>> news, partner_news = update_turn(mathijs, 'black', {}, {})
    >>> olds = imitate_news(mathijs.root, news)
    >>> olds = imitate_news(ethan.root, partner_news)
    >>> can_genmove_white(users, mathijs)
    False

    Must be computer.
    >>> olds = imitate_news(ethan.root, get_white_computer_news(ethan) )
    >>> olds = imitate_news(mathijs.root, get_white_computer_news(mathijs) )

    To move, must be white's turn to play.
    >>> news, partner_news = update_turn(mathijs, 'white', {}, {})
    >>> olds = imitate_news(mathijs.root, news)
    >>> olds = imitate_news(ethan.root, partner_news)
    >>> can_genmove_white(users, mathijs)
    False
    >>> news, partner_news = update_turn(mathijs, 'black', {}, {})
    >>> olds = imitate_news(mathijs.root, news)
    >>> olds = imitate_news(ethan.root, partner_news)

    To move, author must see a game in play.
    >>> mathijs.pb()
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    >>> news = {'game_over_mc': {'currentLabel': 'win'}}
    >>> mathijs.root.game_over_mc.gotoAndPlay('win')
    >>> can_genmove_white(users, mathijs)
    False
    >>> mathijs.root.game_over_mc.gotoAndPlay('none')
    >>> mathijs.pb()
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    >>> can_genmove_white(users, mathijs)
    True

    No partner.
    >>> andre = users.get('andre')
    >>> can_genmove_white(users, andre)
    False
    '''
    if 'computer' == user.root.game_over_mc.white_computer_mc.currentLabel:
        if 'none' != user.root.game_over_mc.currentLabel:
            return False
        partner = get_partner(users, user)
        if partner and 'white' == get_color(partner):
            if is_your_turn(partner):
                return True
    return False

def why_not_move(example_logger, gtp_envoy, users, user, partner, move):
    '''Try the chosen move.  True:  success.  False:  failed.
    >>> example_logger = setup_example_logger(level = logging.INFO)
    >>> gtp_envoy = go_text_protocol.setup_envoy(configuration.gtp_path, configuration.gtp_host, configuration.gtp_port)
    >>> setup_gtp = go_text_protocol.talk(gtp_envoy, 'set_random_seed 0')
    >>> users, ethan, mathijs = setup_users_partners_ethan_mathijs()

    To move, must be white's turn to play.
    >>> news, partner_news = update_turn(mathijs, 'black', {}, {})
    >>> olds = imitate_news(mathijs.root, news)
    >>> olds = imitate_news(ethan.root, partner_news)

    If white moves or passes, then tell black no longer busy.
    >>> mathijs.root.cursor_mc.act_mc.gotoAndPlay('busy')

    If on hidden, reveal hidden and replay.
    >>> mathijs.root._4_2_mc.gotoAndPlay('hide_black')
    >>> mathijs.play_history.append({'black': (4, 2), 'hide': [(4, 2)]})
    >>> mathijs.root._5_1_mc.gotoAndPlay('hide_black')
    >>> mathijs.play_history.append({'black': (5, 1), 'hide': [(5, 1)]})
    >>> mathijs.root._6_2_mc.gotoAndPlay('hide_black')
    >>> mathijs.play_history.append({'black': (6, 2), 'hide': [(6, 2)]})
    >>> mathijs.root._4_4_mc.gotoAndPlay('hide_black')
    >>> mathijs.play_history.append({'black': (4, 4), 'hide': [(4, 4)]})
    >>> mathijs.pb()
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,/,/,,,,
    ,/,,,,,,,
    ,,/,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    >>> is_in_tail('example.log', 60, 'ethan.root._5_2_mc')
    False
    >>> move = (4, 4)
    >>> occupied = why_not_move(example_logger, gtp_envoy, users, mathijs, ethan, move)
    >>> occupied['_4_4_mc']['hide_mc']['currentLabel']
    'reveal'
    >>> mathijs.pb()
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,/,X,,,,
    ,/,,,,,,,
    ,,/,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    >>> ethan.pb()
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,X,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    >>> move = (5, 2)

    If white moves or passes, then tell black no longer busy.
    >>> mathijs.root.cursor_mc.act_mc.currentLabel
    'busy'

    TODO:  Reports error when attackers are hidden.
    >>> why_not_move(example_logger, gtp_envoy, users, mathijs, ethan, move)
    get_dragon_status: response_gtp = ? vertex must not be empty
    <BLANKLINE>
    <BLANKLINE>
    get_attacker_critical_coordinates: error: []
    get_dragon_status: response_gtp = ? vertex must not be empty
    <BLANKLINE>
    <BLANKLINE>
    get_attacker_critical_coordinates: error: []
    get_dragon_status: response_gtp = ? vertex must not be empty
    <BLANKLINE>
    <BLANKLINE>
    get_attacker_critical_coordinates: error: []

    Because in SGF, hidden stones are marked but not played.
    >>> text.load('sgf/_dragon_status.sgf')
    u'(;GM[1]SZ[9];MA[ce];MA[bf];MA[cg];B[ee]CR[ee]MA[ee];W[cf])'
    >>> mathijs.pb()
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,/,X,,,,
    ,/O,,,,,,
    ,,/,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    >>> ethan.pb()
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,X,,,,
    ,,O,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,

    #Scoring reveals.  How can we see what GnuGo sees when making a move?
    #>>> print go_text_protocol.talk(gtp_envoy, 'showboard')
    = 
       A B C D E F G H J
     9 . . . . . . . . . 9
     8 . . . . . . . . . 8
     7 . . + . . . + . . 7
     6 . . . . . . . . . 6
     5 . . . . X . . . . 5
     4 . . O . . . . . . 4
     3 . . + . . . + . . 3
     2 . . . . . . . . . 2     WHITE (O) has captured 0 stones
     1 . . . . . . . . . 1     BLACK (X) has captured 0 stones
       A B C D E F G H J
    <BLANKLINE>
    <BLANKLINE>

    Give GnuGo a moment to catch up on SGF files.
    >>> time.sleep(1)

    Record white's move in example log.
    >>> is_in_tail('example.log', 60, 'ethan.root._5_2_mc')
    True
    
    Now that white has moved, it is black's turn.
    >>> is_your_turn(ethan)
    False
    >>> is_your_turn(mathijs)
    True

    If white moves or passes, then tell black no longer busy.
    >>> mathijs.root.cursor_mc.act_mc.gotoAndPlay('busy')
    >>> occupied = why_not_move(example_logger, gtp_envoy, users, mathijs, ethan, 'pass')
    >>> mathijs.root.cursor_mc.act_mc.currentLabel
    'play'
    '''
    # does network need time to accept a second message?
    # time.sleep(1.0 / user._speed)
    if 'pass' == move or 'resign' == move:
        pass_news = {'pass_mc': {'currentLabel': 'enter'}}
        passed, pass_reply = may_pass_news(example_logger,
                gtp_envoy, users, partner, pass_news)
        partner.publish(pass_reply)
        # >_< already told, so do not need to publish.
        #- return pass_reply
        # return {}
    else:
        row, column = move
        intersection_mc = partner.intersection_mc_array[row][column]
        color = 'white'
        intersection_name = get_intersection_name(row, column)
        user_news = {intersection_name: {'currentLabel': 'play_white'}}
        reply = iterate_intersection(
                example_logger, gtp_envoy, users, partner, 
                intersection_mc, user_news)
        if 'help_mc' in reply:
            logging.warn('may_genmove_white: help_mc %s' % reply.__repr__())
        logging.info('may_genmove_white: place_stone %s' % reply.__repr__())
        result = partner.publish(reply)
        if not 'white' == user.root[intersection_name].currentLabel:
            return reply

def may_not_pass(user, move):
    '''If user option computer_pass none, and gnugo passes, make up a move.
    See computer_pass_example
    >>> mathijs = user_class()
    >>> mathijs.create(1)
    >>> mathijs.root.option_mc.computer_pass_mc.gotoAndPlay('none')
    >>> mathijs.play_history = [{'black': (1, 1)}]
    >>> mathijs.confirm_board_size('_3_3')
    >>> if 'pass' == may_not_pass(mathijs, 'pass'):  move

    If no valid place to play, then pass.
    >>> mathijs.play_history = [{'black': (1, 1)}, {'white': (0, 2)}, {'black': (0, 1)}, {'white': (2, 1)}, {'black': (1, 0)}, {'white': (2, 2)}, {'black': (2, 0)}]
    >>> import smart_go_format
    >>> tuples = smart_go_format.history_to_tuple(mathijs.play_history)
    >>> for r, c, color in tuples:
    ...     mathijs.intersection_mc_array[r][c].gotoAndPlay(color)
    >>> mathijs.intersection_mc_array[1][2].gotoAndPlay('empty_black')
    >>> mathijs.intersection_mc_array[0][0].gotoAndPlay('empty_black')
    >>> mathijs.pb()
    ,XO
    XX,
    XOO
    >>> may_not_pass(mathijs, 'pass')
    'pass'

    If computer_pass, then may pass.
    >>> mathijs.root.option_mc.computer_pass_mc.gotoAndPlay('show')
    >>> mathijs.play_history = [{'black': (1, 1)}]
    >>> may_not_pass(mathijs, 'pass')
    'pass'
    '''
    if 'pass' == move or 'resign' == move:
        computer_pass = user.root.option_mc.computer_pass_mc.currentLabel
        if 'none' == computer_pass:
            board = get_board(user)
            move = referee.random_empty(board, 'white')
            if not move:
                move = 'pass'
    return move


from smart_go_format import next_move_file
def may_genmove_white(example_logger, gtp_envoy, users, user):
    '''precondition: black or white has been notified of their move.
    and now would be the time for white to take a few seconds to move.
    may_genmove_white
        if may_move:
            while not move_ok:
                if not follow_sgf_move:
                    choose_move:
                        gnugo or random
                why_not_move:
                    iterate_intersection
    >>> example_logger = setup_example_logger(level = logging.INFO)
    >>> gtp_envoy = go_text_protocol.setup_envoy(configuration.gtp_path, configuration.gtp_host, configuration.gtp_port)
    >>> setup_gtp = go_text_protocol.talk(gtp_envoy, 'set_random_seed 0')
    >>> users, ethan, mathijs = setup_users_partners_ethan_mathijs()
    >>> size = 9
    >>> may_genmove_white(example_logger, gtp_envoy, users, mathijs)
    {}

    Must be computer.
    >>> olds = imitate_news(ethan.root, get_white_computer_news(ethan) )
    >>> olds = imitate_news(mathijs.root, get_white_computer_news(mathijs) )

    To move, must be white's turn to play.
    >>> news, partner_news = update_turn(mathijs, 'black', {}, {})
    >>> olds = imitate_news(mathijs.root, news)
    >>> olds = imitate_news(ethan.root, partner_news)

    To move, author must see a game in play.
    >>> mathijs.root.game_over_mc.gotoAndPlay('none')

    If user option computer_pass none, and gnugo passes, make up a move.
    See computer_pass_example
    >>> news, partner_news = update_turn(mathijs, 'black', {}, {})
    >>> olds = imitate_news(mathijs.root, news)
    >>> olds = imitate_news(ethan.root, partner_news)
    >>> mathijs.root.option_mc.computer_pass_mc.gotoAndPlay('none')
    >>> mathijs.confirm_board_size('_3_3')
    >>> mathijs.play_history = [{'black': (1, 1)}]
    >>> mathijs.root._1_1_mc.gotoAndPlay('black')
    >>> mathijs.pb()
    ,,,
    ,X,
    ,,,
    >>> result = may_genmove_white(example_logger, gtp_envoy, users, mathijs)
    sgf_from_file: file not found
    >>> from pprint import pprint
    >>> ## pprint(result)
    >>> olds = imitate_news(mathijs.root, result)
    >>> mathijs.root.pass_white_mc.currentLabel
    'none'

    SGF prescribes white's next move.
    To move, must be white's turn to play.
    >>> marije = mathijs
    >>> news, partner_news = update_turn(marije, 'black', {}, {})
    >>> olds = imitate_news(marije.root, news)
    >>> olds = imitate_news(ethan.root, partner_news)
    >>> marije.confirm_board_size('_3_3')
    >>> news = label_from_to(marije.intersection_mc_array, 'white', 'empty_black')
    >>> olds = imitate_news(marije.root, news)
    >>> news = label_from_to(marije.intersection_mc_array, 'black', 'empty_black')

    White follows SGF.
    Head of history must specify same size of board as SGF.
    >>> olds = imitate_news(marije.root, news)
    >>> marije.play_history = [{'size': 3}, {'black': (1, 1)}]
    >>> marije.root._1_1_mc.gotoAndPlay('black')
    >>> marije.pb()
    ,,,
    ,X,
    ,,,
    >>> marije.root.sgf_file_txt.text = 'sgf/test_next_move.sgf'
    >>> result = may_genmove_white(example_logger, gtp_envoy, users, marije)
    >>> olds = imitate_news(marije.root, result)
    >>> marije.pb()
    ,O,
    ,X,
    ,,,

    Reset board.
    >>> marije.confirm_board_size('_5_5')
    >>> news = label_from_to(marije.intersection_mc_array, 'white', 'empty_black')
    >>> olds = imitate_news(marije.root, news)
    >>> news = label_from_to(marije.intersection_mc_array, 'black', 'empty_black')
    >>> olds = imitate_news(marije.root, news)
    >>> news, partner_news = update_turn(marije, 'black', {}, {})
    >>> olds = imitate_news(marije.root, news)
    >>> olds = imitate_news(ethan.root, partner_news)

    In SGF, I use a pass to mean any move is permitted.
    >>> marije.root.option_mc.computer_pass_mc.gotoAndPlay('none')
    >>> marije.root.sgf_file_txt.text = 'sgf/test_match_any.sgf'
    >>> marije.play_history = [{'size': 5}, {'black': (2, 2)}]
    >>> marije.root._2_2_mc.gotoAndPlay('black')
    >>> marije.pb()
    ,,,,,
    ,,,,,
    ,,X,,
    ,,,,,
    ,,,,,
    >>> any_label_equals(marije.intersection_mc_array, 'white')
    False
    >>> result = may_genmove_white(example_logger, gtp_envoy, users, marije)
    >>> olds = imitate_news(marije.root, result)
    >>> any_label_equals(marije.intersection_mc_array, 'white')
    True

    1/8 chance that white randomly picks above. 
    '''
    size = len(user.intersection_mc_array)
    news = {}
    if can_genmove_white(users, user):
        partner = get_partner(users, user)
        if 'black' == get_color(user):
            play_history = user.play_history
        else:
            play_history = partner.play_history
        why_not = 'have not tried'
        attempt = 0
        sgf_move = next_move_file(play_history, user.root.sgf_file_txt.text,
                'white')
        if sgf_move and sgf_move != 'pass':
            why_not = why_not_move(example_logger, gtp_envoy, 
                    users, user, partner, sgf_move)
        while why_not and attempt < 16:
            update_gtp = go_text_protocol.update_gnugo(gtp_envoy, play_history, size)
            move_gtp = go_text_protocol.talk(gtp_envoy, 'genmove white')
            logging.debug('may_genmove_white: move_gtp %s' % move_gtp)
            move = go_text_protocol.gtp_to_move(move_gtp, size)
            logging.debug('may_genmove_white: move %s' % move.__repr__())
            move = may_not_pass(user, move)
            why_not = why_not_move(example_logger, gtp_envoy, 
                    users, user, partner, move)
            attempt += 1
            if 15 <= attempt:
                import pdb; pdb.set_trace();
    return news

import copy
def reveal_history(play_history):
    revealed_history = copy.deepcopy(play_history)
    for event in revealed_history:
        if event.has_key('unhide'):
            event.pop('unhide')
        if event.has_key('hide'):
            event['unhide'] = event['hide']
    return revealed_history


    

def update_territory_and_score(gtp_envoy, user, play_history, color, row, column, 
        old_score, black_capture_total):
    '''Ethan, who was not updating territory before, now sees that his stone will be dead.
    >>> gtp_envoy = go_text_protocol.setup_envoy(configuration.gtp_path, 'localhost', 5903)
    >>> user = user_as.globe_class()
    >>> user.create(1)
    >>> user.setup_events()
    >>> update_territory_and_score(gtp_envoy, user, [], 'black', 4, 4, 0, 0)
    {'score_mc': {'bar_mc': {'currentLabel': '_0', 'marker_mc': {'currentLabel': 'neutral', 'change_txt': {'text': '0'}}, 'territory_txt': {'text': '0'}}}}
    >>> eat = [{'black': (1, 1)}, {'white': (0, 0)}, {'black': (0, 1)}]
    >>> news = update_territory_and_score(gtp_envoy, user, eat, 'black', 1, 1, 0, 0)
    >>> if news.get('_0_0_mc'):
    ...     news
    >>> user.root.territory_mc.gotoAndPlay('show')
    >>> news = update_territory_and_score(gtp_envoy, user, eat, 'black', 1, 1, 0, 0)
    >>> if not news.get('_0_0_mc') == {'territory_mc': {'currentLabel': 'black'}}:
    ...     news
    >>> user.root.dead_mc.gotoAndPlay('show')
    >>> news = update_territory_and_score(gtp_envoy, user, eat, 'black', 1, 1, 0, 0)
    >>> if not news.get('_0_0_mc') == {'territory_mc': {'currentLabel': 'white_dead'}}:
    ...     news

    Even if hidden, black still sees territory.
    On unhide, do not duplicate play at hide.
    >>> hide_eat = [{'black': (1, 1), 'hide': [(1, 1)]}, {'white': (0, 0)}, {'black': (0, 1), 'hide': [(0, 1)]}, {'white': (8, 8)}, {'black': (8, 7), 'hide': [(8, 7)]}, {'white': (8, 6), 'unhide': [(8, 7)]}]
    >>> user.root.dead_mc.gotoAndPlay('none')
    >>> news = update_territory_and_score(gtp_envoy, user, hide_eat, 'black', 1, 1, 0, 0)
    >>> if not news.get('_0_0_mc') == {'territory_mc': {'currentLabel': 'black'}}:
    ...     news
    >>> user.root.dead_mc.gotoAndPlay('show')
    >>> news = update_territory_and_score(gtp_envoy, user, hide_eat, 'black', 1, 1, 0, 0)
    >>> if not news.get('_0_0_mc') == {'territory_mc': {'currentLabel': 'white_dead'}}:
    ...     news
   
    Moonhyoung sees profit on his new castle.
    >>> user.root.game_over_mc._5_5_mc.confirm_mc.dispatchEvent(mouseDown)
    >>> len(user.intersection_mc_array)
    5

    History must include the last move.
    >>> user.root.profit_mc.gotoAndPlay('show')
    >>> user.root.decoration_mc.gotoAndPlay('show')
    >>> black_1_1 = [{'black': (1, 1)}]
    >>> news = update_territory_and_score(gtp_envoy, user, black_1_1, 'black', 1, 1, 0, 0)
    >>> news['score_mc']['bar_mc']['marker_mc']['change_txt']['text']
    '+5'
    >>> news.get('_1_1_mc')
    >>> news = update_territory_and_score(gtp_envoy, user, [{'black': (2, 2)}], 'black', 2, 2, 0, 0)
    >>> news['score_mc']['bar_mc']['marker_mc']['change_txt']['text']
    '+24'

    Moonhyoung sees double roof at 2,2
    >>> news['_2_2_mc']['black_shape_mc']['defend_mc']['profit_mc']['currentLabel']
    'show'

    For example, go_rule_example.py: capture_example
    #>>> import client; client = reload(client); from client import *
    #>>> code_unit.inline_examples(
    ...     capture_example.__doc__, 
    ...     locals(), globals(), 
    ...     verify_examples = False)
    #>>> score_news = update_territory_and_score(gateway_process.gtp_envoy, 
    ...     ethan, joris.play_history, 'white', 1, 2, 0, 0)
    #>>> if not {'territory_mc': {'currentLabel': 'white'}} == score_news.get('_0_2_mc'):
    ...     score_news
    '''
    # DEBUG: if 'white' in play_history[-1]:
    # DEBUG:      if (2, 4) == play_history[-1]['white']:
    # DEBUG:          import pdb; pdb.set_trace();
    if 'none' == user.root.territory_mc.currentLabel:
        values_dictionary = go_text_protocol.neutral_territory_values_dictionary
    elif 'none' == user.root.dead_mc.currentLabel:
        values_dictionary = go_text_protocol.no_dead_territory_values_dictionary
    elif 'show' == user.root.dead_mc.currentLabel:
        values_dictionary = go_text_protocol.territory_values_dictionary
    score, territory_labels = go_text_protocol.update_score_and_territory(
        gtp_envoy, 
        reveal_history(play_history), 
        size = len(user.intersection_mc_array),
        values_dictionary = values_dictionary
    )
    score += black_capture_total
    score_news = get_score_news(old_score, score)
    if 'show' == user.root.profit_mc.currentLabel:
        profit = score - old_score
        if 'show' == user.root.decoration_mc.currentLabel:
            profit_news = get_profit_news(user.intersection_mc_array, 
                    row, column, profit)
            score_news = upgrade(score_news, profit_news)
    territory_news = get_territory_news(user.intersection_mc_array, territory_labels)
    # DEBUG: if '_2_2_mc' in territory_news:
    # DEBUG:     import pdb; pdb.set_trace();
    score_news = upgrade(score_news, territory_news)
    return score_news


def territory_is_dead(news, intersection_name):
    '''Territory is marked dead.
    >>> territory_is_dead({}, '_0_0_mc')
    False
    '''
    dead = False
    intersection = news.get(intersection_name)
    if intersection:
        territory = intersection.get('territory_mc')
        if territory:
            label = territory.get('currentLabel')
            if 'black_dead' == label or 'white_dead' == label:
                dead = True
    return dead


def preview_stone(gtp_envoy, users, user, intersection_mc, color, user_news):
    '''Place a stone on the board.
    >>> users, ethan, joris = setup_ethan_joris()
    >>> news = {'_0_8_mc': {'currentLabel': 'preview_black'}}
    >>> joris.revise(news)
    >>> gtp_envoy = go_text_protocol.setup_envoy(configuration.gtp_path, 'localhost', 5903)
    >>> setup_gtp = go_text_protocol.talk(gtp_envoy, 'set_random_seed 0')
    >>> news = preview_stone(gtp_envoy, users, joris, joris.root._0_8_mc, 'black', news)
    >>> news['_0_8_mc']['currentLabel'] 
    'question_black'
    >>> news = {'_0_8_mc': {'currentLabel': 'preview_hide_black'}}
    >>> joris.revise(news)
    >>> news = preview_stone(gtp_envoy, users, joris, joris.root._0_8_mc, 'black', news)
    >>> news['_0_8_mc']['currentLabel'] 
    'question_hide_black'

    May see critical.  see user_interface_example.py:critical_example
    >>> users, ethan, joris = setup_ethan_joris()
    >>> joris.play_history = [{'black': (2, 2)}, {'white': (1, 1)}]
    >>> news = {'_2_2_mc': {'currentLabel': 'black'}}
    >>> joris.revise(news)
    >>> news = {'_1_1_mc': {'currentLabel': 'white'}}
    >>> joris.revise(news)
    >>> news = {'_1_2_mc': {'currentLabel': 'preview_black'}}
    >>> joris.revise(news)
    >>> news = preview_stone(gtp_envoy, users, joris, joris.root._1_2_mc, 'black', news)
    >>> news.get('_1_2_mc').get('top_move_mc')
    >>> news.get('_2_1_mc').get('top_move_mc')

    Optionally, see top_move of white.
    >>> from pprint import pprint
    >>> if not news.get('_6_2_mc').get('top_move_mc') == {'currentLabel': 'white'}:
    ...     pprint(news)
    >>> joris.root.top_move_mc.gotoAndPlay('none')
    >>> news = preview_stone(gtp_envoy, users, joris, joris.root._1_2_mc, 'black', news)
    >>> if 'top_move_mc' in news.get('_6_2_mc', []):
    ...     pprint(news['_6_2_mc']['top_move_mc'])

    See news in problem.
    >>> yuji = joris
    >>> yuji.root.sgf_file_txt.text = 'sgf/test_capture_3_3.sgf'
    >>> news = {'_0_0_mc': {'currentLabel': 'preview_black'}}
    >>> news = preview_stone(gtp_envoy, users, yuji, yuji.root._0_0_mc, 'black', news)
    >>> news.has_key('comment_mc')
    False

    Clear previous top_move of white.
    
    If in danger, do not show critical or vital.  
    see user_interface_example.py:preview_critical_danger_example

    If change in territory, see preview_territory_example
    '''
    ok, news = prepare_stone(users, user, intersection_mc, color, user_news)
    if not ok:
        return news
    previewing = {'cursor_mc': {'act_mc': {'currentLabel': 'preview'}}}
    # XXX see white_formation_example:  prevent rollback to previous preview.
    user.revise(previewing)
    news = upgrade(news, previewing)
    # follow sgf.  see emmet* yuji_capture_3_3_example:  first move
    #on_path, on_path_reply = on_problem_path(user, intersection_mc)
    #news = upgrade(news, on_path_reply)
    path_news = update_path(user, intersection_mc)
    news = upgrade(news, path_news)
    label = intersection_mc.currentLabel
    partner = get_partner(users, user)
    capture_news, partner_news, new_board, black_capture_total = \
            get_capture_news(user, partner, intersection_mc)
    news = upgrade(news, capture_news)
    # capture news overwrites question with black, so go back to question.
    question_label = label.replace('preview_', 'question_')
    move = {intersection_mc.name: {'currentLabel': question_label}}
    news = upgrade(news, move)
    color = get_color(user)
    row, column = get_row_column(intersection_mc.name)
    preview_event = {color: (row, column)}
    preview_history = user.play_history + [preview_event]
    board_size = len(new_board) 
    show_top_move = user.root.top_move_mc.currentLabel == 'show'
    if show_top_move:
        top_move_news = get_top_move_news(gtp_envoy, preview_history, 
            user.intersection_mc_array, 'white', 'white', board_size)
        news = upgrade(news, top_move_news)
    show_critical = user.root.critical_mc.currentLabel == 'show'
    if show_critical:
        # XXX before change this block: modify expectation at
        # user_interface_example.py:critical_example
        dangers = referee.find_danger(new_board)
        if (row, column) not in dangers:
            #! # XXX critical news slows less than 0.06125 seconds 
            # last turn's history, not counting preview.
            critical_news = get_critical_news(gtp_envoy, preview_history, 
                    new_board, color, row, column, user.intersection_mc_array)
            news = upgrade(news, critical_news)
    def _preview_territory(news):
        '''If change in territory, see preview_territory_example'''
        show_territory = user.root.territory_mc.currentLabel == 'show'
        if show_territory:
            author = user
            old_score = int(author.root.score_mc.bar_mc.territory_txt.text)
            score_news = update_territory_and_score(gtp_envoy, author,
                    preview_history, color, row, column, 
                    old_score, black_capture_total)
            news = upgrade(news, score_news)
    _preview_territory(news)
    # XXX before change this block: modify expectation at
    # user_interface_example.py:territory_dead_defend_example
    dead = territory_is_dead(news, intersection_mc.name)
    formation_news = may_get_formation_news(new_board, user, 
            user.intersection_mc_array, intersection_mc, dead = dead)
    news = upgrade(news, formation_news)
    unconditional_status_news = may_get_unconditional_status_news(
            user, preview_history, new_board, color, row, column)
    news = upgrade(news, unconditional_status_news)
    return news


def may_get_unconditional_status_news(user, play_history, 
        board, color, row, column):
    '''XXX before change this function: modify expectation at
    user_interface_example.py:unconditional_status_example
        after preview or play:  
        if show_unconditional: unconditional_status of last stone.
        if not undecided:  get dragon_stones of last stone 
            and mark their unconditional_status_mc.
    '''
    news = {}
    show_unconditional_status = user.root.unconditional_status_mc.currentLabel == 'show'
    if show_unconditional_status:
        sgf_file = 'sgf/_unconditional_status.sgf'
        board_size = len(board)
        save_sgf(play_history, sgf_file, size = board_size)
        status = go_text_protocol.get_unconditional_status(sgf_file, 
                row, column, board_size)
        if 'alive' == status or 'dead' == status:
            dragons = go_text_protocol.get_dragon_coordinates(sgf_file, 
                    row, column, size = board_size)
            label = color + '_' + status
            news = child_label_to(dragons, 'unconditional_status_mc', label)
            if 'alive' == status:
                child_labels = {
                    'block_north_mc': 'none',
                    'block_east_mc': 'none',
                    'block_south_mc': 'none',
                    'block_west_mc': 'none'}
                block_news = child_labels_to(dragons, child_labels)
                news = upgrade(news, block_news)
    return news


def place_stone(gtp_envoy, users, user, intersection_mc, color, user_news):
    '''Try to place a stone on the board, update turn, score, captures, territory.
    #Prevent repeating immediately previous board.
    #>>> code_unit.doctest_unit(client.capture_example, log = False)

    #Black sees white's formation.
    #>>> code_unit.doctest_unit(client.white_formation_example, log = False)

    #Maximum of two turns in a row.  Only extra stone if not already using.
    #>>> code_unit.doctest_unit(client.extra_stone_limit_example, log = False)

    TODO:  Debug doctest with mock to run multiple tests.
    TODO:  Speed up test.
    >>> import client; client = reload(client); from client import *
    >>> code_unit.inline_examples(
    ...     ethan_joris_start_example.__doc__, 
    ...     locals(), globals(), 
    ...     verify_examples = False)
   
    >>> wait = 4.0 / black._speed
    >>> mouse_down_and_sleep(black, black.root._0_1_mc, wait)
    >>> mouse_down_and_sleep(black, black.root._0_1_mc, wait)
    >>> mouse_down_and_sleep(white, white.root._0_0_mc, wait)

    Show white's last move to black.
    >>> black_user = gateway_process.users.get('joris')
    >>> white_user = gateway_process.users.get('ethan')
    >>> if property_diff(black_user, black_user.root._0_0_mc.last_move_mc, 
    ...         'currentLabel', 'white'):
    ...     black_user.pb()

    Reveal black assassin.
    >>> user_news = {'_1_0_mc': {'currentLabel': 'play_hide_black'}}
    >>> black_user.revise(user_news)
    >>> news = place_stone(gateway_process.gtp_envoy, gateway_process.users, 
    ...     black_user, black_user.root._1_0_mc, 'black', user_news)
    >>> if not news['_1_0_mc']['currentLabel'] == 'black':  news
    >>> if not black_user.play_history[-1].get('black') == (1, 0):
    ...     black_user.play_history[-1]
    >>> if not black_user.play_history[-1].get('hide') == [(1, 0)]:
    ...     black_user.play_history[-1]

    Show last move to black.
    >>> if not news.get('_1_0_mc').get('last_move_mc'):  news

    If revealed, show last move to white.
    >>> white_user.root._1_0_mc.last_move_mc.currentLabel
    'black'

    If not used to assassinate, do not reveal hidden.
    >>> mouse_down_and_sleep(white, white.root._0_2_mc, wait)

    >>> user_news = {'_0_3_mc': {'currentLabel': 'play_hide_black'}}
    >>> black_user.revise(user_news)
    >>> news = place_stone(gateway_process.gtp_envoy, gateway_process.users, 
    ...     black_user, black_user.root._0_3_mc, 'black', user_news)
    >>> if not news['_0_3_mc']['currentLabel'] == 'hide_black':  news['_0_3_mc']

    If hidden, hide last move from white.
    For acceptance, see steven_ethan_hide_example
    >>> white_user.root._0_3_mc.last_move_mc.currentLabel
    'none'

    for eat, see also client.real_time_example
    #>>> code_unit.doctest_unit(client.real_time_example)
    for get_critical_news also see client.vital_point_example
    #>>> code_unit.doctest_unit(client.vital_point_example)
    
    if not on sgf path, then do not place stone.
    follow sgf.  see emmet_capture_3_3_example:  first move
    >>> emmet = black_user
    >>> emmet.root.sgf_file_txt.text = 'sgf/test_capture_3_3.sgf'
    >>> user_news = {'_0_2_mc': {'currentLabel': 'play_black'}}
    >>> news = place_stone(gateway_process.gtp_envoy, gateway_process.users, 
    ...     black_user, black_user.root._0_2_mc, 'black', user_news)
    >>> if not news.get('bad_move_mc'):  news
    >>> if not 'play' == news['cursor_mc']['act_mc']['currentLabel']:  news
    >>> news.get('_0_2_mc')
    >>> user_news = {'_1_1_mc': {'currentLabel': 'play_black'}}
    >>> news = place_stone(gateway_process.gtp_envoy, gateway_process.users, 
    ...     black_user, black_user.root._1_1_mc, 'black', user_news)
    >>> if news.get('bad_move_mc'):  news
    >>> if not news.get('_1_1_mc'):  news

    So that white may move, update turn to white.
    >>> olds = imitate_news(black_user.root, news)
    >>> if not 'white' == black_user.root.turn_mc.currentLabel:
    ...     news
    >>> black_user.root.sgf_path_txt.text
    '[1, 1]'

    Check author for SGF.  So partner need not have SGF or path.
    On second move, SGF allows white to move anywhere (denoted by pass W[])
    >>> white_user.root.sgf_file_txt.text = ''
    >>> white_user.root.sgf_path_txt.text = '[]'
    >>> black_user.pb()
    ,XX/,,,,,
    XX,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    >>> user_news = {'_1_2_mc': {'currentLabel': 'play_white'}}
    >>> news = place_stone(gateway_process.gtp_envoy, gateway_process.users, 
    ...     white_user, white_user.root._1_2_mc, 'white', user_news)
    >>> if news.get('bad_move_mc'):  news
    >>> if not news.get('_1_2_mc'):  news

    Partner is author and receives next tutor message.
    >>> black_user.root.tutor_mc.currentLabel
    'surround'

    Partner may also receive news of liberty shortage.
    >>> black_user.root.option_mc.block_mc.currentLabel
    'show'
    >>> black_user.root._1_2_mc.block_north_mc.currentLabel
    'white_warning'

    Optionally win by first capture.
    >>> users, partner, user = setup_users_white_black('ethan', 'laurens')
    >>> user.intersection_mc_array = user_as.get_intersection_array(user.root, 3)
    >>> partner.intersection_mc_array = user_as.get_intersection_array(partner.root, 3)
    >>> user.root.option_mc.first_capture_mc.gotoAndPlay('show')
    >>> board_news = board_to_news(referee.board_pre_capture_3_3, 
    ...     user.intersection_mc_array, 'black')
    >>> olds = user_as.imitate_news(user.root, board_news)
    >>> user.pb()
    ,,,
    ,,X
    ,,O
    >>> user_news = {'_2_1_mc': {'currentLabel': 'play_black'}}
    >>> user.revise(user_news)
    >>> user.pb()
    ,,,
    ,,X
    ,*O
    >>> news = place_stone(gateway_process.gtp_envoy, users, 
    ...     user, user.root._2_1_mc, 'black', user_news)
    >>> news.get('game_over_mc').get('currentLabel')
    'win'
    '''
    news, partner_news = {}, {}
    ok, news = prepare_stone(users, user, intersection_mc, color, user_news)
    if not ok:
        return news
    label = user_news.get(intersection_mc.name).get('currentLabel')
    partner = get_partner(users, user)
    if 'black' == get_color(user):
        author = user
        author_news = news
    elif 'black' == get_color(partner):
        author = partner
        author_news = partner_news
    else:
        logging.error('place_stone: who is black? %s' % intersection_mc.name)
    # follow sgf.  see emmet* yuji_capture_3_3_example:  first move
    path_news = update_path(author, intersection_mc)
    news = upgrade(news, path_news)
    partner_news = upgrade(partner_news, path_news)
    # prohibit bad_move
    if path_news.has_key('bad_move_mc'):
        bad_move = news.get('bad_move_mc')
        if bad_move:
            if 'show' == bad_move.get('currentLabel'):
                empty = 'empty_' + color
                not_here = {
                    intersection_mc.name: {
                        'currentLabel': empty}
                }
                news = upgrade(news, not_here)
                if get_color(user) == user.root.turn_mc.currentLabel:
                    news = upgrade(news, 
                        {'cursor_mc': {'act_mc': {'currentLabel': 'play'}}})
                return news
    # prohibit_danger:  see emmet_capture_3_3_example
    if 'show' == user.root.option_mc.prohibit_danger_mc.currentLabel:
        danger, danger_reply = in_danger(user.intersection_mc_array, 
                intersection_mc)
        if danger:
            news = upgrade(news, danger_reply)
            return news
    capture_news, partner_capture_news, new_board, black_capture_total = \
            get_capture_news(user, partner, intersection_mc)
    news = upgrade(news, capture_news)
    partner_news = upgrade(partner_news, partner_capture_news)
    if 'play_hide_black' == label:
        empty_news = label_from_to(user.intersection_mc_array, 
                    'empty_hide_black', 'empty_black')
        news = upgrade(news, empty_news)
        cursor_news = {'cursor_mc': {'currentLabel': color}} 
        news = upgrade(news, cursor_news)
    # update turn if turn-based, XXX see client.real_time_example
    if 'turn' == author.root.clock_mc.currentLabel:
        news, partner_news = update_turn(user, color, news, partner_news)
        # see yuji_capture_3_3_example
        partner_news = update_empty_block(partner, new_board,
                get_color(partner), partner_news)
    elif 'time' == author.root.clock_mc.currentLabel:
        # see client.real_time_example
        if '_1' == user.root.cursor_mc.extra_stone_mc.currentLabel:
            lose_extra_stone = {'cursor_mc':  {'extra_stone_mc': 
                {'currentLabel':  '_0'}}}
            news = upgrade(news, lose_extra_stone)
        else:
            eat_news = {
                'eat_mc': {
                    'act_mc': {
                        'currentLabel': 'eat'
                    },
                    'x': intersection_mc.x,
                    'y': intersection_mc.y}
            }
            news = upgrade(news, eat_news)
            # partner finishes eating.  see client.real_time_example
            partner_eat_news = {
                'eat_mc': {
                    'act_mc': {
                        'currentLabel': 'none'
                    }
                }
            }
            partner_news = upgrade(partner_news, partner_eat_news)
    else:
        logging.error('place_stone: what is clock label? %s' % intersection_mc.name)
    row, column = get_row_column(intersection_mc.name)
    old_score = int(author.root.score_mc.bar_mc.territory_txt.text)
    play_history = author.play_history
    play_history.append({})
    play_history[-1][color] = row, column
    if color == 'black':
        if 'play_hide_black' == label:
            play_history[-1]['hide'] = [(row, column)]
        score_news = update_territory_and_score(gtp_envoy, user,
                play_history, color, row, column, 
                old_score, black_capture_total)
        news = upgrade(news, score_news)
        # XXX find repeat see client.capture_example
        user.board_history.append(new_board)
        if 2 <= len(user.board_history):
            previous_board = user.board_history[-2]
            partner_color = get_color(partner)
            # TODO: repeat_news = get_repeat_news(previous_board, new_board, 
            # TODO:         partner_color, partner)
            # TODO: partner_news = upgrade(partner_news, repeat_news)
        # XXX before change this block: modify expectation at
        # user_interface_example.py:territory_dead_defend_example
        dead = territory_is_dead(news, intersection_mc.name)
        formation_news = may_get_formation_news(new_board, user, 
                user.intersection_mc_array, intersection_mc, dead = dead)
        news = upgrade(news, formation_news)
        if formation_news:
            gift_news = may_get_gift_news(user)
            news = upgrade(news, gift_news)
        #    if '_0' == user.root.cursor_mc.extra_stone_mc.currentLabel:
        #        news = reward_formation(user, intersection_mc, news)
        #- last_move_news = user_as.get_last_move_news(intersection_mc, color)
        #- news = upgrade(news, last_move_news)
        # news for black.  see sgf_judith_begins_example
        sgf_news = news
        unconditional_status_news = may_get_unconditional_status_news(
            user, play_history, new_board, color, row, column)
        news = upgrade(news, unconditional_status_news)
    elif color == 'white':
        # XXX how much of this is symmetrical to 'black' branch?
        # show white's formation to black but not to white.
        # to stabilize score and encourage by a rising score,
        # only update territory and score after white's turn.
        score_news = update_territory_and_score(gtp_envoy, author,
                play_history, color, row, column, 
                old_score, black_capture_total)
        partner_news = upgrade(partner_news, score_news)
        # XXX find repeat see client.capture_example
        partner.board_history.append(new_board)
        if 2 <= len(partner.board_history):
            previous_board = partner.board_history[-2]
            partner_color = get_color(partner)
            # TODO: repeat_news = get_repeat_news(previous_board, new_board, 
            # TODO:         partner_color, partner)
            # TODO: partner_news = upgrade(partner_news, repeat_news)
        # user_interface_example.py:territory_dead_defend_example
        dead = territory_is_dead(partner_news, intersection_mc.name)
        formation_news = may_get_formation_news(new_board, partner, 
                author.intersection_mc_array, intersection_mc, dead = dead)
        partner_news = upgrade(partner_news, formation_news)
        #formation_enabled = False
        #if formation_enabled:
        #    # XXX see client.formation_example
        #    clear_formation_news = get_clear_formation_news(partner.root)
        #    partner_news = upgrade(partner_news, clear_formation_news)
        #    # XXX see client.white_formation_example
        #    partner.revise(clear_formation_news)
        #    formation_news = get_formation_news(new_board, user.intersection_mc_array, 
        #        intersection_mc)
        #    partner_news = upgrade(partner_news, formation_news)
        sgf_news = partner_news
        unconditional_status_news = may_get_unconditional_status_news(
            partner, play_history, new_board, color, row, column)
        partner_news = upgrade(partner_news, unconditional_status_news)
    else:
        logging.error('place_stone: which color is this? %s' % color)
    # XXX before and after modifying top_move, modify:
    # user_interface_example.py: influence_and_top_move_sgf_example
    # acceptance:  steven_ethan_hide_example
    # playtest.py:  moonhyoung_kyung_animation_example
    #if 'show' == user.root.top_move_mc.currentLabel:
    #    logging.debug('top_move after %s,%s' % (row, column))
    #    top_move_color = clear_color = get_color(partner)
    #    board_size = len(new_board)
    #    top_move_news = get_top_move_news(gtp_envoy, play_history, 
    #            user.intersection_mc_array, clear_color, 
    #            top_move_color, board_size)
    #    news = upgrade(news, top_move_news)
    if 'show' == partner.root.top_move_mc.currentLabel:
        logging.debug('top_move after %s,%s' % (row, column))
        top_move_color = clear_color = get_color(user)
        board_size = len(new_board)
        top_move_news = get_top_move_news(gtp_envoy, play_history, 
                partner.intersection_mc_array, clear_color, 
                top_move_color, board_size)
        partner_news = upgrade(partner_news, top_move_news)
    last_move_news = get_last_move_news(
            author.intersection_mc_array, color, row, column)
    news = upgrade(news, last_move_news)
    if 'play_hide_black' != label:
        last_move_news = get_last_move_news(
            partner.intersection_mc_array, color, row, column)
        partner_news = upgrade(partner_news, last_move_news)
    # XXX before change this block: modify expectation at
    # user_interface_example.py:critical_example
    show_critical = user.root.critical_mc.currentLabel == 'show'
    if show_critical:
        dangers = referee.find_danger(new_board)
        if (row, column) not in dangers:
            #! # XXX critical news slows less than 0.06125 seconds 
            # last turn's history, not counting preview.
            critical_news = get_critical_news(gtp_envoy, play_history, 
                    new_board, color, row, column, author.intersection_mc_array)
            news = upgrade(news, critical_news)
    partner_show_critical = partner.root.critical_mc.currentLabel == 'show'
    if partner_show_critical:
        # before modifying, validate h1_dominate_3_3_example
        #dangers = referee.find_danger(new_board)
        #if (row, column) not in dangers:
            #! # XXX critical news slows less than 0.06125 seconds 
            # last turn's history, not counting preview.
        critical_news = get_critical_news(gtp_envoy, play_history, 
                new_board, color, row, column, author.intersection_mc_array)
        partner_news = upgrade(partner_news, critical_news)
    # Optionally win by first capture.
    # before modifying, modify expectations in jerry_captured_example
    first_capture = False
    if 'show' == user.root.option_mc.first_capture_mc.currentLabel:
        first_capture = True
    elif 'show' == partner.root.option_mc.first_capture_mc.currentLabel:
        first_capture = True
    if first_capture:
        if black_capture_total:
            score = black_capture_total # * first_capture
            #user_score_news = final_score_news(score)
            #news = upgrade(news, user_score_news)
            #menu_news = {'menu_mc': {'currentLabel': 'show'}}
            #news = upgrade(news, menu_news)
            #partner_score_news = final_score_news(0 - score)
            #partner_news = upgrade(partner_news, partner_score_news)
            #menu_news = {'menu_mc': {'currentLabel': 'show'}}
            #partner_news = upgrade(partner_news, menu_news)
            # >>> code_unit.doctest_unit(yuji_capture_3_3_example)
            # >>> code_unit.doctest_unit(yuji_capture_5_5_example)
            insert_prize_news(score, users, user, partner, news, partner_news)
    # Update progress.  user_interface_example.py:  rene_progress_example
    news = update_progress_news(user.intersection_mc_array, news)
    partner_news = update_progress_news(partner.intersection_mc_array, partner_news)
    tell(partner, partner_news)
    # news for black.  see sgf_judith_begins_example
    # note is old, from one turn ago.
    play_history[-1]['news'] = sgf_news
    decoration_note = get_decoration_note(author.intersection_mc_array)
    play_history[-1]['note'] = decoration_note
    sgf_file = 'sgf/_gogui.sgf'
    board_size = len(new_board)
    save_sgf(play_history, sgf_file, size = board_size)
    return news


# Users and GTP

def iterate_intersection(example_logger, gtp_envoy, 
        users, user, intersection_mc, news):
    '''Next state of the intersection or help.
    TODO:  Speed up this example.
    >>> import client; client = reload(client); from client import *
    >>> code_unit.inline_examples(
    ...     ethan_joris_start_example.__doc__, 
    ...     locals(), globals(), 
    ...     verify_examples = False)
    >>> example_logger = logging
    >>> joris_user = gateway_process.users['joris']
    >>> intersection_mc = joris_user.root._0_0_mc
    >>> news = {'_0_0_mc': {'currentLabel': 'play_black'}}
    >>> reply = iterate_intersection(gateway_process.example_logger, 
    ...     gateway_process.gtp_envoy, gateway_process.users, 
    ...     joris_user, intersection_mc, news)
    >>> reply.get('_0_0_mc').get('currentLabel')
    'black'
    >>> olds = imitate_news(joris_user.root, reply)

    Help black and revert cursor to not busy.
    >>> news = {'_0_0_mc': {'currentLabel': 'black'}}
    >>> reply = iterate_intersection(gateway_process.example_logger, 
    ...     gateway_process.gtp_envoy, gateway_process.users, 
    ...     joris_user, intersection_mc, news)
    >>> reply.get('_0_0_mc').get('currentLabel')
    'black'
    >>> reply.get('help_mc').get('currentLabel')
    'warning'
    >>> reply['cursor_mc']['act_mc']['currentLabel']
    'play'
    >>> olds = imitate_news(joris_user.root, reply)

    Do not help white.
    >>> ethan_user = gateway_process.users['ethan']
    >>> olds = imitate_news(ethan_user.root, reply)
    >>> intersection_mc = ethan_user.root._0_0_mc
    >>> news = {'_0_0_mc': {'currentLabel': 'black'}}
    >>> reply = iterate_intersection(gateway_process.example_logger, 
    ...     gateway_process.gtp_envoy, gateway_process.users, 
    ...     ethan_user, intersection_mc, news)
    >>> reply.get('help_mc')
    '''
    mouse_log = write_mouse_down(user, intersection_mc)
    # if '_3_5_mc' == intersection_mc.name:
    # if '_4_4_mc' == intersection_mc.name:
    #     import pdb; pdb.set_trace(); 
    example_logger.info(mouse_log)
    ## import pdb; pdb.set_trace();
    reply = {}
    label = news.get(intersection_mc.name).get('currentLabel')
    if 'preview_black' == label:
        reply = preview_stone(gtp_envoy, users, user, intersection_mc, 
                'black', news)
    elif 'preview_hide_black' == label:
        reply = preview_stone(gtp_envoy, users, user, intersection_mc, 
                'black', news)
    elif 'play_black' == label:
        reply = place_stone(gtp_envoy, users, user, intersection_mc, 'black', news)
    elif 'play_hide_black' == label:
        reply = place_stone(gtp_envoy, users, user, intersection_mc, 'black', news)
    elif 'play_white' == label:
        #- reply = place_expert_stone(users, user, intersection_mc, 'white')
        reply = place_stone(gtp_envoy, users, user, intersection_mc, 'white', news)
    elif 'black' == label or 'white' == label:
        reply = {intersection_mc.name: 
                {'currentLabel': intersection_mc.currentLabel}}
        if get_color(user) == user.root.turn_mc.currentLabel:
            reply = upgrade(reply, {'cursor_mc': {'act_mc': {'currentLabel': 'play'}}})
        if 'black' == get_color(user):
            help = get_help(intersection_mc)
            reply = upgrade(reply, help)
    elif 'x' not in news[intersection_mc.name]:
        ##- import pdb; pdb.set_trace();
        what_is_intersection = 'receive: what do i do with intersection %s.currentLabel = %s?' \
            % (intersection_mc.name, intersection_mc.currentLabel)
        logging.error(what_is_intersection)
        reply = {'gateway_mc':  
            {'currentLabel': 'what_message'}}
    return reply


def may_pass_news(example_logger, gtp_envoy, users, user, news):
    '''See user_interface_example.py:  
        draw_example, win_example, lose_example, computer_pass_example
        user_pass_to_computer_example
        score hidden stones as well.

    if pass is bad move in sgf, disallow pass.  black must move.
    >>> users, h2, h1 = setup_users_white_black('h2', 'h1')
    >>> h1.root.bad_move_mc.gotoAndPlay('show')
    >>> passed, reply = may_pass_news(logging, None, users, h1, {'pass_mc': {'dispatchEvent': 'mouseDown'}})
    >>> passed
    False
    >>> h1.root.bad_move_mc.currentLabel
    'show'
    >>> passed, reply = may_pass_news(logging, None, users, h1, {'pass_mc': {'dispatchEvent': 'mouseDown'}, 'bad_move_mc': {'currentLabel': 'show'}})
    >>> passed
    False

    If pass, reply does not contain pass or white's turn.
    >>> users, h2, h1 = setup_users_white_black('h2', 'h1')
    >>> h1.root.bad_move_mc.gotoAndPlay('none')
    >>> h1.root.turn_mc.gotoAndPlay('black')
    >>> passed, reply = may_pass_news(logging, None, users, h1, {'pass_mc': {'dispatchEvent': 'mouseDown'}})
    >>> passed
    True

    Reset button.  Ideally super user would reset, 
    but that requires refactoring to access outgoing news.
    >>> reply['pass_mc']['currentLabel']
    'none'
    >>> reply['pass_white_mc']['currentLabel']
    'none'
    >>> reply.get('turn_mc')
    >>> reply.get('turn_veil_mc')

    Yet it is white's turn, or computer takes white's turn.
    >>> h1.root.turn_mc.currentLabel
    'white'

    acceptance tests
    h1_pass_example
    h1_pass_computer_example
    h1_see_computer_pass_example
    pass_win_example
    robby_pass_example
    '''
    if not validate_pass(news) \
            or 'show' == user.root.bad_move_mc.currentLabel:
        ## import pdb; pdb.set_trace();
        return False, news
    #user_reply = {}
    passed, user_reply = update_pass_news(users, user, news)
    if passed:
        ## import pdb; pdb.set_trace();
        name = user.root.title_mc.username_txt.text
        pass_log = '>>> %s.root.pass_mc.dispatchEvent(mouseDown)' % name
        example_logger.info(pass_log)
        partner = get_partner(users, user)
        partner_reply = copy.deepcopy(user_reply)
        game_over_object = user_reply.get('game_over_mc')
        if game_over_object \
                and 'score' == game_over_object.get('currentLabel'):
            author = get_author(users, user)
            board = get_board(author)
            size = len(board)
            next_player_gtp = go_text_protocol.update_gnugo(
                    gtp_envoy, reveal_history(author.play_history), size) 
            score = go_text_protocol.final_score(gtp_envoy, 
                    offset_komi = 5.5)
            #if author == partner:
            #    score = 0 - score
            #user_score_news = final_score_news(score)
            #user_reply = upgrade(user_reply, 
            #        user_score_news)
            #menu_news = {'menu_mc': {'currentLabel': 'show'}}
            #user_reply = upgrade(user_reply, 
            #        menu_news)
            #partner_score_news = final_score_news(0 - score)
            #partner_reply = upgrade(partner_reply, 
            #        partner_score_news)
            #menu_news = {'menu_mc': {'currentLabel': 'show'}}
            #partner_reply = upgrade(partner_reply, 
            #        menu_news)
            insert_prize_news(score, users, user, partner, 
                    user_reply, partner_reply)
            tell(partner, partner_reply)
        else:
            color = get_color(user)
            user_reply, partner_reply = update_turn(user, color, 
                user_reply, partner_reply)
            # XXX HACK multiple revise, tell, tell, publish in one iteration.
            user.publish(user_reply)
            tell(partner, partner_reply)
            genmove_news = may_genmove_white(example_logger, 
                    gtp_envoy, users, user)
            # user_reply = genmove_news
            user_reply = {} # XXX UNTESTED 
            user_reply = upgrade(user_reply, genmove_news)
            reset_my_pass = {'pass_white_mc': {'currentLabel': 'none'}}
            user_reply = upgrade(user_reply, reset_my_pass)
        reset_pass = {'pass_mc': {'currentLabel': 'none'}}
        user_reply = upgrade(user_reply, reset_pass)
    return passed, user_reply


# End users and GTP


# load and save remote_control stage to file.

from client import load, save_file_name

def get_no_master_news():
    return {
        'title_mc': {
            'master_txt': {
                'text': 'master'
            }, 
            'slave_txt': {
                'text': 'slave'
            } 
        } 
    }
    
def save_stage(message, save_file_name):
    '''save remote_control stage to file.
    replace master and slave as unset.
    '''
    save_done = {'save_mc': {'currentLabel': 'none'}}
    message = upgrade(message, save_done)
    message = upgrade(message, get_no_master_news())
    import pprint
    import text
    tree_txt = pprint.pformat(message)
    import shutil
    backup = save_file_name + '.bak'
    shutil.copyfile(save_file_name, backup)
    text.save(save_file_name, tree_txt)
    return save_done

def load_one_child(root, child_list):
    '''Load from server.
    Because 96 kB leads server to complain of error, load in parts.
    Does not change x,y.'''
    child = child_list.pop(0)
    if child_list:
        root['load_mc'].gotoAndPlay('entering')
        loading = compose_root(insert_label, root['load_mc'], child)
    else:
        root['load_mc'].gotoAndPlay('none')
        loading = compose_root(insert_label, root['load_mc'], child)
        loading = describe_movie_clip(root, loading)
    return loading, child_list


def get_event_log(user, news, last_time):
    r'''Stamp login, interval, events, chat messages.  Update last_time.
    >>> jade = user_class()
    >>> jade.create(1)
    >>> jade.root.title_mc.username_txt.text = 'jade'
    >>> news = {'title_mc': {'start_btn': {'currentLabel': 'enter'}}}
    >>> last_time = time.time() - 1.125
    >>> log, last_time = get_event_log(jade, news, last_time)
    >>> log #doctest: +ELLIPSIS
    '>>> time.sleep(sloth * 1.12...)\n>>> # jade title_mc.start_btn ...'
    >>> if not time.time() - 0.002 <= last_time:
    ...     time.time(), last_time

    Or without timestamp.
    >>> news = {'chat_input_mc': {'currentLabel': 'none', 'dispatchEvent': 'mouseDown'}, 'chat_input_txt': {'text': 'hello'}}
    >>> last_time = None
    >>> log, last_time = get_event_log(jade, news, last_time)
    >>> log
    '>>> jade.root.chat_input_txt.text = "hello"\n>>> jade.root.chat_input_mc.dispatchEvent(mouseDown)'
    >>> if not time.time() - 0.002 <= last_time:
    ...     time.time(), last_time
    '''
    name = user.root.title_mc.username_txt.text
    context = '%s.%s' % (name, 'root')
    texts = ['chat_input_txt']
    logs = user_as.log_dispatchEvent(news, context, texts)
    # stamp interval
    now = time.time()
    if last_time:
        since = now - last_time
        if 0.000001 <= since:
            event_log = '>>> time.sleep(sloth * %f)' % since
            logs.append(event_log)
    title_mc = news.get('title_mc')
    if title_mc:
        start_btn = title_mc.get('start_btn')
        if start_btn:
            # stamp login
            now_text = time.asctime()
            event_log = '>>> # %s title_mc.start_btn %s' % (name, now_text)
            logs.append(event_log)
    return '\n'.join(logs), now


test_kyung_revert_schedule_current = \
{'attack_mc': {'currentLabel': 'show'},
 'connected_mc': {'currentLabel': 'show'},
 'critical_mc': {'currentLabel': 'show'},
 'currentLabel': 'table',
 'cursor_mc': {'act_mc': {'currentLabel': 'play'}, 'currentLabel': 'black'},
 'dead_mc': {'currentLabel': 'show'},
 'decoration_mc': {'currentLabel': 'show'},
 'defend_mc': {'currentLabel': 'show'},
 'extra_stone_mc': {'currentLabel': 'gift'},
 'game_over_mc': {'balance_mc': {'black_level_txt': {'text': '10'},
                                 'white_level_txt': {'text': '1'}},
                  'currentLabel': 'none',
                  'extra_stone_available_mc': {'currentLabel': '_0'},
                  'hide_available_mc': {'currentLabel': '_0'},
                  'start_mc': {'currentLabel': 'none'}},
 'gateway_mc': {'currentLabel': 'none'},
 'hide_mc': {'currentLabel': 'gift'},
 'liberty_mc': {'currentLabel': 'none'},
 'lobby_mc': {'create_mc': {'currentLabel': 'none'},
              'currentLabel': 'multiplayer',
              'join_mc': {'currentLabel': 'join',
                          'join_txt': {'text': 'moonhyoung'}},
              'main_mc': {'multiplayer_mc': {'currentLabel': 'none',
                                             }}},
#                                             'dispatchEvent': 'mouseDown'}}},
 'log_txt': {'text': 'imitate_news: kyung: gateway_mc:enter title_mc\nlog'},
 'option_mc': {'block_mc': {'currentLabel': 'show'},
               'computer_pass_mc': {'currentLabel': 'show'},
               'empty_block_mc': {'currentLabel': 'show'},
               'extra_stone_available_mc': {'currentLabel': '_0'},
               'first_capture_mc': {'currentLabel': 'none'},
               'gibs_mc': {'currentLabel': 'show'},
               'hide_available_mc': {'currentLabel': '_0'},
               'prohibit_danger_mc': {'currentLabel': 'none'},
               'score_mc': {'currentLabel': 'show'}},
 'profit_mc': {'currentLabel': 'show'},
 'score_mc': {'currentLabel': 'show'},
 'strike_mc': {'currentLabel': 'show'},
 'suicide_mc': {'currentLabel': 'show'},
 'territory_mc': {'currentLabel': 'show'},
 'title_mc': {'master_txt': {'text': 'master'},
              'password_txt': {'text': 'min'},
              'slave_txt': {'text': 'slave'},
              'time_txt': {'text': '53618'},
              'username_txt': {'text': 'kyung'}},
 'top_move_mc': {'currentLabel': 'show'},
 'turn_mc': {'black_user_txt': {'text': 'kyung'},
             'currentLabel': 'black',
             'white_user_txt': {'text': 'moonhyoung'}},
 'turn_veil_mc': {'currentLabel': 'you'},
 'unconditional_status_mc': {'currentLabel': 'show'}}
        

from remote_control import compose_root, insert_label
from lesson import update_path # on_problem_path
class go_club_class(object):
    '''Persistent information about players and games.'''
    def __init__(self, speed):
        self.users = setup_users(speed)
        self.child_list = []
        self.save_dict = {}
        self.is_alive = None
        self.gtp_envoy = go_text_protocol.setup_envoy(configuration.gtp_path, configuration.gtp_host, configuration.gtp_port)
        log_level = logging_levels[configuration.verbose]
        self.example_logger = setup_example_logger(level = log_level)
        self.log_time = None
        ## self.lag = configuration.simulate_lag
        ## self.lag = 1.0
        logging.info('go_club_class initialized')

    def __del__(self):
        logging.shutdown()

    def receive(self, protocol, news):
        '''Reply to unknown user a request for password.
        >>> go_club = go_club_class(1)
        >>> go_club.receive(client.echo_protocol_class(), {})
        {'gateway_mc': {'currentLabel': 'password'}}
       
        Do not reply to a comment.
        >>> comment_message = {'comment_mc': {'_txt': {'text': 'OOPS.'}, 'currentLabel': 'comment'}, 'title_mc': {'username_txt': {'text': 'lukasz'}, 'slave_txt': {'text': 'slave'}, 'password_txt': {'text': 'l'}, 'master_txt': {'text': 'master'}}}
        >>> go_club.receive(client.print_protocol_class(), comment_message)

        Do not reply to a close comment.
        >>> close_comment_message = {'comment_mc': {'currentLabel': 'none'}, 'title_mc': {'username_txt': {'text': 'lukasz'}, 'slave_txt': {'text': 'slave'}, 'password_txt': {'text': 'l'}, 'master_txt': {'text': 'master'}}}
        >>> go_club.receive(client.print_protocol_class(), close_comment_message)

        client logs in.  no state to load.  
        >>> lukasz_start_message = {'title_mc': {'username_txt': {'text': 'lukasz'}, 'password_txt': {'text': 'l'}, 'start_btn': {'dispatchEvent': 'mouseDown'}}}
        >>> go_club.receive(client.echo_protocol_class(), lukasz_start_message)

        client logs in.  server loads saved state.
        Might be a very large chunk of data!
        >>> go_club.users.get('lukasz').root.level_mc.currentLabel
        'up'

        Lukasz toggles score.  Server logs.
        >>> go_club_class.example_logger = setup_example_logger(level = logging.INFO)
        >>> lukasz_credentials = {'title_mc': {'username_txt': {'text': 'lukasz'}, 'password_txt': {'text': 'l'}}}
        >>> toggle_message = {'option_mc': {'score_mc': {'enter_mc': {'dispatchEvent': 'mouseDown'}}}}
        >>> news = upgrade(toggle_message, lukasz_credentials)
        >>> go_club.receive(client.echo_protocol_class(), news)
        >>> import text
        >>> example_log = text.load('example.log')
        >>> if not is_in_tail('example.log', 1000, '>>> lukasz.root.option_mc.score_mc.enter_mc.dispatchEvent(mouseDown)'):
        ...     print example_log[-1000:]
        
        Lukasz selects problem 1.  Server logs.
        >>> problem_message = {'lobby_mc': {'_00_mc': {'capture_3_3_mc': {'dispatchEvent': 'mouseDown'}}}}
        >>> news = upgrade(problem_message, lukasz_credentials)
        >>> go_club.receive(client.echo_protocol_class(), news)
        >>> import text
        >>> example_log = text.load('example.log')
        >>> if not is_in_tail('example.log', 1000, 'lukasz.root.lobby_mc._00_mc.capture_3_3_mc.dispatchEvent(mouseDown)'):
        ...     print example_log[-1000:]

        Revert preview.  restart_problem_example
        Update olds_list to enable reverting
        >>> jade_credentials = {'title_mc': {'username_txt': {'text': 'jade'}, 'password_txt': {'text': 'j'}}}
        >>> jade = go_club.users.get('jade')
        >>> ambassador = client.echo_protocol_class()
        >>> jade.root.currentLabel
        'login'
        >>> news = {'cursor_mc': {'act_mc': {'currentLabel': 'play'}}}
        >>> news = upgrade(news, jade_credentials)
        >>> go_club.receive(ambassador, news)
        >>> jade.root.currentLabel
        'login'
        >>> ambassador.sends[-1].get('currentLabel')
        >>> news = {'currentLabel': 'table', 'cursor_mc': {'act_mc': {'currentLabel': 'preview'}}}

        With credentials, Jade may revert.
        >>> news = upgrade(news, jade_credentials)
        >>> go_club.receive(ambassador, news)
        >>> jade.root.currentLabel
        'table'
        >>> ambassador.sends[-1].get('gateway_mc').get('currentLabel')
        'what_message'
        >>> ambassador.sends[-1].get('currentLabel')
        >>> news = {'menu_mc': {'toggle_mc': {'dispatchEvent': 'mouseDown'}}}
        >>> news = upgrade(news, jade_credentials)
        >>> go_club.receive(ambassador, news)
        >>> jade.root.currentLabel
        'login'
        >>> ambassador.sends[-1].get('currentLabel')
        'login'

        Client is immediately reverted before scheduling new events.
        see user_interface_example: moonhyoung_kyung_revert_schedule_example.
        TODO:  How can i simply expect reverted immediately before schedule?
        #>>> kyung = go_club.users.get('kyung')
        #>>> olds = imitate_news(kyung.root, test_kyung_revert_schedule_current)
        #>>> news = note(kyung.root._4_4_mc, 'dispatchEvent', 'mouseDown')
        #>>> news = upgrade(news, get_note(kyung.root.title_mc.username_txt, 'text'))
        #>>> news = upgrade(news, get_note(kyung.root.title_mc.password_txt, 'text'))
        #>>> go_club.receive(ambassador, news)
        #>>> ambassador.sends[-1]['_2_2_mc']['decoration_mc']['currentLabel']
        #'none'
        #>>> ambassador.sends[-1]['sequence'][-3]['_2_2_mc']['decoration_mc']['currentLabel']
        #'black_defend'
        #>>> from pprint import pprint
        #>>> pprint(ambassador.sends[-1]['sequence'])

        If pass, computer may move.  see user_pass_to_computer_example

        unrecognized dispatchEvent causes infinite loop of spam,
        so do not reply news.
        >>> bad_cursor_news = {'currentLabel': 'table', 'cursor': {'act_mc': {'currentLabel': 'preview'}}}
        >>> reply = go_club.receive(ambassador, bad_cursor_news)
        >>> ambassador.sends[-1].get('cursor')
        >>> ambassador.sends[-1].get('gateway_mc').get('currentLabel')
        'password'
        >>> bad_cursor_news = upgrade(bad_cursor_news, jade_credentials)
        >>> go_club.receive(ambassador, bad_cursor_news)
        >>> ambassador.sends[-1].get('cursor')
        >>> ambassador.sends[-1].get('gateway_mc').get('currentLabel')
        'what_message'

        To test internet conditions by mock lag, 
        set seconds as floating point.  
        lag / user._speed.  does not lag inauthentic messages.
        >>> configuration.simulate_lag = 8.0
        >>> import time
        >>> before = time.time()
        >>> go_club.receive(client.echo_protocol_class(), lukasz_start_message)
        >>> duration = time.time() - before
        >>> if not 1.0 <= duration:  duration
        '''
        user = authenticate_user(self.users, news)
        if not user:
            reply = {'gateway_mc':  {'currentLabel': 'password'}}
            #- reply = upgrade(news, reply)
            return protocol.send(reply)
            ## return reply
        #Not sure of usage, but may need lag again.
        if configuration.simulate_lag:
            from mock_client import mock_lag
            lag = mock_lag(configuration.simulate_lag, 
                    configuration.simulate_lag * 4)
            logging.info('simulate_lag %s' % lag)
            time.sleep(lag / configuration.mock_speed)
        user.news_ok = False
        user.ambassador = protocol
        event_log, self.log_time = get_event_log(user, news, self.log_time)
        self.example_logger.info(event_log)
        reverted = clear_preview(user)
        user.reverted = reverted
        user.revise(news)
        # XXX Since reverted, may only know request from news
        if 'stress' == user.root.gateway_mc.ready_time_txt.text:
            # XXX see client.stress_black
            return client.stress_black(user)
        elif 'echo' == user.root.gateway_mc.ready_time_txt.text:
            # XXX see client.echo
            return client.echo(user, news)
        elif 'echo_large' == user.root.gateway_mc.ready_time_txt.text:
            # XXX see client.echo
            return client.echo_large(user, news)
        title_obj = news.get('title_mc')
        if title_obj:
            start_btn_obj = title_obj.get('start_btn')
            if start_btn_obj:
                if user_as.MouseEvent.MOUSE_DOWN == start_btn_obj.get('dispatchEvent'):
                    name = user.root.title_mc.username_txt.text
                    file_name = 'user/%s.news.py' % name
                    import os
                    if not os.path.exists(file_name):
                        return # {'# TODO': True}
                    else:
                        logging.warn('loading %s' % file_name)
                        reply = load(file_name)
                        return user.publish(reply)
        save_mc = news.get('save_mc')
        if save_mc:
            if 'entering' == save_mc.get('currentLabel'):
                logging.info('save: %s' % news.keys())
                self.save_dict = upgrade(self.save_dict, news)
                reply = compose_root(insert_label, user.root['save_mc'])
                #- reply = upgrade(reverted, reply)
                time.sleep(1.0 / 16) # XXX sometimes a node is not saved.  why?
                return user.publish(reply)
            elif 'enter' == save_mc.get('currentLabel'):
                # XXX Fail to add new node or delete old one.
                self.save_dict = upgrade(self.save_dict, news)
                reply = save_stage(self.save_dict, save_file_name)
                #- reply = upgrade(reverted, reply)
                self.save_dict = {}
                return user.publish(reply)
        load_mc = news.get('load_mc')
        if load_mc:
            if 'entering' == load_mc.get('currentLabel'):
                if not self.child_list:
                    loaded = load(save_file_name)
                    # XXX is revise redundant with publish?
                    user.revise(loaded)
                    self.child_list = [user.root.getChildAt(c)
                                for c in range(user.root.numChildren)]
                reply, self.child_list = load_one_child(user.root, self.child_list)
                return user.publish(reply)
        gateway_mc = news.get('gateway_mc')
        if gateway_mc:
            if 'enter' == gateway_mc.get('currentLabel'):
                reply = enter(self.users, user)
                #- reply = upgrade(reverted, reply)
                return user.publish(reply)
        lobby_reply = may_use_lobby(self.users, user, news)
        if lobby_reply:
            #- reply = upgrade(reverted, lobby_reply)
            reply = lobby_reply
            return user.publish(reply)
        # --> user_class.problem
        #problem_reply = get_start_problem_news(self.users, user, news)
        #if problem_reply:
        #    reply = upgrade(reverted, problem_reply)
        #    return user.publish(reply)
        #turn_mc = news.get('turn_mc')
        #if turn_mc:
        #    white_mc = turn_mc.get('white_mc')
        #    if 'enter' == white_mc.get('currentLabel'):
        #        user_name = user.root.title_mc.username_txt.text
        #        reply = {'turn_mc': {
        #                    'currentLabel': 'white',
        #                    'white_mc': {'currentLabel': 'none'},
        #                    'white_user_txt': {'text':  user_name}
        #                    }
        #                }
        #        return user.publish(reply)
        game_over_dict = news.get('game_over_mc')
        if game_over_dict:
            start_dict = game_over_dict.get('start_mc')
            if start_dict:
                if 'enter' == start_dict.get('currentLabel'):
                    return start_game(self.users, user, self.example_logger)
            white_computer_dict = game_over_dict.get('white_computer_mc')
            if white_computer_dict:
                enter_dict = white_computer_dict.get('enter_mc')
                if 'enter' == enter_dict.get('currentLabel'):
                    reply = get_white_computer_news(user)
                    return user.publish(reply)
        resized = may_resize_board(self.users, user, news)
        if resized:
            return resized
        passed, pass_reply = may_pass_news(self.example_logger, 
                self.gtp_envoy, self.users, user, news)
        if passed:
            #- pass_reply = upgrade(reverted, pass_reply)
            user.publish(pass_reply)
            return pass_reply
        else:
            reply = pass_reply
        intersection_mc = get_first_intersection(
                user.intersection_mc_array, news)
        if intersection_mc:
            #     If client is corrupt, then revert.  see client.capture_example
            intersection_reply = iterate_intersection(
                    self.example_logger, self.gtp_envoy, 
                    self.users, user, intersection_mc, news)
            reply = upgrade(reply, intersection_reply)
            #- reply = upgrade(reverted, reply)
            user.publish(reply)
            logging.debug('after place_stone:\n' 
                    + flash_to_text(user.intersection_mc_array) )
            genmove_news = may_genmove_white(self.example_logger, 
                    self.gtp_envoy, self.users, user)
            if genmove_news:
                reply = upgrade(reply, genmove_news)
            return reply
        extra_stone_gift_mc = news.get('extra_stone_gift_mc')
        if extra_stone_gift_mc:
            mouse_log = write_mouse_down(user, 
                    user.root.extra_stone_gift_mc.use_mc)
            self.example_logger.info(mouse_log)
            reply = request_extra_stone(user, news)
            #use_mc = extra_stone_gift_mc.get('use_mc')
            #if 'enter' == use_mc.get('currentLabel'):
            #    reply = {'extra_stone_gift_mc': {'currentLabel': '_0',
            #                    'use_mc':  {'currentLabel': 'none'}},
            #                'cursor_mc':  {'extra_stone_mc': {'currentLabel': '_1'}}
            #        }
            #- reply = upgrade(reverted, reply)
            return user.publish(reply)
        hide_gift_mc = news.get('hide_gift_mc')
        if hide_gift_mc:
            # see hide_available_example
            mouse_log = write_mouse_down(user, 
                    user.root.hide_gift_mc.use_mc)
            self.example_logger.info(mouse_log)
            use_mc = hide_gift_mc.get('use_mc')
            if 'enter' == use_mc.get('currentLabel'):
                if '_1' == user.root.hide_gift_mc.currentLabel:
                    reply = {'hide_gift_mc': {'currentLabel': '_0',
                                    'use_mc':  {'currentLabel': 'none'}},
                                'cursor_mc':  {'currentLabel': 'hide_black'}
                        }
                    for row in user.intersection_mc_array:
                        for intersection_mc in row:
                            if 'empty_black' == intersection_mc.currentLabel:
                                reply[intersection_mc.name] = {
                                        'currentLabel': 'empty_hide_black'}
                else:
                    reply = {'help_mc': {'currentLabel': 'hide'}}
                #- reply = upgrade(reverted, reply)
                return user.publish(reply)
                
        ##- import pdb; pdb.set_trace();
        clock_object = news.get('clock_mc')
        if clock_object:
            reply, partner_reply = get_clock_news(self.users, user, 
                    clock_object)
            partner = get_partner(self.users, user)
            tell(partner, partner_reply)
            #- reply = upgrade(reverted, reply)
            return user.publish(reply)
        # XXX see lesson.py: beginner_comment_example
        comment_object = news.get('comment_mc')
        if comment_object:
            comment_currentLabel = comment_object.get('currentLabel')
            if comment_currentLabel:
                return
            comment_txt = comment_object.get('_txt')
            if comment_txt:
                comment_text = comment_txt.get('text')
                if comment_text:
                    return
        if user.news_ok:
            if reverted:
                logging.info('receive: news_ok, reverted: %s' % reverted)
                reply = {}
                return user.publish(reply)
        else:
            what_message = 'receive: what do i do with this message?  %s' \
                % news
            logging.error(what_message)
            reply = {'gateway_mc':  
                        {'currentLabel': 'what_message'}}
            # unrecognized dispatchEvent causes infinite loop of spam
            #- reply = upgrade(reply, news)
            #- reply = upgrade(reverted, reply)
            return user.publish(reply)




def receive_extra_stone_example():
    '''
    receive does clear_preview before preview or play or extra_stone.
    such that receive:  preview, extra_stone, preview, still has extra_stone.

    >>> import client; client = reload(client); from client import *
    >>> code_unit.inline_examples(
    ...     ethan_joris_start_example.__doc__, 
    ...     locals(), globals(), 
    ...     verify_examples = False)

    joris uses an extra stone.

    >>> mouse_down_and_sleep(joris, joris.root._2_2_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._2_2_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._6_2_mc, 1.0 / ethan._speed)
    >>> mouse_down_and_sleep(joris, joris.root.extra_stone_gift_mc.use_mc, 1.0 / joris._speed)
    >>> property_diff(joris, joris.root.cursor_mc.extra_stone_mc, 'currentLabel', '_1')

    joris previews.

    >>> mouse_down_and_sleep(joris, joris.root._0_1_mc, 1.0 / joris._speed)
    >>> property_diff(joris, joris.root.cursor_mc.extra_stone_mc, 'currentLabel', '_1')
    >>> property_diff(joris, joris.root._0_1_mc, 'currentLabel', 'question_black')
    >>> mouse_down_and_sleep(joris, joris.root._0_1_mc, 1.0 / joris._speed)
    >>> property_diff(joris, joris.root.cursor_mc.extra_stone_mc, 'currentLabel', '_0')
    >>> property_diff(joris, joris.root._0_1_mc, 'currentLabel', 'black')

    [see client.stress_black]
    '''
    
# Twisted networking and PyAMF encoding

import amf_socket_server
#- from configuration import *


class go_club_protocol_class(amf_socket_server.AmfSocketProtocol):
    def on_receive(self, message):
        '''may redirect to slave.'''
        slave = self.get_slave(message, self.factory.connections)
        if slave:
            #- slave.send(news)
            slave_log = 'go_club on_receive: %i slave=%i: %s' \
                    % (self.connection_serial, slave.connection_serial, message)
            logging.debug(slave_log)
            keywords = user_as.get_keywords(message)
            logging.info('master.send: %s' % keywords)
            amf_socket_server.AmfSocketProtocol.send(slave, message)
        else:
            no_slave_log = 'on_receive: %i no slave: %s' \
                    % (self.connection_serial, message)
            logging.debug(no_slave_log)
            ##- news = self.factory.application.receive(self, message)
            ##- self.send(news)
            self.factory.application.receive(self, message)
    def send(self, message):
        master = self.get_master(message, self.factory.connections)
        if master:
            #- super(go_club_protocol_class, master).send(message)
            master_log = 'go_club send: %i master=%i: %s' \
                    % (self.connection_serial, master.connection_serial, message)
            logging.debug(master_log)
            amf_socket_server.AmfSocketProtocol.send(master, message)
        else:
            no_master_log = 'send: %i no master: %s' \
                    % (self.connection_serial, message)
            logging.debug(no_master_log)
        amf_socket_server.AmfSocketProtocol.send(self, message)
    def get_slave(self, message, connections):
        '''Lookup conection in message.
        >>> message = {'title_mc':  {'slave_txt':  {'text':  '0'}, 'master_txt':  {'text':  '1'}}}
        >>> go_club_protocol = go_club_protocol_class()
        >>> go_club_protocol.get_slave(message, {0: 'connection0'})
        'connection0'

        Log error if not found in connections.
        >>> old_level = logging.getLogger().level
        >>> logging.getLogger().setLevel(logging.CRITICAL)
        >>> go_club_protocol.get_slave(message, {1: 'connection1'})
        >>> logging.getLogger().setLevel(old_level)
        '''
        title_mc = message.get('title_mc')
        if title_mc:
            slave_txt = title_mc.get('slave_txt')
            if slave_txt:
                if slave_txt.get('text').isdigit():
                    slave_serial = int(slave_txt.get('text'))
                    if self.connection_serial != slave_serial:
                        slave_connection = connections.get(slave_serial)
                        if not slave_connection:
                            logging.error('get_slave: slave_connection %i not found' % slave_serial)
                        return slave_connection
    def get_master(self, message, connections):
        '''Lookup conection in message.
        >>> message = {'title_mc':  {'slave_txt':  {'text':  '0'}, 'master_txt':  {'text':  '1'}}}
        >>> go_club_protocol = go_club_protocol_class()
        >>> go_club_protocol.get_master(message, {1: 'connection1'})
        'connection1'

        Log error if not found in connections.
        >>> old_level = logging.getLogger().level
        >>> logging.getLogger().setLevel(logging.CRITICAL)
        >>> go_club_protocol.get_slave(message, {1: 'connection1'})
        >>> logging.getLogger().setLevel(old_level)
        '''
        title_mc = message.get('title_mc')
        if title_mc:
            master_txt = title_mc.get('master_txt')
            if master_txt:
                if master_txt.get('text').isdigit():
                    master_serial = int(master_txt.get('text'))
                    if self.connection_serial != master_serial:
                        master_connection = connections.get(master_serial)
                        if not master_connection:
                            ## import pdb; pdb.set_trace();
                            logging.error('get_master: master_connection %i not found' % master_serial)
                        return master_connection

class go_club_factory_class(amf_socket_server.AmfSocketFactory):
    protocol = go_club_protocol_class
    application = None


def run_server(options):
    go_club_factory = go_club_factory_class(
        options.amf_host, options.amf_port, 
        options.policy_file, options.policy_port)
    go_club_factory.application = go_club_class(1)
    reactor = go_club_factory.setup()
    reactor.run()  # Infinite loop blocks execution

snippet = '''
# !start python code_explorer.py --import embassy.py --snippet snippet
import embassy; embassy = reload(embassy); from embassy import *
'''
# run_examples(shell, place_stone.__doc__)
# run_examples(shell, go_club_class.receive.__doc__)
# run_examples(shell, get_territory_news.__doc__)

import code_unit
def setup_server():
    go_club_factory = go_club_factory_class(
        configuration.amf_host, configuration.amf_port, 
        configuration.policy_file, configuration.policy_port)
    go_club_factory.application = go_club_class(1)
    reactor = go_club_factory.setup()
    # concurrently_run_reactor = code_unit.concurrently(reactor.run)
    # Infinite loop blocks execution
    # concurrently_run_reactor()
    return go_club_factory, reactor

import config
defaults = config.setup_defaults()
configuration = config.borg(defaults)

if __name__ == '__main__':
    import sys
    parser = config.default_parser(defaults)
    (options, args) = config.parse_args(parser, sys.argv)
    configuration.set(options.__dict__)
    config.setup_logging(configuration.verbose)

    log_level = logging_levels[options.verbose]
    logging.basicConfig(level=log_level)

    if options.unit:
        unit = eval(options.unit)
        code_unit.doctest_unit(unit)
    elif options.test:
        units = globals().values()
        code_unit.doctest_units(units)
    else:
        run_server(options)
    if options.wait:
        code_unit.wait(options.wait)




