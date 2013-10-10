#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
Test of Life and Death relay from GnuGo to Flash Client
gtp:  Go Text Protocol
amf:  ActionScript Messaging Format

*>_<*   doh!  i can have old server still running with new server too.
'''
__author__ = 'Ethan Kennerly'



def how_to_play_example():
    '''To get a big piece, cut a cake.

    Here is a cake that has been cut.
        No special items.
        Flash asks referee to load board.
        >>> ambassador = ambassador_class()
        >>> news = ambassador.act_flash({'load_board': 
        ...     'score_white_by_18_board_text'})

        Referee loads board and plays through all moves.
        Flash shows board.
    >>> pb(ambassador.referee.board)
    ,,XOO,,,,
    ,,,XOO,,,
    ,,X,XO,,,
    ,,,XXO,,,
    ,,XXO,,,,
    ,,,XO,,,,
    ,XXOO,O,,
    XXOO,,,,,
    XOO,,,,,,

    Each player's territory is marked.
    >>> if not 10 < len(news.get('territory')):  news
        
    Does red win or lose?
        Win button
        Lose button
    Win:  Try again.
    Lose:  That's right!  Red loses.  Poor red.

    Here is another cake that has been cut.
        >>> news = ambassador.act_flash({'load_board': 
        ...     'score_black_by_14_board_text'})
    >>> referee.pb(ambassador.referee.board)
    ,,XXXO,,,
    ,,XOXOOO,
    ,,XOOO,O,
    ,,XOO,,,O
    ,,XO,OO,,
    ,,XOOXOOO
    ,,XXXXXXX
    ,,,,,,,,,
    ,,,,,,,,,
    
    Each player's territory is marked.
    >>> if not 10 < len(news.get('territory')):  news

    Does red win or lose?
        Win button
        Lose button
        No other elements are interactive
    Lose:  Try again.
    Win:  That's right!  Red wins!

    On a turn you cut one piece of cake.
    If you cut out a section, you eat that section.

    Here is a cake that is almost cut.
        session_1/territory_learn_to_play_go.prb  [1]
    Blue is taking cake.
    Stop blue.
    If move is different:  Try again.
    You win!

    Blue is going to take too much cake.
    Cut up the cake.
        session_1/territory_learn_to_play_go.prb  [2]
    If move is different:  Try again.
    You win!

    But if you get cut out, then your pieces get eaten.
    Eat a piece of cake.

        session_1/save_capture_lvl0_3.prb  [1, 2, 3]

    You can eat two pieces too.

        session_1/save_capture_lvl0_3.prb  [4, 5, 6]

    Careful you can get eaten, too!
    '''


    
def ambassador_timeout_example(patient):
    '''Referee notes timeout gracefully.
    >>> patient = ambassador_class()
    >>> patient.envoy = setup_timeout_example(patient.envoy)
    talk(envoy, 'genmove black') # --> 'timeout'
    >>> import code_unit
    >>> code_unit.print_diff( 
    ...     patient.ask({'genmove': 'white'}),
    ...    {'timeout': True, 'pass': True, 'turn': 'black'}  )
    referee.tell('genmove white', 'timeout')
    referee.tell('list_stones black', 'timeout')
    referee.tell('list_stones white', 'timeout')
    '''
    print 'code_unit.doctest_unit(ambassador_timeout_example)'


def ambassador_resign_example():
    r'''
    >>> ambassador = ambassador_class()
    >>> ambassador.gtp( 'loadsgf sgf/genmove_white_resign.sgf' )
    '= white\n\n'
    >>> news = ambassador.ask({'genmove': 'white'})
    >>> news.get('resign')
    'white'
    '''


def undo_hide_example():
    r'''Undo hide and last white turn.  
    
    Setup hide_black example.
    >>> ambassador = ambassador_class()
    >>> ambassador.referee._give_hide()
    >>> ambassador.referee._give_hide()
    >>> ambassador.referee._give_hide()
    >>> ambassador.gtp('set_random_seed 1257919092')
    '= \n\n'
    >>> news = ambassador.hide_black({'black': [(2, 3)]})
    >>> news = ambassador.act_flash({'genmove': 'white'})
    >>> news = ambassador.act_flash({'black': [(4, 5)]})
    >>> news = ambassador.act_flash({'genmove': 'white'})
    >>> news = ambassador.hide_black({'black': [(8, 8)]})
    >>> news = ambassador.act_flash({'genmove': 'white'})
    >>> print ambassador.referee.show_board()
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,/,O,,,
    ,,,O,,,,,
    ,,,,,X,,,
    ,,,O,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,/
    >>> news.get('territory')
    {'white': [(0, 4), (0, 5), (1, 4), (1, 5), (2, 4)]}
    >>> ambassador.referee.history[-1].get('territory')
    {'white': [(0, 4), (0, 5), (1, 4), (1, 5), (2, 4)]}
    
    Undo last two moves:  hidden stone played and one of white.
    >>> news = ambassador.act_flash({'undo': 2})
    >>> news.get('empty')
    [(2, 5)]
    >>> news.get('unhide')
    >>> neutral = news.get('territory').get('neutral')

    On undo, reset territory.
    >>> if not 40 < len(neutral):  news.get('territory')
    >>> news = ambassador.act_flash({'more': True})

    Unhide empty space so Flash will not hide next stone 
    that is played there.
    >>> news.get('empty')
    [(8, 8)]
    >>> news.get('unhide')
    [(8, 8)]
    >>> print ambassador.referee.show_board()
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,/,,,,,
    ,,,O,,,,,
    ,,,,,X,,,
    ,,,O,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    >>> news = ambassador.act_flash({'black': [(8, 8)]})
    >>> news.get('black')
    [(8, 8)]
    >>> news.get('unhide')
    >>> news.get('territory')
    >>> ambassador.referee.history[-1].get('territory')
    '''

def update_gnugo_example():
    '''Referee shows white's view of a board to GnuGo.

    Manual setup.
    >>> ambassador = ambassador_class()
    >>> ambassador.referee = referee.setup_undo_hide_example2(locals(), globals())
    >>> import time
    >>> time0 = time.clock()
    >>> gtp_response = update_gnugo(ambassador, ambassador.referee.history)
    >>> print ambassador.referee.show_board()
    O/,,,,,,,
    O/,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    >>> print ambassador.gtp('showboard')
    = 
       A B C D E F G H J
     9 O . . . . . . . . 9
     8 O . . . . . . . . 8
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

    White does not see the black spies '/'.
    When black captures, white does see black assassins.
    >>> news = ambassador.act_flash({'black': [[2, 0]]})
    >>> print ambassador.referee.show_board()
    ,X,,,,,,,
    ,X,,,,,,,
    X,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,

    Ambassador does not update GnuGo until white's turn 
    or flushed, so does not contemplate while black plays.
    >>> print ambassador.gtp('showboard')
    = 
       A B C D E F G H J
     9 O . . . . . . . . 9
     8 O . . . . . . . . 8
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
    >>> gtp_response = update_gnugo(ambassador, ambassador.referee.history)
    >>> print ambassador.gtp('showboard')
    = 
       A B C D E F G H J
     9 . X . . . . . . . 9
     8 . X . . . . . . . 8
     7 X . + . . . + . . 7
     6 . . . . . . . . . 6
     5 . . . . + . . . . 5
     4 . . . . . . . . . 4
     3 . . + . . . + . . 3
     2 . . . . . . . . . 2     WHITE (O) has captured 0 stones
     1 . . . . . . . . . 1     BLACK (X) has captured 2 stones
       A B C D E F G H J
    <BLANKLINE>
    <BLANKLINE>
    >>> news = ambassador.act_flash({'genmove': 'white'})
    >>> print ambassador.gtp('showboard')
    = 
       A B C D E F G H J
     9 . X . . . . . . . 9
     8 . X . . . . . . . 8
     7 X . + . . . + . . 7
     6 . . . . . . . . . 6
     5 . . . . O . . . . 5
     4 . . . . . . . . . 4
     3 . . + . . . + . . 3
     2 . . . . . . . . . 2     WHITE (O) has captured 0 stones
     1 . . . . . . . . . 1     BLACK (X) has captured 2 stones
       A B C D E F G H J
    <BLANKLINE>
    <BLANKLINE>
    >>> time1 = time.clock()
    >>> duration = time1 - time0
    >>> if 0.25 < duration:
    ...     duration
    '''

def protocol_example():
    r'''Ambassador keeps referee, Flash, and GnuGo in sync
    for hidden black and play by white.
    >>> ambassador = ambassador_class()
    >>> ambassador.referee._give_hide()
    >>> ambassador.referee._give_hide()
    >>> ambassador.referee._give_hide()
    >>> ambassador.gtp('set_random_seed 0')
    '= \n\n'
    >>> news = ambassador.hide_black({'black': [(0, 1)]})
    >>> news.get('black')
    [(0, 1)]
    >>> news = ambassador.act_flash({'genmove':  'white'})
    >>> news.get('white')
    [(4, 4)]
    >>> news = ambassador.hide_black({'black': [(1, 1)]})
    >>> news.get('black') or news
    [(1, 1)]
    >>> news = ambassador.act_flash({'genmove':  'white'})
    >>> print ambassador.gtp('showboard')
    = 
       A B C D E F G H J
     9 . . . . . . . . . 9
     8 . . . . . . . . . 8
     7 . . + . O . + . . 7
     6 . . . . . . . . . 6
     5 . . . . O . . . . 5
     4 . . . . . . . . . 4
     3 . . + . . . + . . 3
     2 . . . . . . . . . 2     WHITE (O) has captured 0 stones
     1 . . . . . . . . . 1     BLACK (X) has captured 0 stones
       A B C D E F G H J
    <BLANKLINE>
    <BLANKLINE>
    >>> print ambassador.referee.show_board()
    ,/,,,,,,,
    ,/,,,,,,,
    ,,,,O,,,,
    ,,,,,,,,,
    ,,,,O,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    '''


def step_on_black_spy_example():
    r'''GnuGo tries to play at black spy yet plays elsewhere.
    >>> ambassador = ambassador_class()
    >>> ambassador.referee._give_hide()
    >>> ambassador.referee._give_hide()
    >>> ambassador.referee._give_hide()
    >>> ambassador.gtp('set_random_seed 0')
    '= \n\n'
    
    This is same setup as protocol_example,
    so white would play at (4, 4).
    >>> news = ambassador.hide_black({'black': [(4, 4)]})
    >>> news.get('black')
    [(4, 4)]

    Referee reveals black spy to GnuGo.
    Ambassador updates GnuGo to take move again.
    >>> news = ambassador.act_flash({'genmove':  'white'})

    Inspecting:  History reveals unhide. only on white's turn.
    >>> import pprint; pprint.pprint(ambassador.referee.history)
    [{'black': (4, 4), 'hide': [(4, 4)]}, {'unhide': [(4, 4)], 'white': (5, 2)}]
    >>> news.get('white')
    [(5, 2)]
    >>> print ambassador.gtp('showboard')
    = 
       A B C D E F G H J
     9 . . . . . . . . . 9
     8 . . . . . . . . . 8
     7 . . + . . . + . . 7
     6 . . . . . . . . . 6
     5 . . . . X . . . . 5
     4 . . O . . . . . . 4
     3 . . + . . . + . . 3
     2 . . . . . . . . . 2     WHITE (O) has captured 0 stones
     1 . . . . . . . . . 1     BLACK (X) has captured 0 stones
       A B C D E F G H J
    <BLANKLINE>
    <BLANKLINE>
    >>> print ambassador.referee.show_board()
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,X,,,,
    ,,O,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,

    Play continues.
    >>> news = ambassador.act_flash({'black': [(2, 4)]})
    >>> news = ambassador.act_flash({'genmove':  'white'})
    >>> print ambassador.gtp('showboard')
    = 
       A B C D E F G H J
     9 . . . . . . . . . 9
     8 . . . . . . . . . 8
     7 . . O . X . + . . 7
     6 . . . . . . . . . 6
     5 . . . . X . . . . 5
     4 . . O . . . . . . 4
     3 . . + . . . + . . 3
     2 . . . . . . . . . 2     WHITE (O) has captured 0 stones
     1 . . . . . . . . . 1     BLACK (X) has captured 0 stones
       A B C D E F G H J
    <BLANKLINE>
    <BLANKLINE>
    >>> print ambassador.referee.show_board()
    ,,,,,,,,,
    ,,,,,,,,,
    ,,O,X,,,,
    ,,,,,,,,,
    ,,,,X,,,,
    ,,O,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    '''


def mark_territory_example():
    r'''On white's turn, GnuGo estimates territory, 
    which referee sends to Flash.

    >>> ambassador = ambassador_class()
    >>> ambassador.gtp('loadsgf reference_game/white_tiger_wallis.sgf')
    '= black\n\n'
    >>> ambassador.gtp('undo')
    '= \n\n'
    >>> ambassador.gtp('undo')
    '= \n\n'
    >>> print ambassador.gtp('showboard')
    = 
       A B C D E F G H J
     9 . . . . X . . . X 9
     8 . X . O X . X X X 8
     7 . . X X O X X X O 7
     6 . . X . O X . X O 6
     5 . . X . O X O O O 5
     4 . . X . O O X X O 4
     3 X . X X X O X O . 3
     2 X X X O O O X O . 2     WHITE (O) has captured 0 stones
     1 X O O O O . . . . 1     BLACK (X) has captured 4 stones
       A B C D E F G H J
    <BLANKLINE>
    <BLANKLINE>
    >>> territory_text = ambassador.gtp('initial_influence black territory_value')
    >>> ambassador.referee._set_territory_now(territory_text)
        
    Referee remembers old territory.
    'white', 'black'

    Black plays G6.
    White captures at G1.
    On white's turn, after white moves,
    >>> ambassador.gtp('play black G6')
    '= \n\n'
    >>> ambassador.gtp('genmove white')
    '= G1\n\n'
    >>> print ambassador.gtp('showboard')
    = 
       A B C D E F G H J
     9 . . . . X . . . X 9
     8 . X . O X . X X X 8
     7 . . X X O X X X O 7
     6 . . X . O X X X O 6
     5 . . X . O X O O O 5
     4 . . X . O O . . O 4
     3 X . X X X O + O . 3
     2 X X X O O O . O . 2     WHITE (O) has captured 4 stones
     1 X O O O O . O . . 1     BLACK (X) has captured 4 stones
       A B C D E F G H J
    <BLANKLINE>
    <BLANKLINE>

    Referee asks GnuGo to estimate territory.
    Gnugo estimates territory.
    Referee parses territory values.
    Referee notices what is new in territory:  the dead black group has been captured.
    Referee publishes new territory at each location.
    >>> territory2_text = ambassador.gtp('initial_influence black territory_value')
    >>> ambassador.referee._set_territory_now(territory2_text)
    >>> if not ambassador.referee.now.get('territory') == {'white': [(5, 6), (5, 7), (6, 6), (7, 6)], 'neutral': [(8, 6)]}: ambassador.referee.now.get('territory')

    [Data from another example]
    on_ask:  news:  
    Object type is: [Object]
    Object content is: 
    {
        territory: {
            black: [ /*0*/[ /*0*/0, /*1*/7 ], 
                /*1*/[ /*0*/0, /*1*/8 ],
                /*2*/[ /*0*/1, /*1*/7 ], 
                /*3*/[ /*0*/1, /*1*/8 ] ]
        },
        white: [ /*0*/[ /*0*/5, /*1*/2 ] ],
        formation_field: [ /*0*/[ /*0*/5, /*1*/2, /*2*/"rotate_0_mc" ] ],
        turn: "black"
    }

    Flash overlays new territory at each location:  (where the dead black group had been)
        neutral:  [no mark]
        black:  tint to black's color
        white:  tint to white's color

    Flash overlays new stone in territory at each location:  (where the dead black group had been)
        alive:  [no mark]
        dead:  v_v

    intersection_mc.territory_mc "dead", "black", "white", "neutral"
    '''


def setup_score_example():
    r'''
    >>> history = referee.setup_load_example()
    >>> for event in history:
    ...     news = ambassador.referee._turn_from_history(event)
   
    # with code_explorer.run_example
    # XXX even when komi set to 0, in setup_score_example
    # sometimes gnugo seems to get stuck on 5.5 for white.
    # XXX sometimes with setup_score_example, 
    # gnugo loads at move 1 instead of last move,
    # whereas suffix 999 always loads to last move.
    #>>> ambassador.referee._score(resign=False)
    ambassador.gtp( 'komi 0' )
    ambassador.gtp( 'loadsgf sgf/_update_gnugo.sgf 999' )
    ambassador.gtp( 'final_score' )
    #>>> ambassador.gtp('get_komi')
    ambassador.gtp( 'get_komi' )
    '=  5.5\n\n'
    #>>> ambassador.gtp('final_score')
    ambassador.gtp( 'final_score' )
    '= B+6.5\n\n'
    #>>> ambassador.gtp('komi 0')
    ambassador.gtp( 'komi 0' )
    '= \n\n'
    #>>> ambassador.gtp('final_score')
    ambassador.gtp( 'final_score' )
    '= B+6.5\n\n'
    #>>> ambassador.gtp('get_komi')
    ambassador.gtp( 'get_komi' )
    '=  0.0\n\n'
    #>>> ambassador.gtp('final_score')
    ambassador.gtp( 'final_score' )
    '= B+6.5\n\n'
    #>>> 
#>>> print ambassador.gtp('loadsgf sgf/_update_gnugo.sgf 50')
    ambassador.gtp( 'loadsgf sgf/_update_gnugo.sgf 50' )
    = black


#>>> print ambassador.gtp('showboard')
    ambassador.gtp( 'showboard' )
    = 
       A B C D E F G H J
     9 . . . . X . . . X 9
     8 . X . O X . X X . 8
     7 . . + X O X + . . 7
     6 . . X . O X . X . 6
     5 . . X . O X O O . 5
     4 . . X . O O X X O 4
     3 X . X X X O X O . 3
     2 X X X O O O X O . 2     WHITE (O) has captured 0 stones
     1 . O O O O . . . . 1     BLACK (X) has captured 4 stones
       A B C D E F G H J


#>>> print ambassador.gtp('loadsgf sgf/_update_gnugo.sgf')
    ambassador.gtp( 'loadsgf sgf/_update_gnugo.sgf' )
    = white


#>>> print ambassador.gtp('showboard')
    ambassador.gtp( 'showboard' )
    = 
       A B C D E F G H J
     9 . . . . . . . . . 9
     8 . . . . . . . . . 8
     7 . . + X . . + . . 7
     6 . . . . . . . . . 6
     5 . . . . + . . . . 5
     4 . . . . . . . . . 4
     3 . . X . . . X . . 3
     2 . . . . . . . . . 2     WHITE (O) has captured 0 stones
     1 . . . . . . . . . 1     BLACK (X) has captured 0 stones
       A B C D E F G H J


#>>> print ambassador.gtp('loadsgf sgf/_update_gnugo.sgf 999')
    ambassador.gtp( 'loadsgf sgf/_update_gnugo.sgf 999' )
    = black


#>>> print ambassador.gtp('showboard')
    ambassador.gtp( 'showboard' )
    = 
       A B C D E F G H J
     9 . . . . X . . . X 9
     8 . X . O X . X X X 8
     7 . . + X O X + X O 7
     6 . . X . O X X X O 6
     5 . . X . O X O O O 5
     4 . . X . O O . . O 4
     3 X . X X X O + O . 3
     2 X X X O O O . O . 2     WHITE (O) has captured 4 stones
     1 X O O O O . O . . 1     BLACK (X) has captured 4 stones
       A B C D E F G H J

        
    '''

def estimate_score_example():
    r'''Referee estimates score from GnuGo territory value.
    referee asks gnugo for territory value.
    referee estimates score from this.
    >>> history = referee.setup_load_example()
    get_history:  what do i do with this id?  FF
    get_history:  what do i do with this id?  VW
    get_history:  what do i do with this id?  AP
    get_history:  what do i do with this id?  HA
    get_history:  what do i do with this id?  ST
    get_history:  what do i do with this id?  DT
    get_history:  what do i do with this id?  KM
    get_history:  what do i do with this id?  RU
    >>> ambassador = ambassador_class()
    >>> for event in history[:-11]:
    ...     news = ambassador.referee._turn_from_history(event)

    Referee sends estimated score and change in score to flash.
    >>> news = ambassador.act_flash({'genmove':  'white'})
    >>> news = ambassador.act_flash({'black':  [(0, 0)]})
    >>> news = ambassador.act_flash({'genmove':  'white'})
    >>> news = ambassador.act_flash({'black':  [(0, 1)]})
    >>> news = ambassador.act_flash({'genmove':  'white'})
    >>> score = news.get('score', {})
    >>> if not score:  news
    >>> score.get('territory_txt')
    '5'

    Flash displays score number and change in score.  
    Flash also displays gauge showing who is winning.  
    the gauge is from pink to blue (1..79 frames, 0 --> 40).
    Referee clamps frame between 1 and 79.
    >>> score.get('frame')
    45

    The change in score appears with a + mark if positive.
    >>> score.get('change')
    'negative'
    >>> score.get('change_txt')
    '-3'

    On undo, the score reverts.
    >>> change = int(float(score.get('change_txt')))
    >>> today = int(float(score.get('territory_txt')))
    >>> referee.undo_gift = 25
    >>> news = ambassador.act_flash({'undo':  2})
    >>> news = ambassador.act_flash({'more':  True})
    >>> score = news.get('score', {})
    >>> t = int(float(score.get('territory_txt')))
    >>> t
    8
    >>> if not score.get('frame') == t + 40:  t, score.get('frame')

    And the change in score reverts to the change
    from the previous turn.
    For change in score of [-2..2], consider it neutral.
    >>> score.get('change_txt')
    '-2'
    >>> score.get('change')
    'neutral'

    The change equals the difference from last turn.
    >>> score = news.get('score', {})
    >>> yesterday = int(float(score.get('territory_txt')))
    >>> if not change == today - yesterday:  yesterday, change, today

    Score includes captures.
    >>> print 'TODO Score includes captures'
    '''


def pass_example():
    '''When computer passes, we see player's face on pass.

            BLUE
        I have eaten all I can.
        To end the game, click here.

    Here is a cake that has been cut.
        No special items.
        Flash asks referee to load board.
        >>> ambassador = ambassador_class()
        >>> news = ambassador.act_flash({'load_board': 
        ...     'score_white_by_18_board_text'})

        Referee loads board and plays through all moves.
        Flash shows board.
    >>> referee.pb(ambassador.referee.board)
    ,,XOO,,,,
    ,,,XOO,,,
    ,,X,XO,,,
    ,,,XXO,,,
    ,,XXO,,,,
    ,,,XO,,,,
    ,XXOO,O,,
    XXOO,,,,,
    XOO,,,,,,
    >>> news = ambassador.act_flash({'genmove': 'white'})
    >>> news.get('white')
    'pass'
    '''


def final_score_example():
    r'''When both players pass consecutively, end game.
    At end of game, score.
    >>> history = referee.setup_load_example()
    get_history:  what do i do with this id?  FF
    get_history:  what do i do with this id?  VW
    get_history:  what do i do with this id?  AP
    get_history:  what do i do with this id?  HA
    get_history:  what do i do with this id?  ST
    get_history:  what do i do with this id?  DT
    get_history:  what do i do with this id?  KM
    get_history:  what do i do with this id?  RU
    >>> ambassador = ambassador_class()
    >>> for event in history:
    ...     news = ambassador.referee._turn_from_history(event)
    >>> news = ambassador.referee.act_flash({'black':  ['pass']})
    >>> news = ambassador.referee._genmove_white_mock('pass')
    >>> ambassador.gtp('final_score')
    '= B+13.0\n\n'
    >>> ambassador.gtp('get_komi')
    '=  0.0\n\n'

    Anytime white passes, black is prompted.
    >>> news.get('pass_white_mc')
    'pass'

    Black wins
    >>> news.get('game_over')
    'win'

    Score saved gifts.
    >>> score = news.get('score', {})
    >>> score.get('territory_txt')
    '13'
    >>> ambassador.referee.extra_stone_gift * 20
    20
    >>> score.get('extra_stone_txt')
    '20'
    >>> ambassador.referee.hide_gift * 10
    30
    >>> score.get('hide_txt')
    '30'
    >>> ambassador.referee.undo_gift / 2
    15
    >>> score.get('undo_txt')
    '15'

    For a win, experience is the total.
    >>> score.get('experience_txt')
    '+78'

    Or if white resigns, end game and score territory 50.
    >>> ambassador = ambassador_class()
    >>> for event in history:
    ...     news = ambassador.referee._turn_from_history(event)
    >>> news = ambassador.referee._genmove_white_mock('resign')
    >>> score = news.get('score', {})
    >>> score.get('territory_txt')
    '50'
    '''

def undo_example():
    '''Flash client requests undo.
    >>> print 'TODO'
    
    Client asks for more.
    >>> print 'TODO: Client asks for more.'
    >>> print 'TODO:  in test mode, on validate, send more and expect client to ask for more.'
    '''

def evaluate_example():
    '''evaluate in same namespace as ambassador
    >>> ambassador = ambassador_class()
    >>> ambassador.evaluate('str(type(self))')
    "<class 'ambassador.ambassador_class'>"
    '''


def genmove_white_example():
    '''Generate a move for white after several moves have been made.
    >>> import text
    >>> text_sgf_tree = text.load('sgf/_genmove_white_error_white.sgf')
    >>> ambassador = ambassador_class()
    >>> ambassador.referee.history = referee.get_history(referee.parse(text_sgf_tree))
    >>> ambassador.referee.board = referee.history_text_to_board(referee.history_to_text(ambassador.referee.history))
    >>> news = ambassador.act_flash({'genmove':  'white'})
    >>> if not news.get('white'):  news
    '''


def white_capture_eye_example():
    '''White captures black by playing in eye.
    >>> import text
    >>> text_sgf_tree = text.load('sgf/_genmove_white_capture_eye.sgf')
    >>> ambassador = ambassador_class()
    >>> history = referee.get_history(referee.parse(text_sgf_tree))
    >>> for event in history:
    ...     news = ambassador.referee._turn_from_history(event)
    >>> news = ambassador.act_flash({'genmove':  'white'})
    >>> if not news.get('white'):  news
    >>> referee.pb(ambassador.referee.board)
    ,,,,XOOO,
    ,,,,XO,O,
    ,,,,XOO,,
    XX,,XXO,,
    OXXXXO,O,
    OOOXOO,,,
    ,,,OO,OO,
    ,,,,,,,OO
    ,,,,,,,,,
    '''


import configuration

verbose = configuration.verbose

gtp_host = configuration.gtp_host
gtp_port = configuration.gtp_port

import subprocess


def setup_gtp(gtp_port):
    base_command = 'gnugo-3.8.exe'
    import os
    # dirname = os.path.abspath('.')
    # command = dirname + '/' + configuration.computer_start
    command = os.path.join(os.getcwd(), 
            os.path.dirname(__file__),
            base_command)
            # configuration.computer_start)
    # command = dirname + '/gnugo_port' + str(gtp_port) + '.bat'
    options = ['--gtp-listen', '%i' % gtp_port, 
            '--mode', 'gtp', '--boardsize', '9', '--level', '1']
        
    try:
        gtp_pid = subprocess.Popen([command] + options).pid
    except:
        print 'setup_gtp', command
        print 'The system cannot find the file specified'
        raise
    time.sleep(2)
    return gtp_pid


def setup_client():
    '''
    C:\project\lifeanddeath>lifeanddeath.swf
    '''
    gtp_pid = subprocess.Popen(
        ['c:/project/lifeanddeath/lifeanddeath.bat']).pid
    time.sleep(2)
    return gtp_pid
    

amf_host = configuration.amf_host
amf_port = configuration.amf_port

import socket
import time

time_format = '%Y-%m-%d_%H-%M-%S'


def setup_envoy(gtp_host, gtp_port):
    '''Must be setup before testing.
    See ambassador_class for example.
    '''
    gtp_pid = setup_gtp(gtp_port)
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


def setup_timeout_example(envoy):
    r'''
    Time out gracefully
    >>> envoy = setup_envoy(gtp_host, gtp_port)
    >>> envoy = setup_timeout_example(envoy)
    talk(envoy, 'genmove black') # --> 'timeout'
    >>> print talk(envoy, 'showboard')
    = 
       A B C D E F G H J
     9 . . . . . . X . . 9
     8 . . X X . . . X . 8
     7 . X O . . O O . . 7
     6 . X O X . . . X . 6
     5 . X . . O . . . . 5
     4 . . . . . . . . . 4
     3 . . X . . O O . . 3
     2 . . . X . . . . . 2     WHITE (O) has captured 0 stones
     1 . . . . . . X . . 1     BLACK (X) has captured 0 stones
       A B C D E F G H J
    <BLANKLINE>
    <BLANKLINE>
    >>> talk(envoy, 'genmove black')
    timeout:  response: ""
    'timeout'

    on timeout previous message is concatenated with next.
    >>> envoy.settimeout(8)
    >>> talk(envoy, 'get_random_seed')
    '= E4\n\n= 1257816200\n\n'
    >>> envoy = teardown_timeout_example(envoy)
    '''
    envoy = teardown_timeout_example(envoy)
    listen = talk(envoy, 'boardsize 9')
    if 'timeout' == listen:
        print listen
    listen = talk(envoy, 'clear_board')
    if 'timeout' == listen:
        print listen
    listen = talk(envoy, 'loadsgf sgf/timeout_1-32_genmove_black.sgf')
    if 'timeout' == listen:
        print listen
    listen = talk(envoy, 'set_random_seed 0')
    if 'timeout' == listen:
        print listen
    listen = talk(envoy, 'set_random_seed 1257816200')
    if 'timeout' == listen:
        print listen
    envoy.settimeout(1.0/1024)
    listen = talk(envoy, 'clear_cache')
    if 'timeout' == listen:
        print listen
    print "talk(envoy, 'genmove black') # --> 'timeout'"
    return envoy


def teardown_timeout_example(envoy):
    '''Clean up timeout example
    '''
    envoy.settimeout(8)
    talk(envoy, 'set_random_seed 0')
    talk(envoy, 'clear_board')
    return envoy


def talk(envoy, gtp_command, delay = 1.0/256, verbose = False):
    r'''Send and receive in Go Text Protocol to GnuGo.
    Send full message and receive full message 
    and validate GTP format of a single response.
    Creating a second ambassador may corrupt responses.
    For examples, see update_gnugo_example.
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
    while not gtp_response.endswith(referee.gtp_end_of_response):
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
            error_message = 'talk(%s):  socket error %i:  "%s"' \
                        % (gtp_command, 
                                error_number, error_string)
            print error_message
            return error_message
    if not referee.gtp_ok(gtp_response):
        print '''talk(%s) # GnuGo strange response:  "%s"''' \
                    % (gtp_command, gtp_response.__repr__())
        gtp_response = referee.last_response(gtp_response)
    if verbose:
        print 'talk(%s) # gtp response:  "%s"' \
                % (gtp_command, gtp_response)
    return gtp_response


import referee

class ambassador_class(object):
    r'''Stable connection to GnuGo.
    >>> ambassador = ambassador_class()
    >>> ambassador.verbose = True
    >>> ambassador.ask({'clear_board':  True})
    ambassador.ask( {'clear_board': True} )
    ambassador._confer( ['clear_board'] )
    ambassador.gtp( 'clear_board' )
    ambassador._confer( ['list_stones black', 'list_stones white'] )
    ambassador.gtp( 'list_stones black' )
    ambassador.gtp( 'list_stones white' )
    {'clear_board': True, 'turn': 'black'}
    >>> ambassador.verbose = False

    Get same results each time we do this test.
    >>> ambassador.gtp('set_random_seed 0')
    '= \n\n'
    >>> print ambassador.gtp('showboard')
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

    Above, after '=' there is a space.  '= '

    ActionScript returns Array which PyAMF converts to list,
    but referee likes tuples, so convert [2, 3] to (2, 3).
    >>> code_unit.print_diff( ambassador.ask({'black':  [[2, 3]]}),
    ...    {'genmove': 'white', 'black': [(2, 3)], 'turn': 'white'} )
    >>> print ambassador.gtp('showboard')
    = 
       A B C D E F G H J
     9 . . . . . . . . . 9
     8 . . . . . . . . . 8
     7 . . + X . . + . . 7
     6 . . . . . . . . . 6
     5 . . . . + . . . . 5
     4 . . . . . . . . . 4
     3 . . + . . . + . . 3
     2 . . . . . . . . . 2     WHITE (O) has captured 0 stones
     1 . . . . . . . . . 1     BLACK (X) has captured 0 stones
       A B C D E F G H J
    <BLANKLINE>
    <BLANKLINE>

    >>> code_unit.print_diff(ambassador.ask( {'white':  [(4, 5)]}),
    ...     {'white': [(4, 5)], 'turn': 'black'} )
    >>> print ambassador.gtp('showboard')
    = 
       A B C D E F G H J
     9 . . . . . . . . . 9
     8 . . . . . . . . . 8
     7 . . + X . . + . . 7
     6 . . . . . . . . . 6
     5 . . . . + O . . . 5
     4 . . . . . . . . . 4
     3 . . + . . . + . . 3
     2 . . . . . . . . . 2     WHITE (O) has captured 0 stones
     1 . . . . . . . . . 1     BLACK (X) has captured 0 stones
       A B C D E F G H J
    <BLANKLINE>
    <BLANKLINE>

    Refresh board
    >>> code_unit.print_diff( 
    ...     ambassador.ask({'showboard': True}),
    ...     {'black': [(2, 3)], 'clear_board': True, 
    ...     'turn': 'black', 'white': [(4, 5)]} )

    Load file in Smart Go Format (SGF).
    Flash asks Python to ask GnuGo to load SGF.
    Then Python tells Flash to clear the board and play the stones.
    >>> code_unit.print_diff(
    ...     ambassador.ask({'loadsgf':  'sgf/white_tiger.sgf'}),
    ...     {'clear_board': True, 'white': [(5, 4), (7, 3), (7, 5), (8, 4)], 
    ...     'black': [(2, 2), (2, 3), (2, 5), (2, 6), (5, 2), (5, 6), (6, 2), (6, 6)], 'turn': 'black'} )

    TODO:  Show client board.  Update client board.
    >>> print ambassador.gtp('showboard')
    = 
       A B C D E F G H J
     9 . . . . . . . . . 9
     8 . . . . . . . . . 8
     7 . . X X . X X . . 7
     6 . . . . . . . . . 6
     5 . . . . + . . . . 5
     4 . . X . O . X . . 4
     3 . . X . . . X . . 3
     2 . . . O . O . . . 2     WHITE (O) has captured 0 stones
     1 . . . . O . . . . 1     BLACK (X) has captured 0 stones
       A B C D E F G H J
    <BLANKLINE>
    <BLANKLINE>

    Save game to SGF.
    >>> ambassador.ask({'printsgf':  'sgf/white_tiger_test.sgf'})
    {}
    >>> code_unit.print_diff(
    ...     ambassador.ask({'loadsgf':  'sgf/white_tiger_test.sgf'}),
    ...      {'clear_board': True, 'white': [(5, 4), (7, 3), (7, 5), (8, 4)], 
    ...     'black': [(2, 2), (2, 3), (2, 5), (2, 6), (5, 2), (5, 6), (6, 2), (6, 6)], 'turn': 'black'} )

    Print SGF.
    >>> import os
    >>> sgf_path = 'sgf/' + time.strftime(time_format) + '.sgf'
    >>> if os.path.exists(sgf_path):
    ...     os.remove(sgf_path)
    >>> print ambassador.printsgf()
    {}
    >>> os.path.exists(sgf_path)
    True
    >>> code_unit.print_diff( 
    ...     ambassador.ask({'loadsgf':  sgf_path}),
    ...     {'clear_board': True, 
    ...     'white': [(5, 4), (7, 3), (7, 5), (8, 4)], 
    ...     'black': [(2, 2), (2, 3), (2, 5), (2, 6), (5, 2), (5, 6), (6, 2), (6, 6)], 'turn': 'black'} )
    >>> os.remove(sgf_path)

    Play against computer.  Computer generates a move.
    >>> ambassador.referee.configure({'white': 'computer'})
    {'white': 'computer'}
    >>> print ambassador.referee.white
    computer

    Python asks ActionScript to ask Python to ask GnuGo to make a move.
    >>> code_unit.print_diff(
    ...     ambassador.ask({'black':  [(4, 4)]}),
    ...     {'black': [(4, 4)], 'genmove': 'white', 'turn': 'white'} )

    So then, ActionScript asks Python to ask GnuGo to make a move, which Python reports back.
    # >>> print ambassador.gtp('showboard')
    >>> code_unit.print_diff(
    ...     ambassador.ask({'genmove': 'white'}),
    ...     {'white': [(6, 4)], 'turn': 'black'} )
    >>> print ambassador.gtp('showboard')
    = 
       A B C D E F G H J
     9 . . . . . . . . . 9
     8 . . . . . . . . . 8
     7 . . X X . X X . . 7
     6 . . . . . . . . . 6
     5 . . . . X . . . . 5
     4 . . X . O . X . . 4
     3 . . X . O . X . . 3
     2 . . . O . O . . . 2     WHITE (O) has captured 0 stones
     1 . . . . O . . . . 1     BLACK (X) has captured 0 stones
       A B C D E F G H J
    <BLANKLINE>
    <BLANKLINE>

    Do not warn of empty regions.
    >>> code_unit.print_diff(
    ...     ambassador.ask({'black':  [(4, 3)]}),
    ...      {'black': [(4, 3)], 'genmove': 'white', 
    ...         'turn': 'white'} )
    >>> code_unit.print_diff(
    ...     ambassador.ask({'genmove':  'white'}),
    ...      {'white': [(7, 2)], 
    ...         'turn': 'black'} )
    >>> print ambassador.gtp('showboard')
    = 
       A B C D E F G H J
     9 . . . . . . . . . 9
     8 . . . . . . . . . 8
     7 . . X X . X X . . 7
     6 . . . . . . . . . 6
     5 . . . X X . . . . 5
     4 . . X . O . X . . 4
     3 . . X . O . X . . 3
     2 . . O O . O . . . 2     WHITE (O) has captured 0 stones
     1 . . . . O . . . . 1     BLACK (X) has captured 0 stones
       A B C D E F G H J
    <BLANKLINE>
    <BLANKLINE>

    Undo last two moves (so black can move again)
    >>> code_unit.print_diff(
    ...     ambassador.ask({'undo':  2}),
    ...     {'empty': [(4, 3), (7, 2)]} )

    black to move, previous state.
    >>> print ambassador.gtp('showboard')
    = 
       A B C D E F G H J
     9 . . . . . . . . . 9
     8 . . . . . . . . . 8
     7 . . X X . X X . . 7
     6 . . . . . . . . . 6
     5 . . . . X . . . . 5
     4 . . X . O . X . . 4
     3 . . X . O . X . . 3
     2 . . . O . O . . . 2     WHITE (O) has captured 0 stones
     1 . . . . O . . . . 1     BLACK (X) has captured 0 stones
       A B C D E F G H J
    <BLANKLINE>
    <BLANKLINE>

    Hide a stone
    ActionScript asks Python to hide a stone.
    Flash marks hidden stone and increments style such that opponent cannot see.
    >>> services['hide'] = ambassador.hide_black
    >>> code_unit.print_diff( 
    ...     ambassador.referee.hide({'black':  [(7, 2)]}),
    ...     {'black': [(7, 2)], 'genmove': 'white', 'hide': [(7, 2)], 'turn': 'white'} )
    >>> ambassador.referee.moves[-1]
    (7, 2)

    GnuGo doesn't know.
    >>> print ambassador.gtp('showboard')
    = 
       A B C D E F G H J
     9 . . . . . . . . . 9
     8 . . . . . . . . . 8
     7 . . X X . X X . . 7
     6 . . . . . . . . . 6
     5 . . . . X . . . . 5
     4 . . X . O . X . . 4
     3 . . X . O . X . . 3
     2 . . . O . O . . . 2     WHITE (O) has captured 0 stones
     1 . . . . O . . . . 1     BLACK (X) has captured 0 stones
       A B C D E F G H J
    <BLANKLINE>
    <BLANKLINE>

    Referee remembers position of hidden stone.
    >>> ambassador.referee.hidden
    {'black': [(7, 2)]}

    If black would play at hidden stone, 
    Referee notes it's already been played.
    >>> ambassador.ask({'black':  [(7, 2)]})
    {'hide': [(7, 2)]}
    
    If GnuGo would play at hidden stone, 
    Python undoes opponent's move 
    and reveals the hidden stone to both.
    GnuGo plays elsewhere.
    >>> code_unit.print_diff(
    ...     ambassador.ask({'genmove': 'white'}),
    ...     {'genmove': 'white', 'unhide': [(7, 2)]} )

    ActionScript unhides.

    Reveal assassins
    If black would play to capture needing the hidden stone,
    reveal the hidden stone and the next stone.
    >>> code_unit.print_diff( 
    ...     ambassador.ask({'genmove': 'white'}),
    ...    {'white': [(7, 6)], 'turn': 'black'} )
    >>> code_unit.print_diff( 
    ...     ambassador.referee.hide({'black':  [(8, 3)]}),
    ...   {'black': [(8, 3)], 'genmove': 'white', 
    ...     'hide': [(8, 3)], 'turn': 'white', 
    ...     'danger': [(8, 3)], 'warning': [(7, 3), (8, 4)]} )
    >>> print ambassador.gtp('showboard')
    = 
       A B C D E F G H J
     9 . . . . . . . . . 9
     8 . . . . . . . . . 8
     7 . . X X . X X . . 7
     6 . . . . . . . . . 6
     5 . . . . X . . . . 5
     4 . . X . O . X . . 4
     3 . . X . O . X . . 3
     2 . . X O . O O . . 2     WHITE (O) has captured 0 stones
     1 . . . . O . . . . 1     BLACK (X) has captured 0 stones
       A B C D E F G H J
    <BLANKLINE>
    <BLANKLINE>

    After play a hidden stone and white moves, 
    black takes a turn.
    >>> code_unit.print_diff(
    ...     ambassador.ask({'genmove': 'white'}),
    ...     {'white': [(6, 7)], 'turn': 'black'} )

    Transmit danger based on hidden stone.
    If in danger, nevermind saying that warning ended.
    If in warning, nevermind saying that danger ended.
    >>> code_unit.print_diff(
    ...     ambassador.ask({'black':  [(6, 3)]}),
    ...    {'black': [(6, 3)], 'genmove': 'white', 'danger': [(7, 3)], 'turn': 'white'} )
    >>> code_unit.print_diff(
    ...     ambassador.ask({'genmove': 'white'}),
    ...     {'white': [(5, 7)], 'turn': 'black'} )

    GnuGo doesn't see the hidden danger.
    >>> print ambassador.gtp('showboard')
    = 
       A B C D E F G H J
     9 . . . . . . . . . 9
     8 . . . . . . . . . 8
     7 . . X X . X X . . 7
     6 . . . . . . . . . 6
     5 . . . . X . . . . 5
     4 . . X . O . X O . 4
     3 . . X X O . X O . 3
     2 . . X O . O O . . 2     WHITE (O) has captured 0 stones
     1 . . . . O . . . . 1     BLACK (X) has captured 0 stones
       A B C D E F G H J
    <BLANKLINE>
    <BLANKLINE>
    
    Hidden stone can capture!  Reveal.
    >>> code_unit.print_diff( 
    ...     ambassador.ask({'black':  [[7, 4]]}),
    ...    {'assassin':  True, 'black': [(7, 4)], 'danger': [(7, 4), (8, 4)],
    ...     'danger end': [(7, 3)], 'empty': [(7, 3)],
    ...     'genmove': 'white', 'turn': 'white', 'unhide': [(8, 3)], 'warning': [(8, 3)]} )
    >>> print ambassador.gtp('showboard')
    = 
       A B C D E F G H J
     9 . . . . . . . . . 9
     8 . . . . . . . . . 8
     7 . . X X . X X . . 7
     6 . . . . . . . . . 6
     5 . . . . X . . . . 5
     4 . . X . O . X O . 4
     3 . . X X O . X O . 3
     2 . . X . X O O . . 2     WHITE (O) has captured 0 stones
     1 . . . X O . . . . 1     BLACK (X) has captured 1 stones
       A B C D E F G H J
    <BLANKLINE>
    <BLANKLINE>
    >>> news = ambassador.ask({'genmove':  'white'})
    
    If play a hidden stone to capture, immediately reveal.
    >>> print ambassador.referee.show_board()
    ,,,,,,,,,
    ,,,,,,,,,
    ,,XX,XX,,
    ,,,,,,,,,
    ,,,,X,O,,
    ,,X,O,XO,
    ,,XXO,XO,
    ,,X,XOO,,
    ,,,XO,,,,
    >>> code_unit.print_diff( 
    ...        ambassador.hide({'black': [[8, 5]]}),
    ...        {'assassin': True, 'danger end': [(8, 4)], 
    ...            'warning': [(7, 4), (8, 5)], 
    ...            'black': [(8, 5)], 'warning end': [(8, 3)], 
    ...            'genmove': 'white', 'turn': 'white', 'empty': [(8, 4)]}  )
    >>> print ambassador.gtp('showboard')
    = 
       A B C D E F G H J
     9 . . . . . . . . . 9
     8 . . . . . . . . . 8
     7 . . X X . X X . . 7
     6 . . . . . . . . . 6
     5 . . . . X . O . . 5
     4 . . X . O . X O . 4
     3 . . X X O . X O . 3
     2 . . X . X O O . . 2     WHITE (O) has captured 0 stones
     1 . . . X . X . . . 1     BLACK (X) has captured 2 stones
       A B C D E F G H J
    <BLANKLINE>
    <BLANKLINE>
    
    If player asks more than once for same position, ignore duplicates.
    >>> news = ambassador.ask( {'genmove': 'white'} )
    >>> news = ambassador.ask( {'black': [[7, 7]]} )
    >>> news.get('genmove')
    'white'
    >>> ambassador.ask( {'black': [[7, 7]]} )
    {'already_at': [(7, 7)]}
    
    If player asks for two different moves or more in a row, 
    ignore second and the rest.
    >>> ambassador.ask( {'black': [[8, 8]]} )
    {'turn_reminder': 'white'}
    >>> ambassador.ask( {'black': [[7, 8]]} )
    {'turn_reminder': 'white'}
    
    If undo a hide, then unhide that position.
    If undo an unhide, then do not rehide that position 
    because opponent has already seen it.

    When I ask for last_move,
    GnuGo crashes.  Why?
    # >>> ambassador.gtp('last_move')
    '''
    def __init__(self, host = None, gnugo_port = None):
        if str != type(host):
            print 'ambassador():  is this a host?  %s' % host
        if host:
            self.host = host
        else:
            self.host = amf_host
        self.port = amf_port
        if configuration.gtp:
            if not gnugo_port:
                gnugo_port = gtp_port
            if not host:
                self.envoy = setup_envoy(gtp_host, gnugo_port)
            else:
                self.envoy = setup_envoy(host, gnugo_port)
        self.referee = referee.referee_class()
        self.verbose = verbose
        self.referee.verbose = verbose
        self.referee.ambassador = self
        global services
        self.services = services
        if configuration.gtp and self.verbose:
            print self.gtp('get_random_seed').__repr__()
   
    def enter(self):
        return {'root':  'lobby'}

    def act_flash(self, client_request):
        if self.verbose:
            import pprint
            print 'ambassador.act_flash(', \
                pprint.pformat(client_request), \
                ')'
        alerts = self.referee.act_flash(client_request)
        if alerts:
            return alerts
        elif 'genmove' in client_request:
            return self._notify_gtp(client_request)
        else:
            return alerts

    def _notify_gtp(self, client_request):
        '''Please act before notifying.'''
        gtp_commands = self.referee.to_gtp(client_request)
        self._listen_gtp(gtp_commands)
        #gtp_commands = self.referee.to_gtp_list_stones()
        #self._confer(['list_stones white'])
        client_news = self.referee.notify()
        return client_news

    def _listen_gtp(self, gtp_commands):
        if self.verbose:
            print 'ambassador._listen_gtp(', \
                gtp_commands, ')'
        while gtp_commands:
            gtp_response = update_gnugo(self, self.referee.history)
            gtp_command = gtp_commands.pop(0)
            gtp_response = self.gtp(gtp_command)
            #undo moved to referee
            #if 'undo' == gtp_command:
            #    # see result of undoing.
            #    time.sleep(1)
            # if gtp_command.startswith('genmove'):
                # gnugo takes a bit of time to respond.
                # time.sleep(1)
            followups = self.referee.act_white_gtp(
                    gtp_command, gtp_response)
            if followups:
                gtp_commands.extend(followups)
        if self.verbose:
            print self.gtp('showboard')

    def ask(self, client_request):
        '''DEPRECATED for act_flash'''
        if self.verbose:
            import pprint
            print 'ambassador.ask(', \
                pprint.pformat(client_request), \
                ')'
        client_news = self.referee.ask(client_request)
        if client_news:
            return client_news
        return self._do(client_request)

    def _do(self, client_request):
        '''DEPRECATED for _notify_gtp.
        Please ask before doing.'''
        gtp_commands = self.referee.to_gtp(client_request)
        self._confer(gtp_commands)
        gtp_commands = self.referee.to_gtp_list_stones()
        self._confer(gtp_commands)
        client_news = self.referee.notify_dictionary()
        return client_news
    
    def _confer(self, gtp_commands):
        if self.verbose:
            print 'ambassador._confer(', \
                gtp_commands, ')'
        while gtp_commands:
            gtp_command = gtp_commands.pop(0)
            gtp_response = self.gtp(gtp_command)
            if not referee.gtp_ok(gtp_response) \
                    and 'timeout' != gtp_response:
                print '''ambassador._confer:  When I said %s, 
                    GnuGo did not sound happy: %s''' \
                    % (gtp_command, gtp_response)
            if 'undo' == gtp_command:
                # see result of undoing.
                time.sleep(0.5)
            if gtp_command.startswith('genmove'):
                # give a little time before responding.
                time.sleep(1)
            followups = self.referee.tell(
                    gtp_command, gtp_response)
            if followups:
                gtp_commands.extend(followups)

    def hide_black(self, client_request):
        '''Ambassador asks referee to hide,
        referee may ask ambassador to play instead.
        White only needs notification if assassinated.
        '''
        news = self.referee.hide_black(client_request)
        return news
        #gnugo finds out from update_gnugo.
        #if news and news.has_key('assassin'):
        #    return self._notify_black(news)
        #else:
        #    return news

    def hide(self, client_request):
        '''Ambassador asks referee to hide,
        referee may ask ambassador to play instead.
        '''
        news = self.referee.hide(client_request)
        if news and news.has_key('assassin'):
            return self._do(news)
        else:
            return news

    def gtp(self, gtp_command):
        '''Wrap for simple service.
        TODO:  If board is cleared, update previous_stone_dictionary
        Does not update ambassador's board or move history.
        '''
        if self.verbose:
            print "ambassador.gtp( '" \
                + gtp_command + "' )"
        return talk(self.envoy, gtp_command, self.verbose)
        
    def printsgf(self, message_ignored = None):
        '''Return SGF text'''
        if self.verbose:
            import pprint
            print 'printsgf(', \
                    pprint.pformat(message_ignored), ')'
        sgf_path = 'sgf/' + time.strftime(time_format) + '.sgf'
        gtp_command = 'printsgf ' + sgf_path
        gtp_response = self.gtp(gtp_command)
        gtp_response = talk(self.envoy, gtp_command, delay = 1)
        return referee.gtp_response_to_dictionary(gtp_response)

    # same namespace as ambassador
    def echo(self, data):
        '''
        Just return data back to the client.
        '''
        if verbose:
            print 'echo(', str(data), ')'
        return data

    def execute(self, code):
        if verbose:
            print 'execute(', str(code), ')'
        exec(code, globals(), locals())

    def evaluate(self, code):
        if verbose:
            print 'evaluate(', str(code), ')'
        return eval(code, globals(), locals())

import text
def update_gnugo(ambassador, history):
    sgf_tree = referee.get_sgf_tree(history)
    path = 'sgf/_update_gnugo.sgf'
    text.save(path, str(sgf_tree))
    # XXX why does ambassador's GnuGo sometimes load blank board?  
    # is an invalid move being appended to path?
    gtp_command = 'loadsgf ' + path + ' 999'
    return ambassador.gtp(gtp_command)
    

# Gateway

'''
Adapted from PyAMF Hello world example server.
'''



def echo(data):
    '''
    Just return data back to the client.
    '''
    if verbose:
        print 'echo(', str(data), ')'
    return data


def execute(code):
    if verbose:
        print 'execute(', str(code), ')'
    exec(code)

def evaluate(code):
    if verbose:
        print 'evaluate(', str(code), ')'
    return eval(code)

services = {
    #'echo': echo,
    #'execute': execute,
    #'evaluate': evaluate,
}


def echo_response(category, content):
    return category, content



def create(ambassador):
    r'''create WSGI server.  must know ambassador beforehand.
    When ambassador is verbose, httpd app prints request and response.
    >>> ambassador = ambassador_class(host = 'localhost') #doctest: +ELLIPSIS
    ambassador.gtp( 'get_random_seed' )
    '= ...\n\n'
    >>> ambassador.verbose = True
    >>> httpd = create(ambassador)
    >>> app = httpd.get_app()
    >>> app({'PATH_INFO':  '/crossdomain.xml'}, echo_response) #doctest: +ELLIPSIS
    httpd.get_app()({'PATH_INFO': '/crossdomain.xml'}, <function echo_response at 0x...>)
    filename redirects to ...crossdomain.xml
    httpd.get_app()({'PATH_INFO': '/crossdomain.xml'}, <function echo_response at 0x...>) # --> "['<?xml version="1.0"?>\n', '<!DOCTYPE cross-domain-policy SYSTEM "http://www.adobe.com/xml/dtds/cross-domain-policy.dtd">\n', '\n', '<cross-domain-policy>\n', '\t<site-control permitted-cross-domain-policies="all"/>\n', '\t<allow-access-from domain="*.finegamedesign.com"/>\n', '\t<allow-access-from domain="*.finegamedesign.com" to-ports="5900,8000,52502"/>\n', '\t<allow-http-request-headers-from domain="*" headers="*" secure="false"/>\n', '</cross-domain-policy>\n']"
    ['<?xml version="1.0"?>\n', '<!DOCTYPE cross-domain-policy SYSTEM "http://www.adobe.com/xml/dtds/cross-domain-policy.dtd">\n', '\n', '<cross-domain-policy>\n', '\t<site-control permitted-cross-domain-policies="all"/>\n', '\t<allow-access-from domain="*.finegamedesign.com"/>\n', '\t<allow-access-from domain="*.finegamedesign.com" to-ports="5900,8000,52502"/>\n', '\t<allow-http-request-headers-from domain="*" headers="*" secure="false"/>\n', '</cross-domain-policy>\n']

    *>_<*      if an attribute is missing, then obscure internal service error is returned.
    **********************************************************************
File "C:\project\lifeanddeath\client.py", line 481, in simple_client_class
Failed example:
    import pdb; pdb.set_trace(); print client.echo('Hello world!')
Exception raised:
    Traceback (most recent call last):
      File "C:\Python25\lib\doctest.py", line 1212, in __run
        compileflags, 1) in test.globs
      File "<doctest simple_client_class[2]>", line 1, in <module>
        import pdb; pdb.set_trace(); print client.echo('Hello world!')
      File "C:\project\lifeanddeath\ambassador.py", line 1785, in prepend_header
s
        return function(self.headers, *args, **kwargs)
      File "F:\project\lifeanddeath\archive_2009-12-02\server\pyamf\remoting\cli
ent\__init__.py", line 116, in __call__
      File "F:\project\lifeanddeath\archive_2009-12-02\server\pyamf\remoting\cli
ent\__init__.py", line 105, in _call
      File "F:\project\lifeanddeath\archive_2009-12-02\server\pyamf\remoting\cli
ent\__init__.py", line 424, in execute_single
      File "F:\project\lifeanddeath\archive_2009-12-02\server\pyamf\remoting\cli
ent\__init__.py", line 476, in _getResponse
    RemotingError: HTTP Gateway reported status 500 Internal Server Error
**********************************************************************

    '''
    from pyamf.remoting.gateway.wsgi import WSGIGateway
    from wsgiref import simple_server
    gw = WSGIGateway(ambassador.services)

    try:
        httpd = simple_server.WSGIServer(
            (ambassador.host, ambassador.port),
            simple_server.WSGIRequestHandler,
        )
    except:
        print 'create(ambassador) # %s:%i' \
                % (ambassador.host, ambassador.port)
        raise

    import os
    # pasted from pyamf_util.py
    def app(environ, start_response):
        try:
            ## if ambassador.verbose:
            ##     print 'httpd.get_app()(%s, %s)' % (environ, start_response)
            if environ['PATH_INFO'] == '/crossdomain.xml':
                fn = os.path.join(os.getcwd(), 
                        os.path.dirname(__file__),
                        'crossdomain.xml')
                print 'filename redirects to %s' % fn
                fp = open(fn, 'rt')
                buffer = fp.readlines()
                fp.close()
                start_response('200 OK', [
                    ('Content-Type', 'application/xml'),
                    ('Content-Length', str(len(''.join(buffer))))
                ])
                response = buffer
            else:
                response = gw(environ, start_response)
            ## if ambassador.verbose:
            ##     print 'httpd.get_app()(%s, %s) # --> "%s"' \
            ##             % (environ, start_response, response)
        except: 
            print 'httpd.get_app()(%s, %s) # exception' \
                    % (environ, start_response)
            raise
        return response
    httpd.set_app(app)
    return httpd


def run(httpd):
    print 'run:  Hosting simple AMF gateway at http://%s:%i' \
            % httpd.server_address
    try:
        httpd.serve_forever()
    except socket.gaierror:
        print 'run:  Could not reach this address %s and port %i' \
                % httpd.server_address
    except KeyboardInterrupt:
        print 'run:  KeyboardInterrupt'
        httpd.server_close()
    except:
        print 'run:  Closing...'
        httpd.server_close()


from threading import Thread
class run_it(Thread):
    '''run(httpd) locks Python interpretter.  
    So run_it starts a thread.
    # >>> run_snippet(shell, start_snippet)
    # >>> host = run_it(httpd)
    # >>> host.start()
    '''
    def __init__(self, httpd):
        Thread.__init__(self)
        self.httpd = httpd
    def run(self):
        run(self.httpd)


start_service_snippet = '''
services['gtp'] = ambassador.gtp
services['ask'] = ambassador.act_flash
services['printsgf'] = ambassador.printsgf
services['hide'] = ambassador.hide_black
services['configure'] = ambassador.referee.configure
services['set_level'] = ambassador.referee.set_level
services['validate'] = referee.validate
services['show_board'] = ambassador.referee.show_board
services['echo'] = ambassador.echo
services['execute'] = ambassador.execute
services['evaluate'] = ambassador.evaluate
httpd = create(ambassador)
host = run_it(httpd)
host.start()
'''

def register_service(ambassador, services):
    services['gtp'] = ambassador.gtp
    services['ask'] = ambassador.act_flash
    services['printsgf'] = ambassador.printsgf
    services['hide'] = ambassador.hide_black
    services['configure'] = ambassador.referee.configure
    services['set_level'] = ambassador.referee.set_level
    services['validate'] = referee.validate
    services['show_board'] = ambassador.referee.show_board
    services['echo'] = ambassador.echo
    services['execute'] = ambassador.execute
    services['evaluate'] = ambassador.evaluate
    return services
    
def start_service(ambassador):
    httpd = create(ambassador)
    host = run_it(httpd)
    host.start()
    
ambassador_snippet = '''
os.chdir('../lifeanddeath')
from ambassador import *
amf_host = 'localhost'
verbose = True
ambassador = ambassador_class(host = 'localhost')
ambassador.verbose = verbose
ambassador.referee.verbose = verbose
services = register_service(ambassador, services)
start_service(ambassador)
# time.sleep(1)
# run_examples(shell, setup_score_example.__doc__)
# setup_client()
'''
# >>> run_snippet(shell, snippet)


snippet = '''
gateway = setup_gateway(host='localhost', verbose=True)
## gateway = quiet_gateway(host='localhost')
## import client
## kyeong = client.simple_client_class(
##     gateway.services, gateway.host, gateway.port)
## news = kyeong.login('nexon1', 'nexon1')
'''


def setup_test_ambassador():
    '''Silent ambassador starts hosting on localhost.
    >>> ambassador = setup_test_ambassador()
    run:  Hosting simple AMF gateway at http://127.0.0.1:5900
    '''
    global verbose
    verbose = False
    global configuration
    configuration.verbose = False
    configuration.amf_host = 'localhost'
    ambassador = ambassador_class()
    ambassador.host = 'localhost'
    services = register_service(ambassador, services)
    start_service(ambassador)
    import time
    time.sleep(3)
    return ambassador



def face(self, function, *args, **kwargs):
    '''Wrap method to always prepend one's headers.'''
    def prepend_headers(*args, **kwargs):
        return function(self.headers, *args, **kwargs)
    return prepend_headers


def deface(function, *args, **kwargs):
    '''Wrap method to always remove first argument.
    >>> def a(a):  return a
    ...     
    >>> face_a = deface(a)
    >>> face_a('no', 'yes')
    'yes'
    '''
    def remove_headers(*args, **kwargs):
        args = list(args)
        headers = args.pop(0)
        args = tuple(args)
        return function(*args, **kwargs)
    return remove_headers


def _deface_services(services):
    for name, service in services.items():
        service = deface(service)
        services[name] = service
    return services


def _authenticate_login(users, headers):
    '''
    >>> users = {'nexon1': {'password': 'nexon1'}}
    >>> _authenticate_login(users, {})
    False
    >>> 
    >>> _authenticate_login(users, {'credentials': {'user':  'nexon1', 'password': 'nexon1'}})
    True
    >>> _authenticate_login(users, {'credentials': {'user':  'nexon1', 'password': 'Nexon1'}})
    False
    '''
    credentials = headers.get('credentials')
    if not credentials:
        return False
    user_id = credentials.get('user')
    if not user_id:
        return False
    claim = credentials.get('password')
    if claim is None:
        return False
    user = users.get(user_id)
    if not user:
        return False
    actual = user.get('password')
    if not actual:
        return False
    if not actual == claim:
        return False
    return True



def get_user(headers):
    '''
    >>> get_user({})
    >>> get_user({'credentials': {'user':  'nexon1', 'password': 'nexon1'}})
    'nexon1'
    '''
    credentials = headers.get('credentials')
    if not credentials:
        return None
    user = credentials.get('user')
    return user
    

from decorator import decorator

def tuplify(*args):
    '''>>> tuplify(0, 10, 20)
    (0, 10, 20)'''
    return args


def range_float(start, stop, step):
    '''Like range, but with floating point numbers.
    >>> for n in range_float(0, 1, 0.25):
    ...     n
    ...     
    0
    0.25
    0.5
    0.75
    '''
    level = start
    while level < stop:
        yield level
        level += step


@decorator
def authentically(function, *args, **kwargs):
    '''identify user to referee.'''
    # XXX args[...] seems like a hack.
    gateway = args[0]
    headers = args[1]
    user = get_user(headers)
    if _authenticate(gateway.users, headers):
        if 3 <= len(args):
            request = args[2]
            if dict == type(request):
                request.update({'user': user})
        else:
            request = {}
        authentic_args = tuplify(gateway, user, *args[2:])
        news = function(*authentic_args, **kwargs)
        news.update({'echo': {'watch':  4}})
        now = gateway.stopwatch.duration
        # XXX Is idle still essential to critical examples?
        gateway.users = update_idle(gateway.users, 
                user, request, now)
        ## if 'ethan' == user:
        ##     import pdb; pdb.set_trace(); 
        if user in gateway.logins:
            # let others know news has been published
            for other in gateway.logins:
                if gateway.users[other].get('news'):
                    gateway.users[other][
                            'news']['published'] = True
            # wait for my news to be published or time limit
            if 'watch' in request:
                time_limit = request['watch']
                nap = 1.0 / 64
                for moment in range_float(
                        0.0, time_limit, nap):
                    my_news = gateway.users[user].get('news')
                    if my_news.get('published'):
                        ## print 'authentically: ', my_news
                        ## if 'ethan' == user:
                        ##     import pdb; pdb.set_trace(); 
                        break
                    time.sleep(nap)
            # after waiting for publication, pick up the news
            news = referee.notify_user(
                    gateway.users, user, news)
        else:
            print 'authentically:  user authentic but not login?\n  %s\n    %s'  \
                    % (gateway.users, gateway.logins)  
        return news
    elif _authenticate_login(gateway.users, headers):
        if user in gateway.logins:
            return {'gateway_error': 'login_as_you',
                'root':  'login'}
    return {'gateway_error':  'session', 
                'root':  'login'}


@decorator
def login_authentically(function, *args, **kwargs):
    '''User exists and is not logged on.
    See client.two_user_login_example.'''
    # XXX arg0 seems like a hack.
    gateway = args[0]
    headers = args[1]
    if not _authenticate_login(gateway.users, headers):
        return {'gateway_error':  'password', 
                'root':  'login'}
    else:
        user = get_user(headers)
        news_update = {}
        if user in gateway.logins:
            user_data = gateway.users.get(user)
            now = gateway.stopwatch.duration
            gateway.users.get(user)['news'].update( 
                {'gateway_error':  'login_as_you'} )
            gateway._exit(user)
            news_update = {'gateway_error':  'already_login'} 
        else:
            if gateway.max_logins <= len(gateway.logins):
                return {'gateway_error':  'max_logins'}
        authentic_args = tuplify(gateway, user, *args[2:])
        news = function(*authentic_args, **kwargs)
        news = referee.notify_user(gateway.users, user, news)
        news.update(news_update)
        news.update({'echo': {'watch':  4}})
        return news


@decorator
def logout_authentically(function, *args, **kwargs):
    # XXX args[...] seems like a hack.
    gateway = args[0]
    headers = args[1]
    user = get_user(headers)
    if _authenticate(gateway.users, headers):
        if 3 <= len(args):
            request = args[2]
            if dict == type(request):
                request.update({'user': user})
        else:
            request = {}
        authentic_args = tuplify(gateway, user, *args[2:])
        news = function(*authentic_args, **kwargs)
        news = referee.notify_user(gateway.users, user, news)
        now = gateway.stopwatch.duration
        gateway.users = update_idle(gateway.users, 
                user, request, now)
        return news
    else:
        return {'gateway_error':  'session', 
                'root':  'login'}


def _authenticate(users, headers):
    '''Must match user and session ID.
    >>> users = {'nexon1': {'password': 'nexon1', 'session': 1}}
    >>> _authenticate(users, {})
    False
    >>> _authenticate(users, {'credentials': {'user':  'nexon1', 'session': 1}})
    True
    >>> _authenticate(users, {'credentials': {'user':  'nexon1', 'session': 2}})
    False
    >>> session0 = {'nexon1': {'password': 'nexon1', 'session': 0}}
    >>> _authenticate(session0, {'credentials': {'user':  'nexon1', 'session': 0}})
    True
    '''
    credentials = headers.get('credentials')
    if not credentials:
        return False
    user_id = credentials.get('user')
    if not user_id:
        return False
    claim = credentials.get('session')
    if claim is None:
        return False
    user = users.get(user_id)
    if not user:
        return False
    actual = user.get('session')
    if actual is None:
        return False
    if not actual == claim:
        return False
    return True


def is_active(user_data, user, now):
    last_time = user_data.get('last_time', now)
    user_data['last_time'] = last_time
    if now - last_time <= 30 * 60:
        return True
    return False


def update_idle(users, user, request, now):
    '''Change users to show last time and insert news if not active in 30 minutes.
    >>> users = {'nexon1': {'password': 'nexon1', 'session': 0}}
    >>> update_idle(users, 'nexon1', {}, 0)
    {'nexon1': {'session': 0, 'password': 'nexon1', 'last_time': 0}}
    >>> update_idle(users, 'nexon1', {'a': 1}, 1)
    {'nexon1': {'session': 0, 'password': 'nexon1', 'last_time': 1}}
    >>> update_idle(users, 'nexon1', {}, 30 * 60)
    {'nexon1': {'session': 0, 'password': 'nexon1', 'last_time': 1}}
    >>> update_idle(users, 'nexon1', {}, 30 * 60 + 2)
    {'nexon1': {'session': 0, 'news': {'gateway_error': 'inactive'}, 'password': 'nexon1', 'last_time': 1}}

    Modifies users
    >>> users
    {'nexon1': {'session': 0, 'news': {'gateway_error': 'inactive'}, 'password': 'nexon1', 'last_time': 1}}

    First call pastes 'last_time'.
    >>> users = {'nexon1': {'password': 'nexon1', 'session': 0}}
    >>> update_idle(users, 'nexon1', {}, 30 * 60)
    {'nexon1': {'session': 0, 'password': 'nexon1', 'last_time': 1800}}
    >>> update_idle(users, 'nexon1', {}, 59 * 60)
    {'nexon1': {'session': 0, 'password': 'nexon1', 'last_time': 1800}}
    '''
    user_data = users.get(user)
    if not request == {}:
        user_data['last_time'] = now
    else:
        if not is_active(user_data, user, now):
            user_news = user_data.get('news', {})
            user_news.update({'gateway_error':  'inactive'})
            user_data['news'].update(user_news)
    return users



def _subscribe(gateway_users, referee_users):
    '''referee user news refers to gateway user news.
    For example, see client.two_player_example'''
    for color in ['black', 'white']:
        player = referee_users[color]
        if player:
            player_name = player.get('user')
            if player_name:
                user_data = gateway_users.get(
                        player_name)
                if user_data is not None:
                    user_data['news'].update(player['news'])
                    player['news'] = user_data['news']
                    ## print "player['news']: ", player['news']
                    ## print "user_data['news']: ", user_data['news']
                    assert player['news'] is user_data['news']


import stopwatch

class gateway_class(object):
    '''Route user to ambassador.'''
    def __init__(self):
        #self.services = register_service(self, 
        #        services)
        self.max_logins = 2
        self.ambassadors = []
        gnugo_port0 = gtp_port
        for u in range(self.max_logins):
            ambassador = ambassador_class(gtp_host, 
                    gnugo_port0 + u)
            self.ambassadors.append(ambassador)
        self.host = self.ambassadors[0].host
        self.port = self.ambassadors[0].port
        self.verbose = self.ambassadors[0].verbose
        self.logins = []
        self.services = {
            'echo': self.echo,
            'gtp': self.gtp,
            'ask': self.ask,
            'hide': self.hide,
            'configure': self.configure,
            'set_level': self.set_level,
            'validate': self.validate,
            'show_board': self.show_board,
            'echo': self.echo,
            'execute': self.execute,
            'evaluate': self.evaluate,
            'enter': self.enter,
            'create': self.create,
            'join': self.join,
            'start': self.start,
            'stop': self.stop,
            'exit': self.exit,
            'get_start_time': self.get_start_time,
            }
        self.users = {
                'nexon1': {'password': 'nexon1', 'level': 1, 'news':  {}},
                'nexon2': {'password': 'nexon2', 'level': 1, 'news':  {}},
                'ethan': {'password': 'e', 'level': 40, 'news':  {}},
                'jade': {'password': 'j', 'level': 1, 'news':  {}},
                '_usertest_': {'password': '_usertest_', 'level': 1, 'news':  {}},
            }
        self.stopwatch = stopwatch.stopwatch_class()
        self.stopwatch.start()
        self.session_count = 0
        self.start_time = 0

    def getService(self, service_name):
        '''Mock gateway tests locally and quickly, 
        with PDB trace and exception traceback.'''
        return getattr(self, service_name)

    def _exit(self, user):
        '''clear board, logout, and end session.'''
        ambassador = self._get_ambassador(user)
        news = ambassador.act_flash({'clear_board':  True})
        news.update({'root':  'login'})
        self.users[user].pop('session')
        self.logins.remove(user)
        return news

    def get_start_time(self, *args, **kwargs):
        return self.start_time

    @authentically
    def gtp(self, user, *args, **kwargs):
        ambassador = self._get_ambassador(user)
        return ambassador.gtp(*args, **kwargs)

    @authentically
    def ask(self, user, *args, **kwargs):
        ambassador = self._get_ambassador(user)
        return ambassador.act_flash(*args, **kwargs)

    @authentically
    def create(self, creator, *args, **kwargs):
        ambassador = self._get_ambassador(creator)
        level = self.users.get(creator).get('level', 1)
        news = ambassador.referee.create(creator, level)
        if not news.get('root') == 'table':
            print 'create: ', news
        if 'busy' not in news and 'error' not in news:
            _subscribe(self.users, ambassador.referee.users)
            for user in self.logins:
                self.users.get(user)['news'].update(
                    {'offer_table':  creator} )
        return news

    @authentically
    def join(self, user, creator):
        ambassador = self._get_ambassador(creator)
        self.users.get(user)['ambassador'] = ambassador
        level = self.users.get(user).get('level', 1)
        news = ambassador.referee.join(user, level)
        if 'busy' not in news and 'error' not in news:
            _subscribe(self.users, ambassador.referee.users)
        return news

    @authentically
    def start(self, user, *args, **kwargs):
        ambassador = self._get_ambassador(user)
        news = ambassador.referee.start(user)
        return news

    @authentically
    def stop(self, user, *args, **kwargs):
        ambassador = self._get_ambassador(user)
        news = ambassador.referee.stop(user, *args, **kwargs)
        return news

    @authentically
    def hide(self, user, *args, **kwargs):
        ambassador = self._get_ambassador(user)
        return ambassador.hide_black(*args, **kwargs)

    @authentically
    def configure(self, user, *args, **kwargs):
        ambassador = self._get_ambassador(user)
        return ambassador.referee.configure(*args, **kwargs)

    @authentically
    def set_level(self, user, *args, **kwargs):
        ambassador = self._get_ambassador(user)
        return ambassador.referee.set_level(*args, **kwargs)

    def show_board(self, user, *args, **kwargs):
        ambassador = self._get_ambassador(user)
        return ambassador.referee.show_board(*args, **kwargs)

    @login_authentically
    def enter(self, user, *args, **kwargs):
        self.logins.append(user)
        self.users.get(user)['session'] \
                = self.session_count
        self.users.get(user)['news'].update(
                {'session':  self.session_count} )
        self.session_count += 1
        ambassador = self._get_ambassador(user)
        news = ambassador.enter(
                *args, **kwargs)
        level = self.users.get(user).get('level')
        if level:
            news['level'] = str(level)
        return news

    @logout_authentically
    def exit(self, user, *args, **kwargs):
        return self._exit(user)

    @authentically
    def echo(self, user, *args, **kwargs):
        ambassador = self._get_ambassador(user)
        return ambassador.echo(*args, **kwargs)

    @authentically
    def execute(self, user, *args, **kwargs):
        ambassador = self._get_ambassador(user)
        return ambassador.execute(*args, **kwargs)

    @authentically
    def evaluate(self, user, *args, **kwargs):
        ambassador = self._get_ambassador(user)
        return ambassador.evaluate(*args, **kwargs)

    @authentically
    def validate(self, user, *args, **kwargs):
        return referee.validate(*args, **kwargs)

    def _get_ambassador(self, user):
        ambassador = self.users.get(user).get('ambassador')
        if not ambassador:
            index = self.logins.index(user)
            ambassador = self.ambassadors[index]
            self.users.get(user)['ambassador'] = ambassador
        return ambassador


def register_gateway_service(ambassador, services):
##    services['gtp'] = deface(ambassador.gtp)
##    services['ask'] = deface(ambassador.act_flash)
##    services['printsgf'] = deface(ambassador.printsgf)
##    services['hide'] = deface(ambassador.hide_black)
##    services['configure'] = deface(ambassador.referee.configure)
##    services['set_level'] = deface(ambassador.referee.set_level)
##    services['validate'] = deface(referee.validate)
##    services['show_board'] = deface(ambassador.referee.show_board)
    ambassador.echo = deface(ambassador.echo)
    services['echo'] = ambassador.echo
##    services['execute'] = deface(ambassador.execute)
##    services['evaluate'] = deface(ambassador.evaluate)
    return services


from pyamf.remoting.gateway.wsgi import WSGIGateway
from pyamf.remoting.gateway import expose_request

from twisted.web import server
from twisted.web.wsgi import WSGIResource
from twisted.python.threadpool import ThreadPool
from twisted.internet import reactor
from twisted.application import service, strports


def quiet_gateway(host = 'localhost', verbose_option = False):
    '''create gateway that is not verbose'''
    global verbose
    verbose = verbose_option
    global configuration
    configuration.verbose = verbose_option
    configuration.amf_host = host
    gateway = gateway_class()
    gateway.host = host
    return gateway

def setup_gateway(host = 'localhost', verbose = False):
    '''wrap an ambassador.
    TODO:  Serve two users.
    See two_user_login_example in client.py
    >>> gateway = setup_gateway() #doctest: +ELLIPSIS
    run:  Hosting ... AMF gateway at http://127.0.0.1:5900

    If running two, then notify.
    >>> gateway2 = setup_gateway() #doctest: +ELLIPSIS
    run:  Hosting ... AMF gateway at http://127.0.0.1:5900
    setup_gateway:  gateway.start_time ... but client gets ...  Do you have a server setup already?
    '''
    gateway = quiet_gateway(host, verbose)
    start_service(gateway)
    import time
    gateway.start_time = time.asctime()
    _verify_start_time(gateway)
    time.sleep(2)
    return gateway


def _verify_start_time(gateway):
    from pyamf.remoting.client import RemotingService
    client = RemotingService('http://' 
                + gateway.host 
                + ':' + str(gateway.port))
    start_time = client.getService('get_start_time')()
    if not gateway.start_time == start_time:
        print '_verify_start_time:  gateway.start_time %s but client gets %s.\n    Do you have a server setup already?\n    Are you connecting to a server at an unintended host?' \
                % (gateway.start_time, start_time)


import code_unit


if __name__ == '__main__':
    import sys
    start_client = False
    silent = False
    host = False
    for arg in sys.argv:
        if arg == '--test':
            code_unit.test_file_args('./ambassador.py', 
                    sys.argv, locals(), globals())
            # I suspect these tests interfere with socket.
            break
        if arg == '--client':
            start_client = True            
        if arg == '--silent':
            silent = True            
        if arg == '--host':
            host = True
        elif host:
            amf_host = arg
            gtp_host = arg
            host = False
    else:
        if not silent:
            verbose = True
            configuration.verbose = True
        else:
            verbose = False
            configuration.verbose = False
        ambassador = ambassador_class()
        ambassador.verbose = verbose
        ambassador.referee.verbose = verbose
        # services must be defined in global namespace
        services['gtp'] = ambassador.gtp
        services['ask'] = ambassador.act_flash
        services['printsgf'] = ambassador.printsgf
        services['hide'] = ambassador.hide_black
        services['configure'] = ambassador.referee.configure
        services['set_level'] = ambassador.referee.set_level
        services['validate'] = referee.validate
        services['show_board'] = ambassador.referee.show_board
        services['echo'] = ambassador.echo
        services['execute'] = ambassador.execute
        services['evaluate'] = ambassador.evaluate
        httpd = create(ambassador)
        run(httpd)
        ##? host = run_it(httpd)
        ##? host.start()
    if start_client:
        time.sleep(1)
        setup_client()


