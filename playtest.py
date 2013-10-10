#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Playtests of 9x9 Crazy Cake
'''
__author__ = 'Ethan Kennerly'
from client import *
from intersection_mc import get_response_rotate_names

def ethan_mathijs_example():
    '''First two-player game, Mathijs' first time.

    If Mathijs played twice in a row, insert a extra stone.
    If Ethan played at a place Mathijs had played, insert hide stone.
    >>> code_unit.inline_examples(
    ...     ethan_joris_start_example.__doc__, 
    ...     locals(), globals(), 
    ...     verify_examples = False)

    >>> mathijs = joris
    >>> wait = 3.0 / mathijs._speed
    >>> mouse_down_and_sleep(mathijs, mathijs.root._5_5_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._6_7_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._0_2_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._2_4_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._5_5_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._3_3_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._5_6_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._2_2_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._2_2_mc, wait)

    #REAL-TIME
    #ethan clicks clock button.
    #>>> mouse_down_and_sleep(ethan, ethan.root.clock_mc.enter_mc.enter_btn, 1.0 / ethan._speed)

    #joris and ethan see a clock between them.
    #>>> property_diff(joris, joris.root.clock_mc, 'currentLabel', 'time')
    #>>> property_diff(ethan, ethan.root.clock_mc, 'currentLabel', 'time')

    #each player sees that it is their turn.
    #>>> property_diff(joris, joris.root.turn_mc, 'currentLabel', 'black')
    #>>> property_diff(ethan, ethan.root.turn_mc, 'currentLabel', 'white')

    #XXX each player waits until they can eat...
    #>>> mouse_down_and_sleep = digest_and(mouse_down_and_sleep)

    >>> mouse_down_and_sleep(ethan, ethan.root._4_3_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._3_5_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._6_6_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._2_4_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._5_5_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._2_5_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._6_7_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._4_4_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._4_5_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._8_8_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._6_5_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._6_1_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._6_3_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._4_5_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._5_5_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._4_5_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._2_6_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._6_6_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._3_6_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._2_6_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._7_6_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._2_6_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._2_6_mc, wait)
    >>> mouse_down_and_sleep(ethan, ethan.root._2_4_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._3_4_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._3_3_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._2_3_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._3_3_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._1_4_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._2_5_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._6_8_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._3_5_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._3_3_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._3_5_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._4_5_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._4_6_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._3_5_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._4_5_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._4_4_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._3_5_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._3_5_mc, wait)
    >>> mathijs.pb()
    ,,,,,,,,,
    ,,,,,,,,,
    ,,X,O,X,,
    ,,,,,X,,,
    ,,,O,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    >>> ethan.pb()
    ,,,,,,,,,
    ,,,,,,,,,
    ,,X,O,X,,
    ,,,,,X,,,
    ,,,O,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    >>> mouse_down_and_sleep(ethan, ethan.root._3_4_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._6_6_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._3_3_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._2_3_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._1_4_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._1_3_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._2_5_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._4_5_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._6_5_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._5_5_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._5_4_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._4_1_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._0_5_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._1_5_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._1_6_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._3_6_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._2_5_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._4_1_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._6_3_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._6_5_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._4_4_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._3_1_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._4_0_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._5_1_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._7_2_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._6_1_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._3_1_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._3_1_mc, wait)
    >>> mouse_down_and_sleep(ethan, ethan.root._4_5_mc, wait)
    >>> mathijs.pb()
    ,,,,,,,,,
    ,,,,,,,,,
    ,,X,O,X,,
    ,X,,OX,,,
    ,,,O,O,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    >>> ethan.pb()
    ,,,,,,,,,
    ,,,,,,,,,
    ,,X,O,X,,
    ,X,,OX,,,
    ,,,O,O,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    >>> mouse_down_and_sleep(mathijs, mathijs.root._4_6_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._2_5_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._3_6_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._4_6_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._4_7_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._5_6_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._3_6_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._2_5_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._4_6_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._4_6_mc, wait)
    >>> mouse_down_and_sleep(ethan, ethan.root._2_5_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root.hide_gift_mc.use_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._3_6_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._3_6_mc, wait)
    >>> mouse_down_and_sleep(ethan, ethan.root._3_6_mc, wait)
    >>> mouse_down_and_sleep(ethan, ethan.root._5_5_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._6_6_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._5_2_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._1_3_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._1_5_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._1_4_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._5_2_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._7_3_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._7_6_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._7_3_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._6_2_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._6_2_mc, wait)
    >>> mouse_down_and_sleep(ethan, ethan.root._5_2_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._8_5_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._6_3_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._4_2_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._3_3_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._6_4_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._5_3_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._5_6_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._6_6_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._6_4_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._7_4_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._7_3_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._6_3_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._7_4_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._7_5_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._7_6_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._6_7_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._2_3_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._1_3_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._1_4_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._6_6_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._6_4_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._6_3_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._7_3_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._5_3_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._5_4_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._4_4_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._5_4_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._6_7_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._6_4_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._6_3_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._7_3_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._7_4_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._7_4_mc, wait)
    >>> mouse_down_and_sleep(ethan, ethan.root._6_4_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._6_6_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._6_6_mc, wait)
    >>> mouse_down_and_sleep(ethan, ethan.root._7_3_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._6_3_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._6_5_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._6_3_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._5_3_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._6_1_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._6_5_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._7_5_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._3_3_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._4_2_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._5_1_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._4_2_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._4_1_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._2_3_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._1_4_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._4_2_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._5_1_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._4_2_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._5_1_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._2_3_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._4_2_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._5_6_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._7_5_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._5_6_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._6_5_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._7_5_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._6_5_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._6_5_mc, wait)
    >>> mouse_down_and_sleep(ethan, ethan.root._7_5_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._8_4_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._5_6_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._4_2_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._6_1_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._7_2_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._6_3_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._5_3_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._6_3_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._6_1_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._6_3_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._5_3_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._6_3_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._3_3_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._1_3_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._1_4_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._4_2_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._5_1_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._4_2_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._5_1_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._3_3_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._6_1_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._5_1_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._7_2_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._6_3_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._6_3_mc, wait)
    >>> mouse_down_and_sleep(ethan, ethan.root._8_4_mc, wait)
    >>> ## mouse_down_and_sleep(mathijs, mathijs.root.extra_stone_gift_mc.use_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root.hide_gift_mc.use_mc, wait)
    >>> #  mouse_down_and_sleep(mathijs, mathijs.root._7_4_mc, wait)
    >>> #  mouse_down_and_sleep(mathijs, mathijs.root._7_4_mc, wait)
    >>> #  mouse_down_and_sleep(mathijs, mathijs.root._7_4_mc, wait)
    >>> #  mouse_down_and_sleep(mathijs, mathijs.root._7_4_mc, wait)
    >>> #  mouse_down_and_sleep(mathijs, mathijs.root._7_4_mc, wait)
    >>> #  mouse_down_and_sleep(mathijs, mathijs.root._7_4_mc, wait)
    >>> #  mouse_down_and_sleep(mathijs, mathijs.root._7_4_mc, wait)
    >>> #  mouse_down_and_sleep(mathijs, mathijs.root._7_4_mc, wait)
    >>> #  mouse_down_and_sleep(mathijs, mathijs.root._7_4_mc, wait)
    >>> #  mouse_down_and_sleep(mathijs, mathijs.root._7_4_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._7_4_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._5_4_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._4_4_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._5_4_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._5_3_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._5_4_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._5_4_mc, wait)
    >>> mouse_down_and_sleep(ethan, ethan.root._7_4_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._5_6_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._5_6_mc, wait)
    >>> mouse_down_and_sleep(ethan, ethan.root._4_4_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._6_1_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._5_1_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._4_2_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._3_3_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._4_2_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._3_2_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._1_4_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._1_5_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._0_3_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._1_3_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._1_5_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._0_6_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._0_5_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._6_1_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._7_2_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._6_1_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._5_1_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._6_1_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._5_1_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._5_1_mc, wait) # retroactive, server fail to log?
    >>> mouse_down_and_sleep(ethan, ethan.root._7_2_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._5_3_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._5_3_mc, wait)
    >>> mouse_down_and_sleep(ethan, ethan.root._8_8_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._4_2_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._4_2_mc, wait)
    >>> mouse_down_and_sleep(ethan, ethan.root._6_1_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._6_0_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._7_1_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._7_0_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._8_0_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._7_0_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._8_6_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._7_6_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._8_5_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._8_6_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._1_5_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._1_3_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._1_4_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._1_5_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._5_2_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._6_0_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._5_2_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._5_2_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._3_7_mc, wait) # retroactive
    >>> mouse_down_and_sleep(mathijs, mathijs.root._3_7_mc, wait) # retroactive
    >>> mouse_down_and_sleep(ethan, ethan.root._7_1_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._3_3_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._7_0_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._6_0_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._7_0_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._7_6_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._1_5_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._1_3_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._2_3_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._3_3_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._3_3_mc, wait)
    >>> mouse_down_and_sleep(ethan, ethan.root._2_3_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._1_3_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._1_5_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._1_5_mc, wait)
    >>> mouse_down_and_sleep(ethan, ethan.root._1_4_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._0_4_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._0_4_mc, wait)
    >>> mouse_down_and_sleep(ethan, ethan.root._3_2_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._1_3_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._1_3_mc, wait)
    >>> mouse_down_and_sleep(ethan, ethan.root._5_0_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._4_0_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._7_6_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._8_5_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._8_6_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._7_7_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._8_6_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._7_7_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._3_3_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._3_3_mc, wait)
    >>> mouse_down_and_sleep(ethan, ethan.root._3_0_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._4_0_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root.hide_gift_mc.use_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._2_0_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._2_0_mc, wait)
    >>> mouse_down_and_sleep(ethan, ethan.root._2_0_mc, wait)
    >>> mouse_down_and_sleep(ethan, ethan.root._7_6_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._7_7_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._6_7_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root.hide_gift_mc.use_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._7_8_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._7_8_mc, wait)
    >>> mouse_down_and_sleep(ethan, ethan.root._6_7_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._7_7_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._7_7_mc, wait)
    >>> mouse_down_and_sleep(ethan, ethan.root._7_8_mc, wait)
    >>> mouse_down_and_sleep(ethan, ethan.root._6_8_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root.hide_gift_mc.use_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._8_7_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._8_7_mc, wait)
    >>> mouse_down_and_sleep(ethan, ethan.root._8_7_mc, wait)
    >>> mouse_down_and_sleep(ethan, ethan.root._8_6_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._4_0_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._4_0_mc, wait)
    >>> mouse_down_and_sleep(ethan, ethan.root._6_0_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root.hide_gift_mc.use_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._5_7_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._5_7_mc, wait)
    >>> mouse_down_and_sleep(ethan, ethan.root._5_7_mc, wait)
    >>> mouse_down_and_sleep(ethan, ethan.root._5_8_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root.hide_gift_mc.use_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._4_8_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._4_8_mc, wait)
    >>> mouse_down_and_sleep(ethan, ethan.root._4_8_mc, wait)
    >>> mouse_down_and_sleep(ethan, ethan.root._7_7_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._3_7_mc, wait)
    >>> mouse_down_and_sleep(mathijs, mathijs.root._3_7_mc, wait)
    >>> mouse_down_and_sleep(ethan, ethan.root._4_7_mc, wait)
    >>> mathijs.pb()
    ,,,,X,,,,
    ,,,X,X,,,
    X,X,,,X,,
    ,X,X,XX,,
    X,X,,,XOX
    OXXXX,XX,
    OOXXOXX,,
    ,OOOOOOXX
    ,,,,O,OX,
    >>> ethan.pb()
    ,,,,X,,,,
    ,,,X,X,,,
    X,X,,,X,,
    ,X,X,XX,,
    X,X,,,XOX
    OXXXX,XX,
    OOXXOXX,,
    ,OOOOOOXX
    ,,,,O,OX,
    '''

def ethan_michael_example():
    '''Michael's first game (and first game of Go) against Ethan.

    16 ?^_^ when i view michael's the stones being played on the left side, how can i see attacks and defenses?
        !^_^	replay move at 4 seconds.
        !^_^	sometimes, attacker dragon status about 4 seconds.  replay move at 1 second.
            >_<	next move occurs before last one has had its attacker dragon status revealed.  lose stone play.  corrupt replay.

    >>> wait = 4.0
    >>> code_unit.inline_examples(
    ...     ethan_joris_start_example.__doc__, 
    ...     locals(), globals(), 
    ...     verify_examples = False)

    >>> michael = joris
    >>> # example.log level 20 at Thu Apr 15 17:02:07 2010
    >>> mouse_down_and_sleep(joris, joris.root._2_2_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._5_0_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._5_2_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._5_2_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._4_4_mc, wait / ethan._speed)
    >>> mouse_down_and_sleep(joris, joris.root._2_2_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._2_2_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._6_4_mc, wait / ethan._speed)
    >>> mouse_down_and_sleep(joris, joris.root._2_6_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._2_6_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._2_4_mc, wait / ethan._speed)
    >>> mouse_down_and_sleep(joris, joris.root._3_4_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._3_4_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._3_5_mc, wait / ethan._speed)
    >>> mouse_down_and_sleep(joris, joris.root._3_3_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._3_3_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._5_6_mc, wait / ethan._speed)
    >>> mouse_down_and_sleep(joris, joris.root.extra_stone_gift_mc.use_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._4_6_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._3_6_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._2_5_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._2_5_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._2_3_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._2_3_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._3_6_mc, wait / ethan._speed)
    >>> mouse_down_and_sleep(joris, joris.root.hide_gift_mc.use_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._6_3_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._6_3_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._4_3_mc, wait / ethan._speed)
    >>> mouse_down_and_sleep(joris, joris.root._4_2_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._4_2_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._7_2_mc, wait / ethan._speed)
    >>> mouse_down_and_sleep(joris, joris.root._7_3_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._7_3_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._6_3_mc, wait / ethan._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._5_3_mc, wait / ethan._speed)
    >>> mouse_down_and_sleep(joris, joris.root.extra_stone_gift_mc.use_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._8_3_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._8_3_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._2_7_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._2_7_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._6_2_mc, wait / ethan._speed)
    >>> mouse_down_and_sleep(joris, joris.root.extra_stone_gift_mc.use_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._3_7_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._3_7_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._4_7_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._4_7_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._5_7_mc, wait / ethan._speed)
    >>> mouse_down_and_sleep(joris, joris.root.extra_stone_gift_mc.use_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._4_8_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._4_8_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._6_1_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._6_1_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._7_1_mc, wait / ethan._speed)
    >>> mouse_down_and_sleep(joris, joris.root._6_0_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._6_0_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._7_4_mc, wait / ethan._speed)
    >>> mouse_down_and_sleep(joris, joris.root._8_2_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._7_0_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._7_0_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._8_4_mc, wait / ethan._speed)
    >>> mouse_down_and_sleep(joris, joris.root._5_8_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._5_8_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._8_2_mc, wait / ethan._speed)
    >>> mouse_down_and_sleep(joris, joris.root._6_5_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._6_5_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._6_7_mc, wait / ethan._speed)
    >>> mouse_down_and_sleep(joris, joris.root._7_7_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._7_7_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._6_8_mc, wait / ethan._speed)
    >>> mouse_down_and_sleep(joris, joris.root._6_6_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._6_6_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._4_6_mc, wait / ethan._speed)
    >>> mouse_down_and_sleep(joris, joris.root._7_8_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._7_8_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._5_5_mc, wait / ethan._speed)
    >>> mouse_down_and_sleep(joris, joris.root._8_0_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._8_0_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._5_1_mc, wait / ethan._speed)
    >>> mouse_down_and_sleep(joris, joris.root._5_0_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._5_0_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._4_1_mc, wait / ethan._speed)
    >>> joris.pb()
    ,,,,,,,,,
    ,,,,,,,,,
    ,,XXOXXX,
    ,,,XXOOX,
    ,OXOO,OXX
    XOXO,OOOX
    XXO,OXXOO
    XOO,O,,XX
    X,O,O,,,,
    
    >>> mouse_down_and_sleep(joris, joris.root._4_0_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._3_1_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._3_1_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._3_2_mc, wait / ethan._speed)
    >>> mouse_down_and_sleep(joris, joris.root._4_0_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._4_0_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._3_0_mc, wait / ethan._speed)
    >>> mouse_down_and_sleep(joris, joris.root._2_0_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._2_0_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._4_2_mc, wait / ethan._speed)
    >>> joris.pb()
    ,,,,,,,,,
    ,,,,,,,,,
    X,XXOXXX,
    ,XOXXOOX,
    XOOOO,OXX
    XO,O,OOOX
    XXO,OXXOO
    XOO,O,,XX
    X,O,O,,,,
    '''

def ethan_andre_example():
    '''
    !^_^    andre plays gogui 5x5
    & !^_^    andre plays gogui 3x3
    & !^_^    andre plays crazy cake 9x9.  i ignore hide.
        ^_^    on 9x9 with me clarifying, andre uses 5 extra stones and surrounded white's cut.  white resigns.
        ^_^    on 9x9, andre sees animations, browsed, and often selected animations.
        ^_^    i tell andre that the best move is a combo:  attack, defend, and territory.  looks for those.
        ^_^    after 9x9, andre says it reminds him of minesweeper.
        >_<    on 9x9, i tell andre star is attack.  later andre sees star.  andre asks:  star is attack?
        >_<    on 9x9, i tell andre pink is defend.
        >_<    perhaps andre does not see the defend hearts.  andre asks me if a move is a combo attack and defend.
        >_<    i tell andre that the best move is a combo:  attack, defend, and territory.
        >_<    later on, andre finds cherry.  he says that, and I think it is not so good now.
    
    >>> wait = 4.0
    >>> code_unit.inline_examples(
    ...     ethan_joris_start_example.__doc__, 
    ...     locals(), globals(), 
    ...     verify_examples = False)
    >>> andre = joris
    >>> # example.log level 20 at Thu Apr 22 16:09:32 2010
    >>> mouse_down_and_sleep(joris, joris.root._2_6_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._6_6_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._2_6_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._6_2_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._0_7_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._1_7_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._1_8_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._0_0_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._1_0_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._2_0_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._3_0_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._4_0_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._2_6_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._2_8_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._5_3_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._7_4_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._4_5_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._2_2_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._5_5_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._4_2_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._5_6_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._1_1_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._5_2_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._5_2_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._4_4_mc, wait / ethan._speed)
    >>> mouse_down_and_sleep(joris, joris.root._6_6_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._2_6_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._1_2_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._1_2_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._3_2_mc, wait / ethan._speed)
    >>> mouse_down_and_sleep(joris, joris.root._2_6_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._6_4_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._2_4_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._3_3_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._4_1_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._2_4_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._2_4_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._6_4_mc, wait / ethan._speed)
    >>> mouse_down_and_sleep(joris, joris.root.extra_stone_gift_mc.use_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._4_6_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._7_6_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._4_6_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._4_6_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._7_6_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._7_6_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._5_6_mc, wait / ethan._speed)
    >>> mouse_down_and_sleep(joris, joris.root._6_5_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root.extra_stone_gift_mc.use_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._7_3_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._7_3_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._3_1_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._4_1_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._2_1_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._4_1_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._4_1_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._3_1_mc, wait / ethan._speed)
    >>> mouse_down_and_sleep(joris, joris.root._4_3_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root.extra_stone_gift_mc.use_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._4_3_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._4_3_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._3_5_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._3_5_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._3_3_mc, wait / ethan._speed)
    >>> mouse_down_and_sleep(joris, joris.root.extra_stone_gift_mc.use_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._5_3_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._5_3_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._2_2_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._4_2_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._3_4_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._2_3_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._2_0_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._2_3_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._2_3_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._3_4_mc, wait / ethan._speed)
    >>> mouse_down_and_sleep(joris, joris.root._5_5_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._5_4_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._4_2_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._4_5_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._5_5_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._5_5_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._5_4_mc, wait / ethan._speed)
    >>> mouse_down_and_sleep(joris, joris.root._6_5_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._3_0_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._3_3_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root.extra_stone_gift_mc.use_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._5_3_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._4_2_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._7_4_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._6_5_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._7_5_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._6_5_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._6_5_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._4_5_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._7_4_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._6_1_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._6_1_mc, wait / joris._speed)
    >>> joris.pb()
    ,,,,,,,,,
    ,,X,,,,,,
    ,,,XX,,,,
    ,OOOOX,,,
    ,X,XO,X,,
    ,,XXOXO,,
    ,X,,OX,,,
    ,,,X,,X,,
    ,,,,,,,,,
    '''

def joris_5_5_example():
    '''
    >>> code_unit.inline_examples(
    ...     ethan_joris_start_example.__doc__, 
    ...     locals(), globals(), 
    ...     verify_examples = False)

    !^_^    territory, liberty, extra stone, _5_5, white computer.
    >>> wait = 2.0
    >>> mouse_down_and_sleep(joris, joris.root.game_over_mc._5_5_mc.enter_mc, wait / joris._speed)
    >>> ## mouse_down_and_sleep(joris, joris.root.game_over_mc.white_computer_mc.enter_mc, wait / joris._speed)

    >>> mouse_down_and_sleep(joris, joris.root._3_3_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._3_1_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._1_3_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._2_2_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._2_2_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._3_2_mc, wait / ethan._speed)
    >>> mouse_down_and_sleep(joris, joris.root.extra_stone_gift_mc.use_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._3_3_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._2_1_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._3_0_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._2_3_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._2_3_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._4_3_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._3_0_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._3_0_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._3_3_mc, wait / ethan._speed)
    >>> mouse_down_and_sleep(joris, joris.root._4_1_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._3_1_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._4_1_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._4_1_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._3_4_mc, wait / ethan._speed)
    >>> mouse_down_and_sleep(joris, joris.root._2_4_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._3_1_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._3_1_mc, wait / joris._speed)
    >>> joris.pb()
    ,,,,,
    ,,,,,
    ,,XX,
    XXOOO
    ,X,,,
    
    ^_^ joris wins.
    ^_^ joris wants to make candles.
    >_< joris makes candle in the corner and it is a false eye.
    >_< too easy.
    '''



def gnugo_wout_example():
    ''' 05/16/2010 Sun 22:01
    >>> code_unit.inline_examples(
    ...     ethan_joris_start_example.__doc__, 
    ...     locals(), globals(), 
    ...     verify_examples = False)
    >>> wait = 3.0
    >>> wout = joris
    >>> gnugo = ethan
    >>> mouse_down_and_sleep(joris, joris.root._5_3_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._5_3_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._6_2_mc, wait / ethan._speed)
    >>> mouse_down_and_sleep(joris, joris.root.extra_stone_gift_mc.use_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._5_2_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._7_4_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._7_4_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._4_1_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._4_1_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._2_5_mc, wait / ethan._speed)
    >>> mouse_down_and_sleep(joris, joris.root._3_4_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._3_4_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._2_4_mc, wait / ethan._speed)
    >>> mouse_down_and_sleep(joris, joris.root._3_5_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._3_5_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._2_6_mc, wait / ethan._speed)
    >>> mouse_down_and_sleep(joris, joris.root._3_7_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._4_6_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._2_7_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._3_7_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._3_6_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._3_6_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._2_3_mc, wait / ethan._speed)
    >>> mouse_down_and_sleep(joris, joris.root._2_2_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._2_2_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._1_2_mc, wait / ethan._speed)
    >>> mouse_down_and_sleep(joris, joris.root._3_3_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._3_3_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._2_1_mc, wait / ethan._speed)
    >>> mouse_down_and_sleep(joris, joris.root._3_2_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._3_2_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._2_7_mc, wait / ethan._speed)
    >>> mouse_down_and_sleep(joris, joris.root._3_7_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._3_7_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._3_8_mc, wait / ethan._speed)
    >>> mouse_down_and_sleep(joris, joris.root._4_8_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._4_8_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._2_8_mc, wait / ethan._speed)
    >>> mouse_down_and_sleep(joris, joris.root._2_0_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._3_1_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._3_1_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._4_7_mc, wait / ethan._speed)
    >>> mouse_down_and_sleep(joris, joris.root._5_8_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._5_8_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._5_7_mc, wait / ethan._speed)
    >>> mouse_down_and_sleep(joris, joris.root._6_7_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._6_6_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._6_6_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._1_1_mc, wait / ethan._speed)
    >>> mouse_down_and_sleep(joris, joris.root._2_0_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._3_0_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._6_7_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._6_7_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._6_8_mc, wait / ethan._speed)
    >>> mouse_down_and_sleep(joris, joris.root._5_6_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._5_6_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._7_7_mc, wait / ethan._speed)
    >>> mouse_down_and_sleep(joris, joris.root._7_8_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._7_6_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._7_6_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._4_6_mc, wait / ethan._speed)
    >>> mouse_down_and_sleep(joris, joris.root._4_5_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._7_8_mc, wait / ethan._speed)
    >>> mouse_down_and_sleep(joris, joris.root._7_6_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._8_6_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._8_7_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._8_7_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._3_0_mc, wait / ethan._speed)
    >>> mouse_down_and_sleep(joris, joris.root._4_0_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._2_0_mc, wait / ethan._speed)
    >>> mouse_down_and_sleep(joris, joris.root._8_8_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._8_6_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._8_6_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._5_8_mc, wait / ethan._speed)
    >>> mouse_down_and_sleep(joris, joris.root._8_8_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._8_8_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._4_8_mc, wait / ethan._speed)
    >>> mouse_down_and_sleep(joris, joris.root._5_5_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._5_5_mc, wait / joris._speed)
    '''

def gnugo_wout_7_7_example():
    ''' 05/16/2010 Sun 22:01
    >>> code_unit.inline_examples(
    ...     ethan_joris_start_example.__doc__, 
    ...     locals(), globals(), 
    ...     verify_examples = False)
    >>> wout = joris
    >>> gnugo = ethan
    >>> mouse_down_and_sleep(joris, joris.root.game_over_mc._7_7_mc.enter_mc, wait / joris._speed)
    >>> property_diff(joris, joris.root, 'currentLabel', '_7_7')
    >>> property_diff(joris, joris.root.game_over_mc._7_7_mc.enter_mc, 'currentLabel', 'none')
    >>> property_diff(ethan, ethan.root, 'currentLabel', '_7_7')
    >>> property_diff(ethan, ethan.root.game_over_mc._7_7_mc.enter_mc, 'currentLabel', 'none')
    >>> mouse_down_and_sleep(joris, joris.root._3_2_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._3_2_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._3_3_mc, 1.0 / ethan._speed)
    >>> mouse_down_and_sleep(joris, joris.root._4_3_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._4_3_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._2_3_mc, 1.0 / ethan._speed)
    >>> mouse_down_and_sleep(joris, joris.root._4_4_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._4_4_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._2_2_mc, 1.0 / ethan._speed)
    >>> mouse_down_and_sleep(joris, joris.root._4_2_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._4_2_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._3_5_mc, 1.0 / ethan._speed)
    >>> mouse_down_and_sleep(joris, joris.root._4_5_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._4_5_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._3_4_mc, 1.0 / ethan._speed)
    >>> mouse_down_and_sleep(joris, joris.root._2_1_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._2_0_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._2_0_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._1_1_mc, 1.0 / ethan._speed)
    >>> mouse_down_and_sleep(joris, joris.root._2_1_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._2_1_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._1_0_mc, 1.0 / ethan._speed)
    >>> mouse_down_and_sleep(joris, joris.root._3_1_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._3_1_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._4_6_mc, 1.0 / ethan._speed)
    >>> mouse_down_and_sleep(joris, joris.root._5_6_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._5_6_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._3_6_mc, 1.0 / ethan._speed)
    >>> mouse_down_and_sleep(joris, joris.root._5_5_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._5_5_mc, 1.0 / joris._speed)
    '''


def live_5_5_example():
    '''See places to live on 5x5 board.
    >>> code_unit.inline_examples(
    ...     ethan_joris_start_example.__doc__, 
    ...     locals(), globals(), 
    ...     verify_examples = False)

    >>> wait = 3.0
    >>> ezra = joris # actually ethan played, but designed for ezra
    >>> gnugo = ethan
    >>> not_jump_underneath_x = ezra.root.formation_jump_underneath_mc.x
    >>> not_jump_underneath_y = ezra.root.formation_jump_underneath_mc.y

    5x5.
    >>> mouse_down_and_sleep(joris, joris.root.game_over_mc._5_5_mc.enter_mc, wait / joris._speed)
    >>> property_diff(joris, joris.root, 'currentLabel', '_5_5')
    >>> property_diff(joris, joris.root.game_over_mc._5_5_mc.enter_mc, 'currentLabel', 'none')
    >>> property_diff(ethan, ethan.root, 'currentLabel', '_5_5')
    >>> property_diff(ethan, ethan.root.game_over_mc._5_5_mc.enter_mc, 'currentLabel', 'none')

    >>> mouse_down_and_sleep(joris, joris.root._1_1_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._1_1_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._2_2_mc, wait / ethan._speed)

    EZRA SEES ETHAN PERCH.
    >>> get_response_rotate_names(joris.root.formation_perch_mc)
    ['rotate_180_mc', 'rotate_90_mc']
    >>> mouse_down_and_sleep(joris, joris.root._3_3_mc, wait / joris._speed)

    BECAUSE WHITE ATTACKED FIRST, EZRA DOES NOT SEE BLACK ATTACK DECORATION.
    >>> property_diff(ezra, ezra.root._2_3_mc.decoration_mc, 
    ...     'currentLabel', 'white_attack')
    >>> mouse_down_and_sleep(joris, joris.root._1_3_mc, wait / joris._speed)

    EZRA DOES NOT SEE JUMP UNDER.
    >>> get_response_rotate_names(ezra.root.formation_jump_underneath_mc)
    []
    >>> property_diff(ezra, ezra.root.formation_jump_underneath_mc.row_reflect_rotate_0_mc.response_mc, 
    ...     'currentLabel', 'none')
    >>> property_diff(ezra, ezra.root.formation_jump_underneath_mc, 
    ...     'x', not_jump_underneath_x)
    >>> property_diff(ezra, ezra.root.formation_jump_underneath_mc, 
    ...     'y', not_jump_underneath_y)
   
    >>> mouse_down_and_sleep(joris, joris.root._2_4_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._0_3_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._1_2_mc, wait / joris._speed)

    EZRA SEES BLOCK.
    >>> get_response_rotate_names(ezra.root.formation_block_mc)
    ['row_reflect_rotate_0_mc']
    >>> mouse_down_and_sleep(joris, joris.root._3_1_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._2_4_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._4_4_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._2_1_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._2_1_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._1_2_mc, wait / ethan._speed)

    EZRA SEES PROFIT NEUTRALIZE OPPONENT ATTACK.
    >>> property_diff(ezra, ezra.root._3_3_mc.decoration_mc, 
    ...     'currentLabel', 'white_attack')
    >>> mouse_down_and_sleep(joris, joris.root._3_2_mc, wait / joris._speed)

    EZRA SEES PROFIT NEUTRALIZE OPPONENT ATTACK.
    >>> property_diff(ezra, ezra.root._3_3_mc.decoration_mc, 
    ...     'currentLabel', 'none')

    >>> mouse_down_and_sleep(joris, joris.root._3_1_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._3_2_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._3_3_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._1_3_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._0_2_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._3_2_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._3_2_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._2_3_mc, wait / ethan._speed)
    >>> mouse_down_and_sleep(joris, joris.root._3_3_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._3_1_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._3_1_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._0_3_mc, wait / ethan._speed)
    >>> mouse_down_and_sleep(joris, joris.root._2_4_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._3_3_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._3_3_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._1_4_mc, wait / ethan._speed)
    >>> mouse_down_and_sleep(joris, joris.root._3_4_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._3_4_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._0_1_mc, wait / ethan._speed)
    >>> mouse_down_and_sleep(joris, joris.root._2_4_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._1_0_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._0_0_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._1_0_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._1_0_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._0_2_mc, wait / ethan._speed)
    >>> mouse_down_and_sleep(joris, joris.root._0_0_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._2_4_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._2_4_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._0_0_mc, wait / ethan._speed)
    '''

def gnugo_mathijs_example():
    ''' 05/16/2010 Sun 22:01
    >>> code_unit.inline_examples(
    ...     ethan_joris_start_example.__doc__, 
    ...     locals(), globals(), 
    ...     verify_examples = False)
    >>> mathijs = joris
    >>> gnugo = ethan
    >>> mouse_down_and_sleep(joris, joris.root._2_2_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._2_5_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._2_2_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._2_2_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._5_5_mc, 1.0 / ethan._speed)
    >>> mouse_down_and_sleep(joris, joris.root._6_2_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._5_2_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._5_2_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._2_4_mc, 1.0 / ethan._speed)
    >>> mouse_down_and_sleep(joris, joris.root._3_4_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._4_4_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._4_4_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._4_5_mc, 1.0 / ethan._speed)
    >>> mouse_down_and_sleep(joris, joris.root._3_5_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._3_4_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._5_4_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._6_5_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._6_4_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._7_4_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._7_4_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._2_6_mc, 1.0 / ethan._speed)
    >>> mouse_down_and_sleep(joris, joris.root._3_4_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._3_5_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._2_3_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._3_4_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._7_6_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._7_7_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._7_6_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._3_3_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._3_3_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._7_6_mc, 1.0 / ethan._speed)
    >>> mouse_down_and_sleep(joris, joris.root._6_6_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._6_5_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._6_5_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._6_6_mc, 1.0 / ethan._speed)
    >>> mouse_down_and_sleep(joris, joris.root._7_5_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._5_4_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._5_4_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._3_4_mc, 1.0 / ethan._speed)
    >>> mouse_down_and_sleep(joris, joris.root._4_2_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._1_3_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._0_4_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._0_3_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._7_5_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._4_2_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._7_5_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._7_5_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._1_3_mc, 1.0 / ethan._speed)
    >>> mouse_down_and_sleep(joris, joris.root._1_2_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._1_2_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._8_5_mc, 1.0 / ethan._speed)
    >>> mouse_down_and_sleep(joris, joris.root._8_4_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._8_4_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._8_6_mc, 1.0 / ethan._speed)
    >>> mouse_down_and_sleep(joris, joris.root._0_3_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._0_3_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._0_4_mc, 1.0 / ethan._speed)
    >>> mouse_down_and_sleep(joris, joris.root._0_2_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._0_2_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._2_3_mc, 1.0 / ethan._speed)
    >>> mouse_down_and_sleep(joris, joris.root._4_2_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._4_2_mc, 1.0 / joris._speed)
    '''

def ezra_begins_example():
    '''Ezra is disconnected on 5x5.
    example.log level 20 at Tue May 11 14:44:39 2010
    >>> code_unit.inline_examples(
    ...     ethan_joris_start_example.__doc__, 
    ...     locals(), globals(), 
    ...     verify_examples = False)

    #>>> code_unit.inline_examples(
    #...     ezra_begins_snippet.__doc__, 
    #...     locals(), globals(), 
    #...     verify_examples = False)
#def ezra_begins_snippet():

    >>> wait = 4.0
    >>> ezra = joris
    >>> gnugo = ethan

    EZRA CAN SEE TERRITORY, PROFIT, ATTACK, AND DEFEND.
    >>> property_diff(joris, joris.root.territory_mc, 'currentLabel', 'show')
    >>> property_diff(joris, joris.root.option_mc.block_mc, 'currentLabel', 'show')
    >>> property_diff(joris, joris.root.profit_mc, 'currentLabel', 'show')
    >>> property_diff(joris, joris.root.defend_mc, 'currentLabel', 'show')
    >>> property_diff(joris, joris.root.attack_mc, 'currentLabel', 'show')

    EZRA CAN SEE DECORATIONS.
    >>> property_diff(joris, joris.root.decoration_mc, 'currentLabel', 'show')

    5x5.
    >>> mouse_down_and_sleep(joris, joris.root.game_over_mc._5_5_mc.enter_mc, wait / joris._speed)
    >>> property_diff(joris, joris.root, 'currentLabel', '_5_5')
    >>> property_diff(joris, joris.root.game_over_mc._5_5_mc.enter_mc, 'currentLabel', 'none')
    >>> property_diff(ethan, ethan.root, 'currentLabel', '_5_5')
    >>> property_diff(ethan, ethan.root.game_over_mc._5_5_mc.enter_mc, 'currentLabel', 'none')

    >>> mouse_down_and_sleep(ezra, ezra.root._2_2_mc, wait / ezra._speed)
    >>> ezra.pb()
    ,,,,,
    ,,,,,
    ,,%,,
    ,,,,,
    ,,,,,

    EZRA SEES FIELD.
    >>> property_diff(ezra, ezra.root.formation_field_mc, 
    ...     'x', ezra.root['_2_2_mc'].x)
    >>> property_diff(ezra, ezra.root.formation_field_mc, 
    ...     'y', ezra.root['_2_2_mc'].y)
   
    EZRA SEES PINK STARS OVER FIELD.
    >>> property_diff(ezra, ezra.root._2_2_mc.decoration_mc, 
    ...     'currentLabel', 'none')
    >>> property_diff(ezra, ezra.root._2_1_mc.decoration_mc, 
    ...     'currentLabel', 'black_attack')
    >>> property_diff(ezra, ezra.root._3_1_mc.decoration_mc, 
    ...     'currentLabel', 'black_attack')

    >>> mouse_down_and_sleep(ezra, ezra.root._2_2_mc, wait / ezra._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._3_1_mc, wait / ethan._speed)

    EZRA SEES PURPLE STARS PINCH.
    >>> property_diff(ezra, ezra.root.formation_diagonal_attack_mc, 
    ...     'x', ezra.root['_3_1_mc'].x)
    >>> property_diff(ezra, ezra.root.formation_diagonal_attack_mc, 
    ...     'y', ezra.root['_3_1_mc'].y)
   
    EZRA SEES PINK STARS NEUTRALIZED.
    >>> property_diff(ezra, ezra.root._2_2_mc.decoration_mc, 
    ...     'currentLabel', 'none')
    >>> property_diff(ezra, ezra.root._2_1_mc.decoration_mc, 
    ...     'currentLabel', 'none')
    >>> property_diff(ezra, ezra.root._3_1_mc.decoration_mc, 
    ...     'currentLabel', 'none')
    >>> property_diff(ezra, ezra.root._3_2_mc.decoration_mc, 
    ...     'currentLabel', 'none')

    >>> mouse_down_and_sleep(ezra, ezra.root._2_0_mc, wait / ezra._speed)
    >>> ezra.pb()
    ,,,,,
    ,,,,,
    %,X,,
    ,O,,,
    ,,,,,
    >>> mouse_down_and_sleep(ezra, ezra.root._2_0_mc, wait / ezra._speed)
    >>> ezra.pb()
    ,,,,,
    ,,,,,
    X,X,,
    ,O,,,
    ,,,,,

    FOR MAKING WHITE'S PATTERN, EZRA SEES PURPLE STARS CUT THROUGH.
    >>> from pprint import pprint
    >>> if not get_response_rotate_names(ezra.root.formation_peep_mc) == ['rotate_0_mc']:
    ...     pprint(family_tree(ezra.root.formation_peep_mc))
    >>> property_diff(ezra, ezra.root.formation_peep_mc, 
    ...     'x', ezra.root['_3_1_mc'].x)
    >>> if property_diff(ezra, ezra.root.formation_peep_mc, 'y', ezra.root['_3_1_mc'].y):
    ...     ezra.root['_3_1_mc'].x, ezra.root['_3_1_mc'].y
    >>> property_diff(ezra, ezra.root._2_1_mc.decoration_mc, 
    ...     'currentLabel', 'white_attack')

    >>> mouse_down_and_sleep(ethan, ethan.root._2_1_mc, wait / ethan._speed)
    >>> ezra.pb()
    ,,,,,
    ,,,,,
    XOX,,
    ,O,,,
    ,,,,,
    
    EZRA SEES CUT FROM ETHAN.
    >>> property_diff(ezra, ezra.root.formation_cut_mc, 
    ...     'x', ezra.root['_2_1_mc'].x)
    >>> property_diff(ezra, ezra.root.formation_cut_mc, 
    ...     'y', ezra.root['_2_1_mc'].y)
    >>> property_diff(ezra, ezra.root._1_1_mc.decoration_mc, 
    ...     'currentLabel', 'white_attack')

    AT NEW STONE EZRA SEES BLUE STAR DISAPPEAR.
    >>> time.sleep(wait / ezra._speed)
    >>> property_diff(ezra, ezra.root._2_1_mc.decoration_mc, 
    ...     'currentLabel', 'none')

    >>> mouse_down_and_sleep(ezra, ezra.root._3_2_mc, wait / ezra._speed)
    >>> mouse_down_and_sleep(ezra, ezra.root._3_2_mc, wait / ezra._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._1_2_mc, wait / ethan._speed)
    >>> mouse_down_and_sleep(ezra, ezra.root._1_3_mc, wait / ezra._speed)
    >>> mouse_down_and_sleep(ezra, ezra.root._1_3_mc, wait / ezra._speed)

    EZRA SEES TIGER YAWN.
    >>> property_diff(ezra, ezra.root.formation_tiger_yawn_mc, 
    ...     'x', ezra.root['_1_3_mc'].x)
    >>> property_diff(ezra, ezra.root.formation_tiger_yawn_mc, 
    ...     'y', ezra.root['_1_3_mc'].y)

    >>> mouse_down_and_sleep(ethan, ethan.root._0_1_mc, wait / ethan._speed)
    >>> ezra.pb()
    ,O,,,
    ,,OX,
    XOX,,
    ,OX,,
    ,,,,,

    EZRA SEES TIGER MOUTH AROUND 1,1.
    >>> property_diff(ezra, ezra.root.formation_tiger_mouth_mc, 
    ...     'x', ezra.root['_0_1_mc'].x)
    >>> property_diff(ezra, ezra.root.formation_tiger_mouth_mc, 
    ...     'y', ezra.root['_0_1_mc'].y)

    #EZRA SEES FANG OVER 0,2.
    #>>> property_diff(ezra, ezra.root.formation_fang_mc, 
    #...     'x', ezra.root['_0_1_mc'].x)
    #>>> property_diff(ezra, ezra.root.formation_fang_mc, 
    #...     'y', ezra.root['_0_1_mc'].y)
    
    >>> mouse_down_and_sleep(ezra, ezra.root._4_2_mc, wait / ezra._speed)
    >>> mouse_down_and_sleep(ezra, ezra.root._4_2_mc, wait / ezra._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._0_3_mc, wait / ethan._speed)
    >>> mouse_down_and_sleep(ezra, ezra.root._0_4_mc, wait / ezra._speed)
    >>> mouse_down_and_sleep(ezra, ezra.root._0_4_mc, wait / ezra._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._1_4_mc, wait / ethan._speed)

    >>> ezra.pb()
    ,O,O,
    ,,OXO
    XOX,,
    ,OX,,
    ,,X,,

    EZRA SEES MONKEY PEEP.
    >>> from pprint import pprint
    >>> if not get_response_rotate_names(ezra.root.formation_monkey_peep_mc) == ['rotate_180_mc']:
    ...     pprint(family_tree(ezra.root.formation_monkey_peep_mc))

    EZRA SEES PINK IS IN RUINS.
    >>> property_diff(ezra, ezra.root._2_2_mc.territory_mc, 
    ...     'currentLabel', 'black_dead')

    #            HELP
    #    WE CAN DO BETTER.
    #    LET's GO BACK...

    #ARROW POINTS TO UNDO BUTTON.

    #EZRA CLICKS UNDO.

    #>>> ezra.pb()
    #,,,,,
    #,,,,,
    #$,X,,
    #,O,,,
    #,,,,,

    #            HELP
    #    WHAT IS BETTER THAN THIS?


05/11/2010 Tue 
16:26
ezra plays.

^_^ connect?  ezra guesses:  connect.
^_^ reverse peep.  ezra guesses:  connect.
^_^ after i say 'look around' ezra looks around.
^_^ after i say 'click here and you may cut twice' ezra gets the idea.
>_< ezra connects.  ezra says 'i will eat my own?'
>_< ezra clicks.  nothing happens.  crash.  restart.  ezra feels bored.  i feel embarassed.  frustrated.  
>_< start first lesson.  ezra says what do i do?
>_< divide one click per 3 seconds.  ezra watches, slouches on hand.
3>_< see and hear clock.  ezra says 'shut up'
5>_< mouse hovers over score bar.  score help appears and disappears.
>_< second lesson:  ezra watches.  
3>_< open cake.  ezra waits.  he forgets to click 'let's eat'  
>_< ezra sees candle.  he says 'why?'
>_< 5x5:  losing!  nervous chuckle.  ezra is embarrassed.
2>_< 7x7:  losing!  nervous chuckle.  ezra is embarassed.
2>_< ezra clicks on edge.  gnugo cuts in between  XOX.
>_< ezra plays to corner.  i am embarassed.
>_< ezra clicks twice quickly without considering other options.
>_< ezra clicks twice quickly.  second click is lost.
>_< sequence ends.  ezra's turn.  ezra says 'my turn?'

!^_^    replay. and mark good moves and bad moves.  animate.
!^_^    click 
!^_^    ezra suggests:  preview first stone.  next move previews second stone.  both are question marks.  

*>_<*   what was played before?
*>_<*   what size board?
*>_<*   how much time is between clicks?
*>_<*   gnugo spams clicks.

    '''


def marc_begins_example():
    ''' example.log level 20 at Thu May 20 16:20:12 2010
    >>> code_unit.inline_examples(
    ...     ethan_joris_start_example.__doc__, 
    ...     locals(), globals(), 
    ...     verify_examples = False)

    >>> wait = 4.0
    >>> marc = joris
    >>> gnugo = ethan

    _5_5 board
    >>> mouse_down_and_sleep(marc, marc.root.game_over_mc._5_5_mc.enter_mc, wait / marc._speed)
    >>> property_diff(marc, marc.root, 'currentLabel', '_5_5')
    >>> property_diff(marc, marc.root.game_over_mc._5_5_mc.enter_mc, 'currentLabel', 'none')
    >>> property_diff(gnugo, gnugo.root, 'currentLabel', '_5_5')
    >>> property_diff(gnugo, gnugo.root.game_over_mc._5_5_mc.enter_mc, 'currentLabel', 'none')
    
    >>> mouse_down_and_sleep(marc, marc.root._2_1_mc, wait / marc._speed)
    >>> mouse_down_and_sleep(marc, marc.root._2_2_mc, wait / marc._speed)
    >>> mouse_down_and_sleep(marc, marc.root._2_2_mc, wait / marc._speed)
    >>> mouse_down_and_sleep(gnugo, gnugo.root._1_2_mc, wait / gnugo._speed)
    >>> mouse_down_and_sleep(marc, marc.root._0_2_mc, wait / marc._speed)
    >>> mouse_down_and_sleep(marc, marc.root._3_1_mc, wait / marc._speed)
    >>> mouse_down_and_sleep(marc, marc.root._3_3_mc, wait / marc._speed)
    >>> mouse_down_and_sleep(marc, marc.root._3_2_mc, wait / marc._speed)
    >>> mouse_down_and_sleep(marc, marc.root._4_2_mc, wait / marc._speed)

    MARC DOES NOT SEE JUMP.
    >>> get_response_rotate_names(marc.root.formation_jump_mc)
    []

    >>> mouse_down_and_sleep(marc, marc.root._4_1_mc, wait / marc._speed)

    MARC DOES NOT SEE KNIGHT MOVE.
    >>> get_response_rotate_names(marc.root.formation_knight_mc)
    []

    >>> mouse_down_and_sleep(marc, marc.root._3_1_mc, wait / marc._speed)
    >>> mouse_down_and_sleep(marc, marc.root._3_1_mc, wait / marc._speed)
    >>> mouse_down_and_sleep(gnugo, gnugo.root._2_3_mc, wait / gnugo._speed)
    >>> mouse_down_and_sleep(marc, marc.root._2_1_mc, wait / marc._speed)
    >>> mouse_down_and_sleep(marc, marc.root._3_2_mc, wait / marc._speed)
    >>> mouse_down_and_sleep(marc, marc.root._3_3_mc, wait / marc._speed)
    >>> mouse_down_and_sleep(marc, marc.root._3_3_mc, wait / marc._speed)
    >>> mouse_down_and_sleep(gnugo, gnugo.root._1_4_mc, wait / gnugo._speed)
    >>> mouse_down_and_sleep(marc, marc.root._1_1_mc, wait / marc._speed)
    >>> mouse_down_and_sleep(marc, marc.root._1_1_mc, wait / marc._speed)
    >>> mouse_down_and_sleep(gnugo, gnugo.root._0_3_mc, wait / gnugo._speed)
    >>> mouse_down_and_sleep(marc, marc.root._2_4_mc, wait / marc._speed)
    >>> mouse_down_and_sleep(marc, marc.root._3_4_mc, wait / marc._speed)
    >>> mouse_down_and_sleep(marc, marc.root._0_1_mc, wait / marc._speed)
    >>> mouse_down_and_sleep(marc, marc.root._0_1_mc, wait / marc._speed)
    >>> mouse_down_and_sleep(gnugo, gnugo.root._0_2_mc, wait / gnugo._speed)
    >>> mouse_down_and_sleep(marc, marc.root._3_4_mc, wait / marc._speed)
    >>> mouse_down_and_sleep(marc, marc.root._3_4_mc, wait / marc._speed)
    >>> mouse_down_and_sleep(gnugo, gnugo.root._2_4_mc, wait / gnugo._speed)
    '''

def marc_extra_stone_7_7_example():
    ''' example.log level 20 at Thu May 20 16:20:12 2010
    Marc uses 4 extra stones on 7x7.  
    >>> code_unit.inline_examples(
    ...     ethan_joris_start_example.__doc__, 
    ...     locals(), globals(), 
    ...     verify_examples = False)

    >>> wait = 4.0
    >>> marc = joris
    >>> gnugo = ethan

    _7_7 board
    >>> mouse_down_and_sleep(joris, joris.root.game_over_mc._7_7_mc.enter_mc, wait / joris._speed)
    >>> property_diff(joris, joris.root, 'currentLabel', '_7_7')
    >>> property_diff(joris, joris.root.game_over_mc._7_7_mc.enter_mc, 'currentLabel', 'none')
    >>> property_diff(ethan, ethan.root, 'currentLabel', '_7_7')
    >>> property_diff(ethan, ethan.root.game_over_mc._7_7_mc.enter_mc, 'currentLabel', 'none')

    MARC SEES 3,3 IS THE HIGHEST PIECE OF CAKE.

    >>> mouse_down_and_sleep(joris, joris.root._3_3_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._3_3_mc, wait / joris._speed)


    MARC SEES CENTER OF 7X7 HAS A CROSS.
    >>> get_response_rotate_names(marc.root.formation_high_perch_mc)
    ['rotate_0']
    >>> property_diff(marc, marc.root._1_3_mc.decoration_mc, 
    ...     'currentLabel', 'black_attack')
    >>> property_diff(marc, marc.root._3_1_mc.decoration_mc, 
    ...     'currentLabel', 'black_attack')
    >>> property_diff(marc, marc.root._3_5_mc.decoration_mc, 
    ...     'currentLabel', 'black_attack')
    >>> property_diff(marc, marc.root._5_3_mc.decoration_mc, 
    ...     'currentLabel', 'black_attack')

    >>> mouse_down_and_sleep(ethan, ethan.root._4_4_mc, wait / ethan._speed)
    >>> mouse_down_and_sleep(joris, joris.root._4_3_mc, wait / joris._speed)

    MARC SEES ATTACK-DEFEND COMBO.
    >>> get_response_rotate_names(marc.root.formation_diagonal_mc)
    ['rotate_180']
    >>> get_response_rotate_names(marc.root.formation_press_mc)
    ['rotate_90']
    >>> property_diff(marc, marc.root._4_3_mc.formation_mc, 
    ...     'currentLabel', 'black_attack_defend')

    >>> mouse_down_and_sleep(joris, joris.root._5_2_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._4_2_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._5_2_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._5_2_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._3_4_mc, wait / ethan._speed)
    >>> mouse_down_and_sleep(joris, joris.root._2_4_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._3_5_mc, wait / joris._speed)

    >>> marc.pb()
    ,,,,,,,
    ,,,,,,,
    ,,,,,,,
    ,,,XO$,
    ,,,,O,,
    ,,X,,,,
    ,,,,,,,

    MARC DOES NOT KEEP HIS STONES TOGETHER.
    SO MARC SEES THAT GNUGO CUTS.
    >>> get_response_rotate_names(marc.root.formation_cut_mc)
    ['rotate_0']
    >>> property_diff(marc, marc.root._2_4_mc.decoration_mc, 
    ...     'currentLabel', 'white_attack')
    >>> property_diff(marc, marc.root._3_5_mc.formation_mc, 
    ...     'currentLabel', 'white_attack')


    >>> mouse_down_and_sleep(joris, joris.root.extra_stone_gift_mc.use_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._2_4_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._3_5_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._3_5_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._2_4_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._2_5_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._4_5_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._4_3_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._5_4_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._5_4_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._2_4_mc, wait / ethan._speed)
    >>> mouse_down_and_sleep(joris, joris.root._1_4_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._2_2_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._1_5_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._1_3_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._2_2_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._2_2_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._2_5_mc, wait / ethan._speed)
    >>> mouse_down_and_sleep(joris, joris.root.extra_stone_gift_mc.use_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._4_5_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._4_5_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._2_6_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._4_3_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._5_5_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._5_5_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._5_1_mc, wait / ethan._speed)
    >>> mouse_down_and_sleep(joris, joris.root._4_1_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root.extra_stone_gift_mc.use_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._4_1_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._4_1_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._4_2_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._6_1_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._6_1_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._4_2_mc, wait / ethan._speed)
    >>> mouse_down_and_sleep(joris, joris.root.extra_stone_gift_mc.use_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._4_3_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._4_3_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._3_2_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._3_2_mc, wait / joris._speed)
    '''



def judith_begins_example():
    '''May 22 16:30
    >>> code_unit.inline_examples(
    ...     ethan_joris_start_example.__doc__, 
    ...     locals(), globals(), 
    ...     verify_examples = False)

    >>> wait = 4.0
    >>> judith = joris
    >>> gnugo = ethan

    JUDITH CAN SEE ATTACK, AND DEFEND AND CRITICAL.
    >>> property_diff(joris, joris.root.critical_mc, 'currentLabel', 'show')
    >>> property_diff(joris, joris.root.defend_mc, 'currentLabel', 'show')
    >>> property_diff(joris, joris.root.attack_mc, 'currentLabel', 'show')

    _5_5 board
    >>> mouse_down_and_sleep(joris, joris.root.game_over_mc._5_5_mc.enter_mc, wait / joris._speed)
    >>> property_diff(joris, joris.root, 'currentLabel', '_5_5')
    >>> property_diff(joris, joris.root.game_over_mc._5_5_mc.enter_mc, 'currentLabel', 'none')
    >>> property_diff(gnugo, gnugo.root, 'currentLabel', '_5_5')
    >>> property_diff(gnugo, gnugo.root.game_over_mc._5_5_mc.enter_mc, 'currentLabel', 'none')

    >>> mouse_down_and_sleep(joris, joris.root._2_2_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._4_2_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._4_4_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._2_2_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._2_2_mc, wait / joris._speed)
    >>> property_diff(joris, joris.root._2_1_mc.decoration_mc, 'currentLabel', 'black_attack')
    >>> mouse_down_and_sleep(ethan, ethan.root._2_3_mc, wait / ethan._speed)
    >>> property_diff(joris, joris.root._2_4_mc.decoration_mc, 'currentLabel', 'none')
    >>> property_diff(joris, joris.root._1_2_mc.decoration_mc, 'currentLabel', 'none')
    >>> mouse_down_and_sleep(joris, joris.root._1_3_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._3_2_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._1_3_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._3_2_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._3_2_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._1_2_mc, wait / ethan._speed)
    >>> mouse_down_and_sleep(joris, joris.root._1_1_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._4_3_mc, wait / joris._speed)
    >>> property_diff(joris, joris.root._2_1_mc.formation_mc, 'currentLabel', 'none')
    >>> mouse_down_and_sleep(joris, joris.root._2_1_mc, wait / joris._speed)
    >>> property_diff(joris, joris.root._2_1_mc.formation_mc, 'currentLabel', 'black_attack')
    >>> mouse_down_and_sleep(joris, joris.root._2_1_mc, wait / joris._speed)
    >>> property_diff(joris, joris.root._2_1_mc.formation_mc, 'currentLabel', 'black_attack')
    >>> mouse_down_and_sleep(ethan, ethan.root._1_1_mc, wait / ethan._speed)
    >>> property_diff(joris, joris.root._1_2_mc.formation_mc, 'currentLabel', 'none')
    >>> property_diff(joris, joris.root._8_1_mc.decoration_mc, 'currentLabel', 'none')
    >>> mouse_down_and_sleep(joris, joris.root._4_4_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._1_3_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._3_3_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._3_3_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._0_3_mc, wait / ethan._speed)
    >>> mouse_down_and_sleep(joris, joris.root._2_4_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._0_1_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._4_0_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._3_0_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._1_3_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._2_4_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._2_4_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._1_4_mc, wait / ethan._speed)
    >>> mouse_down_and_sleep(joris, joris.root._1_3_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._3_4_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._3_0_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._3_1_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._3_4_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._1_3_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._3_4_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._1_3_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._1_3_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._2_3_mc, wait / ethan._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._2_0_mc, wait / ethan._speed)
    >>> mouse_down_and_sleep(joris, joris.root._3_0_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._0_0_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._1_0_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._0_4_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._2_3_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._1_0_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._3_0_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._3_0_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._2_3_mc, wait / ethan._speed)
    >>> mouse_down_and_sleep(joris, joris.root._0_2_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._4_0_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._4_3_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._4_3_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._3_4_mc, wait / ethan._speed)
    >>> property_diff(joris, joris.root._4_1_mc.vital_point_mc, 'currentLabel', 'defense_point')
    >>> mouse_down_and_sleep(joris, joris.root._3_3_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._2_4_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._1_0_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._1_0_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._4_1_mc, wait / ethan._speed)
    >>> property_diff(joris, joris.root._8_1_mc.decoration_mc, 'currentLabel', 'none')
    
    #+ >>> property_diff(joris, joris.root._2_0_mc.eye_mc, 'currentLabel', 'none')

    notes from both sessions:
    ^_^ judith plays 5x5.  i explain and advise looking at 2 or 3 moves before choosing one.  gnugo gives up.
    ^_^ at first, judith plays in the center.
    ^_^ judith says cake wedge is clear.  
    >_< judith sees purple stars.  she asks, what are they?  i say they are places you may play later.  
    >_< purple heart.  judith does not see.  i ask her to click elsewhere and click back again.  purple heart.  judith does not see.  i ask er to click elsewhere and click back again.  purple heart.
    >_< i say if you surround you take that piece.  judith sees piece on side.  it is taken.  i clarify:  if you surround on edge, then you also take.  
    >_< judith asks:  what is the candle?  i say it is a place completely surrounded.  later judith asks what is a candle?
    >_< judith looks at 2 or 3 moves.  she says it is hard to compare them.  which is better?
    >_< judith is reluctant to tap.  i say you can look at any place.  judith hesitates.
    >_< stars and hearts all over.  judith feels overwhelmed and distracted.
    >_< critical.  sometimes there is an attack in one's own color.  what is going on?
    >_< pink heart means defense?  no that one means last move made.  it is not on one place or another, but inbetween.
    >_< blue heart is upside down?  that is last move made.  it is not on one place or another, but inbetween.  that means last move made.
    >_< blue surrounds and takes vital point.  we did not see the warning.
    >_< judith consider the small corner where she takes a piece.  i say the goal is to cut out the biggest piece.  judith says
    >_< judith says he she doesn't have a brain for this kind of game.  her brother, into math, might.  
    >_< white space.  why is it white?  
    >_< gnugo gives up.  why?  the cake is not even cut yet.  
    >_< piece is taken.  judith does not see it.  she asks which piece was taken.  i point it out.  oh.  
    >_< judith says she can feel her brain hurt.  sorry.
    is it better to attack or defend?  best is both.
    empty triangle.  
    play and see critical attack of other color?  
    play on other side and see cut.
    kind of like minesweeper.
    plays on side, cutting out a piece.  but that is not enough because that piece can be surrounded.  we do not see vital point before blue takes it.  
    '''

def judith_begins_2_example():
    '''May 22 16:30
    >>> code_unit.inline_examples(
    ...     ethan_joris_start_example.__doc__, 
    ...     locals(), globals(), 
    ...     verify_examples = False)

    >>> wait = 4.0
    >>> judith = joris
    >>> gnugo = ethan

    _5_5 board
    >>> mouse_down_and_sleep(joris, joris.root.game_over_mc._5_5_mc.enter_mc, wait / joris._speed)
    >>> property_diff(joris, joris.root, 'currentLabel', '_5_5')
    >>> property_diff(joris, joris.root.game_over_mc._5_5_mc.enter_mc, 'currentLabel', 'none')
    >>> property_diff(gnugo, gnugo.root, 'currentLabel', '_5_5')
    >>> property_diff(gnugo, gnugo.root.game_over_mc._5_5_mc.enter_mc, 'currentLabel', 'none')

    >>> mouse_down_and_sleep(joris, joris.root._2_2_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._2_2_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._2_3_mc, wait / ethan._speed)
    >>> mouse_down_and_sleep(joris, joris.root._4_0_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._3_1_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._1_3_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._1_4_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._1_3_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._1_3_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._1_2_mc, wait / ethan._speed)
    >>> mouse_down_and_sleep(joris, joris.root._1_1_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._3_1_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._1_1_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._3_1_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._1_1_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._3_1_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._1_1_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._1_1_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._1_4_mc, wait / ethan._speed)
    >>> mouse_down_and_sleep(joris, joris.root._0_3_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._0_2_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._0_2_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._0_3_mc, wait / ethan._speed)
    >>> mouse_down_and_sleep(joris, joris.root._2_4_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._3_4_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._1_2_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._0_0_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._4_0_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._3_1_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._1_2_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._1_2_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._3_2_mc, wait / ethan._speed)
    >>> mouse_down_and_sleep(joris, joris.root._3_2_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._3_3_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._2_4_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._3_1_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._0_4_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._3_1_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._4_1_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._3_3_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._3_3_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._4_3_mc, wait / ethan._speed)
    >>> mouse_down_and_sleep(joris, joris.root._3_4_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._2_4_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._2_4_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._3_4_mc, wait / ethan._speed)
    >>> mouse_down_and_sleep(joris, joris.root._2_3_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._3_1_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._4_2_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._0_4_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._3_1_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._2_3_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._2_3_mc, wait / joris._speed)

    see pink hearts on edge on other side of blue.
    start again in center.
    think it will play the same this time.
    cross and see cross attack.  why is blue attack shown at 4,3?
    see purple heart to defend in corner.
    want to walk out of danger.  
    attacked by two stones at once and see critical attack point.  but for all the other information, do not realize that, and so do not play there.  
    make a fat dumpling.  still, win.
    why did gnugo give up again?  
    can we eat it all?
    '''

def make_sgf_judith_begins_example():
    '''In SGF, mark black_attack.  see sgf_judith_begins_example.
    >>> code_unit.inline_examples(
    ...     judith_begins_example.__doc__, 
    ...     locals(), globals(), 
    ...     verify_examples = False)
    >>> import shutil
    >>> shutil.copy('sgf/_gogui.sgf', 'sgf/sgf_judith_begins_example.sgf')

    Beware:  Saving all news means that if the SGF is replayed, then
    the news may overwrite the state of the game.  
    '''

def sgf_judith_begins_example():
    '''In SGF, mark black_attack.
    13  ?*^_^*  when i review decoration in gogui, how can i feel confused?
        !*^_^*  replay judith_begins_example.  
            parse SGF to history.  
            at first move, look for black_attack at 1,1.
    >>> from smart_go_format import get_history, parse
    >>> sgf_text = text.load('sgf/sgf_judith_begins_example.sgf')
    >>> sgf_tree = parse(sgf_text)
    >>> if -1 == str(sgf_tree[1]).find(';B[cc]'):
    ...     print str(sgf_tree[1])
    ...     print str(sgf_tree)
    >>> if -1 == str(sgf_tree[1]).find('MA[bb]'):
    ...     print str(sgf_tree[1])
    >>> if -1 == str(sgf_tree[1]).find('CR[aa]'):
    ...     print str(sgf_tree[1])
    '''

def michael_castle_5_5_example():
    '''Wed May 26 14:57:37 2010
    >>> code_unit.inline_examples(
    ...     ethan_joris_start_example.__doc__, 
    ...     locals(), globals(), 
    ...     verify_examples = False)

    >>> wait = 4.0
    >>> michael = joris
    >>> gnugo = ethan

    michael CAN SEE ATTACK, AND DEFEND AND CRITICAL.
    >>> property_diff(joris, joris.root.critical_mc, 'currentLabel', 'show')
    >>> property_diff(joris, joris.root.defend_mc, 'currentLabel', 'show')
    >>> property_diff(joris, joris.root.attack_mc, 'currentLabel', 'show')

    _5_5 board
    >>> mouse_down_and_sleep(joris, joris.root.game_over_mc._5_5_mc.enter_mc, wait / joris._speed)
    >>> property_diff(joris, joris.root, 'currentLabel', '_5_5')
    >>> property_diff(joris, joris.root.game_over_mc._5_5_mc.enter_mc, 'currentLabel', 'none')
    >>> property_diff(gnugo, gnugo.root, 'currentLabel', '_5_5')
    >>> property_diff(gnugo, gnugo.root.game_over_mc._5_5_mc.enter_mc, 'currentLabel', 'none')

    >>> mouse_down_and_sleep(joris, joris.root._4_1_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._1_1_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._0_1_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._0_2_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._1_3_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._2_2_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._2_2_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._1_2_mc, wait / ethan._speed)
    >>> mouse_down_and_sleep(joris, joris.root._1_1_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._1_1_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._2_1_mc, wait / ethan._speed)
    >>> mouse_down_and_sleep(joris, joris.root._0_1_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._3_1_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._3_1_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._0_1_mc, wait / ethan._speed)
    >>> mouse_down_and_sleep(joris, joris.root._1_0_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._2_0_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._2_0_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._1_0_mc, wait / ethan._speed)
    >>> mouse_down_and_sleep(joris, joris.root._2_1_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._2_1_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._1_3_mc, wait / ethan._speed)
    >>> mouse_down_and_sleep(joris, joris.root._0_0_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._2_3_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._2_3_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._2_4_mc, wait / ethan._speed)
    >>> mouse_down_and_sleep(joris, joris.root._0_3_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._3_4_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._3_4_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._1_4_mc, wait / ethan._speed)
    >>> mouse_down_and_sleep(joris, joris.root._0_0_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._0_0_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._3_3_mc, wait / ethan._speed)
    >>> mouse_down_and_sleep(joris, joris.root._0_2_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._0_2_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._3_2_mc, wait / ethan._speed)
    >>> mouse_down_and_sleep(joris, joris.root._4_3_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._0_1_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._0_1_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._4_4_mc, wait / ethan._speed)
    >>> mouse_down_and_sleep(joris, joris.root._4_2_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._4_2_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._4_3_mc, wait / ethan._speed)
    >>> mouse_down_and_sleep(joris, joris.root._4_1_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._4_1_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._3_4_mc, wait / ethan._speed)

    5x5 and 7x7 observations
    ^_^ michael wins 5x5 without an extra stone.

    ^_^ michael concentrates.
    >_< michael asks if brown is at war with white.  i say no.
    >_< i play into danger.  michael does not capture.  
    '''


def michael_castle_7_7_example():
    '''Wed May 26 14:57:37 2010
    >>> code_unit.inline_examples(
    ...     ethan_joris_start_example.__doc__, 
    ...     locals(), globals(), 
    ...     verify_examples = False)

    >>> wait = 4.0
    >>> michael = joris
    >>> gnugo = ethan

    michael CAN SEE ATTACK, AND DEFEND AND CRITICAL.
    >>> property_diff(joris, joris.root.critical_mc, 'currentLabel', 'show')
    >>> property_diff(joris, joris.root.defend_mc, 'currentLabel', 'show')
    >>> property_diff(joris, joris.root.attack_mc, 'currentLabel', 'show')

    _7_7 board
    >>> mouse_down_and_sleep(joris, joris.root.game_over_mc._7_7_mc.enter_mc, wait / joris._speed)
    >>> property_diff(joris, joris.root, 'currentLabel', '_7_7')
    >>> property_diff(joris, joris.root.game_over_mc._7_7_mc.enter_mc, 'currentLabel', 'none')
    >>> property_diff(gnugo, gnugo.root, 'currentLabel', '_7_7')
    >>> property_diff(gnugo, gnugo.root.game_over_mc._7_7_mc.enter_mc, 'currentLabel', 'none')

    >>> mouse_down_and_sleep(joris, joris.root._3_3_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._3_3_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._2_4_mc, wait / ethan._speed)
    >>> mouse_down_and_sleep(joris, joris.root._3_4_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._3_4_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._2_3_mc, wait / ethan._speed)
    >>> mouse_down_and_sleep(joris, joris.root._2_2_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._2_2_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._1_2_mc, wait / ethan._speed)
    >>> mouse_down_and_sleep(joris, joris.root._3_2_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._2_5_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._3_2_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._3_2_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._1_1_mc, wait / ethan._speed)
    >>> mouse_down_and_sleep(joris, joris.root._2_1_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._2_1_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._2_5_mc, wait / ethan._speed)
    >>> mouse_down_and_sleep(joris, joris.root._3_5_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._3_5_mc, wait / joris._speed)
    >>> property_diff(joris, joris.root._5_3_mc.territory_mc, 'currentLabel', 'black')
    >>> mouse_down_and_sleep(ethan, ethan.root._3_6_mc, wait / ethan._speed)
    >>> michael.pb()
    ,,,,,,,
    ,OO,,,,
    ,XXOOO,
    ,,XXXXO
    ,,,,,,,
    ,,,,,,,
    ,,,,,,,

    MICHAEL SEES TERRITORY DISAPPEAR.
    >>> property_diff(joris, joris.root._5_3_mc.territory_mc, 'currentLabel', 'neutral')

    MICHAEL SEES THREAT OF MONKEY HOP.
    >>> property_diff(joris, joris.root._5_6_mc.top_move_mc, 'currentLabel', 'white')

    >>> mouse_down_and_sleep(joris, joris.root._1_0_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._1_0_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._5_6_mc, wait / ethan._speed)

    MICHAEL SEES THREAT OF MONKEY HOP DISAPPEAR.
    >>> property_diff(joris, joris.root._5_6_mc.top_move_mc, 'currentLabel', 'none')

    >>> mouse_down_and_sleep(joris, joris.root._4_6_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root.extra_stone_gift_mc.use_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._2_6_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._2_6_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._1_6_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._1_6_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._4_6_mc, wait / ethan._speed)
    >>> mouse_down_and_sleep(joris, joris.root._4_5_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._4_5_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._5_5_mc, wait / ethan._speed)
    >>> mouse_down_and_sleep(joris, joris.root._1_4_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._1_4_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._1_3_mc, wait / ethan._speed)
    >>> mouse_down_and_sleep(joris, joris.root._0_3_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._0_3_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._1_5_mc, wait / ethan._speed)
    >>> mouse_down_and_sleep(joris, joris.root._0_4_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._0_4_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._5_4_mc, wait / ethan._speed)
    >>> mouse_down_and_sleep(joris, joris.root.extra_stone_gift_mc.use_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._5_3_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._5_3_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._4_3_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._6_3_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._4_3_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._4_3_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._6_3_mc, wait / ethan._speed)
    >>> mouse_down_and_sleep(joris, joris.root._6_2_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._6_2_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._6_4_mc, wait / ethan._speed)
    >>> mouse_down_and_sleep(joris, joris.root.extra_stone_gift_mc.use_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._0_6_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._0_1_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._0_1_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._5_2_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._5_2_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._0_5_mc, wait / ethan._speed)
    >>> mouse_down_and_sleep(joris, joris.root.extra_stone_gift_mc.use_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._0_0_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._6_5_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._4_4_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._4_4_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._2_0_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._2_0_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._0_2_mc, wait / ethan._speed)
    >>> mouse_down_and_sleep(joris, joris.root._1_4_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._0_6_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._4_2_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._4_2_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._0_0_mc, wait / ethan._speed)
    >>> mouse_down_and_sleep(joris, joris.root._0_1_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._0_1_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._3_0_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._3_0_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._0_1_mc, wait / ethan._speed)
    >>> import shutil
    >>> shutil.copy('sgf/_gogui.sgf', 'sgf/michael_castle_7_7_example.sgf')

    ^_^    michael builds a wall connected to his own and adjacent to enemy and blocking enemy.  i feel a little kevelt(sp?), proud of his behavior.
    ^_^    remind michael that can use extra stone.  michael uses them.
    >_< michael clicks.  click 0.5 seconds later.  no response.  frustrated.  hunch shoulders.
    >_< white turns corner of first line.  michael sees nothing and ignores.  white monkey hops.
    >_< gnugo invades michael at edge.  i am disappointed.
    >_< michael could use extra stone to capture.  michael does not.  i am disappointed.
    >_< when using extra stone, michael could play to capture at 4,6.  he does not.  he loses side and feels flustered.
    >_< i am not sure, but michael might have been playing wiser on cake take theme.  
    ^_^ michael starts in center.
    >_< why does 2,5 protect?
    ^_^ michael protects second line
    >_< michael tries to surround in capture race in which he is behind.
    >_< michael has one stone in corner in danger.  he fills in his own field instead of saving it.  
    >_< michael previews block.  see shields if blocking above rather than below, but already  well protected?
    '''


def marc_castle_5_5_example():
    '''Wed May 26 14:57:37 2010
    >>> code_unit.inline_examples(
    ...     ethan_joris_start_example.__doc__, 
    ...     locals(), globals(), 
    ...     verify_examples = False)

    >>> wait = 4.0
    >>> marc = joris
    >>> gnugo = ethan

    marc CAN SEE ATTACK, AND DEFEND AND CRITICAL.
    >>> property_diff(joris, joris.root.critical_mc, 'currentLabel', 'show')
    >>> property_diff(joris, joris.root.defend_mc, 'currentLabel', 'show')
    >>> property_diff(joris, joris.root.attack_mc, 'currentLabel', 'show')

    _5_5 board
    >>> mouse_down_and_sleep(joris, joris.root.game_over_mc._5_5_mc.enter_mc, wait / joris._speed)
    >>> property_diff(joris, joris.root, 'currentLabel', '_5_5')
    >>> property_diff(joris, joris.root.game_over_mc._5_5_mc.enter_mc, 'currentLabel', 'none')
    >>> property_diff(gnugo, gnugo.root, 'currentLabel', '_5_5')
    >>> property_diff(gnugo, gnugo.root.game_over_mc._5_5_mc.enter_mc, 'currentLabel', 'none')

    >>> mouse_down_and_sleep(joris, joris.root._2_2_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._2_2_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._1_2_mc, wait / ethan._speed)
    >>> mouse_down_and_sleep(joris, joris.root._1_1_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._3_2_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._2_3_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._1_3_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._1_3_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._2_3_mc, wait / ethan._speed)
    >>> mouse_down_and_sleep(joris, joris.root.extra_stone_gift_mc.use_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._3_3_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._3_3_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._1_1_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._1_1_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._2_1_mc, wait / ethan._speed)
    >>> mouse_down_and_sleep(joris, joris.root.extra_stone_gift_mc.use_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._3_2_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._3_2_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._3_1_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._3_1_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._0_3_mc, wait / ethan._speed)
    >>> mouse_down_and_sleep(joris, joris.root.extra_stone_gift_mc.use_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._1_4_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._1_4_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._2_4_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._2_4_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._0_1_mc, wait / ethan._speed)
    >>> mouse_down_and_sleep(joris, joris.root.extra_stone_gift_mc.use_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._1_0_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._1_0_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._2_0_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._2_0_mc, wait / joris._speed)
    >>> import shutil
    >>> shutil.copy('sgf/_gogui.sgf', 'sgf/marc_castle_5_5_example.sgf')

    ^_^ marc dominates 5x5.
    ^_^ marc says he likes the themes.
    >_< marc uses extra stone each turn.  too easy.
    >_< marc ignores big black shields.
    >_< marc sees red critical and black shield.  he does not play at black shield.  
    '''



def stephen_castle_3_3_example():
    '''Wed May 26 14:57:37 2010
    >>> code_unit.inline_examples(
    ...     ethan_joris_start_example.__doc__, 
    ...     locals(), globals(), 
    ...     verify_examples = False)

    >>> wait = 4.0
    >>> stephen = joris
    >>> designer = ethan

    stephen CAN SEE ATTACK, AND DEFEND AND CRITICAL and CONNECTED.
    >>> property_diff(joris, joris.root.critical_mc, 'currentLabel', 'show')
    >>> property_diff(joris, joris.root.defend_mc, 'currentLabel', 'show')
    >>> property_diff(joris, joris.root.attack_mc, 'currentLabel', 'show')
    >>> property_diff(joris, joris.root.connected_mc, 'currentLabel', 'show')

    _3_3 board
    >>> mouse_down_and_sleep(joris, joris.root.game_over_mc._3_3_mc.enter_mc, wait / joris._speed)
    >>> property_diff(joris, joris.root, 'currentLabel', '_3_3')
    >>> property_diff(joris, joris.root.game_over_mc._3_3_mc.enter_mc, 'currentLabel', 'none')
    >>> property_diff(ethan, ethan.root, 'currentLabel', '_3_3')
    >>> property_diff(ethan, ethan.root.game_over_mc._3_3_mc.enter_mc, 'currentLabel', 'none')
    
    >>> mouse_down_and_sleep(joris, joris.root._1_1_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._1_1_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._0_1_mc, wait / ethan._speed)
    >>> mouse_down_and_sleep(joris, joris.root._0_2_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._0_0_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._1_0_mc, wait / joris._speed)

    Stephen sees his stones are connected.
    >>> property_diff(joris, joris.root._1_0_mc.black_shape_mc, 'currentLabel', '_0100')
    >>> property_diff(joris, joris.root._1_1_mc.black_shape_mc, 'currentLabel', '_0001')
    >>> mouse_down_and_sleep(joris, joris.root._1_0_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._1_2_mc, wait / ethan._speed)
    >>> mouse_down_and_sleep(joris, joris.root._2_2_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._2_1_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._2_1_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._0_2_mc, wait / ethan._speed)

    White does not see his stones are connected.
    >>> property_diff(ethan, ethan.root._0_2_mc.white_shape_mc, 'currentLabel', '_0000')
    
    >>> mouse_down_and_sleep(joris, joris.root._2_0_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._0_0_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._0_0_mc, wait / joris._speed)

    >>> import shutil
    >>> shutil.copy('sgf/_gogui.sgf', 'sgf/stephen_castle_3_3_example.sgf')
    '''


def stephen_castle_5_5_example():
    '''Wed May 26 14:57:37 2010
    >>> code_unit.inline_examples(
    ...     ethan_joris_start_example.__doc__, 
    ...     locals(), globals(), 
    ...     verify_examples = False)

    >>> wait = 4.0
    >>> stephen = joris
    >>> gnugo = ethan

    stephen CAN SEE ATTACK, AND DEFEND AND CRITICAL.
    >>> property_diff(joris, joris.root.critical_mc, 'currentLabel', 'show')
    >>> property_diff(joris, joris.root.defend_mc, 'currentLabel', 'show')
    >>> property_diff(joris, joris.root.attack_mc, 'currentLabel', 'show')

    _5_5 board
    >>> mouse_down_and_sleep(joris, joris.root.game_over_mc._5_5_mc.enter_mc, wait / joris._speed)
    >>> property_diff(joris, joris.root, 'currentLabel', '_5_5')
    >>> property_diff(joris, joris.root.game_over_mc._5_5_mc.enter_mc, 'currentLabel', 'none')
    >>> property_diff(gnugo, gnugo.root, 'currentLabel', '_5_5')
    >>> property_diff(gnugo, gnugo.root.game_over_mc._5_5_mc.enter_mc, 'currentLabel', 'none')

    >>> mouse_down_and_sleep(joris, joris.root._2_2_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._2_2_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._2_1_mc, wait / ethan._speed)
    >>> mouse_down_and_sleep(joris, joris.root._0_2_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._1_2_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._1_2_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._3_2_mc, wait / ethan._speed)
    >>> mouse_down_and_sleep(joris, joris.root._3_4_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._2_3_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._2_4_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._1_4_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._1_3_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._1_3_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._1_1_mc, wait / ethan._speed)
    >>> mouse_down_and_sleep(joris, joris.root._3_3_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._3_3_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._3_0_mc, wait / ethan._speed)
    >>> mouse_down_and_sleep(joris, joris.root._0_1_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._4_2_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._0_1_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._0_1_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._4_1_mc, wait / ethan._speed)
    >>> mouse_down_and_sleep(joris, joris.root._1_0_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._4_3_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._0_0_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._4_3_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._4_3_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._1_0_mc, wait / ethan._speed)
    >>> mouse_down_and_sleep(joris, joris.root._0_0_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._4_2_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._4_2_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._3_1_mc, wait / ethan._speed)
    >>> mouse_down_and_sleep(joris, joris.root._0_2_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._0_2_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._0_0_mc, wait / ethan._speed)
    >>> mouse_down_and_sleep(joris, joris.root._2_3_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._2_3_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._0_4_mc, wait / ethan._speed)
    >>> mouse_down_and_sleep(joris, joris.root._1_4_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._1_4_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._3_4_mc, wait / ethan._speed)
    >>> mouse_down_and_sleep(joris, joris.root._4_4_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._4_4_mc, wait / joris._speed)

    >>> import shutil
    >>> shutil.copy('sgf/_gogui.sgf', 'sgf/stephen_castle_5_5_example.sgf')

    ^_^ stephen start in center.
    ^_^ stephen end by connecting his castle.
    >_< do not see some yellow sword.
    >_< stephen ask:  what do symbols mean?  various swords?
    >_<   was territory to none animation too quick?  how about getting territory animation?  
    >_<  what do tints over green mean?  height levels.  
    '''



def joris_castle_3_3_example():
    '''Wed May 26 14:57:37 2010
    >>> code_unit.inline_examples(
    ...     ethan_joris_start_example.__doc__, 
    ...     locals(), globals(), 
    ...     verify_examples = False)

    >>> wait = 4.0
    >>> joris = joris
    >>> designer = ethan

    joris CAN SEE ATTACK, AND DEFEND AND CRITICAL.
    >>> property_diff(joris, joris.root.critical_mc, 'currentLabel', 'show')
    >>> property_diff(joris, joris.root.defend_mc, 'currentLabel', 'show')
    >>> property_diff(joris, joris.root.attack_mc, 'currentLabel', 'show')

    _3_3 board
    >>> mouse_down_and_sleep(joris, joris.root.game_over_mc._3_3_mc.enter_mc, wait / joris._speed)
    >>> property_diff(joris, joris.root, 'currentLabel', '_3_3')
    >>> property_diff(joris, joris.root.game_over_mc._3_3_mc.enter_mc, 'currentLabel', 'none')
    >>> property_diff(gnugo, gnugo.root, 'currentLabel', '_3_3')
    >>> property_diff(gnugo, gnugo.root.game_over_mc._3_3_mc.enter_mc, 'currentLabel', 'none')
    
    >>> mouse_down_and_sleep(joris, joris.root._1_1_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._1_1_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._0_0_mc, wait / ethan._speed)
    >>> mouse_down_and_sleep(joris, joris.root._0_1_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._2_0_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._0_1_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._0_1_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._1_2_mc, wait / ethan._speed)
    >>> mouse_down_and_sleep(joris, joris.root._1_0_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._1_0_mc, wait / joris._speed)

    >>> import shutil
    >>> shutil.copy('sgf/_gogui.sgf', 'sgf/joris_castle_3_3_example.sgf')
    '''


def joris_castle_5_5_example():
    '''Wed May 26 14:57:37 2010
    >>> code_unit.inline_examples(
    ...     ethan_joris_start_example.__doc__, 
    ...     locals(), globals(), 
    ...     verify_examples = False)

    >>> wait = 4.0
    >>> joris = joris
    >>> gnugo = ethan

    joris CAN SEE ATTACK, AND DEFEND AND CRITICAL.
    >>> property_diff(joris, joris.root.critical_mc, 'currentLabel', 'show')
    >>> property_diff(joris, joris.root.defend_mc, 'currentLabel', 'show')
    >>> property_diff(joris, joris.root.attack_mc, 'currentLabel', 'show')

    _5_5 board
    >>> mouse_down_and_sleep(joris, joris.root.game_over_mc._5_5_mc.enter_mc, wait / joris._speed)
    >>> property_diff(joris, joris.root, 'currentLabel', '_5_5')
    >>> property_diff(joris, joris.root.game_over_mc._5_5_mc.enter_mc, 'currentLabel', 'none')
    >>> property_diff(gnugo, gnugo.root, 'currentLabel', '_5_5')
    >>> property_diff(gnugo, gnugo.root.game_over_mc._5_5_mc.enter_mc, 'currentLabel', 'none')

    >>> mouse_down_and_sleep(joris, joris.root._2_2_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._2_2_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._2_1_mc, wait / ethan._speed)
    >>> mouse_down_and_sleep(joris, joris.root._1_1_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._1_1_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._1_2_mc, wait / ethan._speed)
    >>> mouse_down_and_sleep(joris, joris.root._1_3_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._1_3_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._1_0_mc, wait / ethan._speed)
    >>> mouse_down_and_sleep(joris, joris.root._0_2_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._0_2_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._0_1_mc, wait / ethan._speed)
    >>> mouse_down_and_sleep(joris, joris.root._0_0_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._0_0_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._3_2_mc, wait / ethan._speed)
    >>> mouse_down_and_sleep(joris, joris.root._2_0_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._2_0_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._2_3_mc, wait / ethan._speed)
    >>> mouse_down_and_sleep(joris, joris.root._3_1_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._3_1_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._1_4_mc, wait / ethan._speed)
    >>> mouse_down_and_sleep(joris, joris.root._0_3_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._0_3_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._4_2_mc, wait / ethan._speed)
    >>> mouse_down_and_sleep(joris, joris.root._4_1_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._4_1_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._3_4_mc, wait / ethan._speed)
    >>> mouse_down_and_sleep(joris, joris.root._0_4_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._0_4_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._4_3_mc, wait / ethan._speed)
    >>> mouse_down_and_sleep(joris, joris.root._2_4_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._2_4_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._3_3_mc, wait / ethan._speed)
    >>> mouse_down_and_sleep(joris, joris.root._4_4_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._4_4_mc, wait / joris._speed)

    >>> import shutil
    >>> shutil.copy('sgf/_gogui.sgf', 'sgf/joris_castle_5_5_example.sgf')

    '''



def emmet_capture_3_3_example():
    '''
    CASTLE KING

    INT. THRONE ROOM, MOUNTAIN PALACE - DAY

    HUMAN PRINCE WITH SCROLL AND PEN SKETCH OF CASTLE.
    ASIAN BLACK DRAGON ENTERS.
    BLACK DRAGON LAYS OUT MAPS.
    
                MAPS
        3X3 HIGH PASS
        5x5 SPRING VILLAGE (GRAY)
        3X3 LOW PASS (GRAY)
        5x5 SUMMER VILLAGE (GRAY)
    
                PRINCE EMMET
        KING OF DRAGONS?

                BLACK DRAGON
        THE ICE LORD IS SENDING HIS WAR MACHINES TO CONQUER OUR LAND.  
        PRINCE EMMET, YOU ARE THE MASTER OF CASTLES.  
        I NEED YOUR HELP AT HIGH PASS!
        
    BIG ARROW BOUNCES ON TOP OF HIGH PASS.

    [IF EMMET CLICKS 3X3 HIGH PASS, CONTINUE.]

    EXT. 3X3 HIGH PASS - DAY

    #>>> code_unit.inline_examples(
    #...     ethan_joris_start_example.__doc__, 
    #...     locals(), globals(), 
    #...     verify_examples = False)
    >>> code_unit.inline_examples(
    ...     ethan_lukasz_begin_example.__doc__, 
    ...     locals(), globals(), 
    ...     verify_examples = False)

    >>> wait = 5.0 / black._speed
    >>> emmet = black
    >>> designer = white
    >>> mouse_down_and_sleep(black, black.root.lobby_mc._00_mc.capture_3_3_mc,
    ...     wait)


    #_3_3 board
    #>>> mouse_down_and_sleep(black, black.root.game_over_mc._3_3_mc.enter_mc, wait)
    #>>> property_diff(black, black.root, 'currentLabel', '_3_3')
    #>>> property_diff(black, black.root.game_over_mc._3_3_mc.enter_mc, 'currentLabel', 'none')
    #>>> property_diff(white, white.root, 'currentLabel', '_3_3')
    #>>> property_diff(white, white.root.game_over_mc._3_3_mc.enter_mc, 'currentLabel', 'none')
    
    FIRST CAPTURE AT HIGH PASS

    3X3 HILL IN MOUNTAINS.  
    CENTER IS BRIGHT GREEN.  SIDES ARE MUTED GREEN.

                PRINCE EMMET
        A CASTLE MUST TOUCH GREEN FARMLAND FOR FOOD.
        OR ELSE THE ENEMY WILL DESTROY THE CASTLE.

                BLACK DRAGON
        THIS LAND HAS HOLY RELICS, SO:
        DO NOT LET THE ICE LORD SURROUND EVEN ONE OF OUR CASTLES!  

    EMMET CLICKS ON START BUTTON.
    >>> mouse_down_and_sleep(black, black.root.game_over_mc.start_mc, wait)


    EMMET CAN SEE STRIKE, NOT TERRITORY OR SUICIDE.  NOT SCORE.  
    >>> property_diff(black, black.root.strike_mc, 'currentLabel', 'show')
    >>> property_diff(black, black.root.territory_mc, 'currentLabel', 'none')
    >>> property_diff(black, black.root.suicide_mc, 'currentLabel', 'none')
    >>> property_diff(black, black.root.option_mc.score_mc, 'currentLabel', 'none')
    >>> property_diff(black, black.root.option_mc.block_mc, 'currentLabel', 'show')
    >>> property_diff(black, black.root.score_mc, 'currentLabel', 'none')

    EMMET MAY WIN BY FIRST CAPTURE.
    >>> property_diff(black, black.root.option_mc.first_capture_mc, 'currentLabel', 'show')

    FOR REPLAY, COMPUTER IS NOT PLAYING.
    >>> mouse_down_and_sleep(black, black.root.game_over_mc.white_computer_mc.enter_mc, wait)
    >>> property_diff(black, black.root.game_over_mc.white_computer_mc, 'currentLabel', 'none')

    >>> mouse_down_and_sleep(black, black.root._0_1_mc, wait)

    CATAPULT ATTACKS FROM NORTH.
    >>> property_diff(black, black.root._0_1_strike_mc.north_mc, 'currentLabel', 'black_notice_retaliate')

                BLACK DRAGON
        FROM THE MOUNTAINS, ANYBODY CAN ATTACK, SO:
        DO NOT BUILD YOUR FIRST CASTLE BESIDE A MOUNTAIN.
        THERE IS A BETTER PLACE.  CAN YOU FIND IT?

    EMMET CLICKS "?" ANYWAY.  HE SEES NO PREVIEW.
    >>> mouse_down_and_sleep(black, black.root._0_1_mc, wait)
    >>> black.pb()
    ,,,
    ,,,
    ,,,

    HE SEES EXPLANATION
    >>> if not black.root.comment_mc._txt.text.startswith('THERE IS'):
    ...     black.root.comment_mc._txt.text

    >>> mouse_down_and_sleep(black, black.root._1_1_mc, wait)
    >>> black.pb()
    ,,,
    ,%,
    ,,,

    CATAPULT DOES NOT REATTACK OR APPEAR.
    EMMET DOES NOT HEAR OR SEE STRIKE.
    >>> property_diff(black, black.root._0_1_strike_mc.north_mc, 'currentLabel', 'none')

    >>> property_diff(black, black.root._0_1_mc.decoration_mc, 'currentLabel', 'black_defend')

    >>> mouse_down_and_sleep(black, black.root._0_0_mc, wait)
    >>> black.pb()
    %,,
    ,,,
    ,,,

    TWO WHITE CATAPULTS ATTACK FROM MOUNTAINS.
    >>> property_diff(black, black.root._0_0_strike_mc.north_mc, 'currentLabel', 'black_warning_retaliate')
    >>> property_diff(black, black.root._0_0_strike_mc.west_mc, 'currentLabel', 'black_warning_retaliate')
    >>> property_diff(black, black.root._0_0_mc.block_west_mc, 'currentLabel', 'black_warning')

    PREVIOUS CATAPULT DOES NOT REATTACK OR APPEAR.
    >>> property_diff(black, black.root._0_1_strike_mc.north_mc, 'currentLabel', 'none')

                BLACK DRAGON
        ONLY TWO ROADS LEFT!  WE ARE CLOSE TO STARVING.
        ICE LORD ATTACKS US FROM TWO MOUNTAINS!

    EMMET CLICKS QUICKLY TO 0,1, THEN BEFORE SERVER CAN REPLY, HE CLICKS 1,1.
    >>> mouse_down_and_sleep(black, black.root._0_1_mc, 0.05 * wait)
    >>> black.pb()
    ,$,
    ,,,
    ,,,

    #ONE WHITE CATAPULT ATTACKS FROM MOUNTAIN.
    #WAGON SLOWLY HAULS ON THREE GREEN ROADS.
    #>>> property_diff(black, black.root._0_1_strike_mc.north_mc, 'currentLabel', 'black_notice_retaliate')

    #PREVIOUS CATAPULT DOES NOT REATTACK OR APPEAR.
    #>>> property_diff(black, black.root._0_0_strike_mc.north_mc, 'currentLabel', 'none')
    #>>> property_diff(black, black.root._0_0_strike_mc.west_mc, 'currentLabel', 'none')

                BLACK DRAGON
        ONLY THREE ROADS LEFT!  THAT IS DANGEROUS.
        ICE LORD ATTACKS US FROM A MOUNTAIN!

    BEFORE SERVER REPLIES TO FIRST REQUEST, PREVIOUS PREVIEW REVERTS.  
    >>> mouse_down_and_sleep(black, black.root._1_1_mc, 0.05 * wait)
    >>> black.pb()
    ,,,
    ,$,
    ,,,
    >>> time.sleep(2 * wait)
    >>> black.pb()
    ,,,
    ,%,
    ,,,

                BLACK DRAGON
        YES!  THE CENTER IS FREE TO ATTACK ALL SIDES.
        TO BUILD THAT CASTLE, CLICK "?"

    EMMET CLICKS "?"
    >>> mouse_down_and_sleep(black, black.root._1_1_mc, wait)
    >>> black.pb()
    ,,,
    ,X,
    ,,,
    >>> if not black.root.comment_mc._txt.text.startswith('PERFECT'):
    ...     black.root.comment_mc._txt.text

    ICE LORD BUILDS HIS FIRST CASTLE.
    >>> mouse_down_and_sleep(white, white.root._0_1_mc, wait)
    >>> black.pb()
    ,O,
    ,X,
    ,,,

    BLACK CATAPULTS ATTACK WHITE CASTLE FROM MOUNTAIN AND EMMET'S CASTLE.
    TWO WAGONS QUICKLY HAUL ON TWO YELLOW ROADS.

                BLACK DRAGON
        TO SURVIVE, BUILD BESIDE TWO FARMS.
        AFTER THAT, TO CAPTURE AN ICE LORD:
        BUILD ON ALL THE FARMS BESIDE ANY WHITE CASTLE.  

    >>> mouse_down_and_sleep(black, black.root._2_1_mc, wait)
    >>> black.pb()
    ,O,
    ,X,
    ,%,
    >>> mouse_down_and_sleep(black, black.root._2_1_mc, wait)
    >>> black.pb()
    ,O,
    ,X,
    ,X,
    >>> mouse_down_and_sleep(white, white.root._1_2_mc, wait)
    >>> mouse_down_and_sleep(black, black.root._0_0_mc, wait)

    EMMET DOES NOT TRY 0,2, BUT SUPPOSE HE DOES.
    >>> mouse_down_and_sleep(black, black.root._0_2_mc, wait)

    EMMET SEES WHITE STRIKE TO CAPTURE, AND RECEIVES HELP. 
    >>> property_diff(black, black.root._0_2_strike_mc.north_mc, 'currentLabel', 'black_capture_retaliate')
    >>> property_diff(black, black.root.help_mc, 'currentLabel', 'suicide')

    >>> mouse_down_and_sleep(black, black.root._1_0_mc, wait)
    >>> mouse_down_and_sleep(black, black.root._1_0_mc, wait)
    >>> mouse_down_and_sleep(white, white.root._0_0_mc, wait)

    EMMET SEES CATAPULTS.  ETHAN DOES NOT.
    >>> property_diff(black, black.root._0_1_strike_mc.north_mc, 'currentLabel', 'white_danger_retaliate')
    >>> property_diff(black, black.root._0_1_strike_mc.south_mc, 'currentLabel', 'white_danger_retaliate')
    >>> property_diff(white, white.root._0_1_strike_mc.north_mc, 'currentLabel', 'none')
    >>> property_diff(white, white.root._0_1_strike_mc.south_mc, 'currentLabel', 'none')

    >>> black.pb()
    OO,
    XXO
    ,X,

    >>> mouse_down_and_sleep(black, black.root._2_2_mc, wait)

    verify option_mc.prohibit_danger_mc
    >>> property_diff(black, black.root.option_mc.prohibit_danger_mc, 'currentLabel', 'show')

    preview danger.  do not see comment, do see preview.
    >>> black.pb()
    OO,
    XXO
    ,X%
    >>> if black.root.comment_mc._txt.text.startswith('WE WOULD BE SURROUNDED'):
    ...     black.root.comment_mc._txt.text

    click elsewhere.  preview elsewhere.
    >>> mouse_down_and_sleep(black, black.root._2_0_mc, wait)

    emmet no longer sees last previewed strike.
    >>> property_diff(black, black.root._0_1_strike_mc.east_mc, 'currentLabel', 'none')
    >>> property_diff(black, black.root._0_2_strike_mc.west_mc, 'currentLabel', 'none')
    >>> property_diff(black, black.root._0_2_strike_mc.south_mc, 'currentLabel', 'none')
    >>> property_diff(black, black.root._0_2_strike_mc.east_mc, 'currentLabel', 'none')
    >>> property_diff(black, black.root._0_2_strike_mc.north_mc, 'currentLabel', 'none')

    click in danger and click again.  see comment.
    >>> black.pb()
    OO,
    XXO
    %X,
    >>> black.root._2_0_mc.currentLabel
    'question_black'
    >>> mouse_down_and_sleep(black, black.root._2_0_mc, wait)

    pretend 
    >>> # black.root.comment_mc._txt.text = 'WE WOULD BE SURROUNDED! TRY ANOTHER PLACE.' # pretend
    >>> # black.root.comment_mc.gotoAndPlay('comment') # pretend
    >>> # black.root._2_0_mc.gotoAndPlay('empty_black') # pretend
    >>> # set_property(black, black.root.comment_mc._txt, 'text', 'WE WOULD BE SURROUNDED! TRY ANOTHER PLACE.') # pretend
    >>> # set_property(black, black.root.comment_mc, 'currentLabel', 'comment') # pretend
    >>> # set_property(black, black.root._2_0_mc, 'currentLabel', 'empty_black') # pretend

    >>> if not black.root.comment_mc._txt.text.startswith('WE WOULD BE SURROUNDED'):
    ...     black.root.comment_mc._txt.text
    >>> black.root._2_0_mc.currentLabel
    u'empty_black'
    >>> black.root.comment_mc.currentLabel
    'comment'
    
    >>> black.pb()
    OO,
    XXO
    ,X,
    >>> mouse_down_and_sleep(black, black.root._0_2_mc, wait)

    #+ image of castle remains until strike animation completes.
    >>> black.pb()
    ,,%
    XXO
    ,X,
    >>> black.ambassador.receives[-1].get('_0_1_strike_mc').get('west_mc')

    DURING PREVIEW, EMMET DOES NOT SEE WIN.
    >>> property_diff(black, black.root._0_2_mc, 'currentLabel', 'question_black')
    >>> property_diff(black, black.root.game_over_mc, 'currentLabel', 'none')

    EMMET SEES STRIKE TO KILL NORTHWEST AND STRIKE OF DANGER IN SOUTHEAST.
    >>> property_diff(black, black.root._0_1_strike_mc.east_mc, 'currentLabel', 'white_capture')
    >>> property_diff(black, black.root._0_1_strike_mc.north_mc, 'currentLabel', 'white_capture')
    >>> property_diff(black, black.root._0_1_strike_mc.south_mc, 'currentLabel', 'white_capture')
    >>> property_diff(black, black.root._0_1_strike_mc.west_mc, 'currentLabel', 'none')
    >>> property_diff(black, black.root._0_2_strike_mc.west_mc, 'currentLabel', 'none')

    SINCE SOUTHEAST SURVIVES STRIKE, EMMET SEES RETALIATION STRIKE.
    >>> property_diff(black, black.root._1_2_strike_mc.north_mc, 'currentLabel', 'white_danger')
    >>> property_diff(black, black.root._1_2_strike_mc.east_mc, 'currentLabel', 'white_danger')
    >>> property_diff(black, black.root._1_2_strike_mc.west_mc, 'currentLabel', 'white_danger')
    >>> property_diff(black, black.root._0_2_strike_mc.north_mc, 'currentLabel', 'black_danger_retaliate')
    >>> property_diff(black, black.root._0_2_strike_mc.east_mc, 'currentLabel', 'black_danger_retaliate')
    >>> property_diff(black, black.root._0_2_strike_mc.south_mc, 'currentLabel', 'black_danger_retaliate')

    SINCE EMMET CAN SEE REMAINS, EMMET SEES WHITE CASTLE DEMOLISHED, AND RUINS OF WHITE CASTLE.  ETHAN DOES NOT.
    >>> property_diff(black, black.root.option_mc.gibs_mc, 'currentLabel', 'show')
    >>> property_diff(black, black.root._0_1_mc.gibs_mc, 'currentLabel', 'white')
    >>> property_diff(white, white.root._0_1_mc.gibs_mc, 'currentLabel', 'none')

    #+ EMMET SEES WHITE REPAIR.
    #+ >>> property_diff(black, black.root._1_2_strike_mc.south_mc, 'currentLabel', 'white_repair_danger')

    strike labels:
    none
    black_capture
    black_danger
    black_warning
    black_notice
    white_capture
    white_danger
    white_warning
    white_notice

    #+ user can click to skip strike animation.
    #+ user can click option enable/disable strike animation.
    
    >>> mouse_down_and_sleep(black, black.root._0_2_mc, wait)
    >>> black.pb()
    ,,X
    XXO
    ,X,
    >>> black.ambassador.receives[-1].get('_0_1_strike_mc').get('west_mc')

    EMMET SEES STRIKE TO KILL NORTHWEST AND STRIKE OF DANGER IN SOUTHEAST.
    >>> property_diff(black, black.root._0_1_strike_mc.east_mc, 'currentLabel', 'white_capture')
    >>> property_diff(black, black.root._0_1_strike_mc.north_mc, 'currentLabel', 'white_capture')
    >>> property_diff(black, black.root._0_1_strike_mc.south_mc, 'currentLabel', 'white_capture')
    >>> property_diff(black, black.root._0_1_strike_mc.west_mc, 'currentLabel', 'none')
    >>> property_diff(black, black.root._0_2_strike_mc.west_mc, 'currentLabel', 'none')

    SINCE SOUTHEAST SURVIVES STRIKE, EMMET SEES RETALIATION STRIKE.
    >>> property_diff(black, black.root._1_2_strike_mc.north_mc, 'currentLabel', 'white_danger')
    >>> property_diff(black, black.root._1_2_strike_mc.east_mc, 'currentLabel', 'white_danger')
    >>> property_diff(black, black.root._1_2_strike_mc.west_mc, 'currentLabel', 'white_danger')
    >>> property_diff(black, black.root._0_2_strike_mc.north_mc, 'currentLabel', 'black_danger_retaliate')
    >>> property_diff(black, black.root._0_2_strike_mc.east_mc, 'currentLabel', 'black_danger_retaliate')
    >>> property_diff(black, black.root._0_2_strike_mc.south_mc, 'currentLabel', 'black_danger_retaliate')

    EMMET CAPTURES.  EMMET SEES WIN SCREEN.
    >>> property_diff(black, black.root.game_over_mc, 'currentLabel', 'win')

    >>> import shutil
    >>> shutil.copy('sgf/_gogui.sgf', 'sgf/emmet_capture_3_3_example.sgf')

    06/01/2010 Tue 
    21:51
    this afternoon:
    emmet plays 
            ETHAN
    The Great Wall.
    In the mountains of China, at a mountain pass, you plan a wall.
        capture go 3x3
    ^_^ clicks corner.  two roads.  this is worst place to play.
    ^_^ clicks side.  three roads.  this is better.  the roads.  
    >_< does not really distinguish between two roads and three roads by tint and hue of road or frequency of travel.
    >_< not diagonals?
    >_< 3x3, emmet sees no grid.  where do i play?  confused.
    >_< 3x3, emmet clicks center.  ? appears.  is that the right move?  confused.
    >_< emmet plays to corner first.  wants to play there.
    >_< emmet says lose any single one and lose whole game???  really?  emmet says he did not realize that.  he thought he could win by not losing it all.  is he thinking:  why does one sacrifice cost the game?
    >_< emmet places and hears sound.  what was that sound?  he is confused.  i say it was sound of losing liberty.  he asks:  of 2 or 3?  he does not know which is which.  he is confused.
    >_< emmet clicks.  he hears squeak.  he asks:  what was the squeak?  i say it is the snow king building.
    >_< 3x3, tints of territory appear.  emmet asks:  what are those tints for?  i say they are not important now.
    >_< 3x3, tints of height.  emmet asks what are those tints for?  i say there is a hill and the center is the top of the hill.
    >_< emmet sees crossed swords.
    >_< emmet says it is all so small, i am not sure about [something].
    10>_< capture 3x3, emmet previews to put himself into danger.  i stop him and point it out.  he is confused.  he says he had crossed swords.  i say, but white can build there if they starve your castle first.  emmet is perplexed.  he cannot imagine what happens when one person plays there, or why it makes any sense.
    >_< emmet sees board of capture 5x5.  he says he thought there were 4 cells in center.  actually there are nine.  
    >_< emmet see mountains on side and top rotated.  he does not feel they are mountains.
    >_< i talk.  emmet says, i wish what you were saying, or a short version of what you are saying, would appear on bottom right [as a comment].
    >_< capture 3x3, emmet sees score bar.  he asks what is that?  i say it is not important yet.  emmet feels distracted.
    '''

def emmet_capture_5_5_example():
    '''
    >>> code_unit.inline_examples(
    ...     ethan_lukasz_begin_example.__doc__, 
    ...     locals(), globals(), 
    ...     verify_examples = False)

    >>> wait = 4.0
    >>> black = lukasz
    >>> emmet = black
    >>> designer = white
    >>> mouse_down_and_sleep(black, black.root.lobby_mc._00_mc.capture_5_5_mc,
    ...     wait / black._speed)

    #_5_5 board
    #>>> mouse_down_and_sleep(black, black.root.game_over_mc._5_5_mc.enter_mc, wait / black._speed)
    #>>> property_diff(black, black.root, 'currentLabel', '_5_5')
    #>>> property_diff(black, black.root.game_over_mc._5_5_mc.enter_mc, 'currentLabel', 'none')
    #>>> property_diff(white, white.root, 'currentLabel', '_5_5')
    #>>> property_diff(white, white.root.game_over_mc._5_5_mc.enter_mc, 'currentLabel', 'none')

    EMMET CLICKS ON START BUTTON.
    >>> mouse_down_and_sleep(black, black.root.game_over_mc.start_mc, wait / black._speed)

    emmet CAN SEE ATTACK, AND DEFEND AND CRITICAL.
    >>> property_diff(black, black.root.critical_mc, 'currentLabel', 'show')
    >>> property_diff(black, black.root.defend_mc, 'currentLabel', 'show')
    >>> property_diff(black, black.root.attack_mc, 'currentLabel', 'show')

    EMMET CAN SEE STRIKE, NOT TERRITORY OR SUICIDE.
    >>> property_diff(black, black.root.strike_mc, 'currentLabel', 'show')
    >>> property_diff(black, black.root.territory_mc, 'currentLabel', 'none')
    >>> property_diff(black, black.root.suicide_mc, 'currentLabel', 'none')

    TO REPLAY, TURN OFF COMPUTER PLAY.
        >>> mouse_down_and_sleep(black, black.root.game_over_mc.white_computer_mc.enter_mc, wait / black._speed)

    >>> mouse_down_and_sleep(black, black.root._0_1_mc, wait / black._speed)
   
    EMMET SEES WHERE WHITE MIGHT PLAY NEXT.
    >>> if property_diff(black, black.root._2_1_mc.top_move_mc, 'currentLabel', 'white') and property_diff(black, black.root._1_3_mc.top_move_mc, 'currentLabel', 'white') and property_diff(black, black.root._2_2_mc.top_move_mc, 'currentLabel', 'white'):
    ...     black.ambassador.receives[-1]
    
        top_moves_white
        = C3 45.00 

        play B C3
        = 

        top_moves_white
        = C4 0.51 C2 0.51 B3 0.50 D3 0.50 

        undo
        = 

        play B B5
        = 

        top_moves_white
        = B3 1.00 D4 1.00 C3 1.00 
    
    >>> mouse_down_and_sleep(black, black.root._2_2_mc, wait / black._speed)
   
    EMMET SEES WHERE WHITE MIGHT PLAY NEXT.
    >>> if property_diff(black, black.root._2_1_mc.top_move_mc, 'currentLabel', 'white') and property_diff(black, black.root._1_2_mc.top_move_mc, 'currentLabel', 'white') and property_diff(black, black.root._2_3_mc.top_move_mc, 'currentLabel', 'white'):
    ...     black.ambassador.receives[-1]
    
    >>> mouse_down_and_sleep(black, black.root._2_2_mc, wait / black._speed)
    >>> mouse_down_and_sleep(white, white.root._2_1_mc, wait / white._speed)
    >>> mouse_down_and_sleep(black, black.root._3_1_mc, wait / black._speed)
    >>> mouse_down_and_sleep(black, black.root._3_2_mc, wait / black._speed)
    >>> mouse_down_and_sleep(black, black.root._3_1_mc, wait / black._speed)
    >>> mouse_down_and_sleep(black, black.root._3_1_mc, wait / black._speed)
    >>> mouse_down_and_sleep(white, white.root._3_2_mc, wait / white._speed)
    >>> black.pb()
    ,,,,,
    ,,,,,
    ,OX,,
    ,XO,,
    ,,,,,

    cross-cut, see critical.
    
        dragon_status C3
        = critical A2 C4

        top_moves_black
        = D2 31.78 B4 31.77 C4 23.16 A3 11.42 C1 11.42 A2 9.69 B1 6.37 

        top_moves_white
        = A2 43.20 C4 23.45 D3 23.45 B1 20.24 B4 18.68 D2 18.53 

    when critical, emmet does not see vital point.
    emmet sees critical dragons and top_moves_black[0]
    >>> property_diff(black, black.root._3_0_mc.vital_point_mc, 'currentLabel', 'none')
    >>> if property_diff(black, black.root._3_3_mc.top_move_mc, 'currentLabel', 'black') and property_diff(black, black.root._1_1_mc.top_move_mc, 'currentLabel', 'black'):  black.ambassador.receives[-1]
    >>> property_diff(black, black.root._3_1_mc.dragon_status_mc, 'currentLabel', 'white_attack')
    >>> mouse_down_and_sleep(black, black.root._2_3_mc, wait / black._speed)
    >>> property_diff(black, black.root._3_1_mc.dragon_status_mc, 'currentLabel', 'none')
    >>> mouse_down_and_sleep(black, black.root._4_1_mc, wait / black._speed)
    >>> mouse_down_and_sleep(black, black.root._3_3_mc, wait / black._speed)
    >>> mouse_down_and_sleep(black, black.root._3_3_mc, wait / black._speed)
    >>> property_diff(black, black.root._3_1_mc.dragon_status_mc, 'currentLabel', 'none')
    >>> property_diff(black, black.root._4_3_mc.top_move_mc, 'currentLabel', 'none')
    >>> mouse_down_and_sleep(white, white.root._3_0_mc, wait / white._speed)
    >>> mouse_down_and_sleep(black, black.root._4_1_mc, wait / black._speed)
    >>> mouse_down_and_sleep(black, black.root._4_2_mc, wait / black._speed)
    >>> mouse_down_and_sleep(black, black.root._4_2_mc, wait / black._speed)
    >>> mouse_down_and_sleep(white, white.root._4_1_mc, wait / white._speed)
    >>> mouse_down_and_sleep(black, black.root._4_0_mc, wait / black._speed)
    >>> mouse_down_and_sleep(black, black.root._4_0_mc, wait / black._speed)

        capture go 5x5
    ^_^       on 5x5 after he captures.  he clicks just one more time to see what that looks like.  oh, he was right.  it was a good idea.  

    >>> import shutil
    >>> shutil.copy('sgf/_update_gnugo.sgf', 'sgf/emmet_capture_5_5_example.sgf')
    '''




def kgs_kennerly_rats_sgf_example():
    '''Replay SGF from KGS.
    >>> code_unit.inline_examples(
    ...     ethan_joris_start_example.__doc__, 
    ...     locals(), globals(), 
    ...     verify_examples = False)

    #+ kennerly plays white, and rats is rated higher, so
    #+ so give white the visualizations too.

    Joris can see territory, defend, attack.
    >>> wait = 4.0
    >>> time.sleep(wait / joris._speed)
    >>> property_diff(joris, joris.root.profit_mc, 'currentLabel', 'show')
    >>> property_diff(joris, joris.root.defend_mc, 'currentLabel', 'show')
    >>> property_diff(joris, joris.root.attack_mc, 'currentLabel', 'show')
    >>> from master import play_sgf
    >>> play_sgf('reference_game/kennerly-rats.sgf', ethan, joris, mouse_down_and_sleep, wait)
    '''


def kgs_kennerly_brockgo_sgf_example():
    '''Replay SGF from KGS.
    >>> code_unit.inline_examples(
    ...     ethan_joris_start_example.__doc__, 
    ...     locals(), globals(), 
    ...     verify_examples = False)

    #+ kennerly plays white, and rats is rated higher, so
    #+ so give white the visualizations too.

    Joris can see territory, defend, attack.
    >>> wait = 4.0
    >>> time.sleep(wait / joris._speed)
    >>> property_diff(joris, joris.root.defend_mc, 'currentLabel', 'show')
    >>> property_diff(joris, joris.root.attack_mc, 'currentLabel', 'show')
    >>> from master import play_sgf
    >>> play_sgf('reference_game/kennerly-BrockGo.sgf', ethan, joris, mouse_down_and_sleep, wait)
    '''


def kgs_altair38_kennerly_sgf_example():
    '''Replay SGF from KGS.  Black wins by 0.5
    >>> code_unit.inline_examples(
    ...     ethan_joris_start_example.__doc__, 
    ...     locals(), globals(), 
    ...     verify_examples = False)

    Joris can see territory, defend, attack.
    >>> wait = 4.0
    >>> time.sleep(wait / joris._speed)
    >>> property_diff(joris, joris.root.profit_mc, 'currentLabel', 'show')
    >>> property_diff(joris, joris.root.defend_mc, 'currentLabel', 'show')
    >>> property_diff(joris, joris.root.attack_mc, 'currentLabel', 'show')
    >>> from master import play_sgf
    >>> play_sgf('reference_game/altair38-kennerly.sgf', ethan, joris, mouse_down_and_sleep, wait)
    '''


def laurens_example():
    '''
    ! laurens plays 3x3, 5x5 and 9x9 with extra stone.

! laurens plays capture 3x3
    >_< am i doing something right?
    >_< help!
! laurens sees castle and animation.
    >_< laurens says he feels interested.
! laurens sees stones throwing.
! laurens sees biting, and says it is like cake biting.
    >_< laurens is a little disappointed.
! laurens sees orange warning liberty road.  laurens thinks road trade is good.  i say it is a worn out road.
    >_< laurens says he feels misled.
! laurens connects castles together.
    ^_^    laurens says he feels like he is building something big.
! laurens clicks to capture.  win.  i say that was just a preview.
    >_< laurens says he was misled.
! castles instead of cake.
    >_< laurens says it has lost some of its innocence.
! laurens plays capture 5x5
! laurens clicks many places except not center.
    >_< laurens might feel a little embarrassed.
! laurens clicks near corner.  
    >_< why is there no sound here?
! laurens plays extra stone 9x9
! white captures once.  laurens sees lose.
    >_< laurens seems disappointed.
! i say laurens has 3/4 of farm.
    ^_^ laurens seems somewhat satisfied.
! laurens clicks to build.  once.  twice.  thrice.
    >_< is laurens building?  laurens is annoyed.
! extra_stone 9x9.  capture.  win.
    >_< laurens is confused.  this is a level for territory.
! blue remains on white castle.  i say that is a castle laurens attacked.
    >_< laurens is confused.

! laurens sees face of advisor.  at spot, laurens sees advisor.  
! laurens sees blue hammer.  i say it is suggestion to move.
    >_< laurens is confused.
>>> # example.log level 20 at Tue Jun 15 21:11:46 2010  through 21:29
>>> mouse_down_and_sleep(lukasz, lukasz.root.game_over_mc.start_mc, wait / lukasz._speed)
>>> mouse_down_and_sleep(lukasz, lukasz.root._1_2_mc, wait / lukasz._speed)
>>> mouse_down_and_sleep(lukasz, lukasz.root._0_2_mc, wait / lukasz._speed)
>>> mouse_down_and_sleep(lukasz, lukasz.root._1_0_mc, wait / lukasz._speed)
>>> mouse_down_and_sleep(lukasz, lukasz.root._1_1_mc, wait / lukasz._speed)
>>> mouse_down_and_sleep(lukasz, lukasz.root._2_0_mc, wait / lukasz._speed)
>>> mouse_down_and_sleep(lukasz, lukasz.root._1_1_mc, wait / lukasz._speed)
>>> mouse_down_and_sleep(lukasz, lukasz.root._1_1_mc, wait / lukasz._speed)
>>> mouse_down_and_sleep(ethan, ethan.root._0_0_mc, wait / ethan._speed)
>>> mouse_down_and_sleep(lukasz, lukasz.root._0_0_mc, wait / lukasz._speed)
>>> mouse_down_and_sleep(lukasz, lukasz.root._0_1_mc, wait / lukasz._speed)
>>> mouse_down_and_sleep(lukasz, lukasz.root._0_1_mc, wait / lukasz._speed)
>>> mouse_down_and_sleep(ethan, ethan.root._0_2_mc, wait / ethan._speed)
>>> mouse_down_and_sleep(lukasz, lukasz.root._1_2_mc, wait / lukasz._speed)
>>> mouse_down_and_sleep(lukasz, lukasz.root._1_2_mc, wait / lukasz._speed)
>>> mouse_down_and_sleep(ethan, ethan.root._2_2_mc, wait / ethan._speed)
>>> mouse_down_and_sleep(lukasz, lukasz.root.game_over_mc.start_mc, wait / lukasz._speed)
>>> mouse_down_and_sleep(lukasz, lukasz.root._3_1_mc, wait / lukasz._speed)
>>> mouse_down_and_sleep(lukasz, lukasz.root._2_1_mc, wait / lukasz._speed)
>>> mouse_down_and_sleep(lukasz, lukasz.root._3_1_mc, wait / lukasz._speed)
>>> mouse_down_and_sleep(lukasz, lukasz.root._2_1_mc, wait / lukasz._speed)
>>> mouse_down_and_sleep(lukasz, lukasz.root._2_1_mc, wait / lukasz._speed)
>>> mouse_down_and_sleep(lukasz, lukasz.root._2_1_mc, wait / lukasz._speed)
>>> mouse_down_and_sleep(lukasz, lukasz.root._2_1_mc, wait / lukasz._speed)
>>> mouse_down_and_sleep(lukasz, lukasz.root._2_3_mc, wait / lukasz._speed)
>>> mouse_down_and_sleep(lukasz, lukasz.root._2_3_mc, wait / lukasz._speed)
>>> mouse_down_and_sleep(lukasz, lukasz.root._2_2_mc, wait / lukasz._speed)
>>> mouse_down_and_sleep(lukasz, lukasz.root._2_2_mc, wait / lukasz._speed)
>>> mouse_down_and_sleep(ethan, ethan.root._1_2_mc, wait / ethan._speed)
>>> mouse_down_and_sleep(lukasz, lukasz.root._1_1_mc, wait / lukasz._speed)
>>> mouse_down_and_sleep(lukasz, lukasz.root._1_1_mc, wait / lukasz._speed)
>>> mouse_down_and_sleep(ethan, ethan.root._2_1_mc, wait / ethan._speed)
>>> mouse_down_and_sleep(lukasz, lukasz.root._3_1_mc, wait / lukasz._speed)
>>> mouse_down_and_sleep(lukasz, lukasz.root._3_1_mc, wait / lukasz._speed)
>>> mouse_down_and_sleep(ethan, ethan.root._0_1_mc, wait / ethan._speed)
>>> mouse_down_and_sleep(lukasz, lukasz.root._3_1_mc, wait / lukasz._speed)
>>> mouse_down_and_sleep(lukasz, lukasz.root._2_0_mc, wait / lukasz._speed)
>>> mouse_down_and_sleep(lukasz, lukasz.root._2_0_mc, wait / lukasz._speed)
>>> mouse_down_and_sleep(ethan, ethan.root._1_0_mc, wait / ethan._speed)
    '''

def laurens_extra_stone_9_9_example():
    '''
    >>> code_unit.inline_examples(
    ...     ethan_lukasz_begin_example.__doc__, 
    ...     locals(), globals(), 
    ...     verify_examples = False)

    >>> wait = 5.0 / black._speed
    >>> emmet = black
    >>> gnugo = white
    >>> mouse_down_and_sleep(black, black.root.lobby_mc._00_mc.extra_stone_7_7_2_mc,
    ...     wait)

    FOR REPLAY, COMPUTER IS NOT PLAYING.
    >>> mouse_down_and_sleep(black, black.root.game_over_mc.white_computer_mc.enter_mc, wait)
    >>> property_diff(black, black.root.game_over_mc.white_computer_mc, 'currentLabel', 'none')

    LAURENS CLICKS ON START BUTTON.
    >>> mouse_down_and_sleep(black, black.root.game_over_mc.start_mc, wait)

    LAURENS SEES SCORE BAR.
    >>> property_diff(black, black.root.score_mc, 'currentLabel', 'show')

    >>> mouse_down_and_sleep(black, black.root._3_5_mc, wait)
    >>> mouse_down_and_sleep(black, black.root._3_5_mc, wait)
    >>> mouse_down_and_sleep(white, white.root._3_4_mc, wait)
    >>> mouse_down_and_sleep(black, black.root.extra_stone_gift_mc.use_mc, wait)
    >>> mouse_down_and_sleep(black, black.root._2_4_mc, wait)
    >>> mouse_down_and_sleep(black, black.root._2_4_mc, wait)
    >>> mouse_down_and_sleep(black, black.root._3_3_mc, wait)
    >>> mouse_down_and_sleep(black, black.root._3_3_mc, wait)
    >>> property_diff(black, black.root._3_4_mc.dragon_status_mc, 'currentLabel', 'black_attack')
    >>> mouse_down_and_sleep(white, white.root._4_4_mc, wait)
    >>> black.pb()
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,X,,,,
    ,,,XOX,,,
    ,,,,O,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    >>> property_diff(black, black.root._3_4_mc.dragon_status_mc, 'currentLabel', 'none')
    >>> mouse_down_and_sleep(black, black.root.extra_stone_gift_mc.use_mc, wait)
    >>> mouse_down_and_sleep(black, black.root._5_4_mc, wait)
    >>> mouse_down_and_sleep(black, black.root._5_4_mc, wait)
    >>> mouse_down_and_sleep(black, black.root._4_3_mc, wait)
    >>> mouse_down_and_sleep(black, black.root._4_3_mc, wait)
    >>> mouse_down_and_sleep(white, white.root._3_6_mc, wait)
    >>> mouse_down_and_sleep(black, black.root._4_5_mc, wait)
    >>> mouse_down_and_sleep(black, black.root._4_5_mc, wait)
    >>> mouse_down_and_sleep(white, white.root._1_5_mc, wait)
    >>> mouse_down_and_sleep(black, black.root._1_4_mc, wait)
    >>> mouse_down_and_sleep(black, black.root._1_4_mc, wait)
    >>> mouse_down_and_sleep(white, white.root._4_6_mc, wait)
    >>> mouse_down_and_sleep(black, black.root._5_6_mc, wait)
    >>> mouse_down_and_sleep(black, black.root._5_6_mc, wait)
    >>> mouse_down_and_sleep(white, white.root._2_6_mc, wait)
    >>> mouse_down_and_sleep(black, black.root._4_7_mc, wait)
    >>> mouse_down_and_sleep(black, black.root._4_7_mc, wait)
    >>> mouse_down_and_sleep(white, white.root._1_7_mc, wait)
    >>> mouse_down_and_sleep(black, black.root._0_6_mc, wait)
    >>> mouse_down_and_sleep(black, black.root._0_6_mc, wait)
    >>> mouse_down_and_sleep(white, white.root._0_5_mc, wait)
    >>> mouse_down_and_sleep(black, black.root._0_4_mc, wait)
    >>> mouse_down_and_sleep(black, black.root._0_4_mc, wait)
    >>> mouse_down_and_sleep(white, white.root._3_7_mc, wait)
    >>> mouse_down_and_sleep(black, black.root._5_7_mc, wait)
    >>> mouse_down_and_sleep(black, black.root._5_7_mc, wait)
    >>> mouse_down_and_sleep(white, white.root._2_5_mc, wait)
    >>> mouse_down_and_sleep(black, black.root._4_8_mc, wait)
    >>> mouse_down_and_sleep(black, black.root._4_8_mc, wait)
    >>> mouse_down_and_sleep(white, white.root._3_8_mc, wait)
    >>> mouse_down_and_sleep(black, black.root._1_8_mc, wait)
    >>> mouse_down_and_sleep(black, black.root._1_8_mc, wait)
    >>> mouse_down_and_sleep(white, white.root._2_3_mc, wait)
    >>> mouse_down_and_sleep(black, black.root._2_2_mc, wait)
    >>> mouse_down_and_sleep(black, black.root._2_2_mc, wait)
    >>> mouse_down_and_sleep(white, white.root._4_4_mc, wait)
    >>> mouse_down_and_sleep(black, black.root._1_3_mc, wait)
    >>> mouse_down_and_sleep(black, black.root._1_3_mc, wait)
    >>> mouse_down_and_sleep(white, white.root._2_0_mc, wait)
    >>> mouse_down_and_sleep(black, black.root._1_6_mc, wait)
    >>> mouse_down_and_sleep(black, black.root._1_6_mc, wait)
    >>> mouse_down_and_sleep(white, white.root._5_0_mc, wait)
    >>> mouse_down_and_sleep(black, black.root._5_1_mc, wait)
    >>> mouse_down_and_sleep(black, black.root._5_1_mc, wait)
    >>> mouse_down_and_sleep(white, white.root._0_1_mc, wait)
    >>> mouse_down_and_sleep(black, black.root._4_0_mc, wait)
    >>> mouse_down_and_sleep(black, black.root._4_0_mc, wait)
    >>> mouse_down_and_sleep(white, white.root._0_0_mc, wait)
    >>> mouse_down_and_sleep(black, black.root._6_0_mc, wait)
    >>> mouse_down_and_sleep(black, black.root._6_0_mc, wait)
    >>> mouse_down_and_sleep(white, white.root._0_2_mc, wait)
    >>> mouse_down_and_sleep(black, black.root._2_7_mc, wait)
    >>> mouse_down_and_sleep(black, black.root._2_7_mc, wait)
    >>> mouse_down_and_sleep(white, white.root._0_7_mc, wait)
    >>> mouse_down_and_sleep(black, black.root._1_1_mc, wait)
    >>> mouse_down_and_sleep(black, black.root._1_1_mc, wait)
    >>> mouse_down_and_sleep(white, white.root._5_5_mc, wait)
    >>> mouse_down_and_sleep(black, black.root._6_5_mc, wait)
    >>> mouse_down_and_sleep(black, black.root._6_5_mc, wait)
    >>> mouse_down_and_sleep(white, white.root._7_5_mc, wait)
    >>> mouse_down_and_sleep(black, black.root._8_5_mc, wait)

    >>> import shutil
    >>> shutil.copy('sgf/_gogui.sgf', 'sgf/laurens_extra_stone_9_9_example.sgf')
    '''



def yuji_capture_3_3_example():
    '''At Twee Ogen, Yuji captures.
    >>> # example.log level 20 at Tue Jun 29 23:15:42 2010
    >>> code_unit.inline_examples(
    ...     ethan_lukasz_begin_example.__doc__, 
    ...     locals(), globals(), 
    ...     verify_examples = False)

    >>> wait = 5.0 / black._speed
    >>> yuji = black
    >>> random_play = white
    >>> # black.root.gateway_mc.gotoAndPlay('none'); print 'pretend'
    >>> black.root.gateway_mc.currentLabel
    'none'
    >>> mouse_down_and_sleep(black, black.root.lobby_mc._00_mc.capture_3_3_mc,
    ...     wait)

    YUJI CLICKS ON START BUTTON.
    >>> mouse_down_and_sleep(black, black.root.game_over_mc.start_mc, wait)
    >>> property_diff(black, black.root.sgf_file_txt, 
    ...     'text', 'sgf/beginner/capture_3_3.sgf')

    FOR REPLAY, COMPUTER IS NOT PLAYING.
    >>> mouse_down_and_sleep(black, black.root.game_over_mc.white_computer_mc.enter_mc, wait)
    >>> property_diff(black, black.root.game_over_mc.white_computer_mc, 'currentLabel', 'none')
    
    YUJI CAN SEE EMPTY BLOCKS.
    >>> property_diff(black, black.root.option_mc.empty_block_mc, 'currentLabel', 'show')
    >>> property_diff(black, black.root._0_0_mc.empty_block_north_mc, 'currentLabel', 'block')
    >>> property_diff(black, black.root._0_0_mc.empty_block_east_mc, 'currentLabel', 'liberty')

    >>> black.root._2_0_mc.dispatchEvent(mouseDown)
    >>> time.sleep(wait)
    >>> black.root.comment_mc.currentLabel
    'none'
    >>> black.root.tutor_mc.currentLabel
    'corner'
    >>> mouse_down_and_sleep(black, black.root._1_1_mc, wait)
    >>> black.root.tutor_mc.currentLabel
    'question'
    >>> mouse_down_and_sleep(black, black.root._0_0_mc, wait)
    >>> black.root.comment_mc.currentLabel
    'none'
    >>> black.root.tutor_mc.currentLabel
    'corner'
    >>> mouse_down_and_sleep(black, black.root._0_2_mc, wait)
    >>> black.root.comment_mc.currentLabel
    'none'
    >>> black.root.tutor_mc.currentLabel
    'corner'
    >>> mouse_down_and_sleep(black, black.root._1_1_mc, wait)
    >>> black.root.tutor_mc.currentLabel
    'question'

    AFTER PARTNER MOVE, BUT NOT DURING PREVIEW, YUJI SEES LIBERTY.
    >>> property_diff(black, black.root._0_1_mc.empty_block_south_mc, 'currentLabel', 'liberty')
    >>> mouse_down_and_sleep(black, black.root._1_1_mc, wait)
    >>> property_diff(black, black.root._0_1_mc.empty_block_south_mc, 'currentLabel', 'liberty')

    COMPUTER DOES NOT SEE EMPTY BLOCKS.
    >>> property_diff(white, white.root._0_1_mc.empty_block_south_mc, 'currentLabel', 'none')

    >>> mouse_down_and_sleep(white, white.root._0_0_mc, wait)
    >>> # black.root.tutor_mc.gotoAndPlay('surround'); print 'pretend'
    >>> black.root.tutor_mc.currentLabel
    'first_capture'
    >>> property_diff(black, black.root._0_1_mc.empty_block_south_mc, 'currentLabel', 'you')
    >>> property_diff(black, black.root._0_1_mc.empty_block_west_mc, 'currentLabel', 'block')
    >>> property_diff(white, white.root._0_1_mc.empty_block_south_mc, 'currentLabel', 'none')

    >>> mouse_down_and_sleep(black, black.root._0_1_mc, wait)
    >>> # black.root.tutor_mc.gotoAndPlay('capture'); print 'pretend'
    >>> black.root.tutor_mc.currentLabel
    'capture'
    >>> mouse_down_and_sleep(black, black.root._1_0_mc, wait)
    >>> mouse_down_and_sleep(black, black.root._1_0_mc, wait)
    >>> mouse_down_and_sleep(white, white.root._0_1_mc, wait)
    >>> # black.root.tutor_mc.gotoAndPlay('none'); print 'pretend'
    >>> black.root.tutor_mc.currentLabel
    'black_warning'
    >>> mouse_down_and_sleep(black, black.root._0_2_mc, wait)
    >>> mouse_down_and_sleep(black, black.root._0_2_mc, wait)
    >>> mouse_down_and_sleep(white, white.root._0_0_mc, wait)

    YUJI CAPTURES.  YUJI SEES WIN SCREEN.
    >>> property_diff(black, black.root.game_over_mc, 'currentLabel', 'win')

    YUJI SEES EXIT TO LOBBY.
    >>> black.root.game_over_mc.lobby_mc.currentLabel
    'none'

    Experience, level increase, and level up.
    >>> black.root.level_mc.currentLabel
    'none'
    >>> black.root.level_mc._txt.text
    '1'
    >>> black.root.level_mc.progress_mc.currentLabel
    '_49'

    >>> import shutil
    >>> shutil.copy('sgf/_gogui.sgf', 'sgf/yuji_capture_3_3_example.sgf')
    '''


def yuji_capture_5_5_example():
    '''At Twee Ogen, Yuji captures.
    >>> # example.log level 20 at Tue Jun 29 23:15:42 2010
    >>> code_unit.inline_examples(
    ...     ethan_lukasz_begin_example.__doc__, 
    ...     locals(), globals(), 
    ...     verify_examples = False)

    >>> wait = 5.0 / black._speed
    >>> yuji = black
    >>> random_play = white
    >>> mouse_down_and_sleep(black, black.root.lobby_mc._00_mc.capture_5_5_mc,
    ...     wait)

    YUJI CLICKS ON START BUTTON.
    >>> mouse_down_and_sleep(black, black.root.game_over_mc.start_mc, wait)
    >>> property_diff(black, black.root.sgf_file_txt, 
    ...     'text', 'sgf/beginner/capture_5_5.sgf')

    FOR REPLAY, COMPUTER IS NOT PLAYING.
    >>> property_diff(black, black.root.game_over_mc.white_computer_mc, 'currentLabel', 'computer')
    >>> mouse_down_and_sleep(black, black.root.game_over_mc.white_computer_mc.enter_mc, wait)
    >>> property_diff(black, black.root.game_over_mc.white_computer_mc, 'currentLabel', 'none')

    >>> mouse_down_and_sleep(black, black.root._3_3_mc, wait)
    >>> mouse_down_and_sleep(black, black.root._3_3_mc, wait)
    >>> mouse_down_and_sleep(black, black.root._2_2_mc, wait)
    >>> mouse_down_and_sleep(black, black.root._2_2_mc, wait)
    >>> mouse_down_and_sleep(white, white.root._2_1_mc, wait)
    >>> mouse_down_and_sleep(black, black.root._1_1_mc, wait)
    >>> mouse_down_and_sleep(black, black.root._2_0_mc, wait)
    >>> mouse_down_and_sleep(black, black.root._1_0_mc, wait)
    >>> mouse_down_and_sleep(black, black.root._1_2_mc, wait)
    >>> mouse_down_and_sleep(black, black.root._2_3_mc, wait)
    >>> mouse_down_and_sleep(black, black.root._1_2_mc, wait)
    >>> mouse_down_and_sleep(black, black.root._1_2_mc, wait)
    >>> mouse_down_and_sleep(white, white.root._3_2_mc, wait)
    >>> mouse_down_and_sleep(black, black.root._3_3_mc, wait)
    >>> mouse_down_and_sleep(black, black.root._3_3_mc, wait)
    >>> mouse_down_and_sleep(white, white.root._2_3_mc, wait)
    >>> mouse_down_and_sleep(black, black.root._3_1_mc, wait)
    >>> mouse_down_and_sleep(black, black.root._3_1_mc, wait)
    >>> mouse_down_and_sleep(white, white.root._1_1_mc, wait)
    >>> mouse_down_and_sleep(black, black.root._4_2_mc, wait)
    >>> mouse_down_and_sleep(black, black.root._4_2_mc, wait)
    >>> mouse_down_and_sleep(white, white.root._1_3_mc, wait)

    YUJI CAPTURES.  YUJI SEES WIN SCREEN.
    >>> property_diff(black, black.root.game_over_mc, 'currentLabel', 'win')

    Experience, level increase, and level up.
    >>> white.root.level_mc._txt.text
    '36'
    >>> black.root.level_mc.currentLabel
    'up'
    >>> black.root.level_mc._txt.text
    '2'
    >>> black.root.level_mc.progress_mc.currentLabel
    '_4'
    >>> black.root.level_mc.none_mc.dispatchEvent(mouseDown)
    >>> time.sleep(wait)
    >>> black.root.level_mc.currentLabel
    'none'

    >>> import shutil
    >>> shutil.copy('sgf/_gogui.sgf', 'sgf/yuji_capture_5_5_example.sgf')
    '''

def computer_lukasz_snippet():
    '''

    LOAD COMPUTER CONTROLLER
    >>> white = configuration.globe_class()
    >>> white.setup(configuration.mock_speed, configuration.setup_client)
    >>> set_property(white, white.root.title_mc.username_txt, 'text', 'computer_lukasz')
    >>> time.sleep(wait)
    >>> set_property(white, white.root.title_mc.password_txt, 'text', 'computer_lukasz')
    >>> time.sleep(wait)
    >>> mouse_down_and_sleep(white, white.root.title_mc.start_btn, max(2, 2 * wait))
    >>> property_diff(white, white.root, 'currentLabel', 'lobby')
    '''

def yuji_dominate_3_3_example():
    '''At Twee Ogen, Yuji dominates.
    >>> # example.log level 20 at Tue Jun 29 23:15:42 2010
    >>> code_unit.inline_examples(
    ...     ethan_lukasz_begin_example.__doc__, 
    ...     locals(), globals(), 
    ...     verify_examples = False)

    >>> wait = 5.0 / black._speed
    >>> yuji = black
    >>> mouse_down_and_sleep(black, black.root.lobby_mc._00_mc.dominate_3_3_mc,
    ...     wait)

    YUJI CLICKS ON START BUTTON.
    >>> mouse_down_and_sleep(black, black.root.game_over_mc.start_mc, wait)
    >>> property_diff(black, black.root.sgf_file_txt, 
    ...     'text', 'sgf/beginner/dominate_3_3.sgf')

    FOR REPLAY, COMPUTER IS NOT PLAYING.
    >>> mouse_down_and_sleep(black, black.root.game_over_mc.white_computer_mc.enter_mc, wait)
    >>> property_diff(black, black.root.game_over_mc.white_computer_mc, 'currentLabel', 'none')
    >>> random_play = white

    >>> mouse_down_and_sleep(black, black.root._1_1_mc, wait)
    >>> mouse_down_and_sleep(black, black.root._1_1_mc, wait)
    >>> mouse_down_and_sleep(white, white.root._0_2_mc, wait)
    >>> mouse_down_and_sleep(black, black.root._2_1_mc, wait)
    >>> mouse_down_and_sleep(black, black.root._2_2_mc, wait)
    >>> mouse_down_and_sleep(black, black.root._2_1_mc, wait)
    >>> mouse_down_and_sleep(black, black.root._2_1_mc, wait)
    >>> mouse_down_and_sleep(white, white.root._2_2_mc, wait)
    >>> mouse_down_and_sleep(black, black.root._1_2_mc, wait)
    >>> mouse_down_and_sleep(black, black.root._1_0_mc, wait)
    >>> mouse_down_and_sleep(black, black.root._1_0_mc, wait)
    >>> mouse_down_and_sleep(white, white.root._0_0_mc, wait)
    >>> mouse_down_and_sleep(black, black.root.game_over_mc.white_computer_mc.enter_mc, wait)
    >>> property_diff(black, black.root.game_over_mc.white_computer_mc, 'currentLabel', 'computer')
    >>> mouse_down_and_sleep(black, black.root._1_2_mc, wait)
    >>> mouse_down_and_sleep(black, black.root._1_2_mc, wait)
    >>> # mouse_down_and_sleep(white, white.root.pass_mc, wait)
    >>> mouse_down_and_sleep(black, black.root._0_1_mc, wait)
    >>> mouse_down_and_sleep(black, black.root._0_1_mc, wait)
    >>> # mouse_down_and_sleep(white, white.root.pass_mc, wait)

    YUJI DOMINATES.  YUJI SEES WIN SCREEN.
    >>> property_diff(black, black.root.game_over_mc, 'currentLabel', 'win')

    >>> import shutil
    >>> shutil.copy('sgf/_gogui.sgf', 'sgf/yuji_dominate_3_3_example.sgf')
    '''

def yuji_dominate_3_3_no_pass_example():
    '''dominate 3x3.  see that computer passes.  do not pass.  leave.  
    start dominate 5x5.  look at pass.  see no pass.
    >>> # example.log level 20 at Tue Jun 29 23:15:42 2010
    >>> code_unit.inline_examples(
    ...     yuji_dominate_3_3_example.__doc__, 
    ...     locals(), globals(), 
    ...     verify_examples = False)
    >>> property_diff(black, black.root.pass_white_mc, 'currentLabel', 'white')
    >>> mouse_down_and_sleep(black, black.root.lobby_mc.enter_mc,
    ...     wait)
    >>> property_diff(black, black.root, 'currentLabel', 'lobby')
    >>> property_diff(black, black.root.pass_white_mc, 'currentLabel', 'none')
    >>> mouse_down_and_sleep(black, black.root.lobby_mc._00_mc.dominate_5_5_mc,
    ...     wait)
    >>> property_diff(black, black.root.pass_white_mc, 'currentLabel', 'none')
    '''

def yuji_dominate_5_5_example():
    '''At Twee Ogen, Yuji dominates.
    >>> # example.log level 20 at Tue Jun 29 23:15:42 2010
    >>> code_unit.inline_examples(
    ...     ethan_lukasz_begin_example.__doc__, 
    ...     locals(), globals(), 
    ...     verify_examples = False)

    >>> wait = 5.0 / black._speed
    >>> yuji = black
    >>> random_play = white
    >>> mouse_down_and_sleep(black, black.root.lobby_mc._00_mc.dominate_5_5_mc,
    ...     wait)

    YUJI CLICKS ON START BUTTON.
    >>> mouse_down_and_sleep(black, black.root.game_over_mc.start_mc, wait)
    >>> property_diff(black, black.root.sgf_file_txt, 
    ...     'text', 'sgf/beginner/dominate_5_5.sgf')

    FOR REPLAY, COMPUTER IS NOT PLAYING.
    >>> mouse_down_and_sleep(black, black.root.game_over_mc.white_computer_mc.enter_mc, wait)
    >>> property_diff(black, black.root.game_over_mc.white_computer_mc, 'currentLabel', 'none')

    >>> mouse_down_and_sleep(black, black.root._2_2_mc, wait)
    >>> mouse_down_and_sleep(black, black.root._2_2_mc, wait)
    >>> mouse_down_and_sleep(white, white.root._2_1_mc, wait)
    >>> mouse_down_and_sleep(black, black.root._1_2_mc, wait)
    >>> mouse_down_and_sleep(black, black.root._1_2_mc, wait)
    >>> mouse_down_and_sleep(white, white.root._3_2_mc, wait)
    >>> mouse_down_and_sleep(black, black.root._2_3_mc, wait)
    >>> mouse_down_and_sleep(black, black.root._1_1_mc, wait)
    >>> mouse_down_and_sleep(black, black.root._1_1_mc, wait)
    >>> mouse_down_and_sleep(white, white.root._4_1_mc, wait)
    >>> mouse_down_and_sleep(black, black.root._2_0_mc, wait)
    >>> mouse_down_and_sleep(black, black.root._2_0_mc, wait)
    >>> mouse_down_and_sleep(white, white.root._3_0_mc, wait)
    >>> mouse_down_and_sleep(black, black.root._3_3_mc, wait)
    >>> mouse_down_and_sleep(black, black.root._3_3_mc, wait)
    >>> mouse_down_and_sleep(white, white.root._1_0_mc, wait)
    >>> mouse_down_and_sleep(black, black.root._4_3_mc, wait)
    >>> mouse_down_and_sleep(black, black.root._4_2_mc, wait)
    >>> mouse_down_and_sleep(black, black.root._3_1_mc, wait)
    >>> mouse_down_and_sleep(black, black.root._2_3_mc, wait)
    >>> mouse_down_and_sleep(black, black.root._4_3_mc, wait)
    >>> mouse_down_and_sleep(black, black.root._4_3_mc, wait)
    >>> mouse_down_and_sleep(white, white.root._4_2_mc, wait)
    >>> mouse_down_and_sleep(black, black.root._0_0_mc, wait)
    >>> mouse_down_and_sleep(black, black.root._0_1_mc, wait)
    >>> mouse_down_and_sleep(black, black.root._0_1_mc, wait)
    >>> mouse_down_and_sleep(white, white.root._2_0_mc, wait)
    >>> mouse_down_and_sleep(black, black.root._2_3_mc, wait)
    >>> mouse_down_and_sleep(black, black.root._0_0_mc, wait)
    >>> mouse_down_and_sleep(black, black.root._0_0_mc, wait)
    >>> mouse_down_and_sleep(white, white.root._2_3_mc, wait)
    >>> mouse_down_and_sleep(black, black.root._1_3_mc, wait)
    >>> mouse_down_and_sleep(black, black.root._1_3_mc, wait)
    >>> mouse_down_and_sleep(white, white.root._4_4_mc, wait)
    >>> mouse_down_and_sleep(black, black.root._3_4_mc, wait)
    >>> mouse_down_and_sleep(black, black.root._3_4_mc, wait)
    >>> mouse_down_and_sleep(white, white.root._0_2_mc, wait)
    >>> mouse_down_and_sleep(black, black.root._0_4_mc, wait)
    >>> mouse_down_and_sleep(black, black.root._2_4_mc, wait)
    >>> mouse_down_and_sleep(black, black.root._0_3_mc, wait)
    >>> mouse_down_and_sleep(black, black.root._0_3_mc, wait)
    >>> mouse_down_and_sleep(white, white.root._1_4_mc, wait)
    >>> mouse_down_and_sleep(black, black.root._2_4_mc, wait)
    >>> mouse_down_and_sleep(black, black.root._2_4_mc, wait)
    >>> mouse_down_and_sleep(white, white.root._4_0_mc, wait)
    >>> mouse_down_and_sleep(black, black.root._3_1_mc, wait)
    >>> mouse_down_and_sleep(black, black.root._3_1_mc, wait)
    >>> mouse_down_and_sleep(white, white.root._3_2_mc, wait)

    YUJI DOMINATES.  YUJI SEES WIN SCREEN.
    >>> property_diff(black, black.root.game_over_mc, 'currentLabel', 'win')

    >>> import shutil
    >>> shutil.copy('sgf/_gogui.sgf', 'sgf/yuji_dominate_5_5_example.sgf')

    White would not die if it had not filled in its own liberty.  I say this.
    '''


def log_example():
    '''Record button presses.
    ! vimgrep /example.log/j *.py
    ! replay yuji_capture_3_3_example
    ! expect example.log: lukasz.root.lobby_mc._0_mc.dispatchEvent(mouse_down)
    >>> old_example_log = text.load('example.log')
    >>> code_unit.inline_examples(
    ...     yuji_capture_3_3_example.__doc__, 
    ...     locals(), globals(), 
    ...     verify_examples = False)
    >>> from embassy import is_in_tail
    >>> example_log = text.load('example.log')
    >>> added = len(example_log) - len(old_example_log)
    >>> if not is_in_tail('example.log', added, '>>> lukasz.root.lobby_mc._00_mc.capture_3_3_mc.dispatchEvent(mouseDown)'):
    ...     print example_log[-added:]
    '''



def print_items(**kwargs):
    '''
    >>> print_items(a='A')
    a A
    '''
    for k, v in kwargs.items():
        print k, v



def setup_problem_replay(configuration, name, password):
    '''
    >>> computer_jade, jade, wait = setup_problem_replay(configuration, 'jade', 'j')
    >>> jade.root.currentLabel
    'lobby'
    '''
    gateway_process = configuration.subprocess_gateway(configuration.amf_host, 'embassy.py', configuration.verbose)
    black, wait = setup_user(configuration, name, password)
    white, wait = setup_user(configuration, 'computer_lukasz', 'computer_lukasz')
    return white, black, wait

def sleep(live, mock):
    t = min(live, mock)
    time.sleep(t)

def jade_9_9_example():
    '''Jade finished extra_stone_7_7 and starts 9x9.
    >>> # computer_jade, jade, wait = setup_problem_replay(configuration, 'jade', 'j')
    >>> code_unit.inline_examples(
    ...     ethan_lukasz_begin_example.__doc__, 
    ...     locals(), globals(), 
    ...     verify_examples = False)
    >>> jade = black
    >>> computer_jade = white
    >>> ethan = computer_jade
    >>> sloth = 1.0 / jade._speed 
    >>> jade.root.lobby_mc._00_mc.extra_stone_7_7_2_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth *5.304393)

    For replay, computer is not playing.
    >>> jade.root.game_over_mc.white_computer_mc.enter_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth *2.397588)
    >>> mouse_down_and_sleep(jade, jade.root.game_over_mc.start_mc, wait)
    >>> time.sleep(sloth *2.088691)
    >>> mouse_down_and_sleep(jade, jade.root._4_4_mc, wait)
    >>> time.sleep(sloth *2.466794)
    >>> mouse_down_and_sleep(jade, jade.root._4_4_mc, wait)
    >>> time.sleep(sloth)
    >>> mouse_down_and_sleep(computer_jade, computer_jade.root._6_2_mc, wait)
    >>> time.sleep(sloth *16.354936)
    >>> mouse_down_and_sleep(jade, jade.root._6_3_mc, wait)
    >>> time.sleep(sloth *0.954906)
    >>> mouse_down_and_sleep(jade, jade.root._6_3_mc, wait)
    >>> time.sleep(sloth)
    >>> mouse_down_and_sleep(computer_jade, computer_jade.root._5_2_mc, wait)
    >>> time.sleep(sloth *11.183972)
    >>> mouse_down_and_sleep(jade, jade.root._4_3_mc, wait)
    >>> time.sleep(sloth *0.794290)
    >>> time.sleep(sloth *3.043719)
    >>> mouse_down_and_sleep(jade, jade.root._4_3_mc, wait)
    >>> ethan.root.chat_input_txt.text = "well if you want to study up before we play... go on ^_^"
    >>> ethan.root.chat_input_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth *1.287418)
    >>> time.sleep(sloth *1.325931)
    >>> mouse_down_and_sleep(jade, jade.root._4_3_mc, wait)
    >>> time.sleep(sloth)
    >>> mouse_down_and_sleep(computer_jade, computer_jade.root._4_2_mc, wait)
    >>> time.sleep(sloth *8.129968)
    >>> mouse_down_and_sleep(jade, jade.root._3_2_mc, wait)
    >>> time.sleep(sloth *2.325195)
    >>> mouse_down_and_sleep(jade, jade.root._3_2_mc, wait)
    >>> time.sleep(sloth)
    >>> mouse_down_and_sleep(computer_jade, computer_jade.root._2_6_mc, wait)
    >>> time.sleep(sloth *10.968695)
    >>> mouse_down_and_sleep(jade, jade.root._3_6_mc, wait)
    >>> time.sleep(sloth *2.575325)
    >>> mouse_down_and_sleep(jade, jade.root._3_6_mc, wait)
    >>> time.sleep(sloth)
    >>> mouse_down_and_sleep(computer_jade, computer_jade.root._3_7_mc, wait)
    >>> time.sleep(sloth *25.736702)
    >>> mouse_down_and_sleep(jade, jade.root._3_5_mc, wait)
    >>> time.sleep(sloth *4.228666)
    >>> mouse_down_and_sleep(jade, jade.root._3_5_mc, wait)
    >>> time.sleep(sloth)
    >>> mouse_down_and_sleep(computer_jade, computer_jade.root._2_5_mc, wait)
    >>> time.sleep(sloth *5.177847)
    >>> mouse_down_and_sleep(jade, jade.root._2_4_mc, wait)
    >>> time.sleep(sloth *3.424502)
    >>> mouse_down_and_sleep(jade, jade.root._2_4_mc, wait)
    >>> time.sleep(sloth)
    >>> mouse_down_and_sleep(computer_jade, computer_jade.root._1_4_mc, wait)
    >>> time.sleep(sloth *12.892345)
    >>> mouse_down_and_sleep(jade, jade.root._2_3_mc, wait)
    >>> time.sleep(sloth *2.092015)
    >>> mouse_down_and_sleep(jade, jade.root._2_3_mc, wait)
    >>> time.sleep(sloth)
    >>> mouse_down_and_sleep(computer_jade, computer_jade.root._6_6_mc, wait)
    >>> time.sleep(sloth *12.127286)
    >>> mouse_down_and_sleep(jade, jade.root._5_6_mc, wait)
    >>> time.sleep(sloth *3.299999)
    >>> mouse_down_and_sleep(jade, jade.root._5_6_mc, wait)
    >>> time.sleep(sloth)
    >>> mouse_down_and_sleep(computer_jade, computer_jade.root._5_7_mc, wait)
    >>> time.sleep(sloth *18.154168)
    >>> mouse_down_and_sleep(jade, jade.root._4_6_mc, wait)
    >>> time.sleep(sloth *3.418224)
    >>> mouse_down_and_sleep(jade, jade.root._4_6_mc, wait)
    >>> time.sleep(sloth)
    >>> mouse_down_and_sleep(computer_jade, computer_jade.root._4_7_mc, wait)
    >>> time.sleep(sloth *31.665626)
    >>> mouse_down_and_sleep(jade, jade.root._1_5_mc, wait)
    >>> time.sleep(sloth *6.441685)
    >>> mouse_down_and_sleep(jade, jade.root.extra_stone_gift_mc.use_mc, wait)
    >>> time.sleep(sloth *2.709410)
    >>> mouse_down_and_sleep(jade, jade.root._1_5_mc, wait)
    >>> time.sleep(sloth *2.686052)
    >>> mouse_down_and_sleep(jade, jade.root._1_5_mc, wait)
    >>> time.sleep(sloth *1.562535)
    >>> mouse_down_and_sleep(jade, jade.root._1_6_mc, wait)
    >>> time.sleep(sloth *1.975165)
    >>> mouse_down_and_sleep(jade, jade.root._1_6_mc, wait)
    >>> time.sleep(sloth)
    >>> mouse_down_and_sleep(computer_jade, computer_jade.root._5_3_mc, wait)
    >>> time.sleep(sloth *2.916627)
    >>> mouse_down_and_sleep(jade, jade.root._1_6_mc, wait)
    >>> time.sleep(sloth *13.931661)
    >>> mouse_down_and_sleep(jade, jade.root._6_4_mc, wait)
    >>> time.sleep(sloth *1.696116)
    >>> mouse_down_and_sleep(jade, jade.root._6_4_mc, wait)
    >>> time.sleep(sloth)
    >>> mouse_down_and_sleep(computer_jade, computer_jade.root._5_4_mc, wait)
    >>> time.sleep(sloth *21.299758)
    >>> mouse_down_and_sleep(jade, jade.root._5_5_mc, wait)
    >>> time.sleep(sloth *2.299298)
    >>> mouse_down_and_sleep(jade, jade.root._5_5_mc, wait)
    >>> time.sleep(sloth)
    >>> mouse_down_and_sleep(computer_jade, computer_jade.root._6_5_mc, wait)
    >>> time.sleep(sloth *17.259588)
    >>> mouse_down_and_sleep(jade, jade.root._2_7_mc, wait)
    >>> time.sleep(sloth *3.520034)
    >>> mouse_down_and_sleep(jade, jade.root._2_7_mc, wait)
    >>> time.sleep(sloth)
    >>> mouse_down_and_sleep(computer_jade, computer_jade.root._4_1_mc, wait)
    >>> time.sleep(sloth *12.937999)
    >>> mouse_down_and_sleep(jade, jade.root._3_1_mc, wait)
    >>> time.sleep(sloth *3.306715)
    >>> mouse_down_and_sleep(jade, jade.root._3_1_mc, wait)
    >>> time.sleep(sloth)
    >>> mouse_down_and_sleep(computer_jade, computer_jade.root._3_0_mc, wait)
    >>> time.sleep(sloth *10.831854)
    >>> mouse_down_and_sleep(jade, jade.root._2_0_mc, wait)
    >>> time.sleep(sloth *3.009153)
    >>> mouse_down_and_sleep(jade, jade.root._2_0_mc, wait)
    >>> time.sleep(sloth)
    >>> mouse_down_and_sleep(computer_jade, computer_jade.root._4_0_mc, wait)
    >>> time.sleep(sloth *6.385415)
    >>> mouse_down_and_sleep(jade, jade.root._2_1_mc, wait)
    >>> time.sleep(sloth *2.762481)
    >>> mouse_down_and_sleep(jade, jade.root._2_1_mc, wait)
    >>> time.sleep(sloth)
    >>> mouse_down_and_sleep(computer_jade, computer_jade.root._2_8_mc, wait)
    >>> time.sleep(sloth *12.143919)
    >>> mouse_down_and_sleep(jade, jade.root.extra_stone_gift_mc.use_mc, wait)
    >>> time.sleep(sloth *0.996106)
    >>> mouse_down_and_sleep(jade, jade.root._1_7_mc, wait)
    >>> time.sleep(sloth *3.427461)
    >>> mouse_down_and_sleep(jade, jade.root._1_7_mc, wait)
    >>> time.sleep(sloth *3.443742)
    >>> mouse_down_and_sleep(jade, jade.root._3_8_mc, wait)
    >>> time.sleep(sloth *3.201586)
    >>> mouse_down_and_sleep(jade, jade.root._1_8_mc, wait)
    >>> time.sleep(sloth *2.965928)
    >>> mouse_down_and_sleep(jade, jade.root._1_8_mc, wait)
    >>> time.sleep(sloth)
    >>> mouse_down_and_sleep(computer_jade, computer_jade.root._3_8_mc, wait)
    >>> ethan.root.chat_input_txt.text = "after you make peace... please click multiplayer, then 'ethan'"
    >>> ethan.root.chat_input_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth *27.136835)
    >>> time.sleep(sloth *3.861742)
    >>> time.sleep(sloth *6.390469)
    >>> jade.root.pass_mc.dispatchEvent(mouseDown)
    >>> computer_jade.root.pass_mc.dispatchEvent(mouseDown)
    '''


def joris_hide_7_7_example():
    '''Joris hide only on 7x7.  He loses.
    >>> # computer_jade, jade, wait = setup_problem_replay(configuration, 'jade', 'j')
    >>> code_unit.inline_examples(
    ...     ethan_lukasz_begin_example.__doc__, 
    ...     locals(), globals(), 
    ...     verify_examples = False)
    >>> joris = black
    >>> computer_joris = white
    >>> sloth = 0.25 / black._speed 
    >>> # example.log level 20 at Thu Jul 15 21:09:18 2010

    >>> joris.root.lobby_mc.main_mc._20_mc.dispatchEvent(mouseDown)
    >>> time.sleep(wait)
    >>> joris.root.lobby_mc._20_mc.hide_7_7_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 22.359000)

    For replay, computer is not playing.
    >>> joris.root.game_over_mc.white_computer_mc.enter_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 11.670000)
    >>> mouse_down_and_sleep(joris, joris.root.game_over_mc.start_mc, wait)
    >>> time.sleep(sloth * 10.908000)
    >>> mouse_down_and_sleep(joris, joris.root._3_3_mc, wait)
    >>> time.sleep(sloth * 36.609000)
    >>> mouse_down_and_sleep(joris, joris.root._3_3_mc, wait)
    >>> mouse_down_and_sleep(computer_joris, computer_joris.root._2_2_mc, wait)
    >>> time.sleep(sloth * 35.878000)
    >>> mouse_down_and_sleep(joris, joris.root._4_1_mc, wait)
    >>> time.sleep(sloth * 11.301000)
    >>> mouse_down_and_sleep(joris, joris.root.hide_gift_mc.use_mc, wait)
    >>> time.sleep(sloth * 3.772000)
    >>> mouse_down_and_sleep(joris, joris.root._4_1_mc, wait)
    >>> time.sleep(sloth * 4.229000)
    >>> mouse_down_and_sleep(joris, joris.root._4_1_mc, wait)
    >>> mouse_down_and_sleep(computer_joris, computer_joris.root._2_3_mc, wait)
    >>> time.sleep(sloth * 23.070000)
    >>> mouse_down_and_sleep(joris, joris.root.hide_gift_mc.use_mc, wait)
    >>> time.sleep(sloth * 1.954000)
    >>> mouse_down_and_sleep(joris, joris.root._2_5_mc, wait)
    >>> time.sleep(sloth * 8.851000)
    >>> mouse_down_and_sleep(joris, joris.root._1_4_mc, wait)
    >>> time.sleep(sloth * 9.199000)
    >>> mouse_down_and_sleep(joris, joris.root._2_1_mc, wait)
    >>> time.sleep(sloth * 12.400000)
    >>> mouse_down_and_sleep(joris, joris.root._2_5_mc, wait)
    >>> time.sleep(sloth * 4.446000)
    >>> mouse_down_and_sleep(joris, joris.root._2_5_mc, wait)
    >>> mouse_down_and_sleep(computer_joris, computer_joris.root._3_4_mc, wait)
    >>> time.sleep(sloth * 32.852000)
    >>> mouse_down_and_sleep(joris, joris.root._4_3_mc, wait)
    >>> time.sleep(sloth * 4.286000)
    >>> mouse_down_and_sleep(joris, joris.root._4_5_mc, wait)
    >>> time.sleep(sloth * 5.049000)
    >>> mouse_down_and_sleep(joris, joris.root._4_3_mc, wait)
    >>> time.sleep(sloth * 4.732000)
    >>> mouse_down_and_sleep(joris, joris.root._4_3_mc, wait)
    >>> mouse_down_and_sleep(computer_joris, computer_joris.root._4_4_mc, wait)
    >>> time.sleep(sloth * 36.828000)
    >>> mouse_down_and_sleep(joris, joris.root._5_4_mc, wait)
    >>> time.sleep(sloth * 4.635000)
    >>> mouse_down_and_sleep(joris, joris.root._5_4_mc, wait)
    >>> mouse_down_and_sleep(computer_joris, computer_joris.root._5_5_mc, wait)
    >>> time.sleep(sloth * 28.842000)
    >>> mouse_down_and_sleep(joris, joris.root.hide_gift_mc.use_mc, wait)
    >>> time.sleep(sloth * 6.981000)
    >>> mouse_down_and_sleep(joris, joris.root._2_4_mc, wait)
    >>> time.sleep(sloth * 6.121000)
    >>> mouse_down_and_sleep(joris, joris.root._2_4_mc, wait)
    >>> mouse_down_and_sleep(computer_joris, computer_joris.root._4_1_mc, wait)
    >>> mouse_down_and_sleep(computer_joris, computer_joris.root._5_2_mc, wait)
    >>> time.sleep(sloth * 39.999000)
    >>> mouse_down_and_sleep(joris, joris.root._4_5_mc, wait)
    >>> time.sleep(sloth * 4.526000)
    >>> time.sleep(sloth * 0.788000)
    >>> mouse_down_and_sleep(joris, joris.root._4_5_mc, wait)
    >>> time.sleep(sloth * 4.126000)
    >>> time.sleep(sloth * 5.008000)
    >>> time.sleep(sloth * 1.948000)
    >>> mouse_down_and_sleep(joris, joris.root._4_5_mc, wait)
    >>> time.sleep(sloth * 8.467000)
    >>> mouse_down_and_sleep(joris, joris.root._4_5_mc, wait)
    >>> mouse_down_and_sleep(computer_joris, computer_joris.root._5_3_mc, wait)
    >>> time.sleep(sloth * 13.919000)
    >>> mouse_down_and_sleep(joris, joris.root._3_5_mc, wait)
    >>> time.sleep(sloth * 1.782000)
    >>> mouse_down_and_sleep(joris, joris.root._3_5_mc, wait)
    >>> mouse_down_and_sleep(computer_joris, computer_joris.root._1_4_mc, wait)
    >>> time.sleep(sloth * 26.230000)
    >>> mouse_down_and_sleep(joris, joris.root._6_5_mc, wait)
    >>> time.sleep(sloth * 6.876000)
    >>> mouse_down_and_sleep(joris, joris.root._6_5_mc, wait)
    >>> mouse_down_and_sleep(computer_joris, computer_joris.root._3_1_mc, wait)
    >>> time.sleep(sloth * 10.602000)
    >>> mouse_down_and_sleep(joris, joris.root._5_6_mc, wait)
    >>> time.sleep(sloth * 1.970000)
    >>> mouse_down_and_sleep(joris, joris.root._5_6_mc, wait)
    >>> mouse_down_and_sleep(computer_joris, computer_joris.root._4_2_mc, wait)
    >>> time.sleep(sloth * 13.071000)
    >>> mouse_down_and_sleep(joris, joris.root._6_4_mc, wait)
    >>> time.sleep(sloth * 4.397000)
    >>> mouse_down_and_sleep(joris, joris.root._6_4_mc, wait)
    >>> mouse_down_and_sleep(computer_joris, computer_joris.root._1_5_mc, wait)
    >>> time.sleep(sloth * 3.063000)
    >>> mouse_down_and_sleep(joris, joris.root._6_4_mc, wait)
    >>> time.sleep(sloth * 28.592000)
    >>> mouse_down_and_sleep(joris, joris.root.hide_gift_mc.use_mc, wait)
    >>> time.sleep(sloth * 30.618000)
    >>> time.sleep(sloth * 2.486000)
    >>> time.sleep(sloth * 16.938000)
    >>> mouse_down_and_sleep(joris, joris.root._1_6_mc, wait)
    >>> time.sleep(sloth * 3.142000)
    >>> mouse_down_and_sleep(joris, joris.root._1_6_mc, wait)
    >>> mouse_down_and_sleep(computer_joris, computer_joris.root._2_5_mc, wait)
    >>> mouse_down_and_sleep(computer_joris, computer_joris.root._2_6_mc, wait)
    >>> time.sleep(sloth * 7.340000)
    >>> mouse_down_and_sleep(joris, joris.root._3_6_mc, wait)
    >>> time.sleep(sloth * 2.098000)
    >>> mouse_down_and_sleep(joris, joris.root._3_6_mc, wait)
    >>> mouse_down_and_sleep(computer_joris, computer_joris.root._3_2_mc, wait)
    >>> time.sleep(sloth * 27.774000)
    >>> time.sleep(sloth * 15.383000)
    >>> mouse_down_and_sleep(joris, joris.root.hide_gift_mc.use_mc, wait)
    >>> time.sleep(sloth * 1.093000)
    >>> mouse_down_and_sleep(joris, joris.root._1_3_mc, wait)
    >>> time.sleep(sloth * 2.955000)
    >>> time.sleep(sloth * 7.564000)
    >>> time.sleep(sloth * 1.500000)
    >>> mouse_down_and_sleep(joris, joris.root._1_3_mc, wait)
    >>> time.sleep(sloth * 2.341000)
    >>> time.sleep(sloth * 6.045000)
    >>> time.sleep(sloth * 2.644000)
    >>> mouse_down_and_sleep(joris, joris.root._1_3_mc, wait)
    >>> time.sleep(sloth * 4.417000)
    >>> mouse_down_and_sleep(joris, joris.root._1_3_mc, wait)
    >>> mouse_down_and_sleep(computer_joris, computer_joris.root._1_3_mc, wait)
    >>> mouse_down_and_sleep(computer_joris, computer_joris.root._1_2_mc, wait)
    >>> time.sleep(sloth * 16.426000)
    >>> mouse_down_and_sleep(joris, joris.root._0_5_mc, wait)
    >>> time.sleep(sloth * 17.959000)
    >>> mouse_down_and_sleep(joris, joris.root._0_3_mc, wait)
    >>> time.sleep(sloth * 48.441000)
    >>> mouse_down_and_sleep(joris, joris.root._4_0_mc, wait)
    >>> time.sleep(sloth * 2.038000)
    >>> mouse_down_and_sleep(joris, joris.root._4_0_mc, wait)
    >>> mouse_down_and_sleep(computer_joris, computer_joris.root._0_5_mc, wait)
    >>> time.sleep(sloth * 41.921000)
    >>> mouse_down_and_sleep(joris, joris.root._6_3_mc, wait)
    >>> time.sleep(sloth * 12.909000)
    >>> mouse_down_and_sleep(joris, joris.root._3_0_mc, wait)
    >>> time.sleep(sloth * 17.736000)
    >>> mouse_down_and_sleep(joris, joris.root._2_1_mc, wait)
    >>> time.sleep(sloth * 11.535000)
    >>> mouse_down_and_sleep(joris, joris.root._0_3_mc, wait)
    >>> time.sleep(sloth * 11.783000)
    >>> mouse_down_and_sleep(joris, joris.root._0_6_mc, wait)
    >>> time.sleep(sloth * 16.618000)
    >>> mouse_down_and_sleep(joris, joris.root._0_4_mc, wait)
    >>> time.sleep(sloth * 7.663000)
    >>> mouse_down_and_sleep(joris, joris.root._2_1_mc, wait)
    >>> time.sleep(sloth * 9.105000)
    >>> mouse_down_and_sleep(joris, joris.root.hide_gift_mc.use_mc, wait)
    >>> time.sleep(sloth * 20.434000)
    >>> mouse_down_and_sleep(joris, joris.root._2_1_mc, wait)
    >>> time.sleep(sloth * 1.514000)
    >>> time.sleep(sloth * 5.680000)
    >>> time.sleep(sloth * 6.327000)
    >>> mouse_down_and_sleep(joris, joris.root._2_1_mc, wait)
    >>> time.sleep(sloth * 5.827000)
    >>> mouse_down_and_sleep(joris, joris.root._2_1_mc, wait)
    >>> mouse_down_and_sleep(computer_joris, computer_joris.root._6_3_mc, wait)
    >>> time.sleep(sloth * 17.902000)
    >>> mouse_down_and_sleep(joris, joris.root.hide_gift_mc.use_mc, wait)
    >>> time.sleep(sloth * 5.360000)
    >>> mouse_down_and_sleep(joris, joris.root._1_1_mc, wait)
    >>> time.sleep(sloth * 3.301000)
    >>> mouse_down_and_sleep(joris, joris.root._1_1_mc, wait)
    >>> mouse_down_and_sleep(computer_joris, computer_joris.root._0_3_mc, wait)
    >>> time.sleep(sloth * 27.087000)
    >>> mouse_down_and_sleep(joris, joris.root.hide_gift_mc.use_mc, wait)
    >>> time.sleep(sloth * 7.279000)
    >>> mouse_down_and_sleep(joris, joris.root._0_1_mc, wait)
    >>> time.sleep(sloth * 2.147000)
    >>> mouse_down_and_sleep(joris, joris.root._0_1_mc, wait)
    >>> mouse_down_and_sleep(computer_joris, computer_joris.root._0_6_mc, wait)
    >>> time.sleep(sloth * 17.657000)
    >>> mouse_down_and_sleep(joris, joris.root.hide_gift_mc.use_mc, wait)
    >>> time.sleep(sloth * 14.753000)
    >>> mouse_down_and_sleep(joris, joris.root._1_0_mc, wait)
    >>> time.sleep(sloth * 3.324000)
    >>> mouse_down_and_sleep(joris, joris.root._1_0_mc, wait)
    >>> mouse_down_and_sleep(computer_joris, computer_joris.root._2_6_mc, wait)
    >>> time.sleep(sloth * 35.869000)
    >>> mouse_down_and_sleep(joris, joris.root._3_0_mc, wait)
    >>> time.sleep(sloth * 6.072000)
    >>> mouse_down_and_sleep(joris, joris.root._3_0_mc, wait)
    >>> mouse_down_and_sleep(computer_joris, computer_joris.root._5_1_mc, wait)
    >>> time.sleep(sloth * 47.086000)
    >>> mouse_down_and_sleep(joris, joris.root._1_6_mc, wait)
    >>> time.sleep(sloth * 14.584000)
    >>> mouse_down_and_sleep(joris, joris.root._3_4_mc, wait)
    >>> time.sleep(sloth * 13.455000)
    >>> mouse_down_and_sleep(joris, joris.root._0_2_mc, wait)
    >>> time.sleep(sloth * 12.312000)
    >>> mouse_down_and_sleep(joris, joris.root._2_0_mc, wait)
    >>> time.sleep(sloth * 34.946000)
    >>> mouse_down_and_sleep(joris, joris.root._0_2_mc, wait)
    >>> time.sleep(sloth * 4.187000)
    >>> mouse_down_and_sleep(joris, joris.root._2_0_mc, wait)
    >>> time.sleep(sloth * 2.636000)
    >>> mouse_down_and_sleep(joris, joris.root._2_0_mc, wait)
    >>> mouse_down_and_sleep(computer_joris, computer_joris.root._1_6_mc, wait)
    >>> time.sleep(sloth * 53.148000)
    >>> joris.root.pass_mc.dispatchEvent(mouseDown)
    >>> computer_joris.root.pass_mc.dispatchEvent(mouseDown)
    >>> joris.root.menu_mc.toggle_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 39.103000)
    >>> joris.root.menu_mc.toggle_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 2.774000)
    >>> # joris.root.menu_mc.lobby_mc.dispatchEvent(mouseDown)
    >>> # time.sleep(sloth * 2.415000)

    >>> import shutil
    >>> shutil.copy('sgf/_gogui.sgf', 'sgf/joris_hide_7_7_example.sgf')

    Problem setup.  start to read help.  do not press start.
    Read "to build here, click the ?".  Joris clicks ? on help, not on field.
    first move.  hide.  preview dark field on south side.  play.  see yellow field.  worried.
    what is blue bubble?  that is where white will build?
    what do sounds mean?
    Preview but not a question.  Click.  "excuse me what should i do?"
    top move white on top of hide.  huh?
    white stones in south.  joris surrounds 5,5.  does not preview elsewhere.
    losing.  desparately tries to surround large white dragon with isolated, small black castle.
    why is one red block but others are not?
    what are black flags?  
    Sluggish response.
    recognizes and responds to liberty warning and danger.
    '''

def steven_ethan_hide_example():
    r'''Steven (level 50 versus Ethan level 40)  Ethan has 3 hide.
    >>> ethan, steven, wait = setup_example(configuration, 
    ...     ('ethan', 'e'), ('steven', 'houbraken') )
    >>> sloth = 0.25 / wait
    >>> ethan.root.lobby_mc.create_mc.dispatchEvent(mouseDown)
    >>> time.sleep(wait)
    >>> steven.root.lobby_mc.join_mc.enter_btn.dispatchEvent(mouseDown)
    >>> time.sleep(wait)
    >>> ethan.root.level_mc._txt.text
    '40'
    >>> steven.root.level_mc._txt.text
    '50'
    >>> ethan.root.game_over_mc.balance_mc.black_level_txt.text
    '53'
    >>> steven.root.game_over_mc.balance_mc.black_level_txt.text
    '53'
    >>> ethan.root.turn_mc.white_user_txt.text
    'steven'
    >>> steven.root.turn_mc.white_user_txt.text
    'steven'
    >>> ethan.root.turn_mc.black_user_txt.text
    'ethan'
    >>> steven.root.turn_mc.black_user_txt.text
    'ethan'
    >>> ethan.root.chat_input_txt.text = "that means you will not see the stone played."
    >>> ethan.root.chat_input_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 9.286479)
    >>> time.sleep(sloth * 8.102005)
    >>> steven.root.chat_input_txt.text = "inspired by Batoo?"
    >>> steven.root.chat_input_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 3.824381)
    >>> ethan.root.chat_input_txt.text = "exactly"
    >>> ethan.root.chat_input_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 8.527667)
    >>> time.sleep(sloth * 11.358711)
    >>> ethan.root.game_over_mc.extra_stone_available_mc._0_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 5.854104)
    >>> ethan.root.game_over_mc.balance_mc.black_level_txt.text
    '49'
    >>> ethan.root.chat_input_txt.text = "my current equation is 3 hide = 1 extra stone."
    >>> ethan.root.chat_input_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 28.087847)
    >>> ethan.root.game_over_mc.hide_available_mc._3_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 19.117974)
    >>> ethan.root.game_over_mc.balance_mc.black_level_txt.text
    '55'
    >>> ethan.root.chat_input_txt.text = "3 hide ok?"
    >>> ethan.root.chat_input_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 16.947056)
    >>> steven.root.chat_input_txt.text = "ok, should be interesting"
    >>> steven.root.chat_input_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 8.011690)
    >>> time.sleep(sloth * 10.815168)
    >>> mouse_down_and_sleep(steven, steven.root.game_over_mc.start_mc, wait)
    >>> time.sleep(sloth * 9.262263)
    >>> mouse_down_and_sleep(ethan, ethan.root._4_4_mc, wait)
    >>> time.sleep(sloth * 3.533595)
    >>> mouse_down_and_sleep(ethan, ethan.root._4_4_mc, wait)
    >>> time.sleep(sloth * 8.886071)

    Steven sees black.
    >>> steven.root._4_4_mc.currentLabel
    'black'
    >>> steven.root._4_4_mc.last_move_mc.currentLabel
    'black'
    >>> mouse_down_and_sleep(steven, steven.root._2_6_mc, wait)
    >>> ethan.root.comment_mc.none_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 6.300376)
    >>> time.sleep(sloth * 3.240415)
    >>> mouse_down_and_sleep(ethan, ethan.root.hide_gift_mc.use_mc, wait)
    >>> time.sleep(sloth * 12.627582)
    >>> mouse_down_and_sleep(ethan, ethan.root._6_3_mc, wait)
    >>> time.sleep(sloth * 5.059245)
    >>> mouse_down_and_sleep(ethan, ethan.root._6_3_mc, wait)

    Steven does not see white defend.
    >>> steven.root._3_3_mc.decoration_mc.currentLabel
    'none'

    Ethan does not see egg on top of his last castle.
    >>> ethan.root._5_6_mc.top_move_mc.currentLabel
    'none'

    Steven does not see black's hidden stone.
    >>> steven.root._4_4_mc.last_move_mc.currentLabel
    'black'
    >>> steven.root._6_3_mc.currentLabel
    'empty_white'
    >>> steven.root._6_3_mc.last_move_mc.currentLabel
    'none'
    >>> steven.root.chat_input_txt.text = "i still see a little hammer"
    >>> steven.root.chat_input_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 15.988551)
    >>> ethan.root.chat_input_txt.text = "damn.  thanks for the honesty  ;)"
    >>> ethan.root.chat_input_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 20.194703)
    >>> time.sleep(sloth * 14.133051)
    >>> mouse_down_and_sleep(steven, steven.root._2_2_mc, wait)
    >>> ethan.root.comment_mc.none_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 8.424148)
    >>> time.sleep(sloth * 9.189072)
    >>> mouse_down_and_sleep(ethan, ethan.root._5_6_mc, wait)
    >>> time.sleep(sloth * 9.502779)

    Steven does not see white defend.
    >>> steven.root._3_3_mc.decoration_mc.currentLabel
    'none'

    Ethan does not see egg on top of his last castle.
    >>> ethan.root._5_6_mc.top_move_mc.currentLabel
    'none'
    >>> mouse_down_and_sleep(ethan, ethan.root._5_6_mc, wait)
    >>> time.sleep(sloth * 17.535258)

    Do not transmit removal of hidden move.  Last move updates.
    >>> steven.ambassador.receives[-1].get('_6_3_mc')
    >>> steven.root._4_4_mc.last_move_mc.currentLabel
    'none'
    >>> steven.root._6_3_mc.currentLabel
    'empty_white'
    >>> steven.root._4_4_mc.last_move_mc.currentLabel
    'none'
    >>> steven.root._5_6_mc.currentLabel
    'black'
    >>> steven.root._5_6_mc.last_move_mc.currentLabel
    'black'

    Steven does not see white defend.
    >>> steven.root._3_3_mc.decoration_mc.currentLabel
    'none'

    Ethan does not see egg on top of his last castle.
    >>> ethan.root._5_6_mc.top_move_mc.currentLabel
    'none'
    
    >>> mouse_down_and_sleep(steven, steven.root._5_2_mc, wait)
    >>> time.sleep(sloth * 12.273194)
    >>> mouse_down_and_sleep(ethan, ethan.root._2_4_mc, wait)
    >>> time.sleep(sloth * 7.813703)
    >>> mouse_down_and_sleep(ethan, ethan.root._3_7_mc, wait)
    >>> time.sleep(sloth * 12.411148)
    >>> mouse_down_and_sleep(ethan, ethan.root._6_2_mc, wait)
    >>> time.sleep(sloth * 17.599040)
    >>> mouse_down_and_sleep(ethan, ethan.root._3_7_mc, wait)
    >>> time.sleep(sloth * 7.414559)
    >>> mouse_down_and_sleep(ethan, ethan.root._6_2_mc, wait)
    >>> time.sleep(sloth * 4.698810)
    >>> mouse_down_and_sleep(ethan, ethan.root._6_2_mc, wait)
    >>> time.sleep(sloth * 22.894028)
    >>> mouse_down_and_sleep(steven, steven.root._6_1_mc, wait)
    >>> time.sleep(sloth * 15.634407)
    >>> mouse_down_and_sleep(ethan, ethan.root._7_1_mc, wait)
    >>> steven.root.chat_input_txt.text = "what happens if i place a stone on your invicible stone?"
    >>> steven.root.chat_input_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 8.810962)
    >>> ethan.root.chat_input_txt.text = "it is revealed"
    >>> ethan.root.chat_input_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 12.802310)
    >>> time.sleep(sloth * 13.014823)
    >>> mouse_down_and_sleep(ethan, ethan.root._7_1_mc, wait)
    >>> time.sleep(sloth * 6.145280)
    >>> mouse_down_and_sleep(ethan, ethan.root._3_7_mc, wait)
    >>> time.sleep(sloth * 3.667189)
    >>> mouse_down_and_sleep(ethan, ethan.root._7_1_mc, wait)
    >>> time.sleep(sloth * 3.087180)
    >>> mouse_down_and_sleep(ethan, ethan.root._7_1_mc, wait)
    >>> time.sleep(sloth * 9.101581)
    >>> mouse_down_and_sleep(steven, steven.root._5_1_mc, wait)
    >>> ethan.root.chat_input_txt.text = "stone on stone reveals."
    >>> ethan.root.chat_input_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 4.185325)
    >>> time.sleep(sloth * 6.981511)
    >>> mouse_down_and_sleep(ethan, ethan.root._2_4_mc, wait)
    >>> time.sleep(sloth * 4.793517)
    >>> mouse_down_and_sleep(ethan, ethan.root._3_7_mc, wait)
    >>> time.sleep(sloth * 5.850438)
    >>> mouse_down_and_sleep(ethan, ethan.root._3_7_mc, wait)
    >>> time.sleep(sloth * 10.952673)
    >>> mouse_down_and_sleep(steven, steven.root._3_6_mc, wait)
    >>> ethan.root.comment_mc.none_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 7.892035)
    >>> time.sleep(sloth * 4.948100)
    >>> mouse_down_and_sleep(ethan, ethan.root._4_7_mc, wait)
    >>> time.sleep(sloth * 6.896120)
    >>> mouse_down_and_sleep(ethan, ethan.root._4_6_mc, wait)
    >>> steven.root.chat_input_txt.text = "that's fair, never played batoo before"
    >>> steven.root.chat_input_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 5.652381)
    >>> time.sleep(sloth * 0.671424)
    >>> mouse_down_and_sleep(ethan, ethan.root._4_6_mc, wait)
    >>> time.sleep(sloth * 5.648259)
    >>> mouse_down_and_sleep(steven, steven.root._2_7_mc, wait)
    >>> time.sleep(sloth * 14.082564)
    >>> mouse_down_and_sleep(ethan, ethan.root._2_4_mc, wait)
    >>> time.sleep(sloth * 12.899546)
    >>> mouse_down_and_sleep(ethan, ethan.root._4_7_mc, wait)
    >>> time.sleep(sloth * 6.359302)
    >>> mouse_down_and_sleep(ethan, ethan.root._4_7_mc, wait)
    >>> time.sleep(sloth * 26.838794)
    >>> mouse_down_and_sleep(steven, steven.root._3_3_mc, wait)
    >>> time.sleep(sloth * 12.581838)
    >>> mouse_down_and_sleep(ethan, ethan.root.hide_gift_mc.use_mc, wait)
    >>> time.sleep(sloth * 19.314700)
    >>> mouse_down_and_sleep(ethan, ethan.root._4_3_mc, wait)
    >>> time.sleep(sloth * 9.544000)
    >>> mouse_down_and_sleep(ethan, ethan.root._3_4_mc, wait)
    >>> time.sleep(sloth * 10.463407)
    >>> mouse_down_and_sleep(ethan, ethan.root._3_4_mc, wait)
    >>> time.sleep(sloth * 0.757615)
    >>> ethan.root.gateway_mc.none_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 3.892629)
    >>> time.sleep(sloth * 1.059535)
    >>> mouse_down_and_sleep(steven, steven.root._2_4_mc, wait)
    >>> time.sleep(sloth * 30.019316)
    >>> mouse_down_and_sleep(ethan, ethan.root._7_0_mc, wait)
    >>> time.sleep(sloth * 8.625502)
    >>> mouse_down_and_sleep(ethan, ethan.root._4_3_mc, wait)
    >>> time.sleep(sloth * 4.165532)
    >>> mouse_down_and_sleep(ethan, ethan.root._2_8_mc, wait)
    >>> time.sleep(sloth * 11.334691)
    >>> mouse_down_and_sleep(ethan, ethan.root._4_3_mc, wait)
    >>> time.sleep(sloth * 7.146766)
    >>> mouse_down_and_sleep(ethan, ethan.root._7_0_mc, wait)
    >>> time.sleep(sloth * 6.571865)
    >>> mouse_down_and_sleep(ethan, ethan.root._4_3_mc, wait)
    >>> time.sleep(sloth * 2.529006)
    >>> mouse_down_and_sleep(ethan, ethan.root._4_3_mc, wait)
    >>> time.sleep(sloth * 4.295578)
    >>> mouse_down_and_sleep(steven, steven.root._4_2_mc, wait)
    >>> time.sleep(sloth * 9.886972)
    >>> mouse_down_and_sleep(ethan, ethan.root._7_0_mc, wait)
    >>> time.sleep(sloth * 2.515771)
    >>> mouse_down_and_sleep(ethan, ethan.root._7_0_mc, wait)
    >>> time.sleep(sloth * 6.616691)
    >>> mouse_down_and_sleep(steven, steven.root._5_3_mc, wait)
    >>> time.sleep(sloth * 6.483753)
    >>> mouse_down_and_sleep(ethan, ethan.root._5_4_mc, wait)
    >>> time.sleep(sloth * 4.303381)
    >>> mouse_down_and_sleep(ethan, ethan.root._5_4_mc, wait)
    >>> time.sleep(sloth * 21.858858)
    >>> mouse_down_and_sleep(steven, steven.root._3_5_mc, wait)
    >>> time.sleep(sloth * 12.481307)
    >>> mouse_down_and_sleep(ethan, ethan.root._2_8_mc, wait)
    >>> time.sleep(sloth * 0.998259)
    >>> ethan.root.gateway_mc.none_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 3.385950)
    >>> time.sleep(sloth * 2.141719)
    >>> mouse_down_and_sleep(ethan, ethan.root._2_8_mc, wait)
    >>> time.sleep(sloth * 6.473198)
    >>> mouse_down_and_sleep(ethan, ethan.root._2_8_mc, wait)
    >>> steven.root.chat_input_txt.text = "I think 3 invicible stones is really strong, when the little hammer is gone :)"
    >>> steven.root.chat_input_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 22.447790)
    >>> time.sleep(sloth * 21.776265)
    >>> mouse_down_and_sleep(steven, steven.root._1_8_mc, wait)
    >>> ethan.root.comment_mc.none_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 9.678127)
    >>> time.sleep(sloth * 2.206005)
    >>> mouse_down_and_sleep(ethan, ethan.root._3_8_mc, wait)
    >>> time.sleep(sloth * 4.399599)
    >>> mouse_down_and_sleep(ethan, ethan.root._3_8_mc, wait)
    >>> time.sleep(sloth * 12.009348)
    >>> mouse_down_and_sleep(steven, steven.root._1_7_mc, wait)
    >>> time.sleep(sloth * 6.329387)
    >>> mouse_down_and_sleep(ethan, ethan.root._4_5_mc, wait)
    >>> time.sleep(sloth * 11.642528)
    >>> mouse_down_and_sleep(ethan, ethan.root._4_5_mc, wait)
    >>> time.sleep(sloth * 8.975089)
    >>> mouse_down_and_sleep(steven, steven.root._6_0_mc, wait)
    >>> time.sleep(sloth * 12.909331)
    >>> mouse_down_and_sleep(ethan, ethan.root._7_2_mc, wait)
    >>> steven.root.chat_input_txt.text = "i'll be happy to test more in a later stage"
    >>> steven.root.chat_input_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 0.952363)
    >>> time.sleep(sloth * 4.661495)
    >>> mouse_down_and_sleep(ethan, ethan.root._7_2_mc, wait)
    >>> time.sleep(sloth * 21.755554)
    >>> steven.root.pass_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 14.174232)
    >>> ethan.root.pass_mc.dispatchEvent(mouseDown)
    >>> ethan.root.chat_input_txt.text = "your expertise  would be most helpful!  "
    >>> ethan.root.chat_input_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 5.912238)
    >>> ethan.root.chat_input_txt.text = "and thanks for the game."
    >>> ethan.root.chat_input_mc.dispatchEvent(mouseDown)
    '''

def laurens_click_example():
    r'''Laurens clicks.
    >>> laurens, wait = setup_example(configuration, 
    ...     ('laurens', 'groenewegen') )
    >>> sloth = 0.25 / wait
    >>> laurens.root.lobby_mc.join_mc.enter_btn.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * wait)
    >>> laurens.root.lobby_mc.main_mc._10_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 7.479191)
    >>> laurens.root.lobby_mc._10_mc.extra_stone_5_5_2_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 11.456339)
    >>> time.sleep(sloth * 6.986252)
    >>> mouse_down_and_sleep(laurens, laurens.root.game_over_mc.start_mc, wait)
    >>> laurens.root.game_over_mc.white_computer_mc.enter_mc.dispatchEvent(mouseDown)
    >>> laurens.root.game_over_mc.white_computer_mc.enter_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 4.067250)
    >>> mouse_down_and_sleep(laurens, laurens.root._2_1_mc, wait)
    >>> time.sleep(sloth * 5.407490)
    >>> mouse_down_and_sleep(laurens, laurens.root._3_1_mc, wait)
    >>> time.sleep(sloth * 2.738460)
    >>> mouse_down_and_sleep(laurens, laurens.root._3_1_mc, wait)
    >>> laurens.root.comment_mc.none_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 5.278166)
    >>> time.sleep(sloth * 5.576461)
    >>> mouse_down_and_sleep(laurens, laurens.root._1_2_mc, wait)
    >>> time.sleep(sloth * 5.121719)
    >>> mouse_down_and_sleep(laurens, laurens.root._1_2_mc, wait)
    >>> time.sleep(sloth * 5.030448)
    >>> mouse_down_and_sleep(laurens, laurens.root._1_2_mc, wait)
    >>> time.sleep(sloth * 5.808057)
    >>> mouse_down_and_sleep(laurens, laurens.root._2_2_mc, wait)
    >>> time.sleep(sloth * 7.310187)
    >>> mouse_down_and_sleep(laurens, laurens.root._3_1_mc, wait)
    >>> time.sleep(sloth * 9.090465)
    >>> mouse_down_and_sleep(laurens, laurens.root._3_3_mc, wait)
    >>> time.sleep(sloth * 7.222284)
    >>> mouse_down_and_sleep(laurens, laurens.root._2_0_mc, wait)
    >>> time.sleep(sloth * 9.743676)
    >>> mouse_down_and_sleep(laurens, laurens.root._1_2_mc, wait)
    >>> time.sleep(sloth * 12.414105)
    >>> mouse_down_and_sleep(laurens, laurens.root._1_2_mc, wait)
    >>> time.sleep(sloth * 3.118864)
    >>> mouse_down_and_sleep(laurens, laurens.root._1_2_mc, wait)
    >>> time.sleep(sloth * 5.677159)
    >>> mouse_down_and_sleep(laurens, laurens.root._1_2_mc, wait)
    >>> time.sleep(sloth * 13.051769)
    >>> mouse_down_and_sleep(laurens, laurens.root._4_0_mc, wait)
    >>> time.sleep(sloth * 5.177230)
    >>> mouse_down_and_sleep(laurens, laurens.root._2_2_mc, wait)
    >>> time.sleep(sloth * 5.361529)
    >>> mouse_down_and_sleep(laurens, laurens.root._2_2_mc, wait)
    >>> mouse_down_and_sleep(computer_laurens, computer_laurens.root._2_1_mc, wait)
    >>> time.sleep(sloth * 11.062031)
    >>> mouse_down_and_sleep(laurens, laurens.root.extra_stone_gift_mc.use_mc, wait)
    >>> time.sleep(sloth * 8.564841)
    >>> mouse_down_and_sleep(laurens, laurens.root._2_3_mc, wait)
    >>> time.sleep(sloth * 4.803874)
    >>> mouse_down_and_sleep(laurens, laurens.root._2_4_mc, wait)
    >>> time.sleep(sloth * 4.483760)
    >>> mouse_down_and_sleep(laurens, laurens.root._2_4_mc, wait)
    >>> time.sleep(sloth * 6.648305)
    >>> mouse_down_and_sleep(laurens, laurens.root._2_3_mc, wait)
    >>> time.sleep(sloth * 5.089573)
    >>> mouse_down_and_sleep(laurens, laurens.root._2_3_mc, wait)
    >>> computer_laurens.root.pass_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 6.206839)
    >>> mouse_down_and_sleep(laurens, laurens.root._2_1_mc, wait)
    >>> time.sleep(sloth * 1.205535)
    >>> mouse_down_and_sleep(laurens, laurens.root._2_1_mc, wait)
    >>> time.sleep(sloth * 2.692063)
    >>> mouse_down_and_sleep(laurens, laurens.root._2_1_mc, wait)
    >>> time.sleep(sloth * 1.173987)
    >>> mouse_down_and_sleep(laurens, laurens.root._2_1_mc, wait)
    >>> time.sleep(sloth * 3.046553)
    >>> mouse_down_and_sleep(laurens, laurens.root._1_2_mc, wait)
    >>> time.sleep(sloth * 4.257427)
    >>> mouse_down_and_sleep(laurens, laurens.root._1_2_mc, wait)
    >>> mouse_down_and_sleep(computer_laurens, computer_laurens.root._1_1_mc, wait)
    >>> time.sleep(sloth * 18.825173)
    >>> mouse_down_and_sleep(laurens, laurens.root._0_1_mc, wait)
    >>> time.sleep(sloth * 2.105894)
    >>> mouse_down_and_sleep(laurens, laurens.root._0_1_mc, wait)
    >>> computer_laurens.root.pass_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 12.806042)
    >>> mouse_down_and_sleep(laurens, laurens.root._3_1_mc, wait)
    >>> time.sleep(sloth * 2.670501)
    >>> mouse_down_and_sleep(laurens, laurens.root._3_1_mc, wait)
    >>> mouse_down_and_sleep(computer_laurens, computer_laurens.root._3_2_mc, wait)
    >>> time.sleep(sloth * 8.329666)
    >>> mouse_down_and_sleep(laurens, laurens.root._2_0_mc, wait)
    >>> time.sleep(sloth * 2.355923)
    >>> mouse_down_and_sleep(laurens, laurens.root._2_0_mc, wait)
    >>> mouse_down_and_sleep(computer_laurens, computer_laurens.root._3_3_mc, wait)
    >>> time.sleep(sloth * 6.029521)
    >>> mouse_down_and_sleep(laurens, laurens.root._1_0_mc, wait)
    >>> time.sleep(sloth * 3.504583)
    >>> mouse_down_and_sleep(laurens, laurens.root._1_0_mc, wait)
    >>> computer_laurens.root.pass_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 13.416798)
    >>> mouse_down_and_sleep(laurens, laurens.root._4_2_mc, wait)
    >>> time.sleep(sloth * 2.373796)
    >>> mouse_down_and_sleep(laurens, laurens.root._4_2_mc, wait)
    >>> computer_laurens.root.pass_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 26.427770)
    >>> laurens.root.pass_mc.dispatchEvent(mouseDown)
    >>> laurens.root.level_mc.none_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 7.674295)
    >>> laurens.root.menu_mc.lobby_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 78.133564)
    >>> laurens.root.lobby_mc._10_mc.main_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 9.074191)
    >>> laurens.root.lobby_mc.main_mc.multiplayer_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 13.940276)
    >>> time.sleep(sloth * 4.148604)
    >>> laurens.root.game_over_mc.extra_stone_available_mc._2_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 6.529373)
    >>> laurens.root.game_over_mc.hide_available_mc._5_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 2.960263)
    >>> time.sleep(sloth * 1.761093)
    >>> time.sleep(sloth * 29.461804)
    >>> mouse_down_and_sleep(laurens, laurens.root.game_over_mc.start_mc, wait)
    >>> laurens.root.game_over_mc.white_computer_mc.enter_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 4.649338)
    >>> mouse_down_and_sleep(laurens, laurens.root.game_over_mc.start_mc, wait)
    >>> laurens.root.game_over_mc.white_computer_mc.enter_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 1.326186)
    >>> mouse_down_and_sleep(laurens, laurens.root.game_over_mc.start_mc, wait)
    >>> laurens.root.game_over_mc.white_computer_mc.enter_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 1.582114)
    >>> mouse_down_and_sleep(laurens, laurens.root.game_over_mc.start_mc, wait)
    >>> laurens.root.game_over_mc.white_computer_mc.enter_mc.dispatchEvent(mouseDown)
    >>> laurens.root.game_over_mc.hide_available_mc._0_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 17.784375)
    >>> laurens.root.game_over_mc.extra_stone_available_mc._7_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 2.148230)
    >>> laurens.root.game_over_mc.hide_available_mc._2_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 1.862067)
    >>> time.sleep(sloth * 9.155770)
    >>> mouse_down_and_sleep(laurens, laurens.root.game_over_mc.start_mc, wait)
    >>> laurens.root.game_over_mc.white_computer_mc.enter_mc.dispatchEvent(mouseDown)
    >>> laurens.root.menu_mc.toggle_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 2.794377)
    >>> laurens.root.menu_mc.lobby_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 1.523910)
    >>> laurens.root.lobby_mc._main_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 11.648272)
    >>> laurens.root.lobby_mc.main_mc._20_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 6.574222)
    >>> laurens.root.lobby_mc._20_mc.extra_hide_9_9_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 3.639804)
    >>> time.sleep(sloth * 21.808150)
    >>> mouse_down_and_sleep(laurens, laurens.root.game_over_mc.start_mc, wait)
    >>> laurens.root.game_over_mc.white_computer_mc.enter_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 5.143695)
    >>> mouse_down_and_sleep(laurens, laurens.root._4_3_mc, wait)
    >>> time.sleep(sloth * 1.586812)
    >>> mouse_down_and_sleep(laurens, laurens.root._4_3_mc, wait)
    >>> mouse_down_and_sleep(computer_laurens, computer_laurens.root._5_5_mc, wait)
    >>> time.sleep(sloth * 9.258377)
    >>> mouse_down_and_sleep(laurens, laurens.root._5_4_mc, wait)
    >>> time.sleep(sloth * 1.373989)
    >>> mouse_down_and_sleep(laurens, laurens.root._5_4_mc, wait)
    >>> mouse_down_and_sleep(computer_laurens, computer_laurens.root._6_5_mc, wait)
    >>> time.sleep(sloth * 12.534551)
    >>> mouse_down_and_sleep(laurens, laurens.root._7_5_mc, wait)
    >>> time.sleep(sloth * 0.983685)
    >>> mouse_down_and_sleep(laurens, laurens.root._7_5_mc, wait)
    >>> mouse_down_and_sleep(computer_laurens, computer_laurens.root._7_4_mc, wait)
    >>> time.sleep(sloth * 10.926542)
    >>> mouse_down_and_sleep(laurens, laurens.root._7_6_mc, wait)
    >>> time.sleep(sloth * 1.345643)
    >>> mouse_down_and_sleep(laurens, laurens.root._7_6_mc, wait)
    >>> mouse_down_and_sleep(computer_laurens, computer_laurens.root._6_4_mc, wait)
    >>> time.sleep(sloth * 7.286892)
    >>> mouse_down_and_sleep(laurens, laurens.root._6_3_mc, wait)
    >>> time.sleep(sloth * 1.209197)
    >>> mouse_down_and_sleep(laurens, laurens.root._6_3_mc, wait)
    >>> mouse_down_and_sleep(computer_laurens, computer_laurens.root._6_7_mc, wait)
    >>> time.sleep(sloth * 9.380799)
    >>> mouse_down_and_sleep(laurens, laurens.root._4_5_mc, wait)
    >>> time.sleep(sloth * 1.123403)
    >>> mouse_down_and_sleep(laurens, laurens.root._4_5_mc, wait)
    >>> mouse_down_and_sleep(computer_laurens, computer_laurens.root._2_2_mc, wait)
    >>> time.sleep(sloth * 6.970543)
    >>> mouse_down_and_sleep(laurens, laurens.root._8_4_mc, wait)
    >>> time.sleep(sloth * 1.975853)
    >>> mouse_down_and_sleep(laurens, laurens.root._8_4_mc, wait)
    >>> mouse_down_and_sleep(computer_laurens, computer_laurens.root._7_3_mc, wait)
    >>> time.sleep(sloth * 24.613801)
    >>> mouse_down_and_sleep(laurens, laurens.root._7_2_mc, wait)
    >>> time.sleep(sloth * 4.112242)
    >>> mouse_down_and_sleep(laurens, laurens.root.extra_stone_gift_mc.use_mc, wait)
    >>> time.sleep(sloth * 3.799455)
    >>> mouse_down_and_sleep(laurens, laurens.root._7_2_mc, wait)
    >>> time.sleep(sloth * 1.108360)
    >>> time.sleep(sloth * 2.919016)
    >>> mouse_down_and_sleep(laurens, laurens.root._7_2_mc, wait)
    >>> time.sleep(sloth * 1.319565)
    >>> mouse_down_and_sleep(laurens, laurens.root._7_2_mc, wait)
    >>> time.sleep(sloth * 4.714761)
    >>> mouse_down_and_sleep(laurens, laurens.root._8_3_mc, wait)
    >>> time.sleep(sloth * 1.262236)
    >>> time.sleep(sloth * 3.239355)
    >>> mouse_down_and_sleep(laurens, laurens.root._8_3_mc, wait)
    >>> time.sleep(sloth * 1.223149)
    >>> time.sleep(sloth * 5.233332)
    >>> mouse_down_and_sleep(laurens, laurens.root._8_3_mc, wait)
    >>> time.sleep(sloth * 3.685270)
    >>> mouse_down_and_sleep(laurens, laurens.root._8_3_mc, wait)
    >>> mouse_down_and_sleep(computer_laurens, computer_laurens.root._5_7_mc, wait)
    >>> laurens.root.gateway_mc.none_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 38.864737)
    >>> time.sleep(sloth * 2.027848)
    >>> mouse_down_and_sleep(laurens, laurens.root.hide_gift_mc.use_mc, wait)
    >>> time.sleep(sloth * 6.086671)
    >>> mouse_down_and_sleep(laurens, laurens.root._4_7_mc, wait)
    >>> time.sleep(sloth * 1.201947)
    >>> laurens.root.gateway_mc.none_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 3.650225)
    >>> time.sleep(sloth * 1.846227)
    >>> mouse_down_and_sleep(laurens, laurens.root._4_7_mc, wait)
    >>> time.sleep(sloth * 1.615879)
    >>> mouse_down_and_sleep(laurens, laurens.root._4_7_mc, wait)
    >>> mouse_down_and_sleep(computer_laurens, computer_laurens.root._6_2_mc, wait)
    >>> time.sleep(sloth * 9.174377)
    >>> mouse_down_and_sleep(laurens, laurens.root._5_3_mc, wait)
    >>> time.sleep(sloth * 0.880526)
    >>> laurens.root.gateway_mc.none_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 3.238789)
    >>> time.sleep(sloth * 1.766248)
    >>> mouse_down_and_sleep(laurens, laurens.root._5_3_mc, wait)
    >>> time.sleep(sloth * 3.156044)
    >>> mouse_down_and_sleep(laurens, laurens.root._5_3_mc, wait)
    >>> mouse_down_and_sleep(computer_laurens, computer_laurens.root._6_1_mc, wait)
    >>> time.sleep(sloth * 17.968505)
    >>> mouse_down_and_sleep(laurens, laurens.root._6_0_mc, wait)
    >>> time.sleep(sloth * 3.377989)
    >>> mouse_down_and_sleep(laurens, laurens.root._6_0_mc, wait)
    >>> mouse_down_and_sleep(computer_laurens, computer_laurens.root._7_1_mc, wait)
    >>> time.sleep(sloth * 9.401798)
    >>> mouse_down_and_sleep(laurens, laurens.root.hide_gift_mc.use_mc, wait)
    >>> time.sleep(sloth * 1.920063)
    >>> mouse_down_and_sleep(laurens, laurens.root._8_2_mc, wait)
    >>> time.sleep(sloth * 1.003688)
    >>> laurens.root.gateway_mc.none_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 2.614468)
    >>> time.sleep(sloth * 1.666353)
    >>> mouse_down_and_sleep(laurens, laurens.root._8_2_mc, wait)
    >>> time.sleep(sloth * 3.406255)
    >>> mouse_down_and_sleep(laurens, laurens.root._8_2_mc, wait)
    >>> mouse_down_and_sleep(computer_laurens, computer_laurens.root._2_5_mc, wait)
    >>> time.sleep(sloth * 7.860082)
    >>> mouse_down_and_sleep(laurens, laurens.root._5_6_mc, wait)
    >>> time.sleep(sloth * 1.997536)
    >>> time.sleep(sloth * 3.392643)
    >>> mouse_down_and_sleep(laurens, laurens.root._5_6_mc, wait)
    >>> time.sleep(sloth * 6.769963)
    >>> mouse_down_and_sleep(laurens, laurens.root._5_6_mc, wait)
    >>> mouse_down_and_sleep(computer_laurens, computer_laurens.root._6_6_mc, wait)
    >>> laurens.root.gateway_mc.none_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 3.131989)
    >>> time.sleep(sloth * 12.457538)
    >>> mouse_down_and_sleep(laurens, laurens.root.hide_gift_mc.use_mc, wait)
    >>> time.sleep(sloth * 3.149966)
    >>> mouse_down_and_sleep(laurens, laurens.root._4_6_mc, wait)
    >>> time.sleep(sloth * 1.732510)
    >>> mouse_down_and_sleep(laurens, laurens.root._4_6_mc, wait)
    >>> mouse_down_and_sleep(computer_laurens, computer_laurens.root._3_4_mc, wait)
    >>> time.sleep(sloth * 7.968061)
    >>> mouse_down_and_sleep(laurens, laurens.root.hide_gift_mc.use_mc, wait)
    >>> time.sleep(sloth * 8.862414)
    >>> mouse_down_and_sleep(laurens, laurens.root._2_4_mc, wait)
    >>> time.sleep(sloth * 2.144248)
    >>> mouse_down_and_sleep(laurens, laurens.root._2_4_mc, wait)
    >>> mouse_down_and_sleep(computer_laurens, computer_laurens.root._3_2_mc, wait)
    >>> time.sleep(sloth * 15.136173)
    >>> mouse_down_and_sleep(laurens, laurens.root._7_7_mc, wait)
    >>> time.sleep(sloth * 1.109921)
    >>> laurens.root.gateway_mc.none_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 2.569751)
    >>> time.sleep(sloth * 0.956617)
    >>> mouse_down_and_sleep(laurens, laurens.root._7_7_mc, wait)
    >>> time.sleep(sloth * 1.879336)
    >>> time.sleep(sloth * 2.412774)
    >>> mouse_down_and_sleep(laurens, laurens.root._7_7_mc, wait)
    >>> time.sleep(sloth * 1.599335)
    >>> laurens.root.gateway_mc.none_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 4.097983)
    >>> time.sleep(sloth * 1.212735)
    >>> mouse_down_and_sleep(laurens, laurens.root._7_7_mc, wait)
    >>> time.sleep(sloth * 3.299039)
    >>> mouse_down_and_sleep(laurens, laurens.root._7_7_mc, wait)
    >>> mouse_down_and_sleep(computer_laurens, computer_laurens.root._8_2_mc, wait)
    >>> mouse_down_and_sleep(computer_laurens, computer_laurens.root._4_4_mc, wait)
    >>> time.sleep(sloth * 3.498260)
    >>> laurens.root.gateway_mc.none_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 2.918573)
    >>> time.sleep(sloth * 9.234312)
    >>> mouse_down_and_sleep(laurens, laurens.root._6_8_mc, wait)
    >>> time.sleep(sloth * 1.277639)
    >>> laurens.root.gateway_mc.none_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 2.290111)
    >>> time.sleep(sloth * 1.374480)
    >>> mouse_down_and_sleep(laurens, laurens.root._6_8_mc, wait)
    >>> time.sleep(sloth * 2.853819)
    >>> mouse_down_and_sleep(laurens, laurens.root._6_8_mc, wait)
    >>> mouse_down_and_sleep(computer_laurens, computer_laurens.root._4_6_mc, wait)
    >>> mouse_down_and_sleep(computer_laurens, computer_laurens.root._4_7_mc, wait)
    >>> mouse_down_and_sleep(computer_laurens, computer_laurens.root._2_7_mc, wait)
    >>> time.sleep(sloth * 14.552983)
    >>> mouse_down_and_sleep(laurens, laurens.root._5_8_mc, wait)
    >>> time.sleep(sloth * 2.757600)
    >>> mouse_down_and_sleep(laurens, laurens.root._5_8_mc, wait)
    >>> mouse_down_and_sleep(computer_laurens, computer_laurens.root._4_1_mc, wait)
    >>> time.sleep(sloth * 52.839767)
    >>> mouse_down_and_sleep(laurens, laurens.root._5_1_mc, wait)
    >>> time.sleep(sloth * 1.386052)
    >>> laurens.root.gateway_mc.none_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 2.902607)
    >>> time.sleep(sloth * 1.120756)
    >>> mouse_down_and_sleep(laurens, laurens.root._5_1_mc, wait)
    >>> time.sleep(sloth * 3.255497)
    >>> mouse_down_and_sleep(laurens, laurens.root._5_1_mc, wait)
    >>> mouse_down_and_sleep(computer_laurens, computer_laurens.root._5_2_mc, wait)
    >>> time.sleep(sloth * 13.807169)
    >>> mouse_down_and_sleep(laurens, laurens.root._5_0_mc, wait)
    >>> time.sleep(sloth * 4.311302)
    >>> mouse_down_and_sleep(laurens, laurens.root._5_0_mc, wait)
    >>> mouse_down_and_sleep(computer_laurens, computer_laurens.root._4_2_mc, wait)
    >>> time.sleep(sloth * 25.605835)
    >>> mouse_down_and_sleep(laurens, laurens.root._3_3_mc, wait)
    >>> time.sleep(sloth * 1.733677)
    >>> mouse_down_and_sleep(laurens, laurens.root._3_3_mc, wait)
    >>> mouse_down_and_sleep(computer_laurens, computer_laurens.root._2_3_mc, wait)
    >>> time.sleep(sloth * 9.773685)
    >>> mouse_down_and_sleep(laurens, laurens.root._3_5_mc, wait)
    >>> time.sleep(sloth * 2.045599)
    >>> mouse_down_and_sleep(laurens, laurens.root._3_5_mc, wait)
    >>> mouse_down_and_sleep(computer_laurens, computer_laurens.root._1_4_mc, wait)
    >>> time.sleep(sloth * 13.642547)
    >>> mouse_down_and_sleep(laurens, laurens.root._3_4_mc, wait)
    >>> time.sleep(sloth * 1.235187)
    >>> laurens.root.gateway_mc.none_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 2.801216)
    >>> time.sleep(sloth * 1.409646)
    >>> mouse_down_and_sleep(laurens, laurens.root._3_4_mc, wait)
    >>> time.sleep(sloth * 2.997886)
    >>> mouse_down_and_sleep(laurens, laurens.root._3_4_mc, wait)
    >>> mouse_down_and_sleep(computer_laurens, computer_laurens.root._1_5_mc, wait)
    >>> time.sleep(sloth * 16.242607)
    >>> mouse_down_and_sleep(laurens, laurens.root._8_1_mc, wait)
    >>> time.sleep(sloth * 1.369273)
    >>> laurens.root.gateway_mc.none_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 2.806063)
    >>> time.sleep(sloth * 1.016625)
    >>> mouse_down_and_sleep(laurens, laurens.root._8_1_mc, wait)
    >>> time.sleep(sloth * 3.485422)
    >>> mouse_down_and_sleep(laurens, laurens.root._8_1_mc, wait)
    >>> mouse_down_and_sleep(computer_laurens, computer_laurens.root._7_0_mc, wait)
    >>> time.sleep(sloth * 24.161195)
    >>> mouse_down_and_sleep(laurens, laurens.root._3_7_mc, wait)
    >>> time.sleep(sloth * 3.023327)
    >>> mouse_down_and_sleep(laurens, laurens.root._3_7_mc, wait)
    >>> mouse_down_and_sleep(computer_laurens, computer_laurens.root._2_8_mc, wait)
    >>> time.sleep(sloth * 9.467042)
    >>> mouse_down_and_sleep(laurens, laurens.root._2_6_mc, wait)
    >>> time.sleep(sloth * 2.147742)
    >>> mouse_down_and_sleep(laurens, laurens.root._2_6_mc, wait)
    >>> mouse_down_and_sleep(computer_laurens, computer_laurens.root._1_6_mc, wait)
    >>> time.sleep(sloth * 20.092666)
    >>> mouse_down_and_sleep(laurens, laurens.root._3_6_mc, wait)
    >>> time.sleep(sloth * 2.529299)
    >>> mouse_down_and_sleep(laurens, laurens.root._3_6_mc, wait)
    >>> mouse_down_and_sleep(computer_laurens, computer_laurens.root._3_8_mc, wait)
    >>> time.sleep(sloth * 6.776575)
    >>> mouse_down_and_sleep(laurens, laurens.root._1_7_mc, wait)
    >>> time.sleep(sloth * 3.117888)
    >>> mouse_down_and_sleep(laurens, laurens.root._1_7_mc, wait)
    >>> mouse_down_and_sleep(computer_laurens, computer_laurens.root._1_8_mc, wait)
    >>> time.sleep(sloth * 12.994457)
    >>> mouse_down_and_sleep(laurens, laurens.root._0_7_mc, wait)
    >>> time.sleep(sloth * 2.763519)
    >>> mouse_down_and_sleep(laurens, laurens.root._0_7_mc, wait)
    >>> mouse_down_and_sleep(computer_laurens, computer_laurens.root._0_6_mc, wait)
    >>> time.sleep(sloth * 25.806958)
    >>> mouse_down_and_sleep(laurens, laurens.root._4_8_mc, wait)
    >>> time.sleep(sloth * 3.827812)
    >>> mouse_down_and_sleep(laurens, laurens.root._4_8_mc, wait)
    >>> mouse_down_and_sleep(computer_laurens, computer_laurens.root._0_8_mc, wait)
    >>> time.sleep(sloth * 11.518645)
    >>> mouse_down_and_sleep(laurens, laurens.root._1_3_mc, wait)
    >>> time.sleep(sloth * 6.653526)
    >>> mouse_down_and_sleep(laurens, laurens.root._1_3_mc, wait)
    >>> mouse_down_and_sleep(computer_laurens, computer_laurens.root._1_2_mc, wait)
    >>> time.sleep(sloth * 13.288611)
    >>> mouse_down_and_sleep(laurens, laurens.root._0_2_mc, wait)
    >>> time.sleep(sloth * 3.704476)
    >>> mouse_down_and_sleep(laurens, laurens.root._0_2_mc, wait)
    >>> mouse_down_and_sleep(computer_laurens, computer_laurens.root._0_1_mc, wait)
    >>> time.sleep(sloth * 12.652090)
    >>> mouse_down_and_sleep(laurens, laurens.root._0_4_mc, wait)
    >>> time.sleep(sloth * 15.769821)
    >>> mouse_down_and_sleep(laurens, laurens.root._0_7_mc, wait)
    >>> time.sleep(sloth * 2.335627)
    >>> mouse_down_and_sleep(laurens, laurens.root._0_7_mc, wait)
    >>> mouse_down_and_sleep(computer_laurens, computer_laurens.root._1_7_mc, wait)
    >>> time.sleep(sloth * 22.232857)
    >>> mouse_down_and_sleep(laurens, laurens.root._3_1_mc, wait)
    >>> time.sleep(sloth * 2.197928)
    >>> mouse_down_and_sleep(laurens, laurens.root._3_1_mc, wait)
    >>> mouse_down_and_sleep(computer_laurens, computer_laurens.root._4_0_mc, wait)
    >>> time.sleep(sloth * 16.748654)
    >>> mouse_down_and_sleep(laurens, laurens.root._0_0_mc, wait)
    >>> time.sleep(sloth * 2.217815)
    >>> mouse_down_and_sleep(laurens, laurens.root._0_0_mc, wait)
    >>> mouse_down_and_sleep(computer_laurens, computer_laurens.root._8_0_mc, wait)
    >>> time.sleep(sloth * 19.760658)
    >>> mouse_down_and_sleep(laurens, laurens.root._1_1_mc, wait)
    >>> time.sleep(sloth * 2.156591)
    >>> mouse_down_and_sleep(laurens, laurens.root._1_1_mc, wait)
    >>> mouse_down_and_sleep(computer_laurens, computer_laurens.root._0_3_mc, wait)
    >>> time.sleep(sloth * 14.606016)
    >>> mouse_down_and_sleep(laurens, laurens.root._2_1_mc, wait)
    >>> time.sleep(sloth * 2.447701)
    >>> mouse_down_and_sleep(laurens, laurens.root._2_1_mc, wait)
    >>> mouse_down_and_sleep(computer_laurens, computer_laurens.root._0_1_mc, wait)
    >>> time.sleep(sloth * 14.622478)
    >>> mouse_down_and_sleep(laurens, laurens.root._0_2_mc, wait)
    >>> time.sleep(sloth * 15.051117)
    >>> mouse_down_and_sleep(laurens, laurens.root._1_0_mc, wait)
    >>> time.sleep(sloth * 1.432438)
    >>> laurens.root.gateway_mc.none_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 3.482648)
    >>> time.sleep(sloth * 2.909777)
    >>> mouse_down_and_sleep(laurens, laurens.root._3_0_mc, wait)
    >>> time.sleep(sloth * 3.901983)
    >>> mouse_down_and_sleep(laurens, laurens.root._3_0_mc, wait)
    >>> mouse_down_and_sleep(computer_laurens, computer_laurens.root._0_2_mc, wait)
    >>> time.sleep(sloth * 20.882686)
    >>> mouse_down_and_sleep(laurens, laurens.root._0_4_mc, wait)
    >>> time.sleep(sloth * 1.311028)
    >>> laurens.root.gateway_mc.none_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 2.696579)
    >>> time.sleep(sloth * 1.042953)
    >>> mouse_down_and_sleep(laurens, laurens.root._0_4_mc, wait)
    >>> time.sleep(sloth * 4.423067)
    >>> mouse_down_and_sleep(laurens, laurens.root._0_4_mc, wait)
    >>> computer_laurens.root.pass_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 58.634754)
    >>> laurens.root.pass_mc.dispatchEvent(mouseDown)
    >>> laurens.root.menu_mc.lobby_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 16.341560)
    >>> laurens.root.lobby_mc._20_mc.extra_hide_7_7_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 2.171254)
    '''

def laurens_defend_example():
    '''LAURENS DEFENDS, SO HE SEES A ROOF ON HIS CASTLE.
    >>> code_unit.inline_examples(
    ...     ethan_lukasz_begin_example.__doc__, 
    ...     locals(), globals(), 
    ...     verify_examples = False)

    >>> wait = 5.0 / black._speed
    >>> laurens = black
    >>> gnugo = white
    >>> mouse_down_and_sleep(black, black.root.lobby_mc._00_mc.score_5_5_3_mc,
    ...     wait)

    LAURENS CLICKS ON START BUTTON.
    >>> mouse_down_and_sleep(black, black.root.game_over_mc.start_mc, wait)

    FOR REPLAY, COMPUTER IS NOT PLAYING.
    >>> property_diff(black, black.root.game_over_mc.white_computer_mc, 'currentLabel', 'computer')
    >>> mouse_down_and_sleep(black, black.root.game_over_mc.white_computer_mc.enter_mc, wait)
    >>> property_diff(black, black.root.game_over_mc.white_computer_mc, 'currentLabel', 'none')
    >>> black.root.defend_mc.currentLabel
    'show'
    >>> black.root.decoration_mc.currentLabel
    'show'

    >>> mouse_down_and_sleep(black, black.root._3_3_mc, wait)
    >>> mouse_down_and_sleep(black, black.root._3_3_mc, wait)
    >>> black.root._2_2_mc.black_shape_mc.defend_mc.currentLabel
    'none'
    >>> black.root._2_2_mc.black_shape_mc.attack_mc.defend_mc.currentLabel
    'none'
    >>> mouse_down_and_sleep(black, black.root._2_2_mc, wait)
    >>> black.root._1_2_mc.decoration_mc.currentLabel
    'black_attack'
    >>> black.root._2_2_mc.black_shape_mc.defend_mc.currentLabel
    'show'
    >>> black.root._2_2_mc.black_shape_mc.attack_mc.defend_mc.currentLabel
    'show'
    >>> black.root._2_2_mc.black_shape_mc.attack_mc.currentLabel
    '_0000'
    >>> mouse_down_and_sleep(black, black.root._2_2_mc, wait)

    LAURENS SEES BLUE ROOF AND RED DOOR ON CASTLE.
    >>> black.root._2_2_mc.black_shape_mc.defend_mc.currentLabel
    'show'
    >>> black.root._2_2_mc.black_shape_mc.attack_mc.defend_mc.currentLabel
    'show'
    >>> black.root._2_2_mc.black_shape_mc.attack_mc.currentLabel
    '_0000'
    >>> mouse_down_and_sleep(white, white.root._2_1_mc, wait)

    CONNECT ATTACK HAS DIFFERENT SYMBOL, SO FLASH RESETS ATTACK LABEL.
    THEREFORE, ATTACK SYMBOL MUST SPAN ALL SHAPES.
    >>> ## black.root._2_2_mc.black_shape_mc.defend_mc.gotoAndPlay('none')
    >>> ## black.root._2_2_mc.black_shape_mc.attack_mc.defend_mc.gotoAndPlay('none')
    >>> ## black.root._2_2_mc.black_shape_mc.attack_mc.gotoAndPlay('none')
    
    >>> black.root._1_2_mc.dispatchEvent(mouseDown)
    >>> time.sleep(wait)

    LAURENS STILL SEES BLUE ROOF.  BATTLEMENT UPDATES.
    >>> black.root._2_2_mc.black_shape_mc.defend_mc.currentLabel
    'show'
    >>> black.root._2_2_mc.black_shape_mc.attack_mc.defend_mc.currentLabel
    'show'
    >>> black.root._2_2_mc.black_shape_mc.attack_mc.currentLabel
    '_1000'

    '''

def kyung_first_animation_pretend_snippet():
    '''
    Kyung sees an empty field.
    >>> kyung.root.cursor_mc.act_mc.gotoAndPlay('play')
    >>> kyung.root._3_3_mc.gotoAndPlay('empty_black') # pretend
    >>> kyung.root._3_3_mc.formation_mc.gotoAndPlay('none') # pretend
    >>> kyung.root._1_1_mc.decoration_mc.gotoAndPlay('none') # pretend
    >>> kyung.root._1_5_mc.decoration_mc.gotoAndPlay('none') # pretend
    >>> kyung.root._5_1_mc.decoration_mc.gotoAndPlay('none') # pretend
    >>> kyung.root._5_5_mc.decoration_mc.gotoAndPlay('none') # pretend
    >>> kyung.root._3_3_mc.black_shape_mc.defend_mc.gotoAndPlay('none') # pretend
    >>> kyung.root._2_1_mc.decoration_mc.gotoAndPlay('none') # pretend
    >>> kyung.root._2_5_mc.decoration_mc.gotoAndPlay('none') # pretend
    >>> kyung.root._1_2_mc.decoration_mc.gotoAndPlay('none') # pretend
    >>> kyung.root._5_2_mc.decoration_mc.gotoAndPlay('none') # pretend
    >>> kyung.root._1_4_mc.decoration_mc.gotoAndPlay('none') # pretend
    >>> kyung.root._4_1_mc.decoration_mc.gotoAndPlay('none') # pretend
    >>> kyung.root._4_5_mc.decoration_mc.gotoAndPlay('none') # pretend
    >>> kyung.root._5_4_mc.decoration_mc.gotoAndPlay('none') # pretend

    >>> kyung.root._3_1_mc.decoration_mc.gotoAndPlay('none') # pretend
    >>> kyung.root._3_5_mc.decoration_mc.gotoAndPlay('none') # pretend
    >>> kyung.root._1_3_mc.decoration_mc.gotoAndPlay('none') # pretend
    >>> kyung.root._5_3_mc.decoration_mc.gotoAndPlay('none') # pretend
    >>> kyung.root._2_2_mc.decoration_mc.gotoAndPlay('none') # pretend
    >>> kyung.root._4_2_mc.decoration_mc.gotoAndPlay('none') # pretend
    >>> kyung.root._2_4_mc.decoration_mc.gotoAndPlay('none') # pretend
    >>> kyung.root._4_4_mc.decoration_mc.gotoAndPlay('none') # pretend

    >>> kyung.root._3_2_mc.decoration_mc.gotoAndPlay('none') # pretend
    >>> kyung.root._3_4_mc.decoration_mc.gotoAndPlay('none') # pretend
    >>> kyung.root._2_3_mc.decoration_mc.gotoAndPlay('none') # pretend
    >>> kyung.root._4_3_mc.decoration_mc.gotoAndPlay('none') # pretend
    >>> kyung.root._3_3_mc.black_shape_mc.attack_mc.gotoAndPlay('none') # pretend
    >>> kyung.root._4_4_mc.top_move_mc.gotoAndPlay('none') # pretend

    Kyung builds base, top move.  Here is what Kyung sees.
    Each 0.25 seconds +/- 0.0625, Kyung sees an effect.
    >>> lag = 4.0
    >>> # period = 0.25 # too quick with/out delayed animations
    >>> # period = 0.5 # too quick with/out delayed animations
    >>> # period = 4.0 / 8.0 # after a few viewings, ok witout delayed animation
    >>> # period = 5.0 / 8.0 # a bit slow without animations
    >>> # period = 0.75 # too quick with delayed animations
    >>> # period = 1.0 # legible transition, a bit slow, master/slave lag
    >>> period = 2.0 # legible transition, a bit slow
    >>> # period = 1.0 # unclear, boring with delayed animation
    >>> # period = 3.0 # clear, boring
    >>> 1.0 / 16
    0.0625
    >>> margin = 0.0625
    >>> time.sleep(lag * kyung._speed)

    Kyung clicks.
    >>> ## kyung.root._3_3_mc.dispatchEvent(mouseDown) # pretend
    >>> time.sleep(margin * kyung._speed)

    Builders set up scaffold.
    >>> kyung.root._3_3_mc.gotoAndPlay('preview_black') # pretend

    Build on client takes exactly lag seconds to complete +/- margin seconds.
    Kyung sees progress bar and building animation.
    >>> time.sleep((lag - (2 * margin)) * kyung._speed)
    >>> kyung.root._3_3_mc.currentLabel
    'preview_black'

    >>> time.sleep((2.0 * margin) * kyung._speed)

    Builders tear down scaffolding.  Bunker appears.  Outline appears.  
    >>> kyung.root._3_3_mc.gotoAndPlay('question_black') # pretend

    Peasants build catapults beside bunker.
    >>> time.sleep((period - (2 * margin)) * kyung._speed)
    >>> kyung.root._3_2_mc.decoration_mc.gotoAndPlay('none') # pretend
    >>> kyung.root._3_4_mc.decoration_mc.gotoAndPlay('none') # pretend
    >>> kyung.root._2_3_mc.decoration_mc.gotoAndPlay('none') # pretend
    >>> kyung.root._4_3_mc.decoration_mc.gotoAndPlay('none') # pretend
    >>> time.sleep((2.0 * margin) * kyung._speed)
    >>> kyung.root._3_2_mc.decoration_mc.gotoAndPlay('black_attack') # pretend
    >>> kyung.root._3_4_mc.decoration_mc.gotoAndPlay('black_attack') # pretend
    >>> kyung.root._2_3_mc.decoration_mc.gotoAndPlay('black_attack') # pretend
    >>> kyung.root._4_3_mc.decoration_mc.gotoAndPlay('black_attack') # pretend
    
    Peasants build catapults near bunker.
    >>> time.sleep((period - (2 * margin)) * kyung._speed)
    >>> kyung.root._3_1_mc.decoration_mc.gotoAndPlay('none') # pretend
    >>> kyung.root._3_5_mc.decoration_mc.gotoAndPlay('none') # pretend
    >>> kyung.root._1_3_mc.decoration_mc.gotoAndPlay('none') # pretend
    >>> kyung.root._5_3_mc.decoration_mc.gotoAndPlay('none') # pretend
    >>> kyung.root._2_2_mc.decoration_mc.gotoAndPlay('none') # pretend
    >>> kyung.root._4_2_mc.decoration_mc.gotoAndPlay('none') # pretend
    >>> kyung.root._2_4_mc.decoration_mc.gotoAndPlay('none') # pretend
    >>> kyung.root._4_4_mc.decoration_mc.gotoAndPlay('none') # pretend
    >>> time.sleep((2.0 * margin) * kyung._speed)
    >>> kyung.root._3_1_mc.decoration_mc.gotoAndPlay('black_attack') # pretend
    >>> kyung.root._3_5_mc.decoration_mc.gotoAndPlay('black_attack') # pretend
    >>> kyung.root._1_3_mc.decoration_mc.gotoAndPlay('black_attack') # pretend
    >>> kyung.root._5_3_mc.decoration_mc.gotoAndPlay('black_attack') # pretend
    >>> kyung.root._2_2_mc.decoration_mc.gotoAndPlay('black_attack') # pretend
    >>> kyung.root._4_2_mc.decoration_mc.gotoAndPlay('black_attack') # pretend
    >>> kyung.root._2_4_mc.decoration_mc.gotoAndPlay('black_attack') # pretend
    >>> kyung.root._4_4_mc.decoration_mc.gotoAndPlay('black_attack') # pretend

    Knights build catapults far from bunker.
    >>> time.sleep((period - (2 * margin)) * kyung._speed)
    >>> kyung.root._2_1_mc.decoration_mc.gotoAndPlay('none') # pretend
    >>> kyung.root._2_5_mc.decoration_mc.gotoAndPlay('none') # pretend
    >>> kyung.root._1_2_mc.decoration_mc.gotoAndPlay('none') # pretend
    >>> kyung.root._5_2_mc.decoration_mc.gotoAndPlay('none') # pretend
    >>> kyung.root._1_4_mc.decoration_mc.gotoAndPlay('none') # pretend
    >>> kyung.root._4_1_mc.decoration_mc.gotoAndPlay('none') # pretend
    >>> kyung.root._4_5_mc.decoration_mc.gotoAndPlay('none') # pretend
    >>> kyung.root._5_4_mc.decoration_mc.gotoAndPlay('none') # pretend
    >>> time.sleep((2.0 * margin) * kyung._speed)
    >>> kyung.root._2_1_mc.decoration_mc.gotoAndPlay('black_attack') # pretend
    >>> kyung.root._2_5_mc.decoration_mc.gotoAndPlay('black_attack') # pretend
    >>> kyung.root._1_2_mc.decoration_mc.gotoAndPlay('black_attack') # pretend
    >>> kyung.root._5_2_mc.decoration_mc.gotoAndPlay('black_attack') # pretend
    >>> kyung.root._1_4_mc.decoration_mc.gotoAndPlay('black_attack') # pretend
    >>> kyung.root._4_1_mc.decoration_mc.gotoAndPlay('black_attack') # pretend
    >>> kyung.root._4_5_mc.decoration_mc.gotoAndPlay('black_attack') # pretend
    >>> kyung.root._5_4_mc.decoration_mc.gotoAndPlay('black_attack') # pretend
    
    Far away from the bunker, monks build shrines.
    >>> time.sleep((period - (2 * margin)) * kyung._speed)
    >>> kyung.root._1_1_mc.decoration_mc.gotoAndPlay('none') # pretend
    >>> kyung.root._1_5_mc.decoration_mc.gotoAndPlay('none') # pretend
    >>> kyung.root._5_1_mc.decoration_mc.gotoAndPlay('none') # pretend
    >>> kyung.root._5_5_mc.decoration_mc.gotoAndPlay('none') # pretend
    >>> time.sleep((2.0 * margin) * kyung._speed)
    >>> kyung.root._1_1_mc.decoration_mc.gotoAndPlay('black_defend') # pretend
    >>> kyung.root._1_5_mc.decoration_mc.gotoAndPlay('black_defend') # pretend
    >>> kyung.root._5_1_mc.decoration_mc.gotoAndPlay('black_defend') # pretend
    >>> kyung.root._5_5_mc.decoration_mc.gotoAndPlay('black_defend') # pretend

    Fanfare.

    Mason builds temple.
    >>> time.sleep((period - (2 * margin)) * kyung._speed)
    >>> kyung.root._3_3_mc.formation_mc.gotoAndPlay('none') # pretend
    >>> kyung.root._3_3_mc.black_shape_mc.defend_mc.gotoAndPlay('none') # pretend
    >>> time.sleep((2.0 * margin) * kyung._speed)
    >>> kyung.root._3_3_mc.black_shape_mc.defend_mc.gotoAndPlay('show') # pretend
    >>> kyung.root._3_3_mc.formation_mc.gotoAndPlay('black_attack_defend') # pretend

    Freelance builds barracks.
    >>> time.sleep((period - (2 * margin)) * kyung._speed)
    >>> kyung.root._3_3_mc.black_shape_mc.attack_mc.gotoAndPlay('none') # pretend
    >>> time.sleep((2.0 * margin) * kyung._speed)
    >>> kyung.root._3_3_mc.black_shape_mc.attack_mc.gotoAndPlay('_0000') # pretend

    Nearby, a snow dragon lays an egg.
    >>> time.sleep(period * kyung._speed)
    >>> time.sleep((period - (2 * margin)) * kyung._speed)
    >>> kyung.root._4_4_mc.top_move_mc.gotoAndPlay('none') # pretend
    >>> time.sleep((2 * margin) * kyung._speed)
    >>> kyung.root._4_4_mc.top_move_mc.gotoAndPlay('white') # pretend

    Question mark disappears from cursor.
    Question mark appears and bounces.
    >>> time.sleep((period - (2 * margin)) * kyung._speed)
    >>> kyung.root.cursor_mc.act_mc.gotoAndPlay('play') # pretend
    >>> kyung.root._3_3_mc.currentLabel
    'question_black'
    >>> time.sleep((2 * margin) * kyung._speed)
    >>> kyung.root.cursor_mc.act_mc.gotoAndPlay('preview') # pretend
    >>> kyung.root._3_3_mc.gotoAndPlay('question_black_repeat') # pretend


    decoration, top_move, delay
    preview animation takes about 1 second, so repeats 3+ times.  huh?
        >_< unh
    question mark toggles, which distracts me.
        >_< huh?
    delayed appearance looks like loading lag.
        >_< ho hum
    master publishes to slave which has its own lag.
        >_< uh oh
    is master sending messages to deliver causing client not to imitate?
    egg appears.  i do not notice.
        >_< hm?
    hammer of cursor occludes hammer of building.
        >_< huh?
    what does catapult have to do with fire of strike?  or with knight?
        >_< huh?
    '''
    
def kyung_first_animation_snippet():
    '''
    Kyung sees an empty field.
    >>> kyung.root.cursor_mc.act_mc.gotoAndPlay('play')
    >>> kyung.root._3_3_mc.currentLabel
    'empty_black'
    >>> kyung.root._3_3_mc.formation_mc.currentLabel
    'none'
    >>> kyung.root._1_1_mc.decoration_mc.currentLabel
    'none'
    >>> kyung.root._1_5_mc.decoration_mc.currentLabel
    'none'
    >>> kyung.root._5_1_mc.decoration_mc.currentLabel
    'none'
    >>> kyung.root._5_5_mc.decoration_mc.currentLabel
    'none'
    >>> kyung.root._3_3_mc.black_shape_mc.defend_mc.currentLabel
    'none'
    >>> kyung.root._2_1_mc.decoration_mc.currentLabel
    'none'
    >>> kyung.root._2_5_mc.decoration_mc.currentLabel
    'none'
    >>> kyung.root._1_2_mc.decoration_mc.currentLabel
    'none'
    >>> kyung.root._5_2_mc.decoration_mc.currentLabel
    'none'
    >>> kyung.root._1_4_mc.decoration_mc.currentLabel
    'none'
    >>> kyung.root._4_1_mc.decoration_mc.currentLabel
    'none'
    >>> kyung.root._4_5_mc.decoration_mc.currentLabel
    'none'
    >>> kyung.root._5_4_mc.decoration_mc.currentLabel
    'none'

    >>> kyung.root._3_1_mc.decoration_mc.currentLabel
    'none'
    >>> kyung.root._3_5_mc.decoration_mc.currentLabel
    'none'
    >>> kyung.root._1_3_mc.decoration_mc.currentLabel
    'none'
    >>> kyung.root._5_3_mc.decoration_mc.currentLabel
    'none'
    >>> kyung.root._2_2_mc.decoration_mc.currentLabel
    'none'
    >>> kyung.root._4_2_mc.decoration_mc.currentLabel
    'none'
    >>> kyung.root._2_4_mc.decoration_mc.currentLabel
    'none'
    >>> kyung.root._4_4_mc.decoration_mc.currentLabel
    'none'

    >>> kyung.root._3_2_mc.decoration_mc.currentLabel
    'none'
    >>> kyung.root._3_4_mc.decoration_mc.currentLabel
    'none'
    >>> kyung.root._2_3_mc.decoration_mc.currentLabel
    'none'
    >>> kyung.root._4_3_mc.decoration_mc.currentLabel
    'none'
    >>> kyung.root._3_3_mc.black_shape_mc.attack_mc.currentLabel
    'none'
    >>> kyung.root._4_4_mc.top_move_mc.currentLabel
    'none'

    Kyung builds base, top move.  Here is what Kyung sees.
    Each period seconds +/- margin, Kyung sees an effect.
    >>> lag = 4.0
    >>> # period = 0.25 # too quick with/out delayed animations
    >>> # period = 0.5 # too quick with/out delayed animations
    >>> period = 4.0 / 8.0 # after a few viewings, ok witout delayed animation
    >>> # period = 5.0 / 8.0 # a bit slow without animations
    >>> # period = 0.75 # too quick with delayed animations
    >>> # period = 1.0 # legible transition, a bit slow, master/slave lag
    >>> # period = 2.0 # legible transition, a bit slow
    >>> # period = 1.0 # unclear, boring with delayed animation
    >>> # period = 3.0 # clear, boring
    >>> 1.0 / 16
    0.0625
    >>> margin = 0.0625
    >>> time.sleep(lag * kyung._speed)

    Kyung clicks.
        >>> ## time.clock()
    >>> kyung.root._3_3_mc.dispatchEvent(mouseDown)
    >>> time.sleep(margin * kyung._speed)

    Builders set up scaffold.
    >>> kyung.root._3_3_mc.currentLabel
    'preview_black'

    Build on client takes exactly lag seconds to complete +/- margin seconds.
    Kyung sees progress bar and building animation.
    >>> time.sleep((lag - (2 * margin)) * kyung._speed)
        >>> ## time.clock()
        >>> ## from pprint import pprint
        >>> ## pprint(kyung.ambassador.receives[-1])
    >>> kyung.root._3_3_mc.currentLabel
    'preview_black'

    >>> time.sleep((2.0 * margin) * kyung._speed)

    Builders tear down scaffolding.  Bunker appears.  Outline appears.  
    >>> kyung.root._3_3_mc.currentLabel
    'question_black'

#    Knights build catapults beside bunker.
#    >>> time.sleep((period - (2 * margin)) * kyung._speed)
#    >>> kyung.root._3_2_mc.decoration_mc.currentLabel
#    'none'
#    >>> kyung.root._3_4_mc.decoration_mc.currentLabel
#    'none'
#    >>> kyung.root._2_3_mc.decoration_mc.currentLabel
#    'none'
#    >>> kyung.root._4_3_mc.decoration_mc.currentLabel
#    'none'
#    >>> time.sleep((2.0 * margin) * kyung._speed)
#    >>> kyung.root._3_2_mc.decoration_mc.currentLabel
#    'black_attack'
#    >>> kyung.root._3_4_mc.decoration_mc.currentLabel
#    'black_attack'
#    >>> kyung.root._2_3_mc.decoration_mc.currentLabel
#    'black_attack'
#    >>> kyung.root._4_3_mc.decoration_mc.currentLabel
#    'black_attack'
#    
#    Knights build catapults near bunker.
#    >>> time.sleep((period - (2 * margin)) * kyung._speed)
#    >>> kyung.root._3_1_mc.decoration_mc.currentLabel
#    'none'
#    >>> kyung.root._3_5_mc.decoration_mc.currentLabel
#    'none'
#    >>> kyung.root._1_3_mc.decoration_mc.currentLabel
#    'none'
#    >>> kyung.root._5_3_mc.decoration_mc.currentLabel
#    'none'
#    >>> kyung.root._2_2_mc.decoration_mc.currentLabel
#    'none'
#    >>> kyung.root._4_2_mc.decoration_mc.currentLabel
#    'none'
#    >>> kyung.root._2_4_mc.decoration_mc.currentLabel
#    'none'
#    >>> kyung.root._4_4_mc.decoration_mc.currentLabel
#    'none'
#    >>> time.sleep((2.0 * margin) * kyung._speed)
#    >>> kyung.root._3_1_mc.decoration_mc.currentLabel
#    'black_attack'
#    >>> kyung.root._3_5_mc.decoration_mc.currentLabel
#    'black_attack'
#    >>> kyung.root._1_3_mc.decoration_mc.currentLabel
#    'black_attack'
#    >>> kyung.root._5_3_mc.decoration_mc.currentLabel
#    'black_attack'
#    >>> kyung.root._2_2_mc.decoration_mc.currentLabel
#    'black_attack'
#    >>> kyung.root._4_2_mc.decoration_mc.currentLabel
#    'black_attack'
#    >>> kyung.root._2_4_mc.decoration_mc.currentLabel
#    'black_attack'
#    >>> kyung.root._4_4_mc.decoration_mc.currentLabel
#    'black_attack'
#
#    Knights build catapults far from bunker.
#    >>> time.sleep((period - (2 * margin)) * kyung._speed)
#    >>> kyung.root._2_1_mc.decoration_mc.currentLabel
#    'none'
#    >>> kyung.root._2_5_mc.decoration_mc.currentLabel
#    'none'
#    >>> kyung.root._1_2_mc.decoration_mc.currentLabel
#    'none'
#    >>> kyung.root._5_2_mc.decoration_mc.currentLabel
#    'none'
#    >>> kyung.root._1_4_mc.decoration_mc.currentLabel
#    'none'
#    >>> kyung.root._4_1_mc.decoration_mc.currentLabel
#    'none'
#    >>> kyung.root._4_5_mc.decoration_mc.currentLabel
#    'none'
#    >>> kyung.root._5_4_mc.decoration_mc.currentLabel
#    'none'
#    >>> time.sleep((2.0 * margin) * kyung._speed)
#    >>> kyung.root._2_1_mc.decoration_mc.currentLabel
#    'black_attack'
#    >>> kyung.root._2_5_mc.decoration_mc.currentLabel
#    'black_attack'
#    >>> kyung.root._1_2_mc.decoration_mc.currentLabel
#    'black_attack'
#    >>> kyung.root._5_2_mc.decoration_mc.currentLabel
#    'black_attack'
#    >>> kyung.root._1_4_mc.decoration_mc.currentLabel
#    'black_attack'
#    >>> kyung.root._4_1_mc.decoration_mc.currentLabel
#    'black_attack'
#    >>> kyung.root._4_5_mc.decoration_mc.currentLabel
#    'black_attack'
#    >>> kyung.root._5_4_mc.decoration_mc.currentLabel
#    'black_attack'
#    
#    Far away from the bunker, monks build shrines.
#    >>> time.sleep((period - (2 * margin)) * kyung._speed)
#    >>> kyung.root._1_1_mc.decoration_mc.currentLabel
#    'none'
#    >>> kyung.root._1_5_mc.decoration_mc.currentLabel
#    'none'
#    >>> kyung.root._5_1_mc.decoration_mc.currentLabel
#    'none'
#    >>> kyung.root._5_5_mc.decoration_mc.currentLabel
#    'none'
#    >>> time.sleep((2.0 * margin) * kyung._speed)
#    >>> kyung.root._1_1_mc.decoration_mc.currentLabel
#    'black_defend'
#    >>> kyung.root._1_5_mc.decoration_mc.currentLabel
#    'black_defend'
#    >>> kyung.root._5_1_mc.decoration_mc.currentLabel
#    'black_defend'
#    >>> kyung.root._5_5_mc.decoration_mc.currentLabel
#    'black_defend'
#
#    Fanfare.
#
#    Mason builds temple.
#    >>> time.sleep((period - (2 * margin)) * kyung._speed)
#    >>> kyung.root._3_3_mc.formation_mc.currentLabel
#    'none'
#    >>> kyung.root._3_3_mc.black_shape_mc.defend_mc.currentLabel
#    'none'
#    >>> time.sleep((2.0 * margin) * kyung._speed)
#    >>> kyung.root._3_3_mc.black_shape_mc.defend_mc.currentLabel
#    'show'
#    >>> kyung.root._3_3_mc.formation_mc.currentLabel
#    'black_attack_defend'
#
#    Freelance builds barracks.
#    >>> time.sleep((period - (2 * margin)) * kyung._speed)
#    >>> kyung.root._3_3_mc.black_shape_mc.attack_mc.currentLabel
#    'none'
#    >>> time.sleep((2.0 * margin) * kyung._speed)
#    >>> kyung.root._3_3_mc.black_shape_mc.attack_mc.currentLabel
#    '_0000'
#
#    Nearby, a snow dragon lays an egg.
#    >>> time.sleep(period * kyung._speed)
#    >>> time.sleep((period - (2 * margin)) * kyung._speed)
#    >>> kyung.root._4_4_mc.top_move_mc.currentLabel
#    'none'
#    >>> time.sleep((2 * margin) * kyung._speed)
#    >>> kyung.root._4_4_mc.top_move_mc.currentLabel
#    'white'
#
    Question mark disappears from cursor.
    Question mark appears and bounces.
    >>> time.sleep((period - (2 * margin)) * kyung._speed)
    >>> kyung.root.cursor_mc.act_mc.currentLabel
    'play'
    >>> kyung.root._3_3_mc.currentLabel
    'question_black'
    >>> time.sleep((2 * margin) * kyung._speed)
    >>> kyung.root.cursor_mc.act_mc.currentLabel
    'preview'
    >>> kyung.root._3_3_mc.currentLabel
    'question_black_repeat'


    decoration, top_move, delay
    preview animation takes about 1 second, so repeats 3+ times.  huh?
        >_< unh
    question mark toggles, which distracts me.
        >_< huh?
    delayed appearance looks like loading lag.
        >_< ho hum
    master publishes to slave which has its own lag.
        >_< uh oh
    is master sending messages to deliver causing client not to imitate?
    egg appears.  i do not notice.
        >_< hm?
    hammer of cursor occludes hammer of building.
        >_< huh?
    what does catapult have to do with fire of strike?  or with knight?
        >_< huh?
    '''
    
def kyung_first_animation_gather_snippet():
    '''
    Kyung sees an empty field.
    >>> kyung.root.cursor_mc.act_mc.gotoAndPlay('play')
    >>> kyung.root._3_3_mc.gotoAndPlay('empty_black') # pretend
    >>> kyung.root._3_3_mc.formation_mc.gotoAndPlay('none') # pretend
    >>> kyung.root._1_1_mc.decoration_mc.gotoAndPlay('none') # pretend
    >>> kyung.root._1_5_mc.decoration_mc.gotoAndPlay('none') # pretend
    >>> kyung.root._5_1_mc.decoration_mc.gotoAndPlay('none') # pretend
    >>> kyung.root._5_5_mc.decoration_mc.gotoAndPlay('none') # pretend
    >>> kyung.root._3_3_mc.black_shape_mc.defend_mc.gotoAndPlay('none') # pretend
    >>> kyung.root._2_1_mc.decoration_mc.gotoAndPlay('none') # pretend
    >>> kyung.root._2_5_mc.decoration_mc.gotoAndPlay('none') # pretend
    >>> kyung.root._1_2_mc.decoration_mc.gotoAndPlay('none') # pretend
    >>> kyung.root._5_2_mc.decoration_mc.gotoAndPlay('none') # pretend
    >>> kyung.root._1_4_mc.decoration_mc.gotoAndPlay('none') # pretend
    >>> kyung.root._4_1_mc.decoration_mc.gotoAndPlay('none') # pretend
    >>> kyung.root._4_5_mc.decoration_mc.gotoAndPlay('none') # pretend
    >>> kyung.root._5_4_mc.decoration_mc.gotoAndPlay('none') # pretend

    >>> kyung.root._3_1_mc.decoration_mc.gotoAndPlay('none') # pretend
    >>> kyung.root._3_5_mc.decoration_mc.gotoAndPlay('none') # pretend
    >>> kyung.root._1_3_mc.decoration_mc.gotoAndPlay('none') # pretend
    >>> kyung.root._5_3_mc.decoration_mc.gotoAndPlay('none') # pretend
    >>> kyung.root._2_2_mc.decoration_mc.gotoAndPlay('none') # pretend
    >>> kyung.root._4_2_mc.decoration_mc.gotoAndPlay('none') # pretend
    >>> kyung.root._2_4_mc.decoration_mc.gotoAndPlay('none') # pretend
    >>> kyung.root._4_4_mc.decoration_mc.gotoAndPlay('none') # pretend

    >>> kyung.root._3_2_mc.decoration_mc.gotoAndPlay('none') # pretend
    >>> kyung.root._3_4_mc.decoration_mc.gotoAndPlay('none') # pretend
    >>> kyung.root._2_3_mc.decoration_mc.gotoAndPlay('none') # pretend
    >>> kyung.root._4_3_mc.decoration_mc.gotoAndPlay('none') # pretend
    >>> kyung.root._3_3_mc.black_shape_mc.attack_mc.gotoAndPlay('none') # pretend
    >>> kyung.root._4_4_mc.top_move_mc.gotoAndPlay('none') # pretend

    Kyung builds base, top move.  Here is what Kyung sees.
    Each 0.25 seconds +/- 0.0625, Kyung sees an effect.
    >>> lag = 4.0
    >>> # period = 0.25 # too quick with/out delayed animations
    >>> # period = 0.5 # too quick with/out delayed animations
    >>> # period = 4.0 / 8.0 # after a few viewings, ok witout delayed animation
    >>> # period = 5.0 / 8.0 # a bit slow without animations
    >>> # period = 0.75 # too quick with delayed animations
    >>> period = 1.0 # legible transition, a bit slow
    >>> # period = 1.0 # unclear, boring with delayed animation
    >>> # period = 3.0 # clear, boring
    >>> 1.0 / 16
    0.0625
    >>> margin = 0.0625
    >>> time.sleep(lag * kyung._speed)

    Kyung clicks.
    >>> ## kyung.root._3_3_mc.dispatchEvent(mouseDown) # pretend
    >>> time.sleep(margin * kyung._speed)

    Builders set up scaffold.
    >>> kyung.root._3_3_mc.gotoAndPlay('preview_black') # pretend

    Build on client takes exactly lag seconds to complete +/- margin seconds.
    Kyung sees progress bar and building animation.
    >>> time.sleep((lag - (2 * margin)) * kyung._speed)
    >>> kyung.root._3_3_mc.currentLabel
    'preview_black'
    >>> kyung.root._3_3_mc.formation_mc.gotoAndPlay('none') # pretend

    >>> time.sleep((2.0 * margin) * kyung._speed)

    Builders tear down scaffolding.  Bunker appears.  Outline appears.  
    >>> kyung.root._3_3_mc.gotoAndPlay('question_black') # pretend

    Fanfare.
    >>> kyung.root._3_3_mc.formation_mc.gotoAndPlay('black_attack_defend') # pretend

    Far away from the bunker, monks build shrines.
    >>> time.sleep((period - (2 * margin)) * kyung._speed)
    >>> kyung.root._1_1_mc.decoration_mc.gotoAndPlay('none') # pretend
    >>> kyung.root._1_5_mc.decoration_mc.gotoAndPlay('none') # pretend
    >>> kyung.root._5_1_mc.decoration_mc.gotoAndPlay('none') # pretend
    >>> kyung.root._5_5_mc.decoration_mc.gotoAndPlay('none') # pretend
    >>> time.sleep((2.0 * margin) * kyung._speed)
    >>> kyung.root._1_1_mc.decoration_mc.gotoAndPlay('black_defend') # pretend
    >>> kyung.root._1_5_mc.decoration_mc.gotoAndPlay('black_defend') # pretend
    >>> kyung.root._5_1_mc.decoration_mc.gotoAndPlay('black_defend') # pretend
    >>> kyung.root._5_5_mc.decoration_mc.gotoAndPlay('black_defend') # pretend

    Knights build catapults far from bunker.
    >>> time.sleep((period - (2 * margin)) * kyung._speed)
    >>> kyung.root._2_1_mc.decoration_mc.gotoAndPlay('none') # pretend
    >>> kyung.root._2_5_mc.decoration_mc.gotoAndPlay('none') # pretend
    >>> kyung.root._1_2_mc.decoration_mc.gotoAndPlay('none') # pretend
    >>> kyung.root._5_2_mc.decoration_mc.gotoAndPlay('none') # pretend
    >>> kyung.root._1_4_mc.decoration_mc.gotoAndPlay('none') # pretend
    >>> kyung.root._4_1_mc.decoration_mc.gotoAndPlay('none') # pretend
    >>> kyung.root._4_5_mc.decoration_mc.gotoAndPlay('none') # pretend
    >>> kyung.root._5_4_mc.decoration_mc.gotoAndPlay('none') # pretend
    >>> time.sleep((2.0 * margin) * kyung._speed)
    >>> kyung.root._2_1_mc.decoration_mc.gotoAndPlay('black_attack') # pretend
    >>> kyung.root._2_5_mc.decoration_mc.gotoAndPlay('black_attack') # pretend
    >>> kyung.root._1_2_mc.decoration_mc.gotoAndPlay('black_attack') # pretend
    >>> kyung.root._5_2_mc.decoration_mc.gotoAndPlay('black_attack') # pretend
    >>> kyung.root._1_4_mc.decoration_mc.gotoAndPlay('black_attack') # pretend
    >>> kyung.root._4_1_mc.decoration_mc.gotoAndPlay('black_attack') # pretend
    >>> kyung.root._4_5_mc.decoration_mc.gotoAndPlay('black_attack') # pretend
    >>> kyung.root._5_4_mc.decoration_mc.gotoAndPlay('black_attack') # pretend
    
    Peasants build catapults near bunker.
    >>> time.sleep((period - (2 * margin)) * kyung._speed)
    >>> kyung.root._3_1_mc.decoration_mc.gotoAndPlay('none') # pretend
    >>> kyung.root._3_5_mc.decoration_mc.gotoAndPlay('none') # pretend
    >>> kyung.root._1_3_mc.decoration_mc.gotoAndPlay('none') # pretend
    >>> kyung.root._5_3_mc.decoration_mc.gotoAndPlay('none') # pretend
    >>> kyung.root._2_2_mc.decoration_mc.gotoAndPlay('none') # pretend
    >>> kyung.root._4_2_mc.decoration_mc.gotoAndPlay('none') # pretend
    >>> kyung.root._2_4_mc.decoration_mc.gotoAndPlay('none') # pretend
    >>> kyung.root._4_4_mc.decoration_mc.gotoAndPlay('none') # pretend
    >>> time.sleep((2.0 * margin) * kyung._speed)
    >>> kyung.root._3_1_mc.decoration_mc.gotoAndPlay('black_attack') # pretend
    >>> kyung.root._3_5_mc.decoration_mc.gotoAndPlay('black_attack') # pretend
    >>> kyung.root._1_3_mc.decoration_mc.gotoAndPlay('black_attack') # pretend
    >>> kyung.root._5_3_mc.decoration_mc.gotoAndPlay('black_attack') # pretend
    >>> kyung.root._2_2_mc.decoration_mc.gotoAndPlay('black_attack') # pretend
    >>> kyung.root._4_2_mc.decoration_mc.gotoAndPlay('black_attack') # pretend
    >>> kyung.root._2_4_mc.decoration_mc.gotoAndPlay('black_attack') # pretend
    >>> kyung.root._4_4_mc.decoration_mc.gotoAndPlay('black_attack') # pretend
    
    Peasants build catapults beside bunker.
    >>> time.sleep((period - (2 * margin)) * kyung._speed)
    >>> kyung.root._3_2_mc.decoration_mc.gotoAndPlay('none') # pretend
    >>> kyung.root._3_4_mc.decoration_mc.gotoAndPlay('none') # pretend
    >>> kyung.root._2_3_mc.decoration_mc.gotoAndPlay('none') # pretend
    >>> kyung.root._4_3_mc.decoration_mc.gotoAndPlay('none') # pretend
    >>> time.sleep((2.0 * margin) * kyung._speed)
    >>> kyung.root._3_2_mc.decoration_mc.gotoAndPlay('black_attack') # pretend
    >>> kyung.root._3_4_mc.decoration_mc.gotoAndPlay('black_attack') # pretend
    >>> kyung.root._2_3_mc.decoration_mc.gotoAndPlay('black_attack') # pretend
    >>> kyung.root._4_3_mc.decoration_mc.gotoAndPlay('black_attack') # pretend

    Mason builds temple.
    >>> time.sleep((period - (2 * margin)) * kyung._speed)
    >>> kyung.root._3_3_mc.black_shape_mc.defend_mc.gotoAndPlay('none') # pretend
    >>> time.sleep((2.0 * margin) * kyung._speed)
    >>> kyung.root._3_3_mc.black_shape_mc.defend_mc.gotoAndPlay('show') # pretend

    Freelance builds barracks.
    >>> time.sleep((period - (2 * margin)) * kyung._speed)
    >>> kyung.root._3_3_mc.black_shape_mc.attack_mc.gotoAndPlay('none') # pretend
    >>> time.sleep((2.0 * margin) * kyung._speed)
    >>> kyung.root._3_3_mc.black_shape_mc.attack_mc.gotoAndPlay('_0000') # pretend

    Nearby, a snow dragon lays an egg.
    >>> time.sleep(period * kyung._speed)
    >>> time.sleep((period - (2 * margin)) * kyung._speed)
    >>> kyung.root._4_4_mc.top_move_mc.gotoAndPlay('none') # pretend
    >>> time.sleep((2 * margin) * kyung._speed)
    >>> kyung.root._4_4_mc.top_move_mc.gotoAndPlay('white') # pretend

    Question mark disappears from cursor.
    Question mark appears and bounces.
    >>> time.sleep((period - (2 * margin)) * kyung._speed)
    >>> kyung.root.cursor_mc.act_mc.gotoAndPlay('play') # pretend
    >>> kyung.root._3_3_mc.currentLabel
    'question_black'
    >>> time.sleep((2 * margin) * kyung._speed)
    >>> kyung.root.cursor_mc.act_mc.gotoAndPlay('preview') # pretend
    >>> kyung.root._3_3_mc.gotoAndPlay('question_black_repeat') # pretend


    decoration, top_move, delay
    preview animation takes about 1 second, so repeats 3+ times.  huh?
        >_< unh
    question mark toggles, which distracts me.
        >_< huh?
    delayed appearance looks like loading lag.
        >_< ho hum
    master publishes to slave which has its own lag.
        >_< uh oh
    is master sending messages to deliver causing client not to imitate?
    egg appears.  i do not notice.
        >_< hm?
    hammer of cursor occludes hammer of building.
        >_< huh?
    '''

def moonhyoung_kyung_animation_example():
    '''Moonhyoung and Kyung play each other.  Kyung sees helpful animation.
    >>> moonhyoung, kyung, wait = setup_example(configuration, 
    ...     ('moonhyoung', 'park'), ('kyung', 'min') )
    >>> moonhyoung_level = int(moonhyoung.root.level_mc._txt.text)
    >>> kyung_level = int(kyung.root.level_mc._txt.text)
    >>> if not kyung_level <= moonhyoung_level:
    ...     kyung_level, moonhyoung_level
    >>> sloth = 1.0 / moonhyoung._speed

    by default, kyung disables preview
    >>> kyung.root.preview_gift_mc.enabled_mc.currentLabel
    'none'

    While simulating random lag, and testing animation, force users to wait.

    >>> time.sleep(max(wait, sloth * 5.036373))
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
    >>> moonhyoung.root._4_4_mc.dispatchEvent(mouseDown)
    >>> time.sleep(max(wait, sloth * 1.130992))

    TODO:  Moonhyoung sees help and cursor that it is not his turn.

    >>> #- kyung.root._3_3_mc.dispatchEvent(mouseDown)
    >>> #- time.sleep(max(wait, sloth * 0.611267))

    >>> #- kyung.root._4_4_mc.dispatchEvent(mouseDown)

    >>> #- time.sleep(max(wait, sloth * 4.423533))
    >>> #- kyung.root._4_3_mc.dispatchEvent(mouseDown)
    >>> #- time.sleep(max(wait, sloth * 0.523546))
    
    Still in preview.  Kyung waits and clicks again.
    >>> #- kyung.root._4_3_mc.dispatchEvent(mouseDown)
    >>> #- time.sleep(max(wait, sloth * 0.523546))
    >>> kyung.root._4_3_mc.dispatchEvent(mouseDown)

    >>> time.sleep(max(wait, sloth * 5.344957))
    >>> moonhyoung.root._4_4_mc.dispatchEvent(mouseDown)

    >>> time.sleep(max(wait, sloth * 8.276772))
    >>> moonhyoung.root._3_4_mc.dispatchEvent(mouseDown)
    >>> #- time.sleep(max(wait, sloth * 0.213273))
    >>> #- kyung.root._5_3_mc.dispatchEvent(mouseDown)
    >>> #- time.sleep(max(wait, sloth * 2.567926))
    >>> kyung.root._5_3_mc.dispatchEvent(mouseDown)
    >>> time.sleep(max(wait, sloth * 3.421529))
    >>> moonhyoung.root._3_4_mc.dispatchEvent(mouseDown)
    >>> #- time.sleep(max(wait, sloth * 4.012697))
    >>> #- kyung.root._6_5_mc.top_move_mc.currentLabel
    'white'
    >>> #- kyung.root._2_4_mc.dispatchEvent(mouseDown)
    >>> #- time.sleep(max(wait, sloth * 0.692491))

    Kyung sees one egg where it would be good for white to play.
    >>> #- kyung.root._3_5_mc.top_move_mc.currentLabel
    'white'
    >>> #- kyung.root._6_5_mc.top_move_mc.currentLabel
    'none'

    Kyung sees white cuts half of his knight's connection.
    >>> #- kyung.root._3_3_mc.decoration_mc.currentLabel
    'white_attack'

    Kyung sees cloud and curse of snow dragon claw on his castle.
    >>> #- kyung.root._2_4_mc.formation_mc.currentLabel
    'white_attack_curse'
    >>> kyung.root._2_4_mc.dispatchEvent(mouseDown)
    >>> time.sleep(max(wait, sloth * 3.000174))
    >>> kyung.root._3_5_mc.top_move_mc.currentLabel
    'white'
    >>> kyung.root._6_5_mc.top_move_mc.currentLabel
    'none'

    >>> moonhyoung.root._2_5_mc.dispatchEvent(mouseDown)
    >>> time.sleep(max(wait, sloth * 6.475936))

    Kyung sees snow dragon attack.  No curse of claw.
    >>> kyung.root._2_5_mc.formation_mc.currentLabel
    'white_attack'
    >>> #- kyung.root._3_5_mc.dispatchEvent(mouseDown)

    >>> #- time.sleep(max(wait, sloth * 3.292762))
    >>> kyung.root._3_5_mc.dispatchEvent(mouseDown)
    >>> time.sleep(max(wait, sloth * 1.550765))
    >>> moonhyoung.root._4_5_mc.dispatchEvent(mouseDown)
    >>> time.sleep(max(wait, sloth * 1.713036))
    >>> moonhyoung.root._4_5_mc.dispatchEvent(mouseDown)
    >>> time.sleep(max(wait, sloth * 3.460098))
    >>> #- kyung.root._4_6_mc.dispatchEvent(mouseDown)
    >>> #- time.sleep(max(wait, sloth * 2.820266))
    >>> kyung.root._5_6_mc.top_move_mc.currentLabel
    'none'
    >>> kyung.root._4_6_mc.dispatchEvent(mouseDown)
    >>> time.sleep(max(wait, sloth * 2.149841))
    >>> kyung.root._5_6_mc.top_move_mc.currentLabel
    'none'
    >>> moonhyoung.root._3_6_mc.dispatchEvent(mouseDown)
    >>> time.sleep(max(wait, sloth * 5.336804))
    >>> kyung.root._5_6_mc.top_move_mc.currentLabel
    'black'
    
    Kyung's castle is destroyed.
    The claw disappears.
    >>> kyung.root._3_5_mc.formation_mc.currentLabel
    'none'
    >>> #- kyung.root._1_5_mc.dispatchEvent(mouseDown)
    >>> #- time.sleep(max(wait, sloth * 3.003314))
    >>> kyung.root._1_5_mc.dispatchEvent(mouseDown)
    >>> time.sleep(max(wait, sloth * 2.901294))
    >>> moonhyoung.root._1_4_mc.dispatchEvent(mouseDown)
    >>> time.sleep(max(wait, sloth * 4.995037))
    >>> #- kyung.root._2_3_mc.dispatchEvent(mouseDown)
    >>> #- time.sleep(max(wait, sloth * 2.795839))
    >>> kyung.root._5_6_mc.top_move_mc.currentLabel
    'black'
    >>> import pdb; pdb.set_trace(); kyung.root._2_3_mc.dispatchEvent(mouseDown)
    >>> time.sleep(max(wait, sloth * 3.655757))

    Critical top move hint disappears.
    >>> kyung.root._5_6_mc.top_move_mc.currentLabel
    'none'
    >>> for r in kyung.ambassador.receives[-8:]:
    ...     s = r.get('sequence', [])
    ...     for i in s:
    ...         i.get('_5_6_mc')
    ...     
    kyung.root._5_6_mc.top_move_mc.currentLabel none ?
    >>> moonhyoung.root._0_5_mc.dispatchEvent(mouseDown)
    >>> time.sleep(max(wait, sloth * 7.606022))
    >>> kyung.root._5_6_mc.top_move_mc.currentLabel
    'none'
    >>> for r in kyung.ambassador.receives[-8:]:
    ...     s = r.get('sequence', [])
    ...     for i in s:
    ...         i.get('_5_6_mc')
    ...     
    kyung.root._5_6_mc.top_move_mc.currentLabel none ?
    >>> #- kyung.root._1_6_mc.dispatchEvent(mouseDown)
    >>> #- time.sleep(max(wait, sloth * 1.895542))
    >>> kyung.root._1_6_mc.dispatchEvent(mouseDown)
    >>> time.sleep(max(wait, sloth * 2.691059))
    >>> kyung.root._5_6_mc.top_move_mc.currentLabel
    'none'
    >>> kyung.root._1_6_mc.dispatchEvent(mouseDown)
    >>> time.sleep(max(wait, sloth * 5.383449))
    >>> moonhyoung.root._0_6_mc.dispatchEvent(mouseDown)
    >>> time.sleep(max(wait, sloth * 1.593581))
    >>> kyung.root._5_6_mc.top_move_mc.currentLabel
    'none'
    >>> moonhyoung.root._0_6_mc.dispatchEvent(mouseDown)
    >>> time.sleep(max(wait, sloth * 8.058797))
    >>> #- kyung.root._0_4_mc.dispatchEvent(mouseDown)
    >>> #- time.sleep(max(wait, sloth * 2.043630))
    >>> kyung.root._0_4_mc.dispatchEvent(mouseDown)
    >>> time.sleep(max(wait, sloth * 1.969553))
    >>> moonhyoung.root._0_3_mc.dispatchEvent(mouseDown)
    >>> time.sleep(max(wait, sloth * 7.454186))
    >>> #- kyung.root._1_3_mc.dispatchEvent(mouseDown)
    >>> #- time.sleep(max(wait, sloth * 1.227600))
    >>> kyung.root._1_3_mc.dispatchEvent(mouseDown)
    >>> time.sleep(max(wait, sloth * 2.526290))
    >>> moonhyoung.root._1_2_mc.dispatchEvent(mouseDown)
    >>> time.sleep(max(wait, sloth * 6.330117))
    >>> #- kyung.root._5_5_mc.dispatchEvent(mouseDown)
    >>> #- time.sleep(max(wait, sloth * 3.836061))
    >>> kyung.root._5_5_mc.dispatchEvent(mouseDown)
    >>> time.sleep(max(wait, sloth * 7.776139))
    >>> kyung.root._5_6_mc.top_move_mc.currentLabel
    'none'
    >>> moonhyoung.root._1_7_mc.dispatchEvent(mouseDown)
    >>> time.sleep(max(wait, sloth * 19.320278))
    >>> kyung.root._5_6_mc.top_move_mc.currentLabel
    'none'
    >>> #- kyung.root._5_4_mc.dispatchEvent(mouseDown)
    >>> #- time.sleep(max(wait, sloth * 3.490391))
    >>> #- kyung.root._3_5_mc.dispatchEvent(mouseDown)
    >>> #- time.sleep(max(wait, sloth * 4.423231))
    >>> #- kyung.root._3_5_mc.dispatchEvent(mouseDown)
    >>> #- time.sleep(max(wait, sloth * 2.924254))
    >>> #- kyung.root._2_6_mc.dispatchEvent(mouseDown)
    >>> #- time.sleep(max(wait, sloth * 2.106020))
    >>> #- kyung.root._2_7_mc.dispatchEvent(mouseDown)
    >>> #- time.sleep(max(wait, sloth * 1.818148))
    >>> #- kyung.root._2_8_mc.dispatchEvent(mouseDown)
    >>> #- time.sleep(max(wait, sloth * 0.976151))
    >>> kyung.root._2_8_mc.dispatchEvent(mouseDown)
    >>> time.sleep(max(wait, sloth * 0.764469))
    >>> kyung.root._2_7_mc.dispatchEvent(mouseDown)
    >>> time.sleep(max(wait, sloth * 1.677573))
    >>> moonhyoung.root._2_6_mc.dispatchEvent(mouseDown)
    >>> time.sleep(max(wait, sloth * 7.100001))
    >>> #- kyung.root._5_4_mc.dispatchEvent(mouseDown)
    >>> #- time.sleep(max(wait, sloth * 2.095440))
    >>> #- kyung.root._5_6_mc.dispatchEvent(mouseDown)
    >>> #- time.sleep(max(wait, sloth * 3.417958))
    >>> #- kyung.root._5_4_mc.dispatchEvent(mouseDown)
    >>> #- time.sleep(max(wait, sloth * 1.619395))
    >>> kyung.root._5_4_mc.dispatchEvent(mouseDown)
    >>> time.sleep(max(wait, sloth * 2.414027))
    >>> #- kyung.root._3_5_mc.dispatchEvent(mouseDown)
    >>> #- time.sleep(max(wait, sloth * 0.543335))
    >>> kyung.root._3_5_mc.dispatchEvent(mouseDown)
    >>> time.sleep(max(wait, sloth * 2.876771))
    >>> moonhyoung.root._5_6_mc.dispatchEvent(mouseDown)
    >>> time.sleep(max(wait, sloth * 7.559221))
    >>> #- kyung.root._6_6_mc.dispatchEvent(mouseDown)
    >>> #- time.sleep(max(wait, sloth * 6.298238))
    >>> #- kyung.root._6_5_mc.dispatchEvent(mouseDown)
    >>> #- time.sleep(max(wait, sloth * 1.426986))
    >>> #- kyung.root._5_7_mc.dispatchEvent(mouseDown)
    >>> #- time.sleep(max(wait, sloth * 1.276478))
    >>> #- kyung.root._4_7_mc.dispatchEvent(mouseDown)
    >>> #- time.sleep(max(wait, sloth * 4.388957))
    >>> kyung.root._4_7_mc.dispatchEvent(mouseDown)
    >>> time.sleep(max(wait, sloth * 8.566781))
    >>> moonhyoung.root._5_7_mc.dispatchEvent(mouseDown)
    >>> time.sleep(max(wait, sloth * 6.321782))
    >>> #- kyung.root._5_8_mc.dispatchEvent(mouseDown)
    >>> #- time.sleep(max(wait, sloth * 3.142668))
    >>> kyung.root._5_8_mc.dispatchEvent(mouseDown)
    >>> time.sleep(max(wait, sloth * 6.731769))
    >>> moonhyoung.root._3_7_mc.dispatchEvent(mouseDown)
    >>> time.sleep(max(wait, sloth * 15.789178))
    >>> #- kyung.root._4_8_mc.dispatchEvent(mouseDown)
    >>> #- time.sleep(max(wait, sloth * 3.322508))
    >>> kyung.root._4_8_mc.dispatchEvent(mouseDown)
    >>> time.sleep(max(wait, sloth * 1.960702))
    >>> moonhyoung.root._3_8_mc.dispatchEvent(mouseDown)
    >>> time.sleep(max(wait, sloth * 8.859553))
    >>> #- kyung.root._6_8_mc.dispatchEvent(mouseDown)
    >>> #- time.sleep(max(wait, sloth * 4.898926))
    >>> kyung.root._6_8_mc.dispatchEvent(mouseDown)
    >>> time.sleep(max(wait, sloth * 2.232298))
    >>> moonhyoung.root._6_7_mc.dispatchEvent(mouseDown)
    >>> time.sleep(max(wait, sloth * 8.733002))
    >>> #- kyung.root._7_7_mc.dispatchEvent(mouseDown)
    >>> #- time.sleep(max(wait, sloth * 5.190020))
    >>> #- kyung.root._6_6_mc.dispatchEvent(mouseDown)
    >>> #- time.sleep(max(wait, sloth * 1.597347))
    >>> #- kyung.root._2_2_mc.dispatchEvent(mouseDown)
    >>> #- time.sleep(max(wait, sloth * 5.532451))
    >>> #- kyung.root._2_1_mc.dispatchEvent(mouseDown)
    >>> #- time.sleep(max(wait, sloth * 1.553206))
    >>> #- kyung.root._1_1_mc.dispatchEvent(mouseDown)
    >>> #- time.sleep(max(wait, sloth * 3.164118))
    >>> #- kyung.root._0_2_mc.dispatchEvent(mouseDown)
    >>> #- time.sleep(max(wait, sloth * 2.074857))
    >>> #- kyung.root._2_2_mc.dispatchEvent(mouseDown)
    >>> #- time.sleep(max(wait, sloth * 3.040964))
    >>> #- kyung.root._2_1_mc.dispatchEvent(mouseDown)
    >>> #- time.sleep(max(wait, sloth * 3.141526))
    >>> #- kyung.root._6_3_mc.dispatchEvent(mouseDown)
    >>> #- time.sleep(max(wait, sloth * 4.665413))
    >>> kyung.root._6_3_mc.dispatchEvent(mouseDown)
    >>> time.sleep(max(wait, sloth * 2.666690))
    >>> moonhyoung.root._7_8_mc.dispatchEvent(mouseDown)
    >>> time.sleep(max(wait, sloth * 6.054614))
    >>> #- kyung.root._7_3_mc.dispatchEvent(mouseDown)
    >>> #- time.sleep(max(wait, sloth * 3.631566))
    >>> #- kyung.root._7_3_mc.dispatchEvent(mouseDown)
    >>> #- time.sleep(max(wait, sloth * 7.372072))
    >>> kyung.root._7_3_mc.dispatchEvent(mouseDown)
    >>> time.sleep(max(wait, sloth * 3.300416))
    >>> #- kyung.root._5_1_mc.dispatchEvent(mouseDown)
    >>> #- time.sleep(max(wait, sloth * 2.965185))
    >>> kyung.root._5_1_mc.dispatchEvent(mouseDown)
    >>> time.sleep(max(wait, sloth * 0.866471))
    >>> moonhyoung.root._2_2_mc.dispatchEvent(mouseDown)
    >>> time.sleep(max(wait, sloth * 4.978062))
    >>> #- kyung.root._6_6_mc.dispatchEvent(mouseDown)
    >>> #- time.sleep(max(wait, sloth * 2.191931))
    >>> kyung.root._6_6_mc.dispatchEvent(mouseDown)
    >>> time.sleep(max(wait, sloth * 4.879634))
    >>> moonhyoung.root._6_5_mc.dispatchEvent(mouseDown)
    >>> time.sleep(max(wait, sloth * 9.095511))
    >>> #- kyung.root._7_6_mc.dispatchEvent(mouseDown)
    >>> #- time.sleep(max(wait, sloth * 10.976270))
    >>> kyung.root._7_6_mc.dispatchEvent(mouseDown)
    >>> time.sleep(max(wait, sloth * 2.352468))
    >>> moonhyoung.root._7_5_mc.dispatchEvent(mouseDown)
    >>> time.sleep(max(wait, sloth * 3.129568))
    >>> #- kyung.root._8_5_mc.dispatchEvent(mouseDown)
    >>> #- time.sleep(max(wait, sloth * 1.818551))
    >>> moonhyoung.root._7_5_mc.dispatchEvent(mouseDown)
    >>> time.sleep(max(wait, sloth * 1.158135))
    >>> kyung.root._8_5_mc.dispatchEvent(mouseDown)
    >>> time.sleep(max(wait, sloth * 3.406220))
    >>> moonhyoung.root._8_6_mc.dispatchEvent(mouseDown)
    >>> time.sleep(max(wait, sloth * 6.607235))
    >>> #- kyung.root._8_7_mc.dispatchEvent(mouseDown)
    >>> #- time.sleep(max(wait, sloth * 4.384253))
    >>> kyung.root._8_7_mc.dispatchEvent(mouseDown)
    >>> time.sleep(max(wait, sloth * 9.042295))
    >>> moonhyoung.root._8_4_mc.dispatchEvent(mouseDown)
    >>> time.sleep(max(wait, sloth * 4.014863))
    >>> #- kyung.root._8_3_mc.dispatchEvent(mouseDown)
    >>> #- time.sleep(max(wait, sloth * 8.242319))
    >>> kyung.root._8_3_mc.dispatchEvent(mouseDown)
    >>> time.sleep(max(wait, sloth * 1.945073))
    >>> kyung.root._7_4_mc.dispatchEvent(mouseDown)
    >>> time.sleep(max(wait, sloth * 5.067233))
    >>> moonhyoung.root._7_4_mc.dispatchEvent(mouseDown)
    >>> time.sleep(max(wait, sloth * 2.304812))
    >>> #- kyung.root._6_4_mc.dispatchEvent(mouseDown)
    >>> #- time.sleep(max(wait, sloth * 1.811712))
    >>> kyung.root._6_4_mc.dispatchEvent(mouseDown)
    >>> time.sleep(max(wait, sloth * 7.267536))
    >>> moonhyoung.root._3_1_mc.dispatchEvent(mouseDown)
    >>> time.sleep(max(wait, sloth * 7.620602))
    >>> #- kyung.root._6_8_mc.dispatchEvent(mouseDown)
    >>> #- time.sleep(max(wait, sloth * 1.191881))
    >>> #- kyung.root._7_7_mc.dispatchEvent(mouseDown)
    >>> #- time.sleep(max(wait, sloth * 2.614871))
    >>> #- kyung.root._5_1_mc.dispatchEvent(mouseDown)
    >>> #- time.sleep(max(wait, sloth * 7.463252))
    >>> kyung.root._5_1_mc.dispatchEvent(mouseDown)
    >>> time.sleep(max(wait, sloth * 5.639728))
    >>> moonhyoung.root._4_0_mc.dispatchEvent(mouseDown)
    >>> time.sleep(max(wait, sloth * 4.833453))
    >>> #- kyung.root._5_0_mc.dispatchEvent(mouseDown)
    >>> #- time.sleep(max(wait, sloth * 2.895378))
    >>> kyung.root._5_0_mc.dispatchEvent(mouseDown)
    >>> time.sleep(max(wait, sloth * 7.222165))
    >>> moonhyoung.root._2_0_mc.dispatchEvent(mouseDown)
    >>> time.sleep(max(wait, sloth * 3.376454))
    >>> #- kyung.root._5_2_mc.dispatchEvent(mouseDown)
    >>> #- time.sleep(max(wait, sloth * 2.739704))
    >>> #- kyung.root._4_1_mc.dispatchEvent(mouseDown)
    >>> #- time.sleep(max(wait, sloth * 4.824631))
    >>> kyung.root._4_1_mc.dispatchEvent(mouseDown)
    >>> time.sleep(max(wait, sloth * 8.675137))
    >>> moonhyoung.root._3_2_mc.dispatchEvent(mouseDown)
    >>> time.sleep(max(wait, sloth * 1.536958))
    >>> #- kyung.root._4_2_mc.dispatchEvent(mouseDown)
    >>> #- time.sleep(max(wait, sloth * 1.500512))
    >>> #- kyung.root._3_2_mc.dispatchEvent(mouseDown)
    >>> #- time.sleep(max(wait, sloth * 1.364050))
    >>> #- kyung.root._4_2_mc.dispatchEvent(mouseDown)
    >>> #- time.sleep(max(wait, sloth * 1.262649))
    >>> #- kyung.root._2_1_mc.dispatchEvent(mouseDown)
    >>> #- time.sleep(max(wait, sloth * 1.603103))
    >>> #- kyung.root._4_2_mc.dispatchEvent(mouseDown)
    >>> #- time.sleep(max(wait, sloth * 3.309604))
    >>> #- kyung.root._3_0_mc.dispatchEvent(mouseDown)
    >>> #- time.sleep(max(wait, sloth * 2.375255))
    >>> kyung.root._3_0_mc.dispatchEvent(mouseDown)
    >>> time.sleep(max(wait, sloth * 6.103130))
    >>> moonhyoung.root._4_0_mc.dispatchEvent(mouseDown)
    >>> time.sleep(max(wait, sloth * 6.301411))
    >>> moonhyoung.root._1_1_mc.dispatchEvent(mouseDown)
    >>> time.sleep(max(wait, sloth * 5.176181))
    >>> #- kyung.root._4_2_mc.dispatchEvent(mouseDown)
    >>> #- time.sleep(max(wait, sloth * 3.796914))
    >>> kyung.root._4_2_mc.dispatchEvent(mouseDown)
    >>> time.sleep(max(wait, sloth * 12.865299))

    HACK:  Do not pass, as this would change levels.
    >>> ## kyung.root.pass_mc.dispatchEvent(mouseDown)
    >>> ## time.sleep(max(wait, sloth * 2.138277))
    >>> ## moonhyoung.root.pass_mc.dispatchEvent(mouseDown)
    >>> ## time.sleep(max(wait, sloth * 9.256537))
    >>> ## moonhyoung.root._8_7_mc.dispatchEvent(mouseDown)
    >>> ## time.sleep(max(wait, sloth * 0.688120))
    >>> ## moonhyoung.root._8_6_mc.dispatchEvent(mouseDown)
    >>> ## time.sleep(max(wait, sloth * 5.208640))
    >>> ## moonhyoung.root._5_3_mc.dispatchEvent(mouseDown)
    >>> ## time.sleep(max(wait, sloth * 2.352339))
    >>> ## moonhyoung.root._4_2_mc.dispatchEvent(mouseDown)
    >>> ## time.sleep(max(wait, sloth * 1.418292))
    >>> ## moonhyoung.root._4_0_mc.dispatchEvent(mouseDown)

    
    kyung leaves three stones unconnected around 2,2
        >_< i am confused and annoyed
    '''


def moonhyoung_kyung_animation_preview_example():
    '''Moonhyoung and Kyung play each other.  Kyung sees helpful animation.
    >>> moonhyoung, kyung, wait = setup_example(configuration, 
    ...     ('moonhyoung', 'park'), ('kyung', 'min') )
    >>> moonhyoung_level = int(moonhyoung.root.level_mc._txt.text)
    >>> kyung_level = int(kyung.root.level_mc._txt.text)
    >>> if not kyung_level <= moonhyoung_level:
    ...     kyung_level, moonhyoung_level
    >>> sloth = 1.0 / moonhyoung._speed

    TODO:  kyung enables preview
    >>> kyung.root.preview_gift_mc.enabled_mc.currentLabel
    'none'
    >>> kyung.root.preview_gift_mc.dispatchEvent(mouseDown)
    >>> time.sleep(wait)
    >>> kyung.root.preview_gift_mc.enabled_mc.currentLabel
    'show'

    While simulating random lag, and testing animation, force users to wait.

    >>> time.sleep(max(wait, sloth * 5.036373))
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
    >>> moonhyoung.root._4_4_mc.dispatchEvent(mouseDown)
    >>> time.sleep(max(wait, sloth * 1.130992))

    TODO:  Moonhyoung sees help and cursor that it is not his turn.

    >>> code_unit.inline_examples(
    ...     kyung_first_animation_snippet.__doc__, 
    ...     locals(), globals(), 
    ...     verify_examples = False)

    #Kyung builds base, top move.  Here is what Kyung sees.
    #Each 0.25 seconds +/- 0.0625, Kyung sees an effect.
    #>>> kyung.root._3_3_mc.gotoAndPlay('empty_black') # pretend

    #>>> kyung.root._3_3_mc.dispatchEvent(mouseDown)
    #>>> time.sleep(0.0625 * kyung._speed)
    #>>> kyung.root._3_3_mc.gotoAndPlay('preview_black') # pretend

    #Build on client takes exactly 4 seconds to complete +/- 0.0625 seconds.
    #Kyung sees progress bar and building animation.
    #>>> 1.0 / 8 / 2
    #0.0625
    #>>> time.sleep((4.0 - (2 * 0.0625)) * kyung._speed)
    #>>> kyung.root._3_3_mc.gotoAndPlay('preview_black') # pretend

    #>>> time.sleep((2.0 * 0.0625) * kyung._speed)

    #Building finishes.  Base is ready for review.
    #>>> kyung.root._3_3_mc.gotoAndPlay('question_black') # pretend

    #Peasants build shrines.
    #>>> time.sleep((0.25 - (2 * 0.0625)) * kyung._speed)
    #>>> kyung.root._1_1_mc.decoration_mc.gotoAndPlay('none') # pretend
    #>>> kyung.root._5_5_mc.decoration_mc.gotoAndPlay('none') # pretend
    #>>> time.sleep((2.0 * 0.0625) * kyung._speed)
    #>>> kyung.root._1_1_mc.decoration_mc.gotoAndPlay('black_defend') # pretend
    #>>> kyung.root._5_5_mc.decoration_mc.gotoAndPlay('black_defend') # pretend

    #Mason builds temple.
    #>>> time.sleep((0.25 - (2 * 0.0625)) * kyung._speed)
    #>>> kyung.root._3_3_mc.black_shape_mc.defend_mc.gotoAndPlay('none') # pretend
    #>>> time.sleep((2.0 * 0.0625) * kyung._speed)
    #>>> kyung.root._3_3_mc.black_shape_mc.defend_mc.gotoAndPlay('show') # pretend

    #Freelance builds barracks.
    #>>> time.sleep((0.25 - (2 * 0.0625)) * kyung._speed)
    #>>> kyung.root._3_3_mc.black_shape_mc.attack_mc.gotoAndPlay('none') # pretend
    #>>> time.sleep((2.0 * 0.0625) * kyung._speed)
    #>>> kyung.root._3_3_mc.black_shape_mc.attack_mc.gotoAndPlay('show') # pretend

    #Peasants build catapults.
    #>>> time.sleep((0.25 - (2 * 0.0625)) * kyung._speed)
    #>>> kyung.root._3_2_mc.decoration_mc.gotoAndPlay('none') # pretend
    #>>> kyung.root._3_4_mc.decoration_mc.gotoAndPlay('none') # pretend
    #>>> time.sleep((2.0 * 0.0625) * kyung._speed)
    #>>> kyung.root._3_2_mc.decoration_mc.gotoAndPlay('black_defend') # pretend
    #>>> kyung.root._3_4_mc.decoration_mc.gotoAndPlay('black_defend') # pretend

    #On the other side of the field, dragon lays an egg.
    #>>> time.sleep((0.25 - (2 * 0.0625)) * kyung._speed)
    #>>> kyung.root._4_4_mc.top_move_mc.gotoAndPlay('none') # pretend
    #>>> time.sleep((2 * 0.0625) * kyung._speed)
    #>>> kyung.root._4_4_mc.top_move_mc.gotoAndPlay('white') # pretend

   # 
    >>> time.sleep(max(wait, sloth * 0.611267))

    >>> kyung.root._4_4_mc.dispatchEvent(mouseDown)

    >>> time.sleep(max(wait, sloth * 4.423533))
    >>> kyung.root._4_3_mc.dispatchEvent(mouseDown)
    >>> time.sleep(max(wait, sloth * 0.523546))
    
    Still in preview.  Kyung waits and clicks again.
    >>> kyung.root._4_3_mc.dispatchEvent(mouseDown)
    >>> time.sleep(max(wait, sloth * 0.523546))
    >>> kyung.root._4_3_mc.dispatchEvent(mouseDown)

    >>> time.sleep(max(wait, sloth * 5.344957))
    >>> moonhyoung.root._4_4_mc.dispatchEvent(mouseDown)

    >>> time.sleep(max(wait, sloth * 8.276772))
    >>> moonhyoung.root._3_4_mc.dispatchEvent(mouseDown)
    >>> time.sleep(max(wait, sloth * 0.213273))
    >>> kyung.root._5_3_mc.dispatchEvent(mouseDown)

    #Kyung sees progress bar and building animation.
    #>>> 1.0 / 8 / 4
    #0.03125
    #>>> time.sleep((1 - 0.03125) * 4.0 * kyung._speed)
    #>>> kyung.root._5_3_mc.currentLabel
    #'preview_black'
    #>>> time.sleep((2 * 0.03125) * kyung._speed)

    #Kyung sees only base and hammer.
    #>>> kyung.root._5_3_mc.currentLabel
    #'question_black'
    #>>> kyung.root._5_3_mc.black_shape_mc.defend_mc.currentLabel
    #'none'
    #>>> kyung.root._5_3_mc.black_shape_mc.attack_mc.currentLabel
    #'none'

    #On the other side of the field, Kyung sees a dragon egg.
    #>>> time.sleep((0.25 - 0.03125) * kyung._speed)
    #>>> kyung.root._6_5_mc.top_move_mc.currentLabel
    #'none'
    #>>> time.sleep((2 * 0.03125) * kyung._speed)
    #>>> kyung.root._6_5_mc.top_move_mc.currentLabel
    #'white'

    #TODO:  Kyung sees white ice.
    #TODO:  Kyung sees green farms.
    #>>> kyung.root._6_0_mc.territory_mc.currentLabel
    #'black'
   # 
    #Kyung sees score and profit.
    #>>> kyung.root.score_mc.bar_mc.territory_txt.text
    #?
    #>>> kyung.root.score_mc.bar_mc.marker_mc.change_txt.text
    #?

    >>> time.sleep(max(wait, sloth * 2.567926))
    >>> kyung.root._5_3_mc.dispatchEvent(mouseDown)
    >>> time.sleep(max(wait, sloth * 3.421529))
    >>> moonhyoung.root._3_4_mc.dispatchEvent(mouseDown)
    >>> time.sleep(max(wait, sloth * 4.012697))
    >>> kyung.root._6_5_mc.top_move_mc.currentLabel
    'white'
    >>> kyung.root._2_4_mc.dispatchEvent(mouseDown)
    >>> time.sleep(max(wait, sloth * 0.692491))

    Kyung sees one egg where it would be good for white to play.
    >>> kyung.root._3_5_mc.top_move_mc.currentLabel
    'white'
    >>> kyung.root._6_5_mc.top_move_mc.currentLabel
    'none'

    Kyung sees white cuts half of his knight's connection.
    >>> kyung.root._3_3_mc.decoration_mc.currentLabel
    'white_attack'

    Kyung sees cloud and curse of snow dragon claw on his castle.
    >>> kyung.root._2_4_mc.formation_mc.currentLabel
    'white_attack_curse'
    >>> kyung.root._2_4_mc.dispatchEvent(mouseDown)
    >>> time.sleep(max(wait, sloth * 3.000174))
    >>> kyung.root._3_5_mc.top_move_mc.currentLabel
    'white'
    >>> kyung.root._6_5_mc.top_move_mc.currentLabel
    'none'

    >>> moonhyoung.root._2_5_mc.dispatchEvent(mouseDown)
    >>> time.sleep(max(wait, sloth * 6.475936))

    Kyung sees snow dragon attack.  No curse of claw.
    >>> kyung.root._2_5_mc.formation_mc.currentLabel
    'white_attack'
    >>> kyung.root._3_5_mc.dispatchEvent(mouseDown)

    >>> time.sleep(max(wait, sloth * 3.292762))
    >>> kyung.root._3_5_mc.dispatchEvent(mouseDown)
    >>> time.sleep(max(wait, sloth * 1.550765))
    >>> moonhyoung.root._4_5_mc.dispatchEvent(mouseDown)
    >>> time.sleep(max(wait, sloth * 1.713036))
    >>> moonhyoung.root._4_5_mc.dispatchEvent(mouseDown)
    >>> time.sleep(max(wait, sloth * 3.460098))
    >>> kyung.root._4_6_mc.dispatchEvent(mouseDown)
    >>> time.sleep(max(wait, sloth * 2.820266))
    >>> kyung.root._4_6_mc.dispatchEvent(mouseDown)
    >>> time.sleep(max(wait, sloth * 2.149841))
    >>> moonhyoung.root._3_6_mc.dispatchEvent(mouseDown)
    >>> time.sleep(max(wait, sloth * 5.336804))
    
    Kyung's castle is destroyed.
    The claw disappears.
    >>> kyung.root._3_5_mc.formation_mc.currentLabel
    'none'
    >>> kyung.root._1_5_mc.dispatchEvent(mouseDown)
    >>> time.sleep(max(wait, sloth * 3.003314))
    >>> kyung.root._1_5_mc.dispatchEvent(mouseDown)
    >>> time.sleep(max(wait, sloth * 2.901294))
    >>> moonhyoung.root._1_4_mc.dispatchEvent(mouseDown)
    >>> time.sleep(max(wait, sloth * 4.995037))
    >>> kyung.root._2_3_mc.dispatchEvent(mouseDown)
    >>> time.sleep(max(wait, sloth * 2.795839))
    >>> kyung.root._2_3_mc.dispatchEvent(mouseDown)
    >>> time.sleep(max(wait, sloth * 3.655757))
    >>> moonhyoung.root._0_5_mc.dispatchEvent(mouseDown)
    >>> time.sleep(max(wait, sloth * 7.606022))
    >>> kyung.root._1_6_mc.dispatchEvent(mouseDown)
    >>> time.sleep(max(wait, sloth * 1.895542))
    >>> kyung.root._1_6_mc.dispatchEvent(mouseDown)
    >>> time.sleep(max(wait, sloth * 2.691059))
    >>> kyung.root._1_6_mc.dispatchEvent(mouseDown)
    >>> time.sleep(max(wait, sloth * 5.383449))
    >>> moonhyoung.root._0_6_mc.dispatchEvent(mouseDown)
    >>> time.sleep(max(wait, sloth * 1.593581))
    >>> moonhyoung.root._0_6_mc.dispatchEvent(mouseDown)
    >>> time.sleep(max(wait, sloth * 8.058797))
    >>> kyung.root._0_4_mc.dispatchEvent(mouseDown)
    >>> time.sleep(max(wait, sloth * 2.043630))
    >>> kyung.root._0_4_mc.dispatchEvent(mouseDown)
    >>> time.sleep(max(wait, sloth * 1.969553))
    >>> moonhyoung.root._0_3_mc.dispatchEvent(mouseDown)
    >>> time.sleep(max(wait, sloth * 7.454186))
    >>> kyung.root._1_3_mc.dispatchEvent(mouseDown)
    >>> time.sleep(max(wait, sloth * 1.227600))
    >>> kyung.root._1_3_mc.dispatchEvent(mouseDown)
    >>> time.sleep(max(wait, sloth * 2.526290))
    >>> moonhyoung.root._1_2_mc.dispatchEvent(mouseDown)
    >>> time.sleep(max(wait, sloth * 6.330117))
    >>> kyung.root._5_5_mc.dispatchEvent(mouseDown)
    >>> time.sleep(max(wait, sloth * 3.836061))
    >>> kyung.root._5_5_mc.dispatchEvent(mouseDown)
    >>> time.sleep(max(wait, sloth * 7.776139))
    >>> moonhyoung.root._1_7_mc.dispatchEvent(mouseDown)
    >>> time.sleep(max(wait, sloth * 19.320278))
    >>> kyung.root._5_4_mc.dispatchEvent(mouseDown)
    >>> time.sleep(max(wait, sloth * 3.490391))
    >>> kyung.root._3_5_mc.dispatchEvent(mouseDown)
    >>> time.sleep(max(wait, sloth * 4.423231))
    >>> kyung.root._3_5_mc.dispatchEvent(mouseDown)
    >>> time.sleep(max(wait, sloth * 2.924254))
    >>> kyung.root._2_6_mc.dispatchEvent(mouseDown)
    >>> time.sleep(max(wait, sloth * 2.106020))
    >>> kyung.root._2_7_mc.dispatchEvent(mouseDown)
    >>> time.sleep(max(wait, sloth * 1.818148))
    >>> kyung.root._2_8_mc.dispatchEvent(mouseDown)
    >>> time.sleep(max(wait, sloth * 0.976151))
    >>> kyung.root._2_8_mc.dispatchEvent(mouseDown)
    >>> time.sleep(max(wait, sloth * 0.764469))
    >>> kyung.root._2_7_mc.dispatchEvent(mouseDown)
    >>> time.sleep(max(wait, sloth * 1.677573))
    >>> moonhyoung.root._2_6_mc.dispatchEvent(mouseDown)
    >>> time.sleep(max(wait, sloth * 7.100001))
    >>> kyung.root._5_4_mc.dispatchEvent(mouseDown)
    >>> time.sleep(max(wait, sloth * 2.095440))
    >>> kyung.root._5_6_mc.dispatchEvent(mouseDown)
    >>> time.sleep(max(wait, sloth * 3.417958))
    >>> kyung.root._5_4_mc.dispatchEvent(mouseDown)
    >>> time.sleep(max(wait, sloth * 1.619395))
    >>> kyung.root._5_4_mc.dispatchEvent(mouseDown)
    >>> time.sleep(max(wait, sloth * 2.414027))
    >>> kyung.root._3_5_mc.dispatchEvent(mouseDown)
    >>> time.sleep(max(wait, sloth * 0.543335))
    >>> kyung.root._3_5_mc.dispatchEvent(mouseDown)
    >>> time.sleep(max(wait, sloth * 2.876771))
    >>> moonhyoung.root._5_6_mc.dispatchEvent(mouseDown)
    >>> time.sleep(max(wait, sloth * 7.559221))
    >>> kyung.root._6_6_mc.dispatchEvent(mouseDown)
    >>> time.sleep(max(wait, sloth * 6.298238))
    >>> kyung.root._6_5_mc.dispatchEvent(mouseDown)
    >>> time.sleep(max(wait, sloth * 1.426986))
    >>> kyung.root._5_7_mc.dispatchEvent(mouseDown)
    >>> time.sleep(max(wait, sloth * 1.276478))
    >>> kyung.root._4_7_mc.dispatchEvent(mouseDown)
    >>> time.sleep(max(wait, sloth * 4.388957))
    >>> kyung.root._4_7_mc.dispatchEvent(mouseDown)
    >>> time.sleep(max(wait, sloth * 8.566781))
    >>> moonhyoung.root._5_7_mc.dispatchEvent(mouseDown)
    >>> time.sleep(max(wait, sloth * 6.321782))
    >>> kyung.root._5_8_mc.dispatchEvent(mouseDown)
    >>> time.sleep(max(wait, sloth * 3.142668))
    >>> kyung.root._5_8_mc.dispatchEvent(mouseDown)
    >>> time.sleep(max(wait, sloth * 6.731769))
    >>> moonhyoung.root._3_7_mc.dispatchEvent(mouseDown)
    >>> time.sleep(max(wait, sloth * 15.789178))
    >>> kyung.root._4_8_mc.dispatchEvent(mouseDown)
    >>> time.sleep(max(wait, sloth * 3.322508))
    >>> kyung.root._4_8_mc.dispatchEvent(mouseDown)
    >>> time.sleep(max(wait, sloth * 1.960702))
    >>> moonhyoung.root._3_8_mc.dispatchEvent(mouseDown)
    >>> time.sleep(max(wait, sloth * 8.859553))
    >>> kyung.root._6_8_mc.dispatchEvent(mouseDown)
    >>> time.sleep(max(wait, sloth * 4.898926))
    >>> kyung.root._6_8_mc.dispatchEvent(mouseDown)
    >>> time.sleep(max(wait, sloth * 2.232298))
    >>> moonhyoung.root._6_7_mc.dispatchEvent(mouseDown)
    >>> time.sleep(max(wait, sloth * 8.733002))
    >>> kyung.root._7_7_mc.dispatchEvent(mouseDown)
    >>> time.sleep(max(wait, sloth * 5.190020))
    >>> kyung.root._6_6_mc.dispatchEvent(mouseDown)
    >>> time.sleep(max(wait, sloth * 1.597347))
    >>> kyung.root._2_2_mc.dispatchEvent(mouseDown)
    >>> time.sleep(max(wait, sloth * 5.532451))
    >>> kyung.root._2_1_mc.dispatchEvent(mouseDown)
    >>> time.sleep(max(wait, sloth * 1.553206))
    >>> kyung.root._1_1_mc.dispatchEvent(mouseDown)
    >>> time.sleep(max(wait, sloth * 3.164118))
    >>> kyung.root._0_2_mc.dispatchEvent(mouseDown)
    >>> time.sleep(max(wait, sloth * 2.074857))
    >>> kyung.root._2_2_mc.dispatchEvent(mouseDown)
    >>> time.sleep(max(wait, sloth * 3.040964))
    >>> kyung.root._2_1_mc.dispatchEvent(mouseDown)
    >>> time.sleep(max(wait, sloth * 3.141526))
    >>> kyung.root._6_3_mc.dispatchEvent(mouseDown)
    >>> time.sleep(max(wait, sloth * 4.665413))
    >>> kyung.root._6_3_mc.dispatchEvent(mouseDown)
    >>> time.sleep(max(wait, sloth * 2.666690))
    >>> moonhyoung.root._7_8_mc.dispatchEvent(mouseDown)
    >>> time.sleep(max(wait, sloth * 6.054614))
    >>> kyung.root._7_3_mc.dispatchEvent(mouseDown)
    >>> time.sleep(max(wait, sloth * 3.631566))
    >>> kyung.root._7_3_mc.dispatchEvent(mouseDown)
    >>> time.sleep(max(wait, sloth * 7.372072))
    >>> kyung.root._7_3_mc.dispatchEvent(mouseDown)
    >>> time.sleep(max(wait, sloth * 3.300416))
    >>> kyung.root._5_1_mc.dispatchEvent(mouseDown)
    >>> time.sleep(max(wait, sloth * 2.965185))
    >>> kyung.root._5_1_mc.dispatchEvent(mouseDown)
    >>> time.sleep(max(wait, sloth * 0.866471))
    >>> moonhyoung.root._2_2_mc.dispatchEvent(mouseDown)
    >>> time.sleep(max(wait, sloth * 4.978062))
    >>> kyung.root._6_6_mc.dispatchEvent(mouseDown)
    >>> time.sleep(max(wait, sloth * 2.191931))
    >>> kyung.root._6_6_mc.dispatchEvent(mouseDown)
    >>> time.sleep(max(wait, sloth * 4.879634))
    >>> moonhyoung.root._6_5_mc.dispatchEvent(mouseDown)
    >>> time.sleep(max(wait, sloth * 9.095511))
    >>> kyung.root._7_6_mc.dispatchEvent(mouseDown)
    >>> time.sleep(max(wait, sloth * 10.976270))
    >>> kyung.root._7_6_mc.dispatchEvent(mouseDown)
    >>> time.sleep(max(wait, sloth * 2.352468))
    >>> moonhyoung.root._7_5_mc.dispatchEvent(mouseDown)
    >>> time.sleep(max(wait, sloth * 3.129568))
    >>> kyung.root._8_5_mc.dispatchEvent(mouseDown)
    >>> time.sleep(max(wait, sloth * 1.818551))
    >>> moonhyoung.root._7_5_mc.dispatchEvent(mouseDown)
    >>> time.sleep(max(wait, sloth * 1.158135))
    >>> kyung.root._8_5_mc.dispatchEvent(mouseDown)
    >>> time.sleep(max(wait, sloth * 3.406220))
    >>> moonhyoung.root._8_6_mc.dispatchEvent(mouseDown)
    >>> time.sleep(max(wait, sloth * 6.607235))
    >>> kyung.root._8_7_mc.dispatchEvent(mouseDown)
    >>> time.sleep(max(wait, sloth * 4.384253))
    >>> kyung.root._8_7_mc.dispatchEvent(mouseDown)
    >>> time.sleep(max(wait, sloth * 9.042295))
    >>> moonhyoung.root._8_4_mc.dispatchEvent(mouseDown)
    >>> time.sleep(max(wait, sloth * 4.014863))
    >>> kyung.root._8_3_mc.dispatchEvent(mouseDown)
    >>> time.sleep(max(wait, sloth * 8.242319))
    >>> kyung.root._8_3_mc.dispatchEvent(mouseDown)
    >>> time.sleep(max(wait, sloth * 1.945073))
    >>> kyung.root._7_4_mc.dispatchEvent(mouseDown)
    >>> time.sleep(max(wait, sloth * 5.067233))
    >>> moonhyoung.root._7_4_mc.dispatchEvent(mouseDown)
    >>> time.sleep(max(wait, sloth * 2.304812))
    >>> kyung.root._6_4_mc.dispatchEvent(mouseDown)
    >>> time.sleep(max(wait, sloth * 1.811712))
    >>> kyung.root._6_4_mc.dispatchEvent(mouseDown)
    >>> time.sleep(max(wait, sloth * 7.267536))
    >>> moonhyoung.root._3_1_mc.dispatchEvent(mouseDown)
    >>> time.sleep(max(wait, sloth * 7.620602))
    >>> kyung.root._6_8_mc.dispatchEvent(mouseDown)
    >>> time.sleep(max(wait, sloth * 1.191881))
    >>> kyung.root._7_7_mc.dispatchEvent(mouseDown)
    >>> time.sleep(max(wait, sloth * 2.614871))
    >>> kyung.root._5_1_mc.dispatchEvent(mouseDown)
    >>> time.sleep(max(wait, sloth * 7.463252))
    >>> kyung.root._5_1_mc.dispatchEvent(mouseDown)
    >>> time.sleep(max(wait, sloth * 5.639728))
    >>> moonhyoung.root._4_0_mc.dispatchEvent(mouseDown)
    >>> time.sleep(max(wait, sloth * 4.833453))
    >>> kyung.root._5_0_mc.dispatchEvent(mouseDown)
    >>> time.sleep(max(wait, sloth * 2.895378))
    >>> kyung.root._5_0_mc.dispatchEvent(mouseDown)
    >>> time.sleep(max(wait, sloth * 7.222165))
    >>> moonhyoung.root._2_0_mc.dispatchEvent(mouseDown)
    >>> time.sleep(max(wait, sloth * 3.376454))
    >>> kyung.root._5_2_mc.dispatchEvent(mouseDown)
    >>> time.sleep(max(wait, sloth * 2.739704))
    >>> kyung.root._4_1_mc.dispatchEvent(mouseDown)
    >>> time.sleep(max(wait, sloth * 4.824631))
    >>> kyung.root._4_1_mc.dispatchEvent(mouseDown)
    >>> time.sleep(max(wait, sloth * 8.675137))
    >>> moonhyoung.root._3_2_mc.dispatchEvent(mouseDown)
    >>> time.sleep(max(wait, sloth * 1.536958))
    >>> kyung.root._4_2_mc.dispatchEvent(mouseDown)
    >>> time.sleep(max(wait, sloth * 1.500512))
    >>> kyung.root._3_2_mc.dispatchEvent(mouseDown)
    >>> time.sleep(max(wait, sloth * 1.364050))
    >>> kyung.root._4_2_mc.dispatchEvent(mouseDown)
    >>> time.sleep(max(wait, sloth * 1.262649))
    >>> kyung.root._2_1_mc.dispatchEvent(mouseDown)
    >>> time.sleep(max(wait, sloth * 1.603103))
    >>> kyung.root._4_2_mc.dispatchEvent(mouseDown)
    >>> time.sleep(max(wait, sloth * 3.309604))
    >>> kyung.root._3_0_mc.dispatchEvent(mouseDown)
    >>> time.sleep(max(wait, sloth * 2.375255))
    >>> kyung.root._3_0_mc.dispatchEvent(mouseDown)
    >>> time.sleep(max(wait, sloth * 6.103130))
    >>> moonhyoung.root._4_0_mc.dispatchEvent(mouseDown)
    >>> time.sleep(max(wait, sloth * 6.301411))
    >>> moonhyoung.root._1_1_mc.dispatchEvent(mouseDown)
    >>> time.sleep(max(wait, sloth * 5.176181))
    >>> kyung.root._4_2_mc.dispatchEvent(mouseDown)
    >>> time.sleep(max(wait, sloth * 3.796914))
    >>> kyung.root._4_2_mc.dispatchEvent(mouseDown)
    >>> time.sleep(max(wait, sloth * 12.865299))

    HACK:  Do not pass, as this would change levels.
    >>> ## kyung.root.pass_mc.dispatchEvent(mouseDown)
    >>> ## time.sleep(max(wait, sloth * 2.138277))
    >>> ## moonhyoung.root.pass_mc.dispatchEvent(mouseDown)
    >>> ## time.sleep(max(wait, sloth * 9.256537))
    >>> ## moonhyoung.root._8_7_mc.dispatchEvent(mouseDown)
    >>> ## time.sleep(max(wait, sloth * 0.688120))
    >>> ## moonhyoung.root._8_6_mc.dispatchEvent(mouseDown)
    >>> ## time.sleep(max(wait, sloth * 5.208640))
    >>> ## moonhyoung.root._5_3_mc.dispatchEvent(mouseDown)
    >>> ## time.sleep(max(wait, sloth * 2.352339))
    >>> ## moonhyoung.root._4_2_mc.dispatchEvent(mouseDown)
    >>> ## time.sleep(max(wait, sloth * 1.418292))
    >>> ## moonhyoung.root._4_0_mc.dispatchEvent(mouseDown)

    
    kyung leaves three stones unconnected around 2,2
        >_< i am confused and annoyed
    '''


def laurens_owner_example():
    '''Laurens selects owner.  Laurens plants and drives out dragon.

    #[This script may start from lobby or new server.]
    #>>> if not globals().get('laurens'):
    #...     laurens, wait = setup_example(configuration, ('laurens', 'groenewegen') )
        >>> code_unit.inline_examples(
        ...     ethan_lukasz_begin_example.__doc__, 
        ...     locals(), globals(), 
        ...     verify_examples = False)
        >>> wait = 4.0 / black._speed
        >>> sloth = 1.0 / black._speed

        >>> laurens = black
        >>> computer_laurens = white

    >>> # example.log level 20 at Thu Aug 12 21:17:06 2010

    >>> laurens.root.level_mc.none_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 4.348000)
    >>> laurens.root.lobby_mc.main_mc._07_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 14.926000)
    >>> laurens.root.lobby_mc._07_mc.score_5_5_2_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 3.216000)
    >>> time.sleep(sloth * 11.608000)

        FOR REPLAY, COMPUTER IS NOT PLAYING.
        >>> laurens.root.game_over_mc.white_computer_mc.enter_mc.dispatchEvent(mouseDown)
        >>> time.sleep(wait)
    >>> mouse_down_and_sleep(laurens, laurens.root.game_over_mc.start_mc, wait)
    >>> time.sleep(sloth * 5.634000)
    >>> mouse_down_and_sleep(laurens, laurens.root._2_2_mc, wait)
    >>> time.sleep(sloth * 11.919000)
    >>> mouse_down_and_sleep(laurens, laurens.root._2_2_mc, wait)
    >>> mouse_down_and_sleep(computer_laurens, computer_laurens.root._1_2_mc, wait)
    >>> time.sleep(sloth * 17.638000)
    >>> mouse_down_and_sleep(laurens, laurens.root._2_1_mc, wait)
    >>> time.sleep(sloth * 5.354000)
    >>> mouse_down_and_sleep(laurens, laurens.root._2_1_mc, wait)
    >>> mouse_down_and_sleep(computer_laurens, computer_laurens.root._1_1_mc, wait)
    >>> time.sleep(sloth * 15.939000)
    >>> mouse_down_and_sleep(laurens, laurens.root._1_0_mc, wait)
    >>> time.sleep(sloth * 2.872000)
    >>> mouse_down_and_sleep(laurens, laurens.root._1_0_mc, wait)
    >>> mouse_down_and_sleep(computer_laurens, computer_laurens.root._0_0_mc, wait)
    >>> time.sleep(sloth * 12.498000)
    >>> mouse_down_and_sleep(laurens, laurens.root._0_1_mc, wait)
    >>> time.sleep(sloth * 2.180000)
    >>> mouse_down_and_sleep(laurens, laurens.root._0_1_mc, wait)
    >>> computer_laurens.root.pass_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 14.222000)
    >>> laurens.root.pass_mc.dispatchEvent(mouseDown)
    >>> laurens.root.level_mc.none_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 5.497000)

    laurens says he feels rich
        ^_^ ah
    laurens guesses dragon arms. yellow attack of some kind against dragon.
        ^_^ o
    laurens says coins jerk.  he asks could coin growth appear fluid?
        >_< uh
    laurens says aw the dragon is giving up already?
        >_< aw
    forget to turn off computer player.  
        during first replay, white 0,0 appears at 4,4.  but second replay okay.
            >_< huh?
    replay twice.  retry manually.  click center.  python master crashes.
        >_< huh?
    '''


def marije_score_example():
    '''Marije tries many spots before going to the center.
        >>> code_unit.inline_examples(
        ...     ethan_lukasz_begin_example.__doc__, 
        ...     locals(), globals(), 
        ...     verify_examples = False)
        >>> wait = 4.0 / black._speed
        >>> sloth = 1.0 / black._speed

        >>> marije = black
        >>> computer_marije = white
    >>> marije.root.lobby_mc._07_mc.score_5_5_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 1.846000)
    >>> time.sleep(sloth * 12.240000)

        FOR REPLAY, COMPUTER IS NOT PLAYING.
        >>> marije.root.game_over_mc.white_computer_mc.enter_mc.dispatchEvent(mouseDown)
        >>> time.sleep(wait)

        white computer button is not blinking.
        >>> marije.root.game_over_mc.white_computer_mc.currentLabel
        'none'
        >>> marije.root.game_over_mc.white_computer_mc.gotoAndPlay('none')


    >>> mouse_down_and_sleep(marije, marije.root.game_over_mc.start_mc, wait)
    >>> time.sleep(sloth * 18.707000)
    >>> mouse_down_and_sleep(marije, marije.root._2_4_mc, wait)
    >>> time.sleep(sloth * 11.345000)
    >>> mouse_down_and_sleep(marije, marije.root._1_3_mc, wait)
    >>> time.sleep(sloth * 10.483000)
    >>> mouse_down_and_sleep(marije, marije.root._4_3_mc, wait)
    >>> time.sleep(sloth * 6.827000)
    >>> mouse_down_and_sleep(marije, marije.root._1_3_mc, wait)
    >>> time.sleep(sloth * 4.515000)
    >>> mouse_down_and_sleep(marije, marije.root._1_3_mc, wait)
    >>> time.sleep(sloth * 3.752000)
    >>> mouse_down_and_sleep(marije, marije.root._1_3_mc, wait)
    >>> time.sleep(sloth * 26.256000)
    >>> mouse_down_and_sleep(marije, marije.root._1_2_mc, wait)
    >>> time.sleep(sloth * 13.395000)
    >>> mouse_down_and_sleep(marije, marije.root._3_2_mc, wait)
    >>> time.sleep(sloth * 13.197000)
    >>> mouse_down_and_sleep(marije, marije.root._4_4_mc, wait)
    >>> time.sleep(sloth * 17.819000)
    >>> mouse_down_and_sleep(marije, marije.root._1_2_mc, wait)
    >>> time.sleep(sloth * 2.381000)
    >>> mouse_down_and_sleep(marije, marije.root._1_2_mc, wait)
    >>> time.sleep(sloth * 2.365000)
    >>> mouse_down_and_sleep(marije, marije.root._1_2_mc, wait)
    >>> time.sleep(sloth * 11.205000)
    >>> mouse_down_and_sleep(marije, marije.root._1_2_mc, wait)
    >>> time.sleep(sloth * 14.343000)
    >>> mouse_down_and_sleep(marije, marije.root._2_3_mc, wait)
    >>> time.sleep(sloth * 13.083000)
    >>> mouse_down_and_sleep(marije, marije.root._2_3_mc, wait)
    >>> time.sleep(sloth * 11.797000)
    >>> mouse_down_and_sleep(marije, marije.root._2_2_mc, wait)
    >>> time.sleep(sloth * 19.607000)
    >>> mouse_down_and_sleep(marije, marije.root._2_2_mc, wait)
    >>> mouse_down_and_sleep(computer_marije, computer_marije.root._3_3_mc, wait)
    >>> marije.root.menu_mc.toggle_mc.dispatchEvent(mouseDown)



see green all over.  
click 1,3.  click 1,2.  see both 
expect to see

INFO:root:prepare_stone(... _1_3_mc, black ...):
,,,,,
,,,$,
,X,,,
,,,,,
,,,,,
INFO:root:imitate_news: lukasz:
INFO:root:imitate_news: lukasz: cursor_mc
INFO:root:imitate_news: lukasz: _0_0_mc _0_1_mc _0_2_mc _0_3_mc _0_4_mc _1_0_mc
_1_1_mc _1_2_mc _1_3_mc:question_black _1_4_mc _2_0_mc _2_2_mc _2_3_mc _2_4_mc _
3_0_mc _3_1_mc _3_2_mc _3_3_mc _3_4_mc _4_0_mc _4_1_mc _4_2_mc _4_3_mc _4_4_mc b
ad_move_mc:show cursor_mc score_mc tutor_mc:small
INFO:root:master.send:
INFO:example:>>> time.sleep(sloth * 30.314000)
INFO:root:imitate_news: lukasz:
INFO:example:>>> mouse_down_and_sleep(lukasz, lukasz.root._1_2_mc, wait)
INFO:root:prepare_stone(... _1_2_mc, black ...):
,,,,,
,,$*,
,X,,,
,,,,,
,,,,,

    '''



def h1_suicide_example():
    '''Game development student at HvA (h1) sees that he previews.
        >>> code_unit.inline_examples(
        ...     ethan_lukasz_begin_example.__doc__, 
        ...     locals(), globals(), 
        ...     verify_examples = False)
        >>> wait = 4.0 / black._speed
        >>> sloth = 1.0 / black._speed
    
        >>> h1 = black
        >>> computer_h1 = white

    >>> h1.root.lobby_mc._00_mc.capture_3_3_2_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 3.465000)

        For replay, computer is not playing.
        >>> h1.root.game_over_mc.white_computer_mc.enter_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 7.540000)
    >>> mouse_down_and_sleep(h1, h1.root.game_over_mc.start_mc, wait)
    >>> time.sleep(sloth * 7.526000)
    >>> mouse_down_and_sleep(h1, h1.root._1_2_mc, wait)
    >>> time.sleep(sloth * 9.874000)
    >>> mouse_down_and_sleep(h1, h1.root._1_1_mc, wait)
    >>> time.sleep(sloth * 3.954000)
    >>> mouse_down_and_sleep(h1, h1.root._1_1_mc, wait)
    >>> mouse_down_and_sleep(computer_h1, computer_h1.root._0_1_mc, wait)
    >>> time.sleep(sloth * 4.430000)
    >>> mouse_down_and_sleep(h1, h1.root._1_2_mc, wait)
    >>> time.sleep(sloth * 7.824000)
    >>> mouse_down_and_sleep(h1, h1.root._0_2_mc, wait)
    >>> time.sleep(sloth * 11.616000)
    >>> mouse_down_and_sleep(h1, h1.root._0_0_mc, wait)
    >>> time.sleep(sloth * 8.339000)
    >>> mouse_down_and_sleep(h1, h1.root._0_0_mc, wait)
    >>> time.sleep(sloth * 8.326000)
    >>> mouse_down_and_sleep(h1, h1.root._1_0_mc, wait)
    >>> time.sleep(sloth * 6.411000)
    >>> mouse_down_and_sleep(h1, h1.root._0_0_mc, wait)
    >>> time.sleep(sloth * 7.021000)
    >>> mouse_down_and_sleep(h1, h1.root._1_0_mc, wait)
    >>> time.sleep(sloth * 2.888000)
    >>> mouse_down_and_sleep(h1, h1.root._1_0_mc, wait)
    >>> mouse_down_and_sleep(computer_h1, computer_h1.root._1_2_mc, wait)
    >>> time.sleep(sloth * 6.005000)
    >>> mouse_down_and_sleep(h1, h1.root._0_0_mc, wait)
    >>> time.sleep(sloth * 6.853000)
    >>> mouse_down_and_sleep(h1, h1.root._0_2_mc, wait)
    >>> time.sleep(sloth * 6.765000)
    >>> mouse_down_and_sleep(h1, h1.root._0_0_mc, wait)
    >>> time.sleep(sloth * 6.840000)
    >>> mouse_down_and_sleep(h1, h1.root._0_0_mc, wait)
    >>> mouse_down_and_sleep(computer_h1, computer_h1.root._2_1_mc, wait)
    >>> time.sleep(sloth * 13.612000)
    
    h1 tries to play on his last liberty.
    he tries again.
    >>> mouse_down_and_sleep(h1, h1.root._2_0_mc, wait)
    >>> time.sleep(sloth * 5.540000)
    >>> mouse_down_and_sleep(h1, h1.root._2_0_mc, wait)
    >>> time.sleep(sloth * 5.818000)
    >>> mouse_down_and_sleep(h1, h1.root._2_2_mc, wait)
    >>> time.sleep(sloth * 8.200000)
    >>> mouse_down_and_sleep(h1, h1.root._0_2_mc, wait)
    >>> time.sleep(sloth * 6.120000)

    Because single capture cannot be snapped back, h1 sees no flames around.
    >>> black.root._0_2_mc.block_south_mc.currentLabel
    'none'
    >>> black.root._0_2_mc.block_west_mc.currentLabel
    'none'
    >>> black.root._0_2_strike_mc.south_mc.currentLabel
    'none'
    >>> black.root._0_2_strike_mc.west_mc.currentLabel
    'none'
    >>> mouse_down_and_sleep(h1, h1.root._2_2_mc, wait)
    >>> time.sleep(sloth * 4.431000)

    h1 had tried to play into surrounded intersection that he could now take.
    >>> mouse_down_and_sleep(h1, h1.root._0_2_mc, wait)
    >>> time.sleep(sloth * 6.353000)
    >>> mouse_down_and_sleep(h1, h1.root._0_2_mc, wait)
    >>> h1.root.level_mc.none_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 11.766000)

    h1 tries to play into a surrounded intersection.

    '''
    

def h1_critical_example():
    '''Game development student at HvA (h1) sees critical and hint.
        >>> code_unit.inline_examples(
        ...     ethan_lukasz_begin_example.__doc__, 
        ...     locals(), globals(), 
        ...     verify_examples = False)
        >>> wait = 4.0 / black._speed
        >>> sloth = 1.0 / black._speed
    
        >>> h1 = black
        >>> computer_h1 = white

    >>> h1.root.lobby_mc._00_mc.capture_critical_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 5.414000)

        For replay, computer is not playing.
        >>> h1.root.game_over_mc.white_computer_mc.enter_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 7.540000)
    >>> ## time.sleep(sloth * 12.443000)
    >>> mouse_down_and_sleep(h1, h1.root.game_over_mc.start_mc, wait)
    >>> time.sleep(sloth * 6.312000)
    >>> mouse_down_and_sleep(h1, h1.root._2_3_mc, wait)
    >>> time.sleep(sloth * 3.618000)
    >>> mouse_down_and_sleep(h1, h1.root._2_3_mc, wait)
    >>> time.sleep(sloth * 3.411000)
    >>> mouse_down_and_sleep(h1, h1.root._2_3_mc, wait)
    >>> time.sleep(sloth * 4.072000)
    >>> mouse_down_and_sleep(h1, h1.root._2_3_mc, wait)
    >>> time.sleep(sloth * 5.135000)
    >>> mouse_down_and_sleep(h1, h1.root._3_1_mc, wait)
    >>> time.sleep(sloth * 4.088000)
    >>> mouse_down_and_sleep(h1, h1.root._3_1_mc, wait)
    >>> mouse_down_and_sleep(computer_h1, computer_h1.root._2_1_mc, wait)
    >>> time.sleep(sloth * 10.216000)
    >>> mouse_down_and_sleep(h1, h1.root._4_2_mc, wait)
    >>> time.sleep(sloth * 6.511000)
    >>> mouse_down_and_sleep(h1, h1.root._4_2_mc, wait)
    >>> time.sleep(sloth * 5.173000)
    >>> mouse_down_and_sleep(h1, h1.root._4_1_mc, wait)
    >>> time.sleep(sloth * 7.023000)
    >>> mouse_down_and_sleep(h1, h1.root._4_1_mc, wait)
    >>> time.sleep(sloth * 12.746000)
    >>> mouse_down_and_sleep(h1, h1.root._1_1_mc, wait)
    >>> time.sleep(sloth * 5.747000)
    >>> mouse_down_and_sleep(h1, h1.root._1_1_mc, wait)
    >>> mouse_down_and_sleep(computer_h1, computer_h1.root._4_1_mc, wait)
    >>> time.sleep(sloth * 6.047000)
    >>> mouse_down_and_sleep(h1, h1.root._2_0_mc, wait)
    >>> time.sleep(sloth * 7.273000)
    >>> mouse_down_and_sleep(h1, h1.root._2_0_mc, wait)
    >>> h1.root.game_over_mc.score_mc.lobby_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 5.218000)
    >>> h1.root.level_mc.none_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 5.378000)
    '''




def h1_capture_example():
    '''Game development student at HvA (h1) captures.
        >>> code_unit.inline_examples(
        ...     ethan_lukasz_begin_example.__doc__, 
        ...     locals(), globals(), 
        ...     verify_examples = False)
        >>> wait = 4.0 / black._speed
        >>> sloth = 1.0 / black._speed
    
        >>> h1 = black
        >>> computer_h1 = white

    >>> h1.root.level_mc.none_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 5.378000)
    >>> h1.root.lobby_mc._00_mc.capture_5_5_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 5.782000)

        For replay, computer is not playing.
        >>> h1.root.game_over_mc.white_computer_mc.enter_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 10.648000)
    >>> mouse_down_and_sleep(h1, h1.root.game_over_mc.start_mc, wait)
    >>> time.sleep(sloth * 6.753000)
    >>> mouse_down_and_sleep(h1, h1.root._0_1_mc, wait)
    >>> time.sleep(sloth * 3.253000)
    >>> mouse_down_and_sleep(h1, h1.root._0_1_mc, wait)
    >>> time.sleep(sloth * 1.388000)
    >>> mouse_down_and_sleep(h1, h1.root._0_1_mc, wait)
    >>> time.sleep(sloth * 13.839000)
    >>> mouse_down_and_sleep(h1, h1.root._1_2_mc, wait)
    >>> time.sleep(sloth * 12.427000)
    >>> mouse_down_and_sleep(h1, h1.root._1_2_mc, wait)
    >>> time.sleep(sloth * 1.814000)
    >>> mouse_down_and_sleep(h1, h1.root._1_2_mc, wait)
    >>> time.sleep(sloth * 3.148000)
    >>> mouse_down_and_sleep(h1, h1.root._1_2_mc, wait)
    >>> time.sleep(sloth * 3.604000)
    >>> mouse_down_and_sleep(h1, h1.root._2_2_mc, wait)
    >>> time.sleep(sloth * 3.025000)
    >>> mouse_down_and_sleep(h1, h1.root._2_2_mc, wait)
    >>> mouse_down_and_sleep(computer_h1, computer_h1.root._2_1_mc, wait)
    >>> time.sleep(sloth * 10.595000)
    >>> mouse_down_and_sleep(h1, h1.root._1_1_mc, wait)
    >>> time.sleep(sloth * 4.392000)
    >>> mouse_down_and_sleep(h1, h1.root._1_1_mc, wait)
    >>> mouse_down_and_sleep(computer_h1, computer_h1.root._2_3_mc, wait)
    >>> time.sleep(sloth * 13.416000)
    >>> mouse_down_and_sleep(h1, h1.root._2_0_mc, wait)
    >>> time.sleep(sloth * 5.672000)
    >>> mouse_down_and_sleep(h1, h1.root._2_0_mc, wait)
    >>> mouse_down_and_sleep(computer_h1, computer_h1.root._3_2_mc, wait)
    >>> time.sleep(sloth * 4.912000)
    >>> mouse_down_and_sleep(h1, h1.root._3_1_mc, wait)
    >>> time.sleep(sloth * 7.885000)
    >>> mouse_down_and_sleep(h1, h1.root._3_1_mc, wait)
    '''


def h1_dominate_5_5_example():
    '''Game development student at HvA (h1) dominates but gives up.
        >>> code_unit.inline_examples(
        ...     ethan_lukasz_begin_example.__doc__, 
        ...     locals(), globals(), 
        ...     verify_examples = False)
        >>> wait = 4.0 / black._speed
        >>> sloth = 1.0 / black._speed
    
        >>> h1 = black
        >>> computer_h1 = white

    >>> h1.root.level_mc.none_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 5.985000)
    >>> h1.root.game_over_mc.score_mc.lobby_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 4.078000)
    >>> h1.root.lobby_mc._04_mc.dominate_5_5_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 6.083000)

        For replay, computer is not playing.
        >>> h1.root.game_over_mc.white_computer_mc.enter_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 5.660000)
    >>> mouse_down_and_sleep(h1, h1.root.game_over_mc.start_mc, wait)
    >>> time.sleep(sloth * 5.760000)
    >>> mouse_down_and_sleep(h1, h1.root._3_2_mc, wait)
    >>> time.sleep(sloth * 4.972000)
    >>> mouse_down_and_sleep(h1, h1.root._3_2_mc, wait)
    >>> time.sleep(sloth * 3.010000)
    >>> mouse_down_and_sleep(h1, h1.root._2_2_mc, wait)
    >>> time.sleep(sloth * 3.390000)
    >>> mouse_down_and_sleep(h1, h1.root._2_2_mc, wait)
    >>> mouse_down_and_sleep(computer_h1, computer_h1.root._2_1_mc, wait)
    >>> time.sleep(sloth * 10.302000)
    >>> mouse_down_and_sleep(h1, h1.root._3_2_mc, wait)
    >>> time.sleep(sloth * 4.380000)
    >>> mouse_down_and_sleep(h1, h1.root._3_2_mc, wait)
    >>> mouse_down_and_sleep(computer_h1, computer_h1.root._1_2_mc, wait)
    >>> time.sleep(sloth * 9.537000)
    >>> mouse_down_and_sleep(h1, h1.root._3_1_mc, wait)
    >>> time.sleep(sloth * 2.385000)
    >>> mouse_down_and_sleep(h1, h1.root._3_1_mc, wait)
    >>> mouse_down_and_sleep(computer_h1, computer_h1.root._0_1_mc, wait)
    >>> time.sleep(sloth * 22.849000)
    >>> mouse_down_and_sleep(h1, h1.root._3_0_mc, wait)
    >>> time.sleep(sloth * 11.656000)
    >>> mouse_down_and_sleep(h1, h1.root._3_0_mc, wait)
    >>> mouse_down_and_sleep(computer_h1, computer_h1.root._2_3_mc, wait)
    >>> time.sleep(sloth * 16.259000)
    >>> mouse_down_and_sleep(h1, h1.root._1_0_mc, wait)
    >>> time.sleep(sloth * 2.591000)
    >>> mouse_down_and_sleep(h1, h1.root._1_0_mc, wait)
    >>> mouse_down_and_sleep(computer_h1, computer_h1.root._1_1_mc, wait)
    >>> time.sleep(sloth * 11.061000)
    >>> mouse_down_and_sleep(h1, h1.root._2_0_mc, wait)
    >>> time.sleep(sloth * 5.315000)
    >>> mouse_down_and_sleep(h1, h1.root._2_0_mc, wait)
    >>> mouse_down_and_sleep(computer_h1, computer_h1.root._3_3_mc, wait)
    >>> time.sleep(sloth * 18.317000)
    >>> mouse_down_and_sleep(h1, h1.root._1_3_mc, wait)
    >>> time.sleep(sloth * 5.584000)
    >>> mouse_down_and_sleep(h1, h1.root._1_3_mc, wait)
    >>> mouse_down_and_sleep(computer_h1, computer_h1.root._0_3_mc, wait)
    >>> time.sleep(sloth * 16.728000)
    >>> mouse_down_and_sleep(h1, h1.root._0_4_mc, wait)
    >>> time.sleep(sloth * 8.422000)
    >>> mouse_down_and_sleep(h1, h1.root._1_4_mc, wait)
    >>> time.sleep(sloth * 2.562000)
    >>> mouse_down_and_sleep(h1, h1.root._1_4_mc, wait)
    >>> mouse_down_and_sleep(computer_h1, computer_h1.root._2_4_mc, wait)
    >>> h1.root.menu_mc.toggle_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 16.118000)

    h1 ignore big green arrow.
    instead he slowly builds a connected castle wall 3_1.
    he builds a bunker that will be dead.
    he connects to that bunker that will die.  also dead.

    '''


def h1_dominate_3_3_example():
    '''Game development student at HvA (h1) dominates 3x3.
        >>> code_unit.inline_examples(
        ...     ethan_lukasz_begin_example.__doc__, 
        ...     locals(), globals(), 
        ...     verify_examples = False)
        >>> wait = 4.0 / black._speed
        >>> sloth = 1.0 / black._speed
    
        >>> h1 = black
        >>> computer_h1 = white

    >>> h1.root.level_mc.none_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 5.985000)
    >>> h1.root.lobby_mc._04_mc.dominate_3_3_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 3.718000)

        For replay, computer is not playing.
        >>> h1.root.game_over_mc.white_computer_mc.enter_mc.dispatchEvent(mouseDown)

    >>> time.sleep(sloth * 8.755000)
    >>> mouse_down_and_sleep(h1, h1.root.game_over_mc.start_mc, wait)
    >>> time.sleep(sloth * 6.502000)
    >>> mouse_down_and_sleep(h1, h1.root._1_1_mc, wait)
    >>> time.sleep(sloth * 2.833000)
    >>> mouse_down_and_sleep(h1, h1.root._1_1_mc, wait)
    >>> mouse_down_and_sleep(computer_h1, computer_h1.root._1_2_mc, wait)
    >>> time.sleep(sloth * 10.384000)
    >>> mouse_down_and_sleep(h1, h1.root._0_2_mc, wait)
    >>> time.sleep(sloth * 4.040000)
    >>> mouse_down_and_sleep(h1, h1.root._0_2_mc, wait)
    >>> mouse_down_and_sleep(computer_h1, computer_h1.root._2_0_mc, wait)
    >>> time.sleep(sloth * 4.970000)
    >>> mouse_down_and_sleep(h1, h1.root._2_2_mc, wait)
    >>> time.sleep(sloth * 6.279000)
    >>> mouse_down_and_sleep(h1, h1.root._2_2_mc, wait)
    >>> h1.root._1_1_mc.dragon_status_mc.currentLabel
    'none'
    >>> h1.root._1_0_mc.top_move_mc.currentLabel
    'none'
    >>> mouse_down_and_sleep(computer_h1, computer_h1.root._2_1_mc, wait)
    >>> time.sleep(sloth * 10.193000)

    Even though white plays into danger,
    h1 as a new player needs to see that his stones are in critical condition.
    h1 sees his stones are in critical condition.
    >>> h1.root._1_1_mc.dragon_status_mc.currentLabel
    'white_attack'
    >>> h1.root._2_2_mc.dragon_status_mc.currentLabel
    'white_attack'
    >>> h1.root._1_0_mc.top_move_mc.currentLabel
    'black'
    >>> mouse_down_and_sleep(h1, h1.root._1_2_mc, wait)
    >>> time.sleep(sloth * 1.799000)
    >>> mouse_down_and_sleep(h1, h1.root._1_2_mc, wait)
    >>> mouse_down_and_sleep(computer_h1, computer_h1.root._1_0_mc, wait)
    >>> time.sleep(sloth * 12.645000)
    >>> mouse_down_and_sleep(h1, h1.root._0_0_mc, wait)
    >>> time.sleep(sloth * 11.786000)
    >>> mouse_down_and_sleep(h1, h1.root._0_0_mc, wait)
    >>> mouse_down_and_sleep(computer_h1, computer_h1.root._2_0_mc, wait)
    >>> time.sleep(sloth * 11.787000)
    >>> mouse_down_and_sleep(h1, h1.root._2_1_mc, wait)
    >>> time.sleep(sloth * 7.337000)
    >>> mouse_down_and_sleep(h1, h1.root._2_1_mc, wait)
    >>> time.sleep(sloth * 5.663000)
    >>> mouse_down_and_sleep(h1, h1.root._1_0_mc, wait)
    >>> time.sleep(sloth * 5.733000)
    >>> mouse_down_and_sleep(h1, h1.root._1_0_mc, wait)
    >>> time.sleep(sloth * 3.160000)
    >>> mouse_down_and_sleep(h1, h1.root._2_0_mc, wait)
    >>> time.sleep(sloth * 1.590000)
    >>> mouse_down_and_sleep(h1, h1.root._2_0_mc, wait)
    >>> h1.root.comment_mc.none_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 7.224000)
    >>> time.sleep(sloth * 51.381000)
    >>> h1.root.pass_mc.dispatchEvent(mouseDown)
    >>> mouse_down_and_sleep(computer_h1, computer_h1.root._2_1_mc, wait)
    >>> time.sleep(sloth * 29.142000)
    >>> h1.root.pass_mc.dispatchEvent(mouseDown)
    >>> mouse_down_and_sleep(computer_h1, computer_h1.root._1_0_mc, wait)
    >>> time.sleep(sloth * 12.831000)
    >>> h1.root.pass_mc.dispatchEvent(mouseDown)
    >>> mouse_down_and_sleep(computer_h1, computer_h1.root._1_2_mc, wait)
    >>> h1.root.menu_mc.toggle_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 4.653000)
   
    h1 does not capture.  instead he fills in.  this reduces his liberties.
    seki.  dual life.  h1 tries to build but dare not.  he tries again to build, which would put him in danger.
    h1 sees old tutor
    '''


def eamon_capture_3_3_example():
    '''Eamon, game development student at HvA (h3) captures 3x3.
    He clicks on several squares.
        >>> code_unit.inline_examples(
        ...     ethan_lukasz_begin_example.__doc__, 
        ...     locals(), globals(), 
        ...     verify_examples = False)
        >>> wait = 4.0 / black._speed
        >>> sloth = 1.0 / black._speed
    
        >>> h3 = black
        >>> computer_h3 = white

    >>> h3.root.level_mc.none_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 5.985000)

        For replay, computer is not playing.
        >>> h3.root.game_over_mc.white_computer_mc.enter_mc.dispatchEvent(mouseDown)

    >>> h3.root.lobby_mc._00_mc.capture_3_3_2_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 4.265254)
    >>> time.sleep(sloth * 5.308617)
    >>> mouse_down_and_sleep(h3, h3.root.game_over_mc.start_mc, wait)
    >>> time.sleep(sloth * 1.173034)
    >>> mouse_down_and_sleep(h3, h3.root._0_2_mc, wait)
    >>> time.sleep(sloth * 0.420009)
    >>> mouse_down_and_sleep(h3, h3.root._1_1_mc, wait)
    >>> time.sleep(sloth * 0.576928)
    >>> mouse_down_and_sleep(h3, h3.root._0_2_mc, wait)
    >>> time.sleep(sloth * 0.558891)
    >>> mouse_down_and_sleep(h3, h3.root._0_0_mc, wait)
    >>> time.sleep(sloth * 0.536804)
    >>> mouse_down_and_sleep(h3, h3.root._0_2_mc, wait)
    >>> time.sleep(sloth * 0.771499)
    >>> mouse_down_and_sleep(h3, h3.root._1_0_mc, wait)
    >>> time.sleep(sloth * 0.644445)
    >>> mouse_down_and_sleep(h3, h3.root._0_2_mc, wait)
    >>> time.sleep(sloth * 0.527314)
    >>> mouse_down_and_sleep(h3, h3.root._1_2_mc, wait)
    >>> time.sleep(sloth * 2.534716)
    >>> mouse_down_and_sleep(h3, h3.root._0_2_mc, wait)
    >>> time.sleep(sloth * 1.544367)
    >>> mouse_down_and_sleep(h3, h3.root._1_0_mc, wait)
    >>> time.sleep(sloth * 0.118066)
    >>> mouse_down_and_sleep(h3, h3.root._1_0_mc, wait)
    >>> time.sleep(sloth * 1.807500)
    >>> mouse_down_and_sleep(h3, h3.root._1_2_mc, wait)
    >>> time.sleep(sloth * 1.956448)
    >>> mouse_down_and_sleep(h3, h3.root._0_2_mc, wait)
    >>> time.sleep(sloth * 1.629161)
    >>> mouse_down_and_sleep(h3, h3.root._1_0_mc, wait)
    >>> time.sleep(sloth * 2.763932)
    >>> mouse_down_and_sleep(h3, h3.root._1_2_mc, wait)
    >>> time.sleep(sloth * 1.203994)
    >>> mouse_down_and_sleep(h3, h3.root._0_2_mc, wait)
    >>> time.sleep(sloth * 0.784401)
    >>> mouse_down_and_sleep(h3, h3.root._1_2_mc, wait)
    >>> time.sleep(sloth * 0.521287)
    >>> mouse_down_and_sleep(h3, h3.root._0_2_mc, wait)
    >>> time.sleep(sloth * 0.855446)
    >>> mouse_down_and_sleep(h3, h3.root._1_2_mc, wait)
    >>> time.sleep(sloth * 1.104164)
    >>> mouse_down_and_sleep(h3, h3.root._0_2_mc, wait)
    >>> time.sleep(sloth * 4.847645)
    >>> mouse_down_and_sleep(h3, h3.root._1_2_mc, wait)
    >>> time.sleep(sloth * 0.610838)
    >>> mouse_down_and_sleep(h3, h3.root._0_2_mc, wait)
    >>> time.sleep(sloth * 1.280123)
    >>> mouse_down_and_sleep(h3, h3.root._1_0_mc, wait)
    >>> time.sleep(sloth * 1.162370)
    >>> mouse_down_and_sleep(h3, h3.root._0_2_mc, wait)
    >>> time.sleep(sloth * 3.689697)
    >>> mouse_down_and_sleep(h3, h3.root._0_2_mc, wait)
    >>> time.sleep(sloth * 2.218811)
    >>> mouse_down_and_sleep(h3, h3.root._0_2_mc, wait)
    >>> time.sleep(sloth * 0.296034)
    >>> mouse_down_and_sleep(h3, h3.root._0_2_mc, wait)
    >>> time.sleep(sloth * 4.702846)
    >>> mouse_down_and_sleep(h3, h3.root._0_2_mc, wait)
    >>> time.sleep(sloth * 0.136423)
    >>> mouse_down_and_sleep(h3, h3.root._0_2_mc, wait)
    >>> time.sleep(sloth * 3.661934)
    >>> mouse_down_and_sleep(h3, h3.root._0_2_mc, wait)
    >>> time.sleep(sloth * 6.445635)
    >>> mouse_down_and_sleep(h3, h3.root._1_0_mc, wait)
    >>> time.sleep(sloth * 4.154466)
    >>> mouse_down_and_sleep(h3, h3.root._1_0_mc, wait)
    >>> time.sleep(sloth * 3.133246)
    >>> mouse_down_and_sleep(h3, h3.root._1_1_mc, wait)
    >>> time.sleep(sloth * 4.173066)
    >>> mouse_down_and_sleep(h3, h3.root._0_2_mc, wait)
    >>> time.sleep(sloth * 5.450723)
    >>> mouse_down_and_sleep(h3, h3.root._0_2_mc, wait)
    >>> time.sleep(sloth * 3.303831)
    >>> mouse_down_and_sleep(h3, h3.root._0_2_mc, wait)
    >>> time.sleep(sloth * 3.448938)
    >>> mouse_down_and_sleep(h3, h3.root._1_0_mc, wait)
    >>> time.sleep(sloth * 3.781643)
    >>> mouse_down_and_sleep(h3, h3.root._2_1_mc, wait)
    >>> time.sleep(sloth * 5.731747)
    >>> h3.root.menu_mc.toggle_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 8.939919)
    '''


def moonhyoung_kyung_join_example():
    '''Moonhyoung logs on and creates multiplayer room.
    Later, Kyung logs on and joins that room.
    >>> moonhyoung, wait = setup_example(configuration, 
    ...     ('moonhyoung', 'park') )
    >>> sloth = 1.0 / moonhyoung._speed
    >>> moonhyoung.root.lobby_mc.main_mc.multiplayer_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 6.416072)

    [TODO:  server logs create and join]
    >>> moonhyoung.root.lobby_mc.create_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 4.180042)
    >>> time.sleep(sloth * 4.685594)
    >>> kyung, wait = setup_user(configuration, 'kyung', 'min')
    >>> kyung.root.level_mc.none_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 2.613354)
    >>> kyung.root.lobby_mc.main_mc._14_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 1.221319)
    >>> kyung.root.lobby_mc._14_mc.main_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 2.335398)
    >>> kyung.root.lobby_mc.main_mc.multiplayer_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 1.711173)
    >>> kyung.root.comment_mc.none_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 6.053805)
    >>> kyung.root.game_over_mc.currentLabel
    'none'
    >>> kyung.root.currentLabel
    'lobby'
    >>> kyung.root.gateway_mc.currentLabel
    'none'

    [TODO:  server logs create and join]
    >>> kyung.root.lobby_mc.join_mc.enter_btn.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 0.859956)
    >>> kyung.root.game_over_mc.currentLabel
    'setup'
    >>> kyung.root.currentLabel
    'table'
    >>> kyung.root.gateway_mc.currentLabel
    'none'
    >>> kyung.root.gateway_mc.none_mc.dispatchEvent(mouseDown)


    #>>> time.sleep(sloth * 2.393575)
    #>>> time.sleep(sloth * 2.143803)
    #>>> kyung.root.lobby_mc.join_mc.enter_btn.dispatchEvent(mouseDown)
    #>>> time.sleep(sloth * 0.798483)
    #>>> kyung.root.gateway_mc.none_mc.dispatchEvent(mouseDown)
    #>>> time.sleep(sloth * 0.835105)
    #>>> time.sleep(sloth * 9.449096)
    #>>> moonhyoung.root.menu_mc.toggle_mc.dispatchEvent(mouseDown)
    #>>> time.sleep(sloth * 5.069107)
    #>>> moonhyoung.root.menu_mc.lobby_mc.dispatchEvent(mouseDown)
    #>>> time.sleep(sloth * 1.130928)
    #>>> moonhyoung.root.lobby_mc._main_mc.dispatchEvent(mouseDown)
    #>>> time.sleep(sloth * 1.776209)
    #>>> moonhyoung.root.lobby_mc.main_mc.multiplayer_mc.dispatchEvent(mouseDown)
    #>>> time.sleep(sloth * 1.539171)
    #>>> time.sleep(sloth * 184.055824)
    #>>> time.sleep(sloth * 10.003608)
    #>>> kyung.root.level_mc.none_mc.dispatchEvent(mouseDown)
    #>>> time.sleep(sloth * 4.269235)
    #>>> kyung.root.menu_mc.toggle_mc.dispatchEvent(mouseDown)
    #>>> time.sleep(sloth * 1.431174)
    #>>> kyung.root.menu_mc.lobby_mc.dispatchEvent(mouseDown)
    #>>> time.sleep(sloth * 0.879121)
    #>>> kyung.root.lobby_mc.main_mc.multiplayer_mc.dispatchEvent(mouseDown)
    #>>> time.sleep(sloth * 1.570883)
    #>>> moonhyoung.root.chat_input_txt.text = "please goto multiplayer and click my room"
    #>>> moonhyoung.root.chat_input_mc.dispatchEvent(mouseDown)
    #>>> time.sleep(sloth * 13.975495)
    #>>> kyung.root.comment_mc.none_mc.dispatchEvent(mouseDown)
    #>>> time.sleep(sloth * 4.612675)
    #>>> moonhyoung.root.comment_mc.none_mc.dispatchEvent(mouseDown)
    #>>> time.sleep(sloth * 1.471209)
    '''

def moonhyoung_kyung_single_join_example():
    '''Moonhyoung logs on and starts single-player, quits.
    He then creates multiplayer room.
    Later, Kyung logs on and joins that room.
    >>> moonhyoung, wait = setup_example(configuration, 
    ...     ('moonhyoung', 'park') )
    >>> sloth = 1.0 / moonhyoung._speed
    >>> moonhyoung.root.lobby_mc._14_mc.extra_stone_9_9_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 1.896891)
    >>> moonhyoung.root.lobby_mc.join_mc.join_txt.text
    'FIELD'
    >>> moonhyoung.root.gateway_mc.none_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 1.550343)
    >>> moonhyoung.root.comment_mc.none_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 0.774998)
    >>> moonhyoung.root.menu_mc.toggle_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 1.592462)
    >>> moonhyoung.root.menu_mc.lobby_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 0.728685)
    >>> moonhyoung.root.lobby_mc._14_mc.main_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 1.152006)
    >>> moonhyoung.root.lobby_mc.main_mc.multiplayer_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 6.416072)
    >>> moonhyoung.root.lobby_mc.join_mc.join_txt.text
    ''

    [TODO:  server logs create and join]
    >>> moonhyoung.root.lobby_mc.create_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 4.180042)
    >>> moonhyoung.root.lobby_mc.join_mc.join_txt.text
    'moonhyoung'
    >>> time.sleep(sloth * 4.685594)
    >>> kyung, wait = setup_user(configuration, 'kyung', 'min')
    >>> kyung.root.level_mc.none_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 2.613354)
    >>> kyung.root.lobby_mc.join_mc.join_txt.text
    'moonhyoung'
    >>> kyung.root.lobby_mc.main_mc._14_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 1.221319)
    >>> kyung.root.lobby_mc._14_mc.main_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 2.335398)
    >>> kyung.root.lobby_mc.main_mc.multiplayer_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 1.711173)
    >>> kyung.root.lobby_mc.join_mc.join_txt.text
    'moonhyoung'
    >>> kyung.root.comment_mc.none_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 6.053805)
    >>> kyung.root.game_over_mc.currentLabel
    'none'
    >>> kyung.root.currentLabel
    'lobby'
    >>> kyung.root.gateway_mc.currentLabel
    'none'
    >>> kyung.root.lobby_mc.join_mc.join_txt.text
    'moonhyoung'

    [TODO:  server logs create and join]
    >>> kyung.root.lobby_mc.join_mc.enter_btn.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 0.859956)
    >>> kyung.root.game_over_mc.currentLabel
    'setup'
    >>> kyung.root.currentLabel
    'table'
    >>> kyung.root.gateway_mc.currentLabel
    'none'
    >>> kyung.root.lobby_mc.join_mc.join_txt.text
    'moonhyoung'
    >>> kyung.root.gateway_mc.none_mc.dispatchEvent(mouseDown)


    #>>> time.sleep(sloth * 2.393575)
    #>>> time.sleep(sloth * 2.143803)
    #>>> kyung.root.lobby_mc.join_mc.enter_btn.dispatchEvent(mouseDown)
    #>>> time.sleep(sloth * 0.798483)
    #>>> kyung.root.gateway_mc.none_mc.dispatchEvent(mouseDown)
    #>>> time.sleep(sloth * 0.835105)
    #>>> time.sleep(sloth * 9.449096)
    #>>> moonhyoung.root.menu_mc.toggle_mc.dispatchEvent(mouseDown)
    #>>> time.sleep(sloth * 5.069107)
    #>>> moonhyoung.root.menu_mc.lobby_mc.dispatchEvent(mouseDown)
    #>>> time.sleep(sloth * 1.130928)
    #>>> moonhyoung.root.lobby_mc._main_mc.dispatchEvent(mouseDown)
    #>>> time.sleep(sloth * 1.776209)
    #>>> moonhyoung.root.lobby_mc.main_mc.multiplayer_mc.dispatchEvent(mouseDown)
    #>>> time.sleep(sloth * 1.539171)
    #>>> time.sleep(sloth * 184.055824)
    #>>> time.sleep(sloth * 10.003608)
    #>>> kyung.root.level_mc.none_mc.dispatchEvent(mouseDown)
    #>>> time.sleep(sloth * 4.269235)
    #>>> kyung.root.menu_mc.toggle_mc.dispatchEvent(mouseDown)
    #>>> time.sleep(sloth * 1.431174)
    #>>> kyung.root.menu_mc.lobby_mc.dispatchEvent(mouseDown)
    #>>> time.sleep(sloth * 0.879121)
    #>>> kyung.root.lobby_mc.main_mc.multiplayer_mc.dispatchEvent(mouseDown)
    #>>> time.sleep(sloth * 1.570883)
    #>>> moonhyoung.root.chat_input_txt.text = "please goto multiplayer and click my room"
    #>>> moonhyoung.root.chat_input_mc.dispatchEvent(mouseDown)
    #>>> time.sleep(sloth * 13.975495)
    #>>> kyung.root.comment_mc.none_mc.dispatchEvent(mouseDown)
    #>>> time.sleep(sloth * 4.612675)
    #>>> moonhyoung.root.comment_mc.none_mc.dispatchEvent(mouseDown)
    #>>> time.sleep(sloth * 1.471209)
    '''


def moonhyoung_kyung_problem_join_example():
    '''Kyung starts problem.  Moonhyoung creates room.
    Kyung quits problem and goes to multiplayer and sees room.
    >>> # example.log level 20 at Wed Sep 22 20:56:22 2010

    >>> moonhyoung, kyung, wait = setup_example(configuration, 
    ...     ('moonhyoung', 'park'), ('kyung', 'min') )
    >>> sloth = 1.0 / moonhyoung._speed
    >>> moonhyoung.root.comment_mc.none_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 4.679000)
    >>> kyung.root.comment_mc.none_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 4.320000)
    >>> kyung.root.lobby_mc.main_mc._00_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 2.410000)
    >>> kyung.root.lobby_mc._00_mc.capture_3_3_1_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 3.416000)
    >>> mouse_down_and_sleep(kyung, kyung.root.game_over_mc.start_mc, wait)
    >>> time.sleep(sloth * 2.831000)
    >>> mouse_down_and_sleep(kyung, kyung.root._1_1_mc, wait)
    >>> ## mouse_down_and_sleep(computer_kyung, computer_kyung.root._2_1_mc, wait)
    >>> moonhyoung.root.lobby_mc.main_mc.multiplayer_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 4.013000)
    >>> moonhyoung.root.lobby_mc.join_mc.join_txt.text
    'FIELD'

    [TODO:  server logs create and join]
    >>> moonhyoung.root.lobby_mc.create_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 4.403000)
    >>> moonhyoung.root.lobby_mc.join_mc.join_txt.text
    'moonhyoung'
    >>> kyung.root.lobby_mc.join_mc.join_txt.text
    'moonhyoung'
    >>> time.sleep(sloth * 3.543000)
    >>> mouse_down_and_sleep(kyung, kyung.root._1_2_mc, wait)
    >>> ## mouse_down_and_sleep(computer_kyung, computer_kyung.root._1_0_mc, wait)
    >>> kyung.root.lobby_mc.join_mc.join_txt.text
    'moonhyoung'
    >>> kyung.root.menu_mc.toggle_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 2.466000)
    >>> kyung.root.lobby_mc.join_mc.join_txt.text
    'moonhyoung'
    >>> kyung.root.currentLabel
    '_3_3'
    >>> kyung.root.menu_mc.lobby_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 3.006000)
    >>> kyung.root.lobby_mc.join_mc.join_txt.text
    'moonhyoung'
    >>> kyung.root.currentLabel
    'lobby'
    >>> kyung.root.lobby_mc._00_mc.main_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 3.656000)
    >>> kyung.root.lobby_mc.join_mc.join_txt.text
    'moonhyoung'
    >>> kyung.root.lobby_mc.main_mc.multiplayer_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 3.755000)
    >>> kyung.root.lobby_mc.join_mc.join_txt.text
    'moonhyoung'

    [TODO:  server logs create and join]
    >>> kyung.root.lobby_mc.join_mc.enter_btn.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 2.859956)
    >>> kyung.root.game_over_mc.currentLabel
    'setup'
    >>> kyung.root.currentLabel
    'table'
    >>> kyung.root.gateway_mc.currentLabel
    'none'
    >>> kyung.root.lobby_mc.join_mc.join_txt.text
    'moonhyoung'
    '''


def jerry_lobby_then_play_example():
    '''Jerry mysteriously goes back to lobby yet then plays a stone.
    This is not valid, yet server remains online.
    TODO:  How can I replicate going through win screen to lobby in middle?
    >>> h1, wait = setup_example(configuration, 
    ...     ('h1', 'hva1') )
    >>> sloth = 1.0 / h1._speed
    >>> h1.root.lobby_mc.main_mc._00_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 7.522876)
    >>> h1.root.lobby_mc._00_mc.capture_3_3_1_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 2.301217)
    >>> time.sleep(sloth * 10.809108)
    >>> time.sleep(sloth * 6.380523)
    >>> mouse_down_and_sleep(h1, h1.root.game_over_mc.start_mc, wait)
    >>> time.sleep(sloth * 0.106331)
    >>> time.sleep(sloth * 3.903500)
    >>> mouse_down_and_sleep(h1, h1.root._2_1_mc, wait)
    >>> ## mouse_down_and_sleep(computer_h1, computer_h1.root._1_2_mc, wait)
    >>> time.sleep(sloth * 5.583395)
    >>> time.sleep(sloth * 10.848192)
    >>> mouse_down_and_sleep(h1, h1.root._0_2_mc, wait)
    >>> time.sleep(sloth * 1.811797)
    >>> time.sleep(sloth * 3.857711)
    >>> h1.root.game_over_mc.score_mc.lobby_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 2.747556)
    >>> h1.root.lobby_mc._00_mc.capture_corner_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 5.387394)
    >>> time.sleep(sloth * 13.231763)
    >>> mouse_down_and_sleep(h1, h1.root.game_over_mc.start_mc, wait)
    >>> time.sleep(sloth * 4.122452)
    >>> mouse_down_and_sleep(h1, h1.root._1_2_mc, wait)
    >>> time.sleep(sloth * 0.505222)
    >>> mouse_down_and_sleep(h1, h1.root._1_2_mc, wait)
    >>> time.sleep(sloth * 3.552595)
    >>> mouse_down_and_sleep(h1, h1.root._1_1_mc, wait)
    >>> ## mouse_down_and_sleep(computer_h1, computer_h1.root._0_1_mc, wait)
    >>> h1.root.game_over_mc.score_mc.lobby_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 4.878348)
    >>> time.sleep(sloth * 9.047403)

    After going to lobby through unknown route,
    can no longer play on this board.
    >>> h1.root.gateway_mc.currentLabel
    'none'
    >>> mouse_down_and_sleep(h1, h1.root._1_0_mc, wait)
    >>> time.sleep(sloth * 16.874376)
    >>> h1.root.gateway_mc.currentLabel
    'what_message'
    >>> mouse_down_and_sleep(h1, h1.root._1_2_mc, wait)
    >>> h1.root.comment_mc.none_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 9.291532)
    >>> h1.pb()

    Does not see multiple plays
    ,*,
    *X*
    ,,O
    >>> h1.root.lobby_mc._00_mc.main_mc.dispatchEvent(mouseDown)
    '''

def jerry_captured_example():
    '''Jerry is in danger.  He passes.  Computer captures.  Jerry loses.
    TODO:  In this problem, Jerry cannot pass.  
    >>> h1, wait = setup_example(configuration, 
    ...     ('h1', 'hva1') )
    >>> sloth = 1.0 / h1._speed
    >>> h1.root.lobby_mc._00_mc.capture_rule_beside_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 2.580329)
    >>> time.sleep(sloth * 4.864116)
    >>> mouse_down_and_sleep(h1, h1.root.game_over_mc.start_mc, wait)
    >>> h1.root.game_over_mc.currentLabel
    'none'
    >>> import pdb; pdb.set_trace(); h1.root.pass_mc.dispatchEvent(mouseDown)
    >>> time.sleep(wait)

    TODO:  SGF prohibits Jerry from passing.  
        Currently update_path does not occur during pass.
    >>> h1.root.bad_move_mc.currentLabel
    'show'
    >>> h1.root.turn_mc.currentLabel
    'black'
    >>> time.sleep(sloth * 4.063175)
    >>> h1.root.pass_mc.dispatchEvent(mouseDown)
    >>> time.sleep(wait)
    >>> h1.root.bad_move_mc.currentLabel
    'show'
    >>> h1.root.turn_mc.currentLabel
    'black'

    If Jerry were allowed to pass, Jerry would lose, not win.  
    >>> h1.root.game_over_mc.currentLabel
    'lose'
    >>> ## mouse_down_and_sleep(computer_h1, computer_h1.root._3_2_mc, wait)
    >>> ## h1.root.game_over_mc.score_mc.lobby_mc.dispatchEvent(mouseDown)
    >>> ## time.sleep(sloth * 8.494042)
    '''


def alexander_play_and_leave_example():
    '''Alexander plays and leaves quickly.  
    He starts another and sees no artifact.
    TODO:  Python text client and ActionScript client differ.
    ActionScript may fail to clear news unless flushing.
    Python text client clears square before I expected.
    >>> h2, wait = setup_example(configuration, 
    ...     ('h2', 'hva2') )
    >>> sloth = 1.0 / h2._speed
    >>> configuration.instant = False
    >>> # example.log level 20 at Fri Sep 10 16:47:56 2010
    >>> h2.root.level_mc.none_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 3.925000)
    >>> h2.root.lobby_mc.main_mc._00_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 3.481000)
    >>> h2.root.lobby_mc._00_mc.capture_3_3_1_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 1.497000)
    >>> time.sleep(sloth * 2.477000)
    >>> mouse_down_and_sleep(h2, h2.root.game_over_mc.start_mc, wait)
    >>> time.sleep(sloth * 1.395000)
    >>> mouse_down_and_sleep(h2, h2.root._2_1_mc, wait)
    >>> ## mouse_down_and_sleep(computer_h2, computer_h2.root._1_2_mc, wait)
    >>> time.sleep(sloth * 2.877000)
    >>> h2.root._1_2_mc.currentLabel
    'white'
    >>> mouse_down_and_sleep(h2, h2.root._0_2_mc, wait)
    >>> h2.root.game_over_mc.score_mc.lobby_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 4.899000)
    >>> h2.root._1_2_mc.currentLabel
    'empty_black'
    >>> h2.root.lobby_mc._00_mc.capture_corner_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 2.372000)
    >>> h2.root._1_2_mc.currentLabel
    'empty_black'
    >>> h2.root.lobby_mc._00_mc.capture_corner_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 5.620000)
    >>> time.sleep(sloth * 4.162000)
    >>> mouse_down_and_sleep(h2, h2.root.game_over_mc.start_mc, wait)
    >>> time.sleep(sloth * 9.904000)
    >>> mouse_down_and_sleep(h2, h2.root._1_1_mc, wait)
    >>> ## mouse_down_and_sleep(computer_h2, computer_h2.root._0_1_mc, wait)
    >>> h2.root.menu_mc.toggle_mc.dispatchEvent(mouseDown)
    >>> ## time.sleep(sloth * 5.304000)
    >>> time.sleep(sloth * 0.304000)
    >>> h2.root._1_0_mc.square_mc.currentLabel
    'show'
    >>> for r in h2.ambassador.receives[-4:]:
    ...     s = r.get('sequence', [])
    ...     for i in s:
    ...         i.get('_1_0_mc')
    ...     
    {'square_mc': {'currentLabel': u'show'}}
    {'square_mc': {'currentLabel': u'none'}}
    >>> h2.root.menu_mc.lobby_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 1.148000)
    >>> import pdb; pdb.set_trace(); h2.root.lobby_mc._00_mc.capture_3_3_1_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 2.313000)
    >>> for r in h2.ambassador.receives[-4:]:
    ...     s = r.get('sequence', [])
    ...     for i in s:
    ...         i.get('_1_0_mc')
    ...     
    {'square_mc': {'currentLabel': u'show'}}
    {'square_mc': {'currentLabel': u'none'}}
    >>> for r in h2.ambassador.receives[-4:]:
    ...     r.get('_1_0_mc')
    ...     
    >>> h2.root._1_0_mc.square_mc.currentLabel
    'none'
    '''


def moonhyoung_kyung_place_example():
    '''
    >>> moonhyoung, kyung, wait = setup_example(configuration, 
    ...     ('moonhyoung', 'park'), ('kyung', 'min') )
    >>> sloth = 1.0 / moonhyoung._speed
    >>> moonhyoung.root.level_mc.none_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 2.482392)
    >>> ## time.sleep(sloth * 25.955897)
    >>> kyung.root.lobby_mc.main_mc.multiplayer_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 6.224653)
    >>> moonhyoung.root.lobby_mc.main_mc.multiplayer_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 1.850807)
    >>> moonhyoung.root.lobby_mc.create_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 2.437807)
    >>> kyung.root.level_mc.none_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 4.096513)
    >>> kyung.root.lobby_mc.join_mc.enter_btn.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 1.604990)
    >>> time.sleep(sloth * 5.424794)
    >>> time.sleep(sloth * 0.623080)
    >>> time.sleep(sloth * 0.637254)
    >>> time.sleep(sloth * 2.062640)
    >>> time.sleep(sloth * 1.287895)
    >>> mouse_down_and_sleep(moonhyoung, moonhyoung.root.game_over_mc.start_mc, wait)
    >>> time.sleep(sloth * 2.406435)
    >>> mouse_down_and_sleep(kyung, kyung.root._6_6_mc, wait)
    >>> time.sleep(sloth * 5.170625)
    >>> mouse_down_and_sleep(moonhyoung, moonhyoung.root._6_6_mc, wait)
    >>> time.sleep(sloth * 3.023289)
    >>> mouse_down_and_sleep(moonhyoung, moonhyoung.root._6_6_mc, wait)
    >>> time.sleep(sloth * 5.445471)
    >>> mouse_down_and_sleep(moonhyoung, moonhyoung.root._2_6_mc, wait)
    >>> time.sleep(sloth * 7.496330)
    >>> mouse_down_and_sleep(kyung, kyung.root._6_2_mc, wait)
    >>> time.sleep(sloth * 4.242559)
    >>> mouse_down_and_sleep(moonhyoung, moonhyoung.root._2_2_mc, wait)
    >>> time.sleep(sloth * 13.837487)
    >>> mouse_down_and_sleep(kyung, kyung.root._4_4_mc, wait)
    >>> time.sleep(sloth * 3.227910)
    >>> mouse_down_and_sleep(moonhyoung, moonhyoung.root._3_4_mc, wait)
    >>> time.sleep(sloth * 10.947873)
    >>> mouse_down_and_sleep(kyung, kyung.root._4_2_mc, wait)
    >>> time.sleep(sloth * 10.048317)
    >>> mouse_down_and_sleep(moonhyoung, moonhyoung.root._3_2_mc, wait)
    >>> time.sleep(sloth * 4.486604)
    >>> mouse_down_and_sleep(kyung, kyung.root._4_6_mc, wait)
    >>> time.sleep(sloth * 5.204278)
    >>> mouse_down_and_sleep(moonhyoung, moonhyoung.root._3_3_mc, wait)
    >>> time.sleep(sloth * 9.707822)
    >>> mouse_down_and_sleep(kyung, kyung.root._4_3_mc, wait)
    >>> time.sleep(sloth * 8.612230)
    >>> mouse_down_and_sleep(moonhyoung, moonhyoung.root._3_5_mc, wait)
    >>> time.sleep(sloth * 5.223554)
    >>> mouse_down_and_sleep(kyung, kyung.root._2_7_mc, wait)
    >>> time.sleep(sloth * 3.248965)
    >>> mouse_down_and_sleep(moonhyoung, moonhyoung.root._3_7_mc, wait)
    >>> time.sleep(sloth * 7.479854)
    >>> mouse_down_and_sleep(kyung, kyung.root._4_7_mc, wait)
    >>> time.sleep(sloth * 3.935718)
    >>> mouse_down_and_sleep(moonhyoung, moonhyoung.root._1_7_mc, wait)
    >>> time.sleep(sloth * 9.436277)
    >>> mouse_down_and_sleep(kyung, kyung.root._4_5_mc, wait)
    >>> time.sleep(sloth * 4.876057)
    >>> mouse_down_and_sleep(moonhyoung, moonhyoung.root._2_8_mc, wait)
    >>> time.sleep(sloth * 11.946369)
    >>> mouse_down_and_sleep(kyung, kyung.root._4_8_mc, wait)
    >>> time.sleep(sloth * 5.039558)
    >>> mouse_down_and_sleep(moonhyoung, moonhyoung.root._4_1_mc, wait)
    >>> time.sleep(sloth * 8.440662)
    >>> mouse_down_and_sleep(kyung, kyung.root._4_0_mc, wait)
    >>> time.sleep(sloth * 3.981304)
    >>> mouse_down_and_sleep(moonhyoung, moonhyoung.root._5_0_mc, wait)
    >>> time.sleep(sloth * 9.025687)
    >>> mouse_down_and_sleep(kyung, kyung.root._3_1_mc, wait)
    >>> time.sleep(sloth * 2.486248)
    >>> mouse_down_and_sleep(moonhyoung, moonhyoung.root._3_0_mc, wait)
    >>> time.sleep(sloth * 15.241723)
    >>> mouse_down_and_sleep(kyung, kyung.root._2_4_mc, wait)
    >>> time.sleep(sloth * 3.088140)
    >>> mouse_down_and_sleep(moonhyoung, moonhyoung.root._2_1_mc, wait)
    >>> time.sleep(sloth * 15.639636)
    >>> mouse_down_and_sleep(kyung, kyung.root._5_1_mc, wait)
    >>> time.sleep(sloth * 6.640774)
    >>> mouse_down_and_sleep(moonhyoung, moonhyoung.root._6_1_mc, wait)
    >>> time.sleep(sloth * 4.831145)
    >>> mouse_down_and_sleep(kyung, kyung.root._6_0_mc, wait)
    >>> time.sleep(sloth * 2.591647)
    >>> mouse_down_and_sleep(moonhyoung, moonhyoung.root._5_2_mc, wait)
    >>> time.sleep(sloth * 13.693374)
    >>> mouse_down_and_sleep(kyung, kyung.root._7_1_mc, wait)
    >>> time.sleep(sloth * 3.082806)
    >>> mouse_down_and_sleep(moonhyoung, moonhyoung.root._7_0_mc, wait)
    >>> time.sleep(sloth * 10.922873)
    >>> mouse_down_and_sleep(kyung, kyung.root._6_0_mc, wait)
    >>> time.sleep(sloth * 6.131557)
    >>> mouse_down_and_sleep(kyung, kyung.root._5_1_mc, wait)
    >>> time.sleep(sloth * 1.828217)
    >>> mouse_down_and_sleep(kyung, kyung.root._5_3_mc, wait)
    >>> time.sleep(sloth * 6.988866)
    >>> mouse_down_and_sleep(moonhyoung, moonhyoung.root._7_2_mc, wait)
    >>> time.sleep(sloth * 5.768541)
    >>> mouse_down_and_sleep(kyung, kyung.root._7_3_mc, wait)
    >>> time.sleep(sloth * 3.511194)
    >>> mouse_down_and_sleep(moonhyoung, moonhyoung.root._8_1_mc, wait)
    >>> time.sleep(sloth * 7.679022)
    >>> mouse_down_and_sleep(kyung, kyung.root._8_3_mc, wait)
    >>> time.sleep(sloth * 3.761703)
    >>> mouse_down_and_sleep(moonhyoung, moonhyoung.root._6_3_mc, wait)
    >>> time.sleep(sloth * 9.928191)
    >>> mouse_down_and_sleep(kyung, kyung.root._6_4_mc, wait)
    >>> time.sleep(sloth * 16.017269)
    >>> mouse_down_and_sleep(moonhyoung, moonhyoung.root._7_7_mc, wait)
    >>> time.sleep(sloth * 7.836972)
    >>> mouse_down_and_sleep(kyung, kyung.root._6_2_mc, wait)
    >>> kyung.root.chat_input_txt.text = "The point(row7, col3), It should be impossible to put my stone there but I could put my stone that place."
    >>> kyung.root.chat_input_mc.dispatchEvent(mouseDown)
    >>> ## time.sleep(sloth * 140.764861)
    >>> time.sleep(sloth * 9.573277)
    >>> mouse_down_and_sleep(moonhyoung, moonhyoung.root._6_3_mc, wait)
    >>> time.sleep(sloth * 2.728621)
    >>> mouse_down_and_sleep(moonhyoung, moonhyoung.root._6_3_mc, wait)
    >>> time.sleep(sloth * 1.311099)
    >>> mouse_down_and_sleep(moonhyoung, moonhyoung.root._6_3_mc, wait)
    >>> time.sleep(sloth * 0.608313)
    >>> mouse_down_and_sleep(moonhyoung, moonhyoung.root._6_3_mc, wait)
    >>> moonhyoung.root.pass_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 0.840913)
    >>> moonhyoung.root.pass_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 4.938898)
    >>> mouse_down_and_sleep(kyung, kyung.root._5_1_mc, wait)
    >>> time.sleep(sloth * 6.692884)
    >>> mouse_down_and_sleep(moonhyoung, moonhyoung.root._5_2_mc, wait)
    >>> time.sleep(sloth * 0.719328)
    >>> mouse_down_and_sleep(moonhyoung, moonhyoung.root._5_2_mc, wait)
    >>> time.sleep(sloth * 1.064357)
    >>> mouse_down_and_sleep(moonhyoung, moonhyoung.root._5_2_mc, wait)
    >>> moonhyoung.root.chat_input_txt.text = "Yes it's a bug, I can't put my stone the point surrounded by enemy's stones"
    >>> moonhyoung.root.chat_input_mc.dispatchEvent(mouseDown)
    >>> ## time.sleep(sloth * 48.952727)
    >>> time.sleep(wait)
    >>> moonhyoung.root.pass_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 7.685835)
    >>> moonhyoung.root.pass_mc.dispatchEvent(mouseDown)
    >>> kyung.root.pass_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 6.435419)
    >>> kyung.root.pass_mc.dispatchEvent(mouseDown)

    Kyung attacks on side.
    Moonhyoung creeps in.
    Kyung believes that after play elsewhere that ko capture-back is still forbidden.
    Although kyung received helpful animation, Moonhyoung won.
    TODO:  log create and join
    '''

def moonhyoung_kyung_help_example():
    '''Play on 5x5 board.
    TODO:  Log setup multiplayer 3x3, 5x5, 7x7, 9x9 board.
    ,,,,,
    ,,,,,
    ,,,,,
    ,*,,,
    ,,,,,
    >>> moonhyoung, kyung, wait = setup_example(configuration, 
    ...     ('moonhyoung', 'park'), ('kyung', 'min') )
    >>> sloth = 1.0 / moonhyoung._speed
    >>> moonhyoung.root.level_mc.none_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 2.517508)
    >>> moonhyoung.root.lobby_mc.create_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 1.901202)
    >>> kyung.root.lobby_mc.join_mc.enter_btn.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 1.901202)
    >>> time.sleep(sloth * 1.733119)
    >>> time.sleep(sloth * 3.443819)
    >>> time.sleep(sloth * 1.287610)
    >>> time.sleep(sloth * 1.599910)
    >>> time.sleep(sloth * 5.698109)
    >>> time.sleep(sloth * 0.638511)
    >>> time.sleep(sloth * 0.501129)
    >>> time.sleep(sloth * 2.371927)
    >>> mouse_down_and_sleep(moonhyoung, moonhyoung.root.game_over_mc.start_mc, wait)
    >>> time.sleep(sloth * 4.583203)
    >>> mouse_down_and_sleep(kyung, kyung.root._3_1_mc, wait)
    >>> time.sleep(sloth * 3.010039)
    >>> mouse_down_and_sleep(moonhyoung, moonhyoung.root._2_2_mc, wait)
    >>> time.sleep(sloth * 22.199173)
    >>> mouse_down_and_sleep(kyung, kyung.root._3_3_mc, wait)
    >>> time.sleep(sloth * 11.041607)
    >>> mouse_down_and_sleep(moonhyoung, moonhyoung.root._2_1_mc, wait)
    >>> time.sleep(sloth * 10.591410)
    >>> mouse_down_and_sleep(kyung, kyung.root._1_1_mc, wait)
    >>> time.sleep(sloth * 5.215296)
    >>> mouse_down_and_sleep(moonhyoung, moonhyoung.root._3_2_mc, wait)
    >>> time.sleep(sloth * 6.544034)
    >>> mouse_down_and_sleep(kyung, kyung.root._4_1_mc, wait)
    >>> time.sleep(sloth * 4.073097)
    >>> mouse_down_and_sleep(moonhyoung, moonhyoung.root._3_0_mc, wait)
    >>> time.sleep(sloth * 9.791677)
    >>> mouse_down_and_sleep(kyung, kyung.root._2_0_mc, wait)
    >>> time.sleep(sloth * 1.647456)
    >>> mouse_down_and_sleep(moonhyoung, moonhyoung.root._1_0_mc, wait)
    >>> time.sleep(sloth * 22.126960)
    >>> mouse_down_and_sleep(kyung, kyung.root._2_3_mc, wait)
    >>> time.sleep(sloth * 3.977058)
    >>> mouse_down_and_sleep(moonhyoung, moonhyoung.root._4_2_mc, wait)
    >>> time.sleep(sloth * 11.334003)
    >>> mouse_down_and_sleep(kyung, kyung.root._4_3_mc, wait)
    >>> time.sleep(sloth * 7.043293)
    >>> mouse_down_and_sleep(moonhyoung, moonhyoung.root._4_0_mc, wait)
    >>> time.sleep(sloth * 13.884236)
    >>> mouse_down_and_sleep(kyung, kyung.root._1_2_mc, wait)
    >>> time.sleep(sloth * 17.507329)
    >>> mouse_down_and_sleep(moonhyoung, moonhyoung.root._1_3_mc, wait)
    >>> time.sleep(sloth * 11.013661)
    >>> mouse_down_and_sleep(kyung, kyung.root._0_3_mc, wait)
    >>> moonhyoung.root.chat_input_txt.text = "I want to see helpers... Why do you show helper only in pipe's screen?"
    >>> moonhyoung.root.chat_input_mc.dispatchEvent(mouseDown)
    >>> ## time.sleep(sloth * 37.866612)
    >>> time.sleep(sloth * 5.240568)
    >>> mouse_down_and_sleep(moonhyoung, moonhyoung.root._1_4_mc, wait)
    >>> time.sleep(sloth * 8.618926)
    >>> mouse_down_and_sleep(kyung, kyung.root._2_4_mc, wait)
    >>> time.sleep(sloth * 5.380266)
    >>> mouse_down_and_sleep(moonhyoung, moonhyoung.root._0_2_mc, wait)
    >>> time.sleep(sloth * 15.602628)
    >>> mouse_down_and_sleep(kyung, kyung.root._0_4_mc, wait)
    >>> moonhyoung.root.pass_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 7.418854)
    >>> moonhyoung.root.pass_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 16.164037)
    >>> mouse_down_and_sleep(kyung, kyung.root._0_0_mc, wait)
    >>> moonhyoung.root.pass_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 8.747863)
    >>> moonhyoung.root.pass_mc.dispatchEvent(mouseDown)
    >>> kyung.root.pass_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 3.255260)
    >>> kyung.root.pass_mc.dispatchEvent(mouseDown)
    '''
    
import code_unit
if __name__ == '__main__':
    from optparse import OptionParser
    parser = OptionParser()
    parser.add_option("--unit", default="",
        dest="unit", help="unit to doctest [default: %default]")
    parser.add_option('-v', '--verbose', dest='verbose', default='warning',
                    help="Increase verbosity")
    (options, args) = parser.parse_args()
    log_level = logging_levels[options.verbose]
    logging.basicConfig(level=log_level)
    if options.unit:
        unit = eval(options.unit)
        code_unit.doctest_unit(unit)
    else:
        units = globals().values()
        ## units.remove(setup_example)
        code_unit.doctest_units(units)

