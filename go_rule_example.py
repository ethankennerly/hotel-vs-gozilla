#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Examples of liberties, score, capture.
'''
__author__ = 'Ethan Kennerly'

from client import *


# Simple go games

def ethan_joris_example():
    '''TODO:  Update.
    Ethan enters the lobby and creates a multiplayer game.
    >>> code_unit.inline_examples(
    ...     ethan_joris_start_example.__doc__, 
    ...     locals(), globals(), 
    ...     verify_examples = False)

    >>> wait = 4.0 / joris._speed

    Joris clicks on the upper right star point.
    Soon, Joris sees a black stone appear there.
    >>> mouse_down_and_sleep(joris, joris.root._2_5_mc, wait)
    >>> property_diff(joris, joris.root._2_5_mc, 'currentLabel', 'question_black')
    >>> mouse_down_and_sleep(joris, joris.root._2_5_mc, wait)
    >>> property_diff(joris, joris.root._2_5_mc, 'currentLabel', 'black')

    Joris receives one extra pieces of cake.
    >>> property_diff(joris, joris.root.extra_stone_gift_mc, 
    ...     'currentLabel', '_1')

    Soon, Ethan sees the black stone that Joris had played.
    >>> time.sleep(wait)
    >>> property_diff(ethan, ethan.root._2_5_mc, 'currentLabel', 'black')

    #+Joris previews formation.
    #+Joris previews formation from a different angle and sees old formation go away.
   
    #+Joris sees multiple rotations of same formation.

    #+Joris is playing by cake_take theme.
    #+>>> property_diff(joris, joris.root.theme_txt, 'text', 'cake_take')
    #+>>> property_diff(joris, joris.root._2_5_mc, 'currentLabel', 'cake_take')

    #+Ethan is playing by traditional theme.
    #+>>> property_diff(ethan, ethan.root.theme_txt, 'text', 'traditional')
    #+>>> property_diff(joris, joris.root._2_5_mc, 'currentLabel', 'traditional')

    Joris sees the blue boy grow and glass fall and text:  partner's turn.
    >>> property_diff(joris, joris.root.turn_mc, 'currentLabel', 'white')
    >>> property_diff(joris, joris.root.turn_veil_mc, 'currentLabel', 'other')

    Ethan sees the blue boy grow and glass lift and text:  his turn.
    >>> property_diff(ethan, ethan.root.turn_mc, 'currentLabel', 'white')
    >>> property_diff(ethan, ethan.root.turn_veil_mc, 'currentLabel', 'you')
    
    Therefore, when Joris presses an intersection, 
    Joris sees that it is not his turn.
    >>> mouse_down_and_sleep(joris, joris.root._4_4_mc, wait)
    >>> property_diff(joris, joris.root.turn_mc, 'currentLabel', 'white')
    >>> property_diff(joris, joris.root.turn_veil_mc, 'currentLabel', 'other')
    >>> property_diff(joris, joris.root._4_4_mc, 'currentLabel', 'empty_black')

    In the center, Ethan sees he may play a white stone.
    >>> property_diff(ethan, ethan.root._4_4_mc, 'currentLabel', 'empty_white')

    #>>> property_diff(joris, joris.root.formation_knight_attack_mc.rotate_0_mc.response_mc, 
    #...     'currentLabel', 'none')

    Ethan plays a white stone.
    >>> mouse_down_and_sleep(ethan, ethan.root._4_4_mc, wait)

    Soon, Ethan sees the white stone that he had played.
    >>> property_diff(ethan, ethan.root._4_4_mc, 'currentLabel', 'white')

    Soon, Joris sees the white stone that Ethan had played.
    >>> property_diff(joris, joris.root._4_4_mc, 'currentLabel', 'white')

    #Joris sees the knight attack formation that Ethan has made.
    #>>> property_diff(joris, joris.root.formation_knight_attack_mc.rotate_0_mc.response_mc, 
    #...     'currentLabel', 'response')

    #Whereas, Ethan sees no formation.
    #>>> property_diff(ethan, ethan.root.formation_knight_attack_mc.rotate_0_mc.response_mc, 
    #...     'currentLabel', 'none')

    Joris sees the red girl grow and glass lift and text:  your turn.
    >>> property_diff(joris, joris.root.turn_mc, 'currentLabel', 'black')
    >>> property_diff(joris, joris.root.turn_veil_mc, 'currentLabel', 'you')

    Ethan sees the red girl grow and glass fall and text:  partner's turn.
    >>> property_diff(ethan, ethan.root.turn_mc, 'currentLabel', 'black')
    >>> property_diff(ethan, ethan.root.turn_veil_mc, 'currentLabel', 'other')
   
    Joris clicks the free cake gift.
    >>> mouse_down_and_sleep(joris, joris.root.extra_stone_gift_mc.use_mc, wait)

    Joris sees that he may take a free piece of cake.
    >>> property_diff(joris, joris.root.cursor_mc.extra_stone_mc, 'currentLabel', '_1')
    >>> property_diff(joris, joris.root.turn_mc, 'currentLabel', 'black')

    Joris has no gifts of cake left.
    >>> property_diff(joris, joris.root.extra_stone_gift_mc, 
    ...     'currentLabel', '_0')

    Joris plays first, where he would not get free cake.
    >>> mouse_down_and_sleep(joris, joris.root._0_0_mc, wait)
    >>> property_diff(joris, joris.root._0_0_mc, 'currentLabel', 'question_black')
    >>> mouse_down_and_sleep(joris, joris.root._0_0_mc, wait)
    >>> property_diff(joris, joris.root._0_0_mc, 'currentLabel', 'black')

    Joris has no extra pieces of cake.
    >>> property_diff(joris, joris.root.extra_stone_gift_mc, 
    ...     'currentLabel', '_0')

    Joris plays twice, where he would get free cake.
    >>> mouse_down_and_sleep(joris, joris.root._2_3_mc, wait)
    >>> mouse_down_and_sleep(joris, joris.root._2_3_mc, wait)
    >>> property_diff(joris, joris.root._2_3_mc, 'currentLabel', 'black')

    Joris has a gift of cake.
    >>> property_diff(joris, joris.root.extra_stone_gift_mc, 
    ...     'currentLabel', '_1')

    Joris sees the blue boy grow and glass fall and text:  partner's turn.
    >>> property_diff(joris, joris.root.turn_mc, 'currentLabel', 'white')
    >>> property_diff(joris, joris.root.turn_veil_mc, 'currentLabel', 'other')
    
    Ethan plays, which Joris sees.
    >>> mouse_down_and_sleep(ethan, ethan.root._6_6_mc, wait)
    >>> property_diff(joris, joris.root._6_6_mc, 'currentLabel', 'white')

    >>> property_diff(joris, joris.root.hide_gift_mc, 
    ...     'currentLabel', '_0')

    Joris plays another pattern.
    >>> mouse_down_and_sleep(joris, joris.root._3_5_mc, wait)
    >>> mouse_down_and_sleep(joris, joris.root._3_5_mc, wait)

    Because Joris has extra cake, Joris gets a gift of hidden cake.
    >>> property_diff(joris, joris.root.hide_gift_mc, 
    ...     'currentLabel', '_1')

    Ethan plays, which Joris sees.
    >>> mouse_down_and_sleep(ethan, ethan.root._5_7_mc, wait)
    >>> property_diff(joris, joris.root._5_7_mc, 'currentLabel', 'white')

    #Joris sees that Ethan made a diagonal formation.
    #Ethan does not see any formation.
    #>>> property_diff(joris, joris.root.formation_diagonal_mc.rotate_180_mc.response_mc, 
    #...     'currentLabel', 'response')
    #>>> property_diff(ethan, ethan.root.formation_diagonal_mc.rotate_0_mc.response_mc, 
    #...     'currentLabel', 'none')

    Joris sees the red girl grow and glass lift and text:  your turn.
    >>> property_diff(joris, joris.root.turn_mc, 'currentLabel', 'black')
    >>> property_diff(joris, joris.root.turn_veil_mc, 'currentLabel', 'you')

    Joris clicks the gift of hidden cake.
    >>> mouse_down_and_sleep(joris, joris.root.hide_gift_mc.use_mc, wait)

    Joris has no more hidden cake.
    >>> property_diff(joris, joris.root.hide_gift_mc, 
    ...     'currentLabel', '_0')

    Joris sees a place to hide a stone.
    >>> property_diff(joris, joris.root._7_7_mc, 
    ...     'currentLabel', 'empty_hide_black')
    
    Joris clicks a piece of cake and secretly takes it.
    >>> mouse_down_and_sleep(joris, joris.root._7_7_mc, wait)
    >>> mouse_down_and_sleep(joris, joris.root._7_7_mc, wait)

    Joris sees that Ethan does not see the stone.
    >>> property_diff(joris, joris.root._7_7_mc, 
    ...     'currentLabel', 'hide_black')
    
    Joris sees the blue boy grow and glass fall and text:  partner's turn.
    >>> property_diff(joris, joris.root.turn_mc, 'currentLabel', 'white')
    >>> property_diff(joris, joris.root.turn_veil_mc, 'currentLabel', 'other')
    
    Ethan cannot see the secretly taken cake.
    >>> property_diff(ethan, ethan.root._7_7_mc, 
    ...     'currentLabel', 'empty_white')

    Ethan plays.
    >>> mouse_down_and_sleep(ethan, ethan.root._6_7_mc, wait)
    >>> property_diff(ethan, ethan.root._6_7_mc, 
    ...     'currentLabel', 'white')

    Joris still sees the hidden cake.
    >>> property_diff(joris, joris.root._7_7_mc, 
    ...     'currentLabel', 'hide_black')
    
    Joris plays, and both players see it is not hidden.
    >>> mouse_down_and_sleep(joris, joris.root._6_4_mc, wait)
    >>> mouse_down_and_sleep(joris, joris.root._6_4_mc, wait)
    >>> property_diff(joris, joris.root._6_4_mc, 
    ...     'currentLabel', 'black')
    >>> property_diff(ethan, ethan.root._6_4_mc, 
    ...     'currentLabel', 'black')

    Until Ethan tries to play there, at which point it becomes unhidden.
    >>> mouse_down_and_sleep(ethan, ethan.root._7_7_mc, wait)
    >>> property_diff(ethan, ethan.root._7_7_mc, 
    ...     'currentLabel', 'black')
    >>> joris.root._7_7_mc.hide_mc.currentLabel
    'reveal'
    >>> ethan.root._7_7_mc.hide_mc.currentLabel
    'reveal'

    Joris sees that Ethan sees stone.
    >>> property_diff(joris, joris.root._7_7_mc, 
    ...     'currentLabel', 'black')
   
    Joris closes the application.
    >>> joris.root.gateway_mc.gotoAndPlay('exit')

    #+ Joris opens the application again.
    #+ Joris logs in again.
    #+ At lobby, Joris sees room for Ethan.
    #+ Joris rejoins room of Ethan.
    #+ Joris sees game in progress.

    Ethan closes the application.
    >>> ethan.root.gateway_mc.gotoAndPlay('exit')
    '''


def liberty_example():
    r'''Show blocked liberty.
    >>> code_unit.inline_examples(
    ...     ethan_joris_start_example.__doc__, 
    ...     locals(), globals(), 
    ...     verify_examples = False)

    tests units:  get_capture_news

    Joris has liberty warning enabled.
    >>> property_diff(joris, joris.root.option_mc.block_mc, 
    ...     'currentLabel', 'show')

    Ethan does not have liberty warning enabled.
    >>> property_diff(ethan, ethan.root.option_mc.block_mc, 
    ...     'currentLabel', 'none')

    Joris sees no blocks.
    >>> board_diff(joris, joris.root._1_1_mc.block_north_mc,
    ...     'currentLabel', 'none')
    >>> board_diff(joris, joris.root._1_1_mc.block_east_mc,
    ...     'currentLabel', 'none')
    >>> board_diff(joris, joris.root._1_1_mc.block_south_mc,
    ...     'currentLabel', 'none')
    >>> board_diff(joris, joris.root._1_1_mc.block_west_mc,
    ...     'currentLabel', 'none')

    Joris plays in interior and sees no blocks.
    >>> mouse_down_and_sleep(joris, joris.root._1_1_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._1_1_mc, 1.0 / joris._speed)
    >>> board_diff(joris, joris.root._1_1_mc.block_north_mc,
    ...     'currentLabel', 'none')
    >>> board_diff(joris, joris.root._1_1_mc.block_east_mc,
    ...     'currentLabel', 'none')
    >>> board_diff(joris, joris.root._1_1_mc.block_south_mc,
    ...     'currentLabel', 'none')
    >>> board_diff(joris, joris.root._1_1_mc.block_west_mc,
    ...     'currentLabel', 'none')

    Ethan takes away a liberty.
    Joris has three out of four liberties left.  Joris sees the blocked liberty.
    >>> board_diff(joris, joris.root._2_1_mc.block_north_mc,
    ...     'currentLabel', 'none')
    >>> board_diff(joris, joris.root._2_1_mc.block_east_mc,
    ...     'currentLabel', 'none')
    >>> board_diff(joris, joris.root._2_1_mc.block_south_mc,
    ...         'currentLabel', 'none')
    >>> board_diff(joris, joris.root._2_1_mc.block_west_mc,
    ...     'currentLabel', 'none')
    >>> mouse_down_and_sleep(ethan, ethan.root._2_1_mc, 1.0 / ethan._speed)
    >>> board_diff(joris, joris.root._1_1_mc.block_north_mc,
    ...     'currentLabel', 'none')
    >>> board_diff(joris, joris.root._1_1_mc.block_east_mc,
    ...     'currentLabel', 'none')
    >>> board_diff(joris, joris.root._1_1_mc.block_south_mc,
    ...         'currentLabel', 'black_block')
    >>> board_diff(joris, joris.root._1_1_mc.block_west_mc,
    ...     'currentLabel', 'none')

    Ethan does not.
    >>> board_diff(ethan, ethan.root._1_1_mc.block_north_mc,
    ...     'currentLabel', 'none')
    >>> board_diff(ethan, ethan.root._1_1_mc.block_east_mc,
    ...     'currentLabel', 'none')
    >>> board_diff(ethan, ethan.root._1_1_mc.block_south_mc,
    ...         'currentLabel', 'none')
    >>> board_diff(ethan, ethan.root._1_1_mc.block_west_mc,
    ...     'currentLabel', 'none')

    Ethan has three out of four liberties left.  Joris sees the blocked liberty.
    >>> board_diff(joris, joris.root._2_1_mc.block_north_mc,
    ...     'currentLabel', 'white_block')
    >>> board_diff(joris, joris.root._2_1_mc.block_east_mc,
    ...     'currentLabel', 'none')
    >>> board_diff(joris, joris.root._2_1_mc.block_south_mc,
    ...         'currentLabel', 'none')
    >>> board_diff(joris, joris.root._2_1_mc.block_west_mc,
    ...     'currentLabel', 'none')

    Ethan does not.
    >>> board_diff(ethan, ethan.root._2_1_mc.block_north_mc,
    ...     'currentLabel', 'none')
    >>> board_diff(ethan, ethan.root._2_1_mc.block_east_mc,
    ...     'currentLabel', 'none')
    >>> board_diff(ethan, ethan.root._2_1_mc.block_south_mc,
    ...         'currentLabel', 'none')
    >>> board_diff(ethan, ethan.root._2_1_mc.block_west_mc,
    ...     'currentLabel', 'none')

    Joris plays north side and sees block at north.
    >>> mouse_down_and_sleep(joris, joris.root._0_2_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._0_2_mc, 1.0 / joris._speed)
    >>> board_diff(joris, joris.root._0_2_mc.block_north_mc,
    ...     'currentLabel', 'black_block')
    >>> board_diff(joris, joris.root._0_2_mc.block_east_mc,
    ...     'currentLabel', 'none')
    >>> board_diff(joris, joris.root._0_2_mc.block_south_mc,
    ...     'currentLabel', 'none')
    >>> board_diff(joris, joris.root._0_2_mc.block_west_mc,
    ...     'currentLabel', 'none')

    Ethan extends.  Joris no longer sees Ethan block.
    >>> mouse_down_and_sleep(ethan, ethan.root._3_1_mc, 1.0 / ethan._speed)
    >>> board_diff(joris, joris.root._2_1_mc.block_north_mc,
    ...     'currentLabel', 'none')
    >>> board_diff(joris, joris.root._2_1_mc.block_east_mc,
    ...     'currentLabel', 'none')
    >>> board_diff(joris, joris.root._2_1_mc.block_south_mc,
    ...         'currentLabel', 'none')
    >>> board_diff(joris, joris.root._2_1_mc.block_west_mc,
    ...     'currentLabel', 'none')

    Yet he still sees his own, since it only has three liberties.
    >>> board_diff(joris, joris.root._1_1_mc.block_north_mc,
    ...     'currentLabel', 'none')
    >>> board_diff(joris, joris.root._1_1_mc.block_east_mc,
    ...     'currentLabel', 'none')
    >>> board_diff(joris, joris.root._1_1_mc.block_south_mc,
    ...         'currentLabel', 'black_block')
    >>> board_diff(joris, joris.root._1_1_mc.block_west_mc,
    ...     'currentLabel', 'none')

    Joris plays corner and sees black_warning.
    >>> mouse_down_and_sleep(joris, joris.root._0_0_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._0_0_mc, 1.0 / joris._speed)
    >>> board_diff(joris, joris.root._0_0_mc.block_north_mc,
    ...     'currentLabel', 'black_warning')
    >>> board_diff(joris, joris.root._0_0_mc.block_east_mc,
    ...     'currentLabel', 'none')
    >>> board_diff(joris, joris.root._0_0_mc.block_south_mc,
    ...     'currentLabel', 'none')
    >>> board_diff(joris, joris.root._0_0_mc.block_west_mc,
    ...     'currentLabel', 'black_warning')

    Ethan plays.  Joris nearly captures.  Joris sees his warning and Ethan's danger.
    >>> mouse_down_and_sleep(ethan, ethan.root._1_2_mc, 1.0 / ethan._speed)
    >>> mouse_down_and_sleep(joris, joris.root._2_2_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._2_2_mc, 1.0 / joris._speed)
    >>> board_diff(joris, joris.root._2_2_mc.block_north_mc,
    ...     'currentLabel', 'black_warning')
    >>> board_diff(joris, joris.root._2_2_mc.block_east_mc,
    ...     'currentLabel', 'none')
    >>> board_diff(joris, joris.root._2_2_mc.block_south_mc,
    ...     'currentLabel', 'none')
    >>> board_diff(joris, joris.root._2_2_mc.block_west_mc,
    ...     'currentLabel', 'black_warning')
    >>> board_diff(joris, joris.root._1_2_mc.block_north_mc,
    ...     'currentLabel', 'white_danger')
    >>> board_diff(joris, joris.root._1_2_mc.block_east_mc,
    ...     'currentLabel', 'none')
    >>> board_diff(joris, joris.root._1_2_mc.block_south_mc,
    ...     'currentLabel', 'white_danger')
    >>> board_diff(joris, joris.root._1_2_mc.block_west_mc,
    ...     'currentLabel', 'white_danger')
    
    Ethan extends.  Joris previews and sees warning.
    >>> mouse_down_and_sleep(ethan, ethan.root._1_3_mc, 1.0 / ethan._speed)
    >>> mouse_down_and_sleep(joris, joris.root._0_1_mc, 1.0 / joris._speed)
    >>> board_diff(joris, joris.root._0_1_mc.block_north_mc,
    ...     'currentLabel', 'black_warning')
    >>> board_diff(joris, joris.root._0_1_mc.block_east_mc,
    ...     'currentLabel', 'none')
    >>> board_diff(joris, joris.root._0_1_mc.block_south_mc,
    ...     'currentLabel', 'none')
    >>> board_diff(joris, joris.root._0_1_mc.block_west_mc,
    ...     'currentLabel', 'none')

    Joris previews elsewhere and previous preview reverts.
    >>> mouse_down_and_sleep(joris, joris.root._2_3_mc, 1.0 / joris._speed)
    >>> board_diff(joris, joris.root._0_1_mc,
    ...     'currentLabel', 'empty_black')
    >>> board_diff(joris, joris.root._0_1_mc.suicide_mc,
    ...     'currentLabel', 'white')
    
    #- >>> board_diff(joris, joris.root._0_1_mc.block_north_mc,
    #- ...     'currentLabel', 'suicide_white')
    #- >>> board_diff(joris, joris.root._0_1_mc.block_east_mc,
    #- ...     'currentLabel', 'suicide_white')
    #- >>> board_diff(joris, joris.root._0_1_mc.block_south_mc,
    #- ...     'currentLabel', 'suicide_white')
    #- >>> board_diff(joris, joris.root._0_1_mc.block_west_mc,
    #- ...     'currentLabel', 'suicide_white')
    
    Joris plays elsewhere and previous preview reverts.
    >>> mouse_down_and_sleep(joris, joris.root._2_3_mc, 1.0 / joris._speed)
    >>> board_diff(joris, joris.root._0_1_mc,
    ...     'currentLabel', 'empty_black')
    >>> board_diff(joris, joris.root._0_1_mc.suicide_mc,
    ...     'currentLabel', 'white')
    
    #- >>> board_diff(joris, joris.root._0_1_mc.block_north_mc,
    #- ...     'currentLabel', 'suicide_white')
    #- >>> board_diff(joris, joris.root._0_1_mc.block_east_mc,
    #- ...     'currentLabel', 'suicide_white')
    #- >>> board_diff(joris, joris.root._0_1_mc.block_south_mc,
    #- ...     'currentLabel', 'suicide_white')
    #- >>> board_diff(joris, joris.root._0_1_mc.block_west_mc,
    #- ...     'currentLabel', 'suicide_white')
    
      0 1 2 3 4 5 6 7 8 
    0 X4?8X2. . . . . . 
    1 . X0O5O7. . . . . 
    2 . O1X6X8. . . . . 
    3 . O3. . . . . . . 
    4 . . . . . . . . . 
    5 . . . . . . . . . 
    6 . . . . . . . . . 
    7 . . . . . . . . . 
    8 . . . . . . . . . 
    '''


    
def score_example():
    r'''After a few plays the score updates.
    >>> code_unit.inline_examples(
    ...     liberty_example.__doc__, 
    ...     locals(), globals(), 
    ...     verify_examples = False)

    Should see a score
    >>> property_diff(joris, joris.root.score_mc.bar_mc, 'currentLabel', 
    ...     '_-38')
    >>> property_diff(joris, joris.root.score_mc.bar_mc.territory_txt, 'text', 
    ...     '-38')
    >>> property_diff(joris, joris.root.score_mc.bar_mc.marker_mc.change_txt, 
    ...     'text', '-8')

    On territory, GnuGo agrees that white is winning by 11.
    >>> from go_text_protocol import load_sgf, talk, setup_envoy, get_score_and_territory
    >>> gtp_envoy = setup_envoy(configuration.gtp_path, 'localhost', 5903)
    >>> load_sgf(gtp_envoy, path='sgf/_update_gnugo.sgf')
    '= black\n\n'
    >>> print talk(gtp_envoy, 'showboard')
    = 
       A B C D E F G H J
     9 X . X . . . . . . 9
     8 . X O O . . . . . 8
     7 . O X . . . + . . 7
     6 . O . . . . . . . 6
     5 . . . . + . . . . 5
     4 . . . . . . . . . 4
     3 . . + . . . + . . 3
     2 . . . . . . . . . 2     WHITE (O) has captured 0 stones
     1 . . . . . . . . . 1     BLACK (X) has captured 0 stones
       A B C D E F G H J
    <BLANKLINE>
    <BLANKLINE>
    >>> score, territory_values = get_score_and_territory(gtp_envoy)
    >>> score
    -38
    >>> from pprint import pprint as pp; pp(territory_values)
    [[2, 1, 2, 1, 1, 1, 1, 0, 0],
     [1, 2, 0, 0, 1, 1, 1, 0, 0],
     [1, 0, 2, 1, 1, 1, 1, 0, 0],
     [1, 0, 1, 1, 1, 1, 0, 0, 0],
     [1, 1, 1, 1, 1, 0, 0, 0, 0],
     [1, 1, 1, 1, 0, 0, 0, 0, 0],
     [1, 1, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0]]
    '''

def score_pass_example_todo():
    '''5x5 game.  
    >>> mouse_down_and_sleep(jade, jade.root.game_over_mc.start_mc, wait)

    >>> mouse_down_and_sleep(jade, jade.root._2_3_mc, wait)

    >>> mouse_down_and_sleep(jade, jade.root._2_3_mc, wait)

    >>> mouse_down_and_sleep(ethan, ethan.root._2_2_mc, wait)

    >>> mouse_down_and_sleep(jade, jade.root._1_3_mc, wait)

    >>> mouse_down_and_sleep(jade, jade.root._1_3_mc, wait)

    >>> mouse_down_and_sleep(ethan, ethan.root._1_2_mc, wait)

    >>> mouse_down_and_sleep(jade, jade.root._0_3_mc, wait)

    >>> mouse_down_and_sleep(jade, jade.root._0_3_mc, wait)

    >>> mouse_down_and_sleep(ethan, ethan.root._0_2_mc, wait)

    >>> mouse_down_and_sleep(jade, jade.root._3_3_mc, wait)

    >>> mouse_down_and_sleep(jade, jade.root._3_3_mc, wait)

    >>> mouse_down_and_sleep(ethan, ethan.root._3_2_mc, wait)

    >>> mouse_down_and_sleep(jade, jade.root._4_3_mc, wait)

    >>> mouse_down_and_sleep(jade, jade.root._4_3_mc, wait)

    >>> mouse_down_and_sleep(ethan, ethan.root._4_2_mc, wait)

    >>> mouse_down_and_sleep(ethan, ethan.root._3_4_mc, wait)

    >>> mouse_down_and_sleep(ethan, ethan.root._3_4_mc, wait)

    >>> mouse_down_and_sleep(jade, jade.root._4_4_mc, wait)

    >>> mouse_down_and_sleep(jade, jade.root._4_4_mc, wait)

    >>> mouse_down_and_sleep(ethan, ethan.root._3_4_mc, wait)

    >>> mouse_down_and_sleep(jade, jade.root._2_1_mc, wait)

    >>> mouse_down_and_sleep(jade, jade.root._2_1_mc, wait)

    >>> mouse_down_and_sleep(ethan, ethan.root._2_4_mc, wait)
    >>> ethan.root.pass_mc.enter_mc.dispatchEvent(mouseDown)
    >>> time.sleep(wait)
    >>> jade.root.pass_mc.enter_mc.dispatchEvent(mouseDown)
    >>> time.sleep(wait)
    >>> jade.root.game_over_mc.score_mc.territory_txt.text
    '-5'
    >>> jade.root.score_mc.bar_mc.territory_txt.text
    '-5'

    got -19
    '''
    
def suicide_example():
    '''Joris gets captured in corner and sees he cannot play there.
    >>> code_unit.inline_examples(
    ...     ethan_joris_start_example.__doc__, 
    ...     locals(), globals(), 
    ...     verify_examples = False)
    >>> mouse_down_and_sleep(joris, joris.root._0_0_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._0_0_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._0_1_mc, 1.0 / ethan._speed)
    >>> mouse_down_and_sleep(joris, joris.root._0_2_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._0_2_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._1_0_mc, 1.0 / ethan._speed)

    No blocks.
    >>> board_diff(joris, joris.root._0_0_mc.block_north_mc,
    ...     'currentLabel', 'none')
    >>> board_diff(joris, joris.root._0_0_mc.block_east_mc,
    ...     'currentLabel', 'none')
    >>> board_diff(joris, joris.root._0_0_mc.block_south_mc,
    ...     'currentLabel', 'none')
    >>> board_diff(joris, joris.root._0_0_mc.block_west_mc,
    ...     'currentLabel', 'none')

    See suicide after own turn or partner's turn.
    >>> property_diff(joris, joris.root.suicide_mc,
    ...     'currentLabel', 'show')
    >>> board_diff(joris, joris.root._0_0_mc.suicide_mc,
    ...     'currentLabel', 'black')
    >>> board_diff(ethan, ethan.root._0_0_mc.suicide_mc,
    ...     'currentLabel', 'none')
    >>> joris.pb()
    ,OX,,,,,,
    O,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,

    Without suicide option, Joris does not see suicide.
    >>> mouse_down_and_sleep(joris, joris.root.suicide_mc.enter_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._1_1_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._1_1_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._1_2_mc, 1.0 / ethan._speed)
    >>> mouse_down_and_sleep(joris, joris.root._0_0_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._0_0_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._2_1_mc, 1.0 / ethan._speed)
    >>> mouse_down_and_sleep(joris, joris.root._2_0_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._2_0_mc, 1.0 / joris._speed)
    >>> joris.pb()
    X,X,,,,,,
    ,XO,,,,,,
    XO,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    >>> property_diff(joris, joris.root._0_1_mc.suicide_mc,
    ...     'currentLabel', 'none')
    '''


def capture_example():
    '''Black captures a white stone in the corner.
    >>> code_unit.inline_examples(
    ...     ethan_joris_start_example.__doc__, 
    ...     locals(), globals(), 
    ...     verify_examples = False)

    black, 0, 1
    Soon, Joris previews a black stone appear there.
    >>> mouse_down_and_sleep(joris, joris.root._0_1_mc, 1.0 / joris._speed)
    >>> board_diff(joris, joris.root._0_1_mc, 'currentLabel', 'question_black')
    >>> mouse_down_and_sleep(joris, joris.root._0_1_mc, 1.0 / joris._speed)
    >>> board_diff(joris, joris.root._0_1_mc, 'currentLabel', 'black')

    white, 0, 0
    >>> mouse_down_and_sleep(ethan, ethan.root._0_0_mc, 1.0 / ethan._speed)
    >>> board_diff(ethan, ethan.root._0_0_mc, 'currentLabel', 'white')

    no captures for black yet.
    >>> property_diff(joris, joris.root.score_mc.bar_mc.marker_mc.capture_mc, 
    ...     'currentLabel', '_0')

    preview black, 1, 0
    >>> mouse_down_and_sleep(joris, joris.root._1_0_mc, 1.0 / joris._speed)
    >>> board_diff(joris, joris.root._0_0_mc, 'currentLabel', 'empty_black')
    >>> board_diff(ethan, ethan.root._0_0_mc, 'currentLabel', 'white')
    >>> board_diff(joris, joris.root._0_1_mc, 'currentLabel', 'black')
    >>> board_diff(joris, joris.root._1_0_mc, 'currentLabel', 'question_black')
    >>> mouse_down_and_sleep(joris, joris.root._1_0_mc, 1.0 / joris._speed)
    >>> board_diff(joris, joris.root._1_0_mc, 'currentLabel', 'black')

    black captures.
    >>> property_diff(joris, joris.root.score_mc.bar_mc.marker_mc.capture_mc, 
    ...     'currentLabel', '_1')

    black captures 0, 0.
    >>> board_diff(joris, joris.root._0_0_mc, 'currentLabel', 'empty_black')
    >>> board_diff(ethan, ethan.root._0_0_mc, 'currentLabel', 'empty_white')
    >>> board_diff(joris, joris.root._0_1_mc, 'currentLabel', 'black')
    >>> board_diff(joris, joris.root._1_0_mc, 'currentLabel', 'black')

    White cannot play suicide.
    >>> mouse_down_and_sleep(ethan, ethan.root._0_0_mc, 1.0 / ethan._speed)
    >>> board_diff(ethan, ethan.root._0_0_mc, 'currentLabel', 'empty_white')
    >>> board_diff(joris, joris.root._0_0_mc, 'currentLabel', 'empty_black')
   
    White surrounds.
    >>> mouse_down_and_sleep(ethan, ethan.root._1_1_mc, 1.0 / ethan._speed)
    >>> board_diff(ethan, ethan.root._1_1_mc, 'currentLabel', 'white')

    Joris plays elsewhere.
    >>> mouse_down_and_sleep(joris, joris.root._8_8_mc, 1.0 / joris._speed)
    >>> board_diff(joris, joris.root._8_8_mc, 'currentLabel', 'question_black')
    >>> mouse_down_and_sleep(joris, joris.root._8_8_mc, 1.0 / joris._speed)
    >>> board_diff(joris, joris.root._8_8_mc, 'currentLabel', 'black')

    Ethan surrounds.
    >>> mouse_down_and_sleep(ethan, ethan.root._0_2_mc, 1.0 / ethan._speed)
    >>> board_diff(ethan, ethan.root._0_2_mc, 'currentLabel', 'white')
    
    Joris plays elsewhere.
    >>> mouse_down_and_sleep(joris, joris.root._8_7_mc, 1.0 / joris._speed)
    >>> board_diff(joris, joris.root._8_7_mc, 'currentLabel', 'question_black')
    >>> mouse_down_and_sleep(joris, joris.root._8_7_mc, 1.0 / joris._speed)
    >>> board_diff(joris, joris.root._8_7_mc, 'currentLabel', 'black')

    Ethan surrounds.
    >>> mouse_down_and_sleep(ethan, ethan.root._2_0_mc, 1.0 / ethan._speed)
    >>> board_diff(ethan, ethan.root._2_0_mc, 'currentLabel', 'white')
    
    Joris cannot play suicide to multiple stones,
    >>> mouse_down_and_sleep(joris, joris.root._0_0_mc, 1.0 / joris._speed)
    >>> board_diff(joris, joris.root._0_0_mc, 'currentLabel', 'empty_black')
    >>> mouse_down_and_sleep(joris, joris.root._0_0_mc, 1.0 / joris._speed)
    >>> board_diff(joris, joris.root._0_0_mc, 'currentLabel', 'empty_black')

    Joris does not lose those stones.
    >>> board_diff(joris, joris.root.help_mc, 'currentLabel', 'suicide')
    >>> board_diff(joris, joris.root._0_1_mc, 'currentLabel', 'black')
    >>> board_diff(joris, joris.root._1_0_mc, 'currentLabel', 'black')

    Joris plays elsewhere.
    >>> mouse_down_and_sleep(joris, joris.root._0_3_mc, 1.0 / joris._speed)
    >>> board_diff(joris, joris.root._0_3_mc, 'currentLabel', 'question_black')
    >>> mouse_down_and_sleep(joris, joris.root._0_3_mc, 1.0 / joris._speed)
    >>> board_diff(joris, joris.root._0_3_mc, 'currentLabel', 'black')

    Ethan plays.  Joris sees this.
    >>> mouse_down_and_sleep(ethan, ethan.root._2_2_mc, 1.0 / ethan._speed)
    >>> board_diff(joris, joris.root._2_2_mc, 'currentLabel', 'white')

    Joris sees suicide before moving.
    >>> board_diff(joris, joris.root._0_0_mc.suicide_mc, 'currentLabel',
    ...     'black')

    Joris previews capture.
    >>> mouse_down_and_sleep(joris, joris.root._1_2_mc, 1.0 / joris._speed)
    >>> board_diff(joris, joris.root._1_2_mc, 'currentLabel', 'question_black')

    Joris previews suicide.
    >>> mouse_down_and_sleep(joris, joris.root._0_0_mc, 1.0 / joris._speed)
    >>> board_diff(joris, joris.root._0_0_mc, 'currentLabel', 'empty_black')

    Joris does not lose those stones.
    >>> board_diff(joris, joris.root.help_mc, 'currentLabel', 'suicide')
    >>> board_diff(joris, joris.root._0_1_mc, 'currentLabel', 'black')
    >>> board_diff(joris, joris.root._1_0_mc, 'currentLabel', 'black')

    >>> mouse_down_and_sleep(joris, joris.root._0_0_mc, 1.0 / joris._speed)
    >>> board_diff(joris, joris.root._0_0_mc, 'currentLabel', 'empty_black')

    Joris does not lose those stones.
    >>> board_diff(joris, joris.root.help_mc, 'currentLabel', 'suicide')
    >>> board_diff(joris, joris.root._0_1_mc, 'currentLabel', 'black')
    >>> board_diff(joris, joris.root._1_0_mc, 'currentLabel', 'black')

    Because, territory assumes white's next move,
    Joris does not see Ethan's stone is dead.
    >>> board_diff(joris, joris.root._0_2_mc.territory_mc, 'currentLabel',
    ...     'neutral')
    
    Joris previews elsewhere.
    >>> mouse_down_and_sleep(joris, joris.root._1_3_mc, 1.0 / joris._speed)
    
    Joris sees suicide.
    >>> board_diff(joris, joris.root._0_0_mc.suicide_mc, 'currentLabel',
    ...     'black')

    Joris sets up to capture.
    >>> mouse_down_and_sleep(joris, joris.root._1_2_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._1_2_mc, 1.0 / joris._speed)
    >>> joris.pb()
    ,X,X,,,,,
    XOX,,,,,,
    O,O,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,XX

    black captures again.
    >>> property_diff(joris, joris.root.score_mc.bar_mc.marker_mc.capture_mc, 
    ...     'currentLabel', '_2')

    Ethan plays to 0, 0 and captures one.  Joris sees this.
    >>> mouse_down_and_sleep(ethan, ethan.root._0_0_mc, 1.0 / ethan._speed)
    >>> joris.pb()
    OX,X,,,,,
    ,OX,,,,,,
    O,O,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,XX

    white reduces captures back to 1.
    >>> property_diff(joris, joris.root.score_mc.bar_mc.marker_mc.capture_mc, 
    ...     'currentLabel', '_1')
    
    #Joris sees that he cannot immediately capture back.
    #>>> board_diff(joris, joris.root._1_0_mc.block_north_mc,
    #...     'currentLabel', 'repeat')
    #>>> board_diff(joris, joris.root._1_0_mc.block_east_mc,
    #...     'currentLabel', 'repeat')
    #>>> board_diff(joris, joris.root._1_0_mc.block_south_mc,
    #...     'currentLabel', 'repeat')
    #>>> board_diff(joris, joris.root._1_0_mc.block_west_mc,
    #...     'currentLabel', 'repeat')
    
    Joris cannot immediately capture one because that repeats previous.
    >>> mouse_down_and_sleep(joris, joris.root._1_0_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._1_0_mc, 1.0 / joris._speed)
    >>> joris.pb()
    OX,X,,,,,
    ,OX,,,,,,
    O,O,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,XX
    >>> if property_diff(joris, joris.root.help_mc, 'currentLabel', 'repeat'):
    ...     import referee
    ...     referee.pb(gateway_process.users.get('joris').board_history[-1])
    ...     referee.pb(gateway_process.users.get('joris').board_history[-2])

    Joris must play elsewhere first then capture.
    >>> mouse_down_and_sleep(joris, joris.root._0_2_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._0_2_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._2_1_mc, 1.0 / ethan._speed)
    >>> joris.pb()
    OXXX,,,,,
    ,OX,,,,,,
    OOO,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,XX
    
    Joris' client becomes corrupt and does not show 2,1.
    Joris clicks at 2,1 but server does not allow it,
    and server resends that intersection to client.
    >>> joris.root._2_1_mc.gotoAndPlay('empty_black')
    >>> joris.pb()
    OXXX,,,,,
    ,OX,,,,,,
    O,O,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,XX
    >>> mouse_down_and_sleep(joris, joris.root._2_1_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._2_1_mc, 1.0 / joris._speed)
    >>> property_diff(joris, joris.root.turn_mc, 'currentLabel', 'black')
    >>> joris.pb()
    OXXX,,,,,
    ,OX,,,,,,
    OOO,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,XX

    >>> mouse_down_and_sleep(joris, joris.root._1_0_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._1_0_mc, 1.0 / joris._speed)
    >>> joris.pb()
    ,XXX,,,,,
    XOX,,,,,,
    OOO,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,XX

    Ethan cannot immediately take back a single stone,
    which would repeat the board position at the beginning of ethan's last turn.
    >>> property_diff(joris, joris.root.turn_mc, 'currentLabel', 'white')
    >>> mouse_down_and_sleep(ethan, ethan.root._0_0_mc, 1.0 / ethan._speed)
    >>> joris.pb()
    ,XXX,,,,,
    XOX,,,,,,
    OOO,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,XX
    >>> property_diff(ethan, ethan.root.help_mc, 'currentLabel', 'repeat')
    >>> property_diff(joris, joris.root.turn_mc, 'currentLabel', 'white')
    >>> mouse_down_and_sleep(ethan, ethan.root._1_3_mc, 1.0 / ethan._speed)
    >>> mouse_down_and_sleep(joris, joris.root._0_4_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._0_4_mc, 1.0 / joris._speed)
    
    Now Ethan may capture.
    >>> mouse_down_and_sleep(ethan, ethan.root._0_0_mc, 1.0 / ethan._speed)
    >>> joris.pb()
    OXXXX,,,,
    ,OXO,,,,,
    OOO,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,XX
    '''

def wout_computer_danger_example():
    '''Wout plays computer, is put in danger, yet may respond.
    >>> import config
    >>> defaults = config.setup_defaults()
    >>> configuration = config.borg(defaults)
    >>> configuration.instant = False
    >>> wout, wait = setup_example(configuration, 
    ...     ('wout', 'merbis') )
    >>> sloth = 1.0 / wout._speed
    >>> # example.log level 20 at Mon Sep 27 15:03:39 2010
    >>> wout.root.lobby_mc.main_mc._07_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 1.048000)
    >>> wout.root.lobby_mc._07_mc.score_5_5_3_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 3.891000)
    >>> mouse_down_and_sleep(wout, wout.root.game_over_mc.start_mc, wait)
    >>> time.sleep(sloth * 5.623000)
    >>> mouse_down_and_sleep(wout, wout.root._2_2_mc, wait)
    >>> ## mouse_down_and_sleep(computer_wout, computer_wout.root._1_2_mc, wait)
    >>> time.sleep(sloth * 5.587000)
    >>> mouse_down_and_sleep(wout, wout.root._2_3_mc, wait)
    >>> time.sleep(sloth * 5.065000)
    >>> mouse_down_and_sleep(wout, wout.root._1_3_mc, wait)
    >>> ## mouse_down_and_sleep(computer_wout, computer_wout.root._2_3_mc, wait)
    >>> time.sleep(sloth * 5.841000)
    >>> mouse_down_and_sleep(wout, wout.root._3_3_mc, wait)
    >>> time.sleep(sloth * 4.189000)
    >>> mouse_down_and_sleep(wout, wout.root._1_1_mc, wait)
    >>> ## mouse_down_and_sleep(computer_wout, computer_wout.root._1_4_mc, wait)
    >>> wout.root.cursor_mc.act_mc.currentLabel
    'play'
    >>> mouse_down_and_sleep(wout, wout.root._0_2_mc, wait)
    >>> wout.pb()
    ,,XO,
    ,X,XO
    ,,XO,
    ,,,,,
    ,,,,,

    In Flash, there it appears last packet was not received 
    by Python text or Flash client.
    Because score is sequenced, I guess packets collided.
    TODO:  Automate test in Flash.
    >>> from pprint import pprint
    >>> if not len(str(wout.ambassador.receives[-2])) < 256:
    ...     pprint(wout.ambassador.receives[-2])
    >>> if not len(str(wout.ambassador.receives[-1])) < 256:
    ...     pprint(wout.ambassador.receives[-1])
    '''
