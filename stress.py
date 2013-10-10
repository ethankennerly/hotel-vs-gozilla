#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Real-time and echo stress tests of network in Crazy Cake.
'''
__author__ = 'Ethan Kennerly'

from client import *

# Real-time

# from decorator import decorator
# @decorator
# XXX decorator stomps docstring?
def digest_and(do, *args, **kwargs):
    '''Force eat to complete, wait a second, then do.
    >>> gateway_process = configuration.subprocess_gateway(configuration.amf_host, 'embassy.py', verbose)
    >>> joris = configuration.globe_class()
    >>> joris.setup(configuration.mock_speed, configuration.setup_client)
    >>> time.sleep(1.0 / joris._speed)
    >>> mouse_down_and_sleep = digest_and(mouse_down_and_sleep)
    >>> mouse_down_and_sleep(joris, joris.root.title_mc.start_btn, 1.0 / joris._speed)
    '''
    def digest_and_do(*args, **kwargs):
        globe = args[0]
        set_property(globe, globe.root.eat_mc.act_mc, 'currentLabel', 'none')
        time.sleep(1.0 / globe._speed)
        diff = property_diff(globe, globe.root.eat_mc.act_mc, 'currentLabel', 'none')
        if diff:
            return diff
        else:
            return do(*args, **kwargs)
    return digest_and_do

def real_time_example():
    '''
    ethan and joris start
    >>> code_unit.inline_examples(
    ...     ethan_joris_start_example.__doc__, 
    ...     locals(), globals(), 
    ...     verify_examples = False)
    
    by default, turns are required.
    ethan may not move.
    white, 0, 0
    >>> mouse_down_and_sleep(ethan, ethan.root._0_0_mc, 1.0 / ethan._speed)
    >>> board_diff(ethan, ethan.root._0_0_mc, 'currentLabel', 'empty_white')
    
    joris moves.
    black, 0, 1
    Soon, Joris previews a black stone appear there.
    >>> mouse_down_and_sleep(joris, joris.root._0_1_mc, 1.0 / joris._speed)
    >>> board_diff(joris, joris.root._0_1_mc, 'currentLabel', 'question_black')
    >>> mouse_down_and_sleep(joris, joris.root._0_1_mc, 1.0 / joris._speed)
    >>> board_diff(joris, joris.root._0_1_mc, 'currentLabel', 'black')
    
    joris may not move again.
    >>> mouse_down_and_sleep(joris, joris.root._1_0_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._1_0_mc, 1.0 / joris._speed)
    >>> board_diff(joris, joris.root._1_0_mc, 'currentLabel', 'empty_black')
    
    ethan moves.
    white, 0, 0
    >>> mouse_down_and_sleep(ethan, ethan.root._0_0_mc, 1.0 / ethan._speed)
    >>> board_diff(ethan, ethan.root._0_0_mc, 'currentLabel', 'white')
    
    ethan may not move again.
    >>> mouse_down_and_sleep(ethan, ethan.root._0_2_mc, 1.0 / ethan._speed)
    >>> board_diff(ethan, ethan.root._0_2_mc, 'currentLabel', 'empty_white')
    >>> joris.pb()
    OX,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    
    REAL-TIME
    ethan clicks clock button.
    >>> mouse_down_and_sleep(ethan, ethan.root.clock_mc.enter_mc.enter_btn, 1.0 / ethan._speed)
    
    joris and ethan see a clock between them.
    >>> property_diff(joris, joris.root.clock_mc, 'currentLabel', 'time')
    >>> property_diff(ethan, ethan.root.clock_mc, 'currentLabel', 'time')
    
    each player sees that it is their turn.
    >>> property_diff(joris, joris.root.turn_mc, 'currentLabel', 'black')
    >>> property_diff(ethan, ethan.root.turn_mc, 'currentLabel', 'white')
    
    joris previews.
    >>> mouse_down_and_sleep(joris, joris.root._1_0_mc, 1.0 / joris._speed)
    >>> if not joris.ambassador.sends[-1].get('eat_mc').get('act_mc').get('currentLabel') == 'none':
    ...     joris.ambassador.sends[-1].get('eat_mc')
    >>> board_diff(ethan, ethan.root._1_0_mc, 'currentLabel', 'empty_white')
    >>> board_diff(joris, joris.root._1_0_mc, 'currentLabel', 'question_black')
    
    ethan moves again.
    >>> property_diff(ethan, ethan.root.eat_mc.act_mc, 'currentLabel', 'none')
    >>> mouse_down_and_sleep(ethan, ethan.root._0_2_mc, 3.0 / ethan._speed)
    >>> property_diff(joris, joris.root.turn_mc, 'currentLabel', 'black')
    >>> property_diff(ethan, ethan.root.turn_mc, 'currentLabel', 'white')
    >>> board_diff(ethan, ethan.root._0_2_mc, 'currentLabel', 'white')
    >>> board_diff(joris, joris.root._0_2_mc, 'currentLabel', 'white')
    
    ethan's move reverts joris' preview of a capture and shows white's new move.
    >>> board_diff(ethan, ethan.root._1_0_mc, 'currentLabel', 'empty_white')
    >>> board_diff(joris, joris.root._1_0_mc, 'currentLabel', 'empty_black')
    >>> board_diff(joris, joris.root._0_0_mc, 'currentLabel', 'white')
    >>> board_diff(joris, joris.root._0_2_mc, 'currentLabel', 'white')
    
    during this time, ethan starts eating, (which in flash lasts for 30 seconds)
    While eating, he cannot move again.
    because client may become corrupt, 
    relying on client for eat animation state is insecure and unfaithful.
    >>> mouse_down_and_sleep(ethan, ethan.root._0_3_mc, 3.0 / ethan._speed)
    >>> board_diff(ethan, ethan.root._0_3_mc, 'currentLabel', 'empty_white')
    >>> board_diff(joris, joris.root._0_3_mc, 'currentLabel', 'empty_black')
    >>> property_diff(ethan, ethan.root.eat_mc.act_mc, 'currentLabel', 'eat')
    >>> property_diff(ethan, ethan.root.help_mc, 'currentLabel', 'eat')
    >>> property_diff(ethan, ethan.root.eat_mc, 'x', ethan.root._0_2_mc.x)
    
    joris previews
    >>> mouse_down_and_sleep(joris, joris.root._6_2_mc, 1.0 / joris._speed)
    
    ethan tries to move.
    >>> property_diff(ethan, ethan.root.eat_mc.act_mc, 'currentLabel', 'eat')
    >>> mouse_down_and_sleep(ethan, ethan.root._0_3_mc, 5.0 / ethan._speed)
    >>> board_diff(ethan, ethan.root._0_3_mc, 'currentLabel', 'empty_white')
    
    in flash, eating expires after about 30 seconds.
    joris moves.  ethan finishes eating.
    only when eat has stopped, is news of eat sent.  joris gets extra stone.
    >>> mouse_down_and_sleep(joris, joris.root._6_2_mc, 1.0 / joris._speed)
    >>> print 'hack to give time to update'; time.sleep(1.0/joris._speed)
    >>> if not joris.ambassador.sends[-1].get('eat_mc').get('act_mc').get('currentLabel') == 'none':
    ...     joris.ambassador.sends[-1].get('eat_mc')
    >>> property_diff(joris, joris.root.eat_mc.act_mc, 'currentLabel', 'eat')
    >>> property_diff(joris, joris.root.turn_mc, 'currentLabel', 'black')
    >>> property_diff(ethan, ethan.root.turn_mc, 'currentLabel', 'white')
    >>> board_diff(joris, joris.root._6_2_mc, 'currentLabel', 'black')
    >>> board_diff(ethan, ethan.root._6_2_mc, 'currentLabel', 'black')
    >>> property_diff(joris, joris.root.extra_stone_gift_mc, 'currentLabel', '_1')
    
    	!^_^	if both are eating, then the player who started eating first can play.  
    !^_^    this is equivalent to:  whenever partner moves, you finish eating.
    >>> property_diff(ethan, ethan.root.eat_mc.act_mc, 'currentLabel', 'none')
    
    joris previews.
    30 seconds passes.  ethan decides not to move.
    only when eat has stopped, is news of eat sent.
    black has moved.
    black is eating.
    black previews.
    black sees eating expire.
    >>> mouse_down_and_sleep(joris, joris.root._2_0_mc, 1.0 / joris._speed)
    >>> time.sleep(30.0 / joris._speed / 32.0)
    >>> joris.ambassador.sends[-1].get('eat_mc')
    >>> set_property(joris, joris.root.eat_mc.act_mc, 'currentLabel', 'none')
    >>> property_diff(joris, joris.root.eat_mc.act_mc, 'currentLabel', 'none')
    
    white moves.
    black sees white moved.
    in pdb, I detected no inconsistency, here:
    >>> mouse_down_and_sleep(ethan, ethan.root._0_3_mc, 1.0 / ethan._speed)
    >>> property_diff(joris, joris.root.turn_mc, 'currentLabel', 'black')
    >>> property_diff(ethan, ethan.root.turn_mc, 'currentLabel', 'white')
    >>> board_diff(ethan, ethan.root._0_3_mc, 'currentLabel', 'white')
    >>> board_diff(joris, joris.root._0_3_mc, 'currentLabel', 'white')
    
    black sees eating remains expired.
    black moves and eating starts at new move.  black gets a hide gift.
    >>> property_diff(joris, joris.root.eat_mc.act_mc, 'currentLabel', 'none')
    >>> mouse_down_and_sleep(joris, joris.root._6_6_mc, 1.0 / joris._speed)
    >>> board_diff(joris, joris.root._6_6_mc, 'currentLabel', 'question_black')
    >>> mouse_down_and_sleep(joris, joris.root._6_6_mc, 1.0 / joris._speed)
    >>> property_diff(joris, joris.root.turn_mc, 'currentLabel', 'black')
    >>> property_diff(ethan, ethan.root.turn_mc, 'currentLabel', 'white')
    >>> joris.ambassador.sends[-1].get('eat_mc').get('act_mc').get('currentLabel')
    'none'
    >>> board_diff(joris, joris.root._6_6_mc, 'currentLabel', 'black')
    >>> board_diff(ethan, ethan.root._6_6_mc, 'currentLabel', 'black')
    >>> property_diff(joris, joris.root.eat_mc, 'x', joris.root._6_6_mc.x)
    >>> property_diff(joris, joris.root.eat_mc, 'y', joris.root._6_6_mc.y)
    >>> property_diff(joris, joris.root.eat_mc.act_mc, 'currentLabel', 'eat')
    >>> property_diff(joris, joris.root.extra_stone_gift_mc, 'currentLabel', '_1')
    >>> property_diff(joris, joris.root.hide_gift_mc, 'currentLabel', '_1')
    
    Because joris moved and now both players are waiting, ethan finishes eating.
    >>> property_diff(ethan, ethan.root.eat_mc.act_mc, 'currentLabel', 'none')
    
    ethan moves.
    >>> ## mouse_down_and_sleep(ethan, ethan.root._0_4_mc, 1.0 / ethan._speed)
    >>> ## set_property(ethan, ethan.root.eat_mc.act_mc, 'currentLabel', 'none')
    >>> mouse_down_and_sleep(ethan, ethan.root._0_4_mc, 1.0 / ethan._speed)
    >>> property_diff(joris, joris.root.turn_mc, 'currentLabel', 'black')
    >>> property_diff(ethan, ethan.root.turn_mc, 'currentLabel', 'white')
    >>> board_diff(ethan, ethan.root._0_4_mc, 'currentLabel', 'white')
    >>> board_diff(joris, joris.root._0_4_mc, 'currentLabel', 'white')
    >>> property_diff(ethan, ethan.root.eat_mc.act_mc, 'currentLabel', 'eat')
    
    Joris could eat immediately.
    >>> property_diff(joris, joris.root.eat_mc.act_mc, 'currentLabel', 'none')
    
    30 seconds passes.  ethan moves.
    >>> time.sleep(30.0 / joris._speed / 32.0)
    >>> set_property(ethan, ethan.root.eat_mc.act_mc, 'currentLabel', 'none')
    >>> mouse_down_and_sleep(ethan, ethan.root._0_5_mc, 1.0 / ethan._speed)
    >>> board_diff(ethan, ethan.root._0_5_mc, 'currentLabel', 'white')
    >>> board_diff(joris, joris.root._0_5_mc, 'currentLabel', 'white')
    >>> joris.pb()
    OXOOOO,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,X,,,X,,
    ,,,,,,,,,
    ,,,,,,,,,
    >>> ethan.pb()
    OXOOOO,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,X,,,X,,
    ,,,,,,,,,
    ,,,,,,,,,
    
    click two cake.  see two cake on cursor.  eating.  click to take.  see 'still eating'.  eating expires.  
    >>> ## property_diff(joris, joris.root.eat_mc.act_mc, 'currentLabel', 'eat')
    >>> mouse_down_and_sleep(joris, joris.root.extra_stone_gift_mc.use_mc, 1.0 / joris._speed)
    >>> property_diff(joris, joris.root.cursor_mc.extra_stone_mc, 'currentLabel', '_1')
    >>> ## property_diff(joris, joris.root.eat_mc.act_mc, 'currentLabel', 'eat')
    >>> ## mouse_down_and_sleep(joris, joris.root._3_0_mc, 1.0 / joris._speed)
    >>> ## mouse_down_and_sleep(joris, joris.root._3_0_mc, 1.0 / joris._speed)
    >>> ## board_diff(joris, joris.root._3_0_mc, 'currentLabel', 'empty_black')
    >>> ## property_diff(joris, joris.root.cursor_mc.extra_stone_mc, 'currentLabel', '_1')
    >>> ## set_property(joris, joris.root.eat_mc.act_mc, 'currentLabel', 'none')
    
    take.  do not see eating.  try to take again.  take.
    >>> mouse_down_and_sleep(joris, joris.root._3_0_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._3_0_mc, 1.0 / joris._speed)
    >>> board_diff(joris, joris.root._3_0_mc, 'currentLabel', 'black')
    >>> board_diff(ethan, ethan.root._3_0_mc, 'currentLabel', 'black')
    >>> property_diff(joris, joris.root.eat_mc.act_mc, 'currentLabel', 'none')
    >>> mouse_down_and_sleep(joris, joris.root._4_0_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._4_0_mc, 1.0 / joris._speed)
    >>> board_diff(joris, joris.root._4_0_mc, 'currentLabel', 'black')
    >>> board_diff(ethan, ethan.root._4_0_mc, 'currentLabel', 'black')
    >>> property_diff(joris, joris.root.eat_mc.act_mc, 'currentLabel', 'eat')
    >>> property_diff(joris, joris.root.eat_mc, 'x', joris.root._4_0_mc.x)
    >>> property_diff(joris, joris.root.eat_mc, 'y', joris.root._4_0_mc.y)
    
    !^_^    black is done eating.  black hides.  
    >>> set_property(joris, joris.root.eat_mc.act_mc, 'currentLabel', 'none')
    >>> property_diff(joris, joris.root.cursor_mc, 'currentLabel', 'black')
    >>> mouse_down_and_sleep(joris, joris.root.hide_gift_mc.use_mc, 1.0 / joris._speed)
    >>> property_diff(joris, joris.root.cursor_mc, 'currentLabel', 'hide_black')
    >>> mouse_down_and_sleep(joris, joris.root._6_4_mc, 1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._6_4_mc, 1.0 / joris._speed)
    >>> board_diff(joris, joris.root._6_4_mc, 'currentLabel', 'hide_black')
    >>> board_diff(ethan, ethan.root._6_4_mc, 'currentLabel', 'empty_white')
     
    After hiding, joris' cursor reverts.
    >>> property_diff(joris, joris.root.cursor_mc, 'currentLabel', 'black')
     
    after white moves, white is eating.  white clicks black hidden.  
    white sees that he is still eating and does not see the hidden black.
    >>> mouse_down_and_sleep(ethan, ethan.root._4_4_mc, 1.0 / ethan._speed)
    >>> property_diff(ethan, ethan.root.eat_mc.act_mc, 'currentLabel', 'eat')
    >>> mouse_down_and_sleep(ethan, ethan.root._6_4_mc, 1.0 / ethan._speed)
    >>> property_diff(ethan, ethan.root.help_mc, 'currentLabel', 'eat')
    >>> board_diff(ethan, ethan.root._6_4_mc, 'currentLabel', 'empty_white')
    >>> board_diff(joris, joris.root._6_4_mc, 'currentLabel', 'hide_black')
    >>> property_diff(ethan, ethan.root.eat_mc.act_mc, 'currentLabel', 'eat')
    >>> property_diff(ethan, ethan.root.eat_mc, 'x', ethan.root._4_4_mc.x)
    >>> property_diff(ethan, ethan.root.eat_mc, 'y', ethan.root._4_4_mc.y)
    '''

def iterate_stress(ethan, joris, delay, r, i, 
        mouse_down_and_sleep, set_property):
    set_property(joris, joris.root.eat_mc.act_mc, 'currentLabel', 'none')
    time.sleep(delay)
    set_property(ethan, ethan.root.eat_mc.act_mc, 'currentLabel', 'none')
    time.sleep(delay)
    joris_intersection_mc = joris.intersection_mc_array[r][i]
    ethan_intersection_mc = ethan.intersection_mc_array[8-r][8-i]
    mouse_down_and_sleep(joris, joris_intersection_mc, delay )
    mouse_down_and_sleep(joris, joris_intersection_mc, delay )
    mouse_down_and_sleep(ethan, ethan_intersection_mc, delay )
    # joris.pb()
    # ethan.pb()

def real_time_stress_example():
    '''
    ethan and joris start
    >>> code_unit.inline_examples(
    ...     ethan_joris_start_example.__doc__, 
    ...     locals(), globals(), 
    ...     verify_examples = False)
    
    by default, turns are required.
    joris moves.
    black, 4, 4
    Soon, Joris previews a black stone appear there.
    >>> mouse_down_and_sleep(joris, joris.root._4_4_mc, 1.0 / joris._speed)
    >>> board_diff(joris, joris.root._4_4_mc, 'currentLabel', 'question_black')
    >>> mouse_down_and_sleep(joris, joris.root._4_4_mc, 1.0 / joris._speed)
    >>> board_diff(joris, joris.root._4_4_mc, 'currentLabel', 'black')
    
    XXX must be ethan's turn to start clock.
    ethan clicks clock button.
    >>> mouse_down_and_sleep(ethan, ethan.root.clock_mc.enter_mc.enter_btn, 1.0 / ethan._speed)
    
    joris and ethan see a clock between them.
    >>> property_diff(joris, joris.root.clock_mc, 'currentLabel', 'time')
    >>> property_diff(ethan, ethan.root.clock_mc, 'currentLabel', 'time')
    
    each player sees that it is their turn.
    >>> property_diff(joris, joris.root.turn_mc, 'currentLabel', 'black')
    >>> property_diff(ethan, ethan.root.turn_mc, 'currentLabel', 'white')
    
    joris and ethan fill the board, nearly simultaneously from opposite corners
    joris previews.
    >>> ## delay = 1.0 / joris._speed; columns = 3 # pass
    >>> ## delay = 1.0 / joris._speed; columns = 9 # pass mock, client, flash
    
    fail half mock, client; with complaint of 'help_mc:eat'
    flash server and master receives all; slave receives none or last only.
    >>> delay = 1.0 / 2 / joris._speed; columns = 9 
    
    >>> ## delay = 1.0 / 4 / joris._speed; columns = 9 # fail half
    >>> logging.info('delay = %s; columns = %s' % (delay, columns))
     
    >>> r = 0
    >>> for c in range(columns):
    ...         iterate_stress(ethan, joris, delay, r, c, mouse_down_and_sleep, set_property)
    >>>
    >>> time.sleep(delay)
    >>> time.sleep(delay)
    >>> joris.pb()
    XXXXXXXXX
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,X,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    OOOOOOOOO
    >>> ethan.pb()
    XXXXXXXXX
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,X,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    OOOOOOOOO
    '''



# Echo to stress network

def echo(globe, news):
    '''Echo by sending back same.
    >>> gateway_process = configuration.subprocess_gateway(configuration.amf_host, 'embassy.py', verbose)

    XXX if more than one line indented, IndentationError 
    >>> if 'ethan' in globals() or 'ethan' in locals():
    ...    mouse_down_and_sleep(ethan, ethan.root.lobby_mc.enter_mc, 1.0 / ethan._speed)
    >>> if 'ethan' not in globals() and 'ethan' not in locals():
    ...     ethan = globe_class(); ethan.setup(configuration.mock_speed, configuration.setup_client)

    >>> set_property(ethan, ethan.root.title_mc.username_txt, 'text', 'ethan')
    >>> time.sleep(1.0 / ethan._speed)
    >>> set_property(ethan, ethan.root.title_mc.password_txt, 'text', 'kennerly')
    >>> time.sleep(1.0 / ethan._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root.title_mc.start_btn, 1.0 / ethan._speed)
    >>> set_property(ethan, ethan.root.gateway_mc.ready_time_txt, 'text', 'echo')

    Need a second to go into echo mode.
    >>> mouse_down_and_sleep(ethan, ethan.root.title_mc.start_btn, 1.0 / ethan._speed)
    >>> set_property(ethan, ethan.root, 'currentLabel', 'table')
    >>> time.sleep(1.0 / ethan._speed)

    pass flash
    >>> columns = 9

    Log does not copy.  Large news at full screen.  04/09/2010 Fri 11:01
    Copy tests that slave receives messages from master.  Slave will not return or echo.  Copy large test passes.  04/09/2010 Fri 15:15
    have slave mouse down, or just mark on the slave if slave is an echo.
    >>> ## inject = slave_log_large_news
    >>> inject = slave_copy
    >>> ## inject = slave_copy_large_news
    >>> ## inject = mouse_down_and_sleep
    >>> ## inject = slave_echo_once
    >>> print inject
    >>> echo_many(inject, ethan, 1.0 / 8,       0, columns)
   
    flash receives most,
    >>> echo_many(inject, ethan, 1.0 /16,       1, columns)
    
    fail one in mock and python client
    >>> echo_many(inject, ethan, 1.0 /32,       2, columns)
    >>> echo_many(inject, ethan, 1.0 /64,       3, columns)
    >>> time.sleep(1.0/4)
    >>> ethan.pb()
    $$$$$$$$$
    $$$$$$$$$
    $$$$$$$$$
    $$$$$$$$$
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,

    Now ask server to echo large news
    >>> set_property(ethan, ethan.root.gateway_mc.ready_time_txt, 'text', 'echo_large')
    >>> time.sleep(1.0 / ethan._speed)
    >>> set_property(ethan, ethan.root.title_mc.username_txt, 'text', 'ethan')
    >>> time.sleep(1.0 / ethan._speed)
    >>> set_property(ethan, ethan.root.title_mc.password_txt, 'text', 'kennerly')
    >>> time.sleep(1.0 / ethan._speed)

    Need a second to go into echo mode.
    >>> mouse_down_and_sleep(ethan, ethan.root.title_mc.start_btn, 1.0 / ethan._speed)
    >>> set_property(ethan, ethan.root, 'currentLabel', 'table')
    >>> time.sleep(1.0 / ethan._speed)

    pass mock and flash, except flash master does not get the board back.
    >>> echo_many(inject, ethan, 1.0/ 4,  5, columns)
    >>> echo_many(inject, ethan, 1.0/ 8,  6, columns)

    in flash, most but not all receive
    >>> echo_many(inject, ethan, 1.0/16,  7, columns)
    >>> echo_many(inject, ethan, 1.0/32,  8, columns)
    >>> time.sleep(1.0/4)
    >>> ethan.pb()
    $$$$$$$$$
    $$$$$$$$$
    $$$$$$$$$
    $$$$$$$$$
    ,,,,,,,,,
    $$$$$$$$$
    $$$$$$$$$
    $$$$$$$$$
    $$$$$$$$$
    '''
    globe.log_news('echo', news)
    # logging.info('echo: %s' % news)
    globe.publish(news)



def echo_many(mouse_down_and_sleep, globe, delay, r, columns):
    logging.info('echo_many delay = %s; r = %s; columns = %s' % (delay, r, columns))
    for c in range(columns):
        mouse_down_and_sleep(globe, globe.intersection_mc_array[r][c], delay)


def echo_test(ethan):
    '''Repeat echo several times.  Watch for failure.
    >>> gateway_process = configuration.subprocess_gateway(configuration.amf_host, 'embassy.py', verbose)
    >>> ethan = configuration.globe_class()
    >>> ethan.setup(configuration.mock_speed, configuration.setup_client)
    >>> set_property(ethan, ethan.root.title_mc.username_txt, 'text', 'ethan')
    >>> time.sleep(1.0 / ethan._speed)
    >>> set_property(ethan, ethan.root.title_mc.password_txt, 'text', 'kennerly')
    >>> time.sleep(1.0 / ethan._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root.title_mc.start_btn, 1.0 / ethan._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root.lobby_mc.enter_mc, 1.0 / ethan._speed)
    >>> echo_test(ethan)
    >>> mouse_down_and_sleep(ethan, ethan.root.lobby_mc.enter_mc, 1.0 / ethan._speed)
    >>> echo_test(ethan)
    >>> mouse_down_and_sleep(ethan, ethan.root.lobby_mc.enter_mc, 1.0 / ethan._speed)
    >>> echo_test(ethan)
    >>> mouse_down_and_sleep(ethan, ethan.root.lobby_mc.enter_mc, 1.0 / ethan._speed)
    >>> echo_test(ethan)
    >>> mouse_down_and_sleep(ethan, ethan.root.lobby_mc.enter_mc, 1.0 / ethan._speed)
    >>> echo_test(ethan)
    >>> mouse_down_and_sleep(ethan, ethan.root.lobby_mc.enter_mc, 1.0 / ethan._speed)
    >>> echo_test(ethan)
    >>> mouse_down_and_sleep(ethan, ethan.root.lobby_mc.enter_mc, 1.0 / ethan._speed)
    >>> echo_test(ethan)
    >>> mouse_down_and_sleep(ethan, ethan.root.lobby_mc.enter_mc, 1.0 / ethan._speed)
    >>> echo_test(ethan)
    >>> mouse_down_and_sleep(ethan, ethan.root.lobby_mc.enter_mc, 1.0 / ethan._speed)
    >>> echo_test(ethan)
    >>> mouse_down_and_sleep(ethan, ethan.root.lobby_mc.enter_mc, 1.0 / ethan._speed)
    >>> echo_test(ethan)
    '''
    ## script = doctest.script_from_examples(echo.__doc__)
    ## trim setup
    # Echo by sending back same.
    #
    set_property(ethan, ethan.root.title_mc.username_txt, 'text', 'ethan')
    time.sleep(1.0 / ethan._speed)
    set_property(ethan, ethan.root.title_mc.password_txt, 'text', 'kennerly')
    time.sleep(1.0 / ethan._speed)
    mouse_down_and_sleep(ethan, ethan.root.title_mc.start_btn, 1.0 / ethan._speed)
    mouse_down_and_sleep(ethan, ethan.root.lobby_mc.enter_mc, 1.0 / ethan._speed)
    set_property(ethan, ethan.root.gateway_mc.ready_time_txt, 'text', 'echo')
    #
    #     Need a second to go into echo mode.
    mouse_down_and_sleep(ethan, ethan.root.title_mc.start_btn, 1.0 / ethan._speed)
    set_property(ethan, ethan.root, 'currentLabel', 'table')
    time.sleep(1.0 / ethan._speed)
    #
    #     pass flash
    columns = 9
    #
    #     Log does not copy.  Large news at full screen.  04/09/2010 Fri 11:01
    #     Copy tests that slave receives messages from master.  Slave will not return or echo.  Copy large test passes.  04/09/2010 Fri 15:15
    #     have slave mouse down, or just mark on the slave if slave is an echo.
    inject = slave_copy
    print inject
    echo_many(inject, ethan, 1.0 / 8,       0, columns)
    #
    #     flash receives most,
    echo_many(inject, ethan, 1.0 /16,       1, columns)
    #
    #     fail one in mock and python client
    echo_many(inject, ethan, 1.0 /32,       2, columns)
    echo_many(inject, ethan, 1.0 /64,       3, columns)
    time.sleep(1.0/4)
    ethan.pb()
    # Expected:
    ## $$$$$$$$$
    ## $$$$$$$$$
    ## $$$$$$$$$
    ## $$$$$$$$$
    ## ,,,,,,,,,
    ## ,,,,,,,,,
    ## ,,,,,,,,,
    ## ,,,,,,,,,
    ## ,,,,,,,,,
    #
    #     Now ask server to echo large news
    set_property(ethan, ethan.root.gateway_mc.ready_time_txt, 'text', 'echo_large')
    time.sleep(1.0 / ethan._speed)
    set_property(ethan, ethan.root.title_mc.username_txt, 'text', 'ethan')
    time.sleep(1.0 / ethan._speed)
    set_property(ethan, ethan.root.title_mc.password_txt, 'text', 'kennerly')
    time.sleep(1.0 / ethan._speed)
    #
    #     Need a second to go into echo mode.
    mouse_down_and_sleep(ethan, ethan.root.title_mc.start_btn, 1.0 / ethan._speed)
    set_property(ethan, ethan.root, 'currentLabel', 'table')
    time.sleep(1.0 / ethan._speed)
    #
    #     pass mock and flash, except flash master does not get the board back.
    echo_many(inject, ethan, 1.0/ 4,  5, columns)
    echo_many(inject, ethan, 1.0/ 8,  6, columns)
    #
    #     in flash, most but not all receive
    echo_many(inject, ethan, 1.0/16,  7, columns)
    echo_many(inject, ethan, 1.0/32,  8, columns)
    time.sleep(1.0/4)
    ethan.pb()
    # Expected:
    ## $$$$$$$$$
    ## $$$$$$$$$
    ## $$$$$$$$$
    ## $$$$$$$$$
    ## ,,,,,,,,,
    ## $$$$$$$$$
    ## $$$$$$$$$
    ## $$$$$$$$$
    ## $$$$$$$$$
    time.sleep(2.0)


    

def echo_large(globe, news):
    '''Large news.  See echo
    '''
    globe.log_news('echo_large', news)
    # logging.info('echo_large: %s' % news)
    large_news = load('lifeanddeath.large_news.py')
    news = upgrade(large_news, news)
    globe.publish(news)

def remote_echo():
    '''test echo remotely in flash.
    >>> code_unit.inline_examples(
    ...     setup_remote_control_snippet.__doc__, 
    ...     locals(), globals(), 
    ...     verify_examples = False)
    >>> code_unit.inline_examples(
    ...     echo.__doc__, 
    ...     locals(), globals(), 
    ...     verify_examples = True)
    '''

def stress_black(globe, start_interval = 16.0):
    '''Stress test black by sending large news to 9 intersections in a row.
    >>> gateway_process = configuration.subprocess_gateway(configuration.amf_host, 'embassy.py', verbose)
    >>> laurens = configuration.globe_class()
    >>> laurens.setup(configuration.mock_speed, configuration.setup_client)
    >>> set_property(laurens, laurens.root.title_mc.username_txt, 'text', 'laurens')
    >>> time.sleep(1.0 / laurens._speed)
    >>> set_property(laurens, laurens.root.title_mc.password_txt, 'text', 'l')
    >>> time.sleep(1.0 / laurens._speed)
    >>> mouse_down_and_sleep(laurens, laurens.root.title_mc.start_btn, 1.0 / laurens._speed)
    >>> set_property(laurens, laurens.root.gateway_mc.ready_time_txt, 'text', 'stress')
    >>> mouse_down_and_sleep(laurens, laurens.root.title_mc.start_btn, 64.0 / laurens._speed)
    >>> laurens.pb()
    XXXXXXXXX
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    >>> len(laurens.ambassador.receives)
    12
    >>> laurens.ambassador.receives[-1].keys()
    '''
    import copy
    logging.info('stress_black start interval=%s' % start_interval)
    interval = 2 * start_interval
    large_news = load('lifeanddeath.large_news.py')
    for r in range(1):
        for c in range(9):
            interval = 0.5 * interval
            news = copy.deepcopy(large_news)
            intersection_name = get_intersection_name(r, c)
            news[intersection_name] = {'currentLabel': 'black'}
            stress_log = 'stress_black publish=%s: interval=%s' % (intersection_name, interval)
            logging.info(stress_log)
            globe.publish(news)
            time.sleep(interval / globe._speed)
    logging.info('stress_black end interval=%s' % interval)
    time.sleep(start_interval)
    globe.pb()


def moonhyoung_computer_pass_example():
    '''Moonhyoung sees computer pass.  Then Moonhyoung moves.
    Gotcha:  want to replay white.  white_computer, not partnered.
    >>> code_unit.inline_examples(
    ...     ethan_lukasz_begin_example.__doc__, 
    ...     locals(), globals(), 
    ...     verify_examples = False)
    >>> moonhyoung = black
    >>> computer_moonhyoung = white
    >>> sloth = 1.0 / moonhyoung._speed
    >>> moonhyoung.root.lobby_mc.main_mc._04_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 1.897133)
    >>> moonhyoung.root.lobby_mc._04_mc.dominate_3_3_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 3.567127)
    >>> mouse_down_and_sleep(moonhyoung, moonhyoung.root.game_over_mc.start_mc, wait)
    >>> moonhyoung.root.game_over_mc.white_computer_mc.currentLabel
    'computer'
    >>> moonhyoung.root.game_over_mc.white_computer_mc.enter_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 2.757399)

    TODO:  do not sequence white computer option
    >>> time.sleep(3 * wait)
    >>> moonhyoung.root.game_over_mc.white_computer_mc.currentLabel
    'none'
    >>> mouse_down_and_sleep(moonhyoung, moonhyoung.root._1_1_mc, wait)
    >>> mouse_down_and_sleep(computer_moonhyoung, computer_moonhyoung.root._2_2_mc, wait)
    >>> time.sleep(sloth * 7.485410)
    >>> mouse_down_and_sleep(moonhyoung, moonhyoung.root._2_1_mc, wait)
    >>> mouse_down_and_sleep(computer_moonhyoung, computer_moonhyoung.root._0_0_mc, wait)
    >>> time.sleep(sloth * 8.023928)
    >>> mouse_down_and_sleep(moonhyoung, moonhyoung.root._2_0_mc, wait)
    >>> mouse_down_and_sleep(computer_moonhyoung, computer_moonhyoung.root._0_2_mc, wait)
    >>> time.sleep(sloth * 2.384054)
    >>> moonhyoung.root.game_over_mc.white_computer_mc.enter_mc.dispatchEvent(mouseDown)
    >>> time.sleep(wait)
    >>> moonhyoung.root.game_over_mc.white_computer_mc.currentLabel
    'computer'
    >>> moonhyoung.pb()
    OXO
    ,X,
    XXO
    >>> mouse_down_and_sleep(moonhyoung, moonhyoung.root._1_0_mc, wait)
    >>> ## computer_moonhyoung.root.pass_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 2.082763)
    >>> moonhyoung.pb()
    ,XO
    XX,
    XXO
    >>> mouse_down_and_sleep(moonhyoung, moonhyoung.root._1_2_mc, wait)
    >>> ## computer_moonhyoung.root.pass_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 2.869093)
    >>> moonhyoung.pb()
    ,X,
    XXX
    XX,
    >>> mouse_down_and_sleep(moonhyoung, moonhyoung.root._0_2_mc, wait)
    >>> ## computer_moonhyoung.root.pass_mc.dispatchEvent(mouseDown)
    >>> moonhyoung.pb()
    ,XX
    XXX
    XX,
    '''

