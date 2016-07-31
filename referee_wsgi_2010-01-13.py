'''
Analyze board of Go for connections.
Captures
Hidden stone.
'''

__author__ = 'Ethan Kennerly'

# doctest abhors '...'
empty = ','
empty_characters = empty + '.+'
black = 'X'
black_hidden = '/'  # opponent does not know black is here
black_characters = black + black_hidden
white = 'O'
white_characters = white
row_count = 9
column_count = 9

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

def is_black(cell):
    '''
    >>> is_black('X')
    True
    '''
    return len(cell) == 1 \
            and cell in black_characters \
            and cell != ''

def is_white(cell):
    '''
    >>> is_white('O')
    True
    '''
    return len(cell) == 1 \
            and cell in white_characters \
            and cell != ''

def is_on_board(mark):
    return is_white(mark) or is_black(mark) or is_empty(mark)


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


def in_bounds(row, column):
    '''
    >>> in_bounds(-1, 0)
    False
    >>> in_bounds(0, 9)
    False
    >>> in_bounds(1, 2)
    True
    >>> 
    '''
    if 0 <= row and row < row_count:
        if 0 <= column and column < column_count:
            return True
    return False


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


def find_individual_liberty(board, row, column):
    '''Liberties for one stone.
    >>> liberty_lines = text_to_array(individual_liberty_board_text)
    >>> find_individual_liberty(liberty_lines, 2, 2)
    [(2, 3)]
    >>> find_individual_liberty(liberty_lines, 2, 4)
    [(1, 4), (2, 3), (2, 5), (3, 4)]
    '''
    individual_liberties = []
    for r, c in find_beside(row, column):
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

def find_beside(row, column):
    '''
    >>> find_beside(0, 0)
    [(0, 1), (1, 0)]
    >>> find_beside(0, 1)
    [(0, 0), (0, 2), (1, 1)]
    >>> find_beside(1, 0)
    [(0, 0), (1, 1), (2, 0)]
    >>> find_beside(1, 1)
    [(0, 1), (1, 0), (1, 2), (2, 1)]
    '''
    beside = []
    for r, c in adjacent:
        intersection = row + r, column + c
        if in_bounds(*intersection):
            beside.append(intersection)
    return beside


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
    '''
    if is_black(me) and is_white(you):
        return True
    elif is_white(me) and is_black(you):
        return True
    else:
        return False
   
def are_we_on_board(me, you):
    return is_on_board(me) and is_on_board(you)


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

#no example
#def same_or_empty(me, you):
#    return same(me, you) or is_empty(me)
#def different_or_empty(me, you):
#    return is_empty(me) or \
#        different_color(me, you)


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
    for r, c in find_beside(row, column):
        if same(me, board[r][c]):
            friends.append((r, c))
    return friends


def find_attacker(board, row, column):
    '''Adjacent, non-empty and different color.'''
    enemies = []
    me = board[row][column]
    for r, c in find_beside(row, column):
        if me != board[r][c] and not is_empty(board[r][c]):
            enemies.append((r, c))
    return enemies


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


def flatten(pairs):
    '''ActionScript had used flat lists.  DEPRECATE.
    >>> flatten([(3, 4), (6, 7)])
    [3, 4, 6, 7]
    '''
    flat_list = []
    for pair in pairs:
        for part in pair:
            flat_list.append(part)
    return flat_list


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
    '''
    uncharted = [(row, column) for row in range(9)
        for column in range(9)]
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
    >>> find_liberty_equals(enclosed_empty_region_board, 2)
    []
    '''
    constrained = []
    groups = find_groups(board)
    for group in groups:
        liberty = find_liberty_of_set(board, group)
        if equals == len(liberty):
            constrained.extend(group)
    return constrained


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
            if desperate in find_beside(*last_move):
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


def find_danger(board):
    '''Find all stones in danger.
    '''
    return find_liberty_equals(board, 1)


def find_warning(board):
    '''Find all stones in danger of becoming in danger.
    '''
    return find_liberty_equals(board, 2)

# Hide

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

def get_color_row_column(event):
    '''
    >>> get_color_row_column({'black':  (7, 2)})
    ('black', 7, 2)
    '''
    for color in 'black', 'white':
        if color in event:
            row, column = event.get(color)
            return color, row, column
    

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

def is_black_hidden(mark):
    return mark == black_hidden

def mark_black_hidden(mark):
    return black_hidden

def mark_empty(mark):
    return empty

def mark_white(mark):
    return white

def mark_black(mark):
    return black

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





#
# Go Text Protocol
#

gtp_start_of_ok = '= '
gtp_start_of_error = '? '
gtp_end_of_response = '\n\n'

def gtp_ok(gtp_response):
    r'''Single, complete, happy response
    >>> gtp_ok('= \n\n')
    True
    >>> gtp_ok('? Cannot\n\n')
    False
    >>> gtp_ok('= C4\n\n')
    True
    >>> gtp_ok('= white\n\n= C4\n\n')
    False
    >>> gtp_ok('= C4\n')
    False
    '''
    return gtp_response.startswith(gtp_start_of_ok) \
            and 1 == gtp_response.count(gtp_end_of_response) \
            and gtp_response.endswith(gtp_end_of_response)


def last_response(response):
    r'''Return only last response.
    >>> single_response = '= B+6.0\n\n'
    >>> last_response(single_response)
    '= B+6.0\n\n'
    >>> double_response = '= B+6.0\n\n= B+6.0\n\n'
    >>> last_response(double_response)
    '= B+6.0\n\n'
    '''
    last = response.split(gtp_end_of_response)[-2]
    last += gtp_end_of_response
    return last


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


# index         0    1    2    3    4    5    6    7    8
column_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J']
row_list = [    9 ,  8 ,  7 ,  6 ,  5 ,  4 ,  3 ,  2 ,  1]

def array_to_gtp(row, column):
    '''Map 2D array to 9x9 board as shown by GnuGo 3.8
    >>> array_to_gtp(0, 2)
    'C9'
    >>> array_to_gtp(2, 2)
    'C7'
    '''
    return column_list[column] + str(row_list[row])


def gtp_to_array(gtp_coordinate):
    '''Map 9x9 board as shown by GnuGo 3.8 to 2D array.
    >>> gtp_to_array('A7')
    (2, 0)
    >>> gtp_to_array('C7')
    (2, 2)
    >>> gtp_to_array('PASS')
    gtp_to_array:  I only know how to handle 2 characters, not PASS
    >>> gtp_to_array('Z7')
    gtp_to_array:  column not found:  Z7
    '''
    if 2 != len(gtp_coordinate):
        print 'gtp_to_array:  I only know how to handle 2 characters, not ' + gtp_coordinate
        return
    gtp_column, gtp_row = gtp_coordinate[0], gtp_coordinate[1:]
    if gtp_column not in column_list:
        print 'gtp_to_array:  column not found:  ' + str(gtp_coordinate)
        return
    column = column_list.index(gtp_column)
    gtp_row = int(gtp_row)
    if gtp_row not in row_list:
        print 'gtp_to_array:  row not found: ' + str(gtp_coordinate)
        return
    row = row_list.index(gtp_row)
    return row, column

def gtp_to_move(gtp_response):
    r'''Stone or PASS.
    >>> gtp_to_move('= A7\n\n')
    (2, 0)
    >>> gtp_to_move('= C7\n\n')
    (2, 2)
    >>> gtp_to_move('= PASS\n\n')
    'pass'
    >>> gtp_to_move('= resign\n\n')
    'resign'
    '''
    stone = gtp_response_to_stone(gtp_response)
    if 'pass' == stone.lower() \
            or 'resign' == stone.lower():
        return stone.lower()
    else:
        return gtp_to_array(stone)

def gtp_response_to_stone(gtp_response):
    a_list = gtp_response_to_list(gtp_response)
    if a_list:
        return a_list[0]
    else:
        return


def gtp_response_to_coordinate(gtp_response):
    r'''
    >>> gtp_response_to_coordinate('= C4\n\n')
    (5, 2)
    '''
    gtp_coordinate = gtp_response_to_stone(
            gtp_response)
    row, column = gtp_to_array(gtp_coordinate)
    return row, column


def gtp_response_to_list(gtp_response):
    r'''GTP to Python data.
    >>> gtp_response_to_list('= C6 C4\n\n')
    ['C6', 'C4']
    >>> gtp_response_to_list('= \n\n')
    []
    >>> gtp_response_to_list('=\n\n')
    []
    >>> gtp_response_to_list('= black\n\n')
    ['black']
    >>> gtp_response_to_list('= PASS\n\n')
    ['PASS']
    '''
    gtp_response = gtp_response.splitlines()[0]
    python_list = gtp_response.split(' ')[1:]
    if '' in python_list:
        python_list.remove('')
    return python_list


def gtp_response_to_text(gtp_response):
    r'''GTP to Python multi-line string.
    >>> print gtp_response_to_text('= C6 C4\n\n')
    C6 C4
    <BLANKLINE>
    <BLANKLINE>
    '''
    return gtp_response.strip('= ')


def gtp_response_to_dictionary(gtp_response):
    r'''GTP to Python dictionary.
    >>> gtp_response_to_dictionary('= \n\n')
    {}
    >>> places = gtp_response_to_dictionary('= C6 C4\n\n')
    >>> if not places == {'C6': True, 'C4': True}:
    ...     print places
    '''
    dictionary = {}
    for key in gtp_response_to_list(gtp_response):
        dictionary[key] = True
    return dictionary


def play_to_gtp(play_dictionary):
    r'''Convert an action and coordinate to GTP.
    >>> print play_to_gtp({'black':  [(2, 3)]})
    ['play black D7']
    >>> print play_to_gtp({'white':  [(1, 0)]})
    ['play white A8']
    >>> print play_to_gtp({'black':  [[2, 3], [3, 3]]})
    ['play black D7', 'play black D6']
    '''
    gtp_commands = []
    for color in ('black', 'white'):
        gtp_action = 'play ' + color
        positions = play_dictionary.get(color, [])
        for r, c in positions:
            gtp_coordinate = array_to_gtp(r, c)
            gtp_commands.append(
                gtp_action + ' ' + gtp_coordinate)
    return gtp_commands


def dictionary_to_gtp(action_dictionary):
    r'''Convert play, undo, showboard.
    >>> dictionary_to_gtp({'black':  [(2, 3)]})
    ['play black D7']
    >>> print dictionary_to_gtp({'white':  [(1, 0)]})
    ['play white A8']
    >>> print dictionary_to_gtp({'undo': 1})
    ['undo']
    >>> print dictionary_to_gtp({'loadsgf': 'sgf/white_tiger.sgf'})
    ['loadsgf sgf/white_tiger.sgf']
    >>> print dictionary_to_gtp({'printsgf': 'sgf/white_tiger.sgf'})
    ['printsgf sgf/white_tiger.sgf']
    >>> print dictionary_to_gtp({'undo': 1})
    ['undo']
    >>> print dictionary_to_gtp({'undo': 2})
    ['undo', 'undo']
    >>> print dictionary_to_gtp({'genmove': 'white'})
    ['genmove white']

    Not prepared to handle multiple commands.
    >>> print dictionary_to_gtp({'undo': 1, 'showboard': True})
    ['showboard']
    '''
    gtp_commands = []
    if 'black' in action_dictionary \
            or 'white' in action_dictionary:
        gtp_commands.extend(play_to_gtp(action_dictionary))
    elif 'undo' in action_dictionary:
        for number in range(action_dictionary['undo']):
            gtp_commands.append(action_dictionary.keys()[0])
    elif 'showboard' in action_dictionary \
            or 'clear_board' in action_dictionary:
        gtp_commands.append(action_dictionary.keys()[0])
    elif 'loadsgf' in action_dictionary:
        gtp_commands.append(
                'loadsgf' + ' ' + action_dictionary['loadsgf'])
    elif 'genmove' in action_dictionary:
        gtp_commands.append(
                'genmove' + ' ' + action_dictionary['genmove'])
    elif 'printsgf' in action_dictionary:
        gtp_commands.append(
                'printsgf' + ' ' + action_dictionary['printsgf'])
    else:
        print 'dictionary_to_gtp:  I was not planning on this action:  ' + action_dictionary.keys()[0]
        gtp_commands.append(action_dictionary.keys()[0])
    return gtp_commands




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
    >>> history = setup_load_example()
    >>> history
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
        old_territory_news = get_territory_news(
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
        self.now['territory'] = get_territory_news(
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
        self.now['territory'] = get_territory_news(
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

# Mark territory

wallis_territory_text = '=  -1.00  -1.00  -1.00  -1.00   0.00  -1.00  -1.00  -1.00   0.00 \n -1.00   0.00  -1.00  -2.00   0.00  -1.00   0.00   0.00   0.00 \n -1.00  -1.00   0.00   0.00   0.00   0.00   0.00   0.00   0.00 \n -1.00  -1.00   0.00   0.00   0.00   0.00   0.00   0.00   0.00 \n -1.00  -1.00   0.00   0.00   0.00   0.00   0.00   0.00   0.00 \n -1.00  -1.00   0.00   0.00   0.00   0.00   2.00   2.00   0.00 \n  0.00  -1.00   0.00   0.00   0.00   0.00   2.00   0.00   1.00 \n  0.00   0.00   0.00   0.00   0.00   0.00   2.00   0.00   1.00 \n  0.00   0.00   0.00   0.00   0.00   1.00   1.00   1.00   1.00 \n\n'


mostly_dead = 1 + 15.0 / 32

def get_territory_values(territory_values_text,
        mostly_dead = mostly_dead):
    '''
    >>> get_territory_values(wallis_territory_text)
    [[-1, -1, -1, -1, 0, -1, -1, -1, 0], [-1, 0, -1, -2, 0, -1, 0, 0, 0], [-1, -1, 0, 0, 0, 0, 0, 0, 0], [-1, -1, 0, 0, 0, 0, 0, 0, 0], [-1, -1, 0, 0, 0, 0, 0, 0, 0], [-1, -1, 0, 0, 0, 0, 2, 2, 0], [0, -1, 0, 0, 0, 0, 2, 0, 1], [0, 0, 0, 0, 0, 0, 2, 0, 1], [0, 0, 0, 0, 0, 1, 1, 1, 1]]
    '''
    # sometimes a value like 1.41 appears, which is close enough to dead.
    if not gtp_ok(territory_values_text):
        print 'get_territory_text(%s) # invalid gtp_response' \
                % (territory_values_text.__repr__())
    territory_values_text = territory_values_text \
            .lstrip(gtp_start_of_ok) \
            .rstrip(gtp_end_of_response)
    territory_values = []
    for line in territory_values_text.splitlines():
        line = line.split(' ')
        while '' in line:
            line.remove('')
        int_line = [int(float(i) * mostly_dead) 
                for i in line]
        territory_values.append(int_line)
    return territory_values

territory_values_dictionary = {
    -2:  'dead',
    -1:  'black',
     0:  'neutral',
     1:  'white',
     2:  'dead'
    }

def get_territory_labels(territory_values):
    '''
    >>> values = get_territory_values(wallis_territory_text)
    >>> get_territory_labels(values)
    [['black', 'black', 'black', 'black', 'neutral', 'black', 'black', 'black', 'neutral'], ['black', 'neutral', 'black', 'dead', 'neutral', 'black', 'neutral', 'neutral', 'neutral'], ['black', 'black', 'neutral', 'neutral', 'neutral', 'neutral', 'neutral', 'neutral', 'neutral'], ['black', 'black', 'neutral', 'neutral', 'neutral', 'neutral', 'neutral', 'neutral', 'neutral'], ['black', 'black', 'neutral', 'neutral', 'neutral', 'neutral', 'neutral', 'neutral', 'neutral'], ['black', 'black', 'neutral', 'neutral', 'neutral', 'neutral', 'dead', 'dead', 'neutral'], ['neutral', 'black', 'neutral', 'neutral', 'neutral', 'neutral', 'dead', 'neutral', 'white'], ['neutral', 'neutral', 'neutral', 'neutral', 'neutral', 'neutral', 'dead', 'neutral', 'white'], ['neutral', 'neutral', 'neutral', 'neutral', 'neutral', 'white', 'white', 'white', 'white']]
    
    Mostly dead is dead too.
    >>> old_values = get_territory_values(mostly_dead_territory_text)
    >>> old_labels = get_territory_labels(old_values)
    >>> old_labels[7][6]
    'dead'
    '''
    territory_labels = []
    for row in territory_values:
        territory_labels.append( [] )
        for value in row:
            territory_labels[-1].append( 
                territory_values_dictionary[value] )
    return territory_labels

mostly_dead_territory_text = '=  -1.00  -1.00  -1.00  -1.00   0.00  -1.00  -1.00  -1.00   0.00 \n -1.00   0.00  -1.00  -2.00   0.00  -1.00   0.00   0.00   0.00 \n -1.00  -1.00   0.00   0.00   0.00   0.00   0.00   0.00   0.00 \n -1.00  -1.00   0.00   0.00   0.00   0.00   0.00   0.00   0.00 \n -1.00  -1.00   0.00   0.00   0.00   0.00   0.00   0.00   0.00 \n -1.00  -1.00   0.00   0.00   0.00   0.00   2.00   2.00   0.00 \n  0.00  -1.00   0.00   0.00   0.00   0.00   2.00   0.00   1.00 \n  0.00   0.00   0.00   0.00   0.00   0.00   1.41   0.00   1.00 \n  0.00   0.00   0.00   0.00   0.00   1.00   1.00   1.00   1.00 \n\n'

wallis_territory2_text = '=  -1.00  -1.00  -1.00  -1.00   0.00  -1.00  -1.00  -1.00   0.00 \n -1.00   0.00  -1.00  -2.00   0.00  -1.00   0.00   0.00   0.00 \n -1.00  -1.00   0.00   0.00   0.00   0.00   0.00   0.00   0.00 \n -1.00  -1.00   0.00   0.00   0.00   0.00   0.00   0.00   0.00 \n -1.00  -1.00   0.00   0.00   0.00   0.00   0.00   0.00   0.00 \n -1.00  -1.00   0.00   0.00   0.00   0.00   1.00   1.00   0.00 \n  0.00  -1.00   0.00   0.00   0.00   0.00   1.00   0.00   1.00 \n  0.00   0.00   0.00   0.00   0.00   0.00   1.00   0.00   1.00 \n  0.00   0.00   0.00   0.00   0.00   1.00   0.00   1.00   1.00 \n\n'

def get_territory_news(old_labels, new_labels):
    '''
    >>> old_values = get_territory_values(wallis_territory_text)
    >>> old_labels = get_territory_labels(old_values)
    >>> new_values = get_territory_values(wallis_territory2_text)
    >>> new_labels = get_territory_labels(new_values)
    >>> get_territory_news(old_labels, new_labels)
    {'white': [(5, 6), (5, 7), (6, 6), (7, 6)], 'neutral': [(8, 6)]}
    >>> get_territory_news([[], []], [['dead'],['black']])
    {'dead': [(1, 0)], 'black': [(1, 1)]}
    '''
    territory_now = {}
    simulcast = zip(enumerate(old_labels), new_labels)
    for (r, old_row), new_row in simulcast:
        simultaneous = zip(enumerate(old_row), new_row)
        for (c, old_label), new_label in simultaneous:
            if old_label != new_label:
                draw(territory_now, new_label, (r, c))
    return territory_now
    

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


def estimate_black_score(territory_values):
    '''Estimate score from territory values.
    >>> values = get_territory_values(wallis_territory_text)
    >>> estimate_black_score(values)
    7
    '''
    sum = 0
    for values in territory_values:
        for value in values:
            sum += value
    return 0 - sum


# ActionScript algorithms

def get_connected(board_lines):
    '''Ordering clockwise (north, east, south, west)
    >>> connected = get_connected(board_lines)
    >>> connected[0][1]
    [False, True, False, True]
    >>> connected[1][1]
    [False, True, True, False]
    >>> connected[2][2]
    [True, True, True, True]
    >>> connected[2][2]
    [True, True, True, True]
    >>> connected[3][3]
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
                cell[north] = board_cell == board_lines[r-1][c]
            if len(board_lines[r]) - 1 == c:
                cell[east] = False
            else:
                cell[east] = board_cell == board_lines[r][c+1]
            if len(board_lines) - 1 == r:
                cell[south] = False
            else:
                cell[south] = board_cell == board_lines[r+1][c]
            if 0 == c:
                cell[west] = False
            else:
                cell[west] = board_cell == board_lines[r][c-1]
    return neighbors


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
    '''
    if is_empty(neighbor):
        return False
    if board_cell == neighbor:
        return False
    return True


def get_blocks(board_lines):
    '''Block means neighbor is off board or an attacker.  Block takes away a liberty.
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
            if is_empty(board_cell):
                neighbors[r][c] = [False, False, False, False]
            else:
                cell = neighbors[r][c]
                if 0 == r:
                    cell[north] = True
                else:
                    neighbor = board_lines[r-1][c]
                    cell[north] = is_blocked(board_cell, neighbor)
                if len(board_lines[r]) - 1 == c:
                    cell[east] = True
                else:
                    neighbor = board_lines[r][c+1]
                    cell[east] = is_blocked(board_cell, neighbor)
                if len(board_lines) - 1 == r:
                    cell[south] = True
                else:
                    neighbor = board_lines[r+1][c]
                    cell[south] = is_blocked(board_cell, neighbor)
                if 0 == c:
                    cell[west] = True
                else:
                    neighbor = board_lines[r][c-1]
                    cell[west] = is_blocked(board_cell, neighbor)
    return neighbors


def get_labels(connected):
    '''
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

def text_mask(positions):
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
    '''
    return doctest_board(
            map_at_position(
                lambda i: '#', clear_board, positions))

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


def history_to_text(history):
    '''9x9 text board from history of up to 80 moves.
    Does not mark hidden.
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

    Pass and resign are not recorded.
    >>> referee.history.append({'white':  'pass'})
    >>> referee.history.append({'white':  'resign'})
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
    #if 82 < len(history):
    #    print 'history_to_text:  I only have marks for 82 moves'
    event_board = []
    for row in range(9):
        event_board.append( ['. '] * 9 )
    for turn, event in enumerate(history):
        event_board = set_event_mark_row_column(
                turn, event, event_board)
    event_board_text = '  0 1 2 3 4 5 6 7 8 '
    for r, row in enumerate(event_board):
        event_board_text += '\n' + str(r) + ' ' + ''.join(row)
    return event_board_text


wallis_history_text = ''' 0 1 2 3 4 5 6 7 8 
0 XX. . . XBOAOCOEXH
1 . XD. OGXvOyXzXFXT
2 . . X2X5OwX7X1XROS
3 . . XtOYOuXlXVXnOQ
4 . . Xj. OiXhOkOmOU
5 . . X9. OcOgXbXpOq
6 XL. X0XfXdOeX3Oo. 
7 XNXJXxO8OMOaXrOs. 
8 XPOKOIOOO6. OW. . '''

def history_text_to_board(history_text):
    '''Convert history text of board to a board.
    >>> print wallis_history_text
      0 1 2 3 4 5 6 7 8 
    0 XX. . . XBOAOCOEXH
    1 . XD. OGXvOyXzXFXT
    2 . . X2X5OwX7X1XROS
    3 . . XtOYOuXlXVXnOQ
    4 . . Xj. OiXhOkOmOU
    5 . . X9. OcOgXbXpOq
    6 XL. X0XfXdOeX3Oo. 
    7 XNXJXxO8OMOaXrOs. 
    8 XPOKOIOOO6. OW. . 
    >>> pb(history_text_to_board(wallis_history_text))
    X...XOOOX
    .X.OXOXXX
    ..XXOXXXO
    ..XOOXXXO
    ..X.OXOOO
    ..X.OOXXO
    X.XXXOXO.
    XXXOOOXO.
    XOOOO.O..
    '''
    board_text = ''
    for line in history_text.splitlines()[1:]:
        for i in range(2, len(line), 2):
            board_text += line[i]
        board_text += '\n'
    return text_to_array(board_text)


def set_event_mark_row_column(turn, event, event_board):
    move = None
    for color in 'black', 'white':
        if color in event:
            move = event[color]
            break
    if move and 'resign' != move and 'pass' != move:
        mark = eval(color)
        history_marks = r'0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()-=_+[]{}<>/?'
        event_mark = mark + history_marks[turn]
        row, column = move
        event_board[row][column] = event_mark
    return event_board

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



def sgf_comment_example():
    r'''You can add a comment to a node and read it.
    >>> tree = sgflib.GameTree(nodelist=None, variations=None)
    >>> node = tree.makeNode([sgflib.Property('W', ['ba'])])
    >>> node = get_node(tree, 'white', 0, 1)
    >>> print node
    ;W[ba]
    >>> comment = node.makeProperty('C', [str(node)])
    >>> node.addProperty(comment)

    I guess each character is escaped to avoid node confusion?
    >>> print node
    ;W[ba]C[;W[ba\]]

    For a sane view:
    >>> ''.join(node.data['C'].data)
    ';W[ba]'
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




def get_sgf_tree(history):
    r'''Supports black, white, hide, unhide, pass, resign.
    >>> print get_sgf_tree([{'black': (0, 1)}])
    (;GM[1]SZ[9];B[ba])
    >>> print get_sgf_tree([{'black': (0, 1), 'hide': [(0, 1)]}])
    (;GM[1]SZ[9];MA[ba])

    Unhide before play.
    append hide as a null move comment.
    two passes in a row would end game.
    >>> print get_sgf_tree([{'black': (0, 1), 'hide': [(0, 1)]}, 
    ...     {'white': (1, 0)},
    ...     {'black': (0, 0)},
    ...     {'white': (1, 1), 'unhide': [(0, 1), (1, 2)]}  ]) #doctest: +NORMALIZE_WHITESPACE
    (;GM[1]SZ[9];MA[ba];W[ab];B[aa];B[ba][cb]CR[ba][cb]W[bb])
    
    >>> print get_sgf_tree([{'white': 'pass'}]) 
    (;GM[1]SZ[9];W[tt])
    >>> print get_sgf_tree([{'white': 'resign'}]) 
    (;GM[1]SZ[9]RE[B+Resign])
    >>> print get_sgf_tree([{'black': (0, 1), 'extra_stone_gift': '_1'}])
    (;GM[1]SZ[9];B[ba]C[extra_stone_gift _1])
    >>> unhide = [{'black_last_move': [(4, 3)], 'black': (4, 3), 'empty': [(3, 3)], 'unhide': [(3, 2)]}]
    >>> print get_sgf_tree(unhide)
    (;GM[1]SZ[9];B[cd][de]CR[cd])
    '''
    tree = sgflib.GameTree(nodelist=None, variations=None)
    node = tree.makeNode([sgflib.Property(sgf_game, [sgf_go_game]), sgflib.Property('SZ', ['9'])])
    #>>> print node
    ##;GM[1]SZ[9]
    tree.append(node)
    #>>> print tree
    ##(;GM[1]SZ[9])
    colors = 'black', 'white'
    for event in history:
        node = tree.makeNode([])
        append_node = True
        if 'unhide' in event.keys():
            unhides = event['unhide']
            coordinates = [ get_coordinates(*unhide)
                for unhide in unhides ]
            play_property = sgflib.Property(sgf_black, 
                    copy.deepcopy(coordinates))
            node.addProperty(play_property)
            unhide_property = sgflib.Property(sgf_unhide, 
                    copy.deepcopy(coordinates))
            node.addProperty(unhide_property)
        for color in colors:
            if color in event.keys():
                move = event[color]
                if 'pass' == move:
                    pass_property = sgflib.Property(
                            get_sgf_color(color), [sgf_pass])
                    node.addProperty(pass_property)
                elif 'resign' == move:
                    if 'black' == color:
                        winner = 'white'
                    else:
                        winner = 'black'
                    sgf_result = 'RE'
                    result = '%s+%s' %  \
                    (get_sgf_color(winner), sgf_resign)
                    tree[0].addProperty(
                        sgflib.Property(sgf_result, 
                            [result]) )
                    append_node = False
                else:
                    #node = get_node(tree, color, row, column)
                    row, column = event[color]
                    hides = event.get('hide', [])
                    for hide in hides:
                        if (row, column) == hide:
                            annotate(node, sgf_hide, row, column)
                    if not hides:
                        if not get_sgf_color(color) in node.data:
                            add_move(node, color, row, column)
                        else:
                            append_move(node, color, 
                                    row, column)
        event_gift_list = []
        for gift in 'extra_stone_gift', 'hide_gift', 'extra_stone':
            if gift in event:
                event_gift_list.append( '%s %s' % (gift, event[gift]) )
        if event_gift_list:
            comment = node.makeProperty(sgf_comment, 
                event_gift_list)
            node.addProperty(comment)
        if append_node:
            tree.append(node)
    #>>> print tree
    ##(;GM[1]SZ[9];W[aa])
    #>>> str(tree)
    ##'(;GM[1]SZ[9];W[aa];W[ab])'
    return tree


def parse(sgf_tree_text):
    '''Text of one game to SGF tree.
    >>> print parse('(;GM[1]SZ[9];B[ba])')
    (;GM[1]SZ[9];B[ba])
    '''
    parser = sgflib.SGFParser(str(sgf_tree_text))
    collection = parser.parseOneGame()
    return collection


def get_history(sgf_tree):
    r'''Convert SGF text into history.
    Supports black, white, hide, unhide, pass, resign.
    >>> get_history( parse('(;GM[1]SZ[9];B[ba])') )
    [{'black': (0, 1)}]
    >>> get_history( parse('(;GM[1]SZ[9];MA[ba])') )
    [{'black': (0, 1), 'hide': [(0, 1)]}]

    Unhide before play.
    append hide as a null move comment.
    two passes in a row would end game.
    >>> hide_unhide_sgf = parse('(;GM[1]SZ[9];MA[ba];W[ab];B[aa];B[ba][cb]CR[ba][cb]W[bb])')
    >>> get_history( hide_unhide_sgf ) # doctest: +NORMALIZE_WHITESPACE
    [{'black': (0, 1), 'hide': [(0, 1)]}, {'white': (1, 0)}, {'black': (0, 0)}, {'white': (1, 1), 'unhide': [(0, 1), (1, 2)]}]
    >>> get_history( parse('(;GM[1]SZ[9];W[tt])') )
    [{'white': 'pass'}]
    >>> get_history( parse('(;GM[1]SZ[9]RE[B+Resign])') )
    [{'white': 'resign'}]
    >>> get_history( parse('(;GM[1]SZ[9];B[ba]C[extra_stone_gift _1])') )
    [{'black': (0, 1), 'extra_stone_gift': '_1'}]
    >>> get_history( parse('(;GM[1]SZ[9];AB[aa][ab][ba])') )
    [{'black': (0, 0)}, {'black': (1, 0)}, {'black': (0, 1)}]
    '''
    history = []
    end = []
    for node in sgf_tree:
        if sgf_game in node.keys():
            # XXX no example for this block!
            for property in node:
                if sgf_game == property.id:
                    if sgf_go_game != property.data[0]:
                        print 'get_history:  I only parse Go games, not:  %s in %s' % (property, node)
                elif sgf_size == property.id:
                    if sgf_size_9 != property.data[0]:
                        print 'get_history:  I only parse 9x9 Go games, not:  %s in %s' % (property, node)
                elif sgf_result == property.id:
                    result = property.data[0]
                    if result.startswith(sgf_black):
                        if result.endswith(sgf_resign) or result.endswith(sgf_resign2):
                            end.append( {'white': 'resign'} )
                    elif result.startswith(sgf_white):
                        if result.endswith(sgf_resign) or result.endswith(sgf_resign2):
                            end.append( {'black': 'resign'} )
                    else:
                        print 'get_history:  what do i do with this result?  %s in %s' % (property, node)
                elif property.id in sgf_add_stone_dictionary:
                    history = _insert_add_stone(history, property)
                else:
                    print 'get_history:  what do i do with this id?  %s' % (property.id)
        else:
            event = {}
            for property in node:
                event = _insert_hide_black(event, property)
            for property in node:
                event = _insert_move(event, property)
            for property in node:
                event = _insert_gift(event, property)
            if event:
                history.append(event)
            for property in node:
                history = _insert_add_stone(history, property)
    history.extend(end)
    return history


def sgf_to_history(file):
    sgf_text = text.load(file)
    history = get_history(parse(sgf_text))
    return history


def _insert_move(dictionary, property):
    '''After unhide, so unhidden are not duplicated as moves.
    >>> insert_move({}, property) #doctest: +SKIP
    {'black': (0, 1)}
    '''
    if str(property.id) in sgf_move_dictionary:
        key = sgf_move_dictionary.get(property.id)
        sgf_move = property.data[0]
        if sgf_pass == sgf_move:
            dictionary[key] = 'pass'
        else:
            position = get_position(sgf_move)
            if position not in dictionary.get('unhide', []):
                dictionary[key] = position
    return dictionary


def _insert_add_stone(history, property):
    '''add several stones'''
    if str(property.id) in sgf_add_stone_dictionary:
        key = sgf_add_stone_dictionary.get(property.id)
        sgf_moves = property.data
        for sgf_move in sgf_moves:
            event = {}
            position = get_position(sgf_move)
            event[key] = position
            history.append(event)
    return history


def _insert_hide_black(dictionary, property):
    id = str(property.id)
    if id in sgf_hide_dictionary:
        if sgf_hide == id:
            hide = sgf_hide_dictionary.get(property.id) 
            position = get_position(property.data[0])
            draw(dictionary, hide, position)
            dictionary['black'] = position
        elif sgf_unhide == id:
            unhide = sgf_hide_dictionary.get(property.id) 
            positions = [ get_position(sgf_coordinate)
                for sgf_coordinate in property.data ]
            draw(dictionary, unhide, *positions)
    return dictionary


def _insert_gift(dictionary, property):
    if str(property.id) == sgf_comment:
        key = sgf_move_dictionary.get(property.id)
        comments = property.data
        for comment in comments:
            for gift in 'extra_stone_gift', 'hide_gift', 'extra_stone':
                if comment.startswith(gift):
                    gift_name, value = comment.split(' ')
                    dictionary[gift_name] = value
    return dictionary


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


import sgflib
import text
sgf_pass = 'tt'
sgf_resign = 'Resign'
sgf_resign2 = 'Resign'
sgf_comment = 'C'
sgf_result = 'RE'
sgf_game = 'GM'
sgf_size = 'SZ'
sgf_size_9 = '9'
sgf_go_game = '1'
sgf_cross = 'MA'
sgf_circle = 'CR'
sgf_black = 'B'
sgf_white = 'W'
sgf_add_black = 'AB'
sgf_add_white = 'AW'

sgf_hide = sgf_cross
sgf_unhide = sgf_circle

sgf_pass_dictionary = {
    sgf_pass:   'pass',
    'R':    'resign',
    'Resign':   'resign',
    #'1':    'go',
        }

sgf_move_dictionary = {
    sgf_black:    'black',
    sgf_white:    'white',
        }

sgf_add_stone_dictionary = {
    sgf_add_black:    'black',
    sgf_add_white:    'white',
        }

sgf_hide_dictionary = {
    sgf_hide:    'hide',
    sgf_unhide:    'unhide',
        }


def set_comment(node, comment_text):
    comment = node.makeProperty(sgf_comment, [comment_text])
    node.addProperty(comment)
    return node

def annotate(node, id, row, column):
    coordinate = get_coordinates(row, column)
    property = node.makeProperty(id, [coordinate])
    node.addProperty(property)
    return node

def get_coordinates(row, column):
    #                  012345678
    sgf_coordinates = 'abcdefghijklmnopqrstuvwxyz'
    sgf_position = sgf_coordinates[column] \
            + sgf_coordinates[row]
    return sgf_position

def get_position(sgf_coordinate):
    '''
    >>> get_position('ba')
    (0, 1)
    '''
    #                  012345678
    sgf_coordinates = 'abcdefghijklmnopqrstuvwxyz'
    row = sgf_coordinates.index(sgf_coordinate[1])
    column = sgf_coordinates.index(sgf_coordinate[0])
    return row, column

def get_sgf_color(color):
    sgf_color = color.capitalize()[0]
    return sgf_color

def get_node(tree, color, row, column):
    '''
    >>> tree = sgflib.GameTree(nodelist=None, variations=None)
    >>> node = get_node(tree, 'white', 0, 1)
    >>> print node
    ;W[ba]
    '''
    sgf_color = get_sgf_color(color)
    sgf_position = get_coordinates(row, column)
    node = tree.makeNode([sgflib.Property(
        sgf_color, [sgf_position])])
    return node

def add_move(node, color, row, column):
    sgf_color = get_sgf_color(color)
    sgf_position = get_coordinates(row, column)
    node.addProperty( sgflib.Property(
        sgf_color, [sgf_position] ) )
    return node

def append_move(node, color, row, column):
    sgf_color = get_sgf_color(color)
    sgf_position = get_coordinates(row, column)
    node[sgf_color].data.append(sgf_position)
    return node

def get_custom_node(tree, id, row, column):
    '''
    >>> tree = sgflib.GameTree(nodelist=None, variations=None)
    >>> node = get_custom_node(tree, sgf_cross, 0, 1)
    >>> print node
    ;MA[ba]
    '''
    sgf_position = get_coordinates(row, column)
    node = tree.makeNode([sgflib.Property(
        id, [sgf_position])])
    return node


def get_property(id, row, column):
    sgf_position = get_coordinates(row, column)
    property = sgflib.Property(id, [sgf_position])
    return property


# Match Patterns
# My ideas and patterns, 
# mostly from experience and Learn to Play Go by Janice Kim, 
# following simpler formatting conventions in GnuGo patterns.db
# For example, see extra_stone_example

pre_jump_board_text = '''
,,,,,,,,,
,,,,,,,,,
,,,,,,X,,
,,,,,,,,,
,,,,,,,,,
,,O,,,,,,
,,,,,,,,,
,,,,,,,,,
,,,,,,,,,
'''
pre_jump_board = text_to_array(pre_jump_board_text)
jump_board_text = '''
,,,,,,,,,
,,,,,,,,,
,,,,X,X,,
,,,,,,,,,
,,,,,,,,,
,,O,,,,,,
,,,,,,,,,
,,,,,,,,,
,,,,,,,,,
'''
jump_board = text_to_array(jump_board_text)
jump_board2_text = '''
,,,,,,,,,
,,,,,,,,,
,,,,X,X,,
,,,,X,,,,
,,,,,,,,,
,,O,,,,,,
,,,,,,,,,
,,,,,,,,,
,,,,,,,,,
'''
jump_board2 = text_to_array(jump_board2_text)
jump_pattern_text = '''
Pattern formation_jump

oOo
...
o*o
?.?

:|,C,shape(5)
'''
jump_attack_board_text = '''
,,,,,,,,,
,,,,,,,,,
,,,,O,X,,
,,,,,,,,,
,,,,,,,,,
,,O,,,,,,
,,,,,,,,,
,,,,,,,,,
,,,,,,,,,
'''
jump_attack_board = text_to_array(jump_attack_board_text)
jump_attack_board2_text = '''
,,,,,,,,,
,,,,,,,,,
,,,,O,X,,
,,,,,,X,,
,,,,,,,,,
,,O,,,,,,
,,,,,,,,,
,,,,,,,,,
,,,,,,,,,
'''
jump_attack_board2 = text_to_array(jump_attack_board2_text)
jump_attack_pattern_text = '''
Pattern formation_jump_attack

?X?
...
o*o
?o?

:|,C,shape(5)
'''

diagonal_board_text = '''
,,,,,,,,,
,,,,,X,,,
,,,,,,X,,
,,,,,,,,,
,,,,,,,,,
,,,,,,,,,
,,,,,,,,,
,,,,,,,,,
,,,,,,,,,
'''
diagonal_board = text_to_array(diagonal_board_text)
diagonal_board2_text = '''
,,,,,,,,,
,,,,,X,,,
,,,,,,X,,
,,,,,,X,,
,,,,,,,,,
,,,,,,,,,
,,,,,,,,,
,,,,,,,,,
,,,,,,,,,
'''
diagonal_board2 = text_to_array(diagonal_board2_text)
diagonal_pattern_text = '''
Pattern formation_diagonal

?.O
o*.
?o?

:/,C,shape(3)
'''
diagonal_attack_board_text = '''
,,,,,,,,,
,,,,,O,,,
,,,,,,X,,
,,,,,,,,,
,,,,,,,,,
,,,,,,,,,
,,,,,,,,,
,,,,,,,,,
,,,,,,,,,
'''
diagonal_attack_board = text_to_array(diagonal_attack_board_text)
diagonal_attack_pattern_text = '''
Pattern formation_diagonal_attack
??.?
?.X.
o*.?
?o??

:/,C,shape(3)
'''

knight_board_text = '''
,,,,,,,,,
,,,,,,,,,
,,,,,,X,,
,,,,X,,,,
,,,,,,,X,
,,,,,,,,,
,,,,,,,,,
,,,,,,,,,
,,,,,,,,,
'''
knight_board = text_to_array(knight_board_text)
knight_pattern_text = '''
Pattern formation_knight

?oO
?..
.*.
?.?

:8,C,shape(4)
'''
knight_attack_board_text = '''
,,,,,,,,,
,,,,,,,,,
,,,,,,X,,
,,,,O,,,,
,,,,,,,O,
,,,,,,,,,
,,,,,,,,,
,,,,,,,,,
,,,,,,,,,
'''
knight_attack_board = text_to_array(knight_attack_board_text)
knight_attack_pattern_text = '''
Pattern formation_knight_attack

?xX
?..
.*.
?.?

:8,C,shape(4)
'''

leap_board_text = '''
,,,,,,,,,
,,,,,,,,,
,,,X,,X,,
,,,,,,,,,
,,,,,,,,,
,,O,,,,,,
,,,,,,,,,
,,,,,,,,,
,,,,,,,,,
'''
leap_board = text_to_array(leap_board_text)
leap_pattern_text = '''
Pattern formation_leap

oOo
...
...
o*o
?.?

:|,C,shape(5)
'''
leap_attack_board_text = '''
,,,,,,,,,
,,,,,,,,,
,,,O,,X,,
,,,,,,,,,
,,,,,,,,,
,,O,,,,,,
,,,,,,,,,
,,,,,,,,,
,,,,,,,,,
'''
leap_attack_board = text_to_array(leap_attack_board_text)
leap_attack_pattern_text = '''
Pattern formation_leap_attack

?X?
...
...
o*o
?o?

:|,C,shape(5)
'''

field_board_text = '''
,,,,,,,,,
,,,,,,,,,
,,,,,,X,,
,,,,,,,,,
,,,,,,,,,
,,O,,,,,,
,,,,,,,,,
,,,,,,,,,
,,,,,,,,,
'''
field_board = text_to_array(field_board_text)
field_pattern_text = '''
Pattern formation_field

.....
.....
..*..
.....
.....

:+,C,shape(15)
'''

dog_mouth_pattern_text = '''
Pattern formation_dog_mouth

?????
?O.O?
?...?
??*??
??.??

:/,C,shape(3)
'''

pattern_mark_dictionary = {
        'X':  enemy,
        'O':  ally,
        # if i don't write an example that requires the code, and i don't write the code, then all code has an example.
        '?':  are_we_on_board,
        '.':  am_i_empty_but_not_you,
        '*':  ally,
        'o':  ally_or_empty,
        'x':  enemy_or_empty,
        #' ':  are_we_on_board,  # if space is preserved.
    }


no_symmetry_rotates = ['rotate_0', 'rotate_90', 
    'rotate_180', 'rotate_270', 
    'row_reflect_rotate_0', 'row_reflect_rotate_90', 
    'row_reflect_rotate_180', 'row_reflect_rotate_270']

axis_1_rotates = ['rotate_0', 'rotate_90', 
    'rotate_180', 'rotate_270']

cross_rotates = ['rotate_0']

symmetry_rotates = {
        '|':  axis_1_rotates,
        '-':  axis_1_rotates,
        '/':  axis_1_rotates,
        '+':  cross_rotates,
        '8':  no_symmetry_rotates,
        }

off_board_mark = '#'

def get_rotates(symmetry):
    if symmetry not in symmetry_rotates:
            print 'get_rotates:  Am I prepared to transform along this symmetry %s' % symmetry
    rotates = symmetry_rotates.get(symmetry, [])
    return rotates


def get_matches(pattern_dictionary, 
        board, last_row, last_column):
    r'''Useful for last or next position.
    >>> pattern_dictionary = get_pattern_dictionary(pattern_texts)
    >>> history = [{'black': (2, 6)}, 
    ...     {'white': (5, 2)}, 
    ...     {'black': (2, 4)}]
    >>> print history_to_text(history)
      0 1 2 3 4 5 6 7 8 
    0 . . . . . . . . . 
    1 . . . . . . . . . 
    2 . . . . X2. X0. . 
    3 . . . . . . . . . 
    4 . . . . . . . . . 
    5 . . O1. . . . . . 
    6 . . . . . . . . . 
    7 . . . . . . . . . 
    8 . . . . . . . . . 
    >>> last_event = history[-1]
    >>> get_color_row_column(last_event)
    ('black', 2, 4)
    >>> last_color, last_row, last_column = \
    ...     get_color_row_column(last_event)
    >>> get_matches(pattern_dictionary,
    ...       jump_board,  last_row,   last_column)
    [['formation_jump', 'rotate_90']]

    #>>> pb(pattern_dictionary['formation_jump']['rotate_90']['pattern'])
    ?o.o
    .*.O
    ?o.o
    >>> get_matches(pattern_dictionary, jump_board, 2, 4)
    [['formation_jump', 'rotate_90']]
    >>> get_matches(pattern_dictionary, jump_board, 2, 2)
    []
    >>> get_matches(pattern_dictionary, jump_board, 5, 4)
    []
    >>> get_matches(pattern_dictionary, jump_board, 2, 8)
    []
    >>> get_matches(pattern_dictionary, jump_board, 5, 8)
    []
    >>> get_matches(pattern_dictionary, jump_board, 2, 0)
    []
    >>> get_matches(pattern_dictionary, jump_board, 5, 0)
    []
    >>> matches = get_matches(pattern_dictionary, pre_jump_board, 2, 6)
    >>> get_matches(pattern_dictionary, pre_jump_board, 2, 5)
    []
    >>> get_matches(pattern_dictionary, pre_jump_board, 2, 4)
    []

    Match knight
    >>> matches = get_matches(pattern_dictionary, knight_board, 2, 6) # doctest: +NORMALIZE_WHITESPACE
    >>> if not ['formation_knight', 'row_reflect_rotate_0'] in matches or not ['formation_knight', 'row_reflect_rotate_90'] in matches:  matches

    Match diagonal
    >>> matches = get_matches(pattern_dictionary, diagonal_board,  
    ...     2, 6) # doctest: +NORMALIZE_WHITESPACE
    >>> if not ['formation_diagonal', 'rotate_270'] in matches:  matches
    
    Match optional diagonal
    >>> matches = get_matches(pattern_dictionary, diagonal_board2,  
    ...     2, 6) # doctest: +NORMALIZE_WHITESPACE
    >>> if not ['formation_diagonal', 'rotate_270'] in matches:  matches
    
    Match diagonal_attack
    >>> matches = get_matches(pattern_dictionary, diagonal_attack_board,  
    ...     2, 6) # doctest: +NORMALIZE_WHITESPACE
    >>> if not ['formation_diagonal_attack', 'rotate_270'] in matches:  matches
    
    Match optional jump
    >>> matches = get_matches(pattern_dictionary, jump_board2,  
    ...     2, 6) # doctest: +NORMALIZE_WHITESPACE
    >>> if not ['formation_jump', 'rotate_270'] in matches:  matches

    Match jump_attack
    >>> matches = get_matches(pattern_dictionary, jump_attack_board,  
    ...     2, 6) # doctest: +NORMALIZE_WHITESPACE
    >>> if not ['formation_jump_attack', 'rotate_270'] in matches:
    ...     matches

    Match optional jump_attack
    >>> matches = get_matches(pattern_dictionary, jump_attack_board2,  
    ...     2, 6) # doctest: +NORMALIZE_WHITESPACE
    >>> if not ['formation_jump_attack', 'rotate_270'] in matches:
    ...     matches

    Match knight_attack
    >>> matches = get_matches(pattern_dictionary, knight_attack_board, 2, 6) # doctest: +NORMALIZE_WHITESPACE
    >>> if not ['formation_knight_attack', 'row_reflect_rotate_0'] in matches or not ['formation_knight_attack', 'row_reflect_rotate_90'] in matches:
    ...     matches
    
    Match leap
    >>> matches = get_matches(pattern_dictionary, leap_board,  
    ...     2, 6) # doctest: +NORMALIZE_WHITESPACE
    >>> if not ['formation_leap', 'rotate_270'] in matches:
    ...     matches

    Match leap_attack
    >>> matches = get_matches(pattern_dictionary, leap_attack_board,  
    ...     2, 6) # doctest: +NORMALIZE_WHITESPACE
    >>> if not ['formation_leap_attack', 'rotate_270'] in matches:
    ...     matches

    Match field
    >>> matches = get_matches(pattern_dictionary, field_board, 2, 6)
    >>> if not ['formation_field', 'rotate_0'] in matches:
    ...     matches
    '''
    matches = []
    for name, transformations in pattern_dictionary.items():
        rotates = get_rotates(transformations['symmetry'])
        for rotate in rotates:
            match_marks = transformations[rotate]['match']
            origin_row, origin_column = transformations[rotate]['origin']
            if is_exact_match(match_marks, 
                    origin_row, origin_column,
                    board,  last_row,   last_column):
                matches.append([name, rotate])
    return matches
    

def is_exact_match(match_marks, origin_row, origin_column, 
        board, last_row, last_column):
    r'''Does the block of the board match this rotation of the pattern?
    >>> history = [{'black': (2, 6)}, 
    ...     {'white': (5, 2)}, 
    ...     {'black': (2, 4)}]
    >>> print history_to_text(history)
      0 1 2 3 4 5 6 7 8 
    0 . . . . . . . . . 
    1 . . . . . . . . . 
    2 . . . . X2. X0. . 
    3 . . . . . . . . . 
    4 . . . . . . . . . 
    5 . . O1. . . . . . 
    6 . . . . . . . . . 
    7 . . . . . . . . . 
    8 . . . . . . . . . 
    >>> last_event = history[-1]
    >>> get_color_row_column(last_event)
    ('black', 2, 4)
    >>> last_color, last_row, last_column = \
    ...     get_color_row_column(last_event)
    >>> name, pattern, attributes = get_name_pattern_attributes(
    ...     jump_pattern_text)
    >>> match_marks = get_match_marks(pattern)
    >>> origin_row, origin_column = get_origin_row_column(pattern)
    >>> is_exact_match(match_marks, origin_row, origin_column,
    ...                jump_board,  last_row,   last_column)
    False
    >>> is_exact_match(match_marks, origin_row, origin_column,
    ...                jump_board,  last_row,   0)
    False
    >>> is_exact_match(match_marks, origin_row, origin_column,
    ...                jump_board,  last_row,   0)
    False
    '''
    if not in_bounds(last_row, last_column):
        print 'is_exact_match:  I am not prepared for last_move off_board:  %s, %s' % (last_row, last_column)
    you = board[last_row][last_column]
    board_row = last_row - origin_row
    board_column = last_column - origin_column
    board_row_max = board_row + len(match_marks)
    # XXX hard to read
    board_row_range = range(board_row, board_row_max)
    for match_row, row in zip(match_marks, board_row_range):
        board_column_max = board_column + len(match_row)
        board_column_range = range(board_column, board_column_max)
        for match, column in zip(match_row, board_column_range):
            if in_bounds(row, column):
                mark = board[row][column]
            else:
                mark = off_board_mark
            if not match(mark, you):
                return False
    return True

    
def get_name_pattern_attributes(pattern_text):
    '''What is the name, pattern, and attributes of this simple db?
    >>> name, pattern, attributes = get_name_pattern_attributes(
    ...     jump_pattern_text)
    >>> name
    'formation_jump'
    >>> pattern
    ['oOo', '...', '.*.', '?.?']
    >>> attributes
    ['|', 'C', 'shape(5)']
    >>> name, pattern, attributes = get_name_pattern_attributes(
    ...     knight_pattern_text)
    >>> name
    'formation_knight'
    '''
    lines = text_to_lines(pattern_text)
    name = lines.pop(0).lstrip('Pattern')
    attributes = []
    pattern = lines
    for line in lines:
        if line.startswith(':'):
            pattern.remove(line)
            attributes.extend( line.strip(':').split(',') )
    return name, pattern, attributes


def get_origin_row_column(pattern):
    '''Which row and and column is the first '*' found?
    >>> name, pattern, attributes = get_name_pattern_attributes(
    ...     jump_pattern_text)
    >>> get_origin_row_column(pattern)
    (2, 1)
    >>> get_origin_row_column(rotate_90(pattern))
    (1, 1)
    '''
    for row, line in enumerate(pattern):
        if '*' in line:
            # no index for tuple
            # www.diveintopython.org/getting_to_know_python/tuples.html
            column = list(line).index('*')
            origin_row, origin_column = row, column
            return origin_row, origin_column


def get_match_marks(pattern):
    '''Generate pattern functions from shorthand text diagram.
    >>> name, pattern, attributes = get_name_pattern_attributes(
    ...     jump_pattern_text)
    >>> match_marks = get_match_marks(pattern)
    '''
    match_marks = []
    for row in pattern:
        match_marks.append( [] )
        for pattern_mark in row:
            is_pattern = pattern_mark_dictionary[pattern_mark]
            match_marks[-1].append(is_pattern)
    return match_marks



def rotate_examples():
    '''Rotate a board image.
    Ragged tables are truncated.
    >>> prevent_diagonal_cut_pattern = [['O', '*'], ['X', 'O']]
    >>> rotate_0(prevent_diagonal_cut_pattern)
    [['O', '*'], ['X', 'O']]
    >>> rotate_90(prevent_diagonal_cut_pattern)
    [('X', 'O'), ('O', '*')]
    >>> rotate_90(rotate_90(prevent_diagonal_cut_pattern))
    [('O', 'X'), ('*', 'O')]
    >>> rotate_180(prevent_diagonal_cut_pattern)
    [('O', 'X'), ('*', 'O')]
    >>> rotate_90(rotate_90(rotate_90(prevent_diagonal_cut_pattern)))
    [('*', 'O'), ('O', 'X')]
    >>> rotate_270(prevent_diagonal_cut_pattern)
    [('*', 'O'), ('O', 'X')]
    >>> rotate_90(rotate_90(rotate_90(rotate_90(prevent_diagonal_cut_pattern))))
    [('O', '*'), ('X', 'O')]

    String form of pattern okay too.
    >>> prevent_diagonal_cut = [['O', '*'], ['X', 'O']]
    >>> pb(prevent_diagonal_cut)
    O*
    XO
    >>> pb(rotate_90(prevent_diagonal_cut))
    XO
    O*

    Reflect enables covering all eight variants
    for patterns with no symmetry.
    >>> extend = [['.', 'X'], ['*', 'O']]
    >>> pb(rotate_0(extend))
    .X
    *O
    >>> pb(rotate_90(extend))
    *.
    OX
    >>> pb(rotate_180(extend))
    O*
    X.
    >>> pb(rotate_270(extend))
    XO
    .*
    >>> pb(row_reflect_rotate_0(extend))
    *O
    .X
    >>> pb(row_reflect_rotate_90(extend))
    .*
    XO
    >>> pb(row_reflect_rotate_180(extend))
    X.
    O*
    >>> pb(row_reflect_rotate_270(extend))
    OX
    *.
    >>> connect = [['.', '.'], ['*', 'O'], ['O', 'X']]
    >>> pb(connect)
    ..
    *O
    OX
    >>> pb(rotate_90(connect))
    O*.
    XO.
    >>> numbers = [range(3), range(3, 6), range(6, 9), range(9, 6, -1)]
    >>> pb(numbers)
    012
    345
    678
    987
    >>> pb(rotate_90(numbers))
    9630
    8741
    7852
    >>> pb(row_reflect_rotate_90(numbers))
    0369
    1478
    2587
    '''

def row_reflect_rotate_0(pattern):
    '''
    >>> pattern = ['?O?', '...', '.*.', '?.?']
    >>> row_reflect_rotate_0(pattern)
    ['?.?', '.*.', '...', '?O?']
    '''
    upside_down = []
    for row in pattern:  
        upside_down.insert(0, row)
    return upside_down

def rotate_0(table):
    return table

def rotate_90(table):
    # I saw Chad Miller's post on this neat hack with zip.
    return zip(*row_reflect_rotate_0(table))

def rotate_180(table):
    return rotate_90(rotate_90(table))

def rotate_270(table):
    return row_reflect_rotate_0(zip(*table))

def row_reflect_rotate_90(table):
    return rotate_90(row_reflect_rotate_0(table))

def row_reflect_rotate_180(table):
    return rotate_180(row_reflect_rotate_0(table))

def row_reflect_rotate_270(table):
    return rotate_270(row_reflect_rotate_0(table))

def get_pattern_dictionary(pattern_texts):
    '''Generate four rotations of vertical or horizontal symmetry patterns.
    >>> pattern_dictionary = get_pattern_dictionary(pattern_texts)
    >>> get_matches(pattern_dictionary,
    ...       jump_board, 2, 6)
    [('formation_jump', 'rotate_270')]
    '''
    pattern_dictionary = {}
    for pattern_text in pattern_texts:
        name, pattern, attributes = get_name_pattern_attributes(
            pattern_text)
        symmetry = attributes.pop(0)
        classification = attributes.pop(0)
        values = attributes
        pattern_dictionary[name] = {
                'symmetry':  symmetry,
                'classification':  classification,
                'values':  values
                }
        for rotate in get_rotates(symmetry):
            rotated_pattern = eval(rotate)(pattern)
            match_marks = get_match_marks(rotated_pattern)
            origin = get_origin_row_column(rotated_pattern)
            pattern_dictionary[name][rotate] = {
                'pattern': rotated_pattern,
                'match': match_marks,
                'origin':  origin,
                }
    return pattern_dictionary


pattern_texts = [
    jump_pattern_text,
    jump_attack_pattern_text,
    knight_pattern_text,
    knight_attack_pattern_text,
    diagonal_pattern_text,
    diagonal_attack_pattern_text,
    leap_pattern_text,
    leap_attack_pattern_text,
    field_pattern_text,
    dog_mouth_pattern_text,
    ]

# only need to generate this once per game
pattern_dictionary = get_pattern_dictionary(pattern_texts)



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


import code_unit

if __name__ == '__main__':
    import sys
    code_unit.test_file_args('./referee.py', sys.argv,
            locals(), globals())

