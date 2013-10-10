#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Analyze board of Go for connections.
Captures
Hidden stone.
'''
__author__ = 'Ethan Kennerly'

from board import *


def dictionary_to_array(dictionary):
    '''
    >>> board = dictionary_to_array(array_to_dictionary(board_lines))
    >>> print doctest_board(board)
    ,,,,,,,,,
    ,OO,,,,,,
    OOOOO,,,,
    ,,OXXX,,,
    ,OX,XX,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    '''
    return get_board_union(clear_board,
            dictionary)


def is_color(mark, color):
    '''
    >>> is_color('.', 'black')
    False
    >>> is_color('/', 'black')
    True
    >>> is_color('X', 'black')
    True
    >>> is_color('X', 'white')
    False
    >>> is_color('O', 'white')
    True
    '''
    return mark in eval(color + '_characters')


def array_to_dictionary(array):
    '''
    >>> array_to_dictionary(clear_board)
    {}
    >>> board = dictionary_to_array(array_to_dictionary(board_lines))
    >>> print doctest_board(board)
    ,,,,,,,,,
    ,OO,,,,,,
    OOOOO,,,,
    ,,OXXX,,,
    ,OX,XX,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    '''
    dictionary = {}
    for row in range(len(array)):
        for column in range(len(array[row])):
            for color in 'black', 'white':
                if is_color(array[row][column], color):
                    draw(dictionary, color, (row, column))
    return dictionary


def prepend(some_text, p='[ '):
    '''Safe to print ... in doctest.
    >>> print prepend(lines_to_text(board_lines))
    [ ,,,,,,,,,
    [ ,OO,,,,,,
    [ OOOOO,,,,
    [ ,,OXXX,,,
    [ ,OX,XX,,,
    [ ,,,,,,,,,
    [ ,,,,,,,,,
    [ ,,,,,,,,,
    [ ,,,,,,,,,
    '''
    mutant = copy.deepcopy(some_text)
    mutant = mutant.replace('\n', '\n' + p)
    mutant = p + mutant
    return mutant




#no example
#def same_or_empty(me, you):
#    return same(me, you) or is_empty(me)
#def different_or_empty(me, you):
#    return is_empty(me) or \
#        different_color(me, you)




def find_attacker_liberty(board, row, column):
    '''Liberties of groups attacking a position.
    In form of [(group0, liberty0), ...]
    >>> find_attacker_liberty(clear_board, 1, 1)
    []
    >>> find_attacker_liberty(liberty_board, 2, 1)
    [([(2, 2), (2, 3)], [(1, 3), (2, 4), (3, 3)])]
    >>> find_attacker_liberty(liberty_board, 6, 5)
    [([(5, 3), (5, 4), (6, 4), (7, 4)], [(4, 4), (5, 5), (8, 4)])]
    >>> find_attacker_liberty(individual_liberty_board, 2, 1)
    [([(2, 2)], [(2, 3)])]
    '''
    group_liberties = []
    for r, c in find_attacker(board, row, column):
        attacker_group = find_region(board, r, c)
        attacker_liberty = find_liberty(board, r, c)
        group_liberties.append( (attacker_group, attacker_liberty) )
    return group_liberties


def get_attacker_in_danger(board, row, column):
    r'''Attackers with one liberty left, aka atari or dansu.
    >>> get_attacker_in_danger(individual_liberty_board, 2, 1)
    [(2, 2)]
    '''
    attackers_liberties = find_attacker_liberty(board, row, column)
    for attacker, liberty in attackers_liberties:
        if len(liberty) == 1:
            return attacker


def to_positions(positions):
    '''Format as a list of tuples.
    >>> to_positions([[0, 1]])
    [(0, 1)]
    >>> to_positions(['pass'])
    ['pass']
    '''
    if 'pass' in positions or 'resign' in positions:
        return positions
    return [tuple(position) for position in positions]


def dictionary_to_positions(client_request):
    '''Dictionary with list of lists to list of tuples.
    ActionScript returns Array which PyAMF converts to list,
    but referee likes tuples, so convert [2, 3] to (2, 3).
    >>> code_unit.print_diff( 
    ...     dictionary_to_positions(
    ...     {'black': [[2, 3]], 'clear_board':  True}),
    ...     {'black': [(2, 3)], 'clear_board':  True}    )
    '''
    request = copy.deepcopy(client_request)
    for key in 'black', 'white', 'empty':
        if client_request.has_key(key):
            request[key] = to_positions(client_request[key])
    return request


def pair(flat_list):
    '''ActionScript had used flat lists.  DEPRECATE.
    >>> pair([3, 4, 6, 7])
    [(3, 4), (6, 7)]
    '''
    nested = []
    for o in range(0, len(flat_list), 2):
        nested.append((flat_list[o], flat_list[o+1]))
    return nested



def pair_coordinates(indexes, row_length):
    '''
    >>> pair_coordinates([1, 21], 9)
    [(0, 1), (2, 3)]
    >>> pair_coordinates([], 9)
    []
    '''
    return [(index / row_length, index % row_length) 
        for index in indexes]
    

def flatten_coordinates(pairs, row_length):
    '''
    >>> flatten_coordinates([(0, 1), (2, 3)], 9)
    [1, 21]
    >>> flatten_coordinates([], 9)
    []
    '''
    return [row * row_length + column 
        for row, column in pairs]


def change_attacker_in_danger(board, news):
    ''' DEPRECATE.  Not needed?  positions in danger.
    >>> news = {'black': [(2, 1)]}
    >>> change_attacker_in_danger(individual_liberty_board, news)
    [(2, 2)]
    >>> news = {'white': [(7, 7)]}
    >>> change_attacker_in_danger(individual_liberty_board, news)
    [(7, 6)]
    '''
    attackers_in_danger = []
    for change_key in 'black', 'white':
        changes = news.get(change_key, [])
        for r, c in changes:
            in_danger = get_attacker_in_danger(board, r, c)
            if in_danger:
                attackers_in_danger.extend(in_danger)
    return attackers_in_danger


def get_remove_add_list(previous_stone_list, stone_list):
    '''
    >>> get_remove_add_list(['C6', 'C4'], ['F7', 'C6', 'C4'])
    ([], ['F7'])
    >>> get_remove_add_list([(2, 1)], [(1, 2), (2, 1)])
    ([], [(1, 2)])
    '''
    add_stone_list = [stone for stone in stone_list
        if stone not in previous_stone_list]
    remove_stone_list = [stone for stone in previous_stone_list
        if stone not in stone_list]
    if '' in add_stone_list:
        print 'get_remove_add_list:  I cannot digest an empty string' + add_stone_list
        ## 
    return remove_stone_list, add_stone_list


def get_stone_list(gtp_response, color):
    stone_list = gtp_response_to_list(gtp_response)
    return stone_list


def list_stones(gtp_command, gtp_response, stone_dictionary):
    r'''
    >>> list_stones('list_stones black', '= \n\n', {})
    {}
    >>> list_stones('list_stones white', '= F2\n\n', {})
    {'white': [(7, 5)]}
    >>> list_stones('list_stones white', '= \n\n', {'white': [(7, 5)]})
    {}

    If timeout, then do not update.
    >>> list_stones('list_stones white', 'timeout', {'white': [(7, 5)]})
    {'white': [(7, 5)]}
    '''
    if 'timeout' == gtp_response:
        return stone_dictionary
    if gtp_command.endswith('black'):
        stone_list = get_stone_list(gtp_response, 'black')
        position_list = [gtp_to_array(stone) 
                for stone in stone_list]
        stone_dictionary['black'] = []
        stone_dictionary = draw(stone_dictionary, 'black',
                *position_list)
        stone_dictionary = discard(stone_dictionary, 'black')
    elif gtp_command.endswith('white'):
        stone_list = get_stone_list(gtp_response, 'white')
        position_list = [gtp_to_array(stone) 
                for stone in stone_list]
        stone_dictionary['white'] = []
        stone_dictionary = draw(stone_dictionary, 'white',
                *position_list)
        stone_dictionary = discard(stone_dictionary, 'white')
    return stone_dictionary



from deck import *

def already_at(stones, play_request):
    '''
    >>> already_at({'black': [(0, 0)]}, {'black': [(1, 0)]})
    []
    >>> already_at({'white': [(1, 0)]}, {'black': [(1, 0)]})
    [(1, 0)]
    '''
    redundancies = []
    for color in 'black', 'white':
        for position in play_request.get(color, []):
            for color in 'black', 'white':
                if position in stones.get(color, []):
                    redundancies.append(position)
    return redundancies

def new_world():
    '''New dictionary deepcopy of default values.'''
    return {'game_over':  'none',
            'turn':  'none',
            'glass':  'none',
            'clear_board':  'none'}

def notify_world(world, user):
    '''
    >>> user = {'news': {}, 'world': {'root': 'lobby', 'turn':  'white', 'clear_board': True}}
    >>> world = {'turn': 'black', 'root': 'table', 'clear_board': True}
    >>> user = notify_world(world, user)
    >>> if not user.get('news') == {'turn': 'black', 'root': 'table'}:  user.get('news')
    >>> if not user.get('world') == {'turn': 'black', 'root': 'table', 'clear_board': True}:  user.get('world')
    '''
    ## print 'notify_world start: world %s, user %s, news %s' % (world, user, news)
    for key, value in world.items():
        if user.get('world').get(key) != world.get(key):
            user['news'].update({key:  value})
            ## print 'notify_world:  news.update({%s:  %s})' \
            ##        % (key, value)
    user.get('world').update(world)
    ## print 'notify_world end: world %s, user %s, news %s' % (world, user, news)
    return user


def notify_user(gateway_users, user, news):
    '''Remove news without breaking reference.
    >>> users = {'a': {'news': {'n': 1}}}
    >>> news = users['a']['news']
    >>> notify_user(users, 'a', {})
    {'n': 1}
    >>> users
    {'a': {'news': {}}}
    >>> news
    {}
    >>> if not news is users['a']['news']:  
    ...     news, users['news']
    '''
    user_data = gateway_users.get(user)
    if not user_data:
        print gateway_users
    your_news = user_data.get('news')
    if your_news:
        news.update(your_news)
        user_data['news'].clear()
    return news


def clear_dictionary_example():
    '''Clear preserves multiple references to the dictionary.
    >>> d = {}
    >>> e = d
    >>> d['a'] = 0
    >>> d
    {'a': 0}
    >>> e
    {'a': 0}
    >>> d.clear()
    >>> d
    {}
    >>> e
    {}
    >>> d = {}
    >>> d['a'] = 0
    >>> e
    {}
    >>> d
    {'a': 0}
    >>> e = d
    >>> e
    {'a': 0}
    >>> d.clear()
    >>> e
    {}
    >>> d
    {}
    '''


def notify_stone(previous_stone_dictionary, 
        stone_dictionary, old_news):
    r'''Get stones to remove and add.
    >>> new = {'black': [(3, 2)]}
    >>> previous, news = notify_stone({}, new, {})
    >>> news
    {'black': [(3, 2)]}

    Captures are 'empty'
    >>> previous, news = notify_stone({'white': [(4, 3), (4, 2)]}, {'white': [(4, 3)]}, {})
    >>> news
    {'empty': [(4, 2)]}
    >>> previous, news = notify_stone({'white': [(4, 3), (4, 2)]}, {'white': [(4, 3)]}, {'genmove': 'white'})
    >>> code_unit.print_diff(news, {'genmove': 'white', 'empty': [(4, 2)]} )
    >>> old = {'white': [(7, 5)]}
    >>> new = {'white': [(7, 5)], 'black': [(7, 2)]}
    >>> previous, news = notify_stone(old, new, {'genmove': 'white', 'turn': 'white'})
    >>> code_unit.print_diff( news, {'black': [(7, 2)], 'genmove': 'white', 'turn': 'white'} )
    >>> code_unit.print_diff(previous, {'white': [(7, 5)], 'black': [(7, 2)]} )
    '''
    news = old_news
    if 'empty' in news.keys():
        news['empty'] = []
    for color in 'black', 'white':
        ## print 'news:  ' + color + str(stone_list)
        removes, adds = get_remove_add_list(
                previous_stone_dictionary.get(color, []), 
                stone_dictionary.get(color, []))
        if removes:
            if 'empty' not in news.keys():
                news['empty'] = []
            for coordinate in removes:
                news['empty'].append(coordinate)
        if adds:
            ## print adds
            news[color] = []
            for coordinate in adds:
                news[color].append(coordinate)
        # XXX:  This overlooks case in which coordinate is in both colors.
    return copy.deepcopy(stone_dictionary), news


def notify_danger(board, previous_danger, 
        previous_warning, news):
    '''new danger.  old danger that has stopped.
    >>> previous_danger, previous_warning, news = notify_danger(individual_liberty_board, [(2, 2)], [], {'black': [(2, 1)]})
    >>> code_unit.print_diff(news, {'black': [(2, 1)], 'warning': [(0, 8), (8, 0), (8, 6)], 'danger': [(7, 6)]} )
    >>> previous_danger
    [(2, 2), (7, 6)]
    >>> previous_warning
    [(0, 8), (8, 0), (8, 6)]
    >>> previous_danger, previous_warning, news = notify_danger(individual_liberty_board, [(2, 1), (2, 2)], [], {'black': [(2, 1)]})
    >>> code_unit.print_diff(news, {'danger end': [(2, 1)], 'black': [(2, 1)], 'warning': [(0, 8), (8, 0), (8, 6)], 'danger': [(7, 6)]} )

    If in danger, nevermind saying that warning ended.
    If in warning, nevermind saying that danger ended.
    >>> previous_danger = [(2, 1), (2, 2), (0, 8)]
    >>> previous_warning = [(2, 2), (7, 6)]
    >>> previous_danger, previous_warning, news = notify_danger(individual_liberty_board, previous_danger, previous_warning, {'black': [(2, 1)]})
    >>> code_unit.print_diff(news, {'danger end': [(2, 1)], 'black': [(2, 1)], 'warning': [(0, 8), (8, 0), (8, 6)], 'danger': [(7, 6)]} )
    '''
    danger = find_danger(board)
    danger_removes, danger_adds = get_remove_add_list(previous_danger, danger)
    warning = find_warning(board)
    warning_removes, warning_adds = get_remove_add_list(previous_warning, warning)
    if danger_adds:
        news['danger'] = danger_adds
    if warning_adds:
        news['warning'] = warning_adds
    if danger_removes:
        danger_safe_list = []
        for safe in danger_removes:
            if safe not in warning:
                danger_safe_list.append(safe)
        if danger_safe_list:
            news['danger end'] = danger_safe_list
    if warning_removes:
        warning_safe_list = []
        for safe in warning_removes:
            if safe not in danger:
                warning_safe_list.append(safe)
        if warning_safe_list:
            news['warning end'] = warning_safe_list
    return danger, warning, news




hide_suicide_board_text = '''
,X,,XOOO,
X,,,XO,OX
,,,,XOOXX
XX,,XXOXX
OXXXXOXXX
OOOXX,XXX
,,,OO/OOX
XO,,,,,OO
O,O,,,,,,
'''
hide_suicide_board = text_to_array(hide_suicide_board_text)



# Hide


def play_to_color(play_color):
    '''Convert 'play black' to 'black'.
    >>> play_to_color('play black')
    'black'
    >>> play_to_color('play white')
    'white'
    >>> play_to_color('white')
    'white'
    '''
    return play_color.strip('play ')


def get_board_union(board, *stones):
    r'''Merge board and non-hidden stone coordinates.
    >>> same = get_board_union(enclosed_empty_region_board, {})
    >>> if not enclosed_empty_region_board == same:
    ...     print doctest_board(same)
    >>> union = get_board_union(enclosed_empty_region_board, 
    ...     {'black': [(8, 3)]})
    >>> print doctest_board(union)
    ,,,,,,,,,
    ,,,,,,,,,
    ,,XX,XX,,
    ,,,,,,,,,
    ,,,XX,,,,
    ,,X,O,X,,
    ,,X,O,X,,
    ,,,O,O,,,
    ,,,XO,,,,
    >>> same = get_board_union(enclosed_empty_region_board, 
    ...     {'black': [(4, 3)]})
    >>> if not enclosed_empty_region_board == same:
    ...     print doctest_board(same)
    >>> all_three = get_board_union(enclosed_empty_region_board, 
    ...     {'black': [(8, 8)]}, {'black': [(0, 8)]})
    >>> print all_three[0][8]
    X
    >>> print all_three[8][8]
    X
    >>> ignore_non_colors = get_board_union(enclosed_empty_region_board, 
    ...     {'black': [(8, 8)]}, {'showboard': True})
    >>> print ignore_non_colors[8][8]
    X
    >>> pb(get_board_union(not_capture_board, {'black': [(0, 1)]}))
    O/,,,,,,,
    O/,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    '''
    united = copy.deepcopy(board)
    for stone in stones:
        for color in 'black', 'white':
            if stone.has_key(color) and stone.get(color):
                for row, column in stone[color]:
                    if not is_color(united[row][column], color):
                        #print 'get_board_union: %s already at (%i, %i): %s' \
                        #        % (color, row, column, united[row][column])
                        united[row][column] = eval(color)
    return united


gnugo_black_assassin_text = '''
,,,,,,,,,
,,,,,,,,,
,,XX,XX,,
,,,,,,,,,
,,,XX,,,,
,,X,O,X,,
,,XXO,X,,
,,XO,O,,,
,,,,O,,,,
'''

gnugo_black_assassin_board = text_to_array(
        gnugo_black_assassin_text)

assassin_board_text = '''
,,,,,,,,,
,,,,,,,,,
,,XX,XX,,
,,,,,,,,,
,,,XX,,,,
,,X,O,X,,
,,XXO,X,,
,,XO,O,,,
,,,/O,,,,
'''
assassin_board = text_to_array(
        assassin_board_text)

ko_board_text = '''
,,,,,,,,,
,,,,,,,,,
,,XX,XX,,
,,,,,,,,,
,,,XX,,,,
,,X,O,X,,
,,XXO,X,,
,,XO,O,,,
,,,XO,,,,
'''
ko_board = text_to_array(
        ko_board_text)



def find_black_assassins(board, hidden, last_move):
    r'''Return the coordinates of hidden black stones that capture.
    >>> find_black_assassins(enclosed_empty_region_board, {'black': [(8, 3)]}, (6, 3))
    []
    >>> find_black_assassins(black_assassin_board, {'black': [(8, 3)]}, (6, 3))
    [(8, 3)]
    >>> find_black_assassins(black_assassin_board, {}, (6, 3))
    []
    >>> find_black_assassins(black_assassin_board, {'black': [(6, 2)]}, (6, 3))
    []
    >>> find_black_assassins(black_assassin_board, {'black': [(6, 2), (7, 2), (8, 3)]}, (6, 3))
    [(7, 2), (8, 3)]

    Return assassins that were killed.
    >>> find_black_assassins(black_assassin_board, {'black': [(6, 2), (7, 4), (8, 3)]}, (7, 3))
    [(7, 4)]

    Merge board first.
    >>> before = gnugo_black_assassin_board
    >>> hidden = {'black': [(8, 3)]}
    >>> client_request = {'black':  [(7, 4)]}
    >>> color, move = get_first_move(client_request)
    >>> board = get_board_union(before,
    ...         hidden, client_request)
    >>> find_black_assassins(
    ...         board, hidden, move)
    [(8, 3)]
    '''
    # find stones that capture the group
    assassins = []
    captured = find_capture(board, last_move)
    for position in captured:
        attackers = find_attacker(board, *position)
        # which are hidden
        for attacker in attackers:
            if attacker in hidden.get('black', []):
                assassins.append(attacker)
        # or assassins that were captured
        if position in hidden.get('black', []):
            assassins.append(position)
    return assassins


def foresee_black_assassins(board, mark, row, column):
    '''must reveal before capture and update_board.
    >>> board = assassin_board
    >>> next_board, assassins = foresee_black_assassins(board, 'X', 7, 4)
    >>> pb(next_board)
    ,,,,,,,,,
    ,,,,,,,,,
    ,,XX,XX,,
    ,,,,,,,,,
    ,,,XX,,,,
    ,,X,O,X,,
    ,,XXO,X,,
    ,,XOXO,,,
    ,,,XO,,,,
    >>> assassins
    [(8, 3)]
    >>> board = assassin_board
    >>> next_board, assassins = foresee_black_assassins(board, '[', 7, 4)
    >>> pb(next_board)
    ,,,,,,,,,
    ,,,,,,,,,
    ,,XX,XX,,
    ,,,,,,,,,
    ,,,XX,,,,
    ,,X,O,X,,
    ,,XXO,X,,
    ,,XOXO,,,
    ,,,XO,,,,
    >>> assassins
    [(7, 4), (8, 3)]
    >>> board = ko_board
    >>> next_board, assassins = foresee_black_assassins(board, '/', 7, 4)
    >>> pb(next_board)
    ,,,,,,,,,
    ,,,,,,,,,
    ,,XX,XX,,
    ,,,,,,,,,
    ,,,XX,,,,
    ,,X,O,X,,
    ,,XXO,X,,
    ,,XOXO,,,
    ,,,XO,,,,
    >>> assassins
    [(7, 4)]
    >>> next_board, assassins = foresee_black_assassins(board, '/', 7, 1)
    >>> pb(next_board)
    ,,,,,,,,,
    ,,,,,,,,,
    ,,XX,XX,,
    ,,,,,,,,,
    ,,,XX,,,,
    ,,X,O,X,,
    ,,XXO,X,,
    ,/XO,O,,,
    ,,,XO,,,,
    >>> assassins
    []
    '''
    if not is_black(mark) and not is_white(mark):
        print 'foresee_black_assassins(', mark, '...) # is not black or white'
    next_board = copy.deepcopy(board)
    next_board[row][column] = mark
    hidden = array_to_hidden(next_board)
    assassins = find_black_assassins(
            next_board, hidden, (row, column))
    if assassins:
        for row, column in assassins:
            next_board[row][column] = black
    return next_board, assassins


def insert_stones(add_dictionary, stones):
    '''Place one new stone.
    >>> insert_stones({'black':  [(7, 2)]}, {})
    {'black': [(7, 2)]}
    >>> stones = insert_stones({'black':  [(8, 3)]}, {'black':  [(7, 2)]})
    >>> if not stones == {'black': [(7, 2), (8, 3)]}:
    ...     print stones
    >>> stones = insert_stones({'white':  [(8, 3)]}, {'white':  [(7, 2)]})
    >>> if not stones == {'white': [(7, 2), (8, 3)]}:
    ...     print stones
    '''
    for color, positions in add_dictionary.items():
        for position in positions:
            if stones.get(color):
                stones[color].append(position)
            else:
                stones[color] = [position]
    return stones


def remove_stones(stones, subtract_dictionary, warn = True):
    '''Take away a stone.
    >>> remove_stones({'black':  [(7, 2)]}, {})
    {'black': [(7, 2)]}

    By default, warn if missing,
    >>> stones = remove_stones({'black':  [(7, 2)]}, {'black':  [(8, 3)]})
    remove_stones:  no such stone 'black' (8, 3) in {'black': [(7, 2)]}
    >>> stones = remove_stones({'black':  [(7, 2)]}, {'black':  [(8, 3)]}, warn = False)
    >>> remove_stones({'black':  [(8, 3)]}, {'black':  [(8, 3)]})
    {}
    >>> remove_stones({'white':  [(8, 3)]}, {'white':  [(8, 3)]})
    {}
    >>> remove_stones({'white':  [(7, 1), (8, 3)]}, {'white':  [(8, 3)]})
    {'white': [(7, 1)]}
    '''
    for color, positions in subtract_dictionary.items():
        for position in positions:
            if stones.get(color) \
                    and position in stones.get(color):
                stones = discard(stones, color, position)
            elif warn:
                print "remove_stones:  no such stone '%s' %s in %s" \
                        % (color, position, stones)
    return stones



def simple_board(board):
    '''X and O.  Black and White.
    >>> start_ko_board[1][0] = '*'
    >>> pb(simple_board(start_ko_board))
    ,X,X,,,,,
    XOX,,,,,,
    O,O,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,XX
    '''
    blacks = get_positions(board, is_black)
    board = map_at_position(mark_black, board, blacks)
    whites = get_positions(board, is_white)
    board = map_at_position(mark_white, board, whites)
    return board


def simple_board_is_same(a_board, b_board):
    '''Black and white version of board is same.
    >>> alternate_ko_board = copy.deepcopy(start_ko_board)
    >>> start_ko_board[1][0] = '*'
    >>> simple_board_is_same(start_ko_board, alternate_ko_board)
    True
    >>> start_ko_board[1][0] = '/'
    >>> simple_board_is_same(start_ko_board, alternate_ko_board)
    True
    >>> start_ko_board[1][0] = '@'
    >>> simple_board_is_same(start_ko_board, alternate_ko_board)
    False
    '''
    a_simple_board = simple_board(a_board)
    b_simple_board = simple_board(b_board)
    return a_simple_board == b_simple_board

def is_repeat(previous_board, board, color, row, column):
    '''ko:  play and update would equal previous board.
    >>> is_repeat(before_ko_board, start_ko_board, 'black', 0, 0)
    False
    >>> is_repeat(before_ko_board, start_ko_board, 'white', 0, 0)
    True
    >>> is_repeat(before_ko_board, start_ko_board, 'white', 0, 1)
    False
    >>> start_ko_board[1][0] = white
    >>> is_repeat(before_ko_board, start_ko_board, 'white', 0, 0)
    False

    Hm, capturing hidden not allowed?
    >>> start_ko_board[1][0] = black_hidden
    >>> is_repeat(before_ko_board, start_ko_board, 'white', 0, 0)
    True
    >>> before_ko_board[1][0] = black_hidden
    >>> is_repeat(before_ko_board, start_ko_board, 'white', 0, 0)
    False
    >>> before_ko_board[1][0] = empty

    May respond to alternate marks for black.
    >>> start_ko_board[1][0] = black
    >>> before_ko_board[0][0] = play_white
    >>> if not is_repeat(before_ko_board, start_ko_board, 'white', 0, 0):
    ...     pb(start_ko_board)
    ...     pb(before_ko_board)

    XXX How fast is this function on 9x9?
    '''
    next_board = play_and_update(board, color, row, column)
    if simple_board_is_same(next_board, previous_board):
        return True
    return False

def find_repeats(previous_board, board, color):
    '''Which positions would cause board to repeat previous?
    >>> find_repeats(before_ko_board, start_ko_board, 'black')
    []
    >>> find_repeats(before_ko_board, start_ko_board, 'white')
    [(0, 0)]

    XXX How fast is this function on 9x9?
    '''
    repeats = []
    for r, row in enumerate(board):
        for c, mark in enumerate(row):
            if is_repeat(previous_board, board, color, r, c):
                coordinate = (r, c)
                repeats.append(coordinate)
    return repeats

def get_first_move(add_dictionary):
    '''First move from dictionary.  Does not distinguish color.
    >>> get_first_move({'black':  [(7, 2)]})
    ('black', (7, 2))
    >>> get_first_move({'black':  [(8, 3)]})
    ('black', (8, 3))
    >>> get_first_move({'white':  [(8, 3)]})
    ('white', (8, 3))
    >>> get_first_move({'showboard':  True, 'white':  [(8, 3)]})
    ('white', (8, 3))
    >>> get_first_move({'showboard':  True})
    >>> get_first_move({'black': ['pass']})
    ('black', 'pass')
    '''
    for color in 'black', 'white':
        if color in add_dictionary:
            positions = add_dictionary.get(color)
            return color, positions[0]

    

def get_last_move(moves):
    '''
    >>> get_last_move([])
    >>> get_last_move([(4, 3)])
    (4, 3)
    >>> get_last_move([(4, 3), (5, 1)])
    (5, 1)
    '''
    if moves:
        return moves[-1]


def notify_hidden(previous_hidden, hidden, old_news):
    r'''Reveal no longer hidden.  Hide newly hidden.
    >>> previous_hidden, news = notify_hidden(
    ...     {'black': [(2, 1)]}, {'black': [(2, 1)]}, {})
    >>> news
    {}
    >>> previous_hidden, news = notify_hidden(
    ...     {'black': [(1, 1), (2, 1)]}, {'black': [(2, 1)]}, {})
    >>> news
    {'unhide': [(1, 1)]}
    >>> previous_hidden, news = notify_hidden(
    ...     {'black': [(2, 1)]}, {'black': [(1, 3), (2, 1)]}, {})
    >>> news
    {'hide': [(1, 3)]}
    '''
    news = old_news
    for color in 'black', 'white':
        ## print 'news:  ', news
        removes, adds = get_remove_add_list(
                previous_hidden.get(color, []), 
                hidden.get(color, []))
        if removes:
            if 'unhide' not in news.keys():
                news['unhide'] = []
            for coordinate in removes:
                news['unhide'].append(coordinate)
        if adds:
            ## print adds
            if 'hide' not in news.keys():
                news['hide'] = []
            for coordinate in adds:
                news['hide'].append(coordinate)
        # XXX:  This overlooks case in which coordinate is in both colors.
    return copy.deepcopy(hidden), news






def hid_black_here_dictionary(hidden, play_dictionary):
    r'''Did black hide a stone here?
    >>> hid_black_here_dictionary( {}, {'black': [(4, 3)]} )
    >>> hid_black_here_dictionary({'black': [(4, 3)]}, 
    ...     {'black': [(4, 3)]} )
    {'hide': [(4, 3)]}
    >>> hid_black_here_dictionary({'black': [(5, 1), (4, 3)]}, 
    ...     {'black': [(4, 3)]} )
    {'hide': [(4, 3)]}
    '''
    hid = {}
    if 'black' in play_dictionary:
        positions = play_dictionary['black']
        for position in positions:
            if 2 != len(position):
                print '''play only valid for position with 
                    two coordinates not %s''' % position
            hidden_list = hidden.get('black', [])
            if position in hidden_list:
                if hid.get('hide'):
                    hid['hide'].append(position)
                else:
                    hid['hide'] = [position]
        if hid:
            return hid


def get_collision_with_black(hidden, gtp_response):
    r'''
    >>> get_collision_with_black(
    ...     {'black': [(5, 2)]}, '= C4\n\n')
    (5, 2)
    >>> get_collision_with_black(
    ...     {'black': [(2, 3)]}, '= D2\n\n')
    '''
    row, column = gtp_response_to_coordinate(gtp_response)
    hidden_list = hidden.get('black', [])
    collision = (row, column) in hidden_list
    if collision:
        return (row, column)


def notify_unhide_collision(hidden, gtp_response, news):
    r'''Notify a collision with hidden stone occurred.
    >>> notify_unhide_collision( 
    ...     {'black': [(7, 2)]}, '= C4\n\n', {})
    {}
    >>> news = notify_unhide_collision( 
    ...     {'black': [(7, 2)]}, '= C2\n\n', {})
    >>> code_unit.print_diff(news, {'genmove': 'white', 'unhide': [(7, 2)]} )
    '''
    unhide_list = []
    collision = get_collision_with_black(
            hidden, gtp_response)
    if collision:
        hidden['black'].remove(collision)
        unhide_list.append(collision)
    if unhide_list:
        news['unhide'] = unhide_list
        news['genmove'] = 'white'
    return news

hidden_board_text = '''
,,,,,,,,,
,OXX,,,,,
,/OOX,X,,
,OX,X,,,,
,,,,,,,,,
,,O,O,O,,
,,,,,,,,,
,,,,,,,,,
,,,,,,,,,
'''
hidden_board = text_to_array(hidden_board_text)

play_hide_black_board_text = '''
,,,,,,,,,
,OXX,,,,,
,|OOX,X,,
,OX,X,,,,
,,,,,,,,,
,,O,O,O,,
,,,,,,,,,
,,,,,,,,,
,,,,,,,,,
'''
play_hide_black_board = text_to_array(play_hide_black_board_text)

def is_black_hidden(mark):
    '''
    >>> is_black_hidden('[')
    True
    >>> is_black_hidden('X')
    False
    >>> is_black_hidden(']')
    True
    >>> is_black_hidden('*')
    False
    >>> is_black_hidden('')
    False
    >>> is_black_hidden('|')
    True
    >>> is_black_hidden(play_hide_black_board[2][1])
    True
    '''
    return len(mark) == 1 \
            and mark in black_hidden_characters \
            and mark != ''



def array_to_hidden(board):
    '''
    >>> array_to_hidden(hidden_board)
    {'black': [(2, 1)]}
    >>> array_to_hidden(not_capture_board)
    {'black': [(0, 1), (1, 1)]}
    '''
    hidden = {}
    positions = get_positions(board, is_black_hidden)
    if positions:
        hidden['black'] = positions
    return hidden

def text_to_stone_hidden(board_text):
    r"""Convert player's text to stone and hidden dictionaries.
    >>> stones, hidden = text_to_stone_hidden(hidden_board_text)
    >>> code_unit.print_diff( stones, {'white': [(1, 1), (2, 2), (2, 3), (3, 1), (5, 2), (5, 4), (5, 6)], 'black': [(1, 2), (1, 3), (2, 1), (2, 4), (2, 6), (3, 2), (3, 4)]} )
    >>> hidden
    {'black': [(2, 1)]}
    >>> print doctest_board(dictionary_to_array(stones))
    ,,,,,,,,,
    ,OXX,,,,,
    ,XOOX,X,,
    ,OX,X,,,,
    ,,,,,,,,,
    ,,O,O,O,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    """
    board = text_to_array(board_text)
    stones = array_to_dictionary(board)
    hidden = array_to_hidden(board)
    return stones, hidden


def stone_hidden_to_text(stones, hidden):
    r'''Stone and hidden dictionary to easy to read examples.
    >>> stones, hidden = text_to_stone_hidden(hidden_board_text)
    >>> hidden
    {'black': [(2, 1)]}
    >>> mark_black_hidden('X')
    '/'
    >>> print stone_hidden_to_text(stones, hidden)
    ,,,,,,,,,
    ,OXX,,,,,
    ,/OOX,X,,
    ,OX,X,,,,
    ,,,,,,,,,
    ,,O,O,O,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    '''
    board = dictionary_to_array(stones)
    board = map_at_position(mark_black_hidden, board, 
            hidden.get('black', []))
    return array_to_text(board)



from go_text_protocol import *


def gtp_dictionary_to_array(stone_dictionary):
    '''
    >>> array = gtp_dictionary_to_array({'white': ['F5'], 'black': ['D7']})
    >>> print doctest_board(array)
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,X,,,,,
    ,,,,,,,,,
    ,,,,,O,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    '''
    array = text_to_array(clear_board_text)
    for color, stone_list in stone_dictionary.items():
        for stone in stone_list:
            r, c = gtp_to_array(stone)
            array[r][c] = eval(color)
    return array





# Referee

def notify_genmove(previous_genmove, turn, black, white, news):
    '''Notify computer's turn if not already notified.
    >>> notify_genmove(None, 'white', 'human', 'human', {})
    ('white', {})
    >>> notify_genmove(None, 'white', 'human', 'computer', {})
    ('white', {'genmove': 'white'})
    >>> previous, news = notify_genmove('black', 'white', 'human', 'computer', 
    ...     {'black':  [(7, 2)], 'hide': [(7, 2)]})
    >>> code_unit.print_diff(news, {'black': [(7, 2)], 'genmove': 'white', 'hide': [(7, 2)]} )

    Do not notify twice in a row.
    >>> previous, news = notify_genmove('white', 'white', 'human', 'computer', {})
    >>> news
    {}
    '''
    genmove_news = news
    if 'white' == turn:
        genmove = 'white'
        if 'computer' == white:
            if 'white' != previous_genmove:
                genmove_news['genmove'] = 'white'
    elif 'black' == turn:
        genmove = 'black'
        if 'computer' == black:
            if 'black' != previous_genmove:
                genmove_news['genmove'] = 'black'
    else:
        print 'notify_genmove:  did you know black nor white has this turn?  ', turn
        genmove = previous_genmove
    return genmove, genmove_news


def notify_turn(previous_turn, turn, news):
    '''
    >>> previous, news = notify_turn('white', 'black', {})
    >>> news
    {'turn': 'black'}
    >>> previous
    'black'
    >>> previous, news = notify_turn(None, 'black', {})
    >>> news
    {'turn': 'black'}
    >>> previous
    'black'
    '''
    if previous_turn != turn:
        news['turn'] = turn
    return turn, news


def next_turn(turn):
    '''Next player's turn.
    >>> next_turn('white')
    'black'
    >>> next_turn('black')
    'white'
    >>> next_turn('empty')
    next_turn:  >_< turn is empty?
    'empty'
    '''
    if 'black' == turn:
        turn = 'white'
    elif 'white' == turn:
        turn = 'black'
    else:
        print 'next_turn:  >_< turn is %s?' \
                % turn
    return turn


def get_next_turns(turns, last_color = None):
    '''Next turn based on last turn's color.
    By default, black goes first.
    >>> get_next_turns([])
    ['black']
    >>> get_next_turns([], 'black')
    ['white']
    >>> get_next_turns(['black'])
    ['black', 'white']
    >>> get_next_turns(['black', 'white'])
    ['black', 'white', 'black']
    >>> get_next_turns(['black', 'white'], 'black')
    ['black', 'white', 'white']
    '''
    if not last_color:
        if 1 <= len(turns):
            last_color = turns[-1]
        else:
            last_color = 'white'
    if last_color:
        turns.append(next_turn(last_color))
    return turns


def get_previous(turns):
    '''
    >>> get_previous([])
    []
    >>> get_previous(['black'])
    []
    >>> get_previous(['black', 'white'])
    ['black']
    '''
    if len(turns) <= 0:
        pass
    else:
        turns.pop(-1)
    return turns


def clear_board_example():
    r'''Clear board clears history of play.
    >>> referee = referee_class()
    >>> news = referee.play_flash({'black': [(0, 1)]})
    >>> print referee.show_board()
    ,X,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    >>> referee.history[0].get('black')
    (0, 1)
    >>> referee.clear_board()
    >>> print referee.show_board()
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    >>> referee.history
    []

    Send news to Flash when Flash asks to clear board.
    >>> referee.secret_gifts = []
    >>> news = referee.act_flash({'clear_board':  'black'})
    >>> if not news.get('clear_board'):  news

    On clear board, reset gifts and tell Flash.
    >>> if not 1 <= len(referee.secret_gifts):  referee.secret_gifts
    >>> news.get('hide_gift')
    '_0'

    On clear board, reset territory as copies of 'neutral'.
    >>> neutral = news.get('territory').get('neutral')
    >>> neutral[0]
    (0, 0)
    >>> neutral[-1]
    (8, 8)

    On clear board, reset game_over.
    >>> news.get('game_over')
    'none'
    '''

def refresh_client_example():
    r'''Client asks for refresh.
    Referee sends full state of board.
    >>> referee = referee_class()
    >>> referee._give_hide()
    >>> news = referee.hide_black({'black': [(0, 1)]})
    >>> news.get('black')
    [(0, 1)]
    >>> news = referee.act_flash({'showboard': True})
    >>> news.get('black')
    [(0, 1)]
    >>> news.get('hide')
    [(0, 1)]
    '''

def referee_resign_example():
    r'''referee accepts white resigns.
    >>> referee = referee_class()
    >>> referee.tell('genmove white', '= resign\n\n')
    >>> news = referee.notify_dictionary()
    >>> news.get('resign', [])
    'white'
    >>> news.get('game_over', [])
    'win'
    '''

def brave_capture_example():
    '''Capture at last liberty for either side.
    >>> referee = referee_class()
    >>> history = sgf_to_history('sgf/_capture_04_13_white_to_black.sgf')
    >>> for event in history[:-2]:
    ...     news = referee._turn_from_history(event)

    At (0, 3), white is poised to capture.
    >>> pb(referee.board)
    ,OX,OX,,,
    ,OXOX,,O,
    ,,OX,,X,,
    ,,OXX,,X,
    ,O,OXXO,,
    ,,,OOOOOO
    ,,X,OXXXO
    ,,XOX,,,X
    ,,,X,X,X,

    White captures at last liberty.
    >>> for event in history[-2:]:
    ...     news = referee._turn_from_history(event)
    >>> pb(referee.board)
    ,O,OOX,,,
    ,O,OX,,O,
    ,,OX,,X,,
    ,,OXX,,X,
    ,O,OXXO,,
    ,X,OOOOOO
    ,,X,OXXXO
    ,,XOX,,,X
    ,,,X,X,X,

    Undo returns to before capture.
    >>> news = referee.act_flash({'undo': 2})
    >>> news = referee.act_flash({'more': True})
    >>> pb(referee.board)
    ,OX,OX,,,
    ,OXOX,,O,
    ,,OX,,X,,
    ,,OXX,,X,
    ,O,OXXO,,
    ,,,OOOOOO
    ,,X,OXXXO
    ,,XOX,,,X
    ,,,X,X,X,
    '''


def setup_undo_hide_example2(locals_dict, globals_dict):
    r'''Play two hidden stones and two white stones.
    >>> referee = referee_class()
    >>> referee._give_hide()
    >>> referee._give_hide()
    >>> referee._give_hide()
    >>> referee.undo_gift = 25
    >>> news = referee.hide_black({'black': [(0, 1)]})
    >>> print referee.show_board()
    ,/,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,

    #>>> news = referee.play({'white': [(0, 0)]}) # A9
    >>> referee.act_flash({'genmove':  'white'})
    >>> referee.act_white_gtp('genmove white', '= A9\n\n')
    ['initial_influence black territory_value']
    >>> news = referee.notify()

    >>> news = referee.hide_black({'black': [(1, 1)]})
    >>> print referee.show_board()
    O/,,,,,,,
    ,/,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    >>> news.get('hide_gift')
    '_1'
    >>> referee.hide_gift
    1

    #>>> news = referee.play({'white': [(1, 0)]}) # A8
    >>> referee.act_flash({'genmove':  'white'})
    >>> referee.act_white_gtp('genmove white', '= A8\n\n')
    ['initial_influence black territory_value']
    >>> news = referee.notify()
    >>> print referee.show_board()
    O/,,,,,,,
    O/,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    '''
    # run my example then return my example's referee.
    code_unit.inline_examples(
        setup_undo_hide_example2.__doc__,
        locals(), globals(), 
        verify_examples = False) # recursive doctest croaks
    return referee


def undo_hide_example():
    r'''
    undo a hidden stone while staying hidden,
    then undo to before its play.
    >>> referee = referee_class()
    >>> referee._give_hide()
    >>> referee._give_hide()
    >>> referee._give_hide()
    >>> news = referee.hide_black({'black': [(0, 1)]})
    >>> news.get('hide_gift')
    '_2'
    >>> if not news.get('black') == [(0, 1)]:  news
    >>> print referee.show_board()
    ,/,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    
    #>>> news = referee.play({'white': [(0, 0)]}) # A9
    >>> referee.act_flash({'genmove':  'white'})
    >>> referee.act_white_gtp('genmove white', '= A9\n\n')
    ['initial_influence black territory_value']
    >>> news = referee.notify()
    >>> news.get('white')
    [(0, 0)]
    >>> print referee.show_board()
    O/,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    >>> referee.hide_gift
    2
    >>> news = referee.act_flash({'undo':  2})
    >>> news.get('more')
    True
    >>> news.get('empty')
    [(0, 0)]
    >>> news = referee.act_flash({'more':  True})
    >>> news.get('empty')
    [(0, 1)]
    >>> news.get('unhide')
    [(0, 1)]
    >>> print referee.show_board()
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,

    >>> code_unit.inline_examples(
    ...     setup_undo_hide_example2.__doc__,
    ...     locals(), globals())
    >>> news = referee.act_flash({'undo': 2})

    Client when receives 'more', echoes back 'more'.
    >>> news.get('more')
    True
    >>> news = referee.act_flash({'more':  True})

    Give back hide_gift
    >>> news.get('hide_gift')
    '_2'
    >>> referee.hide_gift
    2
    >>> print referee.show_board()
    O/,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    >>> news = referee.act_flash({'undo': 2})
    >>> news.get('more')
    True

    While waiting for more, other actions are not accepted,
    until client asks for more.
    >>> news = referee.play_flash({'black': [(0, 0)]})
    referee._wait_your_turn(black) # self.more
    >>> news.get('more')
    True
    >>> news = referee.act_flash({'more': True})
    >>> print referee.show_board()
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,

    When white plays at hidden stone,
    white sees the hidden stone and may move again.
    >>> referee = referee_class()
    >>> referee._give_hide()
    >>> referee._give_hide()
    >>> referee._give_hide()
    >>> news = referee.hide_black({'black': [(0, 1)]})

    if white plays on top of black spy...
    I solved this for white using GTP.
    Let's reuse that solution.
    So the example changes a little.
    #>>> news = referee.play_flash({'white': [(0, 0)]}) # A9
    >>> referee.act_flash({'genmove':  'white'})
    >>> referee.act_white_gtp('genmove white', '= A9\n\n')
    >>> news = referee.notify()
    >>> news = referee.play_flash({'black': [(1, 1)]})
    >>> print referee.show_board()
    O/,,,,,,,
    ,X,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,

    #>>> news = referee.play_flash({'white': [(0, 1)]}) # B9
    >>> referee.act_flash({'genmove':  'white'})
    >>> referee.act_white_gtp('genmove white', '= B9\n\n')
    ['genmove white']
    >>> referee.act_white_gtp('genmove white', '= A8\n\n')
    >>> news = referee.notify()
    >>> print referee.show_board()
    OX,,,,,,,
    OX,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,

    undo after white's play reveals a hidden stone, 
    yet to after hidden stone had been played.
    >>> referee.hide_gift
    2
    >>> news = referee.act_flash({'undo': 2})
    >>> news = referee.act_flash({'more': True})
    >>> print referee.show_board()
    OX,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,

    when undoing stone that had been found,
    do not give back gift, as black would explot this.
    >>> referee.hide_gift
    2
    >>> news = referee.hide_black({'black': [(1, 1)]})
    >>> referee.act_flash({'genmove':  'white'})
    >>> referee.act_white_gtp('genmove white', '= B8\n\n')
    ['genmove white']
    >>> referee.act_white_gtp('genmove white', '= A8\n\n')
    >>> news = referee.notify()
    >>> print referee.show_board()
    OX,,,,,,,
    OX,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    >>> referee.hide_gift
    1
    >>> news = referee.act_flash({'undo': 2})
    >>> news = referee.act_flash({'more': True})
    >>> print referee.show_board()
    OX,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    >>> referee.hide_gift
    1
    '''


def undo_capture_example():
    r'''After assassination, undo leaves black assasins.
    in which the assassin had been there for a couple of turns, 
    so as to remain there.
    >>> referee = referee_class()
    >>> referee._give_hide()
    >>> referee._give_hide()
    >>> referee._give_hide()
    >>> news = referee.hide_black({'black': [(0, 1)]})

    #>>> news = referee.play_flash({'white': [(0, 0)]}) # A9
    >>> referee.act_flash({'genmove':  'white'})
    >>> referee.act_white_gtp('genmove white', '= A9\n\n')
    >>> news = referee.notify()
    >>> g = referee.hide_gift
    >>> news = referee.hide_black({'black': [(1, 1)]})
    >>> if not g - referee.hide_gift == 1:  g, referee.hide_gift, news, 

    #>>> news = referee.play_flash({'white': [(1, 0)]}) # A8
    >>> referee.act_flash({'genmove':  'white'})
    >>> referee.act_white_gtp('genmove white', '= A8\n\n')
    >>> news = referee.notify()
    >>> print referee.show_board()
    O/,,,,,,,
    O/,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,

    After assassination, undo leaves black assasins
    revealed, although they may be unplayed.
    If playing an assassin, do not pay gift,
    since this option is strongly dominated by not paying.
    >>> referee.hide_gift
    1
    >>> news = referee.hide_black({'black': [(2, 0)]})
    >>> referee.hide_gift
    1
    >>> news.get('hide_gift')
    >>> news.get('unhide')
    [(0, 1), (1, 1)]
    >>> referee.history[-1].get('unhide')
    [(0, 1), (1, 1)]
    >>> referee.act_flash({'genmove': 'white'})
    >>> referee.act_white_gtp('genmove white', '= B7\n\n')
    >>> news = referee.notify()
    >>> print referee.show_board()
    ,X,,,,,,,
    ,X,,,,,,,
    XO,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    >>> news = referee.act_flash({'undo': 2})
    >>> print referee.show_board()
    ,X,,,,,,,
    ,X,,,,,,,
    X,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    >>> news = referee.act_flash({'more': True})
    >>> print referee.show_board()
    OX,,,,,,,
    OX,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    >>> news = referee.act_flash({'undo': 2})
    >>> print referee.show_board()
    OX,,,,,,,
    ,X,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    >>> news = referee.act_flash({'more': True})
    >>> print referee.show_board()
    OX,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,

    In these examples, for convenience,
    referee is unconcerned with security or protocol (GTP or SGF).
    Ambassador or other functions must ensure security of clients.
    # TODO:  undo GnuGo
    '''


def white_captures_spy_example():
    r'''when black spy is caught it is unhid.
    >>> referee = referee_class()
    >>> referee._give_hide()
    >>> referee._give_hide()
    >>> referee._give_hide()
    >>> news = referee.hide_black({'black': [(0, 0)]})
    >>> referee.act_flash({'genmove':  'white'})
    >>> referee.act_white_gtp('genmove white', '= B9\n\n')
    >>> news = referee.notify()
    >>> news = referee.hide_black({'black': [(1, 0)]})
    >>> referee.act_flash({'genmove':  'white'})
    >>> referee.act_white_gtp('genmove white', '= B8\n\n')
    >>> news = referee.notify()
    >>> print referee.show_board()
    /O,,,,,,,
    /O,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    >>> news = referee.hide_black({'black': [(2, 1)]})
    >>> referee.act_flash({'genmove':  'white'})
    >>> referee.act_white_gtp('genmove white', '= A7\n\n')
    >>> news = referee.notify()

    Flash sees his stones are unhid, so may update.
    >>> news.get('unhide')
    [(0, 0), (1, 0)]
    >>> referee.history[-1].get('unhide')
    [(0, 0), (1, 0)]
    >>> print referee.show_board()
    ,O,,,,,,,
    ,O,,,,,,,
    O/,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    '''

def spy_group_no_danger_example():
    r'''Spy and black neighbor share liberties.
    >>> referee = referee_class()
    >>> referee._give_hide()
    >>> referee._give_hide()
    >>> referee._give_hide()
    >>> news = referee.hide_black({'black': [(0, 0)]})
    >>> news.get('warning')
    [(0, 0)]
    >>> referee.act_flash({'genmove':  'white'})
    >>> referee.act_white_gtp('genmove white', '= A2\n\n')
    >>> news = referee.notify()

    Black spy and normal black share liberties.
    >>> news = referee.act_flash({'black': [(0, 1)]})
    >>> news.get('warning')
    >>> news.get('danger')
    '''


def enable_hide_example():
    r'''Referee only allows 3 hidden stones in play + reserve.
    Reward deck may contain more than 3 hidden stones.
    >>> referee = referee_class()
    >>> referee.undo_gift = 25
    >>> referee.hide_max
    3
    
    When 2 hidden stones in play and 0 in reserve.
    When undo rewarded, referee gives hidden.
    >>> news = referee.act_flash({'black': [[2, 2]]})
    >>> news = referee._genmove_white_mock((4, 4))

    For test, manually give before the turn.
    >>> referee._give_hide()

    Flash movieClip label cannot start with a number,
    so an underscore prepends the number.
    >>> news = referee.act_flash({'black': [[2, 6]]})
    >>> news.get('hide_gift')
    '_1'
    >>> news = referee._genmove_white_mock((4, 3))
        
    >>> referee._give_hide()
    >>> news = referee.act_flash({'black': [[2, 4]]})
    >>> news.get('hide_gift')
    '_2'
    >>> news = referee._genmove_white_mock((4, 2))
    
    when 0 hidden stones in play and 2 in reserve.
    When style rewarded, referee gives 
    >>> referee._give_hide()
    >>> news = referee.act_flash({'black': [[6, 2]]})
    >>> news.get('hide_gift')
    '_3'
    >>> news = referee._genmove_white_mock((4, 1))

    when 0 hidden stones in play and 3 in reserve.
    When style rewarded, referee does not give,
    instead returns error and prints error.
    >>> referee._give_hide()
    referee._give_hide:  cannot have 4 hide in play because hide_max is 3
    'referee._give_hide:  cannot have 4 hide in play because hide_max is 3'
    >>> news = referee.act_flash({'black': [[6, 6]]})
    >>> news.get('hide_gift')
    >>> news = referee._genmove_white_mock((3, 2))
    >>> news = referee.hide_black({'black': [[3, 3]]})
    >>> news.get('hide_gift')
    '_2'
    >>> referee.act_flash({'genmove':  'white'})
    >>> referee.act_white_gtp('genmove white', '= D6\n\n')
    ['genmove white']
    >>> referee.act_white_gtp('genmove white', '= B6\n\n')
    >>> news = referee.notify()
    
    When Flash hides a stone, referee updates gift count.
    >>> news = referee.hide_black({'black': [[0, 0]]})
    >>> news.get('hide_gift')
    '_1'
    >>> referee.act_flash({'genmove':  'white'})
    >>> referee.act_white_gtp('genmove white', '= A8\n\n')
    >>> news = referee.notify()

    >>> referee._give_hide()
    >>> news = referee.act_flash({'black': [[0, 1]]})
    >>> news.get('hide_gift')
    '_2'
    >>> news = referee._genmove_white_mock((8, 8))

    >>> news = referee.hide_black({'black': [[7, 7]]})
    >>> news = referee._genmove_white_mock((8, 7))
    >>> news = referee.hide_black({'black': [[7, 6]]})
    >>> news = referee._genmove_white_mock((8, 6))
    
    When no hide gifts left, may not hide 
    but may move again.
    >>> news = referee.hide_black({'black': [[7, 0]]})
    referee._why_not_hide:  cannot hide because hide_gift is 0
    >>> news.get('hide_gift')
    '_0'
    >>> news.get('error')
    'hide_gift'

    When style rewarded, referee does not give 
    when 3 hidden stones in play and 0 in reserve.
    >>> referee._give_hide()
    referee._give_hide:  cannot have 4 hide in play because hide_max is 3
    'referee._give_hide:  cannot have 4 hide in play because hide_max is 3'
    >>> news = referee.hide_black({'black': [[7, 5]]})
    referee._why_not_hide:  cannot hide because hide_gift is 0
    >>> news.get('hide_gift')
    '_0'
    >>> news.get('error')
    'hide_gift'
    
    when 2 hidden stones in play and 1 in reserve.
    When style rewarded, referee does not give 
    >>> referee._give_hide()
    referee._give_hide:  cannot have 4 hide in play because hide_max is 3
    'referee._give_hide:  cannot have 4 hide in play because hide_max is 3'
    >>> news = referee.act_flash({'black': [[7, 4]]})
    >>> news.get('hide_gift')
    '''


def setup_extra_stone_example():
    '''
    INT. PC ROOM, SEOUL - NIGHT
        (For simplicity, only jump, diagonal, dog mouth 
    patterns are used.)
        >>> pattern_texts = [ jump_pattern_text,
        ...     diagonal_pattern_text, 
        ...     dog_mouth_pattern_text ]
        >>> pattern_dictionary = get_pattern_dictionary(
        ...     pattern_texts)
    >>> referee = referee_class()

    Dooburm starts a game.
    Dooburm plays against stronger player so will receive gifts.
        (Secretly referee selects and shuffles.  Referee, but not the player, sees that the next gifts will be:  two cake boxes, hide, two cake boxes, hide, two cake boxes.  In any shuffling, there are never two cake boxes in a row.)
        >>> referee.secret_gifts = ['hide_gift', 'extra_stone_gift', 'hide_gift', 'extra_stone_gift', 'extra_stone_gift', 'hide_gift']

    (History of moves appear in diagram at end of this example.)
    
    Cannot take extra stone if do not have one.
    >>> news = referee.act_flash({'extra_stone_gift':  '_1'})
    >>> news.get('help')
    >>> news.get('extra_stone_gift')
    '_0'
    
    Flash sends black stone here.
    >>> news = referee.act_flash({'black': [[2, 6]]})

    Each turn, black's last move is marked.
    If pass, do not send marker.
    >>> news.get('black_last_move')
    [(2, 6)]

    Suppose GnuGo sends white stone here.
    >>> news = referee._genmove_white_mock((5, 2))
    >>> referee.secret_gifts
    ['extra_stone_gift', 'hide_gift', 'extra_stone_gift', 'extra_stone_gift', 'hide_gift']

    Each turn, white's last move is marked.
    >>> news.get('white_last_move')
    [(5, 2)]
    '''

def extra_stone_example():
    '''On a good move, referee gives an extra stone to black.

    Outline of flow:
    	Flash press and sends intersection
		referee validates move
		Referee matches formation, 
		Referee cites each animation of formation and rotation at position
		Referee increases undo_gift
		Referee decides if to gift
			Referee gives gift.
				Flash updates gift button
			+ Flash animates formation of rotation, 
			+ Flash animates undo_gift
			Flash shows new stones, danger, connections
	Flash press and send gift 
			(undo_gift, hide, extra stone), 
		Referee interprets gift
		Referee decreases undo_gift
			Flash updates gift

    >>> code_unit.inline_examples(
    ...     setup_extra_stone_example.__doc__,
    ...     locals(), globals())

    Dooburm makes a JUMP.

          . . 
        X . X .
          . .

    Flash sends black stone here.
    >>> referee.undo_gift
    11
    >>> news = referee.act_flash({'black': [[2, 4]]})
        
        (Technical details:  Referee matches formation of jump 
            (Flash does not call _give_gift)
        Referee sends new undo_gift level 5 to Flash.)
        Flash listens to undo_gift at level 1 to 25.
        >>> if not 'undo_gift' in required_dictionary:  required_dictionary
        >>> if not news.get('undo_gift') == 21:  news, referee.secret_gifts
        
        verify MANUALLY:  Flash validates undo_gift.
        verify MANUALLY:  Flash plays undo_gift.
        
        Flash listens to jump formation with rotation 90 at position.
        Referee sends jump formation with 90 rotation 90 at position to Flash
        >>> ## if not 'formation_jump' in required_dictionary:  required_dictionary
        >>> news.get('formation_jump')
        [(2, 4, 'rotate_90_mc')]
        
        verify MANUALLY:  Flash validates formation.
        verify MANUALLY:  Flash plays animation with rotation 90 at position (2, 3))
        
    He sees a heart between the pieces of cake.

    The piece of cake lifts up, and underneath is are TWO CAKE BOXES.

    >>> if not news.get('extra_stone_gift') == '_1':  news
    >>> if not '_1' in required_dictionary.get('extra_stone_gift'):
    ...     print required_dictionary
    >>> news.get('help')
    'extra_stone_gift'
    >>> if not 'extra_stone_gift' in required_dictionary.get('help'):
    ...     print required_dictionary
    
    Box moves over to gift bag on right side of screen.

                KATIE
        CLICK ME TO TAKE TWO CAKES!

    White claims center.
    >>> news = referee._genmove_white_mock((4, 4))

    Dooburm makes a DIAGONAL:
    
        X .
        . X .
          .

    He receives another gift, 
    which cannot be an extra stone, 
    because he can only have one extra stone gift at a time.
    Anyway he gets a hide gift.
        >>> referee.secret_gifts # inspect
        ['hide_gift', 'extra_stone_gift', 'extra_stone_gift', 'hide_gift']

    >>> news = referee.act_flash({'black': [[1, 3]]})
    >>> news.get('extra_stone_gift')
    >>> news.get('extra_stone')

    White also matches pattern, and black sees this,
    but white gets no gift.
    White does not see the formations that black matches.
        >>> referee.secret_gifts # inspect
        ['extra_stone_gift', 'extra_stone_gift', 'hide_gift']
    >>> news = referee._genmove_white_mock((3, 2))
    >>> news.get('formation_jump')
    [(3, 2, 'rotate_180_mc')]
    >>> news.get('undo_gift')

    Dooburm still has two cake boxes, makes a JUMP.
    He gets another extra stone, but must use it now.
    He uses it to hide his extra stone.
    >>> before = referee.undo_gift
    >>> news = referee.hide_black({'black': [[1, 1]]})
    >>> if not news.get('help') == 'extra_stone':  news
    >>> news.get('extra_stone_gift')
    '_1'
    >>> if news.get('turn') == 'white':  news
    >>> referee.turn
    'black'

    The piece of cake lifts up, and underneath is are TWO CAKE BOXES.

                KATIE
        FREE CAKE!

    For his extra stone,
    Dooburm makes a dog's mouth, which is a double knight's move,
    although it it partly blocked.

        X . .
        . . X .
        X . O

    He does not receive the next extra stone gift,
    instead he receives the hide gift, and the
    extra stone gift is placed at the bottom of the deck.
        >>> referee.secret_gifts # inspect
        ['extra_stone_gift', 'hide_gift']
        >>> referee.hide_gift
        1
    >>> news = referee.act_flash({'black': [[4, 5]]})
    referee._give_extra_stone:  cannot have 2 extra_stone + gift because extra_stone_max is 1.
    >>> news.get('formation_dog_mouth')
    [(4, 5, 'rotate_0_mc')]
    >>> referee.extra_stone_black
    0
    >>> referee.extra_stone_gift
    1
    >>> referee.secret_gifts # inspect
    ['extra_stone_gift']
    
    On this extra move, he cannot receive another CAKE BOX gift, because that would discourage white.  Instead, by chance, Dooburm receives a HIDE gift.
    >>> news.get('extra_stone_gift')
    >>> if not news.get('hide_gift') == '_2':  news
    >>> news = referee.act_flash({'black': [[4, 8]]})
    referee._black_turn_for_more(black) # turn_reminder:  white

    White stakes claim for southeast corner or south side.
    >>> news = referee._genmove_white_mock((6, 5))
    
    At his gift bag, Dooburm clicks to take a second turn.
    First he plays on the right.
    >>> news = referee.act_flash({'extra_stone_gift':  '_1'})
    >>> news.get('extra_stone_gift')
    '_0'

    No turn is generated for activating extra stone,
    except to note it was consumed.
    >>> referee.history[-1]
    {'extra_stone': '_1', 'extra_stone_gift': '_0'}
    >>> news = referee.act_flash({'black':  [[6, 6]]})    
    
    He attacks on both sides, catching white in a dog's mouth.
    >>> news = referee.act_flash({'black':  [[6, 4]]})    

    After getting two stones (one extra),
    black cannot move again until white moves.
    >>> news = referee.act_flash({'black':  [[6, 8]]}) 
    referee._black_turn_for_more(black) # turn_reminder:  white
    >>> news.get('turn_reminder')
    'white'
    >>> news = referee._genmove_white_mock((7, 1))
    >>> print history_to_text(referee.history)
      0 1 2 3 4 5 6 7 8 
    0 . . . . . . . . . 
    1 . X6. X4. . . . . 
    2 . . . . X2. X0. . 
    3 . . O5. . . . . . 
    4 . . . . O3X7. . . 
    5 . . O1. . . . . . 
    6 . . . . XbO8Xa. . 
    7 . Oc. . . . . . . 
    8 . . . . . . . . . 
    '''

def setup_load_example():
    example_file = 'reference_game/white_tiger_wallis.sgf'
    sgf_text = text.load(example_file)
    history = get_history(parse(sgf_text))
    return history



def load_example():
    '''Load SGF with white, black, and add black.
    >>> referee = referee_class()
    >>> history = setup_load_example()
    >>> 1 <= len(history) or history
    True
    >>> for event in history:
    ...     news = referee._turn_from_history(event)
    >>> pb(referee.board)
    ,,,,X,,,X
    ,X,OX,XXX
    ,,XXOXXXO
    ,,X,OXXXO
    ,,X,OXOOO
    ,,X,OO,,O
    X,XXXO,O,
    XXXOOO,O,
    XOOOO,O,,
    
    Black wins by about 20.
    >>> referee.score_black(envoy)
    20

    TODO load SGF with branches
    >>> TODO = True
    >>> example_with_branches_file = 'reference_game/white_tiger_invades_black_village_andrew_wallis_2009-09-03.sgf'
    '''


def replay_example():
    '''Save and reload history with gifts.
    >>> code_unit.inline_examples(
    ...      extra_stone_example.__doc__,
    ...      locals(), globals())
    >>> import pprint
    >>> pprint.pprint(referee.history)
    [{'black': (2, 6)},
     {'white': (5, 2)},
     {'black': (2, 4), 'extra_stone_gift': '_1'},
     {'white': (4, 4)},
     {'black': (1, 3), 'hide_gift': '_1'},
     {'white': (3, 2)},
     {'black': (1, 1),
      'extra_stone': '_2',
      'extra_stone_gift': '_1',
      'hide': [(1, 1)],
      'hide_gift': '_0'},
     {'black': (4, 5), 'hide_gift': '_1'},
     {'white': (6, 5)},
     {'extra_stone': '_2', 'extra_stone_gift': '_0'},
     {'black': (6, 6)},
     {'black': (6, 4)},
     {'white': (7, 1)}]
    >>> sgf_tree = get_sgf_tree(referee.history)
    >>> history = get_history(sgf_tree)
    >>> pprint.pprint(history)
    [{'black': (2, 6)},
     {'white': (5, 2)},
     {'black': (2, 4), 'extra_stone_gift': '_1'},
     {'white': (4, 4)},
     {'black': (1, 3), 'hide_gift': '_1'},
     {'white': (3, 2)},
     {'black': (1, 1),
      'extra_stone': '_2',
      'extra_stone_gift': '_1',
      'hide': [(1, 1)],
      'hide_gift': '_0'},
     {'black': (4, 5), 'hide_gift': '_1'},
     {'white': (6, 5)},
     {'extra_stone': '_2', 'extra_stone_gift': '_0'},
     {'black': (6, 6)},
     {'black': (6, 4)},
     {'white': (7, 1)}]
    >>> print history_to_text(history)
      0 1 2 3 4 5 6 7 8 
    0 . . . . . . . . . 
    1 . X6. X4. . . . . 
    2 . . . . X2. X0. . 
    3 . . O5. . . . . . 
    4 . . . . O3X7. . . 
    5 . . O1. . . . . . 
    6 . . . . XbO8Xa. . 
    7 . Oc. . . . . . . 
    8 . . . . . . . . . 
    >>> referee = referee_class()
    >>> for event in history:
    ...     news = referee._turn_from_history(event)

    Why are turns slightly different?
    extra stone is read as single turn?
    >>> print history_to_text(referee.history)
      0 1 2 3 4 5 6 7 8 
    0 . . . . . . . . . 
    1 . X6. X4. . . . . 
    2 . . . . X2. X0. . 
    3 . . O5. . . . . . 
    4 . . . . O3X7. . . 
    5 . . O1. . . . . . 
    6 . . . . XaO8X9. . 
    7 . Ob. . . . . . . 
    8 . . . . . . . . . 
    >>> ## pprint.pprint(referee.history)
    '''

def multiple_formation_examle():
    '''
    >>> TODO = 'Flash plays formation at multiple locations or rotations simultaneously.'
    '''

def match_hide_example():
    '''Hiding a stone also matches formation, 
    same as playing a stone.
    >>> code_unit.inline_examples(
    ...     extra_stone_example.__doc__,
    ...     locals(), globals())
    >>> TODO
    '''

def undo_extra_stone_example():
    '''After extra_stone, placing two black stones in a row,
    undo returns to only one turn.
    Undo also decrements undo.
    >>> code_unit.inline_examples(
    ...     extra_stone_example.__doc__,
    ...     locals(), globals())
    >>> news = referee.act_flash({'undo': 2})
    >>> news.get('more')
    True
    >>> news = referee.act_flash({'more': True})
    >>> print history_to_text(referee.history)
      0 1 2 3 4 5 6 7 8 
    0 . . . . . . . . . 
    1 . X6. X4. . . . . 
    2 . . . . X2. X0. . 
    3 . . O5. . . . . . 
    4 . . . . O3X7. . . 
    5 . . O1. . . . . . 
    6 . . . . . O8Xa. . 
    7 . . . . . . . . . 
    8 . . . . . . . . . 
    >>> referee.extra_stone_gift
    0

    After extra stone, undo returns to last black move.
    Since black took a turn in a row,
    only one turn is undone.
    >>> news = referee.act_flash({'undo': 2})
    >>> news.get('more')
    >>> print history_to_text(referee.history)
      0 1 2 3 4 5 6 7 8 
    0 . . . . . . . . . 
    1 . X6. X4. . . . . 
    2 . . . . X2. X0. . 
    3 . . O5. . . . . . 
    4 . . . . O3X7. . . 
    5 . . O1. . . . . . 
    6 . . . . . O8. . . 
    7 . . . . . . . . . 
    8 . . . . . . . . . 
    >>> referee.extra_stone_gift
    0

    Referee returns extra_stone to black.
    >>> news = referee.act_flash({'undo': 2})
    >>> news = referee.act_flash({'more': True})
    >>> print history_to_text(referee.history)
      0 1 2 3 4 5 6 7 8 
    0 . . . . . . . . . 
    1 . X6. X4. . . . . 
    2 . . . . X2. X0. . 
    3 . . O5. . . . . . 
    4 . . . . O3. . . . 
    5 . . O1. . . . . . 
    6 . . . . . . . . . 
    7 . . . . . . . . . 
    8 . . . . . . . . . 
    >>> referee.extra_stone_gift
    1
    >>> news.get('extra_stone_gift')
    '_1'

    Likewise, territory is reverted when undone.
    >>> TODO = 'territory updates too'

    When undone to beginning of time, then field is neutral as it was before.
    >>> TODO = 'territory updates too'
    
    Last move marker reverts.
    >>> news.get('black_last_move')
    [(1, 1)]
    >>> news.get('white_last_move')
    [(3, 2)]

    If at beginning of time, remove last move markers.
    >>> TODO = 'remove move markers'

    If at beginning of time, undo no further.
    '''


star_positions = [(2, 2), (2, 6), (6, 2), (6, 6)]
def star_example():
    '''If unoccupied, show star point.
    When occupied, do not see star point.
    >>> referee = referee_class()
    >>> news = referee.act_flash({'showboard':  True})
    >>> news.get('star')
    [(2, 2), (2, 6), (6, 2), (6, 6)]
    >>> news = referee.act_flash({'black': [(2, 6)]})
    '''


handicap_9x9_list = [
    # undo,     hide,   extra
      [0 ,      0 ,      0 ],
      [5 ,      2 ,      1 ],
      [15 ,     3 ,      2 ],       
      [25 ,     4 ,      2 ],
      [25 ,     5 ,      3 ],
      [25 ,     5 ,      8 ],
      [25 ,     0 ,      12 ],
      [25 ,     0 ,      20 ],
      [25 ,     0 ,      28 ],
    ]

gnugo_rank = -14

def get_rank(level):
    '''
    >>> get_rank(1)
    -39
    >>> get_rank(10)
    -30
    >>> get_rank(42)
    -14
    '''
    return (level / 2) - 35 - max(0, 5 - level)


def get_level(rank):
    '''
    >>> get_level(-39)
    1
    >>> get_level(-30)
    10
    >>> get_level(-14)
    42
    '''
    return int(((5 + rank) - min(-30, rank + 4.5)) * 2)

def set_level(referee, black_level):
    '''
    >>> referee = referee_class()
    >>> get_rank(1)
    -39
    >>> referee = set_level(referee, 1)
    >>> referee.turns_in_a_row_max
    4
    >>> referee.secret_gifts.count('extra_stone_gift')
    12
    >>> referee = set_level(referee, 10)
    >>> referee.secret_gifts.count('extra_stone_gift')
    3
    >>> referee.turns_in_a_row_max
    2

    Reset and notify gifts
    >>> referee.hide_gift
    0
    >>> referee.now.get('hide_gift')
    '_0'
    >>> referee.undo_gift
    0
    >>> referee.now.get('undo_gift')
    '_0'
    >>> referee.extra_stone_gift
    0
    >>> referee.now.get('extra_stone_gift')
    '_0'
    >>> referee.extra_stone_black
    0
    '''
    referee.black_rank = get_rank(black_level)
    difference = referee.white_rank - referee.black_rank
    referee.secret_gifts = get_secret_gifts(difference)
    if difference <= 20:
        referee.turns_in_a_row_max = 2
    else:
        referee.turns_in_a_row_max = 4
    referee.hide_gift = 0
    referee.now['hide_gift'] = '_0'
    referee.undo_gift = 0
    referee.now['undo_gift'] = '_0'
    referee.extra_stone_gift = 0
    referee.now['extra_stone_gift'] = '_0'
    referee.extra_stone_black = 0
    return referee


def get_secret_gifts(handicap_19x19 = 16):
    '''Give a deck of gifts to beginner player, 
    which will be revealed during play.
    >>> secret_gifts = get_secret_gifts()

    Some say GnuGo level 1 plays about 14 kyu.
    New players lose against GnuGo with 3 extra stone and 5 hide cards.
    Rank difference (white - black):
    9x9 handicap = 19x19 handicap / 4
    
    http://www.cs.umanitoba.ca/~bate/BIG/Sect4p1.html
    http://senseis.xmp.net//HandicapForSmallerBoardSizes
    Level       Kyu rank
    1           39
    10          30
    32          14      GnuGo 3.8 (level 1)
    50          10
    68          1       Dan
    70                  1
    79                  6       Pro
    80                          1
    90                          9

    after level 50, only performance determines rank.

    GnuGo   rank difference
    30      16
    26      12
    22      8
    18      4
    14      0

    >>> beginner = get_rank(10)
    >>> beginner
    -30
    >>> rank_difference = gnugo_rank - beginner
    >>> gifts = get_secret_gifts(rank_difference)
    >>> gifts.count('extra_stone_gift')
    3
    >>> gifts.count('hide_gift')
    5
    >>> complete_beginner = get_rank(1)
    >>> complete_beginner
    -48
    >>> rank_difference = gnugo_rank - complete_beginner
    >>> gifts = get_secret_gifts(rank_difference)
    >>> gifts.count('extra_stone_gift')
    12
    >>> gifts.count('hide_gift')
    0
    '''
    handicap_9x9 = handicap_19x19 / 4
    handicap_9x9 = min(handicap_9x9, len(handicap_9x9_list) - 1)
    undo, hide, extra = handicap_9x9_list[handicap_9x9]
    extra_stone_cards = extra * ['extra_stone_gift']
    hide_cards = hide * ['hide_gift']
    secret_gifts = extra_stone_cards + hide_cards
    import random
    random.shuffle(secret_gifts)
    return secret_gifts


def generate_level_experience():
    return [ 10 * (level-1)**2 for level in range(1, 50) ]

level_experience = [0, 10, 40, 90, 160, 250, 360, 490, 640, 810, 1000, 1210, 1440, 1690, 1960, 2250, 2560, 2890, 3240, 3610, 4000, 4410, 4840, 5290, 5760, 6250, 6760, 7290, 7840, 8410, 9000, 9610, 10240, 10890, 11560, 12250, 12960, 13690, 14440, 15210, 16000, 16810, 17640, 18490, 19360, 20250, 21160, 22090, 23040]

def generate_level_difference():
    return [ 32.0 / (level_difference + 1) for level_difference in range(0, 32) ]

level_difference = [32.0, 16.0, 10.666666666666666, 8.0, 6.4000000000000004, 5.333333333333333, 4.5714285714285712, 4.0, 3.5555555555555554, 3.2000000000000002, 2.9090909090909092, 2.6666666666666665, 2.4615384615384617, 2.2857142857142856, 2.1333333333333333, 2.0, 1.8823529411764706, 1.7777777777777777, 1.6842105263157894, 1.6000000000000001, 1.5238095238095237, 1.4545454545454546, 1.3913043478260869, 1.3333333333333333, 1.28, 1.2307692307692308, 1.1851851851851851, 1.1428571428571428, 1.103448275862069, 1.0666666666666667, 1.032258064516129, 1.0]


import time
import copy

class referee_class(object):
    r'''
    	!*^_^*	text board is quick and light, so port as much of rules to a text board referee and limit ambassador relaying the referee's judgements.  
		!*^_^*	everything that is inbetween gnugo and flash communication is offloaded to referee.  examples are ported to referee.  (envoy:gnugo to return:actionscript
)
		!*^_^*	hide has no calls to envoy, therefore does not talk to gnugo, so may be completely ported to referee.	
        
    >>> referee = referee_class()
    >>> referee._give_hide()
    >>> referee._give_hide()
    >>> referee._give_hide()

    Referee hides a stone from GnuGo.
    >>> referee.board = enclosed_empty_region_board
    >>> referee.configure({'white': 'computer'})
    {'white': 'computer'}

    Ignore mistakes (like 'hide' instead of 'black')
    and let the client retry immediately.
    >>> news = referee.hide({'hide':  [(7, 2)]})
    referee.hide:  I only know how to hide black, not {'hide': [(7, 2)]}
    >>> news.get('error')
    'hide_color'
    >>> news = referee.hide({'black':  [(7, 2)]})
    >>> code_unit.print_diff(news, {'black': [(7, 2)], 'genmove': 'white', 'hide': [(7, 2)], 'turn': 'white'} )
    >>> referee.moves[-1]
    (7, 2)

    Referee remembers position of hidden stone.
    >>> referee.hidden
    {'black': [(7, 2)]}

    If GnuGo would play at hidden stone, 
    Python undoes opponent's move 
    and reveals the hidden stone to both.
    GnuGo plays elsewhere.
    >>> gtp_at_hidden = '= C2\n\n'
    >>> referee.turn
    'white'
    >>> referee.previous_turn
    'white'
    >>> referee.tell('genmove white', gtp_at_hidden)
    ['undo', 'play black C2']

    This erases memory of genmove.
    >>> referee.previous_genmove
    >>> referee.tell('undo', '= \n\n')
    >>> referee.tell('play black C2', '= \n\n')
    >>> referee.list_stones('list_stones black', '= C2\n\n')
    >>> referee.list_stones('list_stones white', '= F2\n\n')
    >>> news = referee.notify_dictionary()

    It's still white's turn, 
    so do not tell client to change turn to white,
    but do listen for white to move again.
    >>> code_unit.print_diff(news, {'white': [(7, 5)], 'genmove': 'white', 'unhide': [(7, 2)]} )

    If black would play at hidden stone, 
    Referee notes it's already been played.
    #>>> referee.act_flash({'black':  [(7, 2)]})
    #{'hide': [(7, 2)]}
    >>> referee.tell('play white A1', '= \n\n')
    >>> news = referee.notify_dictionary()
    >>> referee.ask({'black':  [(1, 2)]})
    >>> referee.tell('play black C8', '= \n\n')
    >>> news = referee.notify_dictionary()

    How to use a referee:
    Ask a referee before moving.
    If no answer, no problem.
    >>> referee.ask({'genmove':  'white'})

    Tell a referee after moving.
    If no answer, no problem.
    >>> referee.tell('genmove white', '= G2\n\n')

    The referee doesn't know how to update the board.
    GnuGo updates the referee's stone_dictionary
    >>> referee.list_stones('list_stones black', '= C2\n\n')
    >>> referee.list_stones('list_stones white', '= F2 G2\n\n')

    Get client news from referee after asking and telling.
    >>> news = referee.notify_dictionary()
    >>> code_unit.print_diff(news, {'white': [(7, 6)], 'turn': 'black'} )
    >>> code_unit.print_diff(referee.previous_stone_dictionary, {'white': [(7, 5), (7, 6)], 'black': [(7, 2)]} )
    >>> code_unit.print_diff(referee.stone_dictionary, {'white': [(7, 5), (7, 6)], 'black': [(7, 2)]} )

    ask, tell, list, list, notify
    ActionScript returns Array which PyAMF converts to list,
    but referee likes tuples, so convert [2, 3] to (2, 3).
    >>> referee.ask({'black':  [[8, 2]]})
    >>> referee.to_gtp({'showboard':  True})
    ['showboard']
    >>> referee.to_gtp({'black':  [(8, 2)]})
    ['play black C1']
    >>> referee.tell('play black C1', '= \n\n')
    >>> referee.list_stones('list_stones black', '= C1 C2\n\n')
    >>> referee.list_stones('list_stones white', '= F2 G2\n\n')
    >>> news = referee.notify_dictionary()
    >>> code_unit.print_diff(news, {'genmove': 'white', 'black': [(8, 2)], 'turn': 'white'} )

    ambassador      referee     ambassador
    flash   -->     ask
            <--     tell    <-- gnugo
                    list    <-- gnugo
                    list    <-- gnugo
    flash   <--     notify

    If GnuGo would play at hidden stone, 
    Python undoes opponent's move 
    and reveals the hidden stone to both.
    GnuGo plays elsewhere.
    >>> referee.ask({'clear_board':  True})
    >>> referee.tell('clear_board', '= \n\n')
    >>> referee.board = gnugo_black_assassin_board
    >>> referee.hidden
    {}
    >>> referee.previous_hidden
    {}
    >>> referee.turn = 'black'

    ActionScript returns Array which PyAMF converts to list,
    but referee likes tuples, so convert [8, 3] to (8, 3).
    >>> code_unit.print_diff( referee.hide({'black': [[8, 3]]}), 
    ...        {'hide': [(8, 3)], 'black': [(8, 3)], 'turn': 'white', 'genmove': 'white', 'clear_board': True} )
    >>> referee.ask({'genmove':  'white'})
    >>> referee.tell('genmove white', '= D1\n\n')
    ['undo', 'play black D1']

    >>> referee.tell('play black D1', '= \n\n')
    
    ['genmove white']
    TODO:  Do not rely on black client for white to move.
    TODO:  Do list stones and notify, but instead of client asking, referee tells gnugo he may move.

    TODO:  Merge list_stones into tell?
    Referee asks for black stones, then white stones.
    >>> referee.list_stones('list_stones black', '= C2 D1\n\n')
    >>> referee.list_stones('list_stones white', '= F2\n\n')
    
    ActionScript unhides spy.
    White takes their turn again.
    >>> referee.previous_hidden
    {'black': [(8, 3)]}
    >>> referee.hidden
    {}
    >>> news = referee.notify_dictionary()
    >>> if news['unhide'] != [(8, 3)]:
    ...     print news
    
    >>> referee.ask({'genmove':  'white'})
    >>> referee.tell('genmove white', '= G2\n\n')
    >>> referee.list_stones('list_stones black', '= C2 D1\n\n')
    >>> referee.list_stones('list_stones white', '= F2 G2\n\n')

    >>> news = referee.notify_dictionary()
    >>> code_unit.print_diff(news, {'white': [(7, 6)], 'turn': 'black'} )

    Reveal assassins
    If black would play to capture needing the hidden stone,
    reveal the hidden stone and play the next stone.
    >>> referee.clear_board()
    >>> referee.ask({'clear_board':  True})
    >>> referee.tell('clear_board', '= \n\n')
    >>> referee.stone_dictionary = array_to_dictionary(gnugo_black_assassin_board)
    >>> referee.turns = ['black']
    >>> code_unit.print_diff(
    ...     referee.hide({'black': [(8, 3)]}),
    ...    {'black': [(2, 2), (2, 3), (2, 5), (2, 6), (4, 3), (4, 4), (5, 2), (5, 6), (6, 2), (6, 3), (6, 6), (7, 2), (8, 3)],
    ...     'clear_board': True, 'danger': [(7, 3), (8, 3)], 
    ...     'genmove': 'white', 'hide': [(8, 3)], 'turn': 'white', 'warning': [(8, 4)], 
    ...     'white': [(5, 4), (6, 4), (7, 3), (7, 5), (8, 4)]} )
    >>> print doctest_board(referee.board)
    ,,,,,,,,,
    ,,,,,,,,,
    ,,XX,XX,,
    ,,,,,,,,,
    ,,,XX,,,,
    ,,X,O,X,,
    ,,XXO,X,,
    ,,XO,O,,,
    ,,,XO,,,,

    White moves...
    >>> referee.tell('play white G1', '= \n\n')
    >>> news = referee.notify_dictionary()
     
    On hide, do not notify white, except to make a move.
    >>> referee.ask({'black':  [(7, 4)]})
    >>> referee.to_gtp({'black':  [(7, 4)]})
    ['play black D1', 'play black E2']
    >>> referee.tell('play black D1', '= \n\n')
    >>> referee.tell('play black E2', '= \n\n')
    >>> referee.to_gtp_list_stones()
    ['list_stones black', 'list_stones white']
    >>> referee.tell('list_stones black', '= C2 E2 D1\n\n')
    >>> referee.tell('list_stones white', '= F2 G2\n\n')
    
    Unhide assassins.
    >>> news = referee.notify_dictionary()
    >>> if news['unhide'] != [(8, 3)]:
    ...     print news
    >>> if news.get('genmove') != 'white':
    ...     print news
    ...     print referee.previous_genmove
    ...     print referee.previous_turn, referee.turn
   
    When verbose, echo common requests.
    >>> referee.verbose = True
    >>> referee.ask({'showboard':  True})
    referee.ask( {'showboard': True} )
    >>> referee.verbose = False

    #>>> if news.get('turn') != 'white':
    #...     print news
    #...     print referee.previous_turn
    #...     print referee.turn

    Transmit danger based on hidden stone.

    Read a board.
    >>> referee.load_board_dictionary(hidden_board_text, 'black')
    
    See a board.
    >>> print referee.show_board_dictionary()
    ,,,,,,,,,
    ,OXX,,,,,
    ,/OOX,X,,
    ,OX,X,,,,
    ,,,,,,,,,
    ,,O,O,O,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
     
    Suppose black plays.  First the assassin is revealed.
    >>> referee.ask( {'black': [[3, 3]]} )
    >>> referee.to_gtp( {'black': [[3, 3]]} )
    ['play black B7', 'play black D6']
    >>> print referee.show_board_dictionary()
    ,,,,,,,,,
    ,OXX,,,,,
    ,XOOX,X,,
    ,OX,X,,,,
    ,,,,,,,,,
    ,,O,O,O,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    
    If instead of black, white were to play,
    the assassin is revealed.
    >>> referee.load_board_dictionary(hidden_board_text)
    >>> print referee.show_board_dictionary()
    ,,,,,,,,,
    ,OXX,,,,,
    ,/OOX,X,,
    ,OX,X,,,,
    ,,,,,,,,,
    ,,O,O,O,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    >>> referee.ask({'genmove':  'white'})
    >>> referee.tell('genmove white', '= B7\n\n')
    ['undo', 'play black B7']
    >>> print referee.show_board_dictionary()
    ,,,,,,,,,
    ,OXX,,,,,
    ,XOOX,X,,
    ,OX,X,,,,
    ,,,,,,,,,
    ,,O,O,O,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    >>> referee.tell('genmove white', '= A1\n\n')
    >>> news = referee.notify_dictionary()
    
    >>> news = referee.hide({'black': [(4, 2)]})
    >>> (4, 2) in news['black']
    True
    >>> news['genmove']
    'white'
    >>> news['turn']
    'white'
    >>> referee.tell('genmove white', '= A2\n\n')
    >>> news = referee.notify_dictionary()

    If play a hidden stone to capture, immediately reveal.
    >>> news = referee.hide({'black': [(3, 3)]})
    >>> news.get('black', []).count( (3, 3) )
    1
    >>> news.get('assassin')
    True

    If ask more than once for same position, ignore duplicates.
    _why_not_play or hide:  referee busy until notify.
    Otherwise, black can issue two requests quickly, 
    which causes two moves to be replied.
    >>> referee.clear_board()
    >>> referee.ask( {'black': [[7, 7]]} )
    >>> referee.ask( {'black': [[7, 6]]} )
    referee._become_busy() # True
    {'busy': True}
    >>> referee.ask( {'black': [[7, 7]]} )
    referee._become_busy() # True
    {'busy': True}
    >>> referee.ask( {'black': [[7, 7]]} )
    referee._become_busy() # True
    {'busy': True}
    >>> referee.to_gtp({'black':  [(7, 7)]})
    ['play black H2']
    >>> referee.tell('play black H2', '= \n\n')
    >>> referee.to_gtp_list_stones()
    ['list_stones black', 'list_stones white']
    >>> referee.tell('list_stones black', '= H2\n\n')
    >>> referee.tell('list_stones white', '= \n\n')
    >>> code_unit.print_diff(
    ...     referee.ask( {'black': [[7, 7]]} ),
    ...     {'already_at': [(7, 7)]} )
    >>> news = referee.notify_dictionary()
    >>> news.get('genmove')
    'white'
    >>> news = referee.notify_dictionary()
    >>> news.get('genmove')
    
    If player asks for two different moves or more out of turn, 
    ignore second and the rest as out of turn.
    >>> referee.ask( {'black': [[8, 8]]} )
    {'turn_reminder': 'white'}
    >>> news = referee.notify_dictionary()
    >>> news.get('genmove')
    >>> referee.ask( {'black': [[7, 8]]} )
    {'turn_reminder': 'white'}
    >>> referee.tell('genmove white', '= G2\n\n')
    >>> news = referee.notify_dictionary()

    Already at reminder, takes precedence over out of turn.
    >>> referee.ask( {'black': [[7, 7]]} )
    {'already_at': [(7, 7)]}

    Log pass and go to next turn.
    >>> referee.tell('genmove white', '= PASS\n\n')
    >>> referee.moves[-1]
    'pass'
    >>> news = referee.notify_dictionary()
    >>> if not 'pass' in news:
    ...     print news
    >>> referee.tell('play black A2', '= \n\n')
    >>> news = referee.notify_dictionary()

    If timeout, then pass.
    >>> referee.tell('genmove white', 'timeout')
    referee.tell('genmove white', 'timeout')
    >>> referee.moves[-1]
    'pass'
    >>> news = referee.notify_dictionary()
    >>> if not 'pass' in news or 'timeout' not in news:
    ...     print news

    If list of stones times out, then do not update stones.
    >>> referee.tell('genmove white', 'timeout')
    referee.tell('genmove white', 'timeout')
    >>> referee.tell('list_stones black', 'timeout')
    referee.tell('list_stones black', 'timeout')
    >>> referee.tell('list_stones white', 'timeout')
    referee.tell('list_stones white', 'timeout')
    >>> news = referee.notify_dictionary()
    >>> if 'black' in news or 'white' in news:
    ...     print news

    TODO:  If both pass, start scoring.

    If undo a hide, then unhide that position.
    If undo an unhide, then do not rehide that position 
    because opponent has already seen it.

    '''
    def __init__(self):
        self.previous_stone_dictionary = {}
        self.stone_dictionary = {}
        self.previous_danger = []
        self.previous_warning = []
        self.now = {}
        self.news = {}
        self.present = {}
        self.news_time = 0
        self.board = copy.deepcopy(clear_board)
        self.previous_hidden = {}
        self.hidden = {}
        self.previous_turn = None
        self.turn = 'black'
        self.previous_genmove = None
        self.black = 'human'
        self.black_rank = get_rank(1)
        self.black_theme = 'cake_take'
        self.white = 'computer'
        self.white_rank = gnugo_rank
        self.white_theme = 'traditional'
        # XXX are users & white/black partially redundant or inconsistent?
        self.users = {
            'black':  {'user': '', 
                    'news':  {}, 'world':  new_world()},
            'white':  {'user': '',
                    'news':  {}, 'world':  new_world()},
            }
        self.world = new_world()
        self.you = ''
        self.moves = []
        self.move_colors = []
        self.verbose = False
        self.more = None
        self.history = []
        self.hide_gift = 0
        self.hide_max = 3
        self.extra_stone_black = 0
        self.extra_stone_gift = 0
        self.extra_stone_max = 1
        self.undo_gift = 1
        self.turns_in_a_row_max = 2
        ## self.set_level(get_level(self.black_rank))
        self = set_level(self, get_level(self.black_rank))
        self.secret_gifts = get_secret_gifts(
                self.white_rank - self.black_rank)
        self.gift_function = {
                'extra_stone_gift':  self._give_extra_stone,
                'hide_gift':  self._give_hide
                }
        self.previous_territory_labels = populate_board(None)
        self.ambassador = None

    def play_flash(self, client_request):
        '''Play a stone.  See undo_hide_example.'''
        if self.verbose:
            print 'referee.play_flash(', client_request, ')'
        client_request = dictionary_to_positions(
                client_request)
        color, move = get_first_move(client_request)
        if 'black' != color and 'white' != color:
            print 'referee.play_flash(', client_request, ') # I only accept black or white.'
        # verify user has authority to play this color
        owner = self.users[color].get('user')
        if not owner == client_request['user']:
            self.now['error'] = 'owner'
            return self.notify()
        if 'resign' == move or 'pass' == move:
            please_wait = self._wait_your_turn(color)
            if please_wait:
                return please_wait
            busy = self._become_busy()
            if busy:
                return busy
            self.you = color
            return self._pass_or_resign(color, move)
        else:
            row, column = move
            reason_not_to_play = self._why_not_play(color,
                    row, column)
            if reason_not_to_play:
                return reason_not_to_play
            busy = self._become_busy()
            if busy:
                return busy
            self.you = color
            return self._play_flash(color, row, column)

    def _pass_or_resign(self, color, move):
        self.history.append( {} )
        self.log_move(color, move)
        return self.notify()

    def _play_flash(self, color, row, column):
        '''permission must have been granted.'''
        self.history.append( {} )
        if 'black' == color:
            self._foretell_black_assassins(
                    eval(color), row, column)
        self._do_play(color, row, column)
        self._match_pattern(self.history[-1])
        if self._has_extra_stone_black(color):
            self.turn = 'black'
            # black needs to know they can move again.
            # self.now['turn'] = 'black'
            self.report('turn', 'black')
        return self.notify()

    def _match_pattern(self, last_event):
        '''Match, show, and reward a few good moves for black.'''
        last_color, last_row, last_column = \
                get_color_row_column(last_event)
        matches = get_matches(pattern_dictionary,
                self.board, last_row, last_column)
        for name, label in matches:
            label += '_mc'
            draw(self.now, name, (last_row, last_column, label) )
            if 'black' == last_color:
                self.undo_gift += 5
                if 25 < self.undo_gift:
                    self.undo_gift = 25
                self.now['undo_gift'] = self.undo_gift
        if matches:
            if 'black' == last_color:
                self._give_gift()

    def _foretell_black_assassins(self, mark, row, column):
        '''must reveal before _do_play.'''
        if not is_black(mark) and not is_white(mark):
            print 'referee._foretell_black_assassins(', mark, '...) # is not black or white'
        next_board = copy.deepcopy(self.board)
        next_board[row][column] = mark
        hidden = array_to_hidden(next_board)
        assassins = find_black_assassins(
                next_board, hidden, (row, column))
        if assassins:
            for row, column in assassins:
                self.board[row][column] = black
            self.now['assassin'] = True
            return assassins

    def _why_not_play(self, color, row, column):
        if 'none' != self.world['game_over']:
            self.now['error'] = self.world['game_over']
            return self.notify()
        if 'none' != self.world['glass']:
            self.now['error'] = self.world['glass']
            return self.notify()
        if 'black' != color and 'white' != color:
            print 'referee.play:  I only know how to play black or white, not', play_request
            self.now['error'] = 'play_color'
            return self.notify()  # TODO:  test this case
        occupied = self._occupied(color, row, column)
        if occupied:
            print 'referee._why_not_play(%s, %i, %i) # occupied %s' \
                    % (color, row, column, self.board[row][column])
            return occupied
        please_wait = self._wait_your_turn(color)
        if please_wait:
            return please_wait
        if is_suicide(self.board, color, row, column):
            return {'suicide':  [(row, column)],
                    'error':  'suicide'}
        # TODO ko

    def _do_play(self, color, row, column):
        '''Place stone and resolve standard Go capture
        and record the move.
        Does not consider variants like 'hide' or extra_stone
        or formation match.'''
        self.board[row][column] = eval(color)
        self.board = update_board(
                    self.board, (row, column))
        self.log_move(color, (row, column))

    def act_flash(self, client_request):
        '''Respond to undo.  See undo_hide_example.'''
        if 'more' in client_request:
            if self.more:
                return self.more()
            else:
                print 'referee.act_flash(', client_request, \
                        ') # no more'
        elif 'extra_stone_gift' in client_request:
            return self._extra_stone_black()
        elif 'showboard' in client_request:
            self._forget_previous()
            return self.notify()
        elif 'black' in client_request \
                or 'white' in client_request:
            return self.play_flash(client_request)
        elif 'undo' in client_request:
            return self.undo( client_request.get('undo') )
        elif 'genmove' in client_request:
            color = client_request['genmove']
            please_wait = self._wait_your_turn(color)
            if please_wait:
                return please_wait
            busy = self._become_busy()
            if busy:
                return busy
            self.you = opposite(color)
            self.history.append( {} )
            return
        elif 'load' in client_request:
            return self.load(client_request['load'])
        elif 'load_board' in client_request:
            return self.load_board(
                    eval(client_request['load_board']))
        elif 'glass' in client_request:
            return {'glass':  client_request['glass']}
        elif 'clear_board' in client_request:
            self.clear_board()
            ## self.clear_board()turn = 
            ##         client_request['clear_board'])
            return self.notify()
        elif 'watch' in client_request:
            ## return self.notify()
            return {}
        elif ['user'] == client_request.keys():
            busy = self._become_busy()
            if busy:
                return busy
            user = client_request['user']
            if self.users['black']['user'] == user:
                self.you = 'black'
            elif self.users['white']['user'] == user:
                self.you = 'white'
            else:
                if self.verbose:
                    print '''referee.act_flash:  you have no color
                    black:%s, white:%s, you:%s''' \
                        % (self.users['black']['user'], 
                            self.users['white']['user'], 
                            client_request)
            return self.notify()
        else:
            
            print 'referee.act_flash(', client_request, \
                    ') # I do not expect to be prepared for this request!'
            return self.notify()

    def load(self, file):
        self.history = []
        history = sgf_to_history(file)
        for event in history:
            news = self._turn_from_history(event)
        # ! missing last move.
        self._forget_previous()
        news = self.act_flash({'showboard':  True})
        # ! should not actually generate a move from white.  
        return news

    def _give_gift(self):
        '''Next gift.'''
        problems = ''
        for gift in self.secret_gifts:
            problem = self.gift_function[gift]()
            if not problem:
                self.secret_gifts.remove(gift)
                #print '_give_gift() # gave %s, left are %s' \
                #        % (gift, self.secret_gifts)
                #import pprint
                #pprint.pprint(self.__dict__) # debug
                break
            else:
                problems += '\n' + problem
        else:
            error = '_give_gift() # cannot give any of these %s, because %s' \
                    % (self.secret_gifts, problems)
            print error   # TODO example of this case.
            return error

    def _give_extra_stone(self):
        '''Next gift.  Similar to _give_hide.
        Must be performed after log_move?'''
        new_total = self.extra_stone_gift + 1
        if new_total <= self.extra_stone_max:
            self.extra_stone_gift += 1
            self.now['extra_stone_gift'] = '_%i' \
                    % self.extra_stone_gift
            self.now['help'] = 'extra_stone_gift'
        else:
            if black_turns_in_a_row(self.history) <= self.turns_in_a_row_max - 1:
                # use immediately for only one extra stone.
                # self.turn = 'black'
                # XXX blech, equivalent to self.turn = 'black'
                self.extra_stone_gift += 1
                self._use_extra_stone()
            else:
                error = 'referee._give_extra_stone:  cannot have %i extra_stone + gift because extra_stone_max is %i.' \
                    % (new_total, self.extra_stone_max)
                print error
                return error

    def _give_hide(self):
        '''Next hide gift.'''
        hidden_black = array_to_hidden(self.board).get('black', [])
        new_total = self.hide_gift + len(hidden_black) + 1
        if new_total <= self.hide_max:
            self.hide_gift += 1
            self.now['hide_gift'] = '_%i' % self.hide_gift
        else:
            error = 'referee._give_hide:  cannot have %i hide in play because hide_max is %i' \
                    % (new_total, self.hide_max)
            print error
            return error

    def _extra_stone_black(self):
        '''Black requests to start playing an extra stone.'''
        if self.extra_stone_gift <= 0:
            self.now['extra_stone_gift'] = '_%i' \
                    % self.extra_stone_gift
            return self.notify()
        please_wait = self._wait_your_turn('black')
        if please_wait:
            return please_wait
        busy = self._become_busy()
        if busy:
            return busy
        self.history.append( {} )
        self._use_extra_stone()
        return self.notify()

    def _use_extra_stone(self):
        '''already paid for'''
        self.extra_stone_gift -= 1
        self.extra_stone_black = 1
        # decremented once per extra turn.
        self.now['extra_stone'] = '_%i' % self.extra_stone_black
        self.now['extra_stone_gift'] = '_%i' % self.extra_stone_gift
        self.now['help'] = 'extra_stone'
        self.turn = 'black'
        
    def undo(self, count):
        'Undo to beginning of latest black turn.'
        if self.undo_gift <= 1:
            self.now['error'] = 'undo_gift'
            self.now['undo_gift'] = self.undo_gift
            return self.notify()
        please_wait = self._wait_your_turn('black')
        if please_wait:
            return please_wait
        if not self.history:
            self.now['error'] = 'history'
            return self.notify()
        busy = self._become_busy()
        if busy:
            return busy
        self.undo_gift -= 1
        if self.undo_gift < 1:
            self.undo_gift = 1
        self.now['undo_gift'] = self.undo_gift
        return self._undo_one(count)

    def undo_more(self, count):
        'okay for more, after first iteration of undo.'
        please_wait = self._black_turn_for_more('black')
        if please_wait:
            return please_wait
        busy = self._become_busy()
        if busy:
            return busy
        return self._undo_one(count)

    def _undo_one(self, count):
        'undo turn one by one'
        # remove placed stone
        ## present = self.history.pop()
        if not self.history:
            return self.notify()
        past = self.history.pop()
        for color in 'black', 'white':
            if past.get(color):
                move = past[color]
                if 'pass' != move and 'resign' != move:
                    row, column = move
                    if is_empty(self.board[row][column]):
                        print 'undo:  no stone here', row, column
                        pb(self.board)
                    # flash needs to unhide
                    #elif black_hidden == self.board[row][column]:
                    #    discard(self.previous_hidden, 'black', 
                    #            (row, column) )
                    self.board[row][column] = empty
                    # replace captured stone
                    if 'empty' in past:
                        if 'black' == color:
                            opponent_mark = white
                        elif 'white' == color:
                            opponent_mark = black
                        for captured_row, captured_column in past['empty']:
                            if not is_empty(self.board[captured_row][captured_column]):
                                print 'undo:  stone here', captured_row, captured_column
                                pb(self.board)
                            self.board[captured_row][captured_column] = opponent_mark
                break
        # else:
            # print 'undo:  no color for last turn!', past
            # return self.notify()
        self._redo_gifts(self.history)
        self._redo_territory(self.history)
        self._redo_last_move(self.history)
        self.now['score'] = self._revert_score(self.history)
        # notify but continue if more than once
        self.now['undo'] = count
        count -= 1
        if 'black' == color:
            count = 0
        else:
            count = 2
        if 1 <= count:
            # XXX if two people ask for more, first gets it.
            self.more = lambda:  self.undo_more(count)
            self.now['more'] = True
        else:
            self.more = None
            self.report('turn', 'black')
        return self.notify()

    def _redo_gifts(self, history):
        '''latest hide_gift, extra_stone_gift, extra_stone'''
        for event in history:
            if 'hide_gift' in event:
                hide_gift_news = event['hide_gift']
                self.now['hide_gift'] = hide_gift_news
                self.hide_gift = int(hide_gift_news.lstrip('_'))
            if 'extra_stone_gift' in event:
                extra_stone_gift_news = event['extra_stone_gift']
                self.now['extra_stone_gift'] = extra_stone_gift_news
                self.extra_stone_gift = int(extra_stone_gift_news.lstrip('_'))
        if history and 'extra_stone' in history[-1]:
            extra_stone_news = event['extra_stone']
            self.now['extra_stone'] = extra_stone_news
            self.extra_stone_black = int(extra_stone_news.lstrip('_'))

    def _redo_territory(self, history):
        '''latest territory news'''
        self.previous_territory_labels = populate_board(None)
        territory_labels = populate_board('neutral')
        old_territory_news = get_territory_news_deck(
            self.previous_territory_labels,
            territory_labels )
        for event in history:
            if 'territory' in event:
                territory_news = event['territory']
                # XXX can you show an example of undo territory news?
                old_territory_news = compile(
                        old_territory_news, territory_news)
        self.now['territory'] = old_territory_news
                
    def _redo_last_move(self, history):
        '''latest last_move news'''
        for event in history:
            for color in 'black', 'white':
                title = color + '_last_move'
                if title in event:
                    last_move_news = event[title]
                    self.now[title] = last_move_news

    def _revert_score(self, history):
        score = get_last(history, 'score')
        if not score:
            score = {'territory_txt':  '0',
                    'change_txt':  '0',
                    'change':  'neutral',
                    'frame':  40}
        return score

    def _turn_from_history(self, event):
        '''take a turn.  even if illegal.'''
        news = {}
        if 'extra_stone' in event:
            self._use_extra_stone()
        self._redo_gifts(self.history)
        self._redo_gifts([event])
        if 'black' in event:
            if 'hide' in event:
                news = self.hide_black({'black': event['hide']}) # ugly
            elif 'pass' == event['black'] or 'resign' == event['black']:
                self._pass_or_resign('black', event['black'])
            else:
                news = self._play_flash('black', *event['black'])
                ## news = self.act_flash({'black': [event['black']]}) # ugly
        if 'white' in event:
            news = self._genmove_white_mock(event['white'])
        if news:
            return news
        else:
            return self.notify(news)

    def hide_black(self, client_request):
        '''hide a stone on board.  See undo_hide_example.'''
        client_request = dictionary_to_positions(client_request)
        color, (row, column) = get_first_move(client_request)
        reason_not_to_hide = self._why_not_hide(
                color, row, column)
        if reason_not_to_hide:
            return reason_not_to_hide
        self.history.append( {} )
        assassins = self._foretell_black_assassins(
                black_hidden, row, column)
        self._do_play(color, row, column)
        if not assassins:
            # pay first, but be nice and do not take gift if wasted.
            self.hide_gift -= 1
            self.now['hide_gift'] = '_%i' % self.hide_gift
            self.board[row][column] = black_hidden
            # XXX overwritten by news _archive?
            if 1 <= len(self.history):
                self.history[-1] = draw(self.history[-1],
                        'hide', (row, column))
        self._match_pattern(self.history[-1])
        if self._has_extra_stone_black(color):
            # black needs to know they can move again.
            self.turn = 'black'
            self.report('turn', 'black')
        return self.notify()

    def _occupied(self, color, row, column):
        if 'black' == color:
            if black_hidden == self.board[row][column]:
                draw(self.now, 'hide', (row, column))
        elif 'white' == color:
            if black_hidden == self.board[row][column]:
                draw(self.now, 'unhide', (row, column))
            elif not is_empty(self.board[row][column]):
                self.now['error'] = 'already_at'
        if not is_empty(self.board[row][column]):
            draw(self.now, color, (row, column))
            self.now['already_at'] = [(row, column)]
            return self.notify()
        
    def _why_not_hide(self, color, row, column):
        if 'black' != color:
            print 'referee.hide:  I only know how to hide black, not', color
            self.now['error'] = 'hide_color'
            return self.notify()  # TODO:  test this case
        reason_not_to_play = self._why_not_play(
                color, row, column)
        if reason_not_to_play:
            return reason_not_to_play
        if self.hide_gift <= 0:
            print 'referee._why_not_hide:  cannot hide because hide_gift is %i' \
                    % (self.hide_gift)
            self.now['error'] = 'hide_gift'
            self.now['hide_gift'] = '_%i' % self.hide_gift
            return self.notify()
        busy = self._become_busy()
        if busy:
            return busy

    def _forget_previous(self):
        self.previous_stone_dictionary = {}
        self.previous_danger = []
        self.previous_warning = []
        self.previous_hidden = {}
        self.previous_turn = None
        self.previous_genmove = None
        self.previous_territory_labels = populate_board(None)
        self.now['star'] = star_positions
        self.now['clear_board'] = True
        
    def clear_board(self, turn = 'black'):
        self.previous_stone_dictionary = {}
        self.stone_dictionary = {}
        self.previous_danger = []
        self.previous_warning = []
        self.previous_hidden = {}
        self.hidden = {}
        self.turn = turn
        self.previous_turn = None
        self.previous_genmove = None
        self.history = []
        self.board = copy.deepcopy(clear_board)
        # XXX:  does this corrupt news? self.world = {}
        self.now = {}
        self.previous_territory_labels = populate_board(None)
        self.now['territory'] = get_territory_news_deck(
            self.previous_territory_labels,
            populate_board('neutral') )
        self.report('clear_board', True)
        self.report('game_over', 'none')
        self.report('turn', turn)
        self = set_level(self, get_level(self.black_rank))

    def report(self, about, article):
        self.world[about] = article
        self.now[about] = article
        self.users['white']['news'][about] = article
        self.users['black']['news'][about] = article

    def create(self, creator, level):
        busy = self._become_busy()
        if busy:
            return busy
        self.clear_board()
        self.report('root', 'table')
        self.report('game_over', 'setup')
        self.report('glass', 'block')
        self.you = 'white'
        #self.users['white']['news']['glass'] = 'block'
        #self.users['black']['news']['glass'] = 'block'
        self.white = 'human'
        self.users['white']['user'] = creator
        self.white_rank = get_rank(level)
        self.users['white']['creator'] = True
        return self.notify()

    def join(self, user, level):
        busy = self._become_busy()
        if busy:
            return busy
        if not self.users['black']['user']:
            rank = get_rank(level)
            if rank <= self.white_rank:
                self.black = 'human'
                self.users['black']['user'] = user
                self.black_rank = get_rank(level)
                self.black_theme = 'cake_take'
                self.you = 'black'
                self.users['black']['creator'] = False
                self.users['white']['creator'] = True
            else:
                self.black = self.white
                self.users['black']['user'] = self.users['white']['user']
                self.black_rank = self.white_rank
                self.black_theme = 'cake_take'
                self.users['black']['creator'] = True
                self.white = 'human'
                self.users['white']['user'] = user
                self.white_rank = get_rank(level)
                self.white_theme = 'traditional'
                self.users['white']['creator'] = False
                self.you = 'white'
            self.report('black_user_txt', self.users['black']['user'])
            #self.report('black_theme', self.black_theme)
            self.report('white_user_txt', self.users['white']['user'])
            #self.report('white_theme', self.white_theme)
            #self.users['black']['news']['black_user_txt'] = \
            #        self.users['black']['user']
            #self.users['black']['news']['white_user_txt'] = \
            #        self.users['white']['user']
            self.users['black']['news']['theme'] = \
                    self.black_theme
            #self.users['white']['news']['black_user_txt'] = \
            #        self.users['black']['user']
            #self.users['white']['news']['white_user_txt'] = \
            #        self.users['white']['user']
            self.users['white']['news']['theme'] = \
                    self.white_theme
            self.now['root'] = 'table'
        else:
            self.now['error'] = 'table_full'
        return self.notify()

    def start(self, user):
        busy = self._become_busy()
        if busy:
            return busy
        if self.users['black'].get('creator'):
            if not self.users['black']['user'] == user:
                self.now['error'] = 'creator_start'
                return self.notify()
        elif self.users['white'].get('creator'):
            if not self.users['white']['user'] == user:
                self.now['error'] = 'creator_start'
                return self.notify()
        else:
            self.now['error'] = 'creator_start'
            return self.notify()
        self.clear_board()
        self.report('glass', 'none')
        return self.notify()
            
    def stop(self, user, confirm = ''):
        if 'none' == self.world['game_over']:
            if 'confirm' != confirm:
                return {'confirm':  'stop_lose'}
        busy = self._become_busy()
        if busy:
            return busy
        self.report('glass', 'none')
        self.report('root', 'lobby')
        self.report('game_over', 'stop')
        return self.notify()
            
    def load_board(self, board_text, turn = None):
        '''Clear board and read a board.'''
        self.clear_board(turn)
        self.board = text_to_array(board_text)
        if turn:
            self.turn = turn
        return self.notify()

    def load_board_dictionary(self, board_text, turn = None):
        '''Clear board and read a board into dictionary.'''
        self.clear_board(turn)
        self.stone_dictionary, self.hidden \
                = text_to_stone_hidden(board_text)
        if turn:
            self.turn = turn
        
    def show_board(self):
        '''Return current board as text.'''
        return array_to_text(self.board)

    def show_board_dictionary(self):
        '''Return current board as text.'''
        return stone_hidden_to_text(self.stone_dictionary,
                self.hidden)
    
    def set_level(self, black_level):
        self = set_level(self, black_level)
        return self.notify()

    def configure(self, dictionary):
        '''Change a text property and confirm change.'''
        if self.verbose:
            print 'referee.configure:  ', dictionary
        for key, value in dictionary.items():
            exec( 'self.' + key + ' = "' + value + '"')
        return dictionary

    def ask(self, client_request):
        '''Before GTP, ask for client news.'''
        if self.verbose:
            import pprint
            print 'referee.ask(', \
                pprint.pformat(client_request), \
                ')'
        if 'black' in client_request \
                or 'white' in client_request:
            return self._why_not_play_dictionary(client_request)

    def hide(self, client_request):
        '''DEPRECATE dictionary.  hide_black instead.
        Hide a new black stone from GnuGo.'''
        if self.verbose:
            print 'referee.hide(', client_request, ')'
        client_request = dictionary_to_positions(client_request)
        if 'black' in client_request:
            color = 'black'
        else:
            print 'referee.hide:  I only know how to hide black, not', client_request
            self.now['error'] = 'hide_color'
            return self.notify_dictionary()  # TODO:  test this case
        please_wait = self.wait_your_turn(client_request)
        if please_wait:
            return please_wait
            return self.notify_dictionary()  # TODO:  test this case
        self.hidden = insert_stones(client_request, 
                self.hidden)
        assassins = self.find_black_assassins(client_request)
        if assassins:
            client_request = self.insert_black_assassins(
                    client_request)
            client_request['assassin'] = True
            return client_request
        else:
            color, move = get_first_move(client_request)
            self.log_move_lists(color, move)
            return self.notify_dictionary()

    def _do_play_dictionary(self, color, position):
        '''DEPRECATE.  _do_play instead.'''
        if 'pass' != position and 'resign' != position:
            self.stone_dictionary = insert_stones(
                    {color: [position]}, 
                    self.stone_dictionary)
        self.log_move_lists(color, position)

    def _why_not_play_dictionary(self, play_request):
        '''DEPRECATE.  _why_not_play instead.'''
        play_request = dictionary_to_positions(play_request)
        if 'black' in play_request:
            color = 'black'
        elif 'white' in play_request:
            color = 'white'
        else:
            print 'referee.play:  I only know how to play black or white, not', play_request
            self.now['error'] = 'play_color'
            return self.notify_dictionary()  # TODO:  test this case
        if hid_black_here_dictionary(self.hidden, play_request):
            return hid_black_here_dictionary(self.hidden, play_request)
        redundancies = already_at(self.stone_dictionary, 
                play_request)
        if redundancies:
            return {'already_at':  redundancies}
        please_wait = self.wait_your_turn(play_request)
        if please_wait:
            return please_wait

    def _wait_your_turn(self, color):
        #XXX undo_more hits error, 
        # and already check for more in act_flash
        # hide_black does not otherwise check more.
        if self.more:
            print 'referee._wait_your_turn(%s) # %s' \
                    % (color, 'self.more')
            return {'more': True}
        return self._black_turn_for_more(color)
            
    def _black_turn_for_more(self, color):
        if 'white' == self.turn:
            if 'black' == color:
                print 'referee._black_turn_for_more(%s) # %s' \
                        % (color, 'turn_reminder:  white')
                return {'turn_reminder': 'white'}
            
    def _become_busy(self):
        if self.now.get('busy'):
            print 'referee._become_busy() # %s' \
                    % self.now.get('busy')
            return {'busy': self.now.get('busy')}
        else:
            self.now['busy'] = True

    def wait_your_turn(self, play_request):
        '''DEPRECAte.  _wait_your_turn instead.'''
        color, move = get_first_move(play_request)
        if self._wait_your_turn(color):
            return self._wait_your_turn(color)
        return self._become_busy()
        
    def log_move(self, color, position):
        '''Record a move in Go.'''
        if 'pass' == position:
            self.now['pass'] = True
            if 2 <= len(self.history):
                if 'pass' == self.history[-2].get(opposite(color)):
                    self._score()
        if 'resign' == position:
            self.now['resign'] = True
            self._score(resign = True)
        if 'pass' != position and 'resign' != position:
            self.now[color + '_last_move'] = [position]
        self.history[-1][color] = position
        self.turn = next_turn(color)
        ## self.world['turn'] = self.turn
        self.report('turn', self.turn)

    def _score(self, resign = False):
        '''referee asks gnugo to score the game'''
        territory_score = None
        if resign:
            territory_score = 50
        if territory_score is None and self.ambassador:
            gnugo_komi = 5.5
            ## komi = self.ambassador.gtp('komi ' + str(gnugo_komi))
            # XXX sometimes with setup_score_example, 
            # gnugo loads at move 1 instead of last move,
            # whereas suffix 999 always loads to last move.
            # XXX sometimes GnuGo times out when asking for score.
            ## loadsgf = self.ambassador.gtp('loadsgf sgf/_update_gnugo.sgf 999')
            score_gtp = self.ambassador.gtp('final_score')
            score_text = score_gtp.lstrip('= ').rstrip('\n\n')
            if score_text.startswith(sgf_black):
                score_value_text = score_text.lstrip(
                        sgf_black + '+')
            elif score_text.startswith(sgf_white):
                score_value_text = '-' + score_text.lstrip(
                        sgf_white + '+')
            else:
                print 'referee._score:  what is this score_text? %s' % score_text
                print '    making up a score of 12 for now'
                score_value_text = '12'
            # XXX even when komi set to 0, in setup_score_example
            # sometimes gnugo seems to get stuck on 5.5 for white.
            territory_score = int(float(score_value_text) 
                    + gnugo_komi )
        extra_stone_score = 20 * self.extra_stone_gift
        hide_score = 10 * self.hide_gift
        undo_score = self.undo_gift / 2
        experience = extra_stone_score \
            + hide_score + undo_score \
            + max(territory_score, 0)
        if 1 <= territory_score:
            self.now['game_over'] = 'win'
        elif 0 == territory_score:
            self.now['game_over'] = 'draw'
            experience /= 3
        else:
            self.now['game_over'] = 'lose'
            experience /= 10
        score = {
            'experience_txt': '+' + str(experience),
            'territory_txt':  str(territory_score),
            'extra_stone_txt':  str(extra_stone_score),
            'hide_txt':  str(hide_score),
            'undo_txt':  str(undo_score),
                }
        self.now['score'] = score

    def _estimate_score(self, territory_values, history):
        territory_score = estimate_black_score(territory_values)
        frame = territory_score + 40
        if frame < 1:
            frame = 1
        elif 79 < frame:
            frame = 79
        old_score = 0
        last_score = get_last(history, 'score')
        if last_score:
            old_score = last_score.get('territory_txt')
            if old_score:
                old_score = int(float(old_score))
        change = territory_score - old_score
        if change <= -3:
            change_label = 'negative'
            change_txt = str(change)
        elif change == 0:
            change_label = 'neutral'
            change_txt = str(change)
        elif change <= 2:
            change_label = 'neutral'
            change_txt = '+%s' % (change)
        else:
            change_label = 'positive'
            change_txt = '+%s' % (change)
        score = self.now.get('score', {})
        score['territory_txt'] = str(territory_score)
        score['frame'] = frame
        score['change_txt'] = str(change)
        score['change'] = change_label
        return score

    def _has_extra_stone_black(self, color):
        'XXX if white plays a black stone:  false positive'
        if 'black' == color:
            if self.extra_stone_black <= 0:
                self.extra_stone_black = 0
                return False
            if self.turns_in_a_row_max <= black_turns_in_a_row(self.history):
                self.extra_stone_black = 0
                return False
            self.extra_stone_black = 0
            return True

    def log_move_lists(self, color, position):
        if 'pass' == position:
            self.now['pass'] = True
        else:
            pass
            #self.stone_dictionary = insert_stones(
            #        {color: [position]}, 
            #    self.stone_dictionary)
        self.move_colors.append(color)
        self.moves.append(position)
        self.turn = next_turn(color)
        
    def tell_play(self, gtp_command, gtp_response):
        if gtp_command.startswith('play black') \
                or gtp_command.startswith('play white'):
            if gtp_ok(gtp_response):
                play, color, stone = gtp_command.split(' ')
                position = gtp_to_array(stone)
                self.log_move_lists(color, position)
            else:
                print 'referee.tell_play:  gtp not happy', gtp_command, gtp_response.__repr__()
        else:
            print 'referee.play:  what play is this?  ', \
                    play_request

    def _does_avoid_collision(self, gtp_response):
        '''if colliding, avoid and reveal hidden black.'''
        move = gtp_to_move(gtp_response)
        if 'pass' != move and 'resign' != move:
            collision = get_collision_with_black(
                self.hidden, gtp_response)
            if collision:
                self.hidden = discard(self.hidden, 'black',
                        collision)
                gtp_coordinate = array_to_gtp(*collision)
                play_flash = 'play black ' + gtp_coordinate
                self.previous_genmove = None
                return ['undo', play_flash]

    def _genmove_white(self, gtp_command, gtp_response):
        '''Respond to a white move that GnuGo generated.
        Uses board, not dictionary.'''
        if not gtp_command.endswith('white'):
            print 'referee._genmove_white(', \
                    gtp_command, ',', gtp_response.__repr__(), \
                    ') #  I am only prepared to genmove white'
        play, color = gtp_command.split(' ')
        if not gtp_ok(gtp_response):
            move = 'pass'
            self.now['timeout'] = True
        else:
            move = gtp_to_move(gtp_response)
        if not self.now.get('timeout') and 'pass' == move:
            self.now['pass_white_mc'] = 'pass'
        if 'resign' == move or 'pass' == move:
            self.log_move(color, move)
            return ['initial_influence black territory_value']
        elif 2 != len(move):
            print 'referee._genmove_white("%s", "%s") # invalid move, so white will pass.' \
                    % ( gtp_command, gtp_response.__repr__())
            self.log_move(color, move)
            return ['initial_influence black territory_value']
        else:
            row, column = move
            if black_hidden == self.board[row][column]:
                # TODO How about remove now['genmove'] instead?
                self.previous_genmove = None
                self.board[row][column] = black
                #if 1 <= len(self.history):
                # XXX must merge unhide
                #self.history.append(
                #        {'unhide':  [(row, column)]})
                self.history[-1] = draw(self.history[-1], 
                        'unhide', (row, column))
                return ['genmove white']
            elif gtp_ok(gtp_response):
                play, color = gtp_command.split(' ')
                reason_not_to_play = self._why_not_play(
                        color, row, column)
                if reason_not_to_play:
                    print 'referee._genmove_white(%s, %s) # reason not to play:  %s' \
                        % ( gtp_command.__repr__(), 
                            gtp_response.__repr__(),
                            reason_not_to_play )
                    ## time_since_news = time.clock() - self.news_time
                    ## if time_since_news < 10:
                    if 'already_at' != reason_not_to_play.get('error'): 
                        # XXX if white plays out of turn:  infinite loop
                        return ['genmove white']
                    else:
                        print 'referee._genmove_white:  GnuGo or I am mistaken.  pass.  %s'  % ( self.__dict__ )
                        self.log_move(color, 'pass')
                        return ['initial_influence black territory_value']
                self._foretell_black_assassins(
                        eval(color), row, column)
                self._do_play(color, row, column)
                self._match_pattern(self.history[-1])
                #self._replay_turn_may_merge_unhide(self.history)
                return ['initial_influence black territory_value']
        
    def _set_territory_now(self, gtp_response):
        '''must call after _score if any.'''
        new_values = get_territory_values(gtp_response)
        if not self.now.get('game_over'):
            self.now['score'] = self._estimate_score(new_values,
                self.history)
        new_labels = get_territory_labels(new_values)
        self.now['territory'] = get_territory_news_deck(
                self.previous_territory_labels, 
                new_labels)
        self.previous_territory_labels = new_labels

    def _genmove_white_mock(referee, move):
        '''Force white to play.  
        Shortcut for examples without network.
        So does not talk to gnugo or get gnugo's score.
        >>> referee = referee_class()
        >>> news = referee._genmove_white_mock((0, 1))
        >>> news.get('white')
        [(0, 1)]
        >>> referee.board[0][1]
        'O'
        '''
        referee.act_flash({'genmove':  'white'})
        if 'pass' != move and 'resign' != move:
            row, column = move
            gtp_coordinate = array_to_gtp(row, column)
            gtp_response = '= %s\n\n' % gtp_coordinate
            referee.act_white_gtp('genmove white', gtp_response)
        else:
            gtp_response = '= %s\n\n' % move
            referee.act_white_gtp('genmove white', gtp_response)
        news = referee.notify()
        return news

    #obsolete
    #def _replay_turn_may_merge_unhide(self, history):
    #    'if unhide this turn, merge duplicate turn.'
    #    if 2 <= len(history):
    #        while 2 <= len(history) \
    #                and ['unhide'] == history[-2].keys():
    #            unhides = history.pop(-2)
    #            draw(history[-1], 'unhide', *unhides)

    def _genmove_white_dictionary(self, gtp_command, gtp_response):
        '''DEPRECATE dictionary
        Respond to a white move that GnuGo generated.'''
        if not gtp_command.endswith('white'):
            print 'referee._genmove_white_dictionary:  I am only prepared to genmove for white, not ', gtp_command
        if 'timeout' == gtp_response:
            gtp_response = '= PASS\n\n'
            self.now['timeout'] = True
        if '= resign\n\n' == gtp_response:
            self.now['resign'] = 'white'
            self.now['game_over'] = 'win'  
            # TODO:  example of black win, white lose, opposite news
        else:
            avoids_collision = self._does_avoid_collision(
                gtp_response)
            if avoids_collision:
                return avoids_collision
        if gtp_ok(gtp_response):
            play, color = gtp_command.split(' ')
            move = gtp_to_move(gtp_response)
            self._do_play_dictionary(color, move)
        else:
            print 'referee._genmove_white_dictionary:  gtp not happy', gtp_command, gtp_response.__repr__()

    def find_black_assassins(self, client_request):
        '''DEPRECATE.  Only find black assassins.
        won't have last move until play is made.
        won't have assassins until hidden are noted.
        '''
        board = get_board_union(
                copy.deepcopy(clear_board),
                self.stone_dictionary,
                client_request)
        color, move = get_first_move(client_request)
        #print doctest_board(board)
        #print 'self.hidden', self.hidden
        #print 'client_request', client_request
        #print 'move', move
        assassins = find_black_assassins(
                board, self.hidden, move)
        return assassins

    def insert_black_assassins(self, client_request):
        '''Only inserts black assassins.'''
        assassins = self.find_black_assassins(client_request)
        if assassins:
            #print 'assassins:  ', assassins
            self.hidden = discard(self.hidden, 'black',
                    *assassins)
            plays = []
            for assassin in assassins:
                if assassin not in client_request['black']:
                    plays.append(assassin)
            reveal_to_white = copy.deepcopy(
                    client_request)
            plays.extend(reveal_to_white['black'])
            reveal_to_white['black'] = plays
            self.now['assassin'] = True
            return reveal_to_white
        else:
            return client_request
     
    def to_gtp(self, client_request):
        '''Convert client request to list of gtp_commands.'''
        client_request = dictionary_to_positions(client_request)
        if 'black' in client_request or 'white' in client_request:
            client_request = self.insert_black_assassins(
                    client_request)
        return dictionary_to_gtp(client_request)
     
    def act_white_gtp(self, gtp_command, gtp_response):
        '''After talking to GnuGo, tell referee what was said.
        Does not use dictionary.  uses board.'''
        if self.verbose \
                or 'timeout' == gtp_response:
            print "referee.act_white_gtp('" + gtp_command \
                    + "', " + gtp_response.__repr__() + ")"
        if 'undo' == gtp_command:
            if gtp_ok(gtp_response):
                print 'referee.act_white_gtp:  did i already undo?'
        elif 'showboard' == gtp_command:
            if gtp_ok(gtp_response):
                self.clear_board()
        elif 'clear_board' == gtp_command:
            if gtp_ok(gtp_response):
                self.clear_board()
        elif gtp_command.startswith('loadsgf'):
            if gtp_ok(gtp_response):
                self.clear_board()
                self.turn = gtp_response_to_list(gtp_response)[0]
                # XXX If undo, turns may diverge.
        elif gtp_command.startswith('printsgf'):
            pass
        #elif gtp_command.startswith('play'):
        #    self._tell_play(gtp_command, gtp_response)
        elif gtp_command.startswith('genmove'):
            return self._genmove_white(
                    gtp_command, gtp_response)
        elif gtp_command.endswith('territory_value'):
            return self._set_territory_now(gtp_response)
        elif gtp_command.startswith('list_stones'):
            print 'referee.act_white_gtp(list_stones) # XXX deprecate list_stones?  referee manages stones'
            return self._list_stones(
                    gtp_command, gtp_response)
        else:
            print 'go_play:  Am I prepared to handle this gtp_command?  (%s, %s)' % (gtp_command, gtp_response)
   
    def tell(self, gtp_command, gtp_response):
        '''After talking to GnuGo, tell referee what was said.'''
        if self.verbose \
                or 'timeout' == gtp_response:
            print "referee.tell('" + gtp_command \
                    + "', " + gtp_response.__repr__() + ")"
        if 'undo' == gtp_command:
            if gtp_ok(gtp_response):
                self.move_colors = get_previous(
                        self.move_colors)
                self.moves = get_previous(self.moves)
        elif 'showboard' == gtp_command:
            if gtp_ok(gtp_response):
                self.clear_board()
        elif 'clear_board' == gtp_command:
            if gtp_ok(gtp_response):
                self.clear_board()
        elif gtp_command.startswith('loadsgf'):
            if gtp_ok(gtp_response):
                self.clear_board()
                self.turn = gtp_response_to_list(gtp_response)[0]
                # XXX If undo, turns may diverge.
        elif gtp_command.startswith('printsgf'):
            pass
        elif gtp_command.startswith('play'):
            self.tell_play(gtp_command, gtp_response)
        elif gtp_command.startswith('genmove'):
            return self._genmove_white_dictionary(gtp_command, gtp_response)
        elif gtp_command.startswith('list_stones'):
            return self.list_stones(gtp_command, gtp_response)
        else:
            print 'go_play:  Am I prepared to handle this gtp_command?  (%s, %s)' % (gtp_command, gtp_response)
   
    def to_gtp_list_stones(self):
        '''Done, now tell me your stones.'''
        gtp_commands = ['list_stones ' + color
                for color in 'black', 'white']
        return gtp_commands
        
    def list_stones(self, gtp_command, gtp_response):
        '''black or white stones, but not both.'''
        self.stone_dictionary = list_stones(
                gtp_command, gtp_response,
                self.stone_dictionary)

    def _update_board(self, color, last_move):
        ## XXX Sloppy
        #self.stone_dictionary = insert_stones(
        #            {color: [last_move]}, 
        #        self.stone_dictionary)
        #self.board = self._merge_board()
        #captured = find_capture(self.board, last_move)
        #self.board = map_at_position(mark_empty, 
        #        self.board, captured)
        # 
        self.board = update_board(self.board, last_move)
        # TODO:  Deprecate stone_dictionary and hidden for board.
        self.stone_dictionary = array_to_dictionary(
                self.board)
        self.hidden = array_to_hidden(self.board)
        return self.board

    def _merge_board(self):
        if self.hidden.has_key('black') \
                and self.hidden['black']:
            self.stone_dictionary = draw(
                self.stone_dictionary, 'black', 
                *self.hidden['black'])
        return get_board_union(
                copy.deepcopy(clear_board),
                self.stone_dictionary)

    def notify(self, news = None): 
        '''Notify using a board.'''
        if news is None:
            news = {}
        stones = array_to_dictionary(self.board)
        # if stones change, cannot these be added to 'now'?
        self.previous_stone_dictionary, news \
                = notify_stone(
                    self.previous_stone_dictionary,
                    stones, news)
        if 'black' in news:
            for user_data in self.users.values():
                user_data['news']['black'] = news['black']
        if 'white' in news:
            for user_data in self.users.values():
                user_data['news']['white'] = news['white']
        hidden = array_to_hidden(self.board)
        self.previous_hidden, news = notify_hidden(
                self.previous_hidden, hidden, news)
        self.previous_turn, news = notify_turn(
                self.previous_turn, self.turn, news)
        self.previous_genmove, news = notify_genmove(
                self.previous_genmove, self.turn,
                self.black, self.white, news)
        self.previous_danger, self.previous_warning, news \
                = notify_danger(self.board, 
                        self.previous_danger,
                        self.previous_warning,
                        news)
        self.present, news = self._predict_suicides(
                self.board, self.present, news)
        for user_name, user_data in self.users.items():
            user_data = notify_world(self.world, user_data)
        if self.you:
            you = self.users.get(self.you)
            news = notify_user(self.users, self.you, news)
            self.you = ''
        self.now, news = self.notify_toggles(self.now, news)
        # no changes to news during or after archiving
        if 'undo' not in news:
            self.history = self._archive(self.history, news)
        # self.present = copy.deepcopy(news)
        ## self.news_time = time.clock()
        if self.verbose:
            print self.show_board()
            print history_to_text(self.history)
            import pprint
            print 'referee.notify(', \
                pprint.pformat(news), ')'
            #print 'referee.history = ', \
            #    pprint.pformat(self.history)
        return news

    def _predict_suicides(self, board, present, news):
        for color in 'black', 'white':
            suicides = predict_suicides(board, color)
            if 'black' == color:
                story = 'suicide'
            elif 'white' == color:
                story = 'suicide_white'
            new_suicides = [suicide for suicide in suicides \
                if suicide not in present.get(story, [])]
            saved = [suicide for suicide \
                    in present.get(story, [])
                if suicide not in suicides]
            # must not alter during or after publishing
            if new_suicides:
                news[story] = new_suicides
                present[story] = suicides
            if not suicides and present.get(story):
                present.pop(story)
            end = story + '_end'
            if saved:
                self.now[end] = saved
                present[end] = saved
            if not saved and present.get(end):
                present.pop(end)
        return present, news

    def _archive(self, history, news):
        '''suspend during undo.
        if history archives news, and news includes undo, then
            is there an inconsistency?
        '''
        if 1 <= len(history):
            if 'hide' in news:
                history[-1]['hide'] = news['hide']
            if 'unhide' in news:
                history[-1]['unhide'] = news['unhide']
            if 'empty' in news:
                history[-1]['empty'] = news['empty']
            # gifts
            if 'hide_gift' in news:
                history[-1]['hide_gift'] = news['hide_gift']
            if 'extra_stone_gift' in news:
                history[-1]['extra_stone_gift'] = news['extra_stone_gift']
            if 'extra_stone' in news:
                history[-1]['extra_stone'] = news['extra_stone']
            if 'territory' in news:
                history[-1]['territory'] = news['territory']
            if 'black_last_move' in news:
                history[-1]['black_last_move'] = news['black_last_move']
            if 'white_last_move' in news:
                history[-1]['white_last_move'] = news['white_last_move']
            if 'score' in news:
                history[-1]['score'] = news['score']
        return history

    def notify_dictionary(self, news = None): 
        '''Must list_stones black + white before notify'''
        if not news:
            news = {}
        self.board = self._merge_board()
        self.previous_stone_dictionary, news \
                = notify_stone(
                    self.previous_stone_dictionary,
                    self.stone_dictionary, news)
        self.previous_turn, news = notify_turn(
                self.previous_turn, self.turn, news)
        self.previous_hidden, news = notify_hidden(
                self.previous_hidden, self.hidden, news)
        self.previous_genmove, news = notify_genmove(
                self.previous_genmove, self.turn,
                self.black, self.white, news)
        self.previous_danger, self.previous_warning, news \
                = notify_danger(self.board, 
                        self.previous_danger,
                        self.previous_warning,
                        news)
        self.now, news = self.notify_toggles(self.now, news)
        if self.verbose:
            print self.show_board_dictionary()
            import pprint
            print 'referee.notify_dictionary(', \
                pprint.pformat(news), ')'
        return news

    def notify_toggles(self, now, news):
        '''if true, notify and turn off.'''
        if now.get('busy'):
            now.pop('busy')
        news.update(now)
        return {}, news



def populate_board(mark, rows = 9, columns = 9):
    '''Each item of 2D array is a copy.
    >>> c = populate_board('c', 3, 2)
    >>> c[2][1] = 3
    >>> c
    [['c', 'c'], ['c', 'c'], ['c', 3]]

    a is distinct.
    >>> a = [[j] * 3 for j in ['a' for i in range(3)]]
    >>> a[2][1] = 1
    >>> a
    [['a', 'a', 'a'], ['a', 'a', 'a'], ['a', 1, 'a']]

    b is referenced.
    >>> b = [['b'] * 3] * 3
    >>> b[2][1] = 2
    >>> b
    [['b', 2, 'b'], ['b', 2, 'b'], ['b', 2, 'b']]
    '''
    return [[c] * columns 
            for c in [mark for m in range(rows)]]


def play_flash(self, client_request):
        '''Play a stone.  See undo_hide_example.  
        DOES not match pattern or notify.
        Made to setup_extra_stone_example before making pattern.'''
        if self.verbose:
            print 'referee.play_flash(', client_request, ')'
        client_request = dictionary_to_positions(
                client_request)
        color, position = get_first_move(client_request)
        row, column = position
        if 'black' != color:
            print 'referee.play_flash(', client_request, ') # I only accept black, because black is human and white speaks GTP.'
        #return self._play(color, row, column)
        #
        #    def _play(self, color, row, column):
        reason_not_to_play = self._why_not_play(color,
                row, column)
        if reason_not_to_play:
            return reason_not_to_play
        busy = self._become_busy()
        if busy:
            return busy
        self.you = color
        self.history.append( {} )
        self._foretell_black_assassins(eval(color), row, column)
        self._do_play(color, row, column)

def compile(old_news, news):
    '''Cards in hands are drawn and discarded.
    >>> a = {'a':[1, 2]}
    >>> b = {'a':[3], 'b':[4]}
    >>> ab = {'a':[1, 2, 3], 'b':[4]}
    >>> if not compile(a, b) == ab:   compile(a, b)
    >>> c = {'c': [3, 4]}
    >>> abc = {'a': [1, 2], 'c': [3, 4]}
    >>> ab = compile(a, b)
    >>> if not compile(ab, c) == abc:   compile(ab, c)
    '''
    old = copy.deepcopy(old_news)
    new = copy.deepcopy(news)
    for volume, issues in new.items():
        for issue in issues:
            for old_volume, old_issues in old.items():
                if issue in old_issues:
                    discard(old, old_volume, issue)
    for volume, issues in new.items():
        old = draw(old, volume, *issues)
    new = old
    return new


def get_territory_news_deck(old_labels, new_labels):
    '''
    >>> old_values = get_territory_values(wallis_territory_text)
    >>> old_labels = get_territory_labels(old_values)
    >>> new_values = get_territory_values(wallis_territory2_text)
    >>> new_labels = get_territory_labels(new_values)
    >>> get_territory_news_deck(old_labels, new_labels)
    {'white': [(5, 6), (5, 7), (6, 6), (7, 6)], 'neutral': [(8, 6)]}
    >>> import pdb; pdb.set_trace(); get_territory_news_deck([[], []], [['dead'],['black']])
    {'dead': [(1, 0)], 'black': [(1, 1)]}
    '''
    from deck import draw
    territory_now = {}
    simulcast = zip(enumerate(old_labels), new_labels)
    for (r, old_row), new_row in simulcast:
        simultaneous = zip(enumerate(old_row), new_row)
        for (c, old_label), new_label in simultaneous:
            if old_label != new_label:
                draw(territory_now, new_label, (r, c))
    return territory_now
    




# Functional programming on board

def do_at(do_this, grid, positions):
    '''
    >>> def p(i):  return i
    >>> do_at(p, clear_board, [(0, 0)])
    [',']
    '''
    return [do_this(grid[row][column]) 
        for row, column in positions]


def do_at_this_way(do_this, grid, positions, this_way):
    '''
    >>> def p(i, n):  return i * n
    >>> do_at_this_way(p, clear_board, [(0, 0)], 3)
    [',,,']
    '''
    return [do_this(grid[row][column], this_way)
        for row, column in positions]


def do_at_these_ways(do_this, grid, positions, *these_ways):
    '''
    >>> def p(i, n, m):  return i * n * m
    >>> do_at_these_ways(p, clear_board, [(0, 0)], 3, 2)
    [',,,,,,']
    '''
    return [do_this(grid[row][column], *these_ways)
        for row, column in positions]


def map_grid(do_this_at, grid):
    '''
    >>> map_grid(lambda i, r, c:  False, clear_board)[0][0]
    False
    >>> map_grid(lambda i, r, c:  False, clear_board)[0][1]
    False
    '''
    mapped = copy.deepcopy(grid)
    for row in range(len(grid)):
        for column in range(len(grid[row])):
            mapped[row][column] = do_this_at(grid[row][column], row, column)
    return mapped



def get_positions(board, is_true):
    '''Get positions that are true.
    >>> get_positions(hidden_board, is_black_hidden)
    [(2, 1)]
    '''
    positions = []
    for row in range(len(board)):
        for column in range(len(board[row])):
            if is_true(board[row][column]):
                positions.append( (row, column) )
    return positions


def make_mask(grid, positions):
    '''
    >>> mask = make_mask(clear_board, [(0, 0)])
    >>> mask[0][0]
    True
    >>> mask[0][1]
    False
    '''
    def mark_true(item):
        return True
    mask = map_grid(lambda i, r, c:  False, grid)
    mask = map_at_position(mark_true, mask, positions)
    return mask


def respond_at(response, trigger_key, action, grid):
    '''
    >>> respond_at({'warn': [(2, 2)], 'danger': [(0, 0)]}, 'warn', lambda i:  ('warning', i), clear_board)
    [('warning', ',')]
    '''
    if response.has_key(trigger_key):
        if response[trigger_key]:
            return do_at(action, grid, response[trigger_key])


def respond_at_this_way(response, trigger_key, 
        action, grid, this_way):
    '''
    >>> respond_at_this_way({'warn': [(2, 2)], 'danger': [(0, 0)]}, 'warn', lambda i, j:  (j, i), clear_board, 'warning')
    [('warning', ',')]
    '''
    if response.has_key(trigger_key):
        if response[trigger_key]:
            return do_at_this_way(action, grid, response[trigger_key], 
                    this_way)



#
# Smart Go Format (SGF)
# Update GnuGo by saving and loading SGF.
#


def undo_hide_sgf_example():
    r'''
    >>> code_unit.inline_examples(
    ...     setup_undo_hide_example2.__doc__,
    ...     locals(), globals())
    >>> print referee.show_board()
    O/,,,,,,,
    O/,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    >>> referee.history
    [{'hide': [(0, 1)], 'black': (0, 1)}, {'white': (0, 0)}, {'hide': [(1, 1)], 'black': (1, 1)}, {'white': (1, 0)}]
    >>> print get_sgf_tree(referee.history)
    (;GM[1]SZ[9];MA[ba];W[aa];MA[bb];W[ab])
    '''



def read_sgf_example():
    '''SGF
    >>> code_unit.inline_examples(
    ...     extra_stone_example.__doc__,
    ...     locals(), globals())
    >>> print history_to_text(referee.history)
      0 1 2 3 4 5 6 7 8 
    0 . . . . . . . . . 
    1 . X6. X4. . . . . 
    2 . . . . X2. X0. . 
    3 . . O5. . . . . . 
    4 . . . . O3X7. . . 
    5 . . O1. . . . . . 
    6 . . . . XbO8Xa. . 
    7 . Oc. . . . . . . 
    8 . . . . . . . . . 
    >>> sgf_tree = get_sgf_tree(referee.history)
    >>> import text
    >>> text.save('sgf/read_sgf_example.sgf', str(sgf_tree))
    >>> referee.history = []
    >>> print history_to_text(referee.history)
      0 1 2 3 4 5 6 7 8 
    0 . . . . . . . . . 
    1 . . . . . . . . . 
    2 . . . . . . . . . 
    3 . . . . . . . . . 
    4 . . . . . . . . . 
    5 . . . . . . . . . 
    6 . . . . . . . . . 
    7 . . . . . . . . . 
    8 . . . . . . . . . 
    >>> text_sgf_tree = text.load('sgf/read_sgf_example.sgf')
    >>> referee.history = get_history(parse(text_sgf_tree))
    >>> print history_to_text(referee.history)
      0 1 2 3 4 5 6 7 8 
    0 . . . . . . . . . 
    1 . X6. X4. . . . . 
    2 . . . . X2. X0. . 
    3 . . O5. . . . . . 
    4 . . . . O3X7. . . 
    5 . . O1. . . . . . 
    6 . . . . XbO8Xa. . 
    7 . Oc. . . . . . . 
    8 . . . . . . . . . 
    '''

def suicide_example():
    '''Cannot play at suicide.
    >>> referee = referee_class()
    >>> referee.board = suicide_board
    >>> news = referee.act_flash({'black':  [(0, 8)]})
    >>> news.get('black')
    >>> news.get('suicide')
    [(0, 8)]
    >>> news.get('error')
    'suicide'

    After any successful move, referee predicts suicides.
    This is technically the first turn, so suicide news
    is published this turn.
    >>> news = referee.act_flash({'black':  [(6, 0)]})
    >>> if not (6, 0) in news.get('black'):  news
    >>> suicide_mask = news.get('suicide')
    >>> print text_mask(suicide_mask)
    ,,,,,,,,#
    ,,,,,,#,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    >>> suicide_mask
    [(0, 8), (1, 6)]

    Show suicides for white as a safe place for black.
    >>> suicide_white_mask = news.get('suicide_white')
    >>> print text_mask(suicide_white_mask)
    #,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    
    >>> news = referee._genmove_white_mock((1, 1))

    Flash shows each suicide to the user 
    as a cake with bite marks in all four sides.

    When suicide ends, referee notifies Flash.
    Flash removes the suicide mark.
    >>> news = referee.act_flash({'black':  [(6, 1)]})

    After white moves, referee predicts suicides.
    >>> news = referee._genmove_white_mock((1, 6))
    >>> news.get('suicide')
    >>> news.get('suicide_end')
    [(0, 8), (1, 6)]

    On undo, referee reverts suicide mask.
    >>> referee.undo_gift = 25
    >>> news = referee.act_flash({'undo':  2})
    >>> suicide_mask = news.get('suicide')
    >>> if not suicide_mask == [(0, 8), (1, 6)]:
    ...     predict_suicides(referee.board, 'black')
    ...     referee.present.get('suicide')
    ...     suicide_mask
    >>> news.get('suicide_white')
    [(0, 0)]
    >>> news = referee.act_flash({'more':  True})

    #>>> suicide_mask = news.get('suicide')
    #>>> if not suicide_mask == [(0, 8), (1, 6)]:
    ...     predict_suicides(referee.board, 'black')
    ...     referee.present.get('suicide')
    ...     suicide_mask
    #>>> news.get('suicide_white')
    [(0, 0)]
    >>> news = referee.act_flash({'black':  [(6, 1)]})

    When white ends suicide, referee notifies Flash.
    >>> news = referee._genmove_white_mock((0, 2))
    >>> news.get('suicide_white')
    >>> news.get('suicide_white_end')
    [(0, 0)]

    Suicide is like complete block on an empty location.
    Suicide can never be at same location as block of stone.
    Therefore Flash can reuse warning/danger block indicator,
    to show that an empty position is completely blocked.
    '''

def goto_history_example():
    '''Travel forward and backward in history.
    >>> code_unit.inline_examples(
    ...     read_sgf_example.__doc__,
    ...     locals(), globals())
    >>> referee.goto(0)
    >>> print history_to_text(referee.history)
      0 1 2 3 4 5 6 7 8 
    0 . . . . . . . . . 
    1 . . . . . . . . . 
    2 . . . . . . . . . 
    3 . . . . . . . . . 
    4 . . . . . . . . . 
    5 . . . . . . . . . 
    6 . . . . . . . . . 
    7 . . . . . . . . . 
    8 . . . . . . . . . 
    >>> referee.extra_stone_gift
    0
    >>> referee.goto(5)
    >>> print history_to_text(referee.history)
      0 1 2 3 4 5 6 7 8 
    0 . . . . . . . . . 
    1 . . . X4. . . . . 
    2 . . . . X2. X0. . 
    3 . . . . . . . . . 
    4 . . . . O3. . . . 
    5 . . O1. . . . . . 
    6 . . . . . . . . . 
    7 . . . . . . . . . 
    8 . . . . . . . . . 
    
    In addition to moves, also recreate gifts.
    >>> referee.extra_stone_gift
    1
    '''



from smart_go_format import *


def get_last(history, label):
    '''Latest event in history with this label.
    '''
    # more elegant way to go through list in reverse?
    backwards = copy.deepcopy(history)
    backwards.reverse()
    for event in backwards:
        score = event.get(label)
        if score:
            return score

many_turns_in_a_row_history = [{'black': (6, 6), 'extra_stone_gift': '_1', 'black_last_move': [(6, 6)]}, {u'white': (3, 3), 'territory': {'neutral': [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (0, 8), (1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8), (2, 0), (2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (2, 6), (2, 7), (2, 8), (3, 0), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (3, 6), (3, 7), (3, 8), (4, 0), (4, 1), (4, 2), (4, 3), (4, 4), (4, 5), (4, 6), (4, 7), (4, 8), (5, 0), (5, 1), (5, 2), (5, 3), (5, 4), (5, 5), (5, 6), (5, 7), (5, 8), (6, 0), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5), (6, 6), (7, 0), (7, 1), (7, 2), (7, 3), (7, 4), (7, 5), (8, 0), (8, 1), (8, 2), (8, 3), (8, 4), (8, 5)], 'black': [(6, 7), (6, 8), (7, 6), (7, 7), (7, 8), (8, 6), (8, 7), (8, 8)]}, 'white_last_move': [(3, 3)]}, {'extra_stone': '_1', 'extra_stone_gift': '_0'}, {'black': (2, 6), 'extra_stone_gift': '_1', 'black_last_move': [(2, 6)]}, {'extra_stone': '_1', 'extra_stone_gift': '_0'}, {'black': (6, 2), 'extra_stone_gift': '_1', 'black_last_move': [(6, 2)]}, {'extra_stone': '_1', 'extra_stone_gift': '_0'}, {'black': (4, 6), 'extra_stone_gift': '_1', 'black_last_move': [(4, 6)]}, {'extra_stone': '_1', 'extra_stone_gift': '_0'}, {'black': (4, 4), 'extra_stone_gift': '_1', 'black_last_move': [(4, 4)]}, {'extra_stone': '_1', 'extra_stone_gift': '_0'}, {'black': (6, 4), 'extra_stone_gift': '_1', 'black_last_move': [(6, 4)]}, {'extra_stone': '_1', 'extra_stone_gift': '_0'}, {'black': (4, 2), 'extra_stone_gift': '_1', 'black_last_move': [(4, 2)]}, {'extra_stone': '_1', 'extra_stone_gift': '_0'}, {'black': (2, 2), 'extra_stone_gift': '_1', 'black_last_move': [(2, 2)]}, {'extra_stone': '_1', 'black': (2, 4), 'extra_stone_gift': '_1', 'black_last_move': [(2, 4)]}, {'extra_stone': '_1', 'black': (3, 7), 'extra_stone_gift': '_1', 'black_last_move': [(3, 7)]}, {'black': (5, 7), 'black_last_move': [(5, 7)]}]

def black_turns_in_a_row(history):
    '''Number of turns is taking in a row.
    >>> black_turns_in_a_row([])
    0
    >>> black_turns_in_a_row([{'black':  (0, 0)}])
    1
    >>> black_turns_in_a_row([{'black':  (0, 0)}, {'white':  (0, 1)}])
    0
    >>> black_turns_in_a_row([{'black':  (0, 0)}, {'black':  (1, 0)}, {'white':  (0, 1)}, {'black':  (2, 0)}])
    1
    >>> black_turns_in_a_row([{'black':  (0, 0)}, {'black':  (1, 0)}, {'white':  (0, 1)}, {'black':  (2, 0)}, {'black':  (3, 0)}])
    2
    >>> black_turns_in_a_row(many_turns_in_a_row_history)
    10
    '''
    turns_in_a_row = 0
    backwards = copy.deepcopy(history)
    backwards.reverse()
    for event in backwards:
        if 'black' in event:
            turns_in_a_row += 1
        elif 'white' in event:
            break
    return turns_in_a_row


from pattern import *

#no example
#def invert_colors(pattern):
#    '''White to black, and black to white.
#    >>> invert_colors(['?O?', '...', '.*.', '?.?'])
#    [['?', 'X', '?'], ['.', '.', '.'], ['.', '*', '.'], ['?', '.', '?']]
#    '''
#    black_pattern = []
#    for row in pattern:
#        black_pattern.append( [] )
#        for pattern_mark in row:
#            if is_white(pattern_mark):
#                black_pattern[-1].append(black)
#            elif is_black(pattern_mark):
#                black_pattern[-1].append(white)
#            else:
#                black_pattern[-1].append(pattern_mark)
#    


# Flash Client

required_dictionary = {
        'error':  ['undo_gift'],
        'extra_stone_gift':  ['_0', '_1'],
        #'formation_jump':  ['response'],
        # 'formation_jump_response':  ['response'],
        'game_over':  ['none', 'win', 'lose', 'draw'],
        'glass':  ['none', 'block'],
        'help':  ['first_move', 'extra_stone_gift', 'extra_stone'],
        'hide_gift':  ['_0', '_1', '_2', '_3'],
        'pass_white_mc':  ['none', 'pass'],
        'undo_gift':  [1, 25],
        # XXX each intersection is different
        # 'territory':  ['neutral', 'dead', 'black', 'white'],
    }


def validate(mc_dictionary, 
        required_dictionary = required_dictionary,
        verbose = False):
    '''Which required labels are missing?
    >>> validate({'game_over': ['none', 'win']}, {'game_over': ['none', 'win']}, verbose = True)
    validate( {'game_over': ['none', 'win']} )
    {}
    >>> validate({'game_over': ['none', 'win', 'lose']}, {'game_over': ['none', 'win']}, verbose = True)
    validate( {'game_over': ['none', 'win', 'lose']} )
    {}
    >>> validate({'game_over': ['none', 'lose']}, {'game_over': ['none', 'win']}, verbose = True)
    validate( {'game_over': ['none', 'lose']} )
    validate missing:  {'game_over': ['win']}
    {'game_over': ['win']}
    '''
    if verbose:
        print 'validate(', mc_dictionary, ')'
    missing = {}
    for title, necessary_labels in required_dictionary.items():
        labels = mc_dictionary.get(title, [])
        for necessary in necessary_labels:
            if necessary not in labels:
                draw(missing, title, necessary)
    if missing:
        print 'validate missing: ', missing
    return missing


critical_board_text = '''
,,,,,,,,,
,,,,,,,,,
,,,,,,,,,
,,,,,,,,,
,,,,,,,,,
,,,,,,,,,
OOOO,,,,,
XXXXO,,,,
,X,X,,,,,
'''
critical_board = text_to_array(critical_board_text)

def update_history_and_critical_news(play_history, board, color, row, column):
        # intersection_mc_array, intersection_mc):
    '''
	find neighbors beside white's last play.  
    convert history to sgf.  
    for neighbors, show gnugo sgf, and ask gnugo for dragon status.  
    if critical, convert all blocks to danger.
    notify black.
    '''
    sgf_file = 'sgf/_dragon_status.sgf'
    # row, column = get_row_column(intersection_mc.name)
    play_history.append({})
    play_history[-1][color] = row, column
    smart_go_format.save_sgf(play_history, sgf_file)
    #board_text = flash_to_text(intersection_mc_array)
    #board = referee.text_to_array(board_text)
    attackers = referee.find_attacker(board, row, column)
    go_text_protocol.get_attacker_critical_coordinates(sgf_file, attackers)
    news = set_block_news(coordinates, 'danger')
    return play_history, news

import code_unit

snippet = '''
import referee; referee = reload(referee); from referee import *
'''

if __name__ == '__main__':
    import sys
    code_unit.test_file_args('./referee.py', sys.argv,
            locals(), globals())

