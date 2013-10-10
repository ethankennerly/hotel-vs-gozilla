#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
Relay from GnuGo to Flash Client
gtp:  Go Text Protocol
amf:  ActionScript Messaging Format
'''
__author__ = 'Ethan Kennerly'


def example():
    '''Make a move in GnuGo and see the board.
    >>> gtp_envoy = setup_envoy(configuration.gtp_path, 'localhost', 5903)
    >>> print talk(gtp_envoy, 'showboard')
    = 
       A B C D E F G H J
     9 . . . . . . . . . 9
     8 . . . . . . . . . 8
     7 . . + . . . + . . 7
     6 . . . . . . . . . 6
     5 . . . . + . . . . 5
     4 . . . . . . . . . 4
     3 . . + . . . + . . 3
     2 . . . . . . . . . 2     WHITE (O) has captured 0 stones
     1 . . . . . . . . . 1     BLACK (X) has captured 0 stones
       A B C D E F G H J
    <BLANKLINE>
    <BLANKLINE>
    >>> print talk(gtp_envoy, 'play black C3')
    = 
    <BLANKLINE>
    <BLANKLINE>
    >>> print talk(gtp_envoy, 'showboard')
    = 
       A B C D E F G H J
     9 . . . . . . . . . 9
     8 . . . . . . . . . 8
     7 . . + . . . + . . 7
     6 . . . . . . . . . 6
     5 . . . . + . . . . 5
     4 . . . . . . . . . 4
     3 . . X . . . + . . 3
     2 . . . . . . . . . 2     WHITE (O) has captured 0 stones
     1 . . . . . . . . . 1     BLACK (X) has captured 0 stones
       A B C D E F G H J
    <BLANKLINE>
    <BLANKLINE>
    '''


def dragon_critical_crash_example():
    '''Crash GnuGo. Why?  Excluded from global test.
    >>> from configuration import *
    >>> gtp_envoy = setup_envoy(configuration.gtp_path, configuration.gtp_host, configuration.gtp_port)
    >>> turn_to_move = talk(gtp_envoy, 'loadsgf sgf/eye_critical_example.sgf')
    >>> critical = talk(gtp_envoy, 'dragon_status A2')
    '''


def dragon_status_crash_example():
    '''Crash GnuGo.  Why?  exclude from global test.
    >>> from configuration import *
    >>> gtp_envoy = setup_envoy(configuration.gtp_path, configuration.gtp_host, configuration.gtp_port)
    >>> print talk(gtp_envoy, 'loadsgf sgf/eye_example.sgf')
    = black
    <BLANKLINE>
    <BLANKLINE>
    >>> print talk(gtp_envoy, 'showboard')
    = 
       A B C D E F G H J
     9 . . . . . . . . . 9
     8 . . . . . . . . . 8
     7 . . + . . . + . . 7
     6 . . . . . . . . . 6
     5 . . . . + . . . . 5
     4 . . . . . . . . . 4
     3 O O O O . . + . . 3
     2 X X X X . . . . . 2     WHITE (O) has captured 0 stones
     1 . . . X . . . . . 1     BLACK (X) has captured 0 stones
       A B C D E F G H J
    <BLANKLINE>
    <BLANKLINE>
    >>> print talk(gtp_envoy, 'dragon_status A2')
    = alive
    <BLANKLINE>
    <BLANKLINE>
    >>> print talk(gtp_envoy, 'white E2')
    = 
    <BLANKLINE>
    <BLANKLINE>

    Dragon status.  GnuGo crash.  Why?
    >>> print talk(gtp_envoy, 'dragon_status A2')
    talk(dragon_status A2):  socket error <class 'socket.error'>:  "(10054, 'Connection reset by peer')"
    talk(dragon_status A2):  socket error <class 'socket.error'>:  "(10054, 'Connection reset by peer')"
    '''

    
import time
import subprocess
def setup_gtp(gtp_path, gtp_port):
    '''In a subprocess, start a program for an artificial go player.
    >>> gtp_pid = setup_gtp(configuration.gtp_path, configuration.gtp_port)
    '''
    #- base_command = 'gnugo-3.8.exe'
    #- import os
    # dirname = os.path.abspath('.')
    # command = dirname + '/' + configuration.computer_start
    #- command = os.path.join(os.getcwd(), 
    #-        os.path.dirname(__file__),
    #-        base_command)
            # configuration.computer_start)
    # command = dirname + '/gnugo_port' + str(gtp_port) + '.bat'
    options = ['--gtp-listen', '%i' % gtp_port, 
            '--mode', 'gtp', '--boardsize', '9', '--level', '1']

    command_log = '%s %s' % (gtp_path, options)
    import logging
    logging.info(command_log)
    try:
        gtp_pid = subprocess.Popen([gtp_path] + options).pid
    except:
        print 'setup_gtp', gtp_path
        print 'The system cannot find the file specified'
        raise
    ## # if complaint that GTP is not ready yet, then sleep first.
    time.sleep(2)
    return gtp_pid



def exec_gtp(gtp_path, sgf_file, gtp_input):
    r'''In a subprocess, start a program for an artificial go player and wait for its result.
    For example:
    gnugo-3.8.exe --mode gtp --boardsize 9 --level 1\
            --infile sgf/eye_critical_example.sgf 
            --gtp-input sgf/dragon_status.gtp   
    where the gtp-input file contains:  dragon_status A2
    >>> print exec_gtp(configuration.gtp_path, 'sgf/eye_critical_example.sgf', 'dragon_status A2')
    = critical B1 B1
    <BLANKLINE>
    <BLANKLINE>
    >>> print exec_gtp(configuration.gtp_path, 'sgf/eye_critical_example.sgf', 'dragon_status A2')
    = critical B1 B1
    <BLANKLINE>
    <BLANKLINE>
    >>> print exec_gtp(configuration.gtp_path, 'sgf/eye_critical_example.sgf', 'showboard')
    = 
       A B C D E F G H J
     9 . . . . . . . . . 9
     8 . . . . . . . . . 8
     7 . . + . . . + . . 7
     6 . . . . . . . . . 6
     5 . . . . + . . . . 5
     4 . . . . . . . . . 4
     3 O O O O . . + . . 3
     2 X X X X O . . . . 2     WHITE (O) has captured 0 stones
     1 . . . X . . . . . 1     BLACK (X) has captured 0 stones
       A B C D E F G H J
    <BLANKLINE>
    <BLANKLINE>

    If memory set to 512 (-M 512), this takes over half a second to execute.
    Whereas, without, the speed is fast.
    >>> import timeit
    >>> timer = timeit.Timer(stmt="exec_gtp(configuration.gtp_path, 'sgf/eye_critical_example.sgf', 'dragon_status A2')", setup="from go_text_protocol import exec_gtp, configuration")
    >>> duration = timer.timeit(10)
    >>> duration < 0.5
    True
    '''
    gtp_input_file = 'sgf/__input.gtp'
    response_file = 'sgf/__response.gtp'
    text.save(gtp_input_file, gtp_input + gtp_end_of_response)
    options = ['--mode', 'gtp', '--boardsize', '9', '--level', '1',
            '--infile', sgf_file,
            '--gtp-input', gtp_input_file]
    command_log = '%s %s' % (gtp_path, options)
    import logging
    logging.info(command_log)
    # Delete contents of response file.
    text.save(response_file, '...')
    out = open(response_file, 'w')
    try:
        process = subprocess.Popen([gtp_path] + options, 
                stdout = out)
    except:
        print 'setup_gtp', gtp_path
        print 'The system cannot find the file specified'
        raise
    out.close()
    response = open(response_file, 'r')
    response_string = ''
    line = response.readline()
    while not response_string.endswith(gtp_end_of_response):
        response_string += line
        line = response.readline()
    return response_string


#- migrated to smart_go_format
#- def save_sgf(history, path):
#-     sgf_tree = get_sgf_tree(history)
#-     text.save(path, str(sgf_tree))



def get_dragon_status(sgf_file, row, column, size = 9):
    '''Coordinates of a dragon that are in critical condition.
    >>> sgf_file = 'sgf/eye_example.sgf'
    >>> status_attack_defense = get_dragon_status(sgf_file, 7, 3)
    >>> status_attack_defense
    ['alive']
    >>> sgf_file = 'sgf/eye_critical_example.sgf'
    >>> status_attack_defense = get_dragon_status(sgf_file, 7, 3)
    >>> status_attack_defense
    ['critical', (8, 1), (8, 1)]
    >>> status_attack_defense = get_dragon_status(sgf_file, 4, 3, 5)
    >>> status_attack_defense
    ['critical', (4, 1), (4, 1)]
    '''
    coordinate_gtp = array_to_gtp(row, column, size)
    gtp_input = 'dragon_status %s' % coordinate_gtp
    response_gtp = exec_gtp(configuration.gtp_path, sgf_file, gtp_input)
    return parse_dragon_status_coordinates(response_gtp, size)


def parse_dragon_status_coordinates(response_gtp, size = 9):
    r'''
    >>> response_gtp = '= critical A3 PASS\n\n'
    >>> parse_dragon_status_coordinates(response_gtp, 3)
    ['critical', (0, 0)]
    '''
    if not gtp_ok(response_gtp):
        print 'get_dragon_status: response_gtp = %s' % response_gtp
        return []
    status_attack_defense = gtp_response_to_list(response_gtp)
    if status_attack_defense:
        status_attack_defense_coordinates = [status_attack_defense[0]]
        for s, stone in enumerate(status_attack_defense[1:]):
            if 'PASS' != stone:
                coordinate = gtp_to_array(stone, size)
                if coordinate:
                    status_attack_defense_coordinates.append(coordinate)
                else:
                    print 'parse_dragon_status_coordinates:  what is this strange stone? %s' % stone
    return status_attack_defense_coordinates




def get_unconditional_status(sgf_file, row, column, size):
    '''Coordinates of a dragon that are in critical condition.
    >>> sgf_file = 'sgf/unconditional_status_example.sgf'
    >>> status = get_unconditional_status(sgf_file, 2, 0, 5)
    >>> status
    'alive'
    >>> status = get_unconditional_status(sgf_file, 1, 0, 5)
    >>> status
    'dead'
    >>> status = get_unconditional_status(sgf_file, 4, 3, 5)
    >>> status
    'undecided'
    '''
    coordinate_gtp = array_to_gtp(row, column, size)
    gtp_input = 'unconditional_status %s' % coordinate_gtp
    response_gtp = exec_gtp(configuration.gtp_path, sgf_file, gtp_input)
    if not gtp_ok(response_gtp):
        print 'get_unconditional_status: response_gtp = %s' % response_gtp
        return []
    status = gtp_response_to_list(response_gtp)[0]
    return status


def get_dragon_coordinates(sgf_file, row, column, size = 9):
    '''Coordinates of a dragon that are in critical condition.
    >>> sgf_file = 'sgf/eye_critical_example.sgf'
    >>> get_dragon_coordinates(sgf_file, 7, 3)
    [(7, 0), (7, 1), (7, 2), (7, 3), (8, 3)]
    >>> get_dragon_coordinates(sgf_file, 6, 3)
    [(6, 0), (6, 1), (6, 2), (6, 3)]
    '''
    coordinate_gtp = array_to_gtp(row, column, size)
    dragon_stones_gtp = 'dragon_stones %s' % coordinate_gtp
    stones_gtp = exec_gtp(configuration.gtp_path, sgf_file, dragon_stones_gtp)
    stones = gtp_response_to_list(stones_gtp)
    coordinates = [gtp_to_array(stone, size) for stone in stones]
    return coordinates


def get_attacker_critical_coordinates(sgf_file, attackers, size = 9):
    '''All critical coordinates of the attackers.
    >>> sgf_file = 'sgf/eye_example.sgf'
    >>> attackers = [(7, 3)]
    >>> dragons, vitals = get_attacker_critical_coordinates(sgf_file, attackers)
    >>> dragons
    []
    >>> vitals
    []

    >>> sgf_file = 'sgf/eye_critical_example.sgf'
    >>> attackers = [(7, 3)]
    >>> dragons, vitals = get_attacker_critical_coordinates(sgf_file, attackers)
    >>> dragons
    [(7, 0), (7, 1), (7, 2), (7, 3), (8, 3)]
    >>> vitals
    [(8, 1)]
    '''
    dragons = []
    vitals = []
    for r, c in attackers:
        status_attack_defense = get_dragon_status(sgf_file, r, c, size)
        if not status_attack_defense:
            print 'get_attacker_critical_coordinates: error:', status_attack_defense
            continue
        status = status_attack_defense[0]
        if not 'critical' == status:
            continue
        for point in status_attack_defense[1:]:
            if point not in vitals:
                vitals.append(point)
        dragon = get_dragon_coordinates(sgf_file, r, c, size)
        dragons.extend(dragon)
    return dragons, vitals


import socket

def setup_envoy(gtp_path, gtp_host, gtp_port):
    '''Must be setup before testing.
    >>> gtp_envoy = setup_envoy(configuration.gtp_path, configuration.gtp_host, configuration.gtp_port)
    '''
    gtp_pid = setup_gtp(gtp_path, gtp_port)
    envoy = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    if str != type(gtp_host):
        print 'setup_envoy(%s, %s) # gtp_host should be string' \
            % (gtp_host, gtp_port)
    try:
        envoy.connect((gtp_host, gtp_port))
    except:
        print 'setup_envoy(%s, %s) # exception' \
            % (gtp_host, gtp_port)
        raise
    envoy.settimeout(16)
    return envoy


def talk(envoy, gtp_command, delay = 1.0/256, verbose = False):
    r'''Send and receive in Go Text Protocol to GnuGo.
    Send full message and receive full message 
    and validate GTP format of a single response.
    Creating a second ambassador may corrupt responses.
    For examples, see update_gnugo_example.

    socket.error:  dragon_status_crash_example
    '''
    if verbose:
        print 'talk(%s)' % (gtp_command)
    gtp_string = str(gtp_command) + '\n'
    # docs.python.org/howto/sockets.html
    message_length = len(gtp_string)
    total_sent = 0
    while total_sent < message_length:
        sent = envoy.send(gtp_string[total_sent:])
        if 0 == sent:
            print 'RuntimeError socket connection broken'
        total_sent += sent
    # If waiting 1/128 or less, sometimes the message is truncated.
    # I guess there is a variable execution and socket delay.
    gtp_response = ''
    while not gtp_response.endswith(gtp_end_of_response):
        # http://bytes.com/topic/python/answers/22953-how-catch-socket-timeout
        time.sleep(delay)
        try:
            chunk = envoy.recv(1024)
            if '' == chunk:
                print 'talk(%s):  RuntimeError socket connection broken' % (gtp_command)
            gtp_response += chunk
        except socket.timeout:
            print 'talk(%s):  timeout:  gtp_response: "%s"' \
                    % (gtp_command, gtp_response.__repr__())
            return 'timeout'
        except socket.error:
            import sys
            error_number, error_string = sys.exc_info()[:2]
            
            error_message = 'talk(%s):  socket error %s:  "%s"' \
                        % (gtp_command, 
                                error_number, error_string)
            print error_message
            return error_message
    if not gtp_ok(gtp_response):
        print '''talk(%s) # GnuGo strange response:  "%s"''' \
                    % (gtp_command, gtp_response.__repr__())
        gtp_response = last_response(gtp_response)
    if verbose:
        print 'talk(%s) # gtp response:  "%s"' \
                % (gtp_command, gtp_response)
    return gtp_response



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



# index         0    1    2    3    4    5    6    7    8
column_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J']
row_list = [    9 ,  8 ,  7 ,  6 ,  5 ,  4 ,  3 ,  2 ,  1]

def array_to_gtp(row, column, size = 9):
    '''Map 2D array to 9x9 board as shown by GnuGo 3.8
    >>> array_to_gtp(0, 2)
    'C9'
    >>> array_to_gtp(2, 2)
    'C7'
    >>> array_to_gtp(1, 2)
    'C8'

    3x3 board
    >>> array_to_gtp(1, 2, 3)
    'C2'
    >>> array_to_gtp(4, 2, 3)
    array_to_gtp:  row out of bounds 4
    '''
    if row <= -1 or size <= row or len(row_list) <= row:
        print 'array_to_gtp:  row out of bounds %s' % row
        return
    if column <= -1 or size <= column or len(column_list) <= column:
        print 'array_to_gtp:  column out of bounds %s' % column
        return
    if size <= -1 or len(row_list) < size or len(column_list) < size:
        print 'array_to_gtp:  size out of bounds %s' % size
        return
    offset = len(row_list) - size
    return column_list[column] + str(row_list[row + offset])


def gtp_to_array(gtp_coordinate, size = 9):
    '''Map 9x9 board as shown by GnuGo 3.8 to 2D array.
    >>> gtp_to_array('A7')
    (2, 0)
    >>> gtp_to_array('C7')
    (2, 2)
    >>> gtp_to_array('PASS')
    gtp_to_array:  I only know how to handle 2 characters, not PASS
    >>> gtp_to_array('Z7')
    gtp_to_array:  column not found:  Z7

    >>> gtp_to_array('A3', 9)
    (6, 0)
    >>> gtp_to_array('A3', 3)
    (0, 0)
    >>> gtp_to_array('B3', 5)
    (2, 1)
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
    offset = len(row_list) - size
    row = row_list.index(gtp_row + offset)
    return row, column

def gtp_to_move(gtp_response, size = 9):
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
        return gtp_to_array(stone, size)

def gtp_response_to_stone(gtp_response):
    a_list = gtp_response_to_list(gtp_response)
    if a_list:
        return a_list[0]
    else:
        return


def gtp_response_to_coordinate(gtp_response, size = 9):
    r'''
    >>> gtp_response_to_coordinate('= C4\n\n')
    (5, 2)
    '''
    gtp_coordinate = gtp_response_to_stone(
            gtp_response)
    row, column = gtp_to_array(gtp_coordinate, size)
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



# Mark territory

wallis_territory_text = '=  -1.00  -1.00  -1.00  -1.00   0.00  -1.00  -1.00  -1.00   0.00 \n -1.00   0.00  -1.00  -2.00   0.00  -1.00   0.00   0.00   0.00 \n -1.00  -1.00   0.00   0.00   0.00   0.00   0.00   0.00   0.00 \n -1.00  -1.00   0.00   0.00   0.00   0.00   0.00   0.00   0.00 \n -1.00  -1.00   0.00   0.00   0.00   0.00   0.00   0.00   0.00 \n -1.00  -1.00   0.00   0.00   0.00   0.00   2.00   2.00   0.00 \n  0.00  -1.00   0.00   0.00   0.00   0.00   2.00   0.00   1.00 \n  0.00   0.00   0.00   0.00   0.00   0.00   2.00   0.00   1.00 \n  0.00   0.00   0.00   0.00   0.00   1.00   1.00   1.00   1.00 \n\n'


mostly_dead = 1 + 15.0 / 32
mostly_mine = 1.0 / 0.72
not_black = '-0.72'
black_dead = '1.41'

def scale_value(raw):
    '''
    >>> scale_value(not_black)
    0
    >>> scale_value(black_dead)
    2
    '''
    number = float(raw)
    if abs(number) <= 1:
        return int(number * mostly_mine)
    else:
        return int(number * mostly_dead)


def get_territory_values(territory_values_text):
    '''
    >>> from pprint import pprint
    >>> pprint(get_territory_values(wallis_territory_text))
    [[-1, -1, -1, -1, 0, -1, -1, -1, 0],
     [-1, 0, -1, -2, 0, -1, 0, 0, 0],
     [-1, -1, 0, 0, 0, 0, 0, 0, 0],
     [-1, -1, 0, 0, 0, 0, 0, 0, 0],
     [-1, -1, 0, 0, 0, 0, 0, 0, 0],
     [-1, -1, 0, 0, 0, 0, 2, 2, 0],
     [0, -1, 0, 0, 0, 0, 2, 0, 1],
     [0, 0, 0, 0, 0, 0, 2, 0, 1],
     [0, 0, 0, 0, 0, 1, 1, 1, 1]]
    >>> pprint(get_territory_values(mostly_dead_territory_text))
    [[-1, -1, -1, -1, 0, -1, -1, -1, 0],
     [-1, 0, -1, -2, 0, -1, 0, 0, 0],
     [-1, -1, 0, 0, 0, 0, 0, 0, 0],
     [-1, -1, 0, 0, 0, 0, 0, 0, 0],
     [-1, -1, 0, 0, 0, 0, 0, 0, 0],
     [-1, -1, 0, 0, 0, 0, 2, 2, 0],
     [0, -1, 0, 0, 0, 0, 2, 0, 1],
     [0, 0, 0, 0, 0, 0, 2, 0, 1],
     [0, 0, 0, 0, 0, 1, 1, 1, 1]]
    >>> get_territory_values(mostly_dead_territory_text)[7][6]
    2
    
    Distinguish suboptimal move in 5x5 board.
    >>> pprint(get_territory_values(beside_center_values_text))
    [[-1, -1, -1, -1, -1],
     [-1, -1, 0, -1, -1],
     [-1, -1, -1, -1, -1],
     [-1, 0, -1, 0, -1],
     [0, 0, 0, 0, 0]]
    >>> pprint(get_territory_values(center_values_text))
    [[-1, -1, -1, -1, -1],
     [-1, -1, -1, -1, -1],
     [-1, -1, 0, -1, -1],
     [-1, -1, -1, -1, -1],
     [-1, -1, -1, -1, -1]]
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
        int_line = [scale_value(i) for i in line]
        territory_values.append(int_line)
    return territory_values





neutral_territory_values_dictionary = {
    -2:  'neutral',
    -1:  'neutral',
     0:  'neutral',
     1:  'neutral',
     2:  'neutral'
    }

no_dead_territory_values_dictionary = {
    -2:  'black',
    -1:  'black',
     0:  'neutral',
     1:  'white',
     2:  'white'
    }

territory_values_dictionary = {
    -2:  'white_dead',
    -1:  'black',
     0:  'neutral',
     1:  'white',
     2:  'black_dead'
    }


def get_territory_labels(territory_values, 
        values_dictionary = territory_values_dictionary):
    '''
    >>> values = get_territory_values(wallis_territory_text)
    >>> get_territory_labels(values)
    [['black', 'black', 'black', 'black', 'neutral', 'black', 'black', 'black', 'neutral'], ['black', 'neutral', 'black', 'white_dead', 'neutral', 'black', 'neutral', 'neutral', 'neutral'], ['black', 'black', 'neutral', 'neutral', 'neutral', 'neutral', 'neutral', 'neutral', 'neutral'], ['black', 'black', 'neutral', 'neutral', 'neutral', 'neutral', 'neutral', 'neutral', 'neutral'], ['black', 'black', 'neutral', 'neutral', 'neutral', 'neutral', 'neutral', 'neutral', 'neutral'], ['black', 'black', 'neutral', 'neutral', 'neutral', 'neutral', 'black_dead', 'black_dead', 'neutral'], ['neutral', 'black', 'neutral', 'neutral', 'neutral', 'neutral', 'black_dead', 'neutral', 'white'], ['neutral', 'neutral', 'neutral', 'neutral', 'neutral', 'neutral', 'black_dead', 'neutral', 'white'], ['neutral', 'neutral', 'neutral', 'neutral', 'neutral', 'white', 'white', 'white', 'white']]
    
    Mostly dead is dead too.
    >>> old_values = get_territory_values(mostly_dead_territory_text)
    >>> old_labels = get_territory_labels(old_values)
    >>> old_labels[7][6]
    'black_dead'

    Optionally, do not show dead mark.
    >>> old_labels = get_territory_labels(old_values, 
    ...     no_dead_territory_values_dictionary)
    >>> old_labels[7][6]
    'white'
    '''
    territory_labels = []
    for row in territory_values:
        territory_labels.append( [] )
        for value in row:
            territory_labels[-1].append( 
                values_dictionary[value] )
    return territory_labels


mostly_dead_territory_text = '=  -1.00  -1.00  -1.00  -1.00   0.00  -1.00  -1.00  -1.00   0.00 \n -1.00   0.00  -1.00  -2.00   0.00  -1.00   0.00   0.00   0.00 \n -1.00  -1.00   0.00   0.00   0.00   0.00   0.00   0.00   0.00 \n -1.00  -1.00   0.00   0.00   0.00   0.00   0.00   0.00   0.00 \n -1.00  -1.00   0.00   0.00   0.00   0.00   0.00   0.00   0.00 \n -1.00  -1.00   0.00   0.00   0.00   0.00   2.00   2.00   0.00 \n  0.00  -1.00   0.00   0.00   0.00   0.00   2.00   0.00   1.00 \n  0.00   0.00   0.00   0.00   0.00   0.00   1.41   0.00   1.00 \n  0.00   0.00   0.00   0.00   0.00   1.00   1.00   1.00   1.00 \n\n'

wallis_territory2_text = '=  -1.00  -1.00  -1.00  -1.00   0.00  -1.00  -1.00  -1.00   0.00 \n -1.00   0.00  -1.00  -2.00   0.00  -1.00   0.00   0.00   0.00 \n -1.00  -1.00   0.00   0.00   0.00   0.00   0.00   0.00   0.00 \n -1.00  -1.00   0.00   0.00   0.00   0.00   0.00   0.00   0.00 \n -1.00  -1.00   0.00   0.00   0.00   0.00   0.00   0.00   0.00 \n -1.00  -1.00   0.00   0.00   0.00   0.00   1.00   1.00   0.00 \n  0.00  -1.00   0.00   0.00   0.00   0.00   1.00   0.00   1.00 \n  0.00   0.00   0.00   0.00   0.00   0.00   1.00   0.00   1.00 \n  0.00   0.00   0.00   0.00   0.00   1.00   0.00   1.00   1.00 \n\n'


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



beside_center_values_text = '''=  -1.00  -1.00  -1.00  -1.00  -1.00 
 -0.98  -1.00   0.00  -1.00  -0.98 
 -0.95  -0.73  -0.99  -0.73  -0.95 
 -0.73  -0.72  -0.73  -0.72  -0.73 
 -0.72  -0.72  -0.72  -0.72  -0.72

'''
center_values_text = '''=  -1.00  -1.00  -1.00  -1.00  -1.00 
 -1.00  -1.00  -1.00  -1.00  -1.00 
 -1.00  -1.00   0.00  -1.00  -1.00 
 -1.00  -1.00  -1.00  -1.00  -1.00 
 -1.00  -1.00  -1.00  -1.00  -1.00

'''

def score_5_5_example():
    '''Distinguish suboptimal move in 5x5 board.
    >>> pprint(get_territory_values(beside_center_values_text))
    [[-1, -1, -1, -1, -1],
     [-1, -1, 0, -1, -1],
     [-1, -1, -1, -1, -1],
     [-1, 0, -1, 0, -1],
     [0, 0, 0, 0, 0]]
    >>> pprint(get_territory_values(center_values_text))
    [[-1, -1, -1, -1, -1],
     [-1, -1, -1, -1, -1],
     [-1, -1, 0, -1, -1],
     [-1, -1, -1, -1, -1],
     [-1, -1, -1, -1, -1]]
    '''


# Delay dependence on Smart Go Format

import smart_go_format

import text
def update_gnugo(envoy, history, size = 9):
    sgf_tree = smart_go_format.get_sgf_tree(history, size)
    path = 'sgf/_update_gnugo.sgf'
    text.save(path, str(sgf_tree))
    return load_sgf(envoy, path)

def load_sgf(envoy, path = 'sgf/_update_gnugo.sgf'):
    # XXX why does ambassador's GnuGo sometimes load blank board?  
    # is an invalid move being appended to path?
    gtp_command = 'loadsgf ' + path + ' 999'
    return talk(envoy, gtp_command)

def get_score_and_territory(gtp_envoy):
    '''
    >>> gtp_envoy = setup_envoy(configuration.gtp_path, 'localhost', 5903)
    >>> next_player_gtp = update_gnugo(gtp_envoy, [])
    >>> score, territory_values = get_score_and_territory(gtp_envoy)
    >>> loaded = load_sgf(gtp_envoy, 'sgf/test_initial_influence.sgf')
    >>> score, territory_values = get_score_and_territory(gtp_envoy)
    >>> 0 == territory_values[5][5]
    True
    '''
    territory_gtp = 'initial_influence white territory_value'
    territory_text = talk(gtp_envoy, territory_gtp)
    territory_values = get_territory_values(territory_text)
    score = estimate_black_score(territory_values)
    return score, territory_values

def update_score_and_territory(gtp_envoy, history, size = 9,
        values_dictionary = territory_values_dictionary):
    '''
    >>> gtp_envoy = setup_envoy(configuration.gtp_path, 'localhost', 5903)
    >>> score, territory_labels = update_score_and_territory(gtp_envoy, [])
    >>> score, territory_labels = update_score_and_territory(gtp_envoy, [], size = 3)
    >>> score, territory_labels = update_score_and_territory(gtp_envoy, [], 
    ...     size = 3, values_dictionary = no_dead_territory_values_dictionary)
    '''
    next_player_gtp = update_gnugo(gtp_envoy, history, size) 
    score, territory_values = get_score_and_territory(gtp_envoy)
    territory_labels = get_territory_labels(territory_values, values_dictionary)
    return score, territory_labels


from smart_go_format import sgf_black, sgf_white
def final_score(gtp_envoy, offset_komi = 5.5):
    '''ask gnugo to score the game for black.
    Return estimate.  Offset compensation to white.
    XXX even when komi set to 0, in setup_score_example
    sometimes gnugo seems to get stuck on 5.5 for white.
    Must update gnugo beforehand.
    >>> gtp_envoy = setup_envoy(configuration.gtp_path, 'localhost', 5903)
    >>> next_player_gtp = update_gnugo(gtp_envoy, [], 3) 
    >>> final_score(gtp_envoy, 5.5)
    0
    >>> next_player_gtp = update_gnugo(gtp_envoy, [{'black': (1, 1)}, {'white': (0, 0)}, {'black': (0, 1)}, {'white': (1, 0)}, {'black': (2, 1)}], size = 3)
    >>> final_score(gtp_envoy, 5.5)
    8
    >>> print talk(gtp_envoy, 'showboard')
    = 
       A B C
     3 O X . 3
     2 O X . 2     WHITE (O) has captured 0 stones
     1 . X . 1     BLACK (X) has captured 0 stones
       A B C
    <BLANKLINE>
    <BLANKLINE>
    >>> print talk(gtp_envoy, 'final_score')
    = B+2.5
    <BLANKLINE>
    <BLANKLINE>
    '''
    score_gtp = talk(gtp_envoy, 'final_score')
    score_text = score_gtp.lstrip('= ').rstrip('\n\n')
    if score_text.startswith(sgf_black):
        score_value_text = score_text.lstrip(
                sgf_black + '+')
    elif score_text.startswith(sgf_white):
        score_value_text = '-' + score_text.lstrip(
                sgf_white + '+')
    else:
        print 'final_score:  what is this score_text? %s' % score_text
        print '    making up a score of 12 for now'
        score_value_text = '12'
    territory_score = int(float(score_value_text) 
            + offset_komi )
    return territory_score


def get_coordinate(gtp_envoy, gtp_input, board_size):
    '''Return row and column of top move.
    >>> gtp_envoy = setup_envoy(configuration.gtp_path, 'localhost', 5903)
    >>> sgf_file = 'sgf/test_initial_influence.sgf'
    >>> loaded = load_sgf(gtp_envoy, sgf_file)
    >>> row_column = get_coordinate(gtp_envoy, 'top_moves_white', 7)
    >>> row_column
    (5, 6)

    If hopeless for white, return nothing.
    >>> sgf_file = 'sgf/white_hopeless.sgf'
    >>> loaded = load_sgf(gtp_envoy, sgf_file)
    >>> row_column = get_coordinate(gtp_envoy, 'top_moves_white', 3)
    >>> row_column
    '''
    response_gtp = talk(gtp_envoy, gtp_input)
    moves_values = gtp_response_to_list(response_gtp)
    if not moves_values:
        return
    top_move = moves_values[0]
    row, column = gtp_to_array(top_move, board_size)
    return row, column


def get_top_coordinate_white(gtp_envoy, board_size):
    return get_coordinate(gtp_envoy, 'top_moves_white', board_size)


# Obsolete?  Not used anymore?

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


import code_unit
snippet = '''
import go_text_protocol; go_text_protocol = reload(go_text_protocol); from go_text_protocol import *
'''

import config
defaults = config.setup_defaults()
configuration = config.borg(defaults)

if __name__ == '__main__':
    import sys
    units = globals()
    units.pop('dragon_critical_crash_example')
    units.pop('dragon_status_crash_example')
    code_unit.test_file_args('./go_text_protocol.py', sys.argv,
            locals(), globals())

