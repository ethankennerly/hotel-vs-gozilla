#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
3x3, 5x5, 7x7, and 9x9 board examples.
'''
__author__ = 'Ethan Kennerly'

from client import *


# Other board sizes

def board_3_3_example():
    '''Joris captures in southeast corner of 3x3 board.
    >>> wait = 4.0
    >>> code_unit.inline_examples(
    ...     ethan_joris_start_example.__doc__, 
    ...     locals(), globals(), 
    ...     verify_examples = False)
    >>> andre = joris
    >>> wait = 4.0

    Joris presses 3x3.
    >>> mouse_down_and_sleep(joris, joris.root.game_over_mc._3_3_mc.enter_mc, wait / joris._speed)
    >>> property_diff(joris, joris.root, 'currentLabel', '_3_3')
    >>> property_diff(joris, joris.root.game_over_mc._3_3_mc.enter_mc, 'currentLabel', 'none')
    >>> property_diff(ethan, ethan.root, 'currentLabel', '_3_3')
    >>> property_diff(ethan, ethan.root.game_over_mc._3_3_mc.enter_mc, 'currentLabel', 'none')

    Joris captures.
    >>> mouse_down_and_sleep(joris, joris.root._1_2_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._1_2_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._2_2_mc, wait / ethan._speed)
    >>> joris.pb()
    ,,,
    ,,X
    ,,O
    >>> ethan.pb()
    ,,,
    ,,X
    ,,O
    >>> mouse_down_and_sleep(joris, joris.root._2_1_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._2_1_mc, wait / joris._speed)
    >>> joris.pb()
    ,,,
    ,,X
    ,X,
    >>> ethan.pb()
    ,,,
    ,,X
    ,X,
    >>> mouse_down_and_sleep(ethan, ethan.root._2_2_mc, wait / ethan._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._1_1_mc, wait / ethan._speed)
    >>> mouse_down_and_sleep(joris, joris.root._1_0_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._1_0_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._0_1_mc, wait / ethan._speed)
    >>> mouse_down_and_sleep(joris, joris.root._0_2_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._2_2_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._2_2_mc, wait / joris._speed)
    >>> joris.pb()
    ,O,
    XOX
    ,XX
    >>> ethan.pb()
    ,O,
    XOX
    ,XX
    >>> mouse_down_and_sleep(ethan, ethan.root._2_2_mc, wait / ethan._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._0_2_mc, wait / ethan._speed)
    >>> mouse_down_and_sleep(joris, joris.root._0_0_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._0_0_mc, wait / joris._speed) 
    >>> ethan.pb()
    X,,
    X,X
    ,XX
    '''


def board_5_5_example():
    '''Joris captures in southeast corner of 5x5 board.
    >>> wait = 4.0
    >>> code_unit.inline_examples(
    ...     ethan_joris_start_example.__doc__, 
    ...     locals(), globals(), 
    ...     verify_examples = False)
    >>> andre = joris
    >>> wait = 4.0

    Joris presses 5x5.
    >>> mouse_down_and_sleep(joris, joris.root.game_over_mc._5_5_mc.enter_mc, wait / joris._speed)
    >>> property_diff(joris, joris.root, 'currentLabel', '_5_5')
    >>> property_diff(joris, joris.root.game_over_mc._5_5_mc.enter_mc, 'currentLabel', 'none')
    >>> property_diff(ethan, ethan.root, 'currentLabel', '_5_5')
    >>> property_diff(ethan, ethan.root.game_over_mc._5_5_mc.enter_mc, 'currentLabel', 'none')

    Joris captures.
    >>> mouse_down_and_sleep(joris, joris.root._3_4_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._3_4_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._4_4_mc, wait / ethan._speed)
    >>> joris.pb()
    ,,,,,
    ,,,,,
    ,,,,,
    ,,,,X
    ,,,,O
    >>> ethan.pb()
    ,,,,,
    ,,,,,
    ,,,,,
    ,,,,X
    ,,,,O
    >>> mouse_down_and_sleep(joris, joris.root._4_3_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._4_3_mc, wait / joris._speed)
    >>> joris.pb()
    ,,,,,
    ,,,,,
    ,,,,,
    ,,,,X
    ,,,X,
    >>> ethan.pb()
    ,,,,,
    ,,,,,
    ,,,,,
    ,,,,X
    ,,,X,
    '''



def board_7_7_example():
    '''Joris captures in southeast corner of 7x7 board.
    >>> code_unit.inline_examples(
    ...     ethan_joris_start_example.__doc__, 
    ...     locals(), globals(), 
    ...     verify_examples = False)
    >>> andre = joris
    >>> wait = 4.0

    Joris presses 7x7.
    >>> mouse_down_and_sleep(joris, joris.root.game_over_mc._7_7_mc.enter_mc, wait / joris._speed)
    >>> property_diff(joris, joris.root, 'currentLabel', '_7_7')
    >>> property_diff(joris, joris.root.game_over_mc._7_7_mc.enter_mc, 'currentLabel', 'none')
    >>> property_diff(ethan, ethan.root, 'currentLabel', '_7_7')
    >>> property_diff(ethan, ethan.root.game_over_mc._7_7_mc.enter_mc, 'currentLabel', 'none')

    Joris captures.
    >>> mouse_down_and_sleep(joris, joris.root._5_6_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._5_6_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._6_6_mc, wait / ethan._speed)
    >>> joris.pb()
    ,,,,,,,
    ,,,,,,,
    ,,,,,,,
    ,,,,,,,
    ,,,,,,,
    ,,,,,,X
    ,,,,,,O
    >>> ethan.pb()
    ,,,,,,,
    ,,,,,,,
    ,,,,,,,
    ,,,,,,,
    ,,,,,,,
    ,,,,,,X
    ,,,,,,O
    >>> mouse_down_and_sleep(joris, joris.root._6_5_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._6_5_mc, wait / joris._speed)
    >>> joris.pb()
    ,,,,,,,
    ,,,,,,,
    ,,,,,,,
    ,,,,,,,
    ,,,,,,,
    ,,,,,,X
    ,,,,,X,
    >>> ethan.pb()
    ,,,,,,,
    ,,,,,,,
    ,,,,,,,
    ,,,,,,,
    ,,,,,,,
    ,,,,,,X
    ,,,,,X,
    '''


def count_5_5_snippet():
    '''Game has started.
    >>> wait = 4.0
    >>> mouse_down_and_sleep(joris, joris.root.game_over_mc._5_5_mc.enter_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._2_2_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._2_2_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._2_3_mc, wait / ethan._speed)
    >>> mouse_down_and_sleep(joris, joris.root._3_2_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._3_2_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._3_3_mc, wait / ethan._speed)
    >>> mouse_down_and_sleep(joris, joris.root._4_2_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._4_2_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._4_3_mc, wait / ethan._speed)
    >>> mouse_down_and_sleep(joris, joris.root._1_2_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._1_2_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._1_3_mc, wait / ethan._speed)
    >>> mouse_down_and_sleep(joris, joris.root._0_2_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._0_2_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._0_3_mc, wait / ethan._speed)
    >>> mouse_down_and_sleep(joris, joris.root._2_1_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._2_1_mc, wait / joris._speed)
    >>> joris.pb()
    ,,XO,
    ,,XO,
    ,XXO,
    ,,XO,
    ,,XO,

    >_<    black must play again to set score.
    '''

def connect_5_5_example():
    '''
    >>> code_unit.inline_examples(
    ...     ethan_joris_start_example.__doc__, 
    ...     locals(), globals(), 
    ...     verify_examples = False)
    >>> andre = joris
    >>> code_unit.inline_examples(
    ...     connect_5_5_snippet.__doc__, 
    ...     locals(), globals(), 
    ...     verify_examples = True)
    '''

def connect_5_5_snippet():
    '''Game has started.
    Joris presses 5x5.  Sequence then white computer.
    code_explorer usage >>> run_examples(shell, connect_5_5_snippet.__doc__)

    >>> wait = 4.0
    >>> mouse_down_and_sleep(joris, joris.root.game_over_mc._5_5_mc.enter_mc, wait / joris._speed)
    >>> # example.log level 20 at Mon Apr 26 12:53:11 2010
    >>> mouse_down_and_sleep(joris, joris.root._2_2_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._2_2_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._2_3_mc, wait / ethan._speed)
    >>> mouse_down_and_sleep(joris, joris.root._3_2_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._3_2_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._3_3_mc, wait / ethan._speed)
    >>> mouse_down_and_sleep(joris, joris.root._4_2_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._4_2_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._4_3_mc, wait / ethan._speed)
    >>> mouse_down_and_sleep(joris, joris.root._0_2_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._0_2_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._0_3_mc, wait / ethan._speed)
    >>> mouse_down_and_sleep(joris, joris.root._2_1_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._2_1_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._1_0_mc, wait / ethan._speed)
    >>> mouse_down_and_sleep(joris, joris.root._2_0_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._2_0_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._1_3_mc, wait / ethan._speed)
    >>> mouse_down_and_sleep(joris, joris.root._0_1_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._0_1_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._1_1_mc, wait / ethan._speed)
    >>> joris.pb()
    ,XXO,
    OO,O,
    XXXO,
    ,,XO,
    ,,XO,
    >>> mouse_down_and_sleep(joris, joris.root.game_over_mc.white_computer_mc.enter_mc, wait / joris._speed)
    >>> property_diff(joris, joris.root.game_over_mc.white_computer_mc, 'currentLabel', 'computer')
    '''



# Starting a game



def restart_example():
    '''Return to a game in progress.  Or start a new game.
    ethan and joris start.  
    >>> code_unit.inline_examples(
    ...     ethan_joris_start_example.__doc__, 
    ...     locals(), globals(), 
    ...     verify_examples = False)
    >>> andre = joris
    >>> wait = 4.0 / joris._speed

    joris plays and gets an extra piece of cake.  
    >>> joris.root.option_mc.extra_stone_available_mc.currentLabel
    '_4'
    >>> mouse_down_and_sleep(joris, joris.root._4_4_mc, wait)
    >>> mouse_down_and_sleep(joris, joris.root._4_4_mc, wait)
    >>> property_diff(joris, joris.root.extra_stone_gift_mc, 
    ...     'currentLabel', '_1')

    # joris exits to lobby.  
    # joris returns.
    # >>> mouse_down_and_sleep(joris, joris.root.menu_mc.toggle_mc, wait)
    # >>> mouse_down_and_sleep(joris, joris.root.menu_mc.lobby_mc, wait)
    # >>> property_diff(joris, joris.root['lobby_mc']['join_mc'], 'currentLabel', 
    # ...     'join')
    # >>> property_diff(joris, joris.root['lobby_mc']['join_mc']['join_txt'], 'text', 
    # ...     'ethan')
    # >>> mouse_down_and_sleep(joris, joris.root.lobby_mc.join_mc.enter_btn,
    # ...     wait)
    # >>> property_diff(joris, joris.root, 'currentLabel', 'table')
    # >>> board_diff(joris, joris.root._4_4_mc, 'currentLabel', 'black')
    # >>> board_diff(ethan, ethan.root._4_4_mc, 'currentLabel', 'black')

    ethan leaves table.  
    >>> mouse_down_and_sleep(ethan, ethan.root.menu_mc.toggle_mc, wait)
    >>> mouse_down_and_sleep(ethan, ethan.root.menu_mc.lobby_mc, wait)

    by ethan leaving, joris is also ejected.
    >>> joris.root.currentLabel
    'lobby'
    >>> joris.root.menu_mc.toggle_mc.dispatchEvent(mouseDown)
    >>> joris.root.menu_mc.lobby_mc.dispatchEvent(mouseDown)

    joris and ethan soon see lobby.  
    >>> property_diff(joris, joris.root, 'currentLabel', 'lobby')
    >>> property_diff(ethan, ethan.root, 'currentLabel', 'lobby')

    no room.  
    >>> property_diff(joris, joris.root['lobby_mc']['join_mc'], 'currentLabel', 
    ...     'none')
    >>> property_diff(joris, joris.root['lobby_mc']['join_mc']['join_txt'], 'text', 
    ...     '')

    ethan creates room.  

    Ethan has played before and wants to host a game.
    >>> mouse_down_and_sleep(ethan, ethan.root.lobby_mc.create_mc,
    ...     wait)
    
    Soon, Ethan enters a room.  Ethan sees board.
    >>> property_diff(ethan, ethan.root, 'currentLabel', 'table')

    Soon, white becomes selected, black is not selected.
    >>> property_diff(ethan, ethan.root.turn_mc, 'currentLabel', 'white')

    The white text changes to his name and black text is not his name.
    >>> property_diff(ethan, ethan.root.turn_mc.white_user_txt, 'text', 'ethan')
    >>> property_diff(ethan, ethan.root.turn_mc.black_user_txt, 'text', 'BLACK')
    
    ethan sees board is clear.  
    >>> board_diff(ethan, ethan.root._4_4_mc, 'currentLabel', 'empty_white')

    Meanwhile,
    joris sees room has same name as creator, ethan.  
    joris select room, ethan.  
    Joris sees Ethan's room.
    >>> property_diff(joris, joris.root['lobby_mc']['join_mc'], 'currentLabel', 
    ...     'join')
    >>> property_diff(joris, joris.root['lobby_mc']['join_mc']['join_txt'], 'text', 
    ...     'ethan')

    Joris clicks Ethan's room.
    >>> mouse_down_and_sleep(joris, joris.root.lobby_mc.join_mc.enter_btn,
    ...     wait)

    Soon Joris enters.  
    >>> property_diff(joris, joris.root, 'currentLabel', 'table')
    
    Joris sees he is playing as black by name and large icon.
    >>> property_diff(joris, joris.root['turn_mc'], 'currentLabel', 
    ...     'black')
    >>> property_diff(joris, joris.root['turn_mc']['black_user_txt'], 'text', 
    ...     'joris')

    Joris sees that Ethan is playing white by name.
    >>> property_diff(joris, joris.root['turn_mc']['white_user_txt'], 'text', 
    ...     'ethan')
   
    joris sees board is clear.  
    >>> board_diff(joris, joris.root._4_4_mc, 'currentLabel', 'empty_black')
    >>> board_diff(ethan, ethan.root._4_4_mc, 'currentLabel', 'empty_white')

    Joris has no extra pieces of cake.
    >>> property_diff(joris, joris.root.extra_stone_gift_mc, 
    ...     'currentLabel', '_0')

    Joris clicks button to start the game.
    >>> mouse_down_and_sleep(joris, joris.root.game_over_mc.start_mc, wait)

    #- Ethan clicks button to start the game.
    #- >>> mouse_down_and_sleep(ethan, ethan.root.game_over_mc.start_mc, wait)

    Start button resets.
    >>> property_diff(joris, joris.root.game_over_mc.start_mc, 'currentLabel', 'none')
    >>> property_diff(ethan, ethan.root.game_over_mc.start_mc, 'currentLabel', 'none')

    Soon, Joris sees it is his turn to move.
    >>> property_diff(joris, joris.root.turn_mc, 'currentLabel', 'black')
    >>> property_diff(joris, joris.root.turn_veil_mc, 'currentLabel', 'you')
    >>> property_diff(joris, joris.root.game_over_mc, 'currentLabel', 'none')

    Ethan sees it is Joris' turn to move.
    >>> property_diff(ethan, ethan.root.turn_mc, 'currentLabel', 'black')
    >>> property_diff(ethan, ethan.root.turn_veil_mc, 'currentLabel', 'other')
    >>> property_diff(ethan, ethan.root.game_over_mc, 'currentLabel', 'none')

    Joris sets board to 5x5.
    Joris presses 5x5.
    >>> mouse_down_and_sleep(joris, joris.root.game_over_mc._5_5_mc.enter_mc, wait)
    >>> property_diff(joris, joris.root, 'currentLabel', '_5_5')
    >>> property_diff(joris, joris.root.game_over_mc._5_5_mc.enter_mc, 'currentLabel', 'none')
    >>> property_diff(ethan, ethan.root, 'currentLabel', '_5_5')
    >>> property_diff(ethan, ethan.root.game_over_mc._5_5_mc.enter_mc, 'currentLabel', 'none')

    Joris moves.
    >>> board_diff(joris, joris.root._4_4_mc, 'currentLabel', 'empty_black')
    >>> board_diff(ethan, ethan.root._4_4_mc, 'currentLabel', 'empty_white')
    >>> mouse_down_and_sleep(joris, joris.root._4_4_mc, wait)
    >>> mouse_down_and_sleep(joris, joris.root._4_4_mc, wait)
    >>> board_diff(joris, joris.root._4_4_mc, 'currentLabel', 'black')
    >>> if board_diff(ethan, ethan.root._4_4_mc, 'currentLabel', 'black'):
    ...     print 'last time, embassy user.board_history was not cleared.'

    ethan removes table.  joris and ethan soon see lobby.  
    >>> mouse_down_and_sleep(ethan, ethan.root.menu_mc.toggle_mc, wait)
    >>> mouse_down_and_sleep(ethan, ethan.root.menu_mc.lobby_mc, wait)
    >>> property_diff(joris, joris.root, 'currentLabel', 'lobby')

    >>> property_diff(ethan, ethan.root, 'currentLabel', 'lobby')

    no room.  
    >>> property_diff(joris, joris.root['lobby_mc']['join_mc'], 'currentLabel', 
    ...     'none')
    >>> property_diff(joris, joris.root['lobby_mc']['join_mc']['join_txt'], 'text', 
    ...     '')

    ethan creates room.  

    Ethan has played before and wants to host a game.
    >>> mouse_down_and_sleep(ethan, ethan.root.lobby_mc.create_mc,
    ...     wait)

    To acknowledge, the create button is reset.
    >>> property_diff(ethan, ethan.root.lobby_mc.create_mc, 'currentLabel', 'none')

    Soon, Ethan enters a room.  Ethan sees board.
    >>> property_diff(ethan, ethan.root, 'currentLabel', 'table')

    Soon, white becomes selected, black is not selected.
    >>> property_diff(ethan, ethan.root.turn_mc, 'currentLabel', 'white')

    The white text changes to his name and black text is not his name.
    >>> property_diff(ethan, ethan.root.turn_mc.white_user_txt, 'text', 'ethan')
    >>> property_diff(ethan, ethan.root.turn_mc.black_user_txt, 'text', 'BLACK')
    
    ethan sees board is clear.  
    >>> board_diff(ethan, ethan.root._4_4_mc, 'currentLabel', 'empty_white')

    Meanwhile,
    joris sees room has same name as creator, ethan.  
    joris select room, ethan.  
    Joris sees Ethan's room.
    >>> property_diff(joris, joris.root['lobby_mc']['join_mc'], 'currentLabel', 
    ...     'join')
    >>> property_diff(joris, joris.root['lobby_mc']['join_mc']['join_txt'], 'text', 
    ...     'ethan')

    Joris clicks Ethan's room.
    >>> mouse_down_and_sleep(joris, joris.root.lobby_mc.join_mc.enter_btn,
    ...     wait)

    Soon Joris enters.  
    >>> property_diff(joris, joris.root, 'currentLabel', 'table')

    joris and ethan see 9x9 board.
    >>> len(joris.intersection_mc_array)
    9
    >>> len(ethan.intersection_mc_array)
    9
    
    joris sees board is clear.  
    >>> board_diff(joris, joris.root._4_4_mc, 'currentLabel', 'empty_black')
    >>> board_diff(ethan, ethan.root._4_4_mc, 'currentLabel', 'empty_white')

    Joris has no extra pieces of cake.
    >>> property_diff(joris, joris.root.extra_stone_gift_mc, 
    ...     'currentLabel', '_0')

    Joris clicks button to start the game.
    >>> mouse_down_and_sleep(joris, joris.root.game_over_mc.start_mc, wait)

    #- Ethan clicks button to start the game.
    #- >>> mouse_down_and_sleep(ethan, ethan.root.game_over_mc.start_mc, wait)
    
    Joris sets board to 5x5.
    Joris presses 5x5.
    >>> mouse_down_and_sleep(joris, joris.root.game_over_mc._5_5_mc.enter_mc, wait)
    >>> property_diff(joris, joris.root, 'currentLabel', '_5_5')
    >>> property_diff(joris, joris.root.game_over_mc._5_5_mc.enter_mc, 'currentLabel', 'none')
    >>> property_diff(ethan, ethan.root, 'currentLabel', '_5_5')
    >>> property_diff(ethan, ethan.root.game_over_mc._5_5_mc.enter_mc, 'currentLabel', 'none')

    Updating size of board updates empty blocks at edge of board.
    >>> black.root.option_mc.empty_block_mc.currentLabel
    'show'
    >>> black.root._4_0_mc.empty_block_west_mc.currentLabel
    'block'
    >>> black.root._4_4_mc.empty_block_east_mc.currentLabel
    'block'

    Joris moves.
    >>> board_diff(joris, joris.root._4_4_mc, 'currentLabel', 'empty_black')
    >>> board_diff(ethan, ethan.root._4_4_mc, 'currentLabel', 'empty_white')
    >>> mouse_down_and_sleep(joris, joris.root._4_4_mc, wait)
    >>> mouse_down_and_sleep(joris, joris.root._4_4_mc, wait)
    >>> board_diff(joris, joris.root._4_4_mc, 'currentLabel', 'black')
    >>> board_diff(ethan, ethan.root._4_4_mc, 'currentLabel', 'black')
    '''

def restart_problem_example():
    '''After preview, supposedly any action press reverts.
    Jade previews a move, then quits the problem.
    When he reenters the problem, he sees his preview has been cleared.
    >>> code_unit.inline_examples(
    ...     ethan_lukasz_begin_example.__doc__, 
    ...     locals(), globals(), 
    ...     verify_examples = False)

    >>> jade = black
    >>> lukasz = black
    >>> computer_lukasz = white
    >>> wait = 5.0 / black._speed
    
    >>> lukasz.root.lobby_mc._00_mc.dominate_3_3_mc.dispatchEvent(mouseDown)
    >>> time.sleep(wait)

    FOR REPLAY, COMPUTER IS NOT PLAYING.
    >>> mouse_down_and_sleep(black, black.root.game_over_mc.white_computer_mc.enter_mc, wait)
    >>> property_diff(black, black.root.game_over_mc.white_computer_mc, 'currentLabel', 'none')
    >>> mouse_down_and_sleep(lukasz, lukasz.root.game_over_mc.start_mc, wait)
    >>> mouse_down_and_sleep(lukasz, lukasz.root._1_1_mc, wait)
    >>> mouse_down_and_sleep(lukasz, lukasz.root._1_1_mc, wait)
    >>> mouse_down_and_sleep(computer_lukasz, computer_lukasz.root._0_1_mc, wait)
    >>> mouse_down_and_sleep(lukasz, lukasz.root._0_0_mc, wait)
    >>> mouse_down_and_sleep(lukasz, lukasz.root._0_0_mc, wait)
    >>> mouse_down_and_sleep(lukasz, lukasz.root._1_0_mc, wait)
    >>> mouse_down_and_sleep(lukasz, lukasz.root._1_0_mc, wait)
    >>> mouse_down_and_sleep(computer_lukasz, computer_lukasz.root._2_1_mc, wait)
    >>> mouse_down_and_sleep(lukasz, lukasz.root._2_0_mc, wait)
    >>> lukasz.root.menu_mc.toggle_mc.dispatchEvent(mouseDown)
    >>> time.sleep(wait)
    >>> black.root._2_0_mc.currentLabel
    'empty_black'
    >>> lukasz.root.menu_mc.lobby_mc.dispatchEvent(mouseDown)
    >>> time.sleep(wait)
    >>> lukasz.root.lobby_mc._00_mc.dominate_3_3_mc.dispatchEvent(mouseDown)
    >>> time.sleep(wait)
    >>> mouse_down_and_sleep(lukasz, lukasz.root.game_over_mc.start_mc, wait)
    >>> black.root._2_0_mc.currentLabel
    'empty_black'
    >>> black.root._2_0_mc.black_shape_mc.currentLabel
    '_0000'
    '''

