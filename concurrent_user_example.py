#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Playtests of 9x9 Crazy Cake
'''
__author__ = 'Ethan Kennerly'
from client import *

def concurrent_single_player_example():
    '''Yuji and Jade try to play single-player at the same time.
    >>> code_unit.inline_examples(
    ...     lukasz_begin_example.__doc__, 
    ...     locals(), globals(), 
    ...     verify_examples = False)
    >>> yuji = black
    >>> joris = configuration.globe_class()
    >>> jade = joris
    >>> jade.setup(1, configuration.setup_client)
    >>> set_property(jade, jade.root.title_mc.username_txt, 'text', 'joris')
    >>> set_property(jade, jade.root.title_mc.password_txt, 'text', 'j')
    >>> mouse_down_and_sleep(jade, jade.root.title_mc.start_btn, wait)
    >>> mouse_down_and_sleep(yuji, yuji.root.lobby_mc._00_mc.capture_3_3_mc,
    ...     wait)
    >>> mouse_down_and_sleep(yuji, yuji.root.game_over_mc.start_mc, wait)
    >>> mouse_down_and_sleep(yuji, yuji.root._1_1_mc, wait)
    >>> mouse_down_and_sleep(yuji, yuji.root._1_1_mc, wait)
    >>> mouse_down_and_sleep(jade, jade.root.lobby_mc._00_mc.dominate_3_3_mc,
    ...     wait)
    >>> mouse_down_and_sleep(jade, jade.root.game_over_mc.start_mc, wait)
    >>> mouse_down_and_sleep(jade, jade.root._1_1_mc, wait)
    >>> mouse_down_and_sleep(jade, jade.root._1_1_mc, wait)
    >>> mouse_down_and_sleep(jade, jade.root._2_1_mc, wait)
    >>> mouse_down_and_sleep(jade, jade.root._2_1_mc, wait)
    >>> mouse_down_and_sleep(yuji, yuji.root._2_1_mc, wait)
    >>> mouse_down_and_sleep(yuji, yuji.root._2_1_mc, wait)
    '''


