#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Examples of last move, click, help, preview.
'''
__author__ = 'Ethan Kennerly'

from client import *


# User interface

def toggle_example():
    '''Ethan creates table and looks at score.
    >>> code_unit.inline_examples(
    ...     ethan_create_table_example.__doc__, 
    ...     locals(), globals(), 
    ...     verify_examples = False)

    >>> wait = 4.0
    >>> property_diff(ethan, ethan.root.score_mc, 'currentLabel', 'none')
    >>> mouse_down_and_sleep(ethan, ethan.root.option_mc.score_mc.enter_mc, wait / ethan._speed)
    >>> property_diff(ethan, ethan.root.score_mc, 'currentLabel', 'show')
    >>> mouse_down_and_sleep(ethan, ethan.root.option_mc.score_mc.enter_mc, wait / ethan._speed)
    >>> property_diff(ethan, ethan.root.score_mc, 'currentLabel', 'none')
    '''


def mouse_intersection_example():
    '''Mathijs presses intersection.  Only button responds.
    >>> code_unit.inline_examples(
    ...     ethan_joris_start_example.__doc__, 
    ...     locals(), globals(), 
    ...     verify_examples = False)
    >>> mathijs = joris
    >>> wait = 2.0 / joris._speed

    May press intersection or button, but not overlay or other children.
    >>> board_diff(joris, joris.root._0_0_mc, 'currentLabel', 'empty_black')
    >>> mouse_down_and_sleep(joris, joris.root._0_0_mc.overlay_mc, wait)
    >>> board_diff(joris, joris.root._0_0_mc, 'currentLabel', 'empty_black')
    >>> mouse_down_and_sleep(joris, joris.root._0_1_mc.question_mc, wait)
    >>> board_diff(joris, joris.root._0_1_mc, 'currentLabel', 'empty_black')
    >>> mouse_down_and_sleep(joris, joris.root._0_1_mc.overlay_mc, wait)
    >>> board_diff(joris, joris.root._0_1_mc, 'currentLabel', 'empty_black')

    # If no eventListener, bubble up to parent.
    #>>> ## mouse_down_and_sleep(joris, joris.root._0_1_mc.overlay_mc._btn, wait)
    #>>> ## board_diff(joris, joris.root._0_1_mc, 'currentLabel', 'question_black')
    >>> mouse_down_and_sleep(joris, joris.root._0_0_mc, wait)
    >>> board_diff(joris, joris.root._0_0_mc, 'currentLabel', 'question_black')
    >>> mouse_down_and_sleep(joris, joris.root._0_0_mc.question_mc, wait)
    >>> board_diff(joris, joris.root._0_0_mc, 'currentLabel', 'question_black')

    #>>> ## mouse_down_and_sleep(joris, joris.root._0_0_mc.overlay_mc._btn, wait)
    >>> mouse_down_and_sleep(joris, joris.root._0_0_mc, wait)
    >>> board_diff(joris, joris.root._0_0_mc, 'currentLabel', 'black')
    '''

def last_move_example():
    '''how can server snap last move and set "place"?
    after a successful move, snap that color's marker to the x and y of intersection.
    first move of black and white, 0,0 then 0,1.
    >>> code_unit.inline_examples(
    ...     ethan_joris_start_example.__doc__, 
    ...     locals(), globals(), 
    ...     verify_examples = False)

    >>> mouse_down_and_sleep(joris, joris.root._0_0_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._0_0_mc, 1.0 / joris._speed)
    >>> property_diff(joris, joris.root._0_0_mc.last_move_mc, 
    ...     'currentLabel', 'black')

    >>> mouse_down_and_sleep(ethan, ethan.root._0_1_mc, 1.0 / ethan._speed)
    >>> property_diff(joris, joris.root._0_0_mc.last_move_mc, 
    ...     'currentLabel', 'black')
    >>> property_diff(joris, joris.root._0_1_mc.last_move_mc, 
    ...     'currentLabel', 'white')

    >>> mouse_down_and_sleep(joris, joris.root._0_2_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._0_2_mc, 1.0 / joris._speed)
    >>> property_diff(joris, joris.root._0_0_mc.last_move_mc, 
    ...     'currentLabel', 'none')
    >>> property_diff(joris, joris.root._0_1_mc.last_move_mc, 
    ...     'currentLabel', 'white')
    >>> property_diff(joris, joris.root._0_2_mc.last_move_mc, 
    ...     'currentLabel', 'black')
    '''


def stone_help_example():
    '''Mathijs clicks a stone and gets help.
    >>> code_unit.inline_examples(
    ...     ethan_joris_start_example.__doc__, 
    ...     locals(), globals(), 
    ...     verify_examples = False)

    >>> mouse_down_and_sleep(joris, joris.root._0_0_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._0_0_mc, 1.0 / joris._speed)

    Ethan only sees that there is a stone, and receives no error.
    >>> property_diff(ethan, ethan.root.help_mc, 'currentLabel', 'none')
    >>> mouse_down_and_sleep(ethan, ethan.root._0_0_mc, 1.0 / ethan._speed)
    >>> property_diff(ethan, ethan.root.help_mc, 'currentLabel', 'none')
    >>> mouse_down_and_sleep(ethan, ethan.root._1_1_mc, 1.0 / ethan._speed)
    
    Joris sees help about dead.
    >>> property_diff(joris, joris.root.help_mc, 'currentLabel', 'none')
    >>> mouse_down_and_sleep(joris, joris.root._0_0_mc, 1.0 / joris._speed)
    >>> property_diff(joris, joris.root.help_mc, 'currentLabel', 'dead')

    If not dead and no danger or warning or notice, then nothing.
    >>> mouse_down_and_sleep(joris, joris.root._1_1_mc, 1.0 / joris._speed)
    >>> property_diff(joris, joris.root.help_mc, 'currentLabel', 'none')

    If warning, then warning.
    >>> mouse_down_and_sleep(joris, joris.root._0_1_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._0_1_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._6_6_mc, 1.0 / ethan._speed)
    >>> mouse_down_and_sleep(joris, joris.root._0_1_mc, 1.0 / joris._speed)
    >>> property_diff(joris, joris.root.help_mc, 'currentLabel', 'warning')

    If notice, then block.
    >>> mouse_down_and_sleep(joris, joris.root._1_2_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._1_2_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._3_1_mc, 1.0 / ethan._speed)
    >>> mouse_down_and_sleep(joris, joris.root._1_2_mc, 1.0 / joris._speed)
    >>> property_diff(joris, joris.root.help_mc, 'currentLabel', 'block')

    If danger, then danger.
    >>> mouse_down_and_sleep(joris, joris.root._1_0_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._0_2_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._2_1_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._1_0_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._1_0_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._2_0_mc, 1.0 / ethan._speed)
    >>> mouse_down_and_sleep(joris, joris.root._1_0_mc, 1.0 / joris._speed)
    >>> property_diff(joris, joris.root.help_mc, 'currentLabel', 'danger')
    '''

def rapid_click_example():
    '''Mathijs rapidly clicks.  Server ignores subsequent rapid clicks.
    DISCONTINUED?  Mouse shield on client.
    >>> code_unit.inline_examples(
    ...     ethan_joris_start_example.__doc__, 
    ...     locals(), globals(), 
    ...     verify_examples = False)
    >>> twitch = 0.125 / joris._speed
    >>> logging.warn('rapid_click_example: joris._speed = %i' % joris._speed)
    >>> board_diff(joris, joris.root._0_0_mc, 'currentLabel', 'empty_black')
    >>> mouse_down_and_sleep(joris, joris.root._0_0_mc, twitch)
    >>> mouse_down_and_sleep(joris, joris.root._0_0_mc, twitch)
    >>> mouse_down_and_sleep(joris, joris.root._0_0_mc, twitch)
    >>> mouse_down_and_sleep(joris, joris.root._0_0_mc, twitch)
    >>> mouse_down_and_sleep(joris, joris.root._0_0_mc, twitch)
    >>> mouse_down_and_sleep(joris, joris.root._0_0_mc, twitch)
    >>> mouse_down_and_sleep(joris, joris.root._0_1_mc, twitch)
    >>> mouse_down_and_sleep(joris, joris.root._0_1_mc, twitch)
    >>> mouse_down_and_sleep(joris, joris.root._0_1_mc, twitch)
    >>> mouse_down_and_sleep(joris, joris.root._0_1_mc, twitch)
    >>> mouse_down_and_sleep(joris, joris.root._0_1_mc, twitch)
    >>> mouse_down_and_sleep(joris, joris.root._0_1_mc, twitch)
    >>> mouse_down_and_sleep(joris, joris.root._0_0_mc, twitch)
    >>> mouse_down_and_sleep(joris, joris.root._0_0_mc, twitch)
    >>> mouse_down_and_sleep(joris, joris.root._0_0_mc, twitch)
    >>> mouse_down_and_sleep(joris, joris.root._0_0_mc, twitch)

    Client may overwrite news from server with its rapid inputs.
    >>> time.sleep(1.0 / joris._speed)
    >>> if board_diff(joris, joris.root._0_0_mc, 'currentLabel', 'preview_black'):
    ...     joris.root.gateway_mc.ready_time_txt.text

    Yet still, a patient click later is handled.
    >>> mouse_down_and_sleep(joris, joris.root._0_0_mc, 1.0 / joris._speed)
    >>> if board_diff(joris, joris.root._0_0_mc, 'currentLabel', 'question_black'):
    ...     joris.root.gateway_mc.ready_time_txt.text

                GATEWAY
        SORRY, THAT WAS 
        TOO FAST FOR ME.
        TRY AGAIN?
    >>> if property_diff(joris, joris.root.gateway_mc, 'currentLabel', 'too_fast'):
    ...     joris.root.gateway_mc.ready_time_txt.text

    After half a second, server accepts clicks and clears problem.
    >>> mouse_down_and_sleep(joris, joris.root._0_1_mc, twitch)
    >>> mouse_down_and_sleep(joris, joris.root._0_1_mc, twitch)
    >>> mouse_down_and_sleep(joris, joris.root._0_1_mc, twitch)
    >>> mouse_down_and_sleep(joris, joris.root._0_1_mc, twitch)
    >>> time.sleep(1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._0_1_mc, 1.0 / joris._speed)
    >>> if board_diff(joris, joris.root._0_1_mc, 'currentLabel', 'question_black'):
    ...     joris.root.gateway_mc.ready_time_txt.text

    A click is observed even if followed by rapid inputs.
    >>> mouse_down_and_sleep(joris, joris.root._0_0_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._0_0_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._0_0_mc, twitch)
    >>> mouse_down_and_sleep(joris, joris.root._0_0_mc, twitch)
    >>> if board_diff(joris, joris.root._0_0_mc, 'currentLabel', 'black'):
    ...     joris.root.gateway_mc.ready_time_txt.text
    >>> mouse_down_and_sleep(joris, joris.root._0_0_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._0_0_mc, 1.0 / joris._speed)
    >>> if board_diff(joris, joris.root._0_0_mc, 'currentLabel', 'black'):
    ...     joris.root.gateway_mc.ready_time_txt.text
    >>> if property_diff(joris, joris.root.gateway_mc, 'currentLabel', 'none'):
    ...     joris.root.gateway_mc.ready_time_txt.text

    the server could receive messages next to each other because:
        user clicked rapidly.
        user automated clicks.
        network delayed first message much more than second message.
        client delayed first message much more than second message.
    Network delay and processing delay or collision has not been addressed.
    '''

def preview_suicide_example():
    '''Playing on top another stone not allowed in preview or play.
    >>> code_unit.inline_examples(
    ...     ethan_joris_start_example.__doc__, 
    ...     locals(), globals(), 
    ...     verify_examples = False)
    >>> mouse_down_and_sleep(joris, joris.root._0_7_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._0_7_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._0_6_mc, 1.0 / ethan._speed)
    >>> mouse_down_and_sleep(joris, joris.root._1_7_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._1_7_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._1_6_mc, 1.0 / ethan._speed)
    >>> mouse_down_and_sleep(joris, joris.root._2_8_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._2_8_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._2_7_mc, 1.0 / ethan._speed)
    >>> mouse_down_and_sleep(joris, joris.root._2_6_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._2_6_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._3_8_mc, 1.0 / ethan._speed)
    >>> mouse_down_and_sleep(joris, joris.root._3_6_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._3_6_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._0_8_mc, 1.0 / ethan._speed)
    >>> joris.pb()
    ,,,,,,OXO
    ,,,,,,OX,
    ,,,,,,XOX
    ,,,,,,X,O
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,

    Joris previews capture.
    >>> mouse_down_and_sleep(joris, joris.root._1_8_mc, 1.0 / joris._speed)
    >>> board_diff(joris, joris.root._0_8_mc, 'currentLabel', 'empty_black')
    
    Joris cannot play over white's stone.  Previous preview reverts.
    >>> mouse_down_and_sleep(joris, joris.root._0_8_mc, 1.0 / joris._speed)
    >>> board_diff(joris, joris.root._0_8_mc, 'currentLabel', 'white')
    >>> board_diff(joris, joris.root._1_8_mc, 'currentLabel', 'empty_black')
    >>> mouse_down_and_sleep(joris, joris.root._0_8_mc, 1.0 / joris._speed) 

    Joris plays elsewhere and captures.
    >>> mouse_down_and_sleep(joris, joris.root._3_7_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._3_7_mc, 1.0 / joris._speed)

    Ethan remains in corner.
    >>> board_diff(joris, joris.root._0_8_mc, 'currentLabel', 'white')
    >>> board_diff(ethan, ethan.root._0_8_mc, 'currentLabel', 'white')
    '''


def preview_liberty_example():
    '''When Ezra previews liberties, they are only resent when modified.
    >>> code_unit.inline_examples(
    ...     ethan_joris_start_example.__doc__, 
    ...     locals(), globals(), 
    ...     verify_examples = False)
    >>> mouse_down_and_sleep(joris, joris.root._0_0_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._0_0_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._1_1_mc, 1.0 / ethan._speed)
    >>> mouse_down_and_sleep(joris, joris.root._3_1_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._3_3_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._2_4_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._1_0_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._2_0_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._3_0_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._1_0_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._1_0_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._1_2_mc, 1.0 / ethan._speed)
    >>> joris.root._0_0_mc.block_north_mc.currentLabel
    'black_warning'
    >>> joris.root._0_0_mc.block_west_mc.currentLabel
    'black_warning'
    
    Joris previews liberty block.
    >>> mouse_down_and_sleep(joris, joris.root._2_0_mc, 1.0 / joris._speed)
    >>> joris.ambassador.receives[-1].get('_0_0_mc')
    {'block_west_mc': {'currentLabel': 'black_block'}, 'block_north_mc': {'currentLabel': 'black_block'}}
    >>> mouse_down_and_sleep(joris, joris.root._2_1_mc, 1.0 / joris._speed)
    >>> joris.ambassador.receives[-1].get('_0_0_mc')
    {'block_west_mc': {'currentLabel': 'black_warning'}, 'block_north_mc': {'currentLabel': 'black_warning'}}
    >>> mouse_down_and_sleep(joris, joris.root._2_2_mc, 1.0 / joris._speed)

    Joris sees nothing new about liberties for 0,0, 
    since it is the same as previous and before preview.
    >>> joris.ambassador.receives[-1].get('_0_0_mc')
    '''
    

def partner_liberty_example():
    '''Joris sees blocked liberties of Ethan when either player moves.
    >>> code_unit.inline_examples(
    ...     preview_suicide_example.__doc__, 
    ...     locals(), globals(), 
    ...     verify_examples = False)
    >>> joris.pb()
    ,,,,,,OXO
    ,,,,,,OX,
    ,,,,,,X,X
    ,,,,,,XXO
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,

    Ethan is in danger.
    >>> board_diff(joris, joris.root._3_8_mc.block_north_mc,
    ...     'currentLabel', 'white_danger')
    >>> board_diff(joris, joris.root._3_8_mc.block_east_mc,
    ...     'currentLabel', 'white_danger')
    >>> board_diff(joris, joris.root._3_8_mc.block_south_mc,
    ...     'currentLabel', 'none')
    >>> board_diff(joris, joris.root._3_8_mc.block_west_mc,
    ...     'currentLabel', 'white_danger')
    
    Ethan extends.
    >>> mouse_down_and_sleep(ethan, ethan.root._4_8_mc, 1.0 / ethan._speed)

    Joris sees Ethan is out of white_danger, and in white_warning at north, west, east borders.
    >>> board_diff(joris, joris.root._3_8_mc.block_north_mc,
    ...     'currentLabel', 'white_warning')
    >>> board_diff(joris, joris.root._3_8_mc.block_east_mc,
    ...     'currentLabel', 'white_warning')
    >>> board_diff(joris, joris.root._3_8_mc.block_south_mc,
    ...     'currentLabel', 'none')
    >>> board_diff(joris, joris.root._3_8_mc.block_west_mc,
    ...     'currentLabel', 'white_warning')
    >>> board_diff(joris, joris.root._4_8_mc.block_north_mc,
    ...     'currentLabel', 'none')
    >>> board_diff(joris, joris.root._4_8_mc.block_east_mc,
    ...     'currentLabel', 'white_warning')
    >>> board_diff(joris, joris.root._4_8_mc.block_south_mc,
    ...     'currentLabel', 'none')
    >>> board_diff(joris, joris.root._4_8_mc.block_west_mc,
    ...     'currentLabel', 'none')

    Joris follows.  Ethan is back in white_danger.
    >>> mouse_down_and_sleep(joris, joris.root._4_7_mc, 1.0 / joris._speed)
    >>> board_diff(joris, joris.root._3_8_mc.block_north_mc,
    ...     'currentLabel', 'white_danger')
    >>> board_diff(joris, joris.root._3_8_mc.block_east_mc,
    ...     'currentLabel', 'white_danger')
    >>> board_diff(joris, joris.root._3_8_mc.block_south_mc,
    ...     'currentLabel', 'none')
    >>> board_diff(joris, joris.root._3_8_mc.block_west_mc,
    ...     'currentLabel', 'white_danger')
    >>> board_diff(joris, joris.root._4_8_mc.block_north_mc,
    ...     'currentLabel', 'none')
    >>> board_diff(joris, joris.root._4_8_mc.block_east_mc,
    ...     'currentLabel', 'white_danger')
    >>> board_diff(joris, joris.root._4_8_mc.block_south_mc,
    ...     'currentLabel', 'none')
    >>> board_diff(joris, joris.root._4_8_mc.block_west_mc,
    ...     'currentLabel', 'white_danger')
    >>> mouse_down_and_sleep(joris, joris.root._4_7_mc, 1.0 / joris._speed)
    >>> joris.pb()
    ,,,,,,OXO
    ,,,,,,OX,
    ,,,,,,X,X
    ,,,,,,XXO
    ,,,,,,,XO
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    '''

def liberty_block_example():
    '''On 3x3, black sees white liberties blocked.
    >>> code_unit.inline_examples(
    ...     ethan_lukasz_begin_example.__doc__, 
    ...     locals(), globals(), 
    ...     verify_examples = False)
    >>> lukasz = black
    >>> computer_lukasz = white
    >>> wait = 4.0 / lukasz._speed
    >>> lukasz.root.lobby_mc._00_mc.capture_3_3_mc.dispatchEvent(mouseDown)
    >>> time.sleep(wait)
    >>> mouse_down_and_sleep(lukasz, lukasz.root.game_over_mc.start_mc, wait)

    FOR REPLAY, COMPUTER IS NOT PLAYING.
    >>> mouse_down_and_sleep(black, black.root.game_over_mc.white_computer_mc.enter_mc, wait)
    >>> property_diff(black, black.root.game_over_mc.white_computer_mc, 'currentLabel', 'none')
    >>> mouse_down_and_sleep(lukasz, lukasz.root._1_1_mc, wait)
    >>> mouse_down_and_sleep(lukasz, lukasz.root._1_1_mc, wait)
    >>> mouse_down_and_sleep(computer_lukasz, computer_lukasz.root._1_2_mc, wait)
    >>> black.root._1_2_mc.block_west_mc.currentLabel
    'white_warning'
    >>> black.root._1_1_mc.block_east_mc.currentLabel
    'black_block'
    >>> mouse_down_and_sleep(lukasz, lukasz.root._0_2_mc, wait)
    >>> mouse_down_and_sleep(lukasz, lukasz.root._0_2_mc, wait)
    >>> mouse_down_and_sleep(lukasz, lukasz.root._0_1_mc, wait)
    >>> mouse_down_and_sleep(lukasz, lukasz.root._0_1_mc, wait)
    >>> mouse_down_and_sleep(computer_lukasz, computer_lukasz.root._0_2_mc, wait)
    >>> black.pb()
    ,XO
    ,XO
    ,,,
    >>> black.root.option_mc.block_mc.currentLabel
    'show'
    >>> black.root._0_2_mc.block_west_mc.currentLabel
    'white_danger'
    >>> black.root._1_2_mc.block_west_mc.currentLabel
    'white_danger'
    >>> black.root._0_1_mc.block_east_mc.currentLabel
    'black_block'
    >>> black.root._1_1_mc.block_east_mc.currentLabel
    'black_block'
    '''


def formation_example():
    '''Joris sees a formation.
    >>> code_unit.inline_examples(
    ...     ethan_joris_start_example.__doc__, 
    ...     locals(), globals(), 
    ...     verify_examples = False)

    Joris can see territory, defend, attack.
    >>> time.sleep(1.0 / joris._speed)
    >>> property_diff(joris, joris.root.profit_mc, 'currentLabel', 'show')
    >>> property_diff(joris, joris.root.defend_mc, 'currentLabel', 'show')
    >>> property_diff(joris, joris.root.attack_mc, 'currentLabel', 'show')

    Joris sees an intersection to press.
    >>> property_diff(joris, joris.root._2_5_mc, 'currentLabel', 'empty_black')

    This intersection is to the right and down.
    >>> if not (1 <= joris.root['_2_5_mc'].x and 1 <= joris.root['_2_5_mc'].y): joris.root['_2_5_mc'].x, joris.root['_2_5_mc'].y 

    Joris sees a place where he may cut the cake to claim a field.
    There are no other stones on the board and 5x5 empty intersections.
    No field animation is playing now.
    >>> property_diff(joris, joris.root.formation_field_mc.rotate_0_mc.response_mc, 
    ...     'currentLabel', 'none')
    
    Joris clicks on the upper right star point.
    Soon, Joris previews a black stone appear there.
    >>> mouse_down_and_sleep(joris, joris.root._2_5_mc, 1.0 / joris._speed)
    >>> property_diff(joris, joris.root._2_5_mc, 'currentLabel', 'question_black')

    Joris also sees a field formation about his placed stone.
    >>> property_diff(joris, joris.root.formation_field_mc.rotate_0_mc.response_mc, 
    ...     'currentLabel', 'response')
    >>> property_diff(joris, joris.root.formation_field_mc, 
    ...     'x', joris.root['_2_5_mc'].x)
    >>> property_diff(joris, joris.root.formation_field_mc, 
    ...     'y', joris.root['_2_5_mc'].y)

    Joris receives no extra pieces of cake.
    >>> property_diff(joris, joris.root.extra_stone_gift_mc, 
    ...     'currentLabel', '_0')

    Joris clicks on the upper left star point.
    Soon, Joris previews a black stone appear there.
    >>> if not joris.root.formation_leap_mc.x != joris.root['_2_2_mc'].x: joris.root.formation_leap_mc.x, joris.root['_2_2_mc'].x
    >>> mouse_down_and_sleep(joris, joris.root._2_2_mc, 1.0 / joris._speed)
    >>> property_diff(joris, joris.root._2_2_mc, 'currentLabel', 'question_black')

    Joris also sees a field formation about his previewed stone.
    >>> property_diff(joris, joris.root.formation_field_mc.rotate_0_mc.response_mc, 
    ...     'currentLabel', 'response')
    >>> property_diff(joris, joris.root.formation_field_mc, 
    ...     'x', joris.root['_2_2_mc'].x)
    >>> property_diff(joris, joris.root.formation_field_mc, 
    ...     'y', joris.root['_2_2_mc'].y)

#+    Joris sees no formation between his previews.
#+    >>> property_diff(joris, joris.root.formation_leap_mc.rotate_90_mc.response_mc, 
#+    ...     'currentLabel', 'none')
#+    >>> if not joris.root.formation_leap_mc.x != joris.root['_2_2_mc'].x:
#+    ...     joris.root.formation_leap_mc.x, joris.root['_2_2_mc'].x
#+    
#+    Previous preview disappears.
#+    >>> property_diff(joris, joris.root._2_5_mc, 'currentLabel', 'empty_black')
#+
#+    Joris clicks on the upper left corner.
#+    Soon, Joris previews a black stone appear there.
#+    >>> mouse_down_and_sleep(joris, joris.root._0_0_mc, 1.0 / joris._speed)
#+    >>> property_diff(joris, joris.root._0_0_mc, 'currentLabel', 'question_black')
#+
#+    Joris sees no formation about his previewed stone.
#+    >>> property_diff(joris, joris.root.formation_field_mc.rotate_0_mc.response_mc, 
#+    ...     'currentLabel', 'none')
#+    >>> if not joris.root.formation_field_mc.x != joris.root['_0_0_mc'].x: joris.root.formation_field_mc.x, joris.root['_0_0_mc'].x
#+
#+    #Hard to verify expiring animations.
#+    #Soon field formation goes away.
#+    #>>> time.sleep(2.0 / joris._speed)
#+    #>>> property_diff(joris, joris.root.formation_field_mc.rotate_0_mc.response_mc, 
#+    #...     'currentLabel', 'none')
#+    
#+    Joris clicks on the upper right star point.
#+    Soon, Joris sees a black stone appear there.
#+    >>> mouse_down_and_sleep(joris, joris.root._2_5_mc, 1.0 / joris._speed)
#+    >>> property_diff(joris, joris.root._2_5_mc, 'currentLabel', 'question_black')
#+    >>> mouse_down_and_sleep(joris, joris.root._2_5_mc, 1.0 / joris._speed)
#+    >>> property_diff(joris, joris.root._2_5_mc, 'currentLabel', 'black')
#+
#+    Joris receives one extra pieces of cake.
#+    >>> property_diff(joris, joris.root.extra_stone_gift_mc, 
#+    ...     'currentLabel', '_1')
#+
#+    Joris also sees a field formation about his placed stone.
#+    >>> property_diff(joris, joris.root.formation_field_mc.rotate_0_mc.response_mc, 
#+    ...     'currentLabel', 'response')
#+    >>> property_diff(joris, joris.root.formation_field_mc, 
#+    ...     'x', joris.root['_2_5_mc'].x)
#+    >>> property_diff(joris, joris.root.formation_field_mc, 
#+    ...     'y', joris.root['_2_5_mc'].y)
#+
#+    Joris cannot play on top of his own stone.
#+    Joris cannot play when it is not his turn.
    '''

def preview_formation_example():
    '''After white moves, Joris sees white's formation.
    >>> code_unit.inline_examples(
    ...     ethan_joris_start_example.__doc__, 
    ...     locals(), globals(), 
    ...     verify_examples = False)

    >>> ezra = joris
    >>> mouse_down_and_sleep(joris, joris.root._4_4_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._4_4_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._2_2_mc, 1.0 / ethan._speed)
    >>> mouse_down_and_sleep(joris, joris.root._4_6_mc, 1.0 / joris._speed)

    EZRA DOES NOT SEE OLD SOUTH QUARTER FIELD.
    >>> property_diff(joris, joris.root.formation_quarter_field_mc.rotate_180_mc.response_mc, 
    ...     'currentLabel', 'none')
    >>> mouse_down_and_sleep(joris, joris.root._2_4_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._2_4_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._4_2_mc, 1.0 / ethan._speed)
    >>> mouse_down_and_sleep(joris, joris.root._2_6_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._3_4_mc, 1.0 / joris._speed)

    EZRA DOES NOT SEE OLD JUMP ATTACK.
    >>> property_diff(joris, joris.root.formation_jump_attack_mc.rotate_90_mc.response_mc, 
    ...     'currentLabel', 'none')
    >>> property_diff(joris, joris.root.formation_jump_attack_mc.rotate_180_mc.response_mc, 
    ...     'currentLabel', 'none')
    >>> mouse_down_and_sleep(joris, joris.root._5_4_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._4_5_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._2_5_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._1_4_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._3_6_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._6_4_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._6_2_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._1_3_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._6_2_mc, 1.0 / joris._speed)

    >>> property_diff(joris, joris.root.formation_jump_attack_mc.rotate_0_mc.response_mc, 
    ...     'currentLabel', 'response')

    EZRA DOES NOT SEE OLD JUMP ATTACK.
    >>> property_diff(joris, joris.root.formation_jump_attack_mc.rotate_90_mc.response_mc, 
    ...     'currentLabel', 'none')
    >>> property_diff(joris, joris.root.formation_jump_attack_mc.rotate_180_mc.response_mc, 
    ...     'currentLabel', 'none')
    '''

def white_formation_example():
    '''After white moves, Joris sees white's formation.
    >>> code_unit.inline_examples(
    ...     ethan_joris_start_example.__doc__, 
    ...     locals(), globals(), 
    ...     verify_examples = False)

    >>> mouse_down_and_sleep(joris, joris.root._2_2_mc, 1.0 / joris._speed)
    >>> import embassy
    >>> clear_formation_news = embassy.get_clear_formation_news(joris.root)
    >>> if not clear_formation_news:  print 'where is formation?'
    >>> mouse_down_and_sleep(joris, joris.root._2_2_mc, 1.0 / joris._speed)
    >>> clear_formation_news = embassy.get_clear_formation_news(joris.root)
    >>> if not clear_formation_news:  print 'where is formation?'
    >>> mouse_down_and_sleep(ethan, ethan.root._6_6_mc, 1.0 / ethan._speed)
    >>> clear_formation_news = embassy.get_clear_formation_news(joris.root)
    >>> if not clear_formation_news:  print 'where is formation?'
    >>> property_diff(joris, joris.root.formation_field_mc.rotate_0_mc.response_mc, 
    ...     'currentLabel', 'response')
    >>> property_diff(joris, joris.root.formation_field_mc, 
    ...     'x', joris.root['_6_6_mc'].x)
    >>> property_diff(joris, joris.root.formation_field_mc, 
    ...     'y', joris.root['_6_6_mc'].y)
    
    After Joris moves and previews same formation as white's, 
    then makes different formation that white's last, 
    Joris does not see white's last formation.
    >>> mouse_down_and_sleep(joris, joris.root._2_6_mc, 1.0 / joris._speed)
    >>> property_diff(joris, joris.root.formation_field_mc, 
    ...     'y', joris.root['_2_6_mc'].y)
    >>> mouse_down_and_sleep(joris, joris.root._2_4_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._2_4_mc, 1.0 / joris._speed)
    >>> clear_formation_news = embassy.get_clear_formation_news(joris.root)
    >>> if not clear_formation_news:  print 'where is formation?'
    >>> if not property_diff(joris, joris.root.formation_field_mc, 
    ...         'y', joris.root['_6_6_mc'].y):  
    ...     ## print 'should have moved or turned off?'
    ...     property_diff(joris, joris.root.formation_field_mc.rotate_0_mc.response_mc, 'currentLabel', 
    ...         'none')

    Formation state is tricky to detect, 
    because they auto-expire on the client side, 
    which the Python actionscript and remote control does not detect.
    Yet only one formation exists, so Joris moves the formation.

    After Joris previews and sees same formation as white's last,
    and then different formation than last white, 
    then moves, Joris does not see white's previous formation.
    >>> mouse_down_and_sleep(ethan, ethan.root._6_4_mc, 1.0 / ethan._speed)
    >>> clear_formation_news = embassy.get_clear_formation_news(joris.root)
    >>> if not 'formation_jump_mc' in clear_formation_news:  print 'where is formation?'
    >>> mouse_down_and_sleep(joris, joris.root._2_3_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._2_6_mc, 1.0 / joris._speed)
    >>> property_diff(joris, joris.root.formation_jump_mc, 
    ...     'y', joris.root['_2_6_mc'].y)
    >>> mouse_down_and_sleep(joris, joris.root._1_6_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._1_6_mc, 1.0 / joris._speed)
    >>> clear_formation_news = embassy.get_clear_formation_news(joris.root)
    >>> if 'formation_jump_mc' in clear_formation_news:  clear_formation_news
    >>> if not property_diff(joris, joris.root.formation_jump_mc, 
    ...         'y', joris.root['_6_4_mc'].y):  
    ...     ## print 'should have moved or turned off?'
    ...     property_diff(joris, joris.root.formation_jump_mc.rotate_270_mc.response_mc, 'currentLabel', 
    ...         'none')
    >>> joris.pb()
    ,,,,,,,,,
    ,,,,,,X,,
    ,,X,X,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,O,O,,
    ,,,,,,,,,
    ,,,,,,,,,

    #+ After Joris previews and does not see his formation then moves, 
    #+ Joris does not see white's previous formation.
    '''


from intersection_mc import get_response_rotate_names
def formation_open_tiger_yawn_example():
    '''When turn the corner, see formation.
    >>> code_unit.inline_examples(
    ...     ethan_joris_start_example.__doc__, 
    ...     locals(), globals(), 
    ...     verify_examples = False)
    >>> wait = 3.0
    >>> designer = joris
    >>> gnugo = ethan

    PLAYER CAN SEE ATTACK, AND DEFEND AND CRITICAL.
    >>> property_diff(joris, joris.root.critical_mc, 'currentLabel', 'show')
    >>> property_diff(joris, joris.root.defend_mc, 'currentLabel', 'show')
    >>> property_diff(joris, joris.root.attack_mc, 'currentLabel', 'show')

    _5_5 board
    >>> mouse_down_and_sleep(joris, joris.root.game_over_mc._5_5_mc.enter_mc, wait / joris._speed)
    >>> property_diff(joris, joris.root, 'currentLabel', '_5_5')
    >>> property_diff(joris, joris.root.game_over_mc._5_5_mc.enter_mc, 'currentLabel', 'none')
    >>> property_diff(ethan, ethan.root, 'currentLabel', '_5_5')
    >>> property_diff(ethan, ethan.root.game_over_mc._5_5_mc.enter_mc, 'currentLabel', 'none')

    >>> mouse_down_and_sleep(joris, joris.root._4_1_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._4_0_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._0_2_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._1_1_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._1_2_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._1_2_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._2_2_mc, wait / ethan._speed)
    >>> mouse_down_and_sleep(joris, joris.root._2_1_mc, wait / joris._speed)
    >>> joris.pb()
    ,,,,,
    ,,X,,
    ,%O,,
    ,,,,,
    ,,,,,

    PLAYER SEES OPEN TIGER YAWN AND TIGER LICK.
    >>> get_response_rotate_names(joris.root.formation_open_tiger_yawn_mc)
    ['rotate_270_mc']
    >>> get_response_rotate_names(joris.root.formation_tiger_lick_mc)
    ['row_reflect_rotate_0_mc']
    >>> mouse_down_and_sleep(joris, joris.root._1_1_mc, wait / joris._speed)

    PLAYER DOES NOT SEE PRESS.
    >>> get_response_rotate_names(joris.root.formation_press_mc)
    []
    >>> mouse_down_and_sleep(joris, joris.root._1_1_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._2_1_mc, wait / ethan._speed)
    >>> mouse_down_and_sleep(joris, joris.root._2_3_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._1_3_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._2_3_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._1_3_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._1_3_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._2_3_mc, wait / ethan._speed)
    >>> mouse_down_and_sleep(joris, joris.root._1_0_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._1_0_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._4_1_mc, wait / ethan._speed)
    >>> mouse_down_and_sleep(joris, joris.root._2_0_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._2_0_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._3_0_mc, wait / ethan._speed)
    >>> mouse_down_and_sleep(joris, joris.root._2_4_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._2_4_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._3_4_mc, wait / ethan._speed)
    >>> mouse_down_and_sleep(joris, joris.root._1_4_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._1_4_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._3_3_mc, wait / ethan._speed)
    >>> mouse_down_and_sleep(joris, joris.root._3_2_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._4_2_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._4_3_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._3_1_mc, wait / joris._speed)
    '''
    
def influence_and_top_move_sgf_example():
    '''After replay SGF, Michael sees a tiger chomp formation.
    >>> code_unit.inline_examples(
    ...     ethan_joris_start_example.__doc__, 
    ...     locals(), globals(), 
    ...     verify_examples = False)

    Michael can see territory and top move.
    >>> michael = joris
    >>> wait = 4.0
    >>> time.sleep(wait / michael._speed)
    >>> property_diff(michael, michael.root.territory_mc, 'currentLabel', 'show')
    >>> property_diff(michael, michael.root.top_move_mc, 'currentLabel', 'show')
    >>> from master import play_sgf
    >>> play_sgf('sgf/test_initial_influence.sgf', ethan, michael, mouse_down_and_sleep, wait)

    Michael sees monkey hop formation near GnuGo's last stone.
    >>> property_diff(michael, michael.root._5_6_mc.top_move_mc, 'currentLabel', 'white')

    Michael sees territory disappear.
    >>> property_diff(michael, michael.root._5_5_mc.territory_mc, 'currentLabel', 'neutral')
    
    After Michael and Ethan moves, old top move disappears.
    >>> mouse_down_and_sleep(michael, michael.root._1_0_mc, wait / michael._speed)

    After Michael previews, Michael sees top move of white.
    >>> property_diff(michael, michael.root._5_6_mc.top_move_mc, 'currentLabel', 'white')
    >>> for row in michael.intersection_mc_array:
    ...     for intersection_mc in row:
    ...         if intersection_mc.top_move_mc.currentLabel != 'none':
    ...             print intersection_mc.name, intersection_mc.top_move_mc.currentLabel
    _5_6_mc white
    >>> mouse_down_and_sleep(michael, michael.root._1_0_mc, wait / michael._speed)

    After Michael moves but before Ethan moves, 
    Michael no longer sees top move of white.
    >>> for row in michael.intersection_mc_array:
    ...     for intersection_mc in row:
    ...         if intersection_mc.top_move_mc.currentLabel != 'none':
    ...             print intersection_mc.name, intersection_mc.top_move_mc.currentLabel
    >>> mouse_down_and_sleep(ethan, ethan.root._4_6_mc, wait / ethan._speed)

    Michael sees monkey hop formation near GnuGo's last stone.
    >>> property_diff(michael, michael.root._5_6_mc.top_move_mc, 'currentLabel', 'none')
    '''


def top_move_disappear_example():
    '''Ethan pretends to be marije, plays and sees no egg.
        >>> code_unit.inline_examples(
        ...     ethan_lukasz_begin_example.__doc__, 
        ...     locals(), globals(), 
        ...     verify_examples = False)
        >>> wait = 4.0 / black._speed
        >>> sloth = 1.0 / black._speed
    
        >>> marije = black
        >>> computer_marije = white

    >>> # example.log level 20 at Tue Aug 24 16:05:03 2010

    >>> marije.root.level_mc.none_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 4.630000)
    >>> marije.root.comment_mc.none_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 1.165000)
    >>> marije.root.lobby_mc.main_mc._04_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 1.907000)
    >>> marije.root.lobby_mc._04_mc.dominate_5_5_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 1.336000)
    >>> time.sleep(sloth * 2.765000)

        FOR REPLAY, COMPUTER IS NOT PLAYING.
        >>> marije.root.game_over_mc.white_computer_mc.enter_mc.dispatchEvent(mouseDown)

        white computer button is not blinking.
        >>> marije.root.game_over_mc.white_computer_mc.enter_mc.currentLabel
        'none'
        >>> marije.root.game_over_mc.white_computer_mc.enter_mc.gotoAndPlay('none')
        >>> time.sleep(wait)
    >>> mouse_down_and_sleep(marije, marije.root.game_over_mc.start_mc, wait)
    >>> time.sleep(sloth * 5.768000)
    >>> mouse_down_and_sleep(marije, marije.root._2_2_mc, wait)
    >>> time.sleep(sloth * 5.705000)
    >>> mouse_down_and_sleep(marije, marije.root._2_2_mc, wait)
    >>> from intersection_mc import children_label_equals
    >>> children_label_equals(marije.intersection_mc_array, 'top_move_mc', 'white')
    []
    '''

def liberty_share_example():
    '''Michael can see liberty warning at 0,2.
    >>> code_unit.inline_examples(
    ...     ethan_joris_start_example.__doc__, 
    ...     locals(), globals(), 
    ...     verify_examples = False)

    Michael can see liberty.
    >>> wait = 3.0
    >>> time.sleep(wait / joris._speed)
    >>> property_diff(joris, joris.root.liberty_mc, 'currentLabel', 'show')

    _5_5 board
    >>> mouse_down_and_sleep(joris, joris.root.game_over_mc._5_5_mc.enter_mc, wait / joris._speed)
    >>> property_diff(joris, joris.root, 'currentLabel', '_5_5')
    >>> property_diff(joris, joris.root.game_over_mc._5_5_mc.enter_mc, 'currentLabel', 'none')
    >>> property_diff(ethan, ethan.root, 'currentLabel', '_5_5')
    >>> property_diff(ethan, ethan.root.game_over_mc._5_5_mc.enter_mc, 'currentLabel', 'none')

    >>> mouse_down_and_sleep(joris, joris.root._0_0_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._0_2_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._0_0_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._0_0_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._2_2_mc, wait / ethan._speed)
    >>> mouse_down_and_sleep(joris, joris.root._0_1_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._0_4_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._0_4_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._1_4_mc, wait / ethan._speed)
    >>> mouse_down_and_sleep(joris, joris.root._0_3_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._0_3_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._0_2_mc, wait / ethan._speed)
    >>> joris.root._0_1_mc.liberty_west_mc.currentLabel
    'black_warning'
    >>> joris.root._0_1_mc.liberty_east_mc.currentLabel
    'white_warning'
    '''


def liberty_3_3_example():
    '''After replay SGF, Michael sees a tiger chomp formation.
    >>> code_unit.inline_examples(
    ...     ethan_joris_start_example.__doc__, 
    ...     locals(), globals(), 
    ...     verify_examples = False)

    Michael can see liberty.
    >>> wait = 3.0
    >>> time.sleep(wait / joris._speed)
    >>> property_diff(joris, joris.root.liberty_mc, 'currentLabel', 'show')
    >>> from master import play_sgf
    >>> play_sgf('sgf/liberty_3_3_example.sgf', ethan, joris, mouse_down_and_sleep, wait)

    Michael sees monkey hop formation near GnuGo's last stone.
    >>> property_diff(joris, joris.root._0_1_mc.liberty_west_mc, 'currentLabel', 'black_danger')

    Michael sees territory disappear.
    >>> property_diff(joris, joris.root._5_5_mc.territory_mc, 'currentLabel', 'neutral')
    '''


def preview_territory_example():
    '''Jade previews enclosing small corner.  He sees corner turn black.
    >>> code_unit.inline_examples(
    ...     ethan_joris_start_example.__doc__, 
    ...     locals(), globals(), 
    ...     verify_examples = False)
    >>> jade = black
    >>> black.root._2_1_mc.dispatchEvent(mouseDown)
    >>> time.sleep(wait)
    >>> black.root._2_1_mc.dispatchEvent(mouseDown)
    >>> time.sleep(wait)
    >>> white.root._6_2_mc.dispatchEvent(mouseDown)
    >>> time.sleep(wait)
    >>> black.root._0_1_mc.territory_mc.currentLabel
    'neutral'
    >>> black.root._1_2_mc.dispatchEvent(mouseDown)
    >>> time.sleep(wait)
    >>> black.root._0_1_mc.territory_mc.currentLabel
    'black'
    >>> black.root._6_4_mc.dispatchEvent(mouseDown)
    >>> time.sleep(wait)
    >>> black.root._0_1_mc.territory_mc.currentLabel
    'neutral'
    >>> black.root._1_2_mc.dispatchEvent(mouseDown)
    >>> time.sleep(wait)
    >>> black.root._1_2_mc.dispatchEvent(mouseDown)
    >>> time.sleep(wait)
    >>> white.root._6_4_mc.dispatchEvent(mouseDown)
    >>> time.sleep(wait)
    >>> black.root._0_1_mc.territory_mc.currentLabel
    'black'
    '''

def diagonal_cut_sgf_example():
    '''After replay SGF, Joris sees a diagonal cut formation.
    >>> code_unit.inline_examples(
    ...     ethan_joris_start_example.__doc__, 
    ...     locals(), globals(), 
    ...     verify_examples = False)

    Joris can see territory, defend, attack.
    >>> wait = 2.0
    >>> time.sleep(wait / joris._speed)
    >>> property_diff(joris, joris.root.profit_mc, 'currentLabel', 'show')
    >>> property_diff(joris, joris.root.defend_mc, 'currentLabel', 'show')
    >>> property_diff(joris, joris.root.attack_mc, 'currentLabel', 'show')
    >>> from master import play_sgf
    >>> play_sgf('sgf/diagonal_cut_example.sgf', ethan, joris, mouse_down_and_sleep, wait)

    Joris sees a diagonal cut formation about Ethan's stone.
    >>> if property_diff(joris, joris.root.formation_diagonal_cut_mc.rotate_0_mc.response_mc, 'currentLabel', 'response'):
    ...     family_tree(joris.root.formation_diagonal_cut_mc)
    >>> property_diff(joris, joris.root.formation_diagonal_cut_mc, 
    ...     'x', joris.root['_2_1_mc'].x)
    >>> property_diff(joris, joris.root.formation_diagonal_cut_mc, 
    ...     'y', joris.root['_2_1_mc'].y)
    '''


def block_sgf_example():
    '''After replay SGF, Joris sees a diagonal cut formation.
    >>> code_unit.inline_examples(
    ...     ethan_joris_start_example.__doc__, 
    ...     locals(), globals(), 
    ...     verify_examples = False)

    Joris can see territory, defend, attack.
    >>> wait = 2.0
    >>> time.sleep(wait / joris._speed)
    >>> property_diff(joris, joris.root.profit_mc, 'currentLabel', 'show')
    >>> property_diff(joris, joris.root.defend_mc, 'currentLabel', 'show')
    >>> property_diff(joris, joris.root.attack_mc, 'currentLabel', 'show')
    >>> from master import play_sgf
    >>> play_sgf('sgf/block_example.sgf', ethan, joris, mouse_down_and_sleep, wait)

    Joris sees a diagonal cut formation about Ethan's stone.
    >>> if property_diff(joris, joris.root.formation_block_mc.rotate_0_mc.response_mc, 'currentLabel', 'response'):
    ...     family_tree(joris.root.formation_block_mc)
    >>> property_diff(joris, joris.root.formation_block_mc, 
    ...     'x', joris.root['_2_3_mc'].x)
    >>> property_diff(joris, joris.root.formation_block_mc, 
    ...     'y', joris.root['_2_3_mc'].y)
    '''


def jump_underneath_sgf_example():
    '''After replay SGF, Joris sees a diagonal cut formation.
    >>> code_unit.inline_examples(
    ...     ethan_joris_start_example.__doc__, 
    ...     locals(), globals(), 
    ...     verify_examples = False)

    Joris can see territory, defend, attack.
    >>> wait = 2.0
    >>> time.sleep(wait / joris._speed)
    >>> property_diff(joris, joris.root.profit_mc, 'currentLabel', 'show')
    >>> property_diff(joris, joris.root.defend_mc, 'currentLabel', 'show')
    >>> property_diff(joris, joris.root.attack_mc, 'currentLabel', 'show')
    >>> from master import play_sgf
    >>> play_sgf('sgf/jump_underneath_example.sgf', ethan, joris, mouse_down_and_sleep, wait)

    Joris sees a jump underneath to his stone.
    >>> if property_diff(joris, joris.root.formation_jump_underneath_mc.rotate_0_mc.response_mc, 'currentLabel', 'response'):
    ...     family_tree(joris.root.formation_jump_underneath_mc)
    >>> property_diff(joris, joris.root.formation_jump_underneath_mc, 
    ...     'x', joris.root['_3_1_mc'].x)
    >>> property_diff(joris, joris.root.formation_jump_underneath_mc, 
    ...     'y', joris.root['_3_1_mc'].y)

    Previous diagonal attack is reset.
    >>> from pprint import pprint
    >>> if property_diff(joris, joris.root.formation_diagonal_attack_mc.rotate_0_mc.response_mc, 'currentLabel', 'response'):
    ...     family_tree(joris.root.formation_diagonal_attack_mc)
    >>> if property_diff(joris, joris.root.formation_diagonal_attack_mc.rotate_270_mc.response_mc, 'currentLabel', 'none'):
    ...     pprint(family_tree(joris.root.formation_diagonal_attack_mc))

    >>> mouse_down_and_sleep(ethan, ethan.root._2_3_mc, 1.0 / ethan._speed)
    >>> mouse_down_and_sleep(joris, joris.root._1_3_mc, 1.0 / joris._speed)

    Joris sees a jump underneath to his stone.
    >>> if property_diff(joris, joris.root.formation_jump_underneath_mc.row_reflect_rotate_90_mc.response_mc, 'currentLabel', 'response'):
    ...     family_tree(joris.root.formation_jump_underneath_mc)
    >>> property_diff(joris, joris.root.formation_jump_underneath_mc, 
    ...     'x', joris.root['_1_3_mc'].x)
    >>> property_diff(joris, joris.root.formation_jump_underneath_mc, 
    ...     'y', joris.root['_1_3_mc'].y)
    '''


def crawl_sgf_example():
    '''After replay SGF, Joris sees a crawl formation.
    >>> code_unit.inline_examples(
    ...     ethan_joris_start_example.__doc__, 
    ...     locals(), globals(), 
    ...     verify_examples = False)

    Joris can see territory, defend, attack.
    >>> wait = 2.0
    >>> time.sleep(wait / joris._speed)
    >>> property_diff(joris, joris.root.profit_mc, 'currentLabel', 'show')
    >>> property_diff(joris, joris.root.defend_mc, 'currentLabel', 'show')
    >>> property_diff(joris, joris.root.attack_mc, 'currentLabel', 'show')
    >>> from master import play_sgf
    >>> play_sgf('sgf/crawl_example.sgf', ethan, joris, mouse_down_and_sleep, wait)

    Joris sees a double crawl to his stone.
    >>> from pprint import pprint
    >>> if property_diff(joris, joris.root.formation_crawl_mc.rotate_90_mc.response_mc, 'currentLabel', 'response'):
    ...     pprint(family_tree(joris.root.formation_crawl_mc))
    >>> if property_diff(joris, joris.root.formation_crawl_mc.row_reflect_rotate_270_mc.response_mc, 'currentLabel', 'response'):
    ...     pprint(family_tree(joris.root.formation_crawl_mc))
    >>> property_diff(joris, joris.root.formation_crawl_mc, 
    ...     'x', joris.root['_2_0_mc'].x)
    >>> property_diff(joris, joris.root.formation_crawl_mc, 
    ...     'y', joris.root['_2_0_mc'].y)
    '''


def diagonal_sharpening_sgf_example():
    '''After replay SGF, Joris sees a diagonal_cut_half formation.
    >>> code_unit.inline_examples(
    ...     ethan_joris_start_example.__doc__, 
    ...     locals(), globals(), 
    ...     verify_examples = False)

    Joris can see territory, defend, attack.
    >>> wait = 2.0
    >>> time.sleep(wait / joris._speed)
    >>> property_diff(joris, joris.root.profit_mc, 'currentLabel', 'show')
    >>> property_diff(joris, joris.root.defend_mc, 'currentLabel', 'show')
    >>> property_diff(joris, joris.root.attack_mc, 'currentLabel', 'show')
    >>> from master import play_sgf
    >>> play_sgf('sgf/diagonal_sharpening_example.sgf', ethan, joris, mouse_down_and_sleep, wait)

    Joris sees a diagonal_cut_half from Ethan's stone.
    >>> from pprint import pprint
    >>> if property_diff(joris, joris.root.formation_diagonal_cut_half_mc.rotate_90_mc.response_mc, 'currentLabel', 'response'):
    ...     pprint(family_tree(joris.root.formation_diagonal_cut_half_mc))
    >>> property_diff(joris, joris.root.formation_diagonal_cut_half_mc, 
    ...     'x', joris.root['_0_2_mc'].x)
    >>> property_diff(joris, joris.root.formation_diagonal_cut_half_mc, 
    ...     'y', joris.root['_0_2_mc'].y)
    '''


def long_knight_cut_half_sgf_example():
    '''After replay SGF, Joris sees a crawl formation.
    >>> code_unit.inline_examples(
    ...     ethan_joris_start_example.__doc__, 
    ...     locals(), globals(), 
    ...     verify_examples = False)

    Joris can see territory, defend, attack.
    >>> wait = 2.0
    >>> time.sleep(wait / joris._speed)
    >>> property_diff(joris, joris.root.profit_mc, 'currentLabel', 'show')
    >>> property_diff(joris, joris.root.defend_mc, 'currentLabel', 'show')
    >>> property_diff(joris, joris.root.attack_mc, 'currentLabel', 'show')
    >>> from master import play_sgf
    >>> play_sgf('sgf/long_knight_cut_half_example.sgf', ethan, joris, mouse_down_and_sleep, wait)

    Joris sees his stones are being cut apart.
    >>> from pprint import pprint
    >>> if property_diff(joris, joris.root.formation_jump_attack_mc.rotate_0_mc.response_mc, 'currentLabel', 'response'):
    ...     pprint(family_tree(joris.root.formation_jump_attack_mc))
    >>> property_diff(joris, joris.root.formation_jump_attack_mc, 
    ...     'x', joris.root['_4_2_mc'].x)
    >>> property_diff(joris, joris.root.formation_jump_attack_mc, 
    ...     'y', joris.root['_4_2_mc'].y)
    >>> if property_diff(joris, joris.root.formation_diagonal_attack_mc.rotate_180_mc.response_mc, 'currentLabel', 'response'):
    ...     pprint(family_tree(joris.root.formation_diagonal_attack_mc))
    >>> property_diff(joris, joris.root.formation_diagonal_attack_mc, 
    ...     'x', joris.root['_4_2_mc'].x)
    >>> property_diff(joris, joris.root.formation_diagonal_attack_mc, 
    ...     'y', joris.root['_4_2_mc'].y)

    Joris sees southwest stone is in danger.
    >>> if property_diff(joris, joris.root.formation_shoulder_hit_mc.rotate_0_mc.response_mc, 'currentLabel', 'response'):
    ...     pprint(family_tree(joris.root.formation_shoulder_hit_mc))
    >>> property_diff(joris, joris.root.formation_shoulder_hit_mc, 
    ...     'x', joris.root['_4_2_mc'].x)
    >>> property_diff(joris, joris.root.formation_shoulder_hit_mc, 
    ...     'y', joris.root['_4_2_mc'].y)

    Joris previews knight underneath.
    Trail of hearts hooks around to outside.
    >>> mouse_down_and_sleep(joris, joris.root._4_1_mc, 1.0 / joris._speed)
    >>> if property_diff(joris, joris.root.formation_knight_underneath_mc.rotate_0_mc.response_mc, 'currentLabel', 'response'):
    ...     pprint(family_tree(joris.root.formation_knight_underneath_mc))
    >>> property_diff(joris, joris.root.formation_knight_underneath_mc, 
    ...     'x', joris.root['_4_1_mc'].x)
    >>> property_diff(joris, joris.root.formation_knight_underneath_mc, 
    ...     'y', joris.root['_4_1_mc'].y)

    But Joris plays elsewhere.  Ethan cuts.  
    At Ethan's stone, Joris sees chariot_attack.
    >>> mouse_down_and_sleep(joris, joris.root._2_4_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._2_4_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._4_1_mc, 1.0 / ethan._speed)
    >>> if property_diff(joris, joris.root.formation_chariot_attack_mc.rotate_0_mc.response_mc, 'currentLabel', 'response'):
    ...     pprint(family_tree(joris.root.formation_chariot_attack_mc))
    >>> property_diff(joris, joris.root.formation_chariot_attack_mc, 
    ...     'x', joris.root['_4_1_mc'].x)
    >>> property_diff(joris, joris.root.formation_chariot_attack_mc, 
    ...     'y', joris.root['_4_1_mc'].y)

    At Ethan's stone, Joris sees block.
    >>> if property_diff(joris, joris.root.formation_block_mc.rotate_180_mc.response_mc, 'currentLabel', 'response'):
    ...     pprint(family_tree(joris.root.formation_block_mc))
    >>> property_diff(joris, joris.root.formation_block_mc, 
    ...     'x', joris.root['_4_1_mc'].x)
    >>> property_diff(joris, joris.root.formation_block_mc, 
    ...     'y', joris.root['_4_1_mc'].y)
    '''


def extra_stone_limit_example():
    ''' !^_^    only give extra stone or hide after last move of sequence 
    and then only if animation was made on last move.  
    >>> code_unit.inline_examples(
    ...         ethan_joris_start_example.__doc__,
    ...         locals(), globals(),
    ...         verify_examples = False)

    >>> laurens = joris

    Laurens has no extra stone
    >>> property_diff(joris, joris.root['extra_stone_gift_mc'], 'currentLabel', '_0')

    Laurens moves 2, 2
    >>> ## mouse_down_and_sleep(joris, joris.root._2_2_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._2_2_mc, 1.0 / joris._speed)

    For making field formation and ending his turn, Laurens gets extra stone
    >>> property_diff(joris, joris.root.formation_field_mc, 
    ...     'x', joris.root['_2_2_mc'].x)
    >>> property_diff(joris, joris.root['turn_mc'], 'currentLabel', 'white')
    >>> property_diff(joris, joris.root['extra_stone_gift_mc'], 'currentLabel', '_1')

    But Laurens cannot use it, because it is Ethan's turn
    Ethan moves at 6, 6
    >>> mouse_down_and_sleep(ethan, ethan.root._6_6_mc, 1.0 / ethan._speed)
    
    On Laurens' turn, he presses extra stone
    >>> mouse_down_and_sleep(joris, joris.root.extra_stone_gift_mc.use_mc, 1.0 / joris._speed)

    Laurens moves 2, 6
    >>> ##_mouse_down_and_sleep(joris, joris.root._2_6_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._2_6_mc, 1.0 / joris._speed)

    Although Laurens made field formation, Laurens does not get extra stone
    >>> property_diff(joris, joris.root.formation_field_mc, 
    ...     'x', joris.root['_2_6_mc'].x)
    >>> property_diff(joris, joris.root['extra_stone_gift_mc'], 'currentLabel', '_0')
    
    Laurens moves 2, 4
    For making jump formation and ending his turn, Laurens gets extra stone
    >>> ## mouse_down_and_sleep(joris, joris.root._2_4_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._2_4_mc, 1.0 / joris._speed)
    >>> property_diff(joris, joris.root.formation_jump_mc, 
    ...     'x', joris.root['_2_4_mc'].x)
    >>> property_diff(joris, joris.root['turn_mc'], 'currentLabel', 'white')
    >>> property_diff(joris, joris.root['extra_stone_gift_mc'], 'currentLabel', '_1')

    But Laurens cannot use it, because it is Ethan's turn

    Even if he tries to and move at 4, 2.
    >>> mouse_down_and_sleep(joris, joris.root.extra_stone_gift_mc.use_mc, 1.0 / joris._speed)
    >>> ## mouse_down_and_sleep(joris, joris.root._4_2_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._4_2_mc, 1.0 / joris._speed)

    Ethan moves at 6, 2
    >>> mouse_down_and_sleep(ethan, ethan.root._6_2_mc, 1.0 / ethan._speed)

    They both see Joris has taken only one extra turn.
    >>> joris.pb()
    ,,,,,,,,,
    ,,,,,,,,,
    ,,X,X,X,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,O,,,O,,
    ,,,,,,,,,
    ,,,,,,,,,
    >>> ethan.pb()
    ,,,,,,,,,
    ,,,,,,,,,
    ,,X,X,X,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,O,,,O,,
    ,,,,,,,,,
    ,,,,,,,,,
    '''
    
def setup_preview_capture_example():
    r"""
    setup board.  setting up board has no history, 
    so preview/revert is corrup.t
    >>> code_unit.inline_examples(
    ...         ethan_joris_start_example.__doc__,
    ...         locals(), globals(),
    ...         verify_examples = False)
    >>> preview_board_text = '''
    ... X,XXXO,O,
    ... ,XO,XXO,,
    ... ,OXXOOOO,
    ... /OXOO,,,O
    ... ,XOOO,O,O
    ... ,XXO,,OO,
    ... ,,XXO,,OX
    ... ,OX,O,OX,
    ... ,,,XOOOO,
    ... '''
    >>> from referee import text_to_array
    >>> from embassy import board_to_news, flash_to_text
    >>> preview_board = text_to_array(preview_board_text)
    >>> preview_news = board_to_news(preview_board, 
    ...     joris.intersection_mc_array, 'black')
    >>> joris.publish(preview_news)
    >>> ethan.publish(preview_news)
    >>> print flash_to_text(joris.intersection_mc_array)
    X,XXXO,O,
    ,XO,XXO,,
    ,OXXOOOO,
    /OXOO,,,O
    ,XOOO,O,O
    ,XXO,,OO,
    ,,XXO,,OX
    ,OX,O,OX,
    ,,,XOOOO,
    >>> print flash_to_text(ethan.intersection_mc_array)
    X,XXXO,O,
    ,XO,XXO,,
    ,OXXOOOO,
    /OXOO,,,O
    ,XOOO,O,O
    ,XXO,,OO,
    ,,XXO,,OX
    ,OX,O,OX,
    ,,,XOOOO,
    """
    
def preview_capture_example():
    r"""After preview capture and preview or move elsewhere, revert capture.
    setup board.
    >>> code_unit.inline_examples(
    ...         setup_preview_capture_example.__doc__,
    ...         locals(), globals(),
    ...         verify_examples = False)

    Joris previews capture at top right.
    >>> board_diff(joris, joris.root._0_6_mc,
    ...     'currentLabel', 'empty_black')
    >>> mouse_down_and_sleep(joris, joris.root._0_6_mc, 1.0 / joris._speed)

    Joris sees he would capture.
    >>> board_diff(joris, joris.root._0_6_mc,
    ...     'currentLabel', 'question_black')
    >>> if board_diff(joris, joris.root._0_5_mc,
    ...     'currentLabel', 'empty_black'):  joris.olds_list[-1]['_0_5_mc']

    Joris previews capture at top left.
    >>> mouse_down_and_sleep(joris, joris.root._2_0_mc, 1.0 / joris._speed)

    Joris sees the previous capture revert.
    >>> if board_diff(joris, joris.root._0_5_mc,
    ...     'currentLabel', 'white'):  joris.olds_list[-1]['_0_5_mc']

    preview another capture 3.  
    confirm other move 2 reverted.
    preview another move 4.
    confirm capture reverted 3.
    do another move 4.
    confirm capture 1, 2, 3 reverted.

        X,XXX@1O,
        ,X@3XXO,,
        2@XXOOOO,
        /@XOO,,,O
        ,XOOO,O,O
        ,XXO,,OO,
        ,,XXO,,OX
        ,OX4O,OX,
        ,,,XOOOO,


        
    """



def critical_example():
    '''?^_^  while i am surrounded and have a vital point, how can i feel alert and satisfied?
    >>> code_unit.inline_examples(
    ...     ethan_joris_start_example.__doc__, 
    ...     locals(), globals(), 
    ...     verify_examples = False)
    >>> wait = 3.0
    >>> mouse_down_and_sleep(joris, joris.root._7_0_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._7_0_mc, wait / joris._speed)
    >>> property_diff(joris, joris.root._7_0_mc.dragon_status_mc, 'currentLabel', 'none')
    >>> mouse_down_and_sleep(ethan, ethan.root._6_0_mc, wait / ethan._speed)
    >>> mouse_down_and_sleep(joris, joris.root._7_1_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._7_1_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._6_1_mc, wait / ethan._speed)
    >>> mouse_down_and_sleep(joris, joris.root._7_2_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._7_2_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._6_2_mc, wait / ethan._speed)
    >>> mouse_down_and_sleep(joris, joris.root._7_3_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._7_3_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._6_3_mc, wait / ethan._speed)
    >>> mouse_down_and_sleep(joris, joris.root._8_3_mc, wait / joris._speed)

    #- On preview joris sees status of his stones.
    #- >>> property_diff(joris, joris.root._8_3_mc.dragon_status_mc, 'currentLabel', 'white_attack')
    #- >>> property_diff(joris, joris.root._7_0_mc.dragon_status_mc, 'currentLabel', 'white_attack')
    
    #- >>> mouse_down_and_sleep(joris, joris.root._8_3_mc, wait / joris._speed)
    
    Joris does not see his dragon is about to be in critical condition.
    >>> property_diff(joris, joris.root._8_3_mc.dragon_status_mc, 'currentLabel', 'none')
    >>> property_diff(joris, joris.root._7_0_mc.dragon_status_mc, 'currentLabel', 'none')
    >>> mouse_down_and_sleep(ethan, ethan.root._7_4_mc, wait / ethan._speed)

    >>> joris.pb()
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    OOOO,,,,,
    XXXXO,,,,
    ,,,X,,,,,

        this is equivalent to:
        #>>> print exec_gtp(gtp_path, 'sgf/eye_critical_example.sgf', 'showboard')
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

    joris sees that his group is in critical condition.
    >>> property_diff(joris, joris.root._7_0_mc.dragon_status_mc, 'currentLabel', 'white_attack')
    >>> property_diff(joris, joris.root._8_3_mc.dragon_status_mc, 'currentLabel', 'white_attack')

    #- >>> property_diff(joris, joris.root._7_0_mc.dragon_status_mc, 'currentLabel', 'critical')

    #- joris sees attack at 8,1.
    #- >>> property_diff(joris, joris.root._8_1_mc.decoration_mc, 'currentLabel', 'white_attack')
    
    #+ joris sees red cross at 8,1.
    #+ >>> property_diff(joris, joris.root._8_1_mc.vital_point_mc, 'currentLabel', 'white_attack')
    
    joris previews 8,1.
    >>> mouse_down_and_sleep(joris, joris.root._8_1_mc, 1.0 / joris._speed)

    joris sees pink heart at 8,1.
    #+ >>> property_diff(joris, joris.root._8_1_mc.vital_point_mc, 'currentLabel', 'defended')

    he sees two candles, one candle at 8,0 and one at 8,2.
    #+ >>> property_diff(joris, joris.root._8_0_mc.eye_mc, 'currentLabel', 'black')
    #+ >>> property_diff(joris, joris.root._8_2_mc.eye_mc, 'currentLabel', 'black')

    #+ >>> joris.pb()
    #+ ,,,,,,,,,
    #+ ,,,,,,,,,
    #+ ,,,,,,,,,
    #+ ,,,,,,,,,
    #+ ,,,,,,,,,
    #+ ,,,,,,,,,
    #+ OOOO,,,,,
    #+ XXXXO,,,,
    #+ ,%,X,,,,,

    joris does not see any blocks on this living group.
    >>> property_diff(joris, joris.root._7_0_mc.block_north_mc, 'currentLabel', 'none')
    >>> property_diff(joris, joris.root._8_1_mc.vital_point_mc, 'currentLabel', 'none')

    joris confirms.
    >>> mouse_down_and_sleep(joris, joris.root._8_1_mc, 1.0 / joris._speed)
    >>> property_diff(joris, joris.root._7_0_mc.block_north_mc, 'currentLabel', 'none')
    >>> property_diff(joris, joris.root._8_1_mc.vital_point_mc, 'currentLabel', 'none')
   
    Ethan envelops, 
    >>> mouse_down_and_sleep(ethan, ethan.root._8_4_mc, 1.0 / ethan._speed)
    >>> joris.pb()
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    OOOO,,,,,
    XXXXO,,,,
    ,X,XO,,,,

    The group is no longer critical.
    >>> property_diff(joris, joris.root._8_1_mc.vital_point_mc, 'currentLabel', 'none')
    >>> property_diff(joris, joris.root._8_3_mc.dragon_status_mc, 'currentLabel', 'none')

    Yet since joris has two eyes, joris sees he is safe.
    >>> property_diff(joris, joris.root._8_3_mc.block_east_mc, 'currentLabel', 'none')
    '''



def preview_critical_example():
    '''After replay SGF, Joris sees a tiger chomp formation.
    >>> code_unit.inline_examples(
    ...     ethan_joris_start_example.__doc__, 
    ...     locals(), globals(), 
    ...     verify_examples = False)

    Joris can see territory, defend, attack.
    >>> wait = 2.0
    >>> time.sleep(wait / joris._speed)
    >>> property_diff(joris, joris.root.profit_mc, 'currentLabel', 'show')
    >>> property_diff(joris, joris.root.defend_mc, 'currentLabel', 'show')
    >>> property_diff(joris, joris.root.attack_mc, 'currentLabel', 'show')
    >>> from master import play_sgf
    >>> play_sgf('sgf/dead_5_5_critical_example.sgf', ethan, joris, mouse_down_and_sleep, wait)
    '''


def preview_critical_danger_example():
    '''If previewing stone is in danger, do not search for critical on neighbors.
    >>> code_unit.inline_examples(
    ...     ethan_joris_start_example.__doc__, 
    ...     locals(), globals(), 
    ...     verify_examples = False)
    >>> wait = 3.0
    >>> designer = joris
    >>> gnugo = ethan

    _5_5 board
    >>> mouse_down_and_sleep(joris, joris.root.game_over_mc._5_5_mc.enter_mc, wait / joris._speed)
    >>> property_diff(joris, joris.root, 'currentLabel', '_5_5')
    >>> property_diff(joris, joris.root.game_over_mc._5_5_mc.enter_mc, 'currentLabel', 'none')
    >>> property_diff(ethan, ethan.root, 'currentLabel', '_5_5')
    >>> property_diff(ethan, ethan.root.game_over_mc._5_5_mc.enter_mc, 'currentLabel', 'none')

    >>> mouse_down_and_sleep(joris, joris.root._1_1_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._1_1_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._2_2_mc, wait / ethan._speed)
    >>> mouse_down_and_sleep(joris, joris.root._1_3_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._1_3_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._2_1_mc, wait / ethan._speed)
    >>> mouse_down_and_sleep(joris, joris.root._1_2_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._2_3_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._2_3_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._3_3_mc, wait / ethan._speed)
    >>> mouse_down_and_sleep(joris, joris.root._2_0_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._2_0_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._3_0_mc, wait / ethan._speed)
    >>> mouse_down_and_sleep(joris, joris.root._1_0_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._1_2_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._1_2_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._1_0_mc, wait / ethan._speed)
    >>> mouse_down_and_sleep(joris, joris.root._3_4_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._3_4_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._4_1_mc, wait / ethan._speed)
    >>> mouse_down_and_sleep(joris, joris.root._4_3_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._3_2_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._3_2_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._4_3_mc, wait / ethan._speed)
    >>> mouse_down_and_sleep(joris, joris.root._4_2_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._4_4_mc, wait / joris._speed) 
    >>> joris.pb()
    ,,,,,
    OXXX,
    ,OOX,
    O,XOX
    ,O,O%
    >>> joris.root._4_3_mc.dragon_status_mc.currentLabel
    u'none'
    '''



def unconditional_status_example():
    '''?^_^    how can i see unconditionally alive stones?

    unconditional_status_mc
        none
        show

    _0_0_mc:
        unconditional_status_mc
            none
            black_alive
            black_dead
            white_alive
            white_dead
    above eye and suicide marks

    after preview or play:  
        if show_unconditional: unconditional_status of last stone.
        if not undecided:  get dragon_stones of last stone 
            and mark their unconditional_status_mc.

    loadsgf sgf/unconditional_status_example.sgf

    unconditional_status A3
    = alive

    dragon_stones A3
    = B5 B4 A3 B3 B2 B1
            
    unconditional_status A4
    = dead

    unconditional_status C3
    = undecided

    After replay SGF, Judith sees black stones are unconditionally alive.
    >>> code_unit.inline_examples(
    ...     ethan_joris_start_example.__doc__, 
    ...     locals(), globals(), 
    ...     verify_examples = False)
    >>> judith = joris

    Judith can see unconditional status.
    >>> wait = 2.0
    >>> time.sleep(wait / joris._speed)
    >>> property_diff(joris, joris.root.unconditional_status_mc, 'currentLabel', 'show')
    >>> from master import play_sgf
    >>> play_sgf('sgf/unconditional_status_example.sgf', ethan, joris, mouse_down_and_sleep, wait)

    Judith sees black stones are alive, a white is dead, and others are undecided.
    >>> property_diff(joris, joris.root._2_0_mc.unconditional_status_mc,
    ...     'currentLabel', 'black_alive')
    >>> property_diff(joris, joris.root._4_1_mc.unconditional_status_mc,
    ...     'currentLabel', 'black_alive')
    >>> property_diff(joris, joris.root._0_1_mc.unconditional_status_mc,
    ...     'currentLabel', 'black_alive')
    >>> property_diff(joris, joris.root._2_1_mc.unconditional_status_mc,
    ...     'currentLabel', 'black_alive')
    >>> property_diff(joris, joris.root._1_0_mc.unconditional_status_mc,
    ...     'currentLabel', 'white_dead')
    >>> property_diff(joris, joris.root._3_2_mc.unconditional_status_mc,
    ...     'currentLabel', 'none')

    Ethan does not see this.
    >>> property_diff(ethan, ethan.root._2_1_mc.unconditional_status_mc,
    ...     'currentLabel', 'none')
    >>> property_diff(ethan, ethan.root._1_0_mc.unconditional_status_mc,
    ...     'currentLabel', 'none')

    At each undecided stone, Judith sees no liberty warning.
    At the dead stone, she sees the liberty warning.
    >>> property_diff(joris, joris.root._1_1_mc.block_west_mc,
    ...     'currentLabel', 'none')
    >>> property_diff(joris, joris.root._1_0_mc.block_east_mc,
    ...     'currentLabel', 'white_danger')

    Judith extends invincible dragon.  She does not see liberty warning.
    >>> mouse_down_and_sleep(joris, joris.root._4_0_mc, 1.0 / joris._speed)
    >>> property_diff(joris, joris.root._4_0_mc.block_south_mc,
    ...     'currentLabel', 'none')
    >>> mouse_down_and_sleep(joris, joris.root._4_0_mc, 1.0 / joris._speed)
    >>> property_diff(joris, joris.root._4_0_mc.block_south_mc,
    ...     'currentLabel', 'none')
    '''



def tiger_chomp_sgf_example():
    '''After replay SGF, Joris sees a tiger chomp formation.
    >>> code_unit.inline_examples(
    ...     ethan_joris_start_example.__doc__, 
    ...     locals(), globals(), 
    ...     verify_examples = False)

    Joris can see territory, defend, attack.
    >>> wait = 2.0
    >>> time.sleep(wait / joris._speed)
    >>> property_diff(joris, joris.root.profit_mc, 'currentLabel', 'show')
    >>> property_diff(joris, joris.root.defend_mc, 'currentLabel', 'show')
    >>> property_diff(joris, joris.root.attack_mc, 'currentLabel', 'show')
    >>> from master import play_sgf
    >>> play_sgf('sgf/tiger_chomp_example.sgf', ethan, joris, mouse_down_and_sleep, wait)

    Joris sees a tiger chomp formation about his placed stone.
    >>> if property_diff(joris, joris.root.formation_tiger_chomp_mc.row_reflect_rotate_180_mc.response_mc, 'currentLabel', 'response'):
    ...     family_tree(joris.root.formation_tiger_chomp_mc)
    >>> property_diff(joris, joris.root.formation_tiger_chomp_mc, 
    ...     'x', joris.root['_1_3_mc'].x)
    >>> property_diff(joris, joris.root.formation_tiger_chomp_mc, 
    ...     'y', joris.root['_1_3_mc'].y)

    Because Joris' stone is in danger, 
    Joris does not see tiger chomp or tiger yawn.
    >>> from pprint import pprint
    >>> mouse_down_and_sleep(joris, joris.root._0_3_mc, 1.0 / joris._speed)
    >>> if property_diff(joris, joris.root.formation_tiger_chomp_mc.rotate_90_mc.response_mc, 'currentLabel', 'none'):
    ...     pprint(family_tree(joris.root.formation_tiger_chomp_mc.rotate_90_mc))
    >>> property_diff(joris, joris.root.formation_tiger_chomp_mc, 
    ...     'x', joris.root['_1_3_mc'].x)
    >>> property_diff(joris, joris.root.formation_tiger_chomp_mc, 
    ...     'y', joris.root['_1_3_mc'].y)

    Because Joris' stone is in danger, 
    Joris does not see tiger yawn.
    >>> mouse_down_and_sleep(joris, joris.root._0_1_mc, 1.0 / joris._speed)
    >>> if property_diff(joris, joris.root.formation_tiger_yawn_mc.row_reflect_rotate_90_mc.response_mc, 'currentLabel', 'none'):
    ...     pprint(family_tree(joris.root.formation_tiger_yawn_mc.rotate_90_mc))
    >>> joris.root['_2_2_mc'].y < joris.root.formation_tiger_yawn_mc.y
    True
    '''



def strike_example():
    '''
    >>> code_unit.inline_examples(
    ...     ethan_joris_start_example.__doc__, 
    ...     locals(), globals(), 
    ...     verify_examples = False)
    >>> wait = 4.0
    >>> joris_start = joris
    >>> ethan_start = ethan

    _5_5 board
    >>> mouse_down_and_sleep(joris, joris.root.game_over_mc._5_5_mc.enter_mc, wait / joris._speed)
    >>> property_diff(joris, joris.root, 'currentLabel', '_5_5')
    >>> property_diff(joris, joris.root.game_over_mc._5_5_mc.enter_mc, 'currentLabel', 'none')
    >>> property_diff(ethan, ethan.root, 'currentLabel', '_5_5')
    >>> property_diff(ethan, ethan.root.game_over_mc._5_5_mc.enter_mc, 'currentLabel', 'none')

    >>> mouse_down_and_sleep(joris_start, joris_start.root._0_2_mc, wait / joris_start._speed)
    >>> mouse_down_and_sleep(joris_start, joris_start.root._0_4_mc, wait / joris_start._speed)
    >>> mouse_down_and_sleep(joris_start, joris_start.root._2_4_mc, wait / joris_start._speed)
    >>> mouse_down_and_sleep(joris_start, joris_start.root._4_4_mc, wait / joris_start._speed)
    >>> mouse_down_and_sleep(joris_start, joris_start.root._2_4_mc, wait / joris_start._speed)
    >>> mouse_down_and_sleep(joris_start, joris_start.root._0_2_mc, wait / joris_start._speed)
    >>> mouse_down_and_sleep(joris_start, joris_start.root._4_0_mc, wait / joris_start._speed)
    >>> joris.root._0_2_strike_mc.north_mc.currentLabel
    u'none'
    >>> mouse_down_and_sleep(joris_start, joris_start.root._0_2_mc, wait / joris_start._speed)
    >>> mouse_down_and_sleep(joris_start, joris_start.root._0_2_mc, wait / joris_start._speed)
    >>> mouse_down_and_sleep(ethan_start, ethan_start.root._2_2_mc, wait / ethan_start._speed)
    >>> joris.root._0_2_strike_mc.north_mc.currentLabel == 'none'
    True
    >>> mouse_down_and_sleep(joris_start, joris_start.root._1_2_mc, wait / joris_start._speed)
    >>> mouse_down_and_sleep(joris_start, joris_start.root._0_0_mc, wait / joris_start._speed)
    >>> mouse_down_and_sleep(joris_start, joris_start.root._0_4_mc, wait / joris_start._speed)
    >>> joris.root._0_2_strike_mc.north_mc.currentLabel == 'none'
    True
    >>> joris.root._0_0_strike_mc.north_mc.currentLabel == 'none'
    True
    >>> joris.root._0_4_strike_mc.north_mc.currentLabel
    'black_warning_retaliate'
    >>> mouse_down_and_sleep(joris_start, joris_start.root._0_4_mc, wait / joris_start._speed)
    >>> mouse_down_and_sleep(ethan_start, ethan_start.root._1_3_mc, wait / ethan_start._speed)
    >>> mouse_down_and_sleep(joris_start, joris_start.root._0_3_mc, wait / joris_start._speed)
    >>> mouse_down_and_sleep(joris_start, joris_start.root._1_2_mc, wait / joris_start._speed)
    >>> joris.root._1_2_strike_mc.east_mc.currentLabel
    'black_notice_retaliate'
    >>> mouse_down_and_sleep(joris, joris.root.lobby_mc.enter_mc, wait)
    >>> joris.root._0_2_strike_mc.north_mc.currentLabel
    'none'
    >>> joris.root._1_2_strike_mc.east_mc.currentLabel == 'none'
    True
    '''

def draw_example():
    '''
    >>> code_unit.inline_examples(
    ...     ethan_joris_start_example.__doc__, 
    ...     locals(), globals(), 
    ...     verify_examples = False)
    >>> wait = 4.0
    >>> joris_start = joris
    >>> ethan_start = ethan

    _3_3 board
    >>> mouse_down_and_sleep(joris, joris.root.game_over_mc._3_3_mc.enter_mc, wait / joris._speed)
    >>> property_diff(joris, joris.root, 'currentLabel', '_3_3')
    >>> property_diff(joris, joris.root.game_over_mc._3_3_mc.enter_mc, 'currentLabel', 'none')
    >>> property_diff(ethan, ethan.root, 'currentLabel', '_3_3')
    >>> property_diff(ethan, ethan.root.game_over_mc._3_3_mc.enter_mc, 'currentLabel', 'none')

    No compensation.  Pass, pass, draw.
    >>> mouse_down_and_sleep(joris, joris.root.pass_mc, wait / joris._speed)
    >>> property_diff(joris, joris.root.pass_white_mc, 'currentLabel', 'black')
    >>> mouse_down_and_sleep(ethan, ethan.root.pass_mc, wait / ethan._speed)
    >>> property_diff(joris, joris.root.game_over_mc, 'currentLabel', 'draw')
    >>> property_diff(joris, joris.root.game_over_mc.score_mc.territory_txt, 'text', '0')
    >>> property_diff(ethan, ethan.root.game_over_mc, 'currentLabel', 'draw')
    >>> property_diff(ethan, ethan.root.game_over_mc.score_mc.territory_txt, 'text', '0')

    Game over.  passes reset.
    >>> property_diff(joris, joris.root.pass_mc, 'currentLabel', 'none')
    >>> property_diff(joris, joris.root.pass_white_mc, 'currentLabel', 'none')
    >>> property_diff(ethan, ethan.root.pass_mc, 'currentLabel', 'none')
    >>> property_diff(ethan, ethan.root.pass_white_mc, 'currentLabel', 'none')
    '''


def pass_win_example():
    '''Both players pass.  One wins.
    >>> code_unit.inline_examples(
    ...     ethan_joris_start_example.__doc__, 
    ...     locals(), globals(), 
    ...     verify_examples = False)
    >>> wait = 4.0 / joris._speed
    >>> joris_start = joris
    >>> ethan_start = ethan

    _3_3 board
    >>> mouse_down_and_sleep(joris, joris.root.game_over_mc._3_3_mc.enter_mc, wait)
    >>> property_diff(joris, joris.root, 'currentLabel', '_3_3')
    >>> property_diff(joris, joris.root.game_over_mc._3_3_mc.enter_mc, 'currentLabel', 'none')
    >>> property_diff(ethan, ethan.root, 'currentLabel', '_3_3')
    >>> property_diff(ethan, ethan.root.game_over_mc._3_3_mc.enter_mc, 'currentLabel', 'none')

    >>> mouse_down_and_sleep(joris_start, joris_start.root._1_1_mc, wait)
    >>> mouse_down_and_sleep(joris_start, joris_start.root._1_1_mc, wait)
    >>> mouse_down_and_sleep(ethan, ethan.root.pass_mc, wait)
    >>> mouse_down_and_sleep(joris_start, joris_start.root._0_1_mc, wait)
    >>> mouse_down_and_sleep(joris_start, joris_start.root._0_1_mc, wait)
    >>> property_diff(joris, joris.root.pass_mc, 'currentLabel', 'none')
    >>> property_diff(joris, joris.root.pass_white_mc, 'currentLabel', 'none')
    >>> mouse_down_and_sleep(ethan_start, ethan_start.root._0_0_mc, wait)

    Game not over until players consecutively pass.
    >>> mouse_down_and_sleep(joris, joris.root.pass_mc, wait)
    >>> property_diff(joris, joris.root.game_over_mc, 'currentLabel', 'none')
    >>> mouse_down_and_sleep(ethan_start, ethan_start.root._1_0_mc, wait)
    >>> mouse_down_and_sleep(joris_start, joris_start.root._2_1_mc, wait)
    >>> mouse_down_and_sleep(joris_start, joris_start.root._2_1_mc, wait)

    No compensation.  Pass, pass, win.
    >>> mouse_down_and_sleep(ethan, ethan.root.pass_mc, wait)
    >>> mouse_down_and_sleep(joris, joris.root.pass_mc, wait)
    >>> property_diff(joris, joris.root.game_over_mc, 'currentLabel', 'win')
    >>> property_diff(joris, joris.root.game_over_mc.score_mc.territory_txt, 'text', '8')
    >>> ethan.root.level_mc._txt.text
    '40'
    >>> joris.root.level_mc._txt.text
    '10'
    >>> joris.root.level_mc.progress_mc.currentLabel
    '_0'

    BOTH SEE EXIT TO LOBBY.
    >>> joris.root.game_over_mc.score_mc.lobby_mc.currentLabel
    'none'
    >>> property_diff(ethan, ethan.root.game_over_mc, 'currentLabel', 'lose')
    >>> property_diff(ethan, ethan.root.game_over_mc.score_mc.territory_txt, 'text', '-8')
    >>> ethan.root.game_over_mc.score_mc.lobby_mc.currentLabel
    'none'
    '''



def lose_example():
    '''
    >>> code_unit.inline_examples(
    ...     ethan_joris_start_example.__doc__, 
    ...     locals(), globals(), 
    ...     verify_examples = False)
    >>> wait = 4.0
    >>> joris_start = joris
    >>> ethan_start = ethan

    _3_3 board
    >>> mouse_down_and_sleep(joris, joris.root.game_over_mc._3_3_mc.enter_mc, wait / joris._speed)
    >>> property_diff(joris, joris.root, 'currentLabel', '_3_3')
    >>> property_diff(joris, joris.root.game_over_mc._3_3_mc.enter_mc, 'currentLabel', 'none')
    >>> property_diff(ethan, ethan.root, 'currentLabel', '_3_3')
    >>> property_diff(ethan, ethan.root.game_over_mc._3_3_mc.enter_mc, 'currentLabel', 'none')

    >>> mouse_down_and_sleep(joris_start, joris_start.root._0_0_mc, wait / joris_start._speed)
    >>> mouse_down_and_sleep(joris_start, joris_start.root._0_0_mc, wait / joris_start._speed)
    >>> mouse_down_and_sleep(ethan_start, ethan_start.root._1_1_mc, wait / ethan_start._speed)
    >>> mouse_down_and_sleep(joris_start, joris_start.root._0_1_mc, wait / joris_start._speed)
    >>> mouse_down_and_sleep(joris_start, joris_start.root._0_1_mc, wait / joris_start._speed)
    >>> mouse_down_and_sleep(ethan_start, ethan_start.root._1_0_mc, wait / ethan_start._speed)
    >>> mouse_down_and_sleep(joris_start, joris_start.root._0_2_mc, wait / joris_start._speed)
    >>> mouse_down_and_sleep(joris_start, joris_start.root._0_2_mc, wait / joris_start._speed)
    >>> mouse_down_and_sleep(ethan_start, ethan_start.root._1_2_mc, wait / ethan_start._speed)
    >>> joris.pb()
    ,,,
    OOO
    ,,,
    >>> ethan.pb()
    ,,,
    OOO
    ,,,

    No compensation.  Pass, pass, lose.
    >>> mouse_down_and_sleep(joris, joris.root.pass_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root.pass_mc, wait / joris._speed)
    >>> property_diff(joris, joris.root.game_over_mc, 'currentLabel', 'lose')
    >>> property_diff(joris, joris.root.game_over_mc.score_mc.territory_txt, 'text', '-9')
    >>> property_diff(ethan, ethan.root.game_over_mc, 'currentLabel', 'win')
    >>> property_diff(ethan, ethan.root.game_over_mc.score_mc.territory_txt, 'text', '9')
    '''


def computer_never_pass_example():
    '''3x3, computer does not pass.
    >>> code_unit.inline_examples(
    ...     ethan_joris_start_example.__doc__, 
    ...     locals(), globals(), 
    ...     verify_examples = False)

    >>> emmet = black
    >>> computer = white
    >>> wait = 4.0 / black._speed

    _3_3 board
    >>> mouse_down_and_sleep(black, black.root.game_over_mc._3_3_mc.enter_mc, wait)
    >>> property_diff(black, black.root, 'currentLabel', '_3_3')
    >>> property_diff(black, black.root.game_over_mc._3_3_mc.enter_mc, 'currentLabel', 'none')
    >>> property_diff(white, white.root, 'currentLabel', '_3_3')
    >>> property_diff(white, white.root.game_over_mc._3_3_mc.enter_mc, 'currentLabel', 'none')

    Computer never pass
    >>> mouse_down_and_sleep(black, black.root.game_over_mc.white_computer_mc.enter_mc, wait)
    >>> property_diff(black, black.root.game_over_mc.white_computer_mc, 'currentLabel', 'computer')
    >>> ## mouse_down_and_sleep(black, black.root.option_mc.computer_pass_mc.enter_mc, wait)
    >>> black.root.option_mc.computer_pass_mc.currentLabel
    u'none'
    >>> black.root.pass_white_mc.currentLabel
    u'none'
    >>> mouse_down_and_sleep(black, black.root._1_1_mc, wait)
    >>> black.pb()
    ,,,
    ,%,
    ,,,
    >>> mouse_down_and_sleep(black, black.root._1_1_mc, 4 * wait)

    Computer plays to some side.
    >>> black.root.pass_white_mc.currentLabel
    u'none'
    >>> from intersection_mc import any_label_equals
    >>> any_label_equals(black.intersection_mc_array, 'white')
    True
    '''


def computer_pass_example():
    '''
    >>> code_unit.inline_examples(
    ...     ethan_joris_start_example.__doc__, 
    ...     locals(), globals(), 
    ...     verify_examples = False)
    >>> emmet = joris
    >>> wait = 4.0 / black._speed

    _3_3 board
    >>> mouse_down_and_sleep(joris, joris.root.game_over_mc._3_3_mc.enter_mc, wait)
    >>> property_diff(joris, joris.root, 'currentLabel', '_3_3')
    >>> property_diff(joris, joris.root.game_over_mc._3_3_mc.enter_mc, 'currentLabel', 'none')
    >>> property_diff(ethan, ethan.root, 'currentLabel', '_3_3')
    >>> property_diff(ethan, ethan.root.game_over_mc._3_3_mc.enter_mc, 'currentLabel', 'none')

    Joris presses computer.
    >>> import go_text_protocol
    >>> setup_gtp = go_text_protocol.talk(gateway_process.gtp_envoy, 'set_random_seed 0')
    >>> mouse_down_and_sleep(joris, joris.root.game_over_mc.white_computer_mc.enter_mc, wait)
    >>> property_diff(joris, joris.root.game_over_mc.white_computer_mc, 'currentLabel', 'computer')


    passes reset.
    >>> mouse_down_and_sleep(black, black.root.option_mc.computer_pass_mc.enter_mc, wait)
    >>> black.root.option_mc.computer_pass_mc.currentLabel
    'show'
    >>> property_diff(joris, joris.root.pass_mc, 'currentLabel', 'none')
    >>> property_diff(joris, joris.root.pass_white_mc, 'currentLabel', 'none')
    >>> property_diff(ethan, ethan.root.pass_mc, 'currentLabel', 'none')
    >>> property_diff(ethan, ethan.root.pass_white_mc, 'currentLabel', 'none')

    >>> mouse_down_and_sleep(joris, joris.root._1_1_mc, wait)
    >>> mouse_down_and_sleep(joris, joris.root._1_1_mc, 2 * wait)
    >>> joris.pb()
    ,,,
    ,X,
    ,,,
    
    The computer passes.
    >>> property_diff(joris, joris.root.pass_mc, 'currentLabel', 'none')
    >>> property_diff(joris, joris.root.pass_white_mc, 'currentLabel', 'white')
    >>> property_diff(ethan, ethan.root.pass_mc, 'currentLabel', 'none')
    >>> property_diff(ethan, ethan.root.pass_white_mc, 'currentLabel', 'white')

    Joris moves.
    >>> mouse_down_and_sleep(joris, joris.root._0_1_mc, wait)
    >>> mouse_down_and_sleep(joris, joris.root._0_1_mc, wait)
    >>> joris.pb()
    ,X,
    ,X,
    ,,,
    '''


def user_pass_to_computer_example():
    '''Jade passes first.  Computer plays.
    >>> code_unit.inline_examples(
    ...     lukasz_begin_example.__doc__, 
    ...     locals(), globals(), 
    ...     verify_examples = False)
    >>> wait = 5.0 / black._speed
    >>> black.root.lobby_mc._00_mc.dominate_3_3_mc.dispatchEvent(mouseDown)
    >>> time.sleep(wait)
    >>> mouse_down_and_sleep(black, black.root.game_over_mc.start_mc, wait)
    >>> black.root.pass_mc.dispatchEvent(mouseDown)
    >>> time.sleep(wait)
    >>> from intersection_mc import any_label_equals
    >>> if not any_label_equals(black.intersection_mc_array, 'white'):
    ...     black.pb()
    '''


def ethan_jade_begin_example():
    '''Ethan creates a table and jade joins.  They start.
    Ethan enters the lobby and creates a multiplayer game.
    >>> gateway_process = configuration.subprocess_gateway(configuration.amf_host, 'embassy.py', configuration.verbose)

    >>> white = configuration.globe_class()
    >>> ethan = white

    Internet lag plus server lag is always less than three seconds.
    >>> wait = 4.0 / configuration.mock_speed
    >>> white.setup(configuration.mock_speed, configuration.setup_client)
    >>> set_property(white, white.root.title_mc.username_txt, 'text', 'ethan')
    >>> time.sleep(wait)
    >>> set_property(white, white.root.title_mc.password_txt, 'text', 'kennerly')
    >>> time.sleep(wait)

    #>>> mouse_down_and_sleep(white, white.root.title_mc.start_btn,
    #...     wait)
    >>> mouse_down_and_sleep(white, white.root.title_mc.start_btn, max(2, 2 * wait))

    Soon, he enters the lobby.
    >>> property_diff(white, white.root, 'currentLabel', 'lobby')

    jade logs in.
    >>> black = configuration.globe_class()
    >>> black = black
    >>> black.setup(configuration.mock_speed, configuration.setup_client)
    >>> black.root.title_mc.username_txt.text = 'jade'
    >>> time.sleep(2 * wait)
    >>> black.root.title_mc.password_txt.text = 'j'
    >>> time.sleep(wait)
    >>> mouse_down_and_sleep(black, black.root.title_mc.start_btn, max(3, 2 * wait))

    INT. TABLES WITH CAKES
    >>> property_diff(white, white.root, 'currentLabel', 'lobby')
    >>> property_diff(black, black.root, 'currentLabel', 'lobby')

    jade SEES NO COMMENT.
    >>> property_diff(black, black.root.comment_mc,
    ...     'currentLabel', 'none')
    '''


def ethan_jade_example():
    '''Ethan creates room.  Jade joins.  they start to play.  
    >>> code_unit.inline_examples(
    ...     ethan_jade_begin_example.__doc__, 
    ...     locals(), globals(), 
    ...     verify_examples = False)
    >>> lukasz = black
    >>> computer_lukasz = white
    >>> jade = black
    >>> ethan = white
    >>> wait = 4.0 / lukasz._speed

    >>> black.root.gateway_mc.currentLabel
    'none'

    Even after play single-player or not played, become observant.
    >>> jade.root.lobby_mc._00_mc.capture_3_3_mc.dispatchEvent(mouseDown)
    >>> time.sleep(wait)
    >>> jade.root.currentLabel
    '_3_3'
    >>> jade.root.tutor_mc.currentLabel
    'start'

    Jade toggles menu between open <--> close.
    >>> jade.root.menu_mc.toggle_mc.dispatchEvent(mouseDown)
    >>> time.sleep(wait)
    >>> jade.root.menu_mc.currentLabel
    'show'
    >>> jade.root.menu_mc.toggle_mc.dispatchEvent(mouseDown)
    >>> time.sleep(wait)
    >>> jade.root.menu_mc.currentLabel
    'none'
    >>> jade.root.menu_mc.toggle_mc.dispatchEvent(mouseDown)
    >>> time.sleep(wait)
    >>> jade.root.menu_mc.currentLabel
    'show'

    From menu, Jade goes to lobby.
    >>> jade.root.menu_mc.lobby_mc.dispatchEvent(mouseDown)
    >>> time.sleep(wait)
    >>> jade.root.menu_mc.currentLabel
    'none'
    >>> jade.root.currentLabel
    'lobby'
    >>> jade.root.menu_mc.lobby_mc.currentLabel
    'none'

    Jade no longer sees tutor comments.
    >>> jade.root.tutor_mc.currentLabel
    'none'

    Even after play single-player or not played, white becomes expert.
    >>> ethan.root.lobby_mc._00_mc.extra_stone_7_7_2_mc.dispatchEvent(mouseDown)
    >>> time.sleep(wait)
    >>> ethan.root.menu_mc.toggle_mc.dispatchEvent(mouseDown)
    >>> time.sleep(wait)
    >>> ethan.root.menu_mc.lobby_mc.dispatchEvent(mouseDown)
    >>> time.sleep(wait)

    >>> ethan.root.lobby_mc.main_mc.multiplayer_mc.dispatchEvent(mouseDown)
    >>> time.sleep(wait)
    >>> jade.root.lobby_mc.main_mc.multiplayer_mc.dispatchEvent(mouseDown)
    >>> time.sleep(wait)

    Without partner, Jade tries to create and change size and black handicap.
    The server continues running.  No game starts.
    >>> jade.root.lobby_mc.create_mc.dispatchEvent(mouseDown)
    >>> time.sleep(wait)
    >>> jade.root.game_over_mc._5_5_mc.enter_mc.dispatchEvent(mouseDown)
    >>> time.sleep(wait)
    >>> jade.root.game_over_mc.extra_stone_available_mc._4_mc.dispatchEvent(mouseDown)
    >>> time.sleep(wait)
    >>> jade.root.game_over_mc.start_mc.dispatchEvent(mouseDown)
    >>> time.sleep(wait)
    >>> jade.root.game_over_mc.currentLabel
    'setup'
    >>> time.sleep(wait)
    >>> jade.root.menu_mc.toggle_mc.dispatchEvent(mouseDown)
    >>> time.sleep(wait)
    >>> jade.root.menu_mc.lobby_mc.dispatchEvent(mouseDown)
    >>> time.sleep(wait)
   
    Ethan creates a room.
    >>> mouse_down_and_sleep(ethan, ethan.root.lobby_mc.create_mc,
    ...     wait)
    >>> mouse_down_and_sleep(jade, jade.root.lobby_mc.join_mc.enter_btn,
    ...     wait)
    >>> time.sleep(wait)

    Even after play single-player or not played, become observant.
    >>> jade.root.connected_mc.currentLabel
    'show'
    >>> jade.root.option_mc.block_mc.currentLabel
    'show'
    >>> jade.root.attack_mc.currentLabel
    'show'
    >>> jade.root.defend_mc.currentLabel
    'show'

    Jade sees we play for score
    >>> jade.root.option_mc.score_mc.currentLabel
    'show'
    >>> black.root.option_mc.first_capture_mc.currentLabel
    'none'

    Jade sees he is playing Ethan.
    >>> jade.root.turn_mc.black_user_txt.text
    'jade'
    >>> jade.root.turn_mc.white_user_txt.text
    'ethan'

    Level is 50 + (0 - KGS kyu).
    Ethan is about 10k on KGS so about level 40.
    20 / 4 equals about 5 stones handicap on 9x9.  -1 for first move.
    We have played close game at 4 stones handicap on 9x9.
    Jade is about 25-30 kyu worse.
    Jade is about level 10-15.
    Full help raises playing level about 8 (if less than level 20).
    Yet, beginners do not take full advantage of extra stones.

    Ethan sets four extra stones.
    >>> ethan.root.game_over_mc.extra_stone_available_mc._4_mc.dispatchEvent(mouseDown)
    >>> time.sleep(wait)

    Jade sees that black has four extra stones.
    >>> jade.root.game_over_mc.extra_stone_available_mc.currentLabel
    '_4'

    Ethan sets one hide.
    >>> ethan.root.game_over_mc.hide_available_mc._1_mc.dispatchEvent(mouseDown)
    >>> time.sleep(wait)

    Jade sees that black has four extra stones.
    >>> jade.root.game_over_mc.hide_available_mc.currentLabel
    '_1'

    Jade starts and sees score.
    >>> jade.root.game_over_mc.start_mc.dispatchEvent(mouseDown)
    >>> time.sleep(wait)
    >>> jade.root.score_mc.currentLabel
    'show'

    In this match, Jade may receive at most four extra stones.
    >>> jade.root.option_mc.extra_stone_available_mc.currentLabel
    '_4'

    In this match, Jade may receive at most one hide.
    >>> jade.root.option_mc.hide_available_mc.currentLabel
    '_1'

    Ethan plays white, expert, so does not see top move.
    >>> ethan.root.top_move_mc.currentLabel
    'none'
    >>> ethan.root.option_mc.empty_block_mc.currentLabel
    'none'
    >>> jade.root._2_2_mc.dispatchEvent(mouseDown)
    >>> time.sleep(wait)

    #Jade sees advice to attack and defend.
    #>>> jade.root.tutor_mc.currentLabel
    #'black_attack_defend'
    >>> jade.root._2_2_mc.dispatchEvent(mouseDown)
    >>> time.sleep(wait)
    >>> ethan.root._6_6_mc.dispatchEvent(mouseDown)
    >>> time.sleep(wait)
    
    >>> jade.root._2_4_mc.dispatchEvent(mouseDown)
    >>> time.sleep(wait)
    >>> jade.root._2_4_mc.dispatchEvent(mouseDown)
    >>> time.sleep(wait)
    >>> ethan.root._6_4_mc.dispatchEvent(mouseDown)
    >>> time.sleep(wait)

    #Jade sees advice to use extra stones early.
    #>>> jade.root.tutor_mc.currentLabel
    #'extra_stone'
    Jade sees advice to use hide.
    >>> jade.root.tutor_mc.currentLabel
    'hide'
    '''


def chat_example():
    '''Jade and Ethan login.  Jade says hello, which Ethan sees.
    >>> code_unit.inline_examples(
    ...     ethan_jade_begin_example.__doc__, 
    ...     locals(), globals(), 
    ...     verify_examples = False)
    >>> jade = black
    >>> ethan = white
    >>> wait = 4.0 / black._speed
    >>> black.root.comment_mc.currentLabel
    'none'
    >>> white.root.comment_mc.currentLabel
    'none'
    >>> black.root.chat_input_txt.text = 'hello'
    >>> time.sleep(wait)
    >>> black.root.chat_input_mc.dispatchEvent(mouseDown)
    >>> time.sleep(wait)
    >>> black.root.comment_mc.currentLabel
    'comment'
    >>> black.root.comment_mc._txt.text
    'jade: hello'
    >>> black.root.chat_input_txt.text
    ''
    >>> white.root.comment_mc.currentLabel
    'comment'
    >>> white.root.comment_mc._txt.text
    'jade: hello'
    '''


def start_multiplayer_example():
    '''Jade enters multiplayer table first.  Ethan follows.  Auto balance.
    >>> code_unit.inline_examples(
    ...     ethan_jade_begin_example.__doc__, 
    ...     locals(), globals(), 
    ...     verify_examples = False)
    >>> jade = black
    >>> ethan = white
    >>> wait = 4.0 / black._speed
    >>> sloth = 1.0 / black._speed

    jade is level 10.  ethan is level 40.  
    >>> jade.root.level_mc._txt.text
    '10'
    >>> ethan.root.level_mc._txt.text
    '40'

    jade go to multiplayer.  make.  try to start.  
    expect to remain.  expect tutor.  
    >>> jade.root.lobby_mc.main_mc.multiplayer_mc.dispatchEvent(mouseDown)
    >>> time.sleep(wait)
    >>> jade.root.lobby_mc.create_mc.dispatchEvent(mouseDown)
    >>> time.sleep(wait)
    >>> time.sleep(wait)
    >>> jade.root.game_over_mc.start_mc.dispatchEvent(mouseDown)
    >>> time.sleep(wait)
    >>> jade.root.game_over_mc.start_mc.dispatchEvent(mouseDown)
    >>> time.sleep(wait)

    ethan joins.  
    >>> ethan.root.lobby_mc.main_mc.multiplayer_mc.dispatchEvent(mouseDown)
    >>> time.sleep(wait)
    >>> ethan.root.lobby_mc.join_mc.enter_btn.dispatchEvent(mouseDown)
    >>> time.sleep(wait)
    
    jade is black.  ethan is white.  
    >>> from super_user import get_color
    >>> get_color(ethan)
    'white'
    >>> get_color(jade)
    'black'

    jade has 4 extra_stone_available.  ethan presses start.  jade is black.  ethan is white.  jade moves first.  jade gets extra stone.  ethan follows.  jade is observant.  ethan is expert.

    Jade and Ethan see that black has four extra stones.
    >>> jade.root.game_over_mc.extra_stone_available_mc.currentLabel
    '_4'
    >>> ethan.root.game_over_mc.extra_stone_available_mc.currentLabel
    '_4'

    Jade sees he is playing Ethan.
    >>> jade.root.turn_mc.black_user_txt.text
    'jade'
    >>> jade.root.turn_mc.white_user_txt.text
    'ethan'

    Ethan sees he is playing Jade.
    >>> ethan.root.turn_mc.black_user_txt.text
    'jade'
    >>> ethan.root.turn_mc.white_user_txt.text
    'ethan'

    Ethan presses start.
    >>> time.sleep(wait)
    >>> time.sleep(wait)
    >>> ethan.root.game_over_mc.start_mc.dispatchEvent(mouseDown)
    >>> time.sleep(wait)

    Even after play single-player or not played, become observant.
    >>> jade.root.connected_mc.currentLabel
    'show'
    >>> jade.root.option_mc.block_mc.currentLabel
    'show'
    >>> jade.root.attack_mc.currentLabel
    'show'
    >>> jade.root.defend_mc.currentLabel
    'show'

    Jade sees we play for score
    >>> jade.root.option_mc.score_mc.currentLabel
    'show'
    >>> black.root.option_mc.first_capture_mc.currentLabel
    'none'

    Ethan plays white, expert, so does not see top move.
    >>> ethan.root.top_move_mc.currentLabel
    'none'
    >>> ethan.root.option_mc.empty_block_mc.currentLabel
    'none'
    >>> jade.root._2_2_mc.dispatchEvent(mouseDown)
    >>> time.sleep(wait)

    Jade sees advice to attack and defend.
    >>> jade.root.tutor_mc.currentLabel
    'black_attack_defend'
    >>> jade.root._2_2_mc.dispatchEvent(mouseDown)
    >>> time.sleep(wait)
    >>> ethan.root._6_6_mc.dispatchEvent(mouseDown)
    >>> time.sleep(wait)
    
    Jade sees advice to use extra stones early.
    >>> jade.root.tutor_mc.currentLabel
    'extra_stone'

    quit game.
    >>> time.sleep(wait)
    >>> ethan.root.menu_mc.toggle_mc.dispatchEvent(mouseDown)
    >>> time.sleep(wait)
    >>> ethan.root.menu_mc.lobby_mc.dispatchEvent(mouseDown)
    >>> time.sleep(wait)

    ethan make game.
    need partner.
    >>> ethan.root.turn_mc.black_user_txt.text
    'RED'
    >>> ethan.root.lobby_mc.create_mc.dispatchEvent(mouseDown)
    >>> time.sleep(wait)
    >>> time.sleep(wait)
    >>> ethan.root.game_over_mc.start_mc.dispatchEvent(mouseDown)
    >>> time.sleep(wait)
    >>> ethan.root.game_over_mc.start_mc.dispatchEvent(mouseDown)
    >>> time.sleep(wait)
    >>> ethan.root.game_over_mc.currentLabel
    'setup'
    
    ethan joins.  
    >>> jade.root.lobby_mc.main_mc.multiplayer_mc.dispatchEvent(mouseDown)
    >>> time.sleep(wait)
    >>> jade.root.lobby_mc.join_mc.enter_btn.dispatchEvent(mouseDown)
    >>> time.sleep(wait)

    jade is black.  ethan is white.  
    >>> from super_user import get_color
    >>> get_color(ethan)
    'white'
    >>> get_color(jade)
    'black'

    jade has 4 extra_stone_available.  ethan presses start.  jade is black.  ethan is white.  jade moves first.  jade gets extra stone.  ethan follows.  jade is observant.  ethan is expert.

    Jade and Ethan see that black has four extra stones.
    >>> jade.root.game_over_mc.extra_stone_available_mc.currentLabel
    '_4'
    >>> ethan.root.game_over_mc.extra_stone_available_mc.currentLabel
    '_4'

    Jade sees he is playing Ethan.
    >>> jade.root.turn_mc.black_user_txt.text
    'jade'
    >>> jade.root.turn_mc.white_user_txt.text
    'ethan'

    Ethan sees he is playing Jade.
    >>> ethan.root.turn_mc.black_user_txt.text
    'jade'
    >>> ethan.root.turn_mc.white_user_txt.text
    'ethan'

    JADE presses start.
    >>> time.sleep(wait)
    >>> jade.root.game_over_mc.start_mc.dispatchEvent(mouseDown)
    >>> time.sleep(wait)

    Jade is observant, so sees attack and defend patterns.
    >>> jade.root.connected_mc.currentLabel
    'show'
    >>> jade.root.option_mc.block_mc.currentLabel
    'show'
    >>> jade.root.attack_mc.currentLabel
    'show'
    >>> jade.root.defend_mc.currentLabel
    'show'

    Jade sees we play for score
    >>> jade.root.option_mc.score_mc.currentLabel
    'show'
    >>> black.root.option_mc.first_capture_mc.currentLabel
    'none'

    Ethan plays white, expert, so does not see top move.
    >>> ethan.root.top_move_mc.currentLabel
    'none'
    >>> ethan.root.option_mc.empty_block_mc.currentLabel
    'none'
    >>> jade.root._2_2_mc.dispatchEvent(mouseDown)
    >>> time.sleep(wait)

    Jade sees advice to attack and defend.
    >>> jade.root.tutor_mc.currentLabel
    'black_attack_defend'
    >>> jade.root._2_2_mc.dispatchEvent(mouseDown)
    >>> time.sleep(wait)
    >>> ethan.root._6_6_mc.dispatchEvent(mouseDown)
    >>> time.sleep(wait)
    
    Jade sees advice to use extra stones early.
    >>> jade.root.tutor_mc.currentLabel
    'extra_stone'

    jade quits game.
    >>> time.sleep(wait)
    >>> jade.root.menu_mc.toggle_mc.dispatchEvent(mouseDown)
    >>> time.sleep(wait)
    >>> jade.root.menu_mc.lobby_mc.dispatchEvent(mouseDown)
    >>> time.sleep(wait)
    >>> time.sleep(wait)
    >>> jade.root.game_over_mc.start_mc.currentLabel
    'none'

    jade make game.
    need partner.
    >>> jade.root.turn_mc.black_user_txt.text
    'RED'
    >>> jade.root.lobby_mc.create_mc.dispatchEvent(mouseDown)
    >>> time.sleep(wait)
    >>> time.sleep(wait)
    >>> jade.root.turn_mc.black_user_txt.text
    'RED'
    >>> jade.root.turn_mc.white_user_txt.text
    'jade'

    Help says need partner.
    >>> jade.root.game_over_mc.currentLabel
    'setup'
    >>> jade.root.game_over_mc.start_mc.dispatchEvent(mouseDown)
    >>> time.sleep(wait)
    >>> jade.root.game_over_mc.start_mc.currentLabel
    'none'
    >>> jade.root.game_over_mc.start_mc.dispatchEvent(mouseDown)
    >>> time.sleep(wait)
    >>> jade.root.game_over_mc.currentLabel
    'setup'
    >>> jade.root.game_over_mc.start_mc.currentLabel
    'none'
    
    ethan joins.  
    >>> ethan.root.lobby_mc.main_mc.multiplayer_mc.dispatchEvent(mouseDown)
    >>> time.sleep(wait)
    >>> ethan.root.lobby_mc.join_mc.enter_btn.dispatchEvent(mouseDown)
    >>> time.sleep(wait)

    jade is black.  ethan is white.  
    >>> from super_user import get_color
    >>> get_color(ethan)
    'white'
    >>> get_color(jade)
    'black'
    >>> jade.root.game_over_mc.start_mc.currentLabel
    'none'
    >>> ethan.root.game_over_mc.start_mc.currentLabel
    'none'
    '''

def kyung_no_partner_example():
    r'''Kyung sees help to get partner until partner joins.
    Kyung tries to setup multiplayer without partner, and sees help.
    >>> kyung, moonhyoung, wait = setup_example(configuration, 
    ...     ('kyung', 'min'), ('moonhyoung', 'park') )
    >>> sloth = 0.25 / wait
    >>> kyung.root.lobby_mc.main_mc.multiplayer_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 5.575397)

    TODO: Log create multiplayer
    >>> kyung.root.lobby_mc.create_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 6.489086)

    Kyung has no partner yet and sees no setup options yet.
    >>> kyung.root.turn_mc.white_user_txt.text
    'kyung'
    >>> kyung.root.turn_mc.black_user_txt.text
    'BLACK'
    >>> kyung.root.game_over_mc.currentLabel
    'invite'
    >>> time.sleep(sloth * 1.314722)

    Moonhyoung joins.  Now Kyung can set and start.
    >>> moonhyoung.root.lobby_mc.join_mc.enter_btn.dispatchEvent(mouseDown)
    >>> time.sleep(wait)
    >>> kyung.root.game_over_mc.currentLabel
    'setup'
    >>> kyung.root.game_over_mc.extra_stone_available_mc._2_mc.dispatchEvent(mouseDown)
    >>> time.sleep(wait)
    >>> kyung.root.game_over_mc.extra_stone_available_mc.currentLabel
    '_2'
    >>> kyung.root.gateway_mc.currentLabel
    'none'
    >>> mouse_down_and_sleep(kyung, kyung.root.game_over_mc.start_mc, wait)
    >>> kyung.root.game_over_mc.currentLabel
    'none'
    '''

def moonhyoung_capture_5_5_example():
    '''Moonhyoung has one stone already on the board.
    >>> code_unit.inline_examples(
    ...     ethan_lukasz_begin_example.__doc__, 
    ...     locals(), globals(), 
    ...     verify_examples = False)
    >>> wait = 5.0 / black._speed
    >>> moonhyoung = black
    >>> computer_moonhyoung = white
    >>> sloth = 0.25 / wait
    >>> moonhyoung = moonhyoung
    >>> moonhyoung.root.lobby_mc._00_mc.capture_5_5_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 2.352143)
    >>> time.sleep(sloth * 6.992064)
    >>> moonhyoung.pb()
    ,,,,,
    ,,X,,
    ,,,,,
    ,,,,,
    ,,,,,
    >>> computer_moonhyoung.pb()
    ,,,,,
    ,,X,,
    ,,,,,
    ,,,,,
    ,,,,,

    For replay, computer is not playing.
    >>> moonhyoung.root.game_over_mc.white_computer_mc.enter_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth)
    >>> mouse_down_and_sleep(moonhyoung, moonhyoung.root.game_over_mc.start_mc, wait)
    >>> time.sleep(sloth * 3.157875)
    >>> moonhyoung.root._1_2_mc.currentLabel
    'black'
    >>> moonhyoung.root.turn_mc.currentLabel
    'black'
    >>> mouse_down_and_sleep(moonhyoung, moonhyoung.root._2_2_mc, wait)
    >>> time.sleep(sloth * 0.663549)
    >>> mouse_down_and_sleep(moonhyoung, moonhyoung.root._2_2_mc, wait)
    >>> moonhyoung.pb()
    ,,,,,
    ,,X,,
    ,,X,,
    ,,,,,
    ,,,,,
    >>> computer_moonhyoung.pb()
    ,,,,,
    ,,X,,
    ,,X,,
    ,,,,,
    ,,,,,

    GnuGo sees added stone.
    >>> import text
    >>> text.load('sgf/_update_gnugo.sgf').splitlines()[0]
    (;GM[1]SZ[5]AB[cb]
    >>> mouse_down_and_sleep(computer_moonhyoung, computer_moonhyoung.root._2_3_mc, wait)
    >>> time.sleep(sloth * 5.578328)
    >>> moonhyoung.pb()
    ,,,,,
    ,,X,,
    ,,XO,
    ,,,,,
    ,,,,,
    >>> computer_moonhyoung.pb()
    ,,,,,
    ,,X,,
    ,,XO,
    ,,,,,
    ,,,,,
    >>> mouse_down_and_sleep(moonhyoung, moonhyoung.root._4_4_mc, wait)
    >>> mouse_down_and_sleep(moonhyoung, moonhyoung.root._4_4_mc, wait)
    >>> # mouse_down_and_sleep(moonhyoung, moonhyoung.root._1_2_mc, wait)
    >>> # time.sleep(sloth * 0.709787)
    >>> # mouse_down_and_sleep(moonhyoung, moonhyoung.root._1_2_mc, wait)
    >>> mouse_down_and_sleep(computer_moonhyoung, computer_moonhyoung.root._3_2_mc, wait)
    >>> time.sleep(sloth * 18.043292)
    >>> mouse_down_and_sleep(moonhyoung, moonhyoung.root._1_3_mc, wait)
    >>> time.sleep(sloth * 3.221376)
    >>> mouse_down_and_sleep(moonhyoung, moonhyoung.root._1_3_mc, wait)
    >>> mouse_down_and_sleep(computer_moonhyoung, computer_moonhyoung.root._4_3_mc, wait)
    >>> time.sleep(sloth * 8.919906)
    >>> mouse_down_and_sleep(moonhyoung, moonhyoung.root._1_4_mc, wait)
    >>> time.sleep(sloth * 1.655395)
    >>> mouse_down_and_sleep(moonhyoung, moonhyoung.root._1_4_mc, wait)
    >>> mouse_down_and_sleep(computer_moonhyoung, computer_moonhyoung.root._2_1_mc, wait)
    >>> time.sleep(sloth * 2.707573)
    >>> mouse_down_and_sleep(moonhyoung, moonhyoung.root._1_1_mc, wait)
    >>> time.sleep(sloth * 2.421209)
    >>> mouse_down_and_sleep(moonhyoung, moonhyoung.root._1_1_mc, wait)
    >>> mouse_down_and_sleep(computer_moonhyoung, computer_moonhyoung.root._3_1_mc, wait)
    >>> time.sleep(sloth * 2.834998)
    >>> mouse_down_and_sleep(moonhyoung, moonhyoung.root._1_0_mc, wait)
    >>> time.sleep(sloth * 0.812281)
    >>> mouse_down_and_sleep(moonhyoung, moonhyoung.root._1_0_mc, wait)
    >>> mouse_down_and_sleep(computer_moonhyoung, computer_moonhyoung.root._2_4_mc, wait)
    >>> time.sleep(sloth * 9.281492)
    >>> mouse_down_and_sleep(moonhyoung, moonhyoung.root._4_2_mc, wait)
    >>> time.sleep(sloth * 1.567370)
    >>> mouse_down_and_sleep(moonhyoung, moonhyoung.root._4_2_mc, wait)
    >>> time.sleep(sloth * 7.295543)
    >>> mouse_down_and_sleep(moonhyoung, moonhyoung.root._4_0_mc, wait)
    >>> time.sleep(sloth * 1.856316)
    >>> mouse_down_and_sleep(moonhyoung, moonhyoung.root._4_0_mc, wait)
    >>> mouse_down_and_sleep(computer_moonhyoung, computer_moonhyoung.root._2_0_mc, wait)
    >>> time.sleep(sloth * 2.696289)
    >>> mouse_down_and_sleep(moonhyoung, moonhyoung.root._4_1_mc, wait)
    >>> time.sleep(sloth * 1.855492)
    >>> mouse_down_and_sleep(moonhyoung, moonhyoung.root._4_1_mc, wait)
    >>> mouse_down_and_sleep(computer_moonhyoung, computer_moonhyoung.root._4_2_mc, wait)
    >>> time.sleep(sloth * 3.082249)
    >>> mouse_down_and_sleep(moonhyoung, moonhyoung.root._3_0_mc, wait)
    >>> moonhyoung.root.menu_mc.toggle_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 5.061528)
    '''

def add_stone_example():
    '''Add several stones on board in a nearly finished 5x5 game.
    Expect to see connect, block, empty_block, territory, score.
    During preview, expect top_move_white.
    >>> code_unit.inline_examples(
    ...     ethan_lukasz_begin_example.__doc__, 
    ...     locals(), globals(), 
    ...     verify_examples = False)
    >>> wait = 5.0 / black._speed
    >>> moonhyoung = black
    >>> computer_moonhyoung = white
    >>> sloth = 0.25 / wait
    >>> moonhyoung = moonhyoung
    >>> moonhyoung.root.lobby_mc._07_mc.score_rule_territory_mc.dispatchEvent(mouseDown)
    >>> time.sleep(4 * wait)

    #For replay, computer is not playing.
    #>>> moonhyoung.root.game_over_mc.white_computer_mc.enter_mc.dispatchEvent(mouseDown)

    Board is setup.
    >>> moonhyoung.pb()
    ,,XXX
    XXXXX
    XXOOO
    XXO,O
    ,,,O,
    >>> computer_moonhyoung.pb()
    ,,XXX
    XXXXX
    XXOOO
    XXO,O
    ,,,O,

    Moonhyoung sees connect, block, empty_block, and territory.
    >>> moonhyoung.root._0_4_mc.black_shape_mc.currentLabel
    '_0011'
    >>> moonhyoung.root._4_3_mc.block_south_mc.currentLabel
    'white_block'
    >>> moonhyoung.root._4_2_mc.empty_block_north_mc.currentLabel
    'block'
    >>> moonhyoung.root._0_1_mc.empty_block_east_mc.currentLabel
    'you'

    Moonhyoung does not yet see score or territory.
    >>> moonhyoung.root._0_0_mc.territory_mc.currentLabel
    'neutral'
    >>> moonhyoung.root.score_mc.bar_mc.currentLabel
    '_0'
    
    >>> mouse_down_and_sleep(moonhyoung, moonhyoung.root.game_over_mc.start_mc, wait)
    >>> time.sleep(wait)
    >>> moonhyoung.root._1_2_mc.currentLabel
    'black'
    >>> moonhyoung.root.turn_mc.currentLabel
    'black'

    During preview, expect top_move_white unless nowhere to gain points.
    >>> moonhyoung.root.pass_white_mc.currentLabel
    'none'
    >>> mouse_down_and_sleep(moonhyoung, moonhyoung.root._4_2_mc, wait)
    >>> moonhyoung.pb()
    ,,XXX
    XXXXX
    XXOOO
    XXO,O
    ,,%O,

        Hack:  GnuGo sees added stone.
        >>> import text
        >>> print text.load('sgf/_update_gnugo.sgf').splitlines()[0] #doctest: +ELLIPSIS
        (;GM[1]SZ[5]AW...

    Territory and score require talking to GnuGo.
    >>> moonhyoung.root.territory_mc.currentLabel
    'show'
    >>> moonhyoung.root._0_0_mc.territory_mc.currentLabel
    'white'
    >>> moonhyoung.root.score_mc.bar_mc.currentLabel
    '_-25'
    >>> moonhyoung.root._4_1_mc.top_move_mc.currentLabel
    'white'
    >>> mouse_down_and_sleep(moonhyoung, moonhyoung.root._4_1_mc, wait)
    >>> moonhyoung.pb()
    ,,XXX
    XXXXX
    XXOOO
    XXO,O
    ,%,O,
    >>> moonhyoung.root._4_1_mc.top_move_mc.currentLabel
    'none'
    >>> moonhyoung.root._4_2_mc.top_move_mc.currentLabel
    'white'

    Territory and score require talking to GnuGo.
    >>> moonhyoung.root._0_0_mc.territory_mc.currentLabel
    'black'
    >>> moonhyoung.root.score_mc.bar_mc.currentLabel
    '_1'
    '''

def profit_example():
    '''Moonhyoung builds profitable castle.
    score_5_5_3.sgf
    >>> code_unit.inline_examples(
    ...     ethan_lukasz_begin_example.__doc__, 
    ...     locals(), globals(), 
    ...     verify_examples = False)
    >>> wait = 5.0 / black._speed
    >>> moonhyoung = black
    >>> sloth = 0.25 / wait
    >>> computer_moonhyoung = white
    >>> black.root.level_mc.none_mc.dispatchEvent(mouseDown)
    >>> time.sleep(wait)
    >>> black.root.comment_mc.none_mc.dispatchEvent(mouseDown)
    >>> time.sleep(wait)
    >>> black.root.lobby_mc.main_mc._07_mc.dispatchEvent(mouseDown)
    >>> time.sleep(wait)
    >>> black.root.lobby_mc._07_mc.score_5_5_3_mc.dispatchEvent(mouseDown)
    >>> time.sleep(wait)
    >>> time.sleep(wait)

    turn on profit option.
    expect profit option.
    >>> black.root.decoration_mc.currentLabel
    'show'
    >>> black.root.profit_mc.currentLabel
    'show'
    >>> mouse_down_and_sleep(black, black.root.game_over_mc.start_mc, wait)
    >>> time.sleep(wait)

    For replay, computer is not playing.
    >>> black.root.game_over_mc.white_computer_mc.enter_mc.dispatchEvent(mouseDown)

    preview 1,1
    Moonhyoung sees no double roof at 1,1.
    >>> black.root._1_1_mc.black_shape_mc.defend_mc.profit_mc.currentLabel
    'none'
    >>> mouse_down_and_sleep(black, black.root._1_1_mc, wait)
    >>> black.root.score_mc.bar_mc.marker_mc.change_txt.text
    '+5'
    >>> black.root._1_1_mc.black_shape_mc.defend_mc.profit_mc.currentLabel
    'none'

    Moonhyoung sees no double roof at 2,2.
    >>> black.root._2_2_mc.black_shape_mc.defend_mc.profit_mc.currentLabel
    'none'

    Moonhyoung previews center, 2,2.
    Moonhyoung sees profit of +24
    >>> mouse_down_and_sleep(black, black.root._2_2_mc, wait)
    >>> black.root.score_mc.bar_mc.marker_mc.change_txt.text
    '+24'

    Moonhyoung sees double roof at 2,2.
    >>> black.root._2_2_mc.black_shape_mc.defend_mc.profit_mc.currentLabel
    'show'

    play. Moonhyoung sees double roof at 2,2.
    >>> mouse_down_and_sleep(black, black.root._2_2_mc, wait)
    >>> black.root.score_mc.bar_mc.marker_mc.change_txt.text
    '+24'
    >>> black.root._2_2_mc.black_shape_mc.defend_mc.profit_mc.currentLabel
    'show'
    
    >>> mouse_down_and_sleep(white, white.root._2_1_mc, wait)
    >>> mouse_down_and_sleep(black, black.root._1_2_mc, wait)

    Fifteen is not enough for double roof.  +20 is minimum.
    >>> black.root.score_mc.bar_mc.marker_mc.change_txt.text
    '+15'
    >>> black.root._1_2_mc.black_shape_mc.defend_mc.profit_mc.currentLabel
    'none'

    Moonhyoung still sees double roof on previously profitable castle.
    >>> black.root._2_2_mc.black_shape_mc.defend_mc.profit_mc.currentLabel
    'show'

    Moonhyoung sees double roof.
    >>> mouse_down_and_sleep(black, black.root._1_1_mc, wait)
    >>> black.root.score_mc.bar_mc.marker_mc.change_txt.text
    '+33'
    >>> black.root._1_2_mc.black_shape_mc.defend_mc.profit_mc.currentLabel
    'none'
    >>> black.root._1_1_mc.black_shape_mc.defend_mc.profit_mc.currentLabel
    'show'
    >>> black.root._2_2_mc.black_shape_mc.defend_mc.profit_mc.currentLabel
    'show'
    
    Preview elsewhere.  Moonhyoung does not see previous double roof.
    >>> mouse_down_and_sleep(black, black.root._3_1_mc, wait)
    >>> black.root.score_mc.bar_mc.marker_mc.change_txt.text
    '+33'
    >>> black.root._1_1_mc.black_shape_mc.defend_mc.profit_mc.currentLabel
    'none'
    >>> black.root._3_1_mc.black_shape_mc.defend_mc.profit_mc.currentLabel
    'show'
    >>> black.root._2_2_mc.black_shape_mc.defend_mc.profit_mc.currentLabel
    'show'

    TODO:  Moonhyoung's castle is captured.  He no longer sees that double roof.
    '''
    
def kyung_no_partner_hack_example():
    r'''TODO:  Even if hacked client sends signal, server gracefully declines.
    Kyung tries to setup multiplayer without partner, and sees help.
    >>> kyung, moonhyoung, wait = setup_example(configuration, 
    ...     ('kyung', 'min'), ('moonhyoung', 'park') )
    >>> sloth = 0.25 / wait
    >>> kyung.root.lobby_mc.main_mc.multiplayer_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 5.575397)

    TODO: Log create multiplayer
    >>> kyung.root.lobby_mc.create_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 6.489086)

    Kyung has no partner yet.
    >>> kyung.root.turn_mc.white_user_txt.text
    'kyung'
    >>> kyung.root.turn_mc.black_user_txt.text
    'BLACK'
    >>> kyung.root.game_over_mc.mission_mc.currentLabel
    'none'
    >>> kyung.root.guide_mc.currentLabel
    'none'
    >>> time.sleep(sloth * 1.314722)
    >>> mouse_down_and_sleep(kyung, kyung.root.game_over_mc.start_mc, wait)
    >>> kyung.root.game_over_mc.currentLabel
    'setup'
    >>> kyung.root.guide_mc.currentLabel
    'invite'
    >>> kyung.root.gateway_mc.currentLabel
    'none'
    >>> kyung.root.guide_mc.none_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 0.896024)
    >>> kyung.root.guide_mc.currentLabel
    'none'
    >>> mouse_down_and_sleep(kyung, kyung.root.game_over_mc.start_mc, wait)
    >>> kyung.root.guide_mc.currentLabel
    'invite'
    >>> kyung.root.gateway_mc.currentLabel
    'none'
    >>> kyung.root.guide_mc.none_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 0.922507)
    >>> mouse_down_and_sleep(kyung, kyung.root.game_over_mc.start_mc, wait)
    >>> time.sleep(sloth * 1.008360)
    >>> mouse_down_and_sleep(kyung, kyung.root.game_over_mc.start_mc, wait)
    >>> time.sleep(sloth * 0.796300)
    >>> mouse_down_and_sleep(kyung, kyung.root.game_over_mc.start_mc, wait)
    >>> kyung.root.game_over_mc.extra_stone_available_mc._8_mc.dispatchEvent(mouseDown)
    >>> kyung.root.game_over_mc.extra_stone_available_mc.currentLabel
    '_8'
    >>> kyung.root.guide_mc.currentLabel
    'invite'
    >>> kyung.root.gateway_mc.currentLabel
    'none'
    >>> kyung.root.guide_mc.none_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 1.897131)
    >>> kyung.root.gateway_mc.none_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 2.022753)
    >>> time.sleep(sloth * 0.751284)
    >>> time.sleep(sloth * 1.082547)
    >>> time.sleep(sloth * 0.946084)
    >>> mouse_down_and_sleep(kyung, kyung.root.game_over_mc.start_mc, wait)
    >>> time.sleep(sloth * 0.636187)
    >>> mouse_down_and_sleep(kyung, kyung.root.game_over_mc.start_mc, wait)
    >>> time.sleep(sloth * 0.523897)
    >>> mouse_down_and_sleep(kyung, kyung.root.game_over_mc.start_mc, wait)
    >>> kyung.root.menu_mc.toggle_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 4.073157)

    Moonhyoung joins.  Now Kyung can set and start.
    >>> moonhyoung.root.lobby_mc.join_mc.enter_btn.dispatchEvent(mouseDown)
    >>> time.sleep(wait)
    >>> kyung.root.game_over_mc.extra_stone_available_mc._2_mc.dispatchEvent(mouseDown)
    >>> kyung.root.game_over_mc.extra_stone_available_mc.currentLabel
    '_2'
    >>> kyung.root.guide_mc.currentLabel
    'none'
    >>> kyung.root.gateway_mc.currentLabel
    'none'
    >>> mouse_down_and_sleep(kyung, kyung.root.game_over_mc.start_mc, wait)
    >>> kyung.root.game_over_mc.currentLabel
    'none'
    '''

def first_capture_example():
    '''First capture, again, again.  Win a series of tutorials.  
    >>> code_unit.inline_examples(
    ...     ethan_lukasz_begin_example.__doc__, 
    ...     locals(), globals(), 
    ...     verify_examples = False)
    >>> lukasz = black
    >>> computer_lukasz = white
    >>> sloth = 0.25 / black._speed 
    >>> # example.log level 20 at Sun Jul 18 20:05:59 2010

    Score bar and captures are neutral.
    >>> lukasz.root.score_mc.bar_mc.marker_mc.capture_mc.currentLabel
    '_0'
    >>> lukasz.root.score_mc.bar_mc.currentLabel
    '_0'
    >>> lukasz.root.lobby_mc.main_mc._00_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 13.308000)
    >>> lukasz.root.lobby_mc._00_mc.capture_3_3_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 7.726000)
    >>> time.sleep(sloth * 2.767000)

    For replay, computer is not playing.
    >>> lukasz.root.game_over_mc.white_computer_mc.enter_mc.dispatchEvent(mouseDown)
    >>> lukasz.root.score_mc.bar_mc.marker_mc.capture_mc.currentLabel
    '_0'
    >>> lukasz.root.score_mc.bar_mc.currentLabel
    '_0'
    >>> mouse_down_and_sleep(lukasz, lukasz.root.game_over_mc.start_mc, wait)
    >>> time.sleep(sloth * 3.294000)
    >>> mouse_down_and_sleep(lukasz, lukasz.root._1_1_mc, wait)
    >>> time.sleep(sloth * 2.249000)
    >>> mouse_down_and_sleep(lukasz, lukasz.root._1_1_mc, wait)
    >>> mouse_down_and_sleep(computer_lukasz, computer_lukasz.root._1_0_mc, wait)
    >>> time.sleep(sloth * 8.593000)
    >>> mouse_down_and_sleep(lukasz, lukasz.root._2_1_mc, wait)
    >>> time.sleep(sloth * 2.305000)
    >>> mouse_down_and_sleep(lukasz, lukasz.root._2_0_mc, wait)
    >>> time.sleep(sloth * 3.615000)
    >>> mouse_down_and_sleep(lukasz, lukasz.root._2_0_mc, wait)
    >>> time.sleep(sloth * 2.537000)
    >>> mouse_down_and_sleep(lukasz, lukasz.root._2_1_mc, wait)
    >>> time.sleep(sloth * 1.599000)
    >>> mouse_down_and_sleep(lukasz, lukasz.root._2_1_mc, wait)
    >>> mouse_down_and_sleep(computer_lukasz, computer_lukasz.root._0_1_mc, wait)
    >>> time.sleep(sloth * 3.001000)
    >>> mouse_down_and_sleep(lukasz, lukasz.root._0_2_mc, wait)
    >>> time.sleep(sloth * 4.100000)
    >>> mouse_down_and_sleep(lukasz, lukasz.root._0_2_mc, wait)
    >>> time.sleep(sloth * 2.814000)
    >>> mouse_down_and_sleep(lukasz, lukasz.root._1_2_mc, wait)
    >>> time.sleep(sloth * 1.753000)
    >>> mouse_down_and_sleep(lukasz, lukasz.root._1_2_mc, wait)
    >>> mouse_down_and_sleep(computer_lukasz, computer_lukasz.root._0_2_mc, wait)
    >>> time.sleep(sloth * 3.451000)
    >>> mouse_down_and_sleep(lukasz, lukasz.root._0_0_mc, wait)
    >>> time.sleep(sloth * 3.763000)
    >>> mouse_down_and_sleep(lukasz, lukasz.root._0_0_mc, wait)
    >>> mouse_down_and_sleep(computer_lukasz, computer_lukasz.root._0_2_mc, wait)
    >>> black.root.game_over_mc.currentLabel
    'win'
    >>> lukasz.root.menu_mc.lobby_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 6.152000)
    >>> lukasz.root.lobby_mc._00_mc.capture_3_3_2_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 3.741000)

    For replay, computer is not playing.
    >>> lukasz.root.game_over_mc.white_computer_mc.enter_mc.dispatchEvent(mouseDown)
    >>> lukasz.root.score_mc.bar_mc.marker_mc.capture_mc.currentLabel
    '_0'
    >>> lukasz.root.score_mc.bar_mc.currentLabel
    '_0'
    >>> time.sleep(sloth * 2.200000)
    >>> mouse_down_and_sleep(lukasz, lukasz.root.game_over_mc.start_mc, wait)
    >>> time.sleep(sloth * 2.469000)
    >>> mouse_down_and_sleep(lukasz, lukasz.root._1_1_mc, wait)
    >>> time.sleep(sloth * 2.461000)
    >>> mouse_down_and_sleep(lukasz, lukasz.root._1_1_mc, wait)
    >>> mouse_down_and_sleep(computer_lukasz, computer_lukasz.root._2_2_mc, wait)
    >>> time.sleep(sloth * 3.034000)
    >>> mouse_down_and_sleep(lukasz, lukasz.root._2_1_mc, wait)
    >>> time.sleep(sloth * 1.465000)
    >>> mouse_down_and_sleep(lukasz, lukasz.root._2_1_mc, wait)
    >>> mouse_down_and_sleep(computer_lukasz, computer_lukasz.root._0_2_mc, wait)
    >>> time.sleep(sloth * 1.803000)
    >>> black.pb()
    ,,O
    ,X,
    ,XO
    >>> mouse_down_and_sleep(lukasz, lukasz.root._1_2_mc, wait)
    >>> time.sleep(sloth * 1.601000)
    >>> mouse_down_and_sleep(lukasz, lukasz.root._1_2_mc, wait)
    >>> mouse_down_and_sleep(computer_lukasz, computer_lukasz.root._2_0_mc, wait)
    >>> black.pb()
    ,,O
    ,XX
    OX,
    >>> black.root.game_over_mc.currentLabel
    'win'
    >>> lukasz.root.menu_mc.lobby_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 12.098000)
    >>> lukasz.root.lobby_mc._00_mc.capture_3_3_2_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 3.158000)

    For replay, computer is not playing.
    >>> lukasz.root.game_over_mc.white_computer_mc.enter_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 2.037000)
    >>> mouse_down_and_sleep(lukasz, lukasz.root.game_over_mc.start_mc, wait)
    >>> time.sleep(sloth * 1.290000)
    >>> mouse_down_and_sleep(lukasz, lukasz.root._1_1_mc, wait)
    >>> time.sleep(sloth * 2.003000)
    >>> mouse_down_and_sleep(lukasz, lukasz.root._1_1_mc, wait)
    >>> mouse_down_and_sleep(computer_lukasz, computer_lukasz.root._1_0_mc, wait)
    >>> time.sleep(sloth * 2.435000)
    >>> mouse_down_and_sleep(lukasz, lukasz.root._2_1_mc, wait)
    >>> time.sleep(sloth * 1.656000)
    >>> mouse_down_and_sleep(lukasz, lukasz.root._2_0_mc, wait)
    >>> time.sleep(sloth * 1.802000)
    >>> mouse_down_and_sleep(lukasz, lukasz.root._2_0_mc, wait)
    >>> mouse_down_and_sleep(computer_lukasz, computer_lukasz.root._2_1_mc, wait)
    >>> black.root.game_over_mc.currentLabel
    'win'
    >>> lukasz.root.menu_mc.lobby_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 25.694000)
    >>> lukasz.root.lobby_mc._00_mc.capture_3_3_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 2.560000)

    For replay, computer is not playing.
    >>> lukasz.root.game_over_mc.white_computer_mc.enter_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 1.486000)
    >>> mouse_down_and_sleep(lukasz, lukasz.root.game_over_mc.start_mc, wait)
    >>> time.sleep(sloth * 1.023000)
    >>> mouse_down_and_sleep(lukasz, lukasz.root._1_1_mc, wait)
    >>> time.sleep(sloth * 1.375000)
    >>> mouse_down_and_sleep(lukasz, lukasz.root._1_1_mc, wait)
    >>> mouse_down_and_sleep(computer_lukasz, computer_lukasz.root._1_2_mc, wait)
    >>> time.sleep(sloth * 1.795000)
    >>> mouse_down_and_sleep(lukasz, lukasz.root._2_2_mc, wait)
    >>> time.sleep(sloth * 1.896000)
    >>> mouse_down_and_sleep(lukasz, lukasz.root._2_2_mc, wait)
    >>> mouse_down_and_sleep(computer_lukasz, computer_lukasz.root._2_1_mc, wait)
    >>> black.root.game_over_mc.currentLabel
    'win'
    >>> lukasz.root.menu_mc.lobby_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 30.864000)
    '''


def moonhyoung_kyung_revert_schedule_example():
    '''Moonhyoung and Kyung play each other.  Kyung sees helpful animation.
    >>> moonhyoung, kyung, wait = setup_example(configuration, 
    ...     ('moonhyoung', 'park'), ('kyung', 'min') )
    >>> moonhyoung_level = int(moonhyoung.root.level_mc._txt.text)
    >>> kyung_level = int(kyung.root.level_mc._txt.text)
    >>> if not kyung_level <= moonhyoung_level:
    ...     kyung_level, moonhyoung_level
    >>> sloth = 1.0 / wait

    While simulating random lag, and testing animation, force users to wait.
        time.sleep(max(wait, sloth * 5.036373))
    >>> moonhyoung.root.lobby_mc.main_mc.multiplayer_mc.dispatchEvent(mouseDown)
    >>> time.sleep(max(wait, sloth * 5.036373))
    >>> moonhyoung.root.lobby_mc.create_mc.dispatchEvent(mouseDown)
    >>> time.sleep(max(wait, sloth * wait))
    >>> kyung.root.lobby_mc.main_mc.multiplayer_mc.dispatchEvent(mouseDown)
    >>> time.sleep(max(wait, sloth * 6.383247))
    >>> kyung.root.lobby_mc.join_mc.enter_btn.dispatchEvent(mouseDown)
    >>> time.sleep(max(wait, sloth * 2.426745))
    >>> moonhyoung.root.game_over_mc.start_mc.dispatchEvent(mouseDown)
    >>> time.sleep(max(wait, sloth * 2.292854))
    >>> from super_user import get_color
    >>> get_color(kyung)
    'black'
    >>> get_color(moonhyoung)
    'white'

    Kyung builds base, top move.  Here is what Kyung sees.
    Each 0.25 seconds +/- 0.0625, Kyung sees an effect.
    >>> kyung.root._3_3_mc.dispatchEvent(mouseDown)

    He quickly clicks elsewhere.
    Kyung sees previous revert and does not see reverted scheduled event.
    [TODO:  python client updates autonomously]
    >>> time.sleep(0.25 * wait)
    >>> kyung.update(None)
    >>> kyung.root._4_4_mc.dispatchEvent(mouseDown)
    >>> time.sleep(0.25 * wait)
    >>> kyung.update(None)
    >>> kyung.root._1_1_mc.decoration_mc.currentLabel
    'none'
    >>> kyung.root._2_2_mc.decoration_mc.currentLabel
    'none'
    >>> time.sleep(wait)
    >>> kyung.update(None)
    >>> kyung.root._1_1_mc.decoration_mc.currentLabel
    'none'
    >>> kyung.root._2_2_mc.decoration_mc.currentLabel
    'black_defend'
    >>> time.sleep(wait)
    >>> kyung.update(None)
    >>> kyung.root._1_1_mc.decoration_mc.currentLabel
    'none'
    >>> kyung.root._2_2_mc.decoration_mc.currentLabel
    'black_defend'
    '''


def laurens_goto_lobby_example():
    '''Laurens exits from a simple problem.
    >>> laurens, wait = setup_example(configuration, 
    ...     ('laurens', 'groenewegen') )
    >>> sloth = 1.0 / wait

    >>> # example.log level 20 at Thu Aug 12 21:07:13 2010

    >>> laurens.root.level_mc.none_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 5.962000)
    >>> ## laurens.root.lobby_mc.main_mc._07_mc.dispatchEvent(mouseDown)
    >>> ## time.sleep(sloth * 30.802000)
    >>> ## laurens.root.lobby_mc._07_mc.main_mc.dispatchEvent(mouseDown)
    >>> ## time.sleep(sloth * 7.068000)
    >>> laurens.root.lobby_mc.main_mc._00_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 9.360000)
    >>> laurens.root.lobby_mc._00_mc.capture_rule_corner_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 8.016000)
    >>> laurens.root.menu_mc.toggle_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 9.481000)
    >>> laurens.root.menu_mc.lobby_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 2.418000)
    >>> laurens.root.gateway_mc.none_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 6.989000)
    >>> ## time.sleep(sloth * 52.051000)
    >>> laurens.root.level_mc.none_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 3.744000)
    >>> laurens.root.lobby_mc._00_mc.capture_rule_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 1.360000)
    >>> time.sleep(sloth * 3.689000)
    >>> mouse_down_and_sleep(laurens, laurens.root.game_over_mc.start_mc, wait)
    >>> time.sleep(sloth * 1.534000)
    >>> mouse_down_and_sleep(laurens, laurens.root._2_1_mc, wait)
    >>> time.sleep(sloth * 4.653000)
    >>> mouse_down_and_sleep(laurens, laurens.root._2_1_mc, wait)
    >>> laurens.root.menu_mc.lobby_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 4.695000)
    >>> laurens.root.gateway_mc.none_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 7.733000)
    >>> ## time.sleep(sloth * 22.652000)
    >>> laurens.root.level_mc.none_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 3.983000)
    '''

def marije_game_over_example():
    '''Ethan pretends to be Marije, wins, and presses OK to return to lobby.
    >>> marije, wait = setup_example(configuration, 
    ...     ('marije', 'vandodeweerd') )
    >>> sloth = 1.0 / wait
    >>> marije.root.level_mc.none_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 5.704000)
    >>> marije.root.comment_mc.none_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 1.645000)
    >>> marije.root.lobby_mc.main_mc._00_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 2.072000)
    >>> marije.root.lobby_mc._00_mc.capture_rule_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 2.788000)
    >>> time.sleep(sloth * 3.162000)
    >>> mouse_down_and_sleep(marije, marije.root.game_over_mc.start_mc, wait)
    >>> time.sleep(sloth * 2.328000)
    >>> mouse_down_and_sleep(marije, marije.root._2_1_mc, wait)
    >>> time.sleep(sloth * 12.843000)
    >>> mouse_down_and_sleep(marije, marije.root._2_1_mc, wait)
    >>> marije.root.game_over_mc.currentLabel
    'win'
    >>> marije.root.game_over_mc.score_mc.lobby_mc.dispatchEvent(mouseDown)
    >>> time.sleep(wait)
    >>> marije.root.currentLabel
    'lobby'
    >>> marije.root.menu_mc.currentLabel
    'none'
    >>> marije.root.game_over_mc.currentLabel
    'none'
    >>> marije.root._2_1_mc.currentLabel
    'empty_black'
    >>> marije.root._0_1_mc.currentLabel
    'empty_black'
    '''

def territory_dead_defend_example():
    '''Kyung tries to defend dead stones and does not see defend decoration.
    >>> kyung, wait = setup_example(configuration, 
    ...     ('kyung', 'min') )
    >>> sloth = 1.0 / kyung._speed
    >>> kyung.root.level_mc.none_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 3.252000)
    >>> kyung.root.lobby_mc.main_mc._14_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 3.665000)
    >>> kyung.root.lobby_mc._14_mc.territory_dead_defend_7_7_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 2.725000)
    >>> kyung.root.comment_mc.none_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 1.259000)
    >>> mouse_down_and_sleep(kyung, kyung.root.game_over_mc.start_mc, wait)
    >>> time.sleep(sloth * 5.217000)
    >>> mouse_down_and_sleep(kyung, kyung.root._1_5_mc, wait)

    Kyung does not see defend.
    >>> kyung.root._0_5_mc.decoration_mc.currentLabel
    'none'
    >>> kyung.root._1_5_mc.black_shape_mc.defend_mc.currentLabel
    'none'
    >>> time.sleep(sloth * 5.217000)

    Kyung cannot play there, because this problem railroads the solution.
    >>> mouse_down_and_sleep(kyung, kyung.root._3_6_mc, wait)
    >>> mouse_down_and_sleep(kyung, kyung.root._3_6_mc, wait)
    >>> kyung.root._3_6_mc.currentLabel
    'black'

    Kyung can play now.  After playing, he does not see defend.
    >>> mouse_down_and_sleep(kyung, kyung.root._1_5_mc, wait)
    >>> kyung.root._1_5_mc.currentLabel
    'question_black'
    >>> kyung.root._0_5_mc.decoration_mc.currentLabel
    'none'
    >>> kyung.root._1_5_mc.black_shape_mc.defend_mc.currentLabel
    'none'
    >>> mouse_down_and_sleep(kyung, kyung.root._1_5_mc, wait)
    >>> kyung.root._1_5_mc.currentLabel
    'black'
    >>> kyung.root._0_5_mc.decoration_mc.currentLabel
    'none'
    >>> kyung.root._1_5_mc.black_shape_mc.defend_mc.currentLabel
    'none'
    '''

def laurens_guard_example():
    '''Laurens guards corner, so does not see block or strike there.
        >>> code_unit.inline_examples(
        ...     lukasz_begin_example.__doc__, 
        ...     locals(), globals(), 
        ...     verify_examples = False)
        >>> wait = 4.0 / black._speed
        >>> sloth = 1.0 / black._speed
    
        >>> laurens = black

    >>> laurens.root.level_mc.none_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 2.881000)
    >>> laurens.root.comment_mc.none_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 3.644000)
    >>> laurens.root.lobby_mc.main_mc._00_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 5.620000)
    >>> laurens.root.lobby_mc._00_mc.capture_3_3_1_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 5.051000)
    >>> mouse_down_and_sleep(laurens, laurens.root.game_over_mc.start_mc, wait)
    >>> time.sleep(sloth * 7.612000)
    >>> laurens.root.comment_mc.none_mc.dispatchEvent(mouseDown)
    >>> time.sleep(wait)
    >>> laurens.root.comment_mc.currentLabel
    'none'

    Laurens captures and guards corner.  
    >>> laurens.root._1_2_mc.dispatchEvent(mouseDown)
    >>> time.sleep(wait)
    >>> laurens.root._2_2_mc.block_north_mc.currentLabel
    'white_danger'
    >>> laurens.root._2_2_strike_mc.north_mc.currentLabel
    'white_danger'
    >>> laurens.root._1_2_mc.dispatchEvent(mouseDown)
    >>> time.sleep(wait)
    >>> laurens.root._1_1_strike_mc.south_mc.currentLabel
    'none'
    >>> laurens.root._1_2_strike_mc.south_mc.currentLabel
    'none'
    >>> laurens.root._2_2_mc.block_north_mc.currentLabel
    'white_danger'
    >>> laurens.root._2_2_strike_mc.north_mc.currentLabel
    'white_danger'
    >>> laurens.root._2_1_mc.block_north_mc.currentLabel
    'white_danger'
    >>> laurens.root._2_1_strike_mc.north_mc.currentLabel
    'white_danger'

    After capture, Laurens sees no block or strike at corner.
    >>> laurens.root._2_0_mc.dispatchEvent(mouseDown)
    >>> time.sleep(wait)
    >>> laurens.root._2_0_strike_mc.south_mc.currentLabel
    'none'
    >>> laurens.root._2_0_mc.block_south_mc.currentLabel
    'none'
    >>> laurens.root._2_0_mc.dispatchEvent(mouseDown)
    >>> time.sleep(wait)
    >>> laurens.root._2_0_strike_mc.south_mc.currentLabel
    'none'
    >>> laurens.root._2_0_mc.block_south_mc.currentLabel
    'none'
    '''

def h1_pass_example():
    '''H1 passes.  Then white moves.  Then h1 moves.
        >>> code_unit.inline_examples(
        ...     ethan_lukasz_begin_example.__doc__, 
        ...     locals(), globals(), 
        ...     verify_examples = False)
        >>> wait = 4.0 / black._speed
        >>> sloth = 1.0 / black._speed
    
        >>> h1 = black
        >>> computer_h1 = white

    >>> # example.log level 20 at Sun Sep 05 13:11:02 2010

    >>> h1.root.level_mc.none_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 2.154000)
    >>> h1.root.lobby_mc.main_mc._04_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 4.115000)
    >>> h1.root.lobby_mc._04_mc.dominate_3_3_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 2.498000)

        For replay, computer is not playing.
        >>> h1.root.game_over_mc.white_computer_mc.enter_mc.dispatchEvent(mouseDown)
        >>> time.sleep(wait)

    >>> mouse_down_and_sleep(h1, h1.root.game_over_mc.start_mc, wait)
    >>> time.sleep(sloth * 9.258000)
    >>> h1.root.pass_mc.dispatchEvent(mouseDown)
    >>> time.sleep(wait)
    >>> h1.root.pass_mc.currentLabel
    'none'

    Computer cannot play.  Black must play.
    >>> mouse_down_and_sleep(computer_h1, computer_h1.root._0_2_mc, wait)
    >>> time.sleep(sloth * 7.450000)
    >>> h1.root.pass_mc.currentLabel
    'none'
    >>> mouse_down_and_sleep(h1, h1.root._1_1_mc, wait)
    >>> mouse_down_and_sleep(computer_h1, computer_h1.root._1_1_mc, wait)
    >>> mouse_down_and_sleep(h1, h1.root._1_1_mc, wait)

    H1 plays.
    >>> h1.pb()
    ,X,
    ,X,
    ,,,
    >>> mouse_down_and_sleep(computer_h1, computer_h1.root._1_1_mc, wait)
    >>> time.sleep(sloth * 4.529000)
    >>> mouse_down_and_sleep(computer_h1, computer_h1.root._0_2_mc, wait)
    >>> time.sleep(sloth * 4.529000)
    >>> h1.pb()
    ,XO
    ,X,
    ,,,
    >>> mouse_down_and_sleep(h1, h1.root._1_2_mc, wait)
    >>> time.sleep(sloth * 4.374000)
    >>> mouse_down_and_sleep(h1, h1.root._1_2_mc, wait)
    >>> mouse_down_and_sleep(computer_h1, computer_h1.root._2_1_mc, wait)
    >>> h1.root.menu_mc.toggle_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 6.121000)
    >>> h1.root.menu_mc.lobby_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 0.960000)
    >>> h1.root.lobby_mc._04_mc.dominate_3_3_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 2.083000)

        For replay, computer is not playing.
        >>> h1.root.game_over_mc.white_computer_mc.enter_mc.dispatchEvent(mouseDown)
        >>> time.sleep(wait)

    >>> time.sleep(sloth * 2.467000)
    >>> mouse_down_and_sleep(h1, h1.root.game_over_mc.start_mc, wait)
    >>> time.sleep(sloth * 9.512000)
    >>> mouse_down_and_sleep(h1, h1.root._1_1_mc, wait)
    >>> time.sleep(sloth * 3.835000)
    >>> h1.root.pass_mc.dispatchEvent(mouseDown)
    >>> mouse_down_and_sleep(computer_h1, computer_h1.root._2_1_mc, wait)
    >>> mouse_down_and_sleep(h1, h1.root._1_1_mc, wait)

    H1 plays.
    >>> h1.pb()
    ,X,
    ,%,
    ,,,
    >>> mouse_down_and_sleep(h1, h1.root._1_1_mc, wait)
    >>> mouse_down_and_sleep(computer_h1, computer_h1.root._2_1_mc, wait)
    >>> time.sleep(sloth * 3.412000)
    >>> mouse_down_and_sleep(h1, h1.root._1_2_mc, wait)
    >>> mouse_down_and_sleep(computer_h1, computer_h1.root._1_1_mc, wait)
    >>> mouse_down_and_sleep(h1, h1.root._1_2_mc, wait)
    >>> mouse_down_and_sleep(computer_h1, computer_h1.root._0_2_mc, wait)
    >>> time.sleep(sloth * 2.595000)
    >>> mouse_down_and_sleep(h1, h1.root._1_2_mc, wait)
    >>> mouse_down_and_sleep(computer_h1, computer_h1.root._0_0_mc, wait)
    '''

def h1_pass_computer_example():
    '''H1 passes.  Then he can play.
        >>> code_unit.inline_examples(
        ...     lukasz_begin_example.__doc__, 
        ...     locals(), globals(), 
        ...     verify_examples = False)
        >>> wait = 4.0 / black._speed
        >>> sloth = 1.0 / black._speed
    
        >>> h1 = black
    >>> # example.log level 20 at Mon Sep 06 07:43:01 2010

    >>> h1.root.level_mc.none_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 2.148000)
    >>> h1.root.comment_mc.none_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 1.354000)
    >>> h1.root.lobby_mc.main_mc._00_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 3.464000)
    >>> h1.root.lobby_mc._00_mc.capture_5_5_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 2.991000)
    >>> time.sleep(sloth * 2.515000)
    >>> mouse_down_and_sleep(h1, h1.root.game_over_mc.start_mc, wait)
    >>> time.sleep(sloth * 5.039000)
    >>> mouse_down_and_sleep(h1, h1.root._2_2_mc, wait)
    >>> time.sleep(sloth * 4.279000)
    >>> mouse_down_and_sleep(h1, h1.root._2_2_mc, wait)
    >>> time.sleep(sloth * 2.281000)
    >>> h1.root.pass_mc.dispatchEvent(mouseDown)
    >>> time.sleep(2 * wait)
    >>> h1.root.pass_mc.currentLabel
    'none'
    >>> h1.root.pass_white_mc.currentLabel
    'none'
    >>> h1.root.turn_mc.currentLabel
    'black'
    '''

def h1_see_computer_pass_example():
    '''Computer passes.  H1 sees prompt.  H1 passes and wins.
        >>> code_unit.inline_examples(
        ...     ethan_lukasz_begin_example.__doc__, 
        ...     locals(), globals(), 
        ...     verify_examples = False)
        >>> wait = 4.0 / black._speed
        >>> sloth = 1.0 / black._speed
    
        >>> h1 = black
        >>> computer_h1 = white
    >>> h1.root.lobby_mc._00_mc.main_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 41.053000)
    >>> h1.root.lobby_mc.main_mc._07_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 26.182000)
    >>> h1.root.lobby_mc._07_mc.score_rule_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 1.922000)
    >>> time.sleep(sloth * 3.018000)
    >>> mouse_down_and_sleep(h1, h1.root.game_over_mc.start_mc, wait)
    >>> time.sleep(sloth * 4.497000)
    >>> mouse_down_and_sleep(h1, h1.root._2_4_mc, wait)
    >>> time.sleep(sloth * 7.717000)
    >>> mouse_down_and_sleep(h1, h1.root._2_4_mc, wait)
    >>> mouse_down_and_sleep(computer_h1, computer_h1.root._2_0_mc, wait)
    >>> time.sleep(sloth * 17.679000)
    >>> mouse_down_and_sleep(h1, h1.root._0_1_mc, wait)
    >>> time.sleep(sloth * 6.812000)
    >>> mouse_down_and_sleep(h1, h1.root._0_1_mc, wait)
    >>> computer_h1.root.pass_mc.dispatchEvent(mouseDown)
    >>> time.sleep(wait)
    >>> h1.root.pass_white_mc.currentLabel
    'white'
    >>> h1.root.pass_mc.dispatchEvent(mouseDown)
    >>> time.sleep(wait)
    >>> h1.root.game_over_mc.currentLabel
    'win'
    '''


def moonhyoung_pass_example():
    '''Moonhyoung makes a bad move.
    Then he corrects.  Computer passes.  Moonhyoung passes and wins.
    >>> moonhyoung, wait = setup_example(configuration, 
    ...     ('moonhyoung', 'park') )
    >>> sloth = 1.0 / moonhyoung._speed
    >>> time.sleep(sloth * 0.903000)
    >>> moonhyoung.root.lobby_mc._07_mc.score_rule_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 5.474000)
    >>> mouse_down_and_sleep(moonhyoung, moonhyoung.root.game_over_mc.start_mc, wait)
    >>> time.sleep(sloth * 6.493000)
    >>> mouse_down_and_sleep(moonhyoung, moonhyoung.root._2_4_mc, wait)
    >>> time.sleep(sloth * 6.370000)
    >>> mouse_down_and_sleep(moonhyoung, moonhyoung.root._4_0_mc, wait)
    >>> moonhyoung.root.bad_move_mc.currentLabel
    'show'
    >>> mouse_down_and_sleep(moonhyoung, moonhyoung.root._0_1_mc, wait)
    >>> moonhyoung.root.bad_move_mc.currentLabel
    'none'
    >>> moonhyoung.root.pass_white_mc.currentLabel
    'white'
    >>> moonhyoung.root.pass_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 1.162000)
    >>> moonhyoung.root.pass_mc.currentLabel
    'none'
    >>> moonhyoung.root.pass_white_mc.currentLabel
    'none'
    >>> moonhyoung.root.game_over_mc.currentLabel
    'win'
    '''


def moonhyoung_no_preview_example():
    '''Moonhyoung clicks once, and thus builds a castle.
    >>> moonhyoung, wait = setup_example(configuration, 
    ...     ('moonhyoung', 'park') )
    >>> sloth = 1.0 / moonhyoung._speed
    >>> moonhyoung.root.comment_mc.none_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 2.105797)
    >>> moonhyoung.root.level_mc.none_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 2.202840)
    >>> moonhyoung.root.lobby_mc.main_mc._00_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 1.449365)
    >>> moonhyoung.root.lobby_mc._00_mc.capture_rule_side_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 2.552323)
    >>> moonhyoung.root.comment_mc.none_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 7.008736)
    >>> moonhyoung.root.menu_mc.toggle_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 2.352989)
    >>> mouse_down_and_sleep(moonhyoung, moonhyoung.root.game_over_mc.start_mc, wait)
    >>> time.sleep(sloth * 1.444695)
    >>> moonhyoung.root.preview_gift_mc.currentLabel
    '_0'
    >>> moonhyoung.root.preview_gift_mc.enabled_mc.currentLabel
    'none'
    >>> moonhyoung.root._0_2_mc.currentLabel
    'empty_black'
    >>> moonhyoung.root.game_over_mc.currentLabel
    'none'

    Moonhyoung makes a bad move.
    >>> mouse_down_and_sleep(moonhyoung, moonhyoung.root._0_2_mc, wait)
    >>> moonhyoung.root._0_2_mc.currentLabel
    'empty_black'
    >>> moonhyoung.root.game_over_mc.currentLabel
    'none'
    >>> moonhyoung.root.bad_move_mc.currentLabel
    'show'
    >>> moonhyoung.root.comment_mc.currentLabel
    'comment'
    >>> moonhyoung.root.comment_mc.none_mc.dispatchEvent(mouseDown)

    Moonhyoung makes a good move.
    >>> time.sleep(sloth * 1.444695)
    >>> moonhyoung.root._1_1_mc.dispatchEvent(mouseDown)
    >>> time.sleep(wait)

    TODO:  Reset bad move.
    >>> moonhyoung.root.bad_move_mc.currentLabel
    'none'
    >>> moonhyoung.root._1_1_mc.currentLabel
    'black'
    '''


def moonhyoung_no_preview_off_path_example():
    '''Moonhyoung tries to build at a bad place.
    >>> moonhyoung, wait = setup_example(configuration, 
    ...     ('moonhyoung', 'park') )
    >>> sloth = 1.0 / moonhyoung._speed
    >>> moonhyoung.root.lobby_mc._00_mc.capture_rule_beside_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 2.088000)
    >>> time.sleep(sloth * 5.234000)
    >>> mouse_down_and_sleep(moonhyoung, moonhyoung.root.game_over_mc.start_mc, wait)
    >>> time.sleep(sloth * 2.135000)
    >>> moonhyoung.root.bad_move_mc.currentLabel
    'none'
    >>> moonhyoung.root.turn_mc.currentLabel
    'black'
    >>> mouse_down_and_sleep(moonhyoung, moonhyoung.root._3_0_mc, wait)

    Moonhyoung sees it is bad and may try again.
    >>> moonhyoung.root.bad_move_mc.currentLabel
    'show'
    >>> moonhyoung.root.turn_mc.currentLabel
    'black'

    >>> mouse_down_and_sleep(moonhyoung, moonhyoung.root._3_4_mc, wait)

    Moonhyoung sees it is bad and may try again.
    >>> moonhyoung.root.bad_move_mc.currentLabel
    'show'
    >>> moonhyoung.root.turn_mc.currentLabel
    'black'

    >>> mouse_down_and_sleep(moonhyoung, moonhyoung.root._3_2_mc, wait)

    TODO:  turn off bad move
    >>> moonhyoung.root.bad_move_mc.currentLabel
    'none'
    >>> moonhyoung.pb()
    ,,,,,
    O,O,,
    ,OXO,
    ,XXX,
    O,,,,
    >>> moonhyoung.root.turn_mc.currentLabel
    'black'
    '''


def ethan_logout_multiplay_example():
    '''Ethan and a guest login.  Ethan creates table.  Ethan leaves table.
    Guest is playing.  Guest logs out.
    Ethan creates table.  Guest logs in and joins Ethan.
    >>> ethan, temporary, wait = setup_example(configuration, 
    ...     ('ethan', 'kennerly'), ('temporary', 'temporary') )
    >>> sloth = 1.0 / ethan._speed
    >>> ethan.root.lobby_mc.main_mc.multiplayer_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 26.832513)
    >>> ethan.root.comment_mc.none_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 3.238164)
    >>> ethan.root.lobby_mc.create_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 2.997478)
    >>> ## time.sleep(sloth * 14.340752)
    >>> temporary.root.lobby_mc.main_mc.multiplayer_mc.dispatchEvent(mouseDown)
    >>> ## time.sleep(sloth * 6.002138)
    >>> time.sleep(sloth * 1.610532)
    >>> temporary.root.lobby_mc.join_mc.enter_btn.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 5.414154)
    >>> mouse_down_and_sleep(temporary, temporary.root.game_over_mc.start_mc, wait)
    >>> time.sleep(sloth * 3.179143)
    >>> mouse_down_and_sleep(temporary, temporary.root._6_6_mc, wait)
    >>> time.sleep(sloth * 10.355483)
    >>> mouse_down_and_sleep(ethan, ethan.root._2_2_mc, wait)
    >>> time.sleep(sloth * 6.354349)
    >>> ## mouse_down_and_sleep(temporary, temporary.root._2_6_mc, wait)
    >>> ## time.sleep(sloth * 6.647674)
    >>> ## mouse_down_and_sleep(ethan, ethan.root._6_3_mc, wait)
    >>> ## time.sleep(sloth * 7.940063)
    >>> ## mouse_down_and_sleep(temporary, temporary.root._2_4_mc, wait)
    >>> ## time.sleep(sloth * 9.689568)
    >>> ## mouse_down_and_sleep(ethan, ethan.root._4_4_mc, wait)
    >>> ## time.sleep(sloth * 6.200956)
    >>> ## mouse_down_and_sleep(temporary, temporary.root._4_5_mc, wait)
    >>> ## time.sleep(sloth * 9.116793)
    >>> ## mouse_down_and_sleep(ethan, ethan.root._6_4_mc, wait)
    >>> ## time.sleep(sloth * 15.217465)
    >>> ## mouse_down_and_sleep(temporary, temporary.root._3_4_mc, wait)
    >>> ## time.sleep(sloth * 6.093496)
    >>> ## mouse_down_and_sleep(ethan, ethan.root._5_5_mc, wait)
    >>> ## time.sleep(sloth * 3.929122)
    >>> ## mouse_down_and_sleep(temporary, temporary.root._5_6_mc, wait)
    >>> ## time.sleep(sloth * 5.692831)
    >>> ## mouse_down_and_sleep(ethan, ethan.root._6_5_mc, wait)
    >>> ## time.sleep(sloth * 5.468522)
    >>> ## mouse_down_and_sleep(temporary, temporary.root._4_3_mc, wait)
    >>> ## time.sleep(sloth * 14.769076)
    >>> ## mouse_down_and_sleep(ethan, ethan.root._4_6_mc, wait)
    >>> ## time.sleep(sloth * 8.183984)
    >>> ## mouse_down_and_sleep(temporary, temporary.root._3_5_mc, wait)
    >>> ## time.sleep(sloth * 12.823467)
    >>> ## mouse_down_and_sleep(ethan, ethan.root._5_7_mc, wait)
    >>> ## time.sleep(sloth * 9.815428)
    >>> ## mouse_down_and_sleep(temporary, temporary.root._6_7_mc, wait)
    >>> ## time.sleep(sloth * 12.335597)
    >>> ## mouse_down_and_sleep(ethan, ethan.root._4_7_mc, wait)
    >>> ## time.sleep(sloth * 8.381025)
    >>> ## mouse_down_and_sleep(temporary, temporary.root._7_6_mc, wait)
    >>> ## time.sleep(sloth * 6.502854)
    >>> ## mouse_down_and_sleep(ethan, ethan.root._7_5_mc, wait)
    >>> ## time.sleep(sloth * 7.791504)
    >>> ## mouse_down_and_sleep(temporary, temporary.root._6_8_mc, wait)
    >>> ## time.sleep(sloth * 7.606397)
    >>> ## mouse_down_and_sleep(ethan, ethan.root._3_7_mc, wait)
    >>> ## time.sleep(sloth * 9.408840)
    >>> ## mouse_down_and_sleep(temporary, temporary.root._2_7_mc, wait)
    >>> ## time.sleep(sloth * 12.092830)
    >>> ## mouse_down_and_sleep(ethan, ethan.root._8_6_mc, wait)
    >>> ## time.sleep(sloth * 30.779214)
    >>> ## mouse_down_and_sleep(temporary, temporary.root._8_7_mc, wait)
    >>> ## time.sleep(sloth * 10.170053)
    >>> ## mouse_down_and_sleep(ethan, ethan.root._8_5_mc, wait)
    >>> ## time.sleep(sloth * 10.195549)
    >>> ## mouse_down_and_sleep(temporary, temporary.root._3_8_mc, wait)
    >>> ## time.sleep(sloth * 14.781752)
    >>> ## mouse_down_and_sleep(ethan, ethan.root._8_8_mc, wait)
    >>> ## time.sleep(sloth * 8.269844)
    >>> ## mouse_down_and_sleep(temporary, temporary.root._7_8_mc, wait)
    >>> ## time.sleep(sloth * 10.556374)
    >>> ## mouse_down_and_sleep(ethan, ethan.root._1_3_mc, wait)
    >>> ## time.sleep(sloth * 7.023006)
    >>> ## mouse_down_and_sleep(temporary, temporary.root._4_2_mc, wait)
    >>> ## time.sleep(sloth * 9.026236)
    >>> ## mouse_down_and_sleep(ethan, ethan.root._6_2_mc, wait)
    >>> ## time.sleep(sloth * 299.497687)
    >>> ## mouse_down_and_sleep(temporary, temporary.root._2_1_mc, wait)
    >>> ## time.sleep(sloth * 14.164251)
    >>> ## mouse_down_and_sleep(ethan, ethan.root._3_1_mc, wait)
    >>> temporary.root.menu_mc.toggle_mc.dispatchEvent(mouseDown)
    >>> ## time.sleep(sloth * 105.611128)
    >>> time.sleep(sloth * 5.611128)
    >>> temporary.root.menu_mc.lobby_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 0.996096)
    >>> temporary.root.lobby_mc._main_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 3.343760)
    >>> temporary.root.lobby_mc.main_mc._14_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 2.999500)
    >>> temporary.root.lobby_mc._14_mc.white_tiger_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 2.757897)
    >>> time.sleep(sloth * 5.108358)
    >>> mouse_down_and_sleep(temporary, temporary.root.game_over_mc.start_mc, wait)
    >>> time.sleep(sloth * 3.365509)
    >>> mouse_down_and_sleep(temporary, temporary.root._4_4_mc, wait)
    >>> ## mouse_down_and_sleep(computer_temporary, computer_temporary.root._6_4_mc, wait)
    >>> ## time.sleep(sloth * 16.162503)
    >>> ## mouse_down_and_sleep(temporary, temporary.root._5_5_mc, wait)
    >>> ## mouse_down_and_sleep(computer_temporary, computer_temporary.root._7_2_mc, wait)
    >>> ## time.sleep(sloth * 11.423917)
    >>> ## mouse_down_and_sleep(temporary, temporary.root._7_1_mc, wait)
    >>> ## mouse_down_and_sleep(computer_temporary, computer_temporary.root._7_6_mc, wait)
    >>> ## time.sleep(sloth * 11.804807)
    >>> ## mouse_down_and_sleep(temporary, temporary.root._7_7_mc, wait)
    >>> ## mouse_down_and_sleep(computer_temporary, computer_temporary.root._8_1_mc, wait)
    >>> ## time.sleep(sloth * 12.726909)
    >>> ## mouse_down_and_sleep(temporary, temporary.root._6_1_mc, wait)
    >>> ## mouse_down_and_sleep(computer_temporary, computer_temporary.root._8_7_mc, wait)
    >>> ## time.sleep(sloth * 13.433638)
    >>> ## mouse_down_and_sleep(temporary, temporary.root._6_7_mc, wait)
    >>> ## mouse_down_and_sleep(computer_temporary, computer_temporary.root._5_3_mc, wait)
    >>> ## time.sleep(sloth * 10.688326)
    >>> ## mouse_down_and_sleep(temporary, temporary.root._4_3_mc, wait)
    >>> ## mouse_down_and_sleep(computer_temporary, computer_temporary.root._7_8_mc, wait)
    >>> ## time.sleep(sloth * 11.228745)
    >>> ## mouse_down_and_sleep(temporary, temporary.root._6_8_mc, wait)
    >>> ## mouse_down_and_sleep(computer_temporary, computer_temporary.root._7_0_mc, wait)
    >>> ## time.sleep(sloth * 11.989811)
    >>> ## mouse_down_and_sleep(temporary, temporary.root._6_0_mc, wait)
    >>> ## mouse_down_and_sleep(computer_temporary, computer_temporary.root._8_6_mc, wait)
    >>> ## time.sleep(sloth * 15.206397)
    >>> ## mouse_down_and_sleep(temporary, temporary.root._8_0_mc, wait)
    >>> ## mouse_down_and_sleep(computer_temporary, computer_temporary.root._8_2_mc, wait)
    >>> ## time.sleep(sloth * 10.560039)
    >>> ## mouse_down_and_sleep(temporary, temporary.root._7_0_mc, wait)
    >>> ## mouse_down_and_sleep(computer_temporary, computer_temporary.root._8_8_mc, wait)
    >>> ## time.sleep(sloth * 14.736795)
    >>> ## mouse_down_and_sleep(temporary, temporary.root._6_3_mc, wait)
    >>> ## mouse_down_and_sleep(computer_temporary, computer_temporary.root._6_5_mc, wait)
    >>> ## time.sleep(sloth * 16740.630768)

    temporary logs out and in again.
    meanwhile ethan creates multiplayer room.
    >>> del temporary
    >>> time.sleep(sloth * 5.772722)
    >>> del ethan
    >>> time.sleep(sloth * 5.772722)
    >>> ethan, wait = setup_user(configuration, 'ethan', 'kennerly')

    >>> time.sleep(sloth * 5.400233)
    >>> ethan.root.menu_mc.toggle_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 25.624529)
    >>> ethan.root.menu_mc.lobby_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 1.905680)
    >>> ethan.root.lobby_mc.create_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 2.849155)

    >>> temporary, wait = setup_user(configuration, 'temporary', 'temporary')

    >>> ## time.sleep(sloth * 26.995807)
    >>> temporary.root.comment_mc.none_mc.dispatchEvent(mouseDown)
    >>> ## time.sleep(sloth * 48.306254)
    >>> temporary.root.menu_mc.toggle_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 3.035825)
    >>> temporary.root.menu_mc.lobby_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 1.794735)
    >>> temporary.root.lobby_mc._14_mc.main_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 5.807857)
    >>> temporary.root.lobby_mc.main_mc.multiplayer_mc.dispatchEvent(mouseDown)
    >>> ## time.sleep(sloth * 21.316657)
    >>> temporary.root.lobby_mc.join_mc.enter_btn.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 3.871197)
    >>> mouse_down_and_sleep(temporary, temporary.root.game_over_mc.start_mc, wait)
    >>> time.sleep(sloth * 2.807390)
    >>> mouse_down_and_sleep(temporary, temporary.root._2_6_mc, wait)
    >>> time.sleep(sloth * 6.159401)
    >>> mouse_down_and_sleep(ethan, ethan.root._2_2_mc, wait)
    >>> time.sleep(sloth * 9.254186)
    >>> ## mouse_down_and_sleep(temporary, temporary.root._6_6_mc, wait)
    >>> ## time.sleep(sloth * 8.968467)
    >>> ## mouse_down_and_sleep(ethan, ethan.root._5_3_mc, wait)
    >>> ## time.sleep(sloth * 6.600657)
    >>> ## mouse_down_and_sleep(temporary, temporary.root._2_4_mc, wait)
    >>> ## time.sleep(sloth * 9.019395)
    >>> ## mouse_down_and_sleep(ethan, ethan.root._5_5_mc, wait)
    >>> ## time.sleep(sloth * 5.866217)
    >>> ## mouse_down_and_sleep(temporary, temporary.root._5_6_mc, wait)
    >>> ## time.sleep(sloth * 11.003646)
    >>> ## mouse_down_and_sleep(ethan, ethan.root._3_5_mc, wait)
    >>> ## time.sleep(sloth * 5.212221)
    >>> ## mouse_down_and_sleep(temporary, temporary.root._2_5_mc, wait)
    >>> ## time.sleep(sloth * 8.550922)
    >>> ## mouse_down_and_sleep(ethan, ethan.root._3_6_mc, wait)
    >>> ## time.sleep(sloth * 20.131254)
    >>> ## mouse_down_and_sleep(temporary, temporary.root.extra_stone_gift_mc.use_mc, wait)
    >>> ## time.sleep(sloth * 5.297723)
    >>> ## mouse_down_and_sleep(temporary, temporary.root._3_3_mc, wait)
    >>> ## time.sleep(sloth * 6.185305)
    >>> ## mouse_down_and_sleep(temporary, temporary.root._4_2_mc, wait)
    >>> ## time.sleep(sloth * 13.034203)
    >>> ## mouse_down_and_sleep(ethan, ethan.root._3_4_mc, wait)
    >>> ## time.sleep(sloth * 12.319080)
    >>> ## mouse_down_and_sleep(temporary, temporary.root.extra_stone_gift_mc.use_mc, wait)
    >>> ## time.sleep(sloth * 1.754173)
    >>> ## mouse_down_and_sleep(temporary, temporary.root._3_7_mc, wait)
    >>> ## time.sleep(sloth * 9.112948)
    >>> ## mouse_down_and_sleep(temporary, temporary.root._4_4_mc, wait)
    '''

def robby_click_fast_example():
    '''Although Robby clicks quickly, he builds only once and 
    next stage retains no artifact from previous stage.
    >>> robby, wait = setup_example(configuration, 
    ...     ('temporary', 'temporary') )
    >>> sloth = 1.0 / robby._speed
    >>> robby.root.lobby_mc._00_mc.capture_corner_mc.dispatchEvent(mouseDown)
    >>> ## time.sleep(sloth * 7.170000)
    >>> time.sleep(sloth * 2.358000)
    >>> mouse_down_and_sleep(robby, robby.root.game_over_mc.start_mc, wait)
    >>> time.sleep(sloth * 2.485000)
    >>> mouse_down_and_sleep(robby, robby.root._1_1_mc, wait)
    >>> ## mouse_down_and_sleep(computer_robby, computer_robby.root._0_1_mc, wait)
    >>> time.sleep(sloth * 0.574000)
    >>> mouse_down_and_sleep(robby, robby.root._1_2_mc, wait)
    >>> ## mouse_down_and_sleep(computer_robby, computer_robby.root._1_0_mc, wait)

    Robby clicks again, before computer reply 
    has been safely received by the socket.
    Robby's fast click does not become a stone.
    >>> robby.root.cursor_mc.act_mc.currentLabel
    'busy'
    >>> time.sleep(sloth * 0.609000)
    >>> mouse_down_and_sleep(robby, robby.root._2_1_mc, wait)
    >>> robby.pb()
    OOO
    ,XX
    O,O

    Robby clicks again, before computer has finished?
    >>> time.sleep(sloth * 0.802000)
    >>> mouse_down_and_sleep(robby, robby.root._1_0_mc, wait)
    >>> robby.root.menu_mc.toggle_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 4.906000)
    >>> robby.root.cursor_mc.act_mc.currentLabel
    'busy'
    >>> robby.pb()
    OOO
    OXX
    O,O

    Robby receives news to turn on and off a white block.
    >>> from pprint import pprint
    >>> from master import find_in_receives_sequence
    >>> pprint(find_in_receives_sequence(robby.ambassador.receives, 
    ...     '_2_0_mc', 'block_south_mc'))
    [(4,
      {'text': u'30318'},
      {'currentLabel': u'white_warning'},
      ['title_mc', 'sequence']),
     (6,
      {'text': u'40071'},
      {'currentLabel': u'none'},
      ['sequence',
       '_1_0_mc',
       '_1_1_mc',
       '_0_1_mc',
       '_2_2_mc',
       'title_mc',
       '_2_0_mc',
       '_0_0_mc',
       '_2_1_mc',
       '_0_2_mc'])]

    #>>> robby.root.menu_mc.lobby_mc.dispatchEvent(mouseDown)
    #>>> time.sleep(sloth * 0.952000)
    #>>> robby.root.lobby_mc._00_mc.capture_3_3_1_mc.dispatchEvent(mouseDown)
    #>>> time.sleep(sloth * 4.036000)
    #>>> robby.root._1_1_mc.block_north_mc.currentLabel
    #'none'
    #>>> robby.root._1_1_mc.block_west_mc.currentLabel
    #'none'
    #>>> robby.root._0_0_mc.square_mc.currentLabel
    #'none'
    '''




def robby_no_artifact_example():
    '''Robby starts next level and sees no flames from previous level.
    >>> robby, wait = setup_example(configuration, 
    ...     ('temporary', 'temporary') )
    >>> sloth = 1.0 / robby._speed
    >>> robby.root.lobby_mc._00_mc.capture_3_3_1_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 5.829000)
    >>> ## time.sleep(sloth * 7.634000)
    >>> mouse_down_and_sleep(robby, robby.root.game_over_mc.start_mc, wait)
    >>> time.sleep(sloth * 2.063000)
    >>> mouse_down_and_sleep(robby, robby.root._1_1_mc, wait)
    >>> ## mouse_down_and_sleep(computer_robby, computer_robby.root._2_1_mc, wait)
    >>> time.sleep(sloth * 1.271000)
    >>> mouse_down_and_sleep(robby, robby.root._1_2_mc, wait)
    >>> ## mouse_down_and_sleep(computer_robby, computer_robby.root._1_0_mc, wait)
    >>> time.sleep(sloth * 1.249000)
    >>> mouse_down_and_sleep(robby, robby.root._1_0_mc, wait)

    TODO:  Robby cannot play twice in a row quickly.
    >>> time.sleep(sloth * 6.691000)
    >>> mouse_down_and_sleep(robby, robby.root._0_1_mc, wait)
    >>> ## mouse_down_and_sleep(computer_robby, computer_robby.root._0_0_mc, wait)

    TODO:  Robby cannot play twice in a row quickly.
    >>> time.sleep(sloth * 1.213000)
    >>> mouse_down_and_sleep(robby, robby.root._2_2_mc, wait)
    >>> time.sleep(sloth * 1.663000)
    >>> mouse_down_and_sleep(robby, robby.root._0_0_mc, wait)
    >>> time.sleep(sloth * 6.690000)
    >>> mouse_down_and_sleep(robby, robby.root._2_0_mc, wait)
    >>> robby.root.game_over_mc.score_mc.lobby_mc.dispatchEvent(mouseDown)
    >>> ## time.sleep(sloth * 10.465000)
    >>> time.sleep(sloth * 1.465000)
    >>> robby.root._1_1_mc.block_south_mc.currentLabel
    'none'
    >>> robby.root.lobby_mc._00_mc.capture_3_3_1_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 2.922000)
    >>> robby.root._1_1_mc.block_south_mc.currentLabel
    'none'
    >>> ## time.sleep(sloth * 22.530000)
    >>> mouse_down_and_sleep(robby, robby.root.game_over_mc.start_mc, wait)
    >>> robby.root._1_1_mc.block_south_mc.currentLabel
    'none'
    '''

def melvin_no_artifact_example():
    '''
>>> h4.root.lobby_mc._04_mc.dominate_rule_connect_mc.dispatchEvent(mouseDown)
>>> time.sleep(sloth * 4.091724)
>>> time.sleep(sloth * 18.497137)
>>> mouse_down_and_sleep(h4, h4.root.game_over_mc.start_mc, wait)
>>> time.sleep(sloth * 2.455879)
>>> mouse_down_and_sleep(h4, h4.root._1_1_mc, wait)
>>> mouse_down_and_sleep(computer_h4, computer_h4.root._2_2_mc, wait)
>>> h4.root.pass_mc.dispatchEvent(mouseDown)
>>> time.sleep(sloth * 12.933879)
>>> h4.root.pass_mc.dispatchEvent(mouseDown)
>>> mouse_down_and_sleep(computer_h4, computer_h4.root._2_0_mc, wait)
>>> time.sleep(sloth * 7.083976)
>>> mouse_down_and_sleep(h4, h4.root._0_2_mc, wait)
>>> mouse_down_and_sleep(computer_h4, computer_h4.root._2_2_mc, wait)
>>> time.sleep(sloth * 3.406987)
>>> mouse_down_and_sleep(h4, h4.root._0_0_mc, wait)
>>> mouse_down_and_sleep(computer_h4, computer_h4.root._2_0_mc, wait)
>>> time.sleep(sloth * 7.302439)
>>> mouse_down_and_sleep(h4, h4.root._1_2_mc, wait)
>>> computer_h4.root.pass_mc.dispatchEvent(mouseDown)
>>> time.sleep(sloth * 2.298039)
>>> mouse_down_and_sleep(h4, h4.root._1_0_mc, wait)
>>> time.sleep(sloth * 1.372560)
>>> mouse_down_and_sleep(h4, h4.root._1_0_mc, wait)
>>> h4.root.game_over_mc.score_mc.lobby_mc.dispatchEvent(mouseDown)
>>> time.sleep(sloth * 6.182780)
>>> h4.root.lobby_mc._04_mc.dominate_3_3_mc.dispatchEvent(mouseDown)
>>> time.sleep(sloth * 7.218691)
>>> time.sleep(sloth * 6.846458)
>>> mouse_down_and_sleep(h4, h4.root.game_over_mc.start_mc, wait)
>>> time.sleep(sloth * 1.960314)
>>> mouse_down_and_sleep(h4, h4.root._1_1_mc, wait)
>>> mouse_down_and_sleep(computer_h4, computer_h4.root._2_1_mc, wait)
>>> time.sleep(sloth * 6.562569)
>>> mouse_down_and_sleep(h4, h4.root._1_2_mc, wait)
>>> mouse_down_and_sleep(computer_h4, computer_h4.root._2_0_mc, wait)
>>> time.sleep(sloth * 6.975394)
>>> mouse_down_and_sleep(h4, h4.root._1_0_mc, wait)
>>> computer_h4.root.pass_mc.dispatchEvent(mouseDown)
>>> time.sleep(sloth * 5.080204)
>>> mouse_down_and_sleep(h4, h4.root._2_2_mc, wait)
>>> mouse_down_and_sleep(computer_h4, computer_h4.root._2_0_mc, wait)
>>> h4.root.pass_mc.dispatchEvent(mouseDown)
>>> time.sleep(sloth * 6.344079)
>>> h4.root.pass_mc.dispatchEvent(mouseDown)
>>> computer_h4.root.pass_mc.dispatchEvent(mouseDown)
>>> h4.root.game_over_mc.score_mc.lobby_mc.dispatchEvent(mouseDown)
>>> time.sleep(sloth * 6.047794)
>>> h4.root.lobby_mc._04_mc.dominate_rule_triple_mc.dispatchEvent(mouseDown)
>>> time.sleep(sloth * 5.390297)
>>> time.sleep(sloth * 9.670338)
>>> mouse_down_and_sleep(h4, h4.root.game_over_mc.start_mc, wait)
>>> time.sleep(sloth * 3.576770)
>>> mouse_down_and_sleep(h4, h4.root._0_0_mc, wait)
>>> time.sleep(sloth * 3.915742)
>>> mouse_down_and_sleep(h4, h4.root._1_2_mc, wait)
>>> computer_h4.root.pass_mc.dispatchEvent(mouseDown)
>>> h4.root.pass_mc.dispatchEvent(mouseDown)
>>> time.sleep(sloth * 6.792353)
>>> h4.root.pass_mc.dispatchEvent(mouseDown)
>>> h4.root.game_over_mc.score_mc.lobby_mc.dispatchEvent(mouseDown)
>>> time.sleep(sloth * 1.415312)
>>> h4.root.lobby_mc._04_mc.dominate_rule_connect_under_mc.dispatchEvent(mouseDown)
>>> time.sleep(sloth * 2.398307)
>>> time.sleep(sloth * 2.878827)
>>> mouse_down_and_sleep(h4, h4.root._2_0_mc, wait)
>>> time.sleep(sloth * 5.811599)
>>> mouse_down_and_sleep(h4, h4.root.game_over_mc.start_mc, wait)
>>> time.sleep(sloth * 3.350740)
>>> mouse_down_and_sleep(h4, h4.root._2_0_mc, wait)
>>> time.sleep(sloth * 1.978621)
>>> mouse_down_and_sleep(h4, h4.root._2_0_mc, wait)
>>> time.sleep(sloth * 5.496527)
>>> mouse_down_and_sleep(h4, h4.root._0_0_mc, wait)
>>> time.sleep(sloth * 3.697619)
>>> mouse_down_and_sleep(h4, h4.root._2_2_mc, wait)
>>> time.sleep(sloth * 1.535496)
>>> mouse_down_and_sleep(h4, h4.root._2_1_mc, wait)
>>> mouse_down_and_sleep(computer_h4, computer_h4.root._0_0_mc, wait)
>>> time.sleep(sloth * 9.103657)
>>> mouse_down_and_sleep(h4, h4.root._0_2_mc, wait)
>>> mouse_down_and_sleep(computer_h4, computer_h4.root._1_1_mc, wait)
>>> time.sleep(sloth * 9.406895)
>>> mouse_down_and_sleep(h4, h4.root._0_1_mc, wait)
>>> computer_h4.root.pass_mc.dispatchEvent(mouseDown)
>>> h4.root.pass_mc.dispatchEvent(mouseDown)
>>> time.sleep(sloth * 6.289980)
>>> h4.root.pass_mc.dispatchEvent(mouseDown)
>>> h4.root.game_over_mc.score_mc.lobby_mc.dispatchEvent(mouseDown)
>>> time.sleep(sloth * 2.385439)
>>> h4.root.lobby_mc._04_mc.dominate_3_3_mc.dispatchEvent(mouseDown)
>>> time.sleep(sloth * 2.859573)
>>> time.sleep(sloth * 10.881913)
>>> mouse_down_and_sleep(h4, h4.root.game_over_mc.start_mc, wait)
>>> time.sleep(sloth * 3.006018)
>>> mouse_down_and_sleep(h4, h4.root._1_1_mc, wait)
>>> mouse_down_and_sleep(computer_h4, computer_h4.root._1_2_mc, wait)
>>> time.sleep(sloth * 6.695237)
>>> mouse_down_and_sleep(h4, h4.root._0_2_mc, wait)
>>> mouse_down_and_sleep(computer_h4, computer_h4.root._1_0_mc, wait)
>>> time.sleep(sloth * 8.445967)
>>> mouse_down_and_sleep(h4, h4.root._0_0_mc, wait)
>>> time.sleep(sloth * 13.996227)
>>> mouse_down_and_sleep(h4, h4.root._2_0_mc, wait)
>>> mouse_down_and_sleep(computer_h4, computer_h4.root._2_1_mc, wait)
>>> time.sleep(sloth * 2.710612)
>>> mouse_down_and_sleep(h4, h4.root._2_2_mc, wait)
>>> computer_h4.root.pass_mc.dispatchEvent(mouseDown)
>>> h4.root.pass_mc.dispatchEvent(mouseDown)
>>> time.sleep(sloth * 5.012920)
>>> h4.root.pass_mc.dispatchEvent(mouseDown)
>>> h4.root.pass_mc.dispatchEvent(mouseDown)
>>> time.sleep(sloth * 1.232955)
>>> h4.root.pass_mc.dispatchEvent(mouseDown)
>>> h4.root.game_over_mc.score_mc.lobby_mc.dispatchEvent(mouseDown)
>>> time.sleep(sloth * 2.589473)
>>> h4.root.lobby_mc._04_mc.dominate_3_3_2_mc.dispatchEvent(mouseDown)
>>> time.sleep(sloth * 2.881688)
>>> time.sleep(sloth * 9.469538)
>>> mouse_down_and_sleep(h4, h4.root.game_over_mc.start_mc, wait)
>>> time.sleep(sloth * 4.071992)
>>> mouse_down_and_sleep(h4, h4.root._1_2_mc, wait)
>>> time.sleep(sloth * 2.386824)
>>> mouse_down_and_sleep(h4, h4.root._1_0_mc, wait)
>>> h4.root.pass_mc.dispatchEvent(mouseDown)
>>> time.sleep(sloth * 5.780014)
>>> h4.root.pass_mc.dispatchEvent(mouseDown)
>>> mouse_down_and_sleep(computer_h4, computer_h4.root._1_1_mc, wait)
>>> h4.root.pass_mc.dispatchEvent(mouseDown)
>>> time.sleep(sloth * 3.962485)
>>> h4.root.pass_mc.dispatchEvent(mouseDown)
>>> mouse_down_and_sleep(computer_h4, computer_h4.root._1_2_mc, wait)
>>> h4.root.comment_mc.none_mc.dispatchEvent(mouseDown)
>>> time.sleep(sloth * 2.462634)
>>> time.sleep(sloth * 3.540115)
>>> mouse_down_and_sleep(h4, h4.root._0_0_mc, wait)
>>> mouse_down_and_sleep(computer_h4, computer_h4.root._1_0_mc, wait)
>>> time.sleep(sloth * 2.648412)
>>> mouse_down_and_sleep(h4, h4.root._1_0_mc, wait)
>>> h4.root.pass_mc.dispatchEvent(mouseDown)
>>> time.sleep(sloth * 11.238823)
>>> h4.root.pass_mc.dispatchEvent(mouseDown)
>>> mouse_down_and_sleep(computer_h4, computer_h4.root._2_2_mc, wait)
>>> h4.root.menu_mc.toggle_mc.dispatchEvent(mouseDown)
>>> time.sleep(sloth * 3.433262)
    '''



def robby_pass_example():
    '''Robby can play after computer passes.  And can later pass.
        >>> code_unit.inline_examples(
        ...     ethan_lukasz_begin_example.__doc__, 
        ...     locals(), globals(), 
        ...     verify_examples = False)
        >>> wait = 4.0 / black._speed
    >>> sloth = 1.0 / black._speed
    >>> robby = black
    >>> computer_robby = white
    >>> robby.root.lobby_mc._04_mc.dominate_3_3_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 4.183000)
    >>> robby.root.game_over_mc.white_computer_mc.enter_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 3.262000)
    >>> mouse_down_and_sleep(robby, robby.root.game_over_mc.start_mc, wait)
    >>> mouse_down_and_sleep(robby, robby.root._1_1_mc, wait)
    >>> mouse_down_and_sleep(computer_robby, computer_robby.root._2_0_mc, wait)
    >>> robby.pb()
    ,X,
    ,X,
    O,,
    >>> mouse_down_and_sleep(robby, robby.root._2_1_mc, wait)
    >>> mouse_down_and_sleep(computer_robby, computer_robby.root._0_0_mc, wait)
    >>> robby.pb()
    OX,
    ,X,
    OX,
    >>> mouse_down_and_sleep(robby, robby.root._1_0_mc, wait)
    >>> mouse_down_and_sleep(computer_robby, computer_robby.root._2_2_mc, wait)
    >>> mouse_down_and_sleep(robby, robby.root._1_2_mc, wait)
    >>> robby.root.cursor_mc.act_mc.currentLabel
    'busy'
    >>> computer_robby.root.pass_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 4.010000)
    >>> robby.root.cursor_mc.act_mc.currentLabel
    'play'
    >>> robby.pb()
    ,X,
    XXX
    ,X,
    >>> computer_robby.root.pass_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 4.010000)
    >>> robby.root.game_over_mc.currentLabel
    'none'
    >>> robby.root.pass_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 6.010000)
    >>> robby.root.game_over_mc.currentLabel
    'win'
    >>> robby.root.comment_mc.none_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 8.938000)
    
    Flash client has error?
    '''

def robby_pass_2_example():
    '''
        >>> code_unit.inline_examples(
        ...     ethan_lukasz_begin_example.__doc__, 
        ...     locals(), globals(), 
        ...     verify_examples = False)
        >>> wait = 4.0 / black._speed
    >>> sloth = 1.0 / black._speed
    >>> robby = black
    >>> computer_robby = white
    >>> robby.root.lobby_mc.main_mc._04_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 3.497624)
    >>> robby.root.lobby_mc._04_mc.dominate_3_3_2_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 5.876726)
        >>> robby.root.game_over_mc.white_computer_mc.enter_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 2.898580)
    >>> mouse_down_and_sleep(robby, robby.root.game_over_mc.start_mc, wait)
    >>> time.sleep(sloth * 2.466570)
    >>> mouse_down_and_sleep(robby, robby.root._1_1_mc, wait)
    >>> mouse_down_and_sleep(computer_robby, computer_robby.root._1_0_mc, wait)
    >>> time.sleep(sloth * 4.268342)
    >>> mouse_down_and_sleep(robby, robby.root._0_1_mc, wait)
    >>> mouse_down_and_sleep(computer_robby, computer_robby.root._2_1_mc, wait)
    >>> time.sleep(sloth * 1.581185)
    >>> mouse_down_and_sleep(robby, robby.root._0_0_mc, wait)
    >>> mouse_down_and_sleep(computer_robby, computer_robby.root._2_2_mc, wait)
    >>> time.sleep(sloth * 4.596676)
    >>> mouse_down_and_sleep(robby, robby.root._2_0_mc, wait)
    >>> mouse_down_and_sleep(computer_robby, computer_robby.root._0_2_mc, wait)
    >>> time.sleep(sloth * 1.183214)
    >>> mouse_down_and_sleep(robby, robby.root._1_2_mc, wait)
    >>> mouse_down_and_sleep(computer_robby, computer_robby.root._2_1_mc, wait)
    >>> time.sleep(sloth * 1.622039)
    >>> robby.root.cursor_mc.act_mc.currentLabel
    'play'
    >>> mouse_down_and_sleep(robby, robby.root._2_2_mc, wait)
    >>> computer_robby.root.pass_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 1.622039)

    Computer passes.  Robby can play.
    >>> robby.root.cursor_mc.act_mc.currentLabel
    'play'
    '''
 
def jerry_pass_example():
    '''Jerry passes.  Computer plays.  Jerry can play.

    I noticed error in Python text client only when sequencing events.
    So configure to sequence events before creating clients.
    >>> import config
    >>> defaults = config.setup_defaults()
    >>> configuration = config.borg(defaults)
    >>> configuration.instant = False

        >>> code_unit.inline_examples(
        ...     ethan_lukasz_begin_example.__doc__, 
        ...     locals(), globals(), 
        ...     verify_examples = False)
        >>> wait = 4.0 / black._speed
    >>> sloth = 1.0 / black._speed
    >>> jerry = black
    >>> computer_jerry = white

    >>> # example.log level 20 at Thu Sep 23 12:49:50 2010
    >>> jerry.root.lobby_mc.main_mc._04_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 3.095000)
    >>> jerry.root.lobby_mc._04_mc.dominate_3_3_2_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 4.057000)
        >>> jerry.root.game_over_mc.white_computer_mc.enter_mc.dispatchEvent(mouseDown)
    >>> mouse_down_and_sleep(jerry, jerry.root.game_over_mc.start_mc, wait)
    >>> time.sleep(sloth * 5.291000)
    >>> mouse_down_and_sleep(jerry, jerry.root._1_1_mc, wait)
    >>> mouse_down_and_sleep(computer_jerry, computer_jerry.root._2_1_mc, wait)
    >>> time.sleep(sloth * 4.826000)
    >>> mouse_down_and_sleep(jerry, jerry.root._0_2_mc, wait)
    >>> mouse_down_and_sleep(computer_jerry, computer_jerry.root._1_0_mc, wait)
    >>> time.sleep(sloth * 2.370000)
    >>> mouse_down_and_sleep(jerry, jerry.root._1_2_mc, wait)
    >>> mouse_down_and_sleep(computer_jerry, computer_jerry.root._0_0_mc, wait)
    >>> jerry.root.pass_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 4.592000)
    >>> ## jerry.root.pass_mc.dispatchEvent(mouseDown)
    >>> import pdb; pdb.set_trace(); mouse_down_and_sleep(computer_jerry, computer_jerry.root._0_1_mc, wait)

    Computer plays.  jerry can play.
    >>> jerry.root.turn_mc.currentLabel
    'black'
    >>> jerry.root.cursor_mc.act_mc.currentLabel
    'play'
    >>> jerry.ambassador.receives[-5]
    >>> jerry.ambassador.receives[-4]
    >>> jerry.ambassador.receives[-3]
    >>> jerry.ambassador.receives[-2]
    >>> jerry.ambassador.receives[-1]
    >>> time.sleep(sloth * 4.592000)
    >>> jerry.root.turn_mc.currentLabel
    'black'
    >>> jerry.root.cursor_mc.act_mc.currentLabel
    'play'
    >>> time.sleep(sloth * 4.592000)
    >>> jerry.root.turn_mc.currentLabel
    'black'
    >>> jerry.root.cursor_mc.act_mc.currentLabel
    'play'
    '''

def jerry_pass_again_example():
    '''Jerry passes and passes.  Computer plays.  Jerry can play.

    I noticed error in Python text client only when sequencing events.
    So configure to sequence events before creating clients.
    >>> import config
    >>> defaults = config.setup_defaults()
    >>> configuration = config.borg(defaults)
    >>> configuration.instant = False

        >>> code_unit.inline_examples(
        ...     ethan_lukasz_begin_example.__doc__, 
        ...     locals(), globals(), 
        ...     verify_examples = False)
        >>> wait = 4.0 / black._speed
    >>> sloth = 1.0 / black._speed
    >>> jerry = black
    >>> computer_jerry = white

    >>> # example.log level 20 at Thu Sep 23 12:49:50 2010
    >>> jerry.root.lobby_mc.main_mc._04_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 3.095000)
    >>> jerry.root.lobby_mc._04_mc.dominate_3_3_2_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 4.057000)
    >>> mouse_down_and_sleep(jerry, jerry.root.game_over_mc.start_mc, wait)
    >>> time.sleep(sloth * 5.291000)
    >>> mouse_down_and_sleep(jerry, jerry.root._1_1_mc, wait)
    >>> time.sleep(sloth * 5.291000)
    >>> jerry.root.turn_mc.currentLabel
    'black'
    >>> jerry.root.cursor_mc.act_mc.currentLabel
    'play'
    >>> jerry.root.pass_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 5.291000)
    >>> jerry.root.turn_mc.currentLabel
    'black'
    >>> jerry.root.cursor_mc.act_mc.currentLabel
    'play'
    >>> jerry.root.pass_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 5.291000)
    >>> jerry.root.turn_mc.currentLabel
    'black'
    >>> jerry.root.cursor_mc.act_mc.currentLabel
    'play'
    >>> jerry.root.pass_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 5.291000)
    >>> jerry.root.turn_mc.currentLabel
    'black'
    >>> jerry.root.cursor_mc.act_mc.currentLabel
    'play'
    '''

def robby_click_stone_example():
    '''Robby clicks stone.  He can still build.
        >>> code_unit.inline_examples(
        ...     ethan_lukasz_begin_example.__doc__, 
        ...     locals(), globals(), 
        ...     verify_examples = False)
        >>> wait = 4.0 / black._speed
        >>> sloth = 1.0 / wait
    >>> # example.log level 20 at Mon Sep 20 12:12:01 2010

    >>> black.root.level_mc.none_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 10.624000)
    >>> black.root.lobby_mc.main_mc._00_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 4.609000)
    >>> black.root.comment_mc.none_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 4.365000)
    >>> black.root.lobby_mc._00_mc.capture_3_3_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 2.791000)
    >>> mouse_down_and_sleep(black, black.root.game_over_mc.start_mc, wait)
    >>> time.sleep(sloth * 3.356000)
    >>> black.root.cursor_mc.act_mc.currentLabel
    'play'
    >>> mouse_down_and_sleep(black, black.root._2_2_mc, wait)
    >>> black.root.cursor_mc.act_mc.currentLabel
    'play'
    >>> mouse_down_and_sleep(black, black.root._1_2_mc, wait)
    >>> black.pb()
    ,,,
    ,XX
    ,OO
    '''

def robby_would_be_surrounded_example():
    '''Robby plays into danger, yet can try again.
        >>> code_unit.inline_examples(
        ...     ethan_lukasz_begin_example.__doc__, 
        ...     locals(), globals(), 
        ...     verify_examples = False)
        >>> wait = 4.0 / black._speed
        >>> sloth = 1.0 / wait
        >>> robby = black
        >>> computer_robby = white
    >>> robby.root.lobby_mc._10_mc.attack_defend_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 5.315000)
    >>> time.sleep(sloth * 2.757000)
    >>> mouse_down_and_sleep(robby, robby.root.game_over_mc.start_mc, wait)
    >>> time.sleep(sloth * 4.051000)
    >>> mouse_down_and_sleep(robby, robby.root._3_1_mc, wait)
    >>> mouse_down_and_sleep(computer_robby, computer_robby.root._1_0_mc, wait)
    >>> time.sleep(sloth * 2.612000)
    >>> mouse_down_and_sleep(robby, robby.root._1_3_mc, wait)
    >>> mouse_down_and_sleep(computer_robby, computer_robby.root._0_1_mc, wait)
    >>> time.sleep(sloth * 2.005000)
    >>> mouse_down_and_sleep(robby, robby.root.extra_stone_gift_mc.use_mc, wait)
    >>> time.sleep(sloth * 1.979000)
    >>> robby.root.cursor_mc.act_mc.currentLabel
    'play'
    >>> mouse_down_and_sleep(robby, robby.root._0_2_mc, wait)
    >>> if not robby.root.comment_mc._txt.text.startswith('WE WOULD BE'):
    ...     robby.root.comment_mc._txt.text
    >>> robby.root.cursor_mc.act_mc.currentLabel
    'play'
    >>> mouse_down_and_sleep(robby, robby.root._0_3_mc, 2 * wait)
    >>> robby.pb()
    ,O,X,
    O,OX,
    ,OX,X
    ,X,X,
    ,,,,,
    '''


def robby_info_example():
    '''Robby mouses over his stone.  In info box, he sees it is black
    and that it attacks and defends.  See "2010-09-24 info.jpg"
        >>> code_unit.inline_examples(
        ...     ethan_lukasz_begin_example.__doc__, 
        ...     locals(), globals(), 
        ...     verify_examples = False)
        >>> wait = 4.0 / black._speed
        >>> sloth = 1.0 / wait
        >>> robby = black
        >>> computer_robby = white
    >>> robby.root.info_mc.currentLabel
    'none'
    >>> robby.root.lobby_mc.main_mc._20_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 3.670000)
    >>> robby.root.lobby_mc._20_mc.extra_hide_9_9_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 3.822000)
        >>> robby.root.game_over_mc.white_computer_mc.enter_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 4.768000)
    >>> mouse_down_and_sleep(robby, robby.root.game_over_mc.start_mc, wait)
    >>> time.sleep(sloth * 4.899000)
    >>> robby.root._2_6_mc.dispatchEvent(mouseOver)
    >>> time.sleep(sloth * 0.5)
    >>> robby.root.info_mc.currentLabel
    'none'
    >>> robby.root.info_mc.stone_mc.currentLabel
    'none'
    >>> robby.root.info_mc.decoration_mc.currentLabel
    'none'
    >>> mouse_down_and_sleep(robby, robby.root._2_6_mc, wait)
    >>> robby.root._2_6_mc.dispatchEvent(mouseOver)
    >>> time.sleep(sloth * 0.5)
    >>> robby.root.info_mc.currentLabel
    'show'
    >>> robby.root.info_mc.stone_mc.currentLabel
    'black'
    >>> robby.root.info_mc.decoration_mc.currentLabel
    'black_attack_defend'
    >>> time.sleep(wait)
    >>> robby.root._2_6_mc.dispatchEvent(mouseOut)
    >>> time.sleep(sloth * 0.5)
    >>> robby.root.info_mc.currentLabel
    'none'
    >>> robby.root.info_mc.stone_mc.currentLabel
    'none'
    >>> robby.root.info_mc.decoration_mc.currentLabel
    'none'
    >>> mouse_down_and_sleep(computer_robby, computer_robby.root._5_3_mc, wait)
    >>> time.sleep(sloth * 4.318000)
    >>> mouse_down_and_sleep(robby, robby.root._4_6_mc, wait)
    >>> mouse_down_and_sleep(computer_robby, computer_robby.root._6_6_mc, wait)
    >>> time.sleep(sloth * 3.821000)
    >>> mouse_down_and_sleep(robby, robby.root._8_6_mc, wait)
    >>> mouse_down_and_sleep(computer_robby, computer_robby.root._5_4_mc, wait)
    >>> time.sleep(sloth * 3.433000)
    >>> robby.root._8_6_mc.dispatchEvent(mouseOver)
    >>> time.sleep(sloth * 0.5)
    >>> robby.root.info_mc.currentLabel
    'show'
    >>> robby.root.info_mc.stone_mc.currentLabel
    'black'
    >>> robby.root.info_mc.territory_mc.currentLabel
    'black_dead'
    >>> time.sleep(sloth * 3.697000)
    >>> mouse_down_and_sleep(robby, robby.root._6_7_mc, wait)
    >>> mouse_down_and_sleep(computer_robby, computer_robby.root._2_3_mc, wait)
    >>> time.sleep(sloth * 2.639000)
    >>> mouse_down_and_sleep(robby, robby.root._1_3_mc, wait)
    >>> mouse_down_and_sleep(computer_robby, computer_robby.root._1_4_mc, wait)
    >>> time.sleep(sloth * 2.206000)
    >>> mouse_down_and_sleep(robby, robby.root._0_4_mc, wait)
    >>> mouse_down_and_sleep(computer_robby, computer_robby.root._1_5_mc, wait)
    >>> time.sleep(sloth * 2.733000)
    >>> mouse_down_and_sleep(robby, robby.root._7_6_mc, wait)
    >>> mouse_down_and_sleep(computer_robby, computer_robby.root._7_3_mc, wait)
    >>> robby.root._7_6_mc.dispatchEvent(mouseOver)
    >>> time.sleep(sloth * 0.5)
    >>> robby.root.info_mc.currentLabel
    'show'
    >>> robby.root.info_mc.stone_mc.currentLabel
    'black'
    >>> robby.root.info_mc.profit_mc.currentLabel
    'show'
    >>> time.sleep(sloth * 2.204000)
    >>> robby.root._8_3_mc.dispatchEvent(mouseOver)
    >>> time.sleep(sloth * 0.5)
    >>> robby.root.info_mc.currentLabel
    'show'
    >>> robby.root.info_mc.stone_mc.currentLabel
    'none'
    >>> robby.root.info_mc.decoration_mc.currentLabel
    'white_attack'
    >>> time.sleep(sloth * 2.204000)
    >>> robby.root._6_2_mc.dispatchEvent(mouseOver)
    >>> time.sleep(sloth * 0.5)
    >>> robby.root.info_mc.currentLabel
    'show'
    >>> robby.root.info_mc.stone_mc.currentLabel
    'none'
    >>> robby.root.info_mc.decoration_mc.currentLabel
    'white_defend'
    >>> robby.root.info_mc.territory_mc.currentLabel
    'white'
    >>> time.sleep(sloth * 2.204000)
    >>> robby.root._6_6_mc.dispatchEvent(mouseOver)
    >>> time.sleep(sloth * 0.5)
    >>> robby.root.info_mc.currentLabel
    'show'
    >>> robby.root.info_mc.stone_mc.currentLabel
    'white'
    >>> robby.root.info_mc.block_mc.currentLabel
    'white_warning'
    >>> time.sleep(sloth * 2.204000)
    >>> robby.root._6_7_mc.dispatchEvent(mouseOver)
    >>> time.sleep(sloth * 0.5)
    >>> robby.root.info_mc.currentLabel
    'show'
    >>> robby.root.info_mc.stone_mc.currentLabel
    'black'
    >>> robby.root.info_mc.block_mc.currentLabel
    'black_block'
    '''

def moonhyoung_sequence_score_example():
    '''Moonhyoung sees low score and sees score rise one point at a time.
        >>> defaults = config.setup_defaults()
        >>> configuration = config.borg(defaults)
        >>> configuration.instant = False
        >>> configuration.mock_speed = 1.0
        >>> code_unit.inline_examples(
        ...     ethan_lukasz_begin_example.__doc__, 
        ...     locals(), globals(), 
        ...     verify_examples = False)
        >>> wait = 4.0 / black._speed
        >>> sloth = 1.0 / wait
        >>> moonhyoung = black
        >>> computer_moonhyoung = white
    >>> # example.log level 20 at Sun Sep 26 10:36:50 2010

    >>> moonhyoung.root.lobby_mc.main_mc._07_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 6.153000)
    >>> moonhyoung.root.lobby_mc._07_mc.score_rule_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 2.158000)
        >>> moonhyoung.root.game_over_mc.white_computer_mc.enter_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 3.948000)
    >>> mouse_down_and_sleep(moonhyoung, moonhyoung.root.game_over_mc.start_mc, wait)
    >>> time.sleep(sloth * 2.923000)
    >>> mouse_down_and_sleep(moonhyoung, moonhyoung.root._2_4_mc, wait)
    >>> mouse_down_and_sleep(computer_moonhyoung, computer_moonhyoung.root._2_0_mc, wait)
    >>> moonhyoung.root.score_mc.bar_mc.currentLabel
    '_-24'
    >>> moonhyoung.root.score_mc.bar_mc.marker_mc.change_txt.text
    '-24'
    >>> mouse_down_and_sleep(moonhyoung, moonhyoung.root._0_1_mc, wait)

    At first score remains same, and then increases.
    >>> moonhyoung.root.score_mc.bar_mc.currentLabel
    '_-24'
    >>> moonhyoung.root.score_mc.bar_mc.marker_mc.change_txt.text
    '-24'
    >>> time.sleep(sloth * 4.004000)
    >>> moonhyoung.root.score_mc.bar_mc.currentLabel
    '_4'
    >>> moonhyoung.root.score_mc.bar_mc.marker_mc.change_txt.text
    '4'
    >>> computer_moonhyoung.root.pass_mc.dispatchEvent(mouseDown)
    '''


def robby_suicide_example():
    '''Robby tries to play suicide but cannot.  He can play elsewhere.
        >>> code_unit.inline_examples(
        ...     ethan_lukasz_begin_example.__doc__, 
        ...     locals(), globals(), 
        ...     verify_examples = False)
        >>> wait = 4.0 / black._speed
        >>> sloth = 1.0 / wait
        >>> robby = black
        >>> computer_robby = white
    >>> robby.root.lobby_mc._00_mc.capture_3_3_1_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 5.450000)
        >>> robby.root.game_over_mc.white_computer_mc.enter_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 3.228000)
    >>> mouse_down_and_sleep(robby, robby.root.game_over_mc.start_mc, wait)
    >>> time.sleep(sloth * 3.342000)
    >>> mouse_down_and_sleep(robby, robby.root._1_1_mc, wait)
    >>> mouse_down_and_sleep(computer_robby, computer_robby.root._2_1_mc, wait)
    >>> time.sleep(sloth * 2.232000)
    >>> mouse_down_and_sleep(robby, robby.root._1_0_mc, wait)
    >>> mouse_down_and_sleep(computer_robby, computer_robby.root._1_2_mc, wait)
    >>> time.sleep(sloth * 2.876000)
    >>> mouse_down_and_sleep(robby, robby.root._2_2_mc, wait)
    >>> robby.root.cursor_mc.act_mc.currentLabel
    'play'
    >>> mouse_down_and_sleep(robby, robby.root._2_0_mc, wait)
    >>> robby.pb()
    ,,,
    XXO
    XO,
    '''

def rene_spam_example():
    '''Rene blocks white.
    >>> rene, wait = setup_example(configuration, 
    ...     ('temporary', 'temporary') )
    >>> sloth = 1.0 / rene._speed
    >>> rene.root.lobby_mc.main_mc._00_mc.dispatchEvent(mouseDown)
    >>> time.sleep(wait)
    >>> rene.root.lobby_mc._00_mc.capture_block_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 4.776711)
    >>> time.sleep(sloth * 3.502065)
    >>> mouse_down_and_sleep(rene, rene.root.game_over_mc.start_mc, wait)
    >>> time.sleep(sloth * 3.408626)
    >>> mouse_down_and_sleep(rene, rene.root._1_2_mc, wait)
    >>> ## mouse_down_and_sleep(computer_rene, computer_rene.root._2_1_mc, wait)

    Rene spams until he can click.
    >>> mouse_down_and_sleep(rene, rene.root._1_0_mc, 0.125 * wait)
    >>> mouse_down_and_sleep(rene, rene.root._1_0_mc, 0.125 * wait)
    >>> mouse_down_and_sleep(rene, rene.root._1_0_mc, 0.125 * wait)
    >>> mouse_down_and_sleep(rene, rene.root._1_0_mc, 0.125 * wait)
    >>> mouse_down_and_sleep(rene, rene.root._1_0_mc, 0.125 * wait)
    >>> mouse_down_and_sleep(rene, rene.root._1_0_mc, 0.125 * wait)
    >>> mouse_down_and_sleep(rene, rene.root._1_0_mc, 0.125 * wait)
   >>> mouse_down_and_sleep(rene, rene.root._1_0_mc, wait)
    >>> ## mouse_down_and_sleep(computer_rene, computer_rene.root._0_2_mc, wait)

    Rene can play.
    >>> rene.root.cursor_mc.act_mc.currentLabel
    'play'
    '''

def rene_progress_example():
    '''rene plays stone and sees progress.  
        >>> code_unit.inline_examples(
        ...     ethan_lukasz_begin_example.__doc__, 
        ...     locals(), globals(), 
        ...     verify_examples = False)
        >>> wait = 4.0 / black._speed
    >>> sloth = 1.0 / black._speed
    >>> rene = black
    >>> computer_rene = white

    >>> rene.root.lobby_mc.main_mc._04_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 3.095000)
    >>> rene.root.lobby_mc._04_mc.dominate_3_3_2_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 4.057000)
        >>> rene.root.game_over_mc.white_computer_mc.enter_mc.dispatchEvent(mouseDown)
    >>> mouse_down_and_sleep(rene, rene.root.game_over_mc.start_mc, wait)
    
    rene moves black.  rene sees progress start.
    if no build, insert nothing.
    >>> rene.root._1_1_mc.progress_mc.currentLabel
    'none'
    >>> computer_rene.root._0_1_mc.currentLabel
    'empty_black'
    >>> rene.root._1_1_mc.dispatchEvent(mouseDown)
    >>> rene.root._1_1_mc.progress_mc.currentLabel
    'black_setup'
    >>> time.sleep(wait)
    >>> rene.root._1_1_mc.progress_mc.currentLabel
    'black_start'
    >>> rene.ambassador.receives[-1]
    
    rene moves white.  rene sees progress start.
    >>> computer_rene.root._0_1_mc.currentLabel
    'empty_white'
    >>> computer_rene.root._0_1_mc.dispatchEvent(mouseDown)
    >>> computer_rene.root._0_1_mc.progress_mc.currentLabel
    'white_setup'
    >>> time.sleep(wait)
    >>> computer_rene.root._0_1_mc.progress_mc.currentLabel
    'white_start'

    when he sees his turn, he also sees progress is complete.
    when black turn, complete progress at any black stone in progress
    when white turn, complete progress at any white stone in progress
    >>> rene.root._1_1_mc.progress_mc.currentLabel
    'black_complete'
    '''


def moonhyoung_info_sequence_example():
    '''Moonhyoung connects his stones, sees defense.  
    Mouse over and sees essential stones of his defense.
        >>> code_unit.inline_examples(
        ...     ethan_lukasz_begin_example.__doc__, 
        ...     locals(), globals(), 
        ...     verify_examples = False)
        >>> wait = 4.0 / black._speed
        >>> sloth = 1.0 / black._speed
        >>> moonhyoung = black
        >>> computer_moonhyoung = white
    >>> time.sleep(sloth * 1.553000)
    >>> moonhyoung.root.lobby_mc.main_mc._10_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 1.573000)
    >>> moonhyoung.root.lobby_mc._10_mc.defend_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 1.084000)
    >>> time.sleep(sloth * 1.489000)
        >>> moonhyoung.root.game_over_mc.white_computer_mc.enter_mc.dispatchEvent(mouseDown)
    >>> mouse_down_and_sleep(moonhyoung, moonhyoung.root.game_over_mc.start_mc, wait)
    >>> moonhyoung.root.comment_mc.none_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 3.219000)
    >>> time.sleep(sloth * 2.613000)
    >>> mouse_down_and_sleep(moonhyoung, moonhyoung.root._2_2_mc, wait)
    >>> computer_moonhyoung.root.pass_mc.dispatchEvent(mouseDown)
    >>> moonhyoung.root.comment_mc.none_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 8.528000)

    Mouse over.  See marks on essential stones in pattern.
    >>> moonhyoung.root['_2_2_mc']['currentLabel']
    'black'
    >>> moonhyoung.root['info_mc']['decoration_mc']['pattern_txt']['text']
    ''
    >>> moonhyoung.root['_1_2_mc']['mark_mc']['currentLabel']
    'none'
    >>> moonhyoung.root._2_2_mc.dispatchEvent(mouseOver)
    >>> time.sleep(sloth * 1.528000)
    >>> moonhyoung.root['info_mc']['decoration_mc']['pattern_txt']['text']
    'CONNECT'
    >>> moonhyoung.root['_1_2_mc']['mark_mc']['currentLabel']
    'show'
    '''
