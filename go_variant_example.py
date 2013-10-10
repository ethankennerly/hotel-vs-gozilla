#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Examples of hide and extra stone.
'''
__author__ = 'Ethan Kennerly'

from client import *



def extra_stone_and_hide_example():
    '''Play extra stone and hide, too.
    >>> code_unit.inline_examples(
    ...     ethan_joris_start_example.__doc__, 
    ...     locals(), globals(), 
    ...     verify_examples = False)

    Joris may receive extra stone and hide gifts.
    >>> property_diff(joris, joris.root.extra_stone_mc, 'currentLabel', 'gift')
    >>> property_diff(joris, joris.root.hide_mc, 'currentLabel', 'gift')

    Ethan may not.
    >>> property_diff(ethan, ethan.root.extra_stone_mc, 'currentLabel', 'none')
    >>> property_diff(ethan, ethan.root.hide_mc, 'currentLabel', 'none')

    before Joris has the extra stone gift, Joris cannot use extra stone.
    >>> property_diff(joris, joris.root.extra_stone_gift_mc, 'currentLabel', '_0')
    >>> mouse_down_and_sleep(joris, joris.root.extra_stone_gift_mc.use_mc, 1.0 / joris._speed)
    >>> property_diff(joris, joris.root.cursor_mc.extra_stone_mc, 'currentLabel', '_0')

    >>> property_diff(joris, joris.root.cursor_mc.act_mc, 'currentLabel', 'play')
    >>> property_diff(joris, joris.root.cursor_mc, 'currentLabel', 'black')
    >>> mouse_down_and_sleep(joris, joris.root._2_2_mc, 1.0 / joris._speed)
    >>> property_diff(joris, joris.root.cursor_mc.act_mc, 'currentLabel', 'preview')
    >>> mouse_down_and_sleep(joris, joris.root._2_2_mc, 1.0 / joris._speed)
    >>> property_diff(joris, joris.root.cursor_mc.act_mc, 'currentLabel', 'none')
    >>> property_diff(joris, joris.root.cursor_mc, 'currentLabel', 'none')
    >>> mouse_down_and_sleep(ethan, ethan.root._4_4_mc, 1.0 / ethan._speed)
    >>> property_diff(joris, joris.root.cursor_mc.act_mc, 'currentLabel', 'play')
    >>> property_diff(joris, joris.root.cursor_mc, 'currentLabel', 'black')
    >>> mouse_down_and_sleep(joris, joris.root._2_4_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._2_4_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._4_2_mc, 1.0 / ethan._speed)
    
    Joris presses extra stone.
    >>> mouse_down_and_sleep(joris, joris.root.extra_stone_gift_mc.use_mc, 1.0 / joris._speed)

    He sees he may take an extra piece.
    >>> property_diff(joris, joris.root.cursor_mc.extra_stone_mc, 'currentLabel', '_1')
    >>> mouse_down_and_sleep(joris, joris.root._6_2_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._6_3_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._6_4_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._6_2_mc, 1.0 / joris._speed)
    >>> property_diff(joris, joris.root.cursor_mc.extra_stone_mc, 'currentLabel', '_1')
    >>> mouse_down_and_sleep(joris, joris.root._6_2_mc, 1.0 / joris._speed)
    >>> property_diff(joris, joris.root.cursor_mc.extra_stone_mc, 'currentLabel', '_0')
    
    since extra stone, still turn of black.
    >>> mouse_down_and_sleep(joris, joris.root._6_4_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._6_4_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._2_5_mc, 1.0 / ethan._speed)

    # >_< formation shows leap through hidden stone 2, 4.  confused.
    Joris presses extra stone.
    >>> mouse_down_and_sleep(joris, joris.root.extra_stone_gift_mc.use_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._7_6_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._7_6_mc, 1.0 / joris._speed)

    Joris presses extra stone, but it cannot be used.
    >>> mouse_down_and_sleep(joris, joris.root.extra_stone_gift_mc.use_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._6_7_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._4_7_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._6_7_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._6_7_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._4_7_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._4_7_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._3_5_mc, 1.0 / ethan._speed)

    Joris presses extra stone.
    >>> mouse_down_and_sleep(joris, joris.root.extra_stone_gift_mc.use_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root.hide_gift_mc.use_mc, 1.0 / joris._speed)

    Joris sees he may now hide.
    >>> property_diff(joris, joris.root.cursor_mc, 'currentLabel', 'hide_black')
    >>> mouse_down_and_sleep(joris, joris.root._2_6_mc, 1.0 / joris._speed)
    >>> joris.pb()
    ,,,,,,,,,
    ,,,,,,,,,
    ,,X,XO],,
    ,,,,,O,,,
    ,,O,O,,,,
    ,,,,,,,,,
    ,,X,X,,X,
    ,,,,,,X,,
    ,,,,,,,,,

    Joris looks elsewhere.
    >>> mouse_down_and_sleep(joris, joris.root._1_6_mc, 1.0 / joris._speed)
    >>> joris.pb()
    ,,,,,,,,,
    ,,,,,,],,
    ,,X,XO,,,
    ,,,,,O,,,
    ,,O,O,,,,
    ,,,,,,,,,
    ,,X,X,,X,
    ,,,,,,X,,
    ,,,,,,,,,
    >>> mouse_down_and_sleep(joris, joris.root._2_6_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._2_6_mc, 1.0 / joris._speed)
    >>> joris.pb()
    ,,,,,,,,,
    ,,,,,,,,,
    ,,X,XO/,,
    ,,,,,O,,,
    ,,O,O,,,,
    ,,,,,,,,,
    ,,X,X,,X,
    ,,,,,,X,,
    ,,,,,,,,,

    Since Joris has extra stone, he can move again.
    >>> property_diff(joris, joris.root.turn_mc, 'currentLabel', 'black')
    >>> property_diff(joris, joris.root.cursor_mc, 'currentLabel', 'black')
    >>> mouse_down_and_sleep(joris, joris.root._1_7_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._1_7_mc, 1.0 / joris._speed)
    >>> joris.pb()
    ,,,,,,,,,
    ,,,,,,,X,
    ,,X,XO/,,
    ,,,,,O,,,
    ,,O,O,,,,
    ,,,,,,,,,
    ,,X,X,,X,
    ,,,,,,X,,
    ,,,,,,,,,
    '''



def hide_not_reveal_example():
    '''
    >>> code_unit.inline_examples(
    ...     ethan_joris_start_example.__doc__, 
    ...     locals(), globals(), 
    ...     verify_examples = False)
    >>> wait = 4.0 / joris._speed

    Joris does not have preview enabled.
    >>> joris.root.preview_gift_mc.enabled_mc.currentLabel
    'none'
    >>> mouse_down_and_sleep(joris, joris.root._2_2_mc, wait)
    >>> ## mouse_down_and_sleep(joris, joris.root._2_2_mc, wait)
    >>> mouse_down_and_sleep(ethan, ethan.root._6_6_mc, wait)
    >>> mouse_down_and_sleep(joris, joris.root._4_2_mc, wait)
    >>> ## mouse_down_and_sleep(joris, joris.root._4_2_mc, wait)
    >>> mouse_down_and_sleep(ethan, ethan.root._6_2_mc, wait)

    Joris clicks the gift of hidden cake.
    >>> mouse_down_and_sleep(joris, joris.root.hide_gift_mc.use_mc, wait)
    >>> property_diff(joris, joris.root.cursor_mc, 'currentLabel', 'hide_black')

    Joris has no more hidden cake.
    >>> property_diff(joris, joris.root.hide_gift_mc, 
    ...     'currentLabel', '_0')

    Joris clicks northeast star and secretly takes it.
    >>> ## mouse_down_and_sleep(joris, joris.root._2_4_mc, wait)
    >>> mouse_down_and_sleep(joris, joris.root._2_6_mc, wait)
    >>> joris.root.preview_gift_mc.enabled_mc.currentLabel
    'none'
    >>> board_diff(joris, joris.root._2_6_mc, 'currentLabel', 'hide_black')
    >>> ## mouse_down_and_sleep(joris, joris.root._2_6_mc, wait)
    >>> board_diff(joris, joris.root._2_6_mc, 'currentLabel', 'hide_black')
    >>> board_diff(ethan, ethan.root._2_6_mc, 'currentLabel', 'empty_white')

    After Ethan plays, Joris sees territory of revealed hidden.
    >>> property_diff(joris, joris.root._1_6_mc.territory_mc, 'currentLabel', 'neutral')

    #+ Territory includes hidden.  GnuGo's response excludes hidden.

    # Ethan clicks there, so both players see it.
    # >>> mouse_down_and_sleep(ethan, ethan.root._2_6_mc, wait)
    # >>> board_diff(joris, joris.root._2_6_mc, 'currentLabel', 'black')
    # >>> board_diff(ethan, ethan.root._2_6_mc, 'currentLabel', 'black')
    >>> mouse_down_and_sleep(ethan, ethan.root._6_4_mc, wait)

    # After Ethan plays, Joris sees territory of revealed hidden.
    >>> property_diff(joris, joris.root._1_6_mc.territory_mc, 'currentLabel', 'neutral')
    '''


def hide_reveal_example():
    '''
    >>> code_unit.inline_examples(
    ...     ethan_joris_start_example.__doc__, 
    ...     locals(), globals(), 
    ...     verify_examples = False)

    >>> mouse_down_and_sleep(joris, joris.root._2_2_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._2_2_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._6_6_mc, 1.0 / ethan._speed)
    >>> mouse_down_and_sleep(joris, joris.root._4_2_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._4_2_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._6_2_mc, 1.0 / ethan._speed)

    Joris clicks the gift of hidden cake.
    >>> mouse_down_and_sleep(joris, joris.root.hide_gift_mc.use_mc, 1.0 / joris._speed)
    >>> property_diff(joris, joris.root.cursor_mc, 'currentLabel', 'hide_black')

    Joris has no more hidden cake.
    >>> property_diff(joris, joris.root.hide_gift_mc, 
    ...     'currentLabel', '_0')

    Joris clicks northeast star and secretly takes it.
    >>> mouse_down_and_sleep(joris, joris.root._2_4_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._2_6_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._2_6_mc, 1.0 / joris._speed)
    >>> board_diff(joris, joris.root._2_6_mc, 'currentLabel', 'hide_black')
    >>> board_diff(ethan, ethan.root._2_6_mc, 'currentLabel', 'empty_white')

    After Ethan plays, Joris sees territory of revealed hidden.
    >>> property_diff(joris, joris.root._1_6_mc.territory_mc, 'currentLabel', 'neutral')

    #+ Territory includes hidden.  GnuGo's response excludes hidden.

    Ethan clicks there, so both players see it.
    >>> mouse_down_and_sleep(ethan, ethan.root._2_6_mc, 1.0 / ethan._speed)
    >>> board_diff(joris, joris.root._2_6_mc, 'currentLabel', 'black')
    >>> board_diff(ethan, ethan.root._2_6_mc, 'currentLabel', 'black')
    >>> mouse_down_and_sleep(ethan, ethan.root._6_4_mc, 1.0 / ethan._speed)

    After Ethan plays, Joris sees territory of revealed hidden.
    >>> property_diff(joris, joris.root._1_6_mc.territory_mc, 'currentLabel', 'black')
    '''


def hide_and_capture_example():
    '''Joris hide.  Capture.  Reveal.
    >>> code_unit.inline_examples(
    ...     ethan_joris_start_example.__doc__, 
    ...     locals(), globals(), 
    ...     verify_examples = False)

    >>> # example.log level 20 at Mon Mar 29 16:20:31 2010
    >>> mouse_down_and_sleep(joris, joris.root._1_1_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._1_1_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._0_0_mc, 1.0 / ethan._speed)
    >>> mouse_down_and_sleep(joris, joris.root._2_2_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._2_2_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._2_0_mc, 1.0 / ethan._speed)

    Joris clicks the gift of hidden cake.
    >>> mouse_down_and_sleep(joris, joris.root.hide_gift_mc.use_mc, 1.0 / joris._speed)
    >>> property_diff(joris, joris.root.cursor_mc, 'currentLabel', 'hide_black')

    Joris has no more hidden cake.
    >>> property_diff(joris, joris.root.hide_gift_mc, 
    ...     'currentLabel', '_0')

    Joris clicks a piece of cake and secretly takes it.
    >>> mouse_down_and_sleep(joris, joris.root._0_2_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._0_1_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._0_1_mc, 1.0 / joris._speed)
    >>> board_diff(joris, joris.root._0_1_mc, 'currentLabel', 'hide_black')
    >>> board_diff(ethan, ethan.root._0_1_mc, 'currentLabel', 'empty_white')
    >>> mouse_down_and_sleep(ethan, ethan.root._4_0_mc, 1.0 / ethan._speed)
    >>> mouse_down_and_sleep(joris, joris.root._1_0_mc, 1.0 / joris._speed)

    Hidden stone assists capture and reveals.
    >>> mouse_down_and_sleep(joris, joris.root._1_0_mc, 1.0 / joris._speed)
    >>> board_diff(joris, joris.root._0_1_mc, 'currentLabel', 'black')
    >>> board_diff(ethan, ethan.root._0_1_mc, 'currentLabel', 'black')
    >>> joris.pb()
    ,X,,,,,,,
    XX,,,,,,,
    O,X,,,,,,
    ,,,,,,,,,
    O,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,

    After white plays, territory reflects revealed hidden.
    >>> property_diff(joris, joris.root._0_0_mc.territory_mc, 'currentLabel', 'dead')

    >>> mouse_down_and_sleep(ethan, ethan.root._3_1_mc, 1.0 / ethan._speed)

    After white plays, territory reflects revealed hidden.
    >>> property_diff(joris, joris.root._0_0_mc.territory_mc, 'currentLabel', 'black')

    >>> mouse_down_and_sleep(joris, joris.root._3_3_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._2_1_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._3_3_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._3_3_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._4_2_mc, 1.0 / ethan._speed)
    >>> mouse_down_and_sleep(joris, joris.root._2_1_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._2_1_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._5_3_mc, 1.0 / ethan._speed)

    Hidden stone captures.

    Joris clicks the gift of hidden cake.
    >>> mouse_down_and_sleep(joris, joris.root.hide_gift_mc.use_mc, 1.0 / joris._speed)
    >>> property_diff(joris, joris.root.cursor_mc, 'currentLabel', 'hide_black')

    >>> mouse_down_and_sleep(joris, joris.root._3_0_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._3_0_mc, 1.0 / joris._speed)

    >>> board_diff(joris, joris.root._2_0_mc, 'currentLabel', 'empty_black')
    >>> board_diff(ethan, ethan.root._2_0_mc, 'currentLabel', 'empty_white')
    >>> board_diff(joris, joris.root._3_0_mc, 'currentLabel', 'black')
    >>> board_diff(ethan, ethan.root._3_0_mc, 'currentLabel', 'black')

    #+ White cannot ko.
    #+ >>> mouse_down_and_sleep(ethan, ethan.root._2_3_mc, 1.0 / ethan._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._6_0_mc, 1.0 / ethan._speed)
    >>> joris.pb()
    ,X,,,,,,,
    XX,,,,,,,
    ,XX,,,,,,
    XO,X,,,,,
    O,O,,,,,,
    ,,,O,,,,,
    O,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,

    White cannot commit suicide at hidden.
    >>> mouse_down_and_sleep(joris, joris.root._2_4_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._2_4_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._4_4_mc, 1.0 / ethan._speed)
    >>> mouse_down_and_sleep(joris, joris.root.hide_gift_mc.use_mc, 1.0 / joris._speed)
    >>> property_diff(joris, joris.root.cursor_mc, 'currentLabel', 'hide_black')
    >>> mouse_down_and_sleep(joris, joris.root._1_3_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._1_3_mc, 1.0 / joris._speed)
    >>> joris.pb()
    ,X,,,,,,,
    XX,/,,,,,
    ,XX,X,,,,
    XO,X,,,,,
    O,O,O,,,,
    ,,,O,,,,,
    O,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    >>> mouse_down_and_sleep(ethan, ethan.root._2_3_mc, 1.0 / ethan._speed)

    #+ After white plays, score reflects revealed hidden.
    #+ >>> property_diff(joris, joris.root.score_mc, 'currentLabel', '_-4')

    Reveal to both players.
    >>> board_diff(joris, joris.root._1_3_mc, 'currentLabel', 'black')
    >>> board_diff(ethan, ethan.root._1_3_mc, 'currentLabel', 'black')
    >>> board_diff(joris, joris.root._2_3_mc, 'currentLabel', 'empty_black')
    >>> board_diff(ethan, ethan.root._2_3_mc, 'currentLabel', 'empty_white')

    White does not lose the turn.
    >>> property_diff(joris, joris.root.turn_mc, 'currentLabel', 'white')
    >>> mouse_down_and_sleep(ethan, ethan.root._5_1_mc, 1.0 / ethan._speed)
    >>> ethan.pb()
    ,X,,,,,,,
    XX,X,,,,,
    ,XX,X,,,,
    XO,X,,,,,
    O,O,O,,,,
    ,O,O,,,,,
    O,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    >>> joris.pb()
    ,X,,,,,,,
    XX,X,,,,,
    ,XX,X,,,,
    XO,X,,,,,
    O,O,O,,,,
    ,O,O,,,,,
    O,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,

    #+ After white plays, territory reflects revealed hidden.
    #+ >>> property_diff(joris, joris.root.score_mc, 'currentLabel', '_-4')

    Reveal two assassins
    >>> mouse_down_and_sleep(joris, joris.root.hide_gift_mc.use_mc, 1.0 / joris._speed)
    >>> property_diff(joris, joris.root.cursor_mc, 'currentLabel', 'hide_black')
    >>> mouse_down_and_sleep(joris, joris.root._3_5_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._3_5_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._3_4_mc, 1.0 / ethan._speed)
    >>> mouse_down_and_sleep(joris, joris.root.hide_gift_mc.use_mc, 1.0 / joris._speed)
    >>> property_diff(joris, joris.root.cursor_mc, 'currentLabel', 'hide_black')
    >>> mouse_down_and_sleep(joris, joris.root._1_5_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._1_5_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._5_5_mc, 1.0 / ethan._speed)
    >>> mouse_down_and_sleep(joris, joris.root._2_6_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._2_6_mc, 1.0 / joris._speed)
    >>> joris.pb()
    ,X,,,,,,,
    XX,X,/,,,
    ,XX,X,X,,
    XO,XO/,,,
    O,O,O,,,,
    ,O,O,O,,,
    O,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    >>> ethan.pb()
    ,X,,,,,,,
    XX,X,,,,,
    ,XX,X,X,,
    XO,XO,,,,
    O,O,O,,,,
    ,O,O,O,,,
    O,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    >>> mouse_down_and_sleep(ethan, ethan.root._2_5_mc, 1.0 / ethan._speed)
    >>> ethan.pb()
    ,X,,,,,,,
    XX,X,X,,,
    ,XX,X,X,,
    XO,XOX,,,
    O,O,O,,,,
    ,O,O,O,,,
    O,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,

    White can still move.
    >>> property_diff(joris, joris.root.turn_mc, 'currentLabel', 'white')
    >>> mouse_down_and_sleep(ethan, ethan.root._4_6_mc, 1.0 / ethan._speed)
    >>> joris.pb()
    ,X,,,,,,,
    XX,X,X,,,
    ,XX,X,X,,
    XO,XOX,,,
    O,O,O,O,,
    ,O,O,O,,,
    O,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,

    After white plays, territory reflects revealed hidden.
    >>> property_diff(joris, joris.root.score_mc, 'currentLabel', '_-17')

    '''

def ethan_mathijs_extra_stone_example():
    '''Mathijs plays his first game.
    >>> code_unit.inline_examples(
    ...     ethan_joris_start_example.__doc__, 
    ...     locals(), globals(), 
    ...     verify_examples = False)

    >>> mathijs = joris

    >>> # example.log level 20 at Sun Mar 28 19:26:56 2010
    >>> mouse_down_and_sleep(joris, joris.root._5_5_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._6_7_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._0_2_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._2_4_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._5_5_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._3_3_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._5_6_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._2_2_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._2_2_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._4_3_mc, 1.0 / ethan._speed)
    >>> mouse_down_and_sleep(joris, joris.root._3_5_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._6_6_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._2_4_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._5_5_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._2_5_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._6_7_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._4_4_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._4_5_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._8_8_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._6_5_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._6_1_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._6_3_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._4_5_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._5_5_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._4_5_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._2_6_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._6_6_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._3_6_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._2_6_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._7_6_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._2_6_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._2_6_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._2_4_mc, 1.0 / ethan._speed)
    >>> mouse_down_and_sleep(joris, joris.root._3_4_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._3_3_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._2_3_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._3_3_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._1_4_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._2_5_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._6_8_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._3_5_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._3_3_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._3_5_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._4_5_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._4_6_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._3_5_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._4_5_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._4_4_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._3_5_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._3_5_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._3_4_mc, 1.0 / ethan._speed)
    >>> mouse_down_and_sleep(joris, joris.root._6_6_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._3_3_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._2_3_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._1_4_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._1_3_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._2_5_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._4_5_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._6_5_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._5_5_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._5_4_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._4_1_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._0_5_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._1_5_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._1_6_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._3_6_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._2_5_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._4_1_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._6_3_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._6_5_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._4_4_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._3_1_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._4_0_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._5_1_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._7_2_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._6_1_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._3_1_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._3_1_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._4_5_mc, 1.0 / ethan._speed)
    >>> mouse_down_and_sleep(joris, joris.root._4_6_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._2_5_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._3_6_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._4_6_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._4_7_mc, 1.0 / joris._speed)
    
    >_<	do not get extra stone.  place at 4, 7.  place at 6, 6.  indignant.
    Joris clicks the free cake gift.
    >>> joris.pb()  # unverfied
    ,,,,,,,,,
    ,,,,,,,,,
    ,,X,O,X,,
    ,X,,OX,,,
    ,,,O,O,%,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    >>> property_diff(joris, joris.root.turn_mc, 'currentLabel', 'black')
    >>> property_diff(joris, joris.root.extra_stone_gift_mc, 
    ...     'currentLabel', '_1')
    >>> mouse_down_and_sleep(joris, joris.root.extra_stone_gift_mc.use_mc, 1.0 / joris._speed)

    Joris sees that he may take a free piece of cake.
    >>> property_diff(joris, joris.root.cursor_mc.extra_stone_mc, 'currentLabel', '_1')
    >>> property_diff(joris, joris.root.turn_mc, 'currentLabel', 'black')
    >>> property_diff(ethan, ethan.root.turn_mc, 'currentLabel', 'black')

    Joris has no gifts of cake left.
    >>> property_diff(joris, joris.root.extra_stone_gift_mc, 
    ...     'currentLabel', '_0')

    >>> mouse_down_and_sleep(joris, joris.root._5_6_mc, 1.0 / joris._speed)
    >>> property_diff(joris, joris.root.cursor_mc.extra_stone_mc, 'currentLabel', '_1')
    >>> mouse_down_and_sleep(joris, joris.root._3_6_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._2_5_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._4_6_mc, 1.0 / joris._speed)
    >>> property_diff(joris, joris.root.cursor_mc.extra_stone_mc, 'currentLabel', '_1')
    >>> mouse_down_and_sleep(joris, joris.root._4_6_mc, 1.0 / joris._speed)

    After first stone, it is still Joris turn.
    >>> property_diff(joris, joris.root.turn_mc, 'currentLabel', 'black')
    >>> property_diff(ethan, ethan.root.turn_mc, 'currentLabel', 'black')
    >>> ## mouse_down_and_sleep(ethan, ethan.root._2_5_mc, 1.0 / ethan._speed)
    >>> mouse_down_and_sleep(joris, joris.root._3_6_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._3_6_mc, 1.0 / joris._speed)
   
    It is Ethan's turn.
    >>> property_diff(joris, joris.root.turn_mc, 'currentLabel', 'white')
    >>> property_diff(ethan, ethan.root.turn_mc, 'currentLabel', 'white')
    >>> joris.pb()  # unverified
    ,,,,,,,,,
    ,,,,,,,,,
    ,,X,O,X,,
    ,X,,OXX,,
    ,,,O,OX,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    '''



def extra_stone_available_example():
    '''Laurens only receives two extra stones.
    attack, defend option on.
    extra stone option on.
    play center.
    get extra stone 1.
    white plays left.
    play extra stone 1 above.
    play below.
    get extra stone 2.
    white plays right.
    play extra stone 2 northeast.
    play northwest.
    do not get extra stone 3.
    white plays southeast.
    try to play extra stone 3 south; instead play single stone south.
    white plays southwest.

    >>> code_unit.inline_examples(
    ...     ethan_lukasz_begin_example.__doc__, 
    ...     locals(), globals(), 
    ...     verify_examples = False)
    >>> wait = 4.0 / black._speed

    [_9_mc:kyu25_9_9.sgf is fragile, where is flexible?]
    >>> mouse_down_and_sleep(black, black.root.lobby_mc._00_mc.hide_7_7_mc,
    ...     wait)
    >>> property_diff(black, black.root.sgf_file_txt, 
    ...     'text', 'sgf/beginner/kyu25_9_9.sgf')
    
    FOR REPLAY, COMPUTER IS NOT PLAYING.
    >>> mouse_down_and_sleep(black, black.root.game_over_mc.white_computer_mc.enter_mc, wait)
    >>> property_diff(black, black.root.game_over_mc.white_computer_mc, 'currentLabel', 'none')

    LAURENS CAN SEE ATTACK, DEFEND AND RECEIVE TWO EXTRA STONE.
    >>> property_diff(black, black.root.attack_mc, 'currentLabel', 'show')
    >>> property_diff(black, black.root.defend_mc, 'currentLabel', 'show')
    >>> property_diff(black, black.root.extra_stone_mc, 'currentLabel', 'gift')
    >>> property_diff(black, black.root.option_mc.extra_stone_available_mc, 'currentLabel', '_2')

    >>> mouse_down_and_sleep(black, black.root.game_over_mc.start_mc, wait)
    >>> mouse_down_and_sleep(black, black.root._4_4_mc, wait)
    >>> mouse_down_and_sleep(black, black.root._4_4_mc, wait)
    >>> mouse_down_and_sleep(ethan, ethan.root._5_2_mc, wait)
    >>> mouse_down_and_sleep(black, black.root.extra_stone_gift_mc.use_mc, wait)
    >>> mouse_down_and_sleep(black, black.root._2_4_mc, wait)
    >>> mouse_down_and_sleep(black, black.root._2_4_mc, wait)
    >>> mouse_down_and_sleep(black, black.root._6_4_mc, wait)
    >>> mouse_down_and_sleep(black, black.root._6_4_mc, wait)
    >>> mouse_down_and_sleep(ethan, ethan.root._2_2_mc, wait)
    >>> mouse_down_and_sleep(black, black.root.extra_stone_gift_mc.use_mc, wait)
    >>> mouse_down_and_sleep(black, black.root._6_6_mc, wait)
    >>> mouse_down_and_sleep(black, black.root._6_6_mc, wait)
    >>> mouse_down_and_sleep(black, black.root._2_6_mc, wait)
    >>> mouse_down_and_sleep(black, black.root._2_6_mc, wait)
    >>> mouse_down_and_sleep(ethan, ethan.root._7_3_mc, wait)
    >>> mouse_down_and_sleep(black, black.root.extra_stone_gift_mc.use_mc, wait)

    LAURENS DOES NOT GET AN EXTRA STONE.
    >>> mouse_down_and_sleep(black, black.root._7_5_mc, wait)
    >>> mouse_down_and_sleep(black, black.root._7_5_mc, wait)
    >>> mouse_down_and_sleep(ethan, ethan.root._1_3_mc, wait)
    >>> black.pb()
    ,,,,,,,,,
    ,,,O,,,,,
    ,,O,X,X,,
    ,,,,,,,,,
    ,,,,X,,,,
    ,,O,,,,,,
    ,,,,X,X,,
    ,,,O,X,,,
    ,,,,,,,,,
    '''


def hide_available_example():
    '''Laurens only receives two extra stones.
    attack, defend option on.
    extra stone option on.
    play center.
    get extra stone 1.
    white plays left.
    play extra stone 1 above.
    play below.
    get extra stone 2.
    white plays right.
    play extra stone 2 northeast.
    play northwest.
    do not get extra stone 3.
    white plays southeast.
    try to play extra stone 3 south; instead play single stone south.
    white plays southwest.

    >>> code_unit.inline_examples(
    ...     ethan_lukasz_begin_example.__doc__, 
    ...     locals(), globals(), 
    ...     verify_examples = False)
    >>> wait = 4.0 / black._speed

    [_9_mc:kyu25_9_9.sgf is fragile, where is flexible?]
    >>> mouse_down_and_sleep(black, black.root.lobby_mc._00_mc.hide_5_5_mc,
    ...     wait)
    >>> property_diff(black, black.root.sgf_file_txt, 
    ...     'text', 'sgf/beginner/hide_9_9.sgf')
    
    FOR REPLAY, COMPUTER IS NOT PLAYING.
    >>> mouse_down_and_sleep(black, black.root.game_over_mc.white_computer_mc.enter_mc, wait)
    >>> property_diff(black, black.root.game_over_mc.white_computer_mc, 'currentLabel', 'none')

    LAURENS CAN SEE ATTACK, DEFEND AND RECEIVE TWO HIDE.
    >>> property_diff(black, black.root.attack_mc, 'currentLabel', 'show')
    >>> property_diff(black, black.root.defend_mc, 'currentLabel', 'show')
    >>> property_diff(black, black.root.hide_mc, 'currentLabel', 'gift')
    >>> property_diff(black, black.root.option_mc.extra_stone_available_mc, 'currentLabel', '_0')
    >>> property_diff(black, black.root.option_mc.hide_available_mc, 'currentLabel', '_2')

    >>> mouse_down_and_sleep(black, black.root.game_over_mc.start_mc, wait)
    >>> property_diff(black, black.root.hide_gift_mc, 'currentLabel', '_0')
    >>> mouse_down_and_sleep(black, black.root._4_4_mc, wait)
    >>> mouse_down_and_sleep(black, black.root._4_4_mc, wait)
    >>> property_diff(black, black.root.hide_gift_mc, 'currentLabel', '_1')
    >>> mouse_down_and_sleep(white, white.root._5_2_mc, wait)
    >>> mouse_down_and_sleep(black, black.root.hide_gift_mc.use_mc, wait)
    >>> mouse_down_and_sleep(black, black.root._2_4_mc, wait)
    >>> mouse_down_and_sleep(black, black.root._2_4_mc, wait)
    >>> property_diff(black, black.root.hide_gift_mc, 'currentLabel', '_1')
    >>> mouse_down_and_sleep(white, white.root._2_2_mc, wait)
    >>> mouse_down_and_sleep(black, black.root.hide_gift_mc.use_mc, wait)
    >>> mouse_down_and_sleep(black, black.root._6_6_mc, wait)
    >>> mouse_down_and_sleep(black, black.root._6_6_mc, wait)
    >>> property_diff(black, black.root.hide_gift_mc, 'currentLabel', '_0')
    >>> mouse_down_and_sleep(white, white.root._7_3_mc, wait)
    >>> mouse_down_and_sleep(black, black.root.hide_gift_mc.use_mc, wait)

    LAURENS DOES NOT GET A HIDE, SO WHITE CAN SEE HIS STONE.
    >>> mouse_down_and_sleep(black, black.root._7_5_mc, wait)
    >>> mouse_down_and_sleep(black, black.root._7_5_mc, wait)
    >>> mouse_down_and_sleep(white, white.root._1_3_mc, wait)
    >>> black.pb()
    ,,,,,,,,,
    ,,,O,,,,,
    ,,O,/,,,,
    ,,,,,,,,,
    ,,,,X,,,,
    ,,O,,,,,,
    ,,,,,,/,,
    ,,,O,X,,,
    ,,,,,,,,,
    >>> white.pb()
    ,,,,,,,,,
    ,,,O,,,,,
    ,,O,,,,,,
    ,,,,,,,,,
    ,,,,X,,,,
    ,,O,,,,,,
    ,,,,,,,,,
    ,,,O,X,,,
    ,,,,,,,,,
    '''

