#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Manipulate a text and array board of Go.
'''
__author__ = 'Ethan Kennerly'


# doctest abhors '...'
empty = ','
empty_black = ','
empty_white = ','
question_black = '%'
question_hide_black = ']'
empty_characters = empty + '.+' \
        + empty_black + empty_white \
        + question_black + question_hide_black
preview_black = '$'
play_black = '*'
black = 'X'
preview_hide_black = '['
play_hide_black = '|'
black_hidden = '/'  # opponent does not know black is here
# XXX exclude question_* because this would cause questions to be played.
black_hidden_characters = preview_hide_black + play_hide_black + black_hidden
black_characters = black + black_hidden + preview_black + play_black + preview_hide_black + question_hide_black + play_hide_black

white = 'O'
play_white = '@'
white_characters = white + play_white
#- row_count = 9
#- column_count = 9
off_board = '#'

board_text = '''
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

def text_to_lines(board_text):
    r'''
    >>> board_lines = text_to_lines(board_text)
    >>> board_lines[2]
    'OOOOO,,,,'
    >>> board_lines[1][2]
    'O'
    >>> board_lines[0][2]
    ','
    >>> len(board_lines)
    9
    >>> len(board_lines[2])
    9
    >>> board_lines[3][3]
    'X'
    '''
    board_lines = board_text.replace(' ', '').split('\n')
    while '' in board_lines:
        board_lines.remove('')
    return board_lines

board_lines = text_to_lines(board_text)

def text_to_array(board_text):
    '''2D text array of the board.
    >>> text_to_array(clear_board_text)[0]
    [',', ',', ',', ',', ',', ',', ',', ',', ',']
    '''
    lines = text_to_lines(board_text)
    array = []
    for line in lines:
        array.append([])
        for character in line:
            array[-1].append(character)
    return array

clear_board_text = '''
,,,,,,,,,
,,,,,,,,,
,,,,,,,,,
,,,,,,,,,
,,,,,,,,,
,,,,,,,,,
,,,,,,,,,
,,,,,,,,,
,,,,,,,,,
'''
clear_board = text_to_array(clear_board_text)

clear_board_5_5_text = '''
,,,,,
,,,,,
,,,,,
,,,,,
,,,,,
'''
clear_board_5_5 = text_to_array(clear_board_5_5_text)
clear_board_3_3 = text_to_array('''
,,,
,,,
,,,
''')


score_white_by_18_board_text = '''
,,XOO,,,,
,,,XOO,,,
,,X,XO,,,
,,,XXO,,,
,,XXO,,,,
,,,XO,,,,
,XXOO,O,,
XXOO,,,,,
XOO,,,,,,
'''
score_white_by_18_board = text_to_array(
        score_white_by_18_board_text)


score_black_by_14_board_text = '''
,,XXXO,,,
,,XOXOOO,
,,XOOO,O,
,,XOO,,,O
,,XO,OO,,
,,XOOXOOO
,,XXXXXXX
,,,,,,,,,
,,,,,,,,,
'''
score_black_by_14_board = text_to_array(
        score_black_by_14_board_text)

adjacent = [
            (-1, 0),
    (0, -1),            (0, 1),
            (1, 0)]


# query single intersection

def is_empty(cell):
    '''Common GTP/GnuGo/DragonGo empty characters.
    >>> is_empty('.')
    True
    >>> is_empty(',')
    True
    >>> is_empty('+')
    True
    >>> is_empty('/')
    False
    >>> is_empty('O')
    False
    >>> is_empty('X')
    False
    >>> is_empty('')
    False
    >>> is_empty(' ')
    False
    '''
    return len(cell) == 1 \
            and cell in empty_characters \
            and cell != ''

def see_same_color(cell):
    '''Return function that sees for same color as cell.
    >>> is_color = see_same_color('X')
    >>> is_color('O')
    False
    >>> is_color('$')
    True
    >>> is_color = see_same_color('.')
    see_same_color:  what color is "."?
    '''
    if is_black(cell):
        return is_black
    if is_white(cell):
        return is_white
    print 'see_same_color:  what color is "%s"?' % cell
    return None


def is_black(cell):
    '''
    >>> is_black('X')
    True

    XXX exclude question_* because this would cause questions to be played.
    >>> is_black('%')
    False
    '''
    return len(cell) == 1 \
            and cell in black_characters \
            and cell != ''


def is_white(cell):
    '''
    >>> is_white('O')
    True
    >>> is_white('@')
    True
    '''
    return len(cell) == 1 \
            and cell in white_characters \
            and cell != ''


def is_occupied(cell):
    '''
    >>> is_occupied('X')
    True
    >>> is_occupied('O')
    True
    >>> is_occupied(',')
    False
    '''
    return is_black(cell) or is_white(cell)

def get_color(cell):
    '''
    >>> get_color('X')
    'black'
    >>> get_color('$')
    'black'
    >>> get_color('.')
    'empty'
    >>> get_color('@')
    'white'
    '''
    if is_black(cell):
        return 'black'
    if is_white(cell):
        return 'white'
    else:
        return 'empty'

def opposite(color):
    '''
    >>> opposite('white')
    'black'
    '''
    if 'black' == color:
        return 'white'
    elif 'white' == color:
        return 'black'
    else:
        print 'other_color:  black or white not %s' % color
        

def is_on_board(mark):
    return is_white(mark) or is_black(mark) or is_empty(mark)

def always_false(mark):
    '''
    >>> always_false('.')
    False
    '''
    return False


def label_to_mark(label):
    '''
    >>> label_to_mark('empty_white')
    ','
    >>> label_to_mark('white')
    'O'
    >>> label_to_mark('square')
    label_to_mark:  what is this? 'square'
    '!'
    >>> label_to_mark('question_black_repeat')
    '%'
    '''
    # XXX dictionary?
    if label.startswith('empty'):
        board_mark = empty
    elif 'black' == label:
        board_mark = black
    elif 'white' == label:
        board_mark = white
    elif 'play_black' == label:
        board_mark = play_black
    elif 'play_white' == label:
        board_mark = play_white
    elif 'hide_black' == label:
        board_mark = black_hidden
    elif label.startswith('preview_black'):
        board_mark = preview_black
    elif label.startswith('question_black'):
        board_mark = question_black
    elif label.startswith('preview_hide_black'):
        board_mark = preview_hide_black
    elif label.startswith('question_hide_black'):
        board_mark = question_hide_black
    elif label.startswith('play_hide_black'):
        board_mark = play_hide_black
    else:
        what_is_this = "label_to_mark:  what is this? '%s'" % label
        #logging.error(what_is_this)
        print what_is_this
        board_mark = '!'
    return board_mark




# compare two intersections

def same(me, you):
    r'''Same color or both empty or both off board.
    >>> same('/', 'X')
    True
    >>> same('.', ',')
    True
    >>> same('.', 'X')
    False
    >>> same('O', 'X')
    False
    '''
    if is_black(me) and is_black(you):
        return True
    elif is_white(me) and is_white(you):
        return True
    elif is_empty(me) and is_empty(you):
        return True
    else:
        return False

def identical(me, you):
    r'''Exactly the same.
    >>> identical('/', 'X')
    False
    >>> identical('.', ',')
    False
    >>> identical('.', 'X')
    False
    >>> identical('O', 'X')
    False
    >>> identical('X', 'X')
    True
    '''
    return me == you

def ally(me, you):
    r'''Are these stones the same color?
    >>> ally('/', 'X')
    True
    >>> ally('.', ',')
    False
    >>> ally('.', 'X')
    False
    >>> ally('O', 'X')
    False
    >>> ally(white, play_white)
    True
    >>> ally(white, play_black)
    False
    '''
    if is_black(me) and is_black(you):
        return True
    elif is_white(me) and is_white(you):
        return True
    else:
        return False

def enemy(me, you):
    r'''Are these stones different colors?
    >>> enemy('/', 'X')
    False
    >>> enemy('.', ',')
    False
    >>> enemy('.', 'X')
    False
    >>> enemy('O', 'X')
    True
    >>> enemy('O', '/')
    True
    >>> enemy(white, play_white)
    False
    >>> enemy(white, play_black)
    True
    '''
    if is_black(me) and is_white(you):
        return True
    elif is_white(me) and is_black(you):
        return True
    else:
        return False
   
def are_we_on_board(me, you):
    return is_on_board(me) and is_on_board(you)

def is_off_board(mark):
    return mark == off_board

def am_i_off_board_but_not_you(me, you):
    '''
    >>> am_i_off_board_but_not_you('#', '*')
    True
    >>> am_i_off_board_but_not_you('#', '#')
    False
    >>> am_i_off_board_but_not_you('.', '*')
    False
    >>> am_i_off_board_but_not_you('*', '#')
    False
    '''
    return is_off_board(me) and is_on_board(you)

def am_i_empty_but_not_you(me, you):
    return is_empty(me) and not is_empty(you)

def ally_or_empty(me, you):
    r'''Are these stones the same color 
    or am i empty but not you?
    >>> ally_or_empty('/', 'X')
    True
    >>> ally_or_empty('.', ',')
    False
    >>> ally_or_empty('.', 'X')
    True
    >>> ally_or_empty('O', 'X')
    False
    '''
    return ally(me, you) or am_i_empty_but_not_you(me, you)

def enemy_or_empty(me, you):
    r'''Are these stones different colors
    or am I empty but not you?
    >>> enemy_or_empty('/', 'X')
    False
    >>> enemy_or_empty('.', ',')
    False
    >>> enemy_or_empty('.', 'X')
    True
    >>> enemy_or_empty('O', 'X')
    True
    >>> enemy_or_empty('O', '/')
    True
    '''
    return enemy(me, you) or am_i_empty_but_not_you(me, you)
   
def different(me, you):
    return is_on_board(me) and not same(me, you)




# query board

def in_bounds(board, row, column):
    '''Is the coordinate on the board?
    >>> in_bounds(clear_board, -1, 0)
    False
    >>> in_bounds(clear_board, 0, 9)
    False
    >>> in_bounds(clear_board, 1, 2)
    True
    >>> in_bounds(clear_board_3_3, 2, 2)
    True
    >>> in_bounds(clear_board_3_3, 2, 3)
    False
    '''
    if 0 <= row and row < len(board):
        if 0 <= column and column < len(board[row]):
            return True
    return False


def doctest_board(array):
    '''Doctest hates ... at start of line, so use ,,,'''
    return array_to_text(array).replace('.', ',')




def lines_to_text(board_lines):
    r'''
    >>> test_board_lines =     [',,,', ',O,', 'X,,']
    >>> print lines_to_text(test_board_lines)
    ,,,
    ,O,
    X,,
    '''
    return '\n'.join(board_lines)




def array_to_text(array):
    '''
    >>> clear_text = array_to_text(  [[',', ','], [',', ',']] )
    >>> print clear_text
    ,,
    ,,
    >>> print array_to_text([[1, 2], [3, 4]])
    12
    34
    '''
    board_lines = []
    for row in array:
        text_row = [str(r) for r in row]
        board_lines.append(''.join(text_row))
    board_text = lines_to_text(board_lines)
    return board_text

def pb(array):
    '''Shortcut to print array_to_text of a board.
    >>> pb(not_capture_board)
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
    print array_to_text(array)



not_capture_board_text = '''
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

not_capture_board = text_to_array(not_capture_board_text)

capture_board_text = '''
OX,,,,,,,
OX,,,,,,,
X,,,,,,,,
,,,,,,,,,
,,,,,,,,,
,,,,,,,,,
,,,,,,,,,
,,,,,,,,,
,,,,,,,,,
'''

capture_board = text_to_array(capture_board_text)


individual_liberty_board_text = '''
,,,,,,,,X
,,X,,,,,,
,XO,,,,,,
,,X,,,,,O
,,,,,,,,,
,,,,,,,,,
,,,,,,,,,
,,,,,OXO,
O,,,,,O,,
'''

individual_liberty_board = text_to_array(individual_liberty_board_text)


# query coordinate on the board

def find_individual_liberty(board, row, column):
    '''Liberties for one stone.
    >>> liberty_lines = text_to_array(individual_liberty_board_text)
    >>> find_individual_liberty(liberty_lines, 2, 2)
    [(2, 3)]
    >>> find_individual_liberty(liberty_lines, 2, 4)
    [(1, 4), (2, 3), (2, 5), (3, 4)]
    '''
    individual_liberties = []
    for r, c in find_beside(board, row, column):
        if is_empty(board[r][c]):
            individual_liberties.append( (r, c) )
    return individual_liberties


liberty_board_text = '''
,,,,,,,,,
,,X,,,,,,
,XOO,,,,,
,,X,,,,,,
,,,X,O,,,
,,XOO,,,,
,,,XOX,,,
,,,XOX,,,
,,,,,,,,,
'''

liberty_board = text_to_array(liberty_board_text)

def find_beside(board, row, column):
    '''
    >>> find_beside(clear_board, 0, 0)
    [(0, 1), (1, 0)]
    >>> find_beside(clear_board, 0, 1)
    [(0, 0), (0, 2), (1, 1)]
    >>> find_beside(clear_board, 1, 0)
    [(0, 0), (1, 1), (2, 0)]
    >>> find_beside(clear_board, 1, 1)
    [(0, 1), (1, 0), (1, 2), (2, 1)]
    >>> find_beside(clear_board_3_3, 2, 2)
    [(1, 2), (2, 1)]
    '''
    beside = []
    for r, c in adjacent:
        intersection = row + r, column + c
        if in_bounds(board, *intersection):
            beside.append(intersection)
    return beside



def find_friend(board, row, column):
    '''Adjacent and same color.
    >>> board = text_to_array(liberty_board_text)
    >>> find_friend(board, 2, 2)
    [(2, 3)]
    >>> if not find_friend(board, 2, 4) == [(1, 4), (2, 5), (3, 4)]:
    ...     print liberty_board_text.replace('.', ',')

    Or adjacent and both empty.
    >>> find_friend(board, 0, 0)
    [(0, 1), (1, 0)]
    >>> find_friend(spy_group_board, 0, 1)
    [(1, 1)]
    '''
    friends = []
    me = board[row][column]
    for r, c in find_beside(board, row, column):
        if same(me, board[r][c]):
            friends.append((r, c))
    return friends


judith_ally_board = text_to_array('''
,,,,,
,@O,,
,XXO,
,,X,,
,,,,,
''')

def find_attacker(board, row, column):
    '''Adjacent, non-empty and different color.
    >>> find_attacker(judith_ally_board, 1, 1)
    [(2, 1)]
    '''
    enemies = []
    me = board[row][column]
    for r, c in find_beside(board, row, column):
        if enemy(me, board[r][c]):
            enemies.append((r, c))
    return enemies


pre_black_assassin_text = '''
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

pre_black_assassin_board = text_to_array(
        pre_black_assassin_text)

black_assassin_text = '''
,,,,,,,,,
,,,,,,,,,
,,XX,XX,,
,,,,,,,,,
,,,XX,,,,
,,X,O,X,,
,,XXO,X,,
,,XOXO,,,
,,,XO,,,,
'''

black_assassin_board = text_to_array(black_assassin_text)

enclosed_empty_region_text = '''
,,,,,,,,,
,,,,,,,,,
,,XX,XX,,
,,,,,,,,,
,,,XX,,,,
,,X,O,X,,
,,X,O,X,,
,,,O,O,,,
,,,,O,,,,
'''

enclosed_empty_region_board = text_to_array(
        enclosed_empty_region_text)


white_capture_eye_board_text = '''
,,,,XOOOX
,,,,XO,OX
,,,,XOOXX
XX,,XXOXX
OXXXXOXOX
OOOXOOXXX
,,,OO,OOX
,,,,,,,OO
,,,,,,,,,
'''
white_capture_eye_board = text_to_array(
        white_capture_eye_board_text)

white_capture_separate_board_text = '''
,,,,XOOOX
,,,,XO,OX
,,,,XOOXX
XX,,XXOXX
OXXXXOOOX
OOOXOOXXO
,,,OO,OOX
,,,,,,,OO
,,,,,,,,,
'''
white_capture_separate_board = text_to_array(
        white_capture_separate_board_text)

suicide_board_text = '''
,X,,XOOO,
X,,,XO,OX
,,,,XOOXX
XX,,XXOXX
OXXXXOXXX
OOOXOOXXX
,,,OO,OOX
XO,,,,,OO
O,O,,,,,,
'''
suicide_board = text_to_array(suicide_board_text)

brave_capture_board_text = '''
,OXOOX,,,
,OXOX,,O,
,,OX,,X,,
,,OXX,,X,
,O,OXXO,,
,X,OOOOOO
,,X,OXXXO
,,XOX,,,X
,,,X,X,X,
'''
brave_capture_board = text_to_array(
        brave_capture_board_text)

brave_capture_hook_board_text = '''
XXXOOOOX,
XOXOXXXO,
XOOX,,X,,
O,OXX,,X,
,O,OXXO,,
,X,OOOOOO
,,X,OXXXO
,,XOX,,,X
,,,X,X,X,
'''
brave_capture_hook_board = text_to_array(
        brave_capture_hook_board_text)

def find_capture(board, last_move):
    '''Find all stones captured.
    >>> find_capture(black_assassin_board, (7, 4))
    [(7, 3)]
    >>> find_capture(black_assassin_board, (7, 3))
    [(7, 4)]
    >>> find_capture(enclosed_empty_region_board, (7, 3))
    []
    >>> find_capture(white_capture_eye_board, (4, 7))
    [(0, 8), (1, 8), (2, 7), (2, 8), (3, 7), (3, 8), (4, 6), (4, 8), (5, 6), (5, 7), (5, 8), (6, 8)]
    >>> find_capture(white_capture_separate_board, (5, 8))
    [(0, 8), (1, 8), (2, 7), (2, 8), (3, 7), (3, 8), (4, 8), (5, 6), (5, 7), (6, 8)]
    >>> suicide_board[0][8] = black
    >>> beach = find_capture(suicide_board, (0, 8))
    >>> print text_mask(beach)
    ,,,,,,,,#
    ,,,,,,,,#
    ,,,,,,,##
    ,,,,,,,##
    ,,,,,,###
    ,,,,,,###
    ,,,,,,,,#
    ,,,,,,,,,
    ,,,,,,,,,

    Remove group that is bravely capturing.
    >>> peninsula = find_capture(brave_capture_board, (0, 3))
    >>> print text_mask(peninsula)
    ,,#,,,,,,
    ,,#,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    >>> hook = find_capture(brave_capture_hook_board, (0, 3))
    >>> print text_mask(hook)
    ###,,,,,,
    #,#,,,,,,
    #,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    '''
    surrounded = find_liberty_equals(board, 0)
    captured = surrounded
    if last_move in surrounded:
        for desperate in surrounded:
            if desperate in find_beside(board, *last_move):
                if last_move in captured:
                    row, column = last_move
                    r, c = desperate
                    if enemy(board[row][column], board[r][c]):
                        #captured.remove(last_move)
                        # remove group
                        group = find_region(board, row, column)
                        for friend in group:
                            if friend in captured: 
                                captured.remove(friend)
    return captured


spy_group_board_text = '''
O/,,,,,,,
OX,,,,,,,
,,,,,,,,,
,,,,,,,,,
,,,,,,,,,
,,,,,,,,,
,,,,,,,,,
,,,,,,,,,
,,,,,,,,,
'''

spy_group_board = text_to_array(spy_group_board_text)

def find_region(board, row, column):
    '''All connected stones in same color
    >>> sea = find_region(liberty_board, 0, 0)
    >>> print text_mask(sea)
    #########
    ##,######
    #,,,#####
    ##,######
    ###,#,###
    ##,,,####
    ###,,,###
    ###,,,###
    #########
    >>> find_region(liberty_board, 2, 2)
    [(2, 2), (2, 3)]
    >>> find_region(liberty_board, 5, 4)
    [(5, 3), (5, 4), (6, 4), (7, 4)]
    >>> find_region(individual_liberty_board, 2, 2)
    [(2, 2)]
    >>> peninsula_two = find_region(spy_group_board, 0, 1)
    >>> print text_mask(peninsula_two)
    ,#,,,,,,,
    ,#,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    '''
    group = [(row, column)]
    new_friends = find_friend(board, row, column)
    while [] != new_friends:
        new_friend = new_friends.pop(0)
        if new_friend not in group:
            group.append(new_friend)
            their_friends = find_friend(board, *new_friend)
            for their_friend in their_friends:
                if their_friend not in new_friends \
                        and their_friend not in group:
                    new_friends.append(their_friend)
    group.sort()
    return group


def find_liberty_of_set(board, group):
    '''group must contain all its stones already.
    '''
    group_liberties = []
    for r, c in group:
        for liberty in find_individual_liberty(board, r, c):
            if liberty not in group_liberties:
                group_liberties.append(liberty)
    group_liberties.sort()
    return group_liberties


liberty_share_board = text_to_array('''
X,OXX
,,,,O
,,O,,
,,,,,
,,,,,
''')

def find_liberty_side_of_set(board, group, suffix):
    '''group must contain all its stones already.
    outside of liberty that faces the stone.
    >>> coordinate_sides = find_liberty_side_of_set(liberty_board, [(1, 2)], '_notice')
    >>> from pprint import pprint
    >>> pprint(coordinate_sides)
    {(0, 2): ['none', 'none', 'black_notice', 'none'],
     (1, 1): ['none', 'black_notice', 'none', 'none'],
     (1, 3): ['none', 'none', 'none', 'black_notice']}

    #Only return first liberty side if multiple sides supply same group at same liberty coordinate.
    #>>> coordinate_sides = find_liberty_side_of_set(suicide_board, [(3, 1), (4, 2)], '_warning')
    #>>> pprint(coordinate_sides)
    #{(2, 1): ['none', 'none', 'black_warning', 'none'],
    # (3, 2): ['none', 'none', 'none', 'black_warning']}

    If different groups share same liberty, return each of those liberty sides.
    >>> coordinate_sides = find_liberty_side_of_set(liberty_share_board, [(0, 0), (0, 2), (1, 4)], '_warning')
    >>> pprint(coordinate_sides[(0, 1)])
    ['none', 'white_warning', 'none', 'black_warning']
    >>> pprint(coordinate_sides[(1, 2)])
    ['white_warning', 'none', 'none', 'none']
    >>> pprint(coordinate_sides)
    {(0, 1): ['none', 'white_warning', 'none', 'black_warning'],
     (1, 0): ['black_warning', 'none', 'none', 'none'],
     (1, 2): ['white_warning', 'none', 'none', 'none'],
     (1, 3): ['none', 'white_warning', 'none', 'none'],
     (2, 4): ['white_warning', 'none', 'none', 'none']}

    '''
    liberty_sides = {}
    facings = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    max = {'_notice': 3, '_warning': 2, '_danger': 1}
    liberateds = []
    def plus(a, b):
        return (a[0]+b[0], a[1]+b[1])
    for r, c in group:
        me = (r, c)
        for liberty in find_individual_liberty(board, r, c):
            if liberty not in liberty_sides:
                liberty_sides[liberty] = ['none', 'none', 'none', 'none']
            for f, facing in enumerate(facings):
                liberated = plus(facing, liberty)
                if liberateds.count(liberated) < max[suffix]:
                    if me == liberated:
                        color = get_color(board[r][c])
                        liberty_sides[liberty][f] = color + suffix
                        liberateds.append(liberated)
    return liberty_sides



def find_exterior_side_of_region(board, region, label):
    '''group must contain all its stones already.
    outside of liberty that faces the stone, or faces edge of board.
    >>> coordinate_sides = find_exterior_side_of_region(enclosed_empty_region_board, [(6, 3), (5, 3)], 'white_capture')
    >>> from pprint import pprint
    >>> pprint(coordinate_sides)
    {(5, 3): ['white_capture', 'white_capture', 'none', 'white_capture'],
     (6, 3): ['none', 'white_capture', 'white_capture', 'white_capture']}
    >>> coordinate_sides = find_exterior_side_of_region(capture_board, [(0, 0), (1, 0)], 'white_capture')
    >>> from pprint import pprint
    >>> pprint(coordinate_sides)
    {(0, 0): ['white_capture', 'white_capture', 'none', 'white_capture'],
     (1, 0): ['none', 'white_capture', 'white_capture', 'white_capture']}
    '''
    exterior_sides = {}
    facings = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    def plus(a, b):
        return (a[0]+b[0], a[1]+b[1])
    for r, c in region:
        me = (r, c)
        sides = ['none', 'none', 'none', 'none']
        for f, facing in enumerate(facings):
            r1, c1 = plus(facing, me)
            if r1 <= -1 or len(board) <= r1:
                sides[f] = label
            elif c1 <= -1 or len(board[r]) <= c1:
                sides[f] = label
            elif different(board[r][c], board[r1][c1]):
                sides[f] = label
        if label in sides:
            exterior_sides[me] = sides
    return exterior_sides



def find_liberty(board, row, column):
    '''Adjacent to group and empty.
    >>> find_liberty(liberty_board, 2, 2)
    [(1, 3), (2, 4), (3, 3)]
    >>> find_liberty(liberty_board, 5, 4)
    [(4, 4), (5, 5), (8, 4)]

    Array or lines can be used for the board.
    >>> array = text_to_array(liberty_board_text)
    >>> find_liberty(array, 2, 2)
    [(1, 3), (2, 4), (3, 3)]
    >>> find_liberty(array, 5, 4)
    [(4, 4), (5, 5), (8, 4)]
    '''
    group_liberties = []
    group = find_region(board, row, column)
    return find_liberty_of_set(board, group)


def find_regions(board):
    '''All regions on board.
    >>> regions = find_regions(liberty_board)
    >>> print text_mask(regions[0])
    #########
    ##,######
    #,,,#####
    ##,######
    ###,#,###
    ##,,,####
    ###,,,###
    ###,,,###
    #########

    solo stone
    >>> print text_mask(regions[1])
    ,,,,,,,,,
    ,,#,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,

    May be slow.
    >>> import timeit
    >>> timer = timeit.Timer(stmt='regions = find_regions(liberty_board)', setup='from board import find_regions, liberty_board')
    >>> took = timer.timeit(number=10)
    >>> if not 0.015625 < took:  took
    '''
    uncharted = [(row, column) for row in range(len(board))
        for column in range(len(board[row]))]
    regions = []
    while uncharted:
        explorer = uncharted[0]
        region = find_region(board, *explorer)
        for coordinate in region:
            uncharted.remove(coordinate)
        regions.append(region)
    return regions


def find_groups(board):
    '''All populated regions on board.
    >>> groups = find_groups(liberty_board)
    >>> groups
    [[(1, 2)], [(2, 1)], [(2, 2), (2, 3)], [(3, 2)], [(4, 3)], [(4, 5)], [(5, 2)], [(5, 3), (5, 4), (6, 4), (7, 4)], [(6, 3), (7, 3)], [(6, 5), (7, 5)]]
    >>> for group in groups:
    ...     for r, c in group:
    ...         print liberty_board[r][c],
    ...     print
    ...     
    X
    X
    O O
    X
    X
    O
    X
    O O O O
    X X
    X X
    '''
    groups = []
    regions = find_regions(board)
    for region in regions:
        r, c = region[0]
        if not is_empty(board[r][c]):
            groups.append(region)
    return groups


def find_liberty_equals(board, equals = 1):
    '''Find all stones with exact liberty.
    >>> find_liberty_equals(individual_liberty_board, 1)
    [(2, 2), (7, 6)]
    >>> find_liberty_equals(individual_liberty_board, 2)
    [(0, 8), (8, 0), (8, 6)]
    >>> find_liberty_equals(enclosed_empty_region_board, 3)
    [(8, 4)]
    '''
    constrained = []
    groups = find_groups(board)
    for group in groups:
        liberty = find_liberty_of_set(board, group)
        if equals == len(liberty):
            constrained.extend(group)
    return constrained


def find_constrained_attackers(board, equals, row, column):
    '''Find all stones with exact liberty 
    that are enemies attached a group at the stone.
    >>> find_constrained_attackers(individual_liberty_board, 1, 1, 2)
    [(2, 2)]
    >>> find_constrained_attackers(individual_liberty_board, 2, 7, 6)
    [(8, 6)]
    >>> find_constrained_attackers(enclosed_empty_region_board, 3, 8, 4)
    []
    '''
    attackers = []
    for r, c in find_attacker(board, row, column):
        group = find_region(board, r, c)
        liberties = find_liberty_of_set(board, group)
        if equals == len(liberties):
            attackers.extend(group)
    return attackers



def find_danger(board):
    '''Find all stones in danger of becoming captured.
    '''
    return find_liberty_equals(board, 1)


def find_warning(board):
    '''Find all stones that could become in danger.
    '''
    return find_liberty_equals(board, 2)

def find_notice(board):
    '''Find all stones that could become a warning.
    '''
    return find_liberty_equals(board, 3)


guard_board = text_to_array('''
,,,
,XX
$,,
''')

guard2_board = text_to_array('''
,,,
,OX
,X,
''')

guard3_board = text_to_array('''
,,,,,
,,,X,
,,XO,
,,OX$
,,,O,
''')

not_guard_board = text_to_array('''
,O,,,
X,,,,
,,,,,
,,,,,
,,,,,
''')

not_guard2_board = text_to_array('''
XO,
,X,
,,,
''')

def remove_guarded(board, warnings, dangers):
    '''Iff group has at least one liberty that is guarded.
    Remove notices or warnings 
    Guarded liberty has no enemy neighbor and zero or one liberties.
        if two or three liberties:
            if at least one liberty is guarded, then 
                downgrade
            guarded:  zero or one liberty and no adjacent enemy.
            guarded: if enemy plays there, then can capture immediately.
                ,O,O,
                ,,OX$
                OOXO,
                XXXXO
                ,,,X,
            if no block, then no strike.
            viable ko threat.
    >>> warnings = [(2, 0)]
    >>> dangers = find_danger(guard_board)
    >>> remove_guarded(guard_board, warnings, dangers)
    []
    >>> warnings = [(2, 1)]
    >>> dangers = find_danger(guard2_board)
    >>> remove_guarded(guard2_board, warnings, dangers)
    []
    >>> notices = [(0, 1), (1, 0)]
    >>> dangers = find_danger(not_guard_board)
    >>> remove_guarded(not_guard_board, notices, dangers)
    [(0, 1), (1, 0)]

    If enemy may capture, then retain notice.
    >>> notices = [(1, 1)]
    >>> dangers = find_danger(not_guard2_board)
    >>> dangers
    [(0, 0), (0, 1)]
    >>> remove_guarded(not_guard2_board, notices, dangers)
    [(1, 1)]

    If may capture, then remove warning.
    >>> warnings = [(4, 2), (4, 3)]
    >>> dangers = find_danger(guard3_board)
    >>> remove_guarded(guard3_board, warnings, dangers)
    []
    '''
    filtered_warnings = []
    for row, column in warnings:
        me = board[row][column]
        guarded = False
        liberties = find_liberty(board, row, column)
        for lr, lc in liberties:
            besides = find_beside(board, lr, lc)
            empty_count = 0
            enemy_count = 0
            endangered = False
            for br, bc in besides:
                you = board[br][bc]
                if (br, bc) in dangers:
                    endangered = True
                elif is_empty(you):
                    empty_count += 1
                elif enemy(me, you):
                    enemy_count += 1
            if not endangered and enemy_count == 0:
                if empty_count == 0 or empty_count == 1:
                    guarded = True
        if not guarded:
            filtered_warnings.append((row, column))
    return filtered_warnings

def is_blocked(board_cell, neighbor):
    '''
    >>> print doctest_board(board_lines)
    ,,,,,,,,,
    ,OO,,,,,,
    OOOOO,,,,
    ,,OXXX,,,
    ,OX,XX,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    >>> is_blocked(board_lines[3][2], board_lines[3][1])
    False
    >>> is_blocked(board_lines[3][2], board_lines[3][3])
    True
    >>> is_blocked(white, play_white)
    False
    >>> is_blocked(white, play_black)
    True
    '''
    if is_empty(neighbor):
        return False
    if ally(board_cell, neighbor):
        return False
    return True


def i_am_empty_but_not_you(board_cell, neighbor):
    '''I am empty and you are not.
    >>> print doctest_board(board_lines)
    ,,,,,,,,,
    ,OO,,,,,,
    OOOOO,,,,
    ,,OXXX,,,
    ,OX,XX,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    >>> i_am_empty_but_not_you(board_lines[3][1], board_lines[3][2])
    True
    >>> i_am_empty_but_not_you(board_lines[3][2], board_lines[3][3])
    False
    >>> i_am_empty_but_not_you(white, play_white)
    False
    >>> i_am_empty_but_not_you(empty, white)
    True
    '''
    if is_empty(board_cell) and is_occupied(neighbor):
        return True
    return False


def get_sides(board_lines, short_circuit, is_cell, border):
    '''Sides of cell that are not short_circuit and do compare to is_cell.
    >>> code_unit.doctest_unit(get_liberties, verbose=False, log=False)
    >>> code_unit.doctest_unit(get_blocks, verbose=False, log=False)
    '''
    north, east, south, west = range(4)
    rows = range(len(board_lines))
    columns = range(len(board_lines[0]))
    neighbors = []
    for row in rows:
        neighbors.append([])
        for column in columns:
            neighbors[-1].append([None, None, None, None])
    for r in rows:
        for c in columns:
            board_cell = board_lines[r][c]
            if short_circuit(board_cell):
                neighbors[r][c] = [False, False, False, False]
            else:
                cell = neighbors[r][c]
                if 0 == r:
                    cell[north] = border
                else:
                    neighbor = board_lines[r-1][c]
                    cell[north] = is_cell(board_cell, neighbor)
                if len(board_lines[r]) - 1 == c:
                    cell[east] = border
                else:
                    neighbor = board_lines[r][c+1]
                    cell[east] = is_cell(board_cell, neighbor)
                if len(board_lines) - 1 == r:
                    cell[south] = border
                else:
                    neighbor = board_lines[r+1][c]
                    cell[south] = is_cell(board_cell, neighbor)
                if 0 == c:
                    cell[west] = border
                else:
                    neighbor = board_lines[r][c-1]
                    cell[west] = is_cell(board_cell, neighbor)
    return neighbors

def get_blocks(board_lines):
    '''Block means neighbor is off board or an attacker.  
    Block takes away a liberty.
    Ordering clockwise (north, east, south, west)
    >>> board_lines[3][2]
    'O'
    >>> board_lines[3][3]
    'X'
    >>> board_lines[3][1]
    ','
    >>> blocks = get_blocks(board_lines)
    >>> blocks[3][2]
    [False, True, True, False]

    If no stone, do not consider blocks.
    >>> blocks[1][0]
    [False, False, False, False]

    If off board, block.
    >>> blocks[2][0]
    [False, False, False, True]
    '''
    return get_sides(board_lines, is_empty, is_blocked, True)

def get_liberties(board_lines):
    '''Neighbors of stones.
    >>> liberties = get_liberties(board_lines)
    >>> liberties[3][1]
    [True, True, True, False]
    >>> liberties[4][0]
    [False, True, False, False]
    '''
    return get_sides(board_lines, is_occupied, i_am_empty_but_not_you, False)


def get_empty_blocks(board_lines):
    r'''Cell (empty or occupied) would be blocked on that side.
    >>> empty_blocks = get_empty_blocks(clear_board_3_3)
    >>> empty_blocks[0][0]
    ['block', 'liberty', 'liberty', 'block']
    >>> empty_blocks[0][1]
    ['block', 'liberty', 'liberty', 'liberty']
    >>> empty_blocks[1][1]
    ['liberty', 'liberty', 'liberty', 'liberty']
    >>> empty_blocks[2][2]
    ['liberty', 'block', 'block', 'liberty']
    >>> clear_board_3_3[1][1] = black
    >>> clear_board_3_3[0][1] = black
    >>> pb(clear_board_3_3)
    ,X,
    ,X,
    ,,,
    >>> empty_blocks = get_empty_blocks(clear_board_3_3)
    >>> empty_blocks[0][1]
    ['block', 'liberty', 'you', 'liberty']
    '''
    def you_liberty(cell, other):
        if is_blocked(cell, other):
            return 'block'
        if ally(cell, other):
            return 'you'
        return 'liberty'
    return get_sides(board_lines, always_false, you_liberty, 'block')

def update_board(board, last_move):
    r'''Remove captured.  Does not count score.
    >>> print array_to_text(update_board(not_capture_board, (1, 1)))
    O/,,,,,,,
    O/,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    >>> print array_to_text(update_board(capture_board, (2, 0)))
    ,X,,,,,,,
    ,X,,,,,,,
    X,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    >>> pb(update_board(white_capture_eye_board, (4, 7)))
    ,,,,XOOO,
    ,,,,XO,O,
    ,,,,XOO,,
    XX,,XXO,,
    OXXXXO,O,
    OOOXOO,,,
    ,,,OO,OO,
    ,,,,,,,OO
    ,,,,,,,,,
    >>> pb(update_board(white_capture_separate_board, (5, 8)))
    ,,,,XOOO,
    ,,,,XO,O,
    ,,,,XOO,,
    XX,,XXO,,
    OXXXXOOO,
    OOOXOO,,O
    ,,,OO,OO,
    ,,,,,,,OO
    ,,,,,,,,,
    '''
    captured = find_capture(board, last_move)
    board = map_at_position(mark_empty, 
            board, captured)
    return board

before_ko_board_text = '''
OX,X,,,,,
,OX,,,,,,
O,O,,,,,,
,,,,,,,,,
,,,,,,,,,
,,,,,,,,,
,,,,,,,,,
,,,,,,,,,
,,,,,,,XX
'''
before_ko_board = text_to_array(
        before_ko_board_text)

start_ko_board_text = '''
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
start_ko_board = text_to_array(
        start_ko_board_text)

fill_ko_board_text = '''
XX,X,,,,,
XOX,,,,,,
O,O,,,,,,
,,,,,,,,,
,,,,,,,,,
,,,,,,,,,
,,,,,,,,,
,,,,,,,,,
,,,,,,,XX
'''
fill_ko_board = text_to_array(
        fill_ko_board_text)


def play_and_update(board, color, row, column):
    '''Resolve captures.  Do not check ko.
    >>> next_board = play_and_update(start_ko_board, 'white', 0, 0)
    >>> if not next_board == before_ko_board:
    ...     pb(next_board)
    ...     pb(before_ko_board)
    >>> next_board = play_and_update(fill_ko_board, 'white', 0, 0)
    >>> if next_board == before_ko_board:
    ...     pb(next_board)
    ...     pb(before_ko_board)
    >>> next_board = play_and_update(capture_board, 'black', 2, 0)
    >>> if next_board == capture_board:
    ...     pb(next_board)
    ...     pb(capture_board)
    '''
    next_board = copy.deepcopy(board)
    if is_empty(board[row][column]):
        next_board[row][column] = eval(color)
    return update_board(next_board, (row, column))



# multiple coordinates on board

def mark_black_hidden(mark):
    return black_hidden

def mark_empty(mark):
    return empty

def mark_white(mark):
    return white

def mark_black(mark):
    return black

import copy
def map_at_position(do_this, grid, positions):
    '''
    >>> map_at_position(lambda i:  'X', 
    ...         liberty_board, [(0, 0)])  [0][0:2]
    ['X', ',']

    Original is not changed.
    >>> liberty_board[0][0:2] 
    [',', ',']
    >>> map_at_position(lambda i:  'X', 
    ...         liberty_board, {'black': [(0, 0)]})
    map_at_position:  This is not a position black {'black': [(0, 0)]}
    '''
    for position in positions:
        if 2 != len(position):
            print 'map_at_position:  This is not a position', position, positions
            return
    mapped = copy.deepcopy(grid)
    for row, column in positions:
        mapped[row][column] = do_this(grid[row][column]) 
    return mapped
    
def text_mask(positions, grid = clear_board):
    '''
    >>> print text_mask([(0, 8), (8, 8)])
    ,,,,,,,,#
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,#
    >>> print text_mask([(0, 4), (4, 4)], grid = clear_board_5_5)
    ,,,,#
    ,,,,,
    ,,,,,
    ,,,,,
    ,,,,#
    '''
    return doctest_board(
            map_at_position(
                lambda i: '#', grid, positions))


# 3x3 board

clear_board_3_3_text = '''
,,,
,,,
,,,
'''
clear_board_3_3 = text_to_array(clear_board_3_3_text)

board_pre_capture_3_3_text = '''
,,,
,,X
,,O
'''
board_pre_capture_3_3 = text_to_array(board_pre_capture_3_3_text)



def filter_board(condition, board):
    '''filter board to each cell that satisfies condition function.
    >>> empties = filter_board(is_empty, clear_board)
    >>> len(empties)
    81
    >>> empties[0]
    (0, 0)
    >>> empties[-1]
    (8, 8)
    '''
    empties = []
    for r, row in enumerate(board):
        for c, cell in enumerate(row):
            if condition(cell):
                empties.append( (r, c) )
    return empties


def flatten(pairs):
    '''
    Degroup.
    >>> flatten([[(3, 4)], [(6, 7)]])
    [(3, 4), (6, 7)]

    ActionScript had used flat lists.  DEPRECATE.
    >>> flatten([(3, 4), (6, 7)])
    [3, 4, 6, 7]
    '''
    flat_list = []
    for pair in pairs:
        for part in pair:
            flat_list.append(part)
    return flat_list

def is_suicide(pre_board, color, row, column):
    '''Would this place have no liberties at end of this move?
    >>> is_suicide(suicide_board, 'black', 0, 8)
    True
    >>> is_suicide(suicide_board, 'black', 1, 6)
    True
    >>> is_suicide(suicide_board, 'black', 1, 6)
    True
    >>> is_suicide(suicide_board, 'black', 8, 1)
    False
    >>> is_suicide(suicide_board, 'black', 6, 0)
    False
    '''
    next_board = copy.deepcopy(pre_board)
    next_board[row][column] = eval(color)
    will_be_captured = find_capture(next_board, (row, column))
    return (row, column) in will_be_captured


def predict_suicides(board, color):
    '''Find all places on board that will be suicide.
    >>> print text_mask(predict_suicides(suicide_board, 'black'))
    ,,,,,,,,#
    ,,,,,,#,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    >>> print text_mask(predict_suicides(suicide_board, 'white'))
    #,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    '''
    regions = find_regions(board)
    singles = [region for region in regions 
            if 1 == len(region)]
    singles = flatten(singles)
    empties = [(row, column) for row, column in singles 
            if is_empty(board[row][column])]
    suicides = [(row, column) for row, column in empties
            if is_suicide(board, color, row, column)]
    return suicides

white_suicide_board = text_to_array('''
,XO
XX,
XOO
''')

import random
def random_empty(board, color):
    '''Randomly select empty coordinate on board that is not suicide.
    >>> random.seed(0)
    >>> random_empty(clear_board, 'white')
    (7, 5)
    >>> random_empty(clear_board, 'white')
    (6, 7)
    >>> random_empty([], 'white')
    >>> random_empty(white_suicide_board, 'white')
    '''
    empties = filter_board(is_empty, board)
    if not empties:
        return None
    suicides = predict_suicides(board, color)
    valids = [empty for empty in empties
            if empty not in suicides]
    if not valids:
        return None
    return random.choice(valids)


# ActionScript algorithms

def get_connected(board_lines):
    '''Ordering clockwise (north, east, south, west)
    >>> connected = get_connected(board_lines)
    >>> connected[0][1]
    [False, False, False, False]
    >>> connected[1][1]
    [False, True, True, False]
    >>> connected[2][2]
    [True, True, True, True]
    >>> connected[2][2]
    [True, True, True, True]
    >>> connected[3][3]
    [False, True, False, False]

    >>> connected = get_connected(judith_ally_board)
    >>> connected[1][1]
    [False, True, False, False]
    >>> connected[2][1]
    [False, True, False, False]
    '''
    north, east, south, west = range(4)
    rows = range(len(board_lines))
    columns = range(len(board_lines[0]))
    neighbors = []
    for row in rows:
        neighbors.append([])
        for column in columns:
            neighbors[-1].append([None, None, None, None])
    for r in rows:
        for c in columns:
            cell = neighbors[r][c]
            board_cell = board_lines[r][c]
            if 0 == r:
                cell[north] = False
            else:
                cell[north] = ally(board_cell, board_lines[r-1][c])
            if len(board_lines[r]) - 1 == c:
                cell[east] = False
            else:
                cell[east] = ally(board_cell, board_lines[r][c+1])
            if len(board_lines) - 1 == r:
                cell[south] = False
            else:
                cell[south] = ally(board_cell, board_lines[r+1][c])
            if 0 == c:
                cell[west] = False
            else:
                cell[west] = ally(board_cell, board_lines[r][c-1])
    return neighbors



def get_labels(connected):
    '''Labels for connected by order NESW.
    >>> connected = get_connected(board_lines)
    >>> labels = get_labels(connected)
    >>> connected[2][2]
    [True, True, True, True]
    >>> connected[3][3]
    [False, True, False, False]
    >>> labels[3][3]
    '_0100'
    '''
    labels = []
    for row in connected:
        labels.append([])
        for column in row:
            labels[-1].append('_')
            for direction in column:
                if direction:
                    labels[-1][-1] += '1'
                else:
                    labels[-1][-1] += '0'
    return labels




import code_unit
snippet = '''
# !start python code_explorer.py --import board.py --snippet snippet
import board; board = reload(board); from board import *
code_unit.doctest_unit(get_liberties)
'''
if __name__ == '__main__':
    from optparse import OptionParser
    parser = OptionParser()
    parser.add_option("--unit", default="",
        dest="unit", help="unit to doctest [default: %default]")
    parser.add_option('-v', '--verbose', dest='verbose', default='warning',
                    help="Increase verbosity")
    (options, args) = parser.parse_args()
    #log_level = logging_levels[options.verbose]
    #logging.basicConfig(level=log_level)
    #logging.basicConfig(level=log_level)
    if options.unit:
        unit = eval(options.unit)
        code_unit.doctest_unit(unit)
    else:
        units = globals().values()
        ## units.remove(setup_example)
        code_unit.doctest_units(units)
    

