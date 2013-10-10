'''Client examples of playing a lesson of Go problems.
'''
__author__ = 'Ethan Kennerly'

from lesson import *
from client import *

def play_lesson(index, white, black, mouse_down_and_sleep, wait):
    # XXX Complaint of circular import if import in global namespace.
    from master import play_sgf
    lesson = pathed_lesson()
    sgf_file = lesson[index]
    play_sgf(sgf_file, white, black, mouse_down_and_sleep, wait)

def wait_to_play_lesson(index, ethan, lukasz, mouse_down_and_sleep, wait):
    '''lock execution up to one minute to play lesson when starting play.'''
    for second in [1] * 60:
        time.sleep(second)
        if lukasz.root.currentLabel in ['_3_3', '_5_5']:
            if 'none' == lukasz.root.game_over_mc.currentLabel:
                if 'black' == lukasz.root.turn_mc.currentLabel:
                    play_lesson(index, ethan, lukasz, mouse_down_and_sleep, wait)
                    break

def listen_to_play_sgf(ethan, lukasz, mouse_down_and_sleep, wait):
    '''Ethan secretly scripts Lukasz SGF player.  
    XXX run_examples complains IndentError if more than one line indented.
    '''
    # XXX Complaint of circular import if import in global namespace.
    from master import play_sgf
    def play_sgf_file_and_clear(mouse_event):
        sgf_file = lukasz.root.sgf_file_txt.text
        if sgf_file and 'sgf_file_txt' != sgf_file:
            # as not to lock up parsing news, start a thread.
            from threading import Thread
            class play_sgf_thread_class(Thread):
                '''as not to lock up parsing news, start a thread.
                '''
                def __init__(self):
                    Thread.__init__(self)
                def run(self):
                    time.sleep(3.0 / lukasz._speed)
                    logging.info('play_sgf_thread started')
                    play_sgf(sgf_file, ethan, lukasz, mouse_down_and_sleep, wait)
                    logging.info('play_sgf_thread shutdown')
            play_sgf_thread = play_sgf_thread_class()
            play_sgf_thread.start()
    lukasz.root.play_sgf_mc.addEventListener(MouseEvent.MOUSE_DOWN, 
            play_sgf_file_and_clear)


def ethan_lukasz_begin_example():
    '''Ethan creates a table and lukasz joins.  They start.
    Ethan enters the lobby and creates a multiplayer game.
    >>> gateway_process = configuration.subprocess_gateway(configuration.amf_host, 'embassy.py', configuration.verbose)

    >>> white = configuration.globe_class()
    >>> ethan = white

    Internet lag plus server lag is always less than three seconds.
    >>> wait = 4.0 / configuration.mock_speed
    >>> white.setup(configuration.mock_speed, configuration.setup_client)
    >>> set_property(white, white.root.title_mc.username_txt, 'text', 'computer_lukasz')
    >>> # set_property(white, white.root.title_mc.username_txt, 'text', 'ethan')
    >>> time.sleep(wait)
    >>> set_property(white, white.root.title_mc.password_txt, 'text', 'computer_lukasz')
    >>> # set_property(white, white.root.title_mc.password_txt, 'text', 'kennerly')
    >>> time.sleep(wait)

    #>>> mouse_down_and_sleep(white, white.root.title_mc.start_btn,
    #...     wait)
    >>> mouse_down_and_sleep(white, white.root.title_mc.start_btn, max(2, 2 * wait))

    Soon, he enters the lobby.
    >>> property_diff(white, white.root, 'currentLabel', 'lobby')

    lukasz logs in.
    >>> black = configuration.globe_class()
    >>> black = black
    >>> black.setup(configuration.mock_speed, configuration.setup_client)
    >>> set_property(black, black.root.title_mc.username_txt, 'text', 'lukasz')
    >>> time.sleep(2 * wait)
    >>> configuration.mock_speed
    1.0
    >>> set_property(black, black.root.title_mc.password_txt, 'text', 'l')
    >>> time.sleep(wait)
    >>> mouse_down_and_sleep(black, black.root.title_mc.start_btn, max(2, 2 * wait))

    INT. TABLES WITH CAKES
    >>> property_diff(white, white.root, 'currentLabel', 'lobby')
    >>> property_diff(black, black.root, 'currentLabel', 'lobby')

    #LUKASZ SEES NO COMMENT.
    #>>> property_diff(black, black.root.comment_mc,
    #...     'currentLabel', 'none')

    #- Ethan secretly scripts Lukasz' SGF player.  
    #- >>> listen_to_play_sgf(white, black, mouse_down_and_sleep, wait)
    '''


def ethan_lukasz_begin_listen_example():
    '''Ethan creates a table and lukasz joins.  They start.
    Ethan enters the lobby and creates a multiplayer game.
    >>> gateway_process = configuration.subprocess_gateway(configuration.amf_host, 'embassy.py', configuration.verbose)
    >>> ethan = configuration.globe_class()
    >>> ethan.setup(configuration.mock_speed, configuration.setup_client)
    >>> set_property(ethan, ethan.root.title_mc.username_txt, 'text', 'ethan')
    >>> time.sleep(1.0 / ethan._speed)
    >>> set_property(ethan, ethan.root.title_mc.password_txt, 'text', 'kennerly')
    >>> time.sleep(1.0 / ethan._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root.title_mc.start_btn,
    ...     1.0 / ethan._speed)

    Soon, he enters the lobby.
    >>> property_diff(ethan, ethan.root, 'currentLabel', 'lobby')

    lukasz logs in.
    >>> lukasz = configuration.globe_class()
    >>> lukasz.setup(configuration.mock_speed, configuration.setup_client)
    >>> set_property(lukasz, lukasz.root.title_mc.username_txt, 'text', 'lukasz')
    >>> time.sleep(1.0 / lukasz._speed)
    >>> set_property(lukasz, lukasz.root.title_mc.password_txt, 'text', 'l')
    >>> time.sleep(1.0 / lukasz._speed)
    >>> mouse_down_and_sleep(lukasz, lukasz.root.title_mc.start_btn,
    ...     1.0 / lukasz._speed)

    INT. TABLES WITH CAKES
        >>> property_diff(lukasz, lukasz.root, 'currentLabel', 'lobby')

    LUKASZ SEES NO COMMENT.
        >>> property_diff(lukasz, lukasz.root.comment_mc,
        ...     'currentLabel', 'none')

    Ethan secretly scripts Lukasz' SGF player.  
    >>> wait = 3.0
    >>> listen_to_play_sgf(ethan, lukasz, mouse_down_and_sleep, wait)
    '''


def lukasz_begin_example():
    '''Ethan creates a table and lukasz joins.  They start.
    Ethan enters the lobby and creates a multiplayer game.
    >>> gateway_process = configuration.subprocess_gateway(configuration.amf_host, 'embassy.py', configuration.verbose)

    Internet lag plus server lag is always less than three seconds.
    >>> wait = 3.0

    lukasz logs in.
    >>> black = configuration.globe_class()
    >>> black.setup(configuration.mock_speed, configuration.setup_client)
    >>> set_property(black, black.root.title_mc.username_txt, 'text', 'lukasz')
    >>> time.sleep(wait / black._speed)
    >>> set_property(black, black.root.title_mc.password_txt, 'text', 'l')
    >>> time.sleep(wait / black._speed)
    >>> mouse_down_and_sleep(black, black.root.title_mc.start_btn,
    ...     wait / black._speed)

    INT. TABLES WITH CAKES
        >>> property_diff(black, black.root, 'currentLabel', 'lobby')
    '''


def beginner_example():
    r'''Lukasz selects a 5x5 cake and counts the pieces of cake.
        >>> code_unit.inline_examples(
        ...     ethan_lukasz_begin_example.__doc__, 
        ...     locals(), globals(), 
        ...     verify_examples = False)

                ETHAN
        ON THE FIRST TABLE,
        CLICK THE FIRST CAKE.

    LUKASZ CLICKS FIRST CAKE.  IT FLASHES UNTIL RECEIVED.
        >>> mouse_down_and_sleep(black, black.root.lobby_mc._00_mc.capture_3_3_mc,
        ...     1.0 / black._speed)
        >>> property_diff(black, black.root.lobby_mc._00_mc.capture_3_3_mc, 
        ...     'currentLabel', 'none')

    WE WAIT A BIT FOR CLIENT TO FINISH.  TODO: Why so slow?
        >>> time.sleep(3.0 / black._speed)

    INT. TABLE - CONTINUOUS

    5X5 CAKE ON TABLE.  THERE ARE NO SETUP OPTIONS.
        >>> property_diff(black, black.root, 'currentLabel', '_5_5')
        >>> property_diff(black, black.root.game_over_mc, 
        ...     'currentLabel', 'preview')


    XXX SERVER REPLIES NAME OF SGF FILE.
        >>> property_diff(black, black.root.sgf_file_txt, 
        ...     'text', 'sgf/beginner/count_5_5.sgf')

                LUKASZ
        RED
        >>> property_diff(black, black.root['turn_mc']['black_user_txt'], 
        ...     'text', 'lukasz')
        >>> property_diff(ethan, ethan.root['turn_mc']['black_user_txt'], 
        ...     'text', 'lukasz')

                ETHAN
        BLUE
        >>> property_diff(black, black.root['turn_mc']['white_user_txt'], 
        ...     'text', 'ethan')
        >>> property_diff(ethan, ethan.root['turn_mc']['white_user_txt'], 
        ...     'text', 'ethan')
        
                BUTTON
        LET'S EAT
        >>> property_diff(black, black.root.pass_white_mc, 'currentLabel', 'none')
        
    LUKASZ CLICKS ON BUTTON.
        >>> mouse_down_and_sleep(black, black.root.game_over_mc.start_mc, 1.0 / black._speed)
        >>> board_diff(ethan, ethan.root._0_0_mc, 
        ...     'currentLabel', 'empty_white')

    SERVER THEN DISPATCH MOUSE DOWN PLAY_SGF_MC.  
    XXX MASTER AUTOMATICALLY STARTS THE SCRIPT.
        >>> clicks = (2 * 5) + 5
        >>> comments = 6
        >>> duration = wait * (clicks + comments)

                LUKASZ
        PROTOTYPE IS QUITE SLOW.  SORRY.
        >>> sludge = 2
        >>> duration *= sludge
        >>> time.sleep(duration / black._speed)

                LUKASZ
        HERE IS A CAKE.  
        WE WANT TO CUT THE BIGGEST PIECE.
        ME AND ETHAN TAKE TURNS CUTTING PIECES.
        WATCH ME.  I AM RED.  I CUT FIRST.
        >>> property_diff(black, black.root.territory_mc, 
        ...     'currentLabel', 'show')
        >>> property_diff(black, black.root['turn_mc'], 
        ...     'currentLabel', 'black')
        >>> property_diff(ethan, ethan.root['turn_mc'], 
        ...     'currentLabel', 'black')

    LUKASZ SEES COMMENT,
        >>> property_diff(black, black.root.comment_mc,
        ...     'currentLabel', 'comment')
        >>> not black.root.comment_mc._txt.text.startswith('_txt')
        True

    WHICH STARTS ON FIRST LINE.
        >>> not black.root.comment_mc._txt.text.startswith('\r')
        True
        >>> not black.root.comment_mc._txt.text.startswith('\n')
        True
        >>> not black.root.comment_mc._txt.text.startswith(' ')
        True
        >>> not black.root.comment_mc._txt.text.endswith('\r')
        True
        >>> not black.root.comment_mc._txt.text.endswith('\n')
        True
        >>> not black.root.comment_mc._txt.text.endswith(' ')
        True

    LUKASZ CLOSES COMMENT.
        >>> mouse_down_and_sleep(black, black.root.comment_mc.none_mc, 1.0 / black._speed)
        >>> property_diff(black, black.root.comment_mc,
        ...     'currentLabel', 'none')

    ONCE PER SECOND, RED AND BLUE CUT THE CAKE.
        >>> black.pb()
        ,,XO,
        ,,XO,
        ,,XO,
        ,,XO,
        ,,XO,
        >>> ethan.pb()
        ,,XO,
        ,,XO,
        ,,XO,
        ,,XO,
        ,,XO,
        >>> property_diff(black, black.root._2_1_mc.territory_mc,
        ...     'currentLabel', 'black')
        >>> property_diff(black, black.root._2_4_mc.territory_mc,
        ...     'currentLabel', 'white')

                LUKASZ
        THE CAKE IS CUT.
        WE ARE RED.
        DID WE WIN?

                LUKASZ
        AT BOTTOM RIGHT, CLICK THE TEA CUP.
        >>> property_diff(black, black.root.pass_white_mc, 'currentLabel', 'pass')

    LUKASZ CLICKS TEA.
        >>> mouse_down_and_sleep(black, black.root.pass_mc, 1.0 / black._speed)
        
    LUKASZ WINS BY FIVE PIECES OF CAKE!
        >>> property_diff(black, black.root.game_over_mc, 'currentLabel', 'win')
        >>> property_diff(black, black.root.game_over_mc.score_mc.territory_txt, 'text', '12')

                LUKASZ
        AT BOTTOM RIGHT, CLICK THE ARROW TO RETURN.

    LUKASZ CLICKS ARROW TO RETURN TO TABLES.
        >>> mouse_down_and_sleep(black, black.root.lobby_mc.enter_mc, 1.0 / black._speed)

    INT. TABLES WITH CAKES
        >>> property_diff(black, black.root, 'currentLabel', 'lobby')
        >>> property_diff(black, black.root.game_over_mc, 'currentLabel', 'none')

    LUKASZ SEES NO COMMENT.
        >>> black.root.comment_mc._txt.text.startswith('_txt')
        True

                LUKASZ
        WE ATE THE FIRST CAKE.
    '''

def beginner_count_example():
    '''Lukasz selects second 5x5 cake and counts the pieces of cake.
        >>> code_unit.inline_examples(
        ...     ethan_lukasz_begin_example.__doc__, 
        ...     locals(), globals(), 
        ...     verify_examples = False)

    INT. TABLES WITH CAKES
        >>> property_diff(lukasz, lukasz.root, 'currentLabel', 'lobby')
    
                LUKASZ
        ON TOP TABLE, CLICK SECOND CAKE.

    LUKASZ CLICKS SECOND CAKE.
        >>> mouse_down_and_sleep(lukasz, lukasz.root.lobby_mc._00_mc.capture_5_5_mc,
        ...     1.0 / lukasz._speed)

    INT. TABLE - CONTINUOUS

    5X5 CAKE ON TABLE.  THERE ARE NO SETUP OPTIONS.
        >>> property_diff(lukasz, lukasz.root, 'currentLabel', '_5_5')
        >>> property_diff(lukasz, lukasz.root.game_over_mc, 
        ...     'currentLabel', 'preview')

                ETHAN
        THIS TIME, I WILL EAT MORE!
            
                BUTTON
        LET'S EAT

    LUKASZ CLICKS ON BUTTON.
        >>> mouse_down_and_sleep(lukasz, lukasz.root.game_over_mc.start_mc, 1.0 / lukasz._speed)

    SERVER THEN DISPATCH MOUSE DOWN PLAY_SGF_MC.  
    XXX CLIENT AUTOMATICALLY STARTS THE SCRIPT.
    XXX QUITE SLOW.  WHY?
        >>> time.sleep(180.0 / lukasz._speed)

    #- ETHAN SECRETLY STARTS THE SCRIPT.
    #-     >>> play_lesson(1, ethan, lukasz, mouse_down_and_sleep, 1.0)
        
    RED AND BLUE CUT MOST OF THE CAKE.
        >>> lukasz.pb()
        ,,,,,
        XXXX,
        ,,,X,
        OOOOO
        ,,,,,
        >>> ethan.pb()
        ,,,,,
        XXXX,
        ,,,X,
        OOOOO
        ,,,,,

                LUKASZ
        THE CAKE IS ALMOST CUT.
        WHERE CAN I PLAY TO CUT A BIG PIECE?

                [SELECT SCENE]
        LUKASZ CLICKS ON 1,4.
        LUKASZ CLICKS ON 2,4.
        LUKASZ CLICKS ANYWHERE ELSE.

    LUKASZ CLICKS ANYWHERE ELSE
        >>> mouse_down_and_sleep(lukasz, lukasz.root._0_3_mc, 1.0 / lukasz._speed)
        >>> mouse_down_and_sleep(lukasz, lukasz.root._0_3_mc, 1.0 / lukasz._speed)

    GNUGO ENCROACHES.
        >>> time.sleep(1.0)
        >>> lukasz.pb()
        ,,,X,
        XXXX,
        ,,,XO
        OOOOO
        ,,,,,

                LUKASZ
        I CAN EAT MORE THAN THAT.
        LET'S TRY AGAIN.

    [RETURN TO LAST "SELECT SCENE".]

    LUKASZ CLICKS ON 1,4

                LUKASZ
        I CAN EAT MORE THAN THAT.
        LET'S TRY AGAIN.

    [RETURN TO LAST "SELECT SCENE".]

    LUKASZ CLICKS ON 2,4

                LUKASZ
        GREAT!  
        WE ATE THE BIGGEST PIECE.

                LUKASZ
        WE FINISHED EATING,
        SO CLICK ON THE TEA CUP.

    LUKASZ CLICKS THE TEA CUP.

    LUKASZ WINS!

                LUKASZ
        AT BOTTOM RIGHT, 
        CLICK THE ARROW TO RETURN.

    LUKASZ CLICKS ARROW TO RETURN TO TABLES.
        >>> mouse_down_and_sleep(lukasz, lukasz.root.lobby_mc.enter_mc, 1.0 / lukasz._speed)

    INT. TABLES WITH CAKES
        >>> property_diff(lukasz, lukasz.root, 'currentLabel', 'lobby')

                LUKASZ
        WE ATE THE SECOND CAKE.
    '''


def beginner_liberty_example():
    '''Lukasz selects third 3x3 cake and watches liberties and captures, 
    and then makes a capture.
        >>> code_unit.inline_examples(
        ...     ethan_lukasz_begin_example.__doc__, 
        ...     locals(), globals(), 
        ...     verify_examples = False)

    INT. TABLES WITH CAKES
        >>> property_diff(lukasz, lukasz.root, 'currentLabel', 'lobby')

                LUKASZ
        TO GET A FORK,
        CLICK THIRD CAKE.

        >>> property_diff(lukasz, lukasz.root.option_mc.block_mc, 
        ...     'currentLabel', 'none')


    LUKASZ CLICKS THIRD CAKE.
        >>> mouse_down_and_sleep(lukasz, lukasz.root.lobby_mc._00_mc.dominate_3_3_mc,
        ...     1.0 / lukasz._speed)

    INT. TABLE - CONTINUOUS

    3X3 CAKE ON TABLE.  THERE ARE NO SETUP OPTIONS.
        >>> property_diff(lukasz, lukasz.root, 'currentLabel', '_3_3')
        >>> property_diff(lukasz, lukasz.root.game_over_mc, 
        ...     'currentLabel', 'preview')

                ETHAN
        NOW I HAVE A FORK,
        SO I WILL EAT YOUR CAKE!
        >>> property_diff(ethan, ethan.root.option_mc.block_mc, 
        ...     'currentLabel', 'none')
            
    LUKASZ RECEIVES A FORK AND PLATE.
        >>> property_diff(lukasz, lukasz.root.option_mc.block_mc, 
        ...     'currentLabel', 'show')
        
                LUKASZ
        BUT WITH YOUR FORK,
        YOU CAN EAT BLUE CAKE!
            
                BUTTON
        LET'S EAT

    LUKASZ CLICKS ON BUTTON.
        >>> mouse_down_and_sleep(lukasz, lukasz.root.game_over_mc.start_mc, 1.0 / lukasz._speed)

    SERVER THEN DISPATCH MOUSE DOWN PLAY_SGF_MC.  
    MASTER AUTOMATICALLY STARTS LESSON.
    XXX QUITE SLOW.  WHY?
        >>> time.sleep(50.0 / lukasz._speed)

    #ETHAN SECRETLY STARTS THE SCRIPT.
    #    >>> play_lesson(2, ethan, lukasz, mouse_down_and_sleep, 1.0)
        
    RED CAPTURES BLUE.  ONLY A FEW PIECES LEFT.
        >>> lukasz.pb()
        XX,
        ,XX
        O,,
        >>> ethan.pb()
        XX,
        ,XX
        O,,

                LUKASZ
        BLUE HAS NO CHANCE.  
        EAT HIS CAKE!

    LUKASZ EATS AND ETHAN CUTS, UNTIL ETHAN CANNOT CUT ANYWHERE.

                LUKASZ
        BLUE CANNOT CUT ANYWHERE.
        ONCE YOU GET TWO CANDLES,
        YOUR SLICE CANNOT BE EATEN.

                LUKASZ
        BLUE HAS NO CHANCE.  
        EAT HIS CAKE!

                LUKASZ
        GREAT!  
        WE ATE THE WHOLE CAKE.

                LUKASZ
        WE FINISHED EATING,
        SO CLICK ON THE TEA CUP.

    LUKASZ CLICKS THE TEA CUP.

    LUKASZ WINS!

                ETHAN
        NEXT TIME, DON'T BE GREEDY!
        I CAN EAT YOUR CAKE, TOO.

                LUKASZ
        AT BOTTOM RIGHT, 
        CLICK THE ARROW TO RETURN.

    LUKASZ CLICKS ARROW TO RETURN TO TABLES.
        >>> mouse_down_and_sleep(lukasz, lukasz.root.lobby_mc.enter_mc, 1.0 / lukasz._speed)

    INT. TABLES WITH CAKES
        >>> property_diff(lukasz, lukasz.root, 'currentLabel', 'lobby')

                LUKASZ
        WE ATE THE THIRD CAKE.
    '''


def beginner_profit_example():
    '''Lukasz selects fifth 5x5 cake and watches liberties and captures, 
    and then makes a capture.
        >>> code_unit.inline_examples(
        ...     ethan_lukasz_begin_example.__doc__, 
        ...     locals(), globals(), 
        ...     verify_examples = False)

    INT. TABLES WITH CAKES
        >>> property_diff(lukasz, lukasz.root, 'currentLabel', 'lobby')

                LUKASZ
        TO GET CHOCOLATE,
        CLICK FIFTH CAKE.
        >>> property_diff(lukasz, lukasz.root.profit_mc, 
        ...     'currentLabel', 'none')
        >>> property_diff(lukasz, lukasz.root.defend_mc, 
        ...     'currentLabel', 'none')
        >>> property_diff(lukasz, lukasz.root.attack_mc, 
        ...     'currentLabel', 'none')

    LUKASZ CLICKS FIFTH CAKE.
        >>> mouse_down_and_sleep(lukasz, lukasz.root.score_5_5_mc,
        ...     1.0 / lukasz._speed)

    WE WAIT A BIT FOR CLIENT TO FINISH.  TODO: Why so slow?
        >>> time.sleep(3.0 / lukasz._speed)

    INT. TABLE - CONTINUOUS

    5X5 CAKE ON TABLE.  THERE ARE NO SETUP OPTIONS.
        >>> property_diff(lukasz, lukasz.root, 'currentLabel', '_5_5')
        >>> property_diff(lukasz, lukasz.root.game_over_mc, 
        ...     'currentLabel', 'preview')
        >>> property_diff(ethan, ethan.root.profit_mc, 
        ...     'currentLabel', 'none')
        >>> property_diff(ethan, ethan.root.defend_mc, 
        ...     'currentLabel', 'none')
        >>> property_diff(ethan, ethan.root.attack_mc, 
        ...     'currentLabel', 'none')
            
    LUKASZ RECEIVES CHOCOLATE.
        >>> property_diff(lukasz, lukasz.root.profit_mc, 
        ...     'currentLabel', 'show')
        
                LUKASZ
        YOU CAN SPRINKLE CHOCOLATE
        ON A BIG PIECE OF CAKE.
        THE CENTER IS THE SWEETEST CAKE.
            
                BUTTON
        LET'S EAT

    LUKASZ CLICKS ON BUTTON.
        >>> mouse_down_and_sleep(lukasz, lukasz.root.game_over_mc.start_mc, 1.0 / lukasz._speed)

    SERVER THEN DISPATCH MOUSE DOWN PLAY_SGF_MC.  
    MASTER AUTOMATICALLY STARTS LESSON.
    XXX QUITE SLOW.  WHY?
        >>> time.sleep(40.0 / lukasz._speed)

    #- ETHAN SECRETLY STARTS THE SCRIPT.
    #-     >>> play_lesson(4, ethan, lukasz, mouse_down_and_sleep, 1.0)
        
    RED CAPTURES BLUE.  ONLY A FEW PIECES LEFT.
        >>> lukasz.pb()
        ,,,,,
        ,,,,,
        ,,X,,
        ,O,,,
        ,,,,,
        >>> ethan.pb()
        ,,,,,
        ,,,,,
        ,,X,,
        ,O,,,
        ,,,,,

    LUKASZ CUTS THE CAKE.

                LUKASZ
        WE FINISHED EATING,
        SO CLICK ON THE TEA CUP.

    LUKASZ CLICKS THE TEA CUP.

    LUKASZ WINS!

                ETHAN
        NEXT TIME, DON'T BE GREEDY!
        I CAN EAT YOUR CAKE, TOO.

                LUKASZ
        AT BOTTOM RIGHT, 
        CLICK THE ARROW TO RETURN.

    LUKASZ CLICKS ARROW TO RETURN TO TABLES.
        >>> mouse_down_and_sleep(lukasz, lukasz.root.lobby_mc.enter_mc, 1.0 / lukasz._speed)

    INT. TABLES WITH CAKES
        >>> property_diff(lukasz, lukasz.root, 'currentLabel', 'lobby')

                LUKASZ
        WE ATE THE FIFTH CAKE.
    '''

def beginner_dead_example():
    '''Lukasz selects SIXTH (5) _3_3 cake, gets KISS to see dead.
        >>> code_unit.inline_examples(
        ...     ethan_lukasz_begin_example.__doc__, 
        ...     locals(), globals(), 
        ...     verify_examples = False)

    INT. TABLES WITH CAKES
        >>> property_diff(lukasz, lukasz.root, 'currentLabel', 'lobby')

                LUKASZ
        TO GET KISS,
        CLICK SIXTH CAKE.
        >>> property_diff(lukasz, lukasz.root.dead_mc, 
        ...     'currentLabel', 'none')

    LUKASZ CLICKS SIXTH CAKE.
        >>> mouse_down_and_sleep(lukasz, lukasz.root.lobby_mc._00_mc.extra_stone_7_7_mc,
        ...     1.0 / lukasz._speed)
        >>> time.sleep(1.0 / lukasz._speed)

    INT. TABLE - CONTINUOUS

    5X5 CAKE ON TABLE.  THERE ARE NO SETUP OPTIONS.
        >>> property_diff(lukasz, lukasz.root, 'currentLabel', '_3_3')
        >>> property_diff(lukasz, lukasz.root.game_over_mc, 
        ...     'currentLabel', 'preview')
        >>> property_diff(ethan, ethan.root.dead_mc, 
        ...     'currentLabel', 'none')
            
    LUKASZ RECEIVES KISS.
        >>> property_diff(lukasz, lukasz.root.dead_mc, 
        ...     'currentLabel', 'show')
        >>> property_diff(lukasz, lukasz.root.territory_mc, 
        ...     'currentLabel', 'show')
        
                LUKASZ
        KISS SHOWS A PIECE THAT 
        WILL GET EATEN.
        EAT WELL!
            
                BUTTON
        LET'S EAT

    LUKASZ CLICKS ON BUTTON.
        >>> mouse_down_and_sleep(lukasz, lukasz.root.game_over_mc.start_mc, 1.0 / lukasz._speed)

    SERVER THEN DISPATCH MOUSE DOWN PLAY_SGF_MC.  
    MASTER AUTOMATICALLY STARTS LESSON.
    XXX QUITE SLOW.  WHY?
        >>> time.sleep(10.0 / lukasz._speed)

    #- ETHAN SECRETLY STARTS THE SCRIPT.
    #-     >>> play_lesson(5, ethan, lukasz, mouse_down_and_sleep, 1.0)
        >>> lukasz.pb()
        ,,,
        ,,,
        ,,,
        >>> ethan.pb()
        ,,,
        ,,,
        ,,,

    RED CAPTURES BLUE.  ONLY A FEW PIECES LEFT.
        >>> mouse_down_and_sleep(lukasz, lukasz.root._1_1_mc, 1.0 / lukasz._speed)
        >>> mouse_down_and_sleep(lukasz, lukasz.root._1_1_mc, 1.0 / lukasz._speed)
        >>> mouse_down_and_sleep(ethan, ethan.root._0_0_mc, 1.0 / ethan._speed)
        >>> mouse_down_and_sleep(lukasz, lukasz.root._0_1_mc, 1.0 / lukasz._speed)
        >>> mouse_down_and_sleep(lukasz, lukasz.root._0_1_mc, 1.0 / lukasz._speed)
        >>> mouse_down_and_sleep(ethan, ethan.root._2_2_mc, 1.0 / ethan._speed)
        >>> property_diff(lukasz, lukasz.root._0_0_mc.territory_mc, 
        ...     'currentLabel', 'white_dead')

    LUKASZ CUTS THE CAKE.

                LUKASZ
        WE FINISHED EATING,
        SO CLICK ON THE TEA CUP.

    LUKASZ CLICKS THE TEA CUP.

    LUKASZ WINS!

                ETHAN
        NEXT TIME, DON'T BE GREEDY!
        I CAN EAT YOUR CAKE, TOO.

                LUKASZ
        AT BOTTOM RIGHT, 
        CLICK THE ARROW TO RETURN.

    LUKASZ CLICKS ARROW TO RETURN TO TABLES.
        >>> mouse_down_and_sleep(lukasz, lukasz.root.lobby_mc.enter_mc, 1.0 / lukasz._speed)

    INT. TABLES WITH CAKES
        >>> property_diff(lukasz, lukasz.root, 'currentLabel', 'lobby')

                LUKASZ
        WE ATE THE SIXTH CAKE.
    '''


def beginner_connect_example():
    '''Lukasz selects seventh cake (index 6) sees a peep and connects.
        >>> code_unit.inline_examples(
        ...     ethan_lukasz_begin_example.__doc__, 
        ...     locals(), globals(), 
        ...     verify_examples = False)

    INT. TABLES WITH CAKES
        >>> property_diff(lukasz, lukasz.root, 'currentLabel', 'lobby')
    
                LUKASZ
        ON TOP TABLE, CLICK SEVENTH CAKE.

    LUKASZ CLICKS SEVENTH CAKE.
        >>> mouse_down_and_sleep(lukasz, lukasz.root.lobby_mc._00_mc.extra_stone_7_7_2_mc,
        ...     wait / lukasz._speed)

    INT. TABLE - CONTINUOUS

    5X5 CAKE ON TABLE.  THERE ARE NO SETUP OPTIONS.
        >>> property_diff(lukasz, lukasz.root, 'currentLabel', '_5_5')
        >>> property_diff(lukasz, lukasz.root.game_over_mc, 
        ...     'currentLabel', 'preview')

                ETHAN
        THIS TIME, I WILL EAT MORE!
            
                BUTTON
        LET'S EAT

    LUKASZ CLICKS ON BUTTON.
        >>> mouse_down_and_sleep(lukasz, lukasz.root.game_over_mc.start_mc, wait / lukasz._speed)

    SERVER THEN DISPATCH MOUSE DOWN PLAY_SGF_MC.  
    XXX MASTER AUTOMATICALLY STARTS THE SCRIPT.
        >>> clicks = (2 * 5) + 5
        >>> comments = 6
        >>> duration = wait * (clicks + comments)

                LUKASZ
        PROTOTYPE IS QUITE SLOW.  SORRY.
        >>> sludge = 2
        >>> duration *= sludge
        >>> time.sleep(duration / lukasz._speed)

    LUKASZ SEES LIBERTY AND DEAD AND PROFIT, ATTACK, DEFEND.
        >>> property_diff(lukasz, lukasz.root.option_mc.block_mc, 'currentLabel', 'show')
        >>> property_diff(lukasz, lukasz.root.territory_mc, 'currentLabel', 'show')
        >>> property_diff(lukasz, lukasz.root.dead_mc, 'currentLabel', 'show')
        >>> property_diff(lukasz, lukasz.root.profit_mc, 'currentLabel', 'show')
        >>> property_diff(lukasz, lukasz.root.attack_mc, 'currentLabel', 'show')
        >>> property_diff(lukasz, lukasz.root.defend_mc, 'currentLabel', 'show')

    RED AND BLUE CUT MOST OF THE CAKE.
        >>> lukasz.pb()
        ,,X,,
        OOOOO
        XX,XX
        ,,,,,
        ,,,,,
        >>> ethan.pb()
        ,,X,,
        OOOOO
        XX,XX
        ,,,,,
        ,,,,,

    LUKASZ SEES PEEP FROM ETHAN.
    >>> property_diff(lukasz, lukasz.root.formation_peep_mc.rotate_180_mc.response_mc, 
    ...     'currentLabel', 'response')

                LUKASZ
        THE CAKE IS ALMOST CUT.
        WHERE CAN I PLAY TO CUT A BIG PIECE?

                [SELECT SCENE]
        LUKASZ CLICKS ON 2,2.
        LUKASZ CLICKS ANYWHERE ELSE.

    LUKASZ CLICKS ANYWHERE ELSE
        >>> mouse_down_and_sleep(lukasz, lukasz.root._3_2_mc, wait / lukasz._speed)
        >>> mouse_down_and_sleep(lukasz, lukasz.root._3_2_mc, wait / lukasz._speed)

    GNUGO ENCROACHES.
        >>> ## time.sleep(wait)
        >>> lukasz.pb()
        ,,X,,
        OOOOO
        XXOXX
        ,,X,,
        ,,,,,

                LUKASZ
        BLUE WILL EAT ME!
        LET'S TRY AGAIN.

    [RETURN TO LAST "SELECT SCENE".]

    LUKASZ CLICKS ON 2,2

                LUKASZ
        GREAT!  
        WE ATE THE BIGGEST PIECE.

                LUKASZ
        WE FINISHED EATING,
        SO CLICK ON THE TEA CUP.

    LUKASZ CLICKS THE TEA CUP.

    LUKASZ WINS!

                LUKASZ
        AT BOTTOM RIGHT, 
        CLICK THE ARROW TO RETURN.

    LUKASZ CLICKS ARROW TO RETURN TO TABLES.
        >>> mouse_down_and_sleep(lukasz, lukasz.root.lobby_mc.enter_mc, wait / lukasz._speed)

    INT. TABLES WITH CAKES
        >>> property_diff(lukasz, lukasz.root, 'currentLabel', 'lobby')

                LUKASZ
        WE ATE THE SEVENTH CAKE.
    '''


def beginner_connect_reverse_peep_example():
    '''Lukasz selects eighth cake (index 7) sees a peep and connects.
        >>> code_unit.inline_examples(
        ...     ethan_lukasz_begin_example.__doc__, 
        ...     locals(), globals(), 
        ...     verify_examples = False)

    INT. TABLES WITH CAKES
        >>> property_diff(lukasz, lukasz.root, 'currentLabel', 'lobby')
    
                LUKASZ
        ON TOP TABLE, CLICK EIGHTH CAKE.

    LUKASZ CLICKS EIGHTH CAKE.
        >>> mouse_down_and_sleep(lukasz, lukasz.root.lobby_mc._00_mc.extra_stone_9_9_mc,
        ...     wait / lukasz._speed)

    INT. TABLE - CONTINUOUS

    5X5 CAKE ON TABLE.  THERE ARE NO SETUP OPTIONS.
        >>> property_diff(lukasz, lukasz.root, 'currentLabel', '_5_5')
        >>> property_diff(lukasz, lukasz.root.game_over_mc, 
        ...     'currentLabel', 'preview')

                ETHAN
        THIS TIME, I WILL EAT MORE!
            
                BUTTON
        LET'S EAT

    LUKASZ CLICKS ON BUTTON.
        >>> mouse_down_and_sleep(lukasz, lukasz.root.game_over_mc.start_mc, wait / lukasz._speed)

    SERVER THEN DISPATCH MOUSE DOWN PLAY_SGF_MC.  
    XXX CLIENT AUTOMATICALLY STARTS THE SCRIPT.
        >>> clicks = (2 * 5) + 5
        >>> comments = 6
        >>> duration = wait * (clicks + comments)

                LUKASZ
        PROTOTYPE IS QUITE SLOW.  SORRY.
        >>> sludge = 2
        >>> duration *= sludge
        >>> time.sleep(duration / lukasz._speed)

    LUKASZ SEES LIBERTY AND DEAD AND PROFIT, ATTACK, DEFEND.
        >>> property_diff(lukasz, lukasz.root.option_mc.block_mc, 'currentLabel', 'show')
        >>> property_diff(lukasz, lukasz.root.territory_mc, 'currentLabel', 'show')
        >>> property_diff(lukasz, lukasz.root.dead_mc, 'currentLabel', 'show')
        >>> property_diff(lukasz, lukasz.root.profit_mc, 'currentLabel', 'show')
        >>> property_diff(lukasz, lukasz.root.attack_mc, 'currentLabel', 'show')
        >>> property_diff(lukasz, lukasz.root.defend_mc, 'currentLabel', 'show')

    RED AND BLUE CUT MOST OF THE CAKE.
        >>> lukasz.pb()
        ,,XO,
        ,O,O,
        XXXO,
        ,,XO,
        ,,XO,
        >>> ethan.pb()
        ,,XO,
        ,O,O,
        XXXO,
        ,,XO,
        ,,XO,

    LUKASZ SEES PEEP FROM ETHAN.
        >>> property_diff(lukasz, lukasz.root.formation_peep_mc.rotate_90_mc.response_mc, 
        ...     'currentLabel', 'response')
    >>> property_diff(lukasz, lukasz.root.formation_peep_mc, 
    ...     'x', lukasz.root['_1_1_mc'].x)
    >>> property_diff(lukasz, lukasz.root.formation_peep_mc, 
    ...     'y', lukasz.root['_1_1_mc'].y)

                LUKASZ
        THE CAKE IS ALMOST CUT.
        WHERE CAN I PLAY TO CUT A BIG PIECE?

                [SELECT SCENE]
        LUKASZ CLICKS ON 1,2.
        LUKASZ CLICKS ANYWHERE ELSE.

    LUKASZ CLICKS ANYWHERE ELSE
        >>> mouse_down_and_sleep(lukasz, lukasz.root._0_1_mc, wait / lukasz._speed)
        >>> mouse_down_and_sleep(lukasz, lukasz.root._0_1_mc, wait / lukasz._speed)

    GNUGO CONNECTS.
        >>> lukasz.pb()
        ,XXO,
        ,OOO,
        XXXO,
        ,,XO,
        ,,XO,

                LUKASZ
        BLUE WILL EAT ME!
        LET'S TRY AGAIN.

    [RETURN TO LAST "SELECT SCENE".]

    LUKASZ CLICKS ON 1,2

                LUKASZ
        GREAT!  
        WE ATE THE BIGGEST PIECE.

                LUKASZ
        WE FINISHED EATING,
        SO CLICK ON THE TEA CUP.

    LUKASZ CLICKS THE TEA CUP.

    LUKASZ WINS!

                LUKASZ
        AT BOTTOM RIGHT, 
        CLICK THE ARROW TO RETURN.

    LUKASZ CLICKS ARROW TO RETURN TO TABLES.
        >>> mouse_down_and_sleep(lukasz, lukasz.root.lobby_mc.enter_mc, wait / lukasz._speed)

    INT. TABLES WITH CAKES
        >>> property_diff(lukasz, lukasz.root, 'currentLabel', 'lobby')

                LUKASZ
        WE ATE THE EIGHTH CAKE.
    '''



def beginner_comment_example():
    r'''LUKASZ PLAYS PROFIT LESSON, FIFTH LESSON (INDEX 4), SEES COMMENT.  
    IN NEXT LESSON, COMMENT IS CLEAR.
        >>> code_unit.inline_examples(
        ...     ethan_lukasz_begin_example.__doc__, 
        ...     locals(), globals(), 
        ...     verify_examples = False)
        >>> wait = 3.0

    INT. TABLES WITH CAKES
        >>> property_diff(lukasz, lukasz.root, 'currentLabel', 'lobby')

                ETHAN
        ON THE FIRST TABLE,
        CLICK THE FIRST CAKE.

    LUKASZ SEES NO COMMENT.
        >>> property_diff(lukasz, lukasz.root.comment_mc,
        ...     'currentLabel', 'none')

    LUKASZ CLICKS FIRST CAKE.  IT FLASHES UNTIL RECEIVED.
        >>> mouse_down_and_sleep(lukasz, lukasz.root.score_5_5_mc,
        ...     wait / lukasz._speed)
        >>> property_diff(lukasz, lukasz.root.score_5_5_mc, 
        ...     'currentLabel', 'none')

    WE WAIT A BIT FOR CLIENT TO FINISH.  WHY SO SLOW?
        >>> time.sleep(wait / lukasz._speed)

    INT. TABLE - CONTINUOUS

    5X5 CAKE ON TABLE.  THERE ARE NO SETUP OPTIONS.
        >>> property_diff(lukasz, lukasz.root, 'currentLabel', '_5_5')
        >>> property_diff(lukasz, lukasz.root.game_over_mc, 
        ...     'currentLabel', 'preview')

    XXX SERVER REPLIES NAME OF SGF FILE TO MASTER.
        >>> property_diff(lukasz, lukasz.root.sgf_file_txt, 
        ...     'text', 'sgf/beginner/profit_5_5.sgf')

                LUKASZ
        RED
        >>> property_diff(lukasz, lukasz.root['turn_mc']['black_user_txt'], 
        ...     'text', 'lukasz')
        >>> property_diff(ethan, ethan.root['turn_mc']['black_user_txt'], 
        ...     'text', 'lukasz')

                ETHAN
        BLUE
        >>> property_diff(lukasz, lukasz.root['turn_mc']['white_user_txt'], 
        ...     'text', 'ethan')
        >>> property_diff(ethan, ethan.root['turn_mc']['white_user_txt'], 
        ...     'text', 'ethan')
        
                BUTTON
        LET'S EAT
        
    LUKASZ CLICKS ON BUTTON.
        >>> mouse_down_and_sleep(lukasz, lukasz.root.game_over_mc.start_mc, wait / lukasz._speed)
        >>> board_diff(ethan, ethan.root._0_0_mc, 
        ...     'currentLabel', 'empty_white')

    SERVER THEN DISPATCH MOUSE DOWN PLAY_SGF_MC.  
    XXX MASTER AUTOMATICALLY STARTS THE SCRIPT.
    XXX QUITE SLOW.  WHY?
        >>> time.sleep(wait * 30.0 / lukasz._speed)

                LUKASZ
        AT BOTTOM RIGHT, 
        CLICK THE ARROW TO RETURN.

    LUKASZ SEES COMMENT,
        >>> property_diff(lukasz, lukasz.root.comment_mc,
        ...     'currentLabel', 'comment')
        >>> not lukasz.root.comment_mc._txt.text.startswith('_txt')
        True

    WHICH STARTS ON FIRST LINE.
        >>> not lukasz.root.comment_mc._txt.text.startswith('\r')
        True
        >>> not lukasz.root.comment_mc._txt.text.startswith('\n')
        True
        >>> not lukasz.root.comment_mc._txt.text.startswith(' ')
        True
        >>> not lukasz.root.comment_mc._txt.text.endswith('\r')
        True
        >>> not lukasz.root.comment_mc._txt.text.endswith('\n')
        True
        >>> not lukasz.root.comment_mc._txt.text.endswith(' ')
        True

    LUKASZ CLICKS ARROW TO RETURN TO TABLES.
        >>> mouse_down_and_sleep(lukasz, lukasz.root.lobby_mc.enter_mc, wait / lukasz._speed)


    INT. TABLES WITH CAKES
        >>> property_diff(lukasz, lukasz.root, 'currentLabel', 'lobby')

                ETHAN
        ON THE FIRST TABLE,
        CLICK THE FIRST CAKE.

    LUKASZ SEES NO COMMENT.
        >>> property_diff(lukasz, lukasz.root.comment_mc,
        ...     'currentLabel', 'none')

    LUKASZ CLICKS FIRST CAKE.  IT FLASHES UNTIL RECEIVED.
        >>> mouse_down_and_sleep(lukasz, lukasz.root.score_5_5_mc,
        ...     wait / lukasz._speed)
        >>> property_diff(lukasz, lukasz.root.score_5_5_mc, 
        ...     'currentLabel', 'none')

    WE WAIT A BIT FOR CLIENT TO FINISH.  WHY SO SLOW?
        >>> time.sleep(wait / lukasz._speed)

    INT. TABLE - CONTINUOUS

    5X5 CAKE ON TABLE.  THERE ARE NO SETUP OPTIONS.
        >>> property_diff(lukasz, lukasz.root, 'currentLabel', '_5_5')
        >>> property_diff(lukasz, lukasz.root.game_over_mc, 
        ...     'currentLabel', 'preview')

    XXX SERVER REPLIES NAME OF SGF FILE TO MASTER.
        >>> property_diff(lukasz, lukasz.root.sgf_file_txt, 
        ...     'text', 'sgf/beginner/profit_5_5.sgf')

                LUKASZ
        RED
        >>> property_diff(lukasz, lukasz.root['turn_mc']['black_user_txt'], 
        ...     'text', 'lukasz')
        >>> property_diff(ethan, ethan.root['turn_mc']['black_user_txt'], 
        ...     'text', 'lukasz')

                ETHAN
        BLUE
        >>> property_diff(lukasz, lukasz.root['turn_mc']['white_user_txt'], 
        ...     'text', 'ethan')
        >>> property_diff(ethan, ethan.root['turn_mc']['white_user_txt'], 
        ...     'text', 'ethan')
        
                BUTTON
        LET'S EAT
        
    LUKASZ CLICKS ON BUTTON.
        >>> mouse_down_and_sleep(lukasz, lukasz.root.game_over_mc.start_mc, wait / lukasz._speed)
        >>> board_diff(ethan, ethan.root._0_0_mc, 
        ...     'currentLabel', 'empty_white')

    WAIT.  LUKASZ SEES COMMENT.
        >>> time.sleep(wait / lukasz._speed)
        >>> time.sleep(wait / lukasz._speed)
        >>> property_diff(lukasz, lukasz.root.comment_mc,
        ...     'currentLabel', 'comment')

    LUKASZ CLOSES COMMENT.
        >>> mouse_down_and_sleep(lukasz, lukasz.root.comment_mc.none_mc, wait / lukasz._speed)
        >>> property_diff(lukasz, lukasz.root.comment_mc,
        ...     'currentLabel', 'none')
    '''


def beginner_extra_stone_example():
    '''Begin and play ninth lesson (index 8), where player gets all formations and extra stone.
    >>> code_unit.inline_examples(
    ...     ethan_lukasz_begin_example.__doc__, 
    ...     locals(), globals(), 
    ...     verify_examples = False)

    Lukasz starts with no extra stone.
    >>> property_diff(lukasz, lukasz.root.extra_stone_gift_mc, 'currentLabel', '_0')
    >>> start_and_play_lesson(8, ethan, lukasz, mouse_down_and_sleep, 2.0)
    >>> mouse_down_and_sleep(lukasz, lukasz.root._1_1_mc, 1.0 / lukasz._speed)
    >>> mouse_down_and_sleep(lukasz, lukasz.root._1_1_mc, 1.0 / lukasz._speed)

    Lukasz sees his stone and white's.
    >>> lukasz.pb()
    ,,,,,
    ,X,,,
    ,,O,,
    ,,,,,
    ,,,,,

    Lukasz has extra stone.
    >>> property_diff(lukasz, lukasz.root.extra_stone_gift_mc, 'currentLabel', '_1')
    '''


def start_score_example():
    '''Lukasz and ethan make a move, see the score, then start a new game.
    Lukasz sees an even score.
        >>> code_unit.inline_examples(
        ...     ethan_lukasz_begin_example.__doc__, 
        ...     locals(), globals(), 
        ...     verify_examples = False)
    >>> mouse_down_and_sleep(lukasz, lukasz.root.lobby_mc._00_mc.dominate_3_3_mc, 1.0 / lukasz._speed)
    >>> mouse_down_and_sleep(lukasz, lukasz.root.game_over_mc.start_mc, 1.0 / lukasz._speed)
    >>> property_diff(lukasz, lukasz.root.score_mc, 'currentLabel', '_0')
    >>> property_diff(lukasz, lukasz.root.score_mc.marker_mc, 'currentLabel', 'neutral')
    >>> property_diff(lukasz, lukasz.root.score_mc.marker_mc.change_txt, 'text', '0')
    >>> property_diff(lukasz, lukasz.root.score_mc.marker_mc.capture_mc, 'currentLabel', '_0')
    >>> mouse_down_and_sleep(lukasz, lukasz.root._1_1_mc, 1.0 / lukasz._speed)
    >>> mouse_down_and_sleep(lukasz, lukasz.root._1_1_mc, 1.0 / lukasz._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root._0_0_mc, 1.0 / ethan._speed)
    >>> property_diff(lukasz, lukasz.root.score_mc, 'currentLabel', '_9')
    >>> mouse_down_and_sleep(lukasz, lukasz.root.lobby_mc.enter_mc, 1.0 / lukasz._speed)
    >>> mouse_down_and_sleep(lukasz, lukasz.root.lobby_mc._00_mc.dominate_3_3_mc, 1.0 / lukasz._speed)
    >>> property_diff(lukasz, lukasz.root.score_mc, 'currentLabel', '_0')
    >>> property_diff(lukasz, lukasz.root.score_mc.marker_mc, 'currentLabel', 'neutral')
    >>> property_diff(lukasz, lukasz.root.score_mc.marker_mc.change_txt, 'text', '0')
    >>> property_diff(lukasz, lukasz.root.score_mc.marker_mc.capture_mc, 'currentLabel', '_0')
    '''


def introduce_score_example():
    '''Jade sees farms and reads that score is the difference in farms.
    >>> code_unit.inline_examples(
    ...     ethan_lukasz_begin_example.__doc__, 
    ...     locals(), globals(), 
    ...     verify_examples = False)

    >>> wait = 5.0 / black._speed
    >>> jade = black
    >>> gnugo = white
    >>> mouse_down_and_sleep(black, black.root.score_5_5_mc,
    ...     wait)

    JADE CLICKS ON START BUTTON.
    >>> mouse_down_and_sleep(black, black.root.game_over_mc.start_mc, wait)
    >>> black.root.sgf_file_txt.text
    'sgf/beginner/score_5_5.sgf'

    FOR REPLAY, COMPUTER IS NOT PLAYING.
    >>> mouse_down_and_sleep(black, black.root.game_over_mc.white_computer_mc.enter_mc, wait)
    >>> property_diff(black, black.root.game_over_mc.white_computer_mc, 'currentLabel', 'none')

    TUTOR ADVISES JADE TO PLAY IN CENTER.
    >>> black.root.tutor_mc.currentLabel
    'center'

    JADE BUILDS IN CENTER.
    WHITE ATTACHES.
    >>> mouse_down_and_sleep(black, black.root._2_2_mc, wait)
    >>> mouse_down_and_sleep(black, black.root._2_2_mc, wait)
    >>> mouse_down_and_sleep(white, white.root._3_2_mc, wait)

    JADE SEES YELLOW FARMS.
    >>> black.root._4_2_mc.territory_mc.currentLabel
    'white'

    TUTOR SHOWS YELLOW FARMS BELONG TO ENEMY.
    >>> black.root.tutor_mc.currentLabel
    'white_territory'

    JADE BUILDS.
    WHITE BUILDS.
    >>> mouse_down_and_sleep(black, black.root._2_1_mc, wait)
    >>> mouse_down_and_sleep(black, black.root._2_1_mc, wait)
    >>> mouse_down_and_sleep(white, white.root._2_3_mc, wait) 

    TUTOR SHOWS DARK FARMS ARE YOURS.
    >>> black.root.tutor_mc.currentLabel
    'black_territory'

    JADE BUILDS.
    WHITE BUILDS.
    >>> mouse_down_and_sleep(black, black.root._3_1_mc, wait)
    >>> mouse_down_and_sleep(black, black.root._3_1_mc, wait)
    >>> mouse_down_and_sleep(white, white.root._3_4_mc, wait)

    TUTOR SHOWS SCORE BAR.  IF YOU HAVE MORE FARMS THAN WHITE, YOU WIN.
    >>> black.root.tutor_mc.currentLabel
    'score'

    JADE BUILDS.
    WHITE BUILDS.
    >>> mouse_down_and_sleep(black, black.root._1_3_mc, wait)
    >>> mouse_down_and_sleep(black, black.root._1_3_mc, wait)
    >>> mouse_down_and_sleep(white, white.root._1_4_mc, wait) 

    TUTOR REMAINS ON SCORE.
    >>> black.root.tutor_mc.currentLabel
    'score'
    '''


def extra_stone_9_9_example():
    r'''Jade sees farms and reads that score is the difference in farms.
    >>> code_unit.inline_examples(
    ...     ethan_lukasz_begin_example.__doc__, 
    ...     locals(), globals(), 
    ...     verify_examples = False)

    >>> wait = 5.0 / black._speed
    >>> jade = black
    >>> gnugo = white
    >>> mouse_down_and_sleep(black, black.root.lobby_mc._00_mc.extra_stone_7_7_2_mc,
    ...     wait)

    JADE CLICKS ON START BUTTON.
    >>> black.root.game_over_mc.start_mc.dispatchEvent(mouseDown)
    >>> time.sleep(wait)
    >>> black.root.sgf_file_txt.text
    'sgf/beginner/extra_stone_9_9.sgf'

    FOR REPLAY, COMPUTER IS NOT PLAYING.
    #>>> black.root.game_over_mc.white_computer_mc.enter_mc.dispatchEvent(mouseDown)
    #>>> time.sleep(wait)
    #>>> black.root.game_over_mc.white_computer_mc.currentLabel
    #'none'

    JADE BUILDS.
    >>> mouse_down_and_sleep(black, black.root._2_2_mc, wait)
    >>> mouse_down_and_sleep(black, black.root._2_2_mc, wait)
    '''


def start_and_quit(black, lesson_name, wait):
    black.root.lobby_mc[lesson_name].enter_mc.dispatchEvent(mouseDown)
    time.sleep(wait)
    black.root.game_over_mc.start_mc.dispatchEvent(mouseDown)
    time.sleep(wait)
    if not black.root.sgf_file_txt.text.startswith('sgf/beginner'):
        print black.root.sgf_file_txt.text
    black.root._2_2_mc.dispatchEvent(mouseDown)
    time.sleep(wait)
    black.root._2_2_mc.dispatchEvent(mouseDown)
    time.sleep(wait)
    black.root.menu_mc.toggle_mc.dispatchEvent(mouseDown)
    time.sleep(wait)
    black.root.menu_mc.lobby_mc.dispatchEvent(mouseDown)
    time.sleep(wait)
    if not black.root.currentLabel == 'lobby':
        print black.root.currentLabel

def start_lessons():
    r'''Jade starts and quits the lessons.
    >>> code_unit.inline_examples(
    ...     ethan_lukasz_begin_example.__doc__, 
    ...     locals(), globals(), 
    ...     verify_examples = False)

    >>> wait = 5.0 / black._speed
    >>> jade = black
    >>> gnugo = white
    >>> lesson_names = ['_%s_mc' % n for n in range(10)]
    >>> for lesson_name in lesson_names:
    ...     start_and_quit(black, lesson_name, wait)
    '''




def white_computer_lesson_example():
    '''LAURENS STARTS LESSON 1, PLAYS AT CENTER, AND THEN COMPUTER MOVES.
    >>> code_unit.inline_examples(
    ...     lukasz_begin_example.__doc__, 
    ...     locals(), globals(), 
    ...     verify_examples = False)

    >>> wait = 5.0 / black._speed
    >>> laurens = black
    >>> mouse_down_and_sleep(black, black.root.lobby_mc._00_mc.capture_3_3_mc,
    ...     wait)

    LAURENS CLICKS ON START BUTTON.
    >>> mouse_down_and_sleep(black, black.root.game_over_mc.start_mc, wait)

    COMPUTER IS PLAYING.
    >>> ## mouse_down_and_sleep(black, black.root.game_over_mc.white_computer_mc.enter_mc, wait)
    >>> property_diff(black, black.root.game_over_mc.white_computer_mc, 'currentLabel', 'computer')

    >>> mouse_down_and_sleep(black, black.root._1_1_mc, wait)
    >>> black.pb()
    ,,,
    ,%,
    ,,,
    >>> mouse_down_and_sleep(black, black.root._1_1_mc, 2 * wait)
    >>> black.pb()
    ?,,
    ,X,
    ,?,
    '''


def hide_lesson_example():
    '''JADE CLICKS HIDE 7X7 AND STARTS THE LESSON.
    >>> code_unit.inline_examples(
    ...     lukasz_begin_example.__doc__, 
    ...     locals(), globals(), 
    ...     verify_examples = False)

    >>> wait = 5.0 / black._speed
    >>> laurens = black
    >>> mouse_down_and_sleep(black, black.root.lobby_mc._00_mc.hide_5_5_mc,
    ...     wait)

    LAURENS CLICKS ON START BUTTON.
    >>> mouse_down_and_sleep(black, black.root.game_over_mc.start_mc, wait)

    COMPUTER IS PLAYING.
    >>> ## mouse_down_and_sleep(black, black.root.game_over_mc.white_computer_mc.enter_mc, wait)
    >>> property_diff(black, black.root.game_over_mc.white_computer_mc, 'currentLabel', 'computer')

    >>> mouse_down_and_sleep(black, black.root._3_3_mc, wait)
    >>> black.root.tutor_mc.currentLabel
    'question'
    >>> mouse_down_and_sleep(black, black.root._3_3_mc, 2 * wait)
    '''


def start_lesson_1_example():
    r'''LUKASZ SELECTS A 5X5 CAKE AND COUNTS THE PIECES OF CAKE.
        >>> code_unit.inline_examples(
        ...     ethan_lukasz_begin_example.__doc__, 
        ...     locals(), globals(), 
        ...     verify_examples = False)
        >>> emmet = lukasz
       
    LUKASZ CAN NOT SEE STRIKES TO CASTLE.
        >>> property_diff(lukasz, lukasz.root.territory_mc, 
        ...     'currentLabel', 'none')
        >>> property_diff(lukasz, lukasz.root.connected_mc, 
        ...     'currentLabel', 'none')
        >>> property_diff(lukasz, lukasz.root.unconditional_status_mc, 
        ...     'currentLabel', 'none')
        >>> property_diff(lukasz, lukasz.root.strike_mc, 
        ...     'currentLabel', 'none')
        >>> property_diff(lukasz, lukasz.root.option_mc.block_mc, 
        ...     'currentLabel', 'none')

                ETHAN
        ON THE FIRST ROW,
        CLICK THE FIRST FIELD.

    LUKASZ CLICKS FIRST FIELD.  IT FLASHES UNTIL RECEIVED.
        >>> mouse_down_and_sleep(lukasz, lukasz.root.lobby_mc._00_mc.capture_3_3_mc,
        ...     1.0 / lukasz._speed)
        >>> property_diff(lukasz, lukasz.root.lobby_mc._00_mc.capture_3_3_mc, 
        ...     'currentLabel', 'none')

    WE WAIT A BIT FOR CLIENT TO FINISH.  TODO: Why so slow?
        >>> time.sleep(3.0 / lukasz._speed)

    INT. FIELD - CONTINUOUS

    3X3 FIELD IN MOUNTAINS.  THERE ARE NO SETUP OPTIONS.
        >>> property_diff(lukasz, lukasz.root, 'currentLabel', '_3_3')
        >>> property_diff(lukasz, lukasz.root.game_over_mc, 
        ...     'currentLabel', 'preview')


    XXX SERVER REPLIES NAME OF SGF FILE.
        >>> property_diff(lukasz, lukasz.root.sgf_file_txt, 
        ...     'text', 'sgf/beginner/capture_3_3.sgf')

                LUKASZ
        BLACK KING
        >>> property_diff(lukasz, lukasz.root['turn_mc']['black_user_txt'], 
        ...     'text', 'lukasz')
        >>> property_diff(ethan, ethan.root['turn_mc']['black_user_txt'], 
        ...     'text', 'lukasz')

                ETHAN
        WHITE KING
        >>> property_diff(lukasz, lukasz.root['turn_mc']['white_user_txt'], 
        ...     'text', 'ethan')
        >>> property_diff(ethan, ethan.root['turn_mc']['white_user_txt'], 
        ...     'text', 'ethan')
       
    LUKASZ CAN SEE STRIKES TO CASTLE BUT NOT SUICIDE.
        >>> property_diff(lukasz, lukasz.root.territory_mc, 
        ...     'currentLabel', 'none')
        >>> property_diff(lukasz, lukasz.root.suicide_mc, 
        ...     'currentLabel', 'none')
        >>> property_diff(lukasz, lukasz.root.connected_mc, 
        ...     'currentLabel', 'show')
        >>> property_diff(lukasz, lukasz.root.unconditional_status_mc, 
        ...     'currentLabel', 'show')
        >>> property_diff(lukasz, lukasz.root.strike_mc, 
        ...     'currentLabel', 'show')
        >>> property_diff(lukasz, lukasz.root.option_mc.block_mc, 
        ...     'currentLabel', 'show')

                BUTTON
        START
        >>> property_diff(lukasz, lukasz.root.pass_white_mc, 'currentLabel', 'none')
        
    LUKASZ CLICKS ON BUTTON.
        >>> mouse_down_and_sleep(lukasz, lukasz.root.game_over_mc.start_mc, 1.0 / lukasz._speed)
        >>> board_diff(ethan, ethan.root._0_0_mc, 
        ...     'currentLabel', 'empty_white')

    #- WE WAIT A BIT FOR CLIENT TO FINISH.  TODO: Why so slow?
    #-     >>> time.sleep(3.0 / lukasz._speed)

    LUKASZ SEES COMMENT,
        >>> property_diff(lukasz, lukasz.root.comment_mc,
        ...     'currentLabel', 'comment')
        >>> if lukasz.root.comment_mc._txt.text.startswith('_txt'):
        ...     lukasz.root.comment_mc._txt.text

    WHICH STARTS ON FIRST LINE.
        >>> not lukasz.root.comment_mc._txt.text.startswith('\r')
        True
        >>> not lukasz.root.comment_mc._txt.text.startswith('\n')
        True
        >>> not lukasz.root.comment_mc._txt.text.startswith(' ')
        True
        >>> not lukasz.root.comment_mc._txt.text.endswith('\r')
        True
        >>> not lukasz.root.comment_mc._txt.text.endswith('\n')
        True
        >>> not lukasz.root.comment_mc._txt.text.endswith(' ')
        True

    LUKASZ CLOSES COMMENT.
        >>> mouse_down_and_sleep(lukasz, lukasz.root.comment_mc.none_mc, 1.0 / lukasz._speed)
        >>> property_diff(lukasz, lukasz.root.comment_mc,
        ...     'currentLabel', 'none')

    LUKASZ BUILDS CASTLES.
    '''



def start_lesson_10_example():
    r'''LUKASZ SELECTS A 5X5 CAKE AND COUNTS THE PIECES OF CAKE.
        >>> code_unit.inline_examples(
        ...     ethan_lukasz_begin_example.__doc__, 
        ...     locals(), globals(), 
        ...     verify_examples = False)
        >>> emmet = lukasz
       
    LUKASZ CAN NOT SEE STRIKES TO CASTLE.
        >>> property_diff(lukasz, lukasz.root.territory_mc, 
        ...     'currentLabel', 'none')
        >>> property_diff(lukasz, lukasz.root.connected_mc, 
        ...     'currentLabel', 'none')
        >>> property_diff(lukasz, lukasz.root.unconditional_status_mc, 
        ...     'currentLabel', 'none')
        >>> property_diff(lukasz, lukasz.root.strike_mc, 
        ...     'currentLabel', 'none')
        >>> property_diff(lukasz, lukasz.root.option_mc.block_mc, 
        ...     'currentLabel', 'none')

                ETHAN
        ON THE FIRST ROW,
        CLICK THE FIRST FIELD.

    LUKASZ CLICKS FIRST FIELD.  IT FLASHES UNTIL RECEIVED.
        >>> mouse_down_and_sleep(lukasz, lukasz.root.lobby_mc._00_mc.hide_7_7_mc,
        ...     1.0 / lukasz._speed)
        >>> property_diff(lukasz, lukasz.root.lobby_mc._00_mc.hide_7_7_mc, 
        ...     'currentLabel', 'none')

    WE WAIT A BIT FOR CLIENT TO FINISH.  TODO: Why so slow?
        >>> time.sleep(3.0 / lukasz._speed)

    INT. FIELD - CONTINUOUS

    3X3 FIELD IN MOUNTAINS.  THERE ARE NO SETUP OPTIONS.
        >>> property_diff(lukasz, lukasz.root, 'currentLabel', '_9_9')
        >>> property_diff(lukasz, lukasz.root.game_over_mc, 
        ...     'currentLabel', 'preview')


    XXX SERVER REPLIES NAME OF SGF FILE.
        >>> property_diff(lukasz, lukasz.root.sgf_file_txt, 
        ...     'text', 'sgf/beginner/human_9_9.sgf')

                LUKASZ
        BLACK KING
        >>> property_diff(lukasz, lukasz.root['turn_mc']['black_user_txt'], 
        ...     'text', 'lukasz')
        >>> property_diff(ethan, ethan.root['turn_mc']['black_user_txt'], 
        ...     'text', 'lukasz')

                ETHAN
        WHITE KING
        >>> property_diff(lukasz, lukasz.root['turn_mc']['white_user_txt'], 
        ...     'text', 'ethan')
        >>> property_diff(ethan, ethan.root['turn_mc']['white_user_txt'], 
        ...     'text', 'ethan')
       
    LUKASZ CAN SEE STRIKES TO CASTLE AND TERRITORY.
        >>> property_diff(lukasz, lukasz.root.territory_mc, 
        ...     'currentLabel', 'show')
        >>> property_diff(lukasz, lukasz.root.connected_mc, 
        ...     'currentLabel', 'show')
        >>> property_diff(lukasz, lukasz.root.unconditional_status_mc, 
        ...     'currentLabel', 'show')
        >>> property_diff(lukasz, lukasz.root.strike_mc, 
        ...     'currentLabel', 'show')
        >>> property_diff(lukasz, lukasz.root.option_mc.block_mc, 
        ...     'currentLabel', 'show')

                BUTTON
        START
        >>> property_diff(lukasz, lukasz.root.pass_white_mc, 'currentLabel', 'none')
        
    LUKASZ CLICKS ON BUTTON.
        >>> mouse_down_and_sleep(lukasz, lukasz.root.game_over_mc.start_mc, 1.0 / lukasz._speed)
        >>> board_diff(ethan, ethan.root._0_0_mc, 
        ...     'currentLabel', 'empty_white')

    #- WE WAIT A BIT FOR CLIENT TO FINISH.  TODO: Why so slow?
    #-     >>> time.sleep(3.0 / lukasz._speed)

    LUKASZ SEES COMMENT,
        >>> property_diff(lukasz, lukasz.root.comment_mc,
        ...     'currentLabel', 'comment')
        >>> if lukasz.root.comment_mc._txt.text.startswith('_txt'):
        ...     lukasz.root.comment_mc._txt.text

    WHICH STARTS ON FIRST LINE.
        >>> not lukasz.root.comment_mc._txt.text.startswith('\r')
        True
        >>> not lukasz.root.comment_mc._txt.text.startswith('\n')
        True
        >>> not lukasz.root.comment_mc._txt.text.startswith(' ')
        True
        >>> not lukasz.root.comment_mc._txt.text.endswith('\r')
        True
        >>> not lukasz.root.comment_mc._txt.text.endswith('\n')
        True
        >>> not lukasz.root.comment_mc._txt.text.endswith(' ')
        True

    LUKASZ CLOSES COMMENT.
        >>> mouse_down_and_sleep(lukasz, lukasz.root.comment_mc.none_mc, 1.0 / lukasz._speed)
        >>> property_diff(lukasz, lukasz.root.comment_mc,
        ...     'currentLabel', 'none')

    LUKASZ BUILDS CASTLES.
    '''


def yuji_load_user_example():
    '''Yuji logs on.  He sees he is level 2.
    >>> gateway_process = configuration.subprocess_gateway(configuration.amf_host, 'embassy.py', configuration.verbose)
    >>> yuji = configuration.globe_class()
    >>> yuji.setup(configuration.mock_speed, configuration.setup_client)
    >>> wait = 4.0 / yuji._speed
    >>> yuji.root.level_mc._txt.text
    '1'
    >>> yuji.root.title_mc.username_txt.text = 'yuji'
    >>> time.sleep(wait)
    >>> yuji.root.title_mc.password_txt.text = 'kuribara'
    >>> time.sleep(wait)
    >>> yuji.root.title_mc.start_btn.dispatchEvent(mouseDown)
    >>> time.sleep(wait)

    Soon, he enters the lobby and sees he is level 2.
    >>> yuji.root.currentLabel
    'lobby'
    >>> yuji.root.level_mc._txt.text
    '2'
    '''

def rotate_sgf_example():
    '''Marije explores some castles that let the dragon eat farms.
    She sees the dragon will eat some farms and finds the castle to claim the farms.
        >>> code_unit.inline_examples(
        ...     ethan_lukasz_begin_example.__doc__, 
        ...     locals(), globals(), 
        ...     verify_examples = False)
        >>> wait = 4.0 / black._speed
        >>> sloth = 1.0 / black._speed
    
        >>> marije = black
        >>> computer_marije = white

    >>> marije.root.lobby_mc.main_mc._07_mc.dispatchEvent(mouseDown)
    >>> marije.root.lobby_mc._07_mc.score_5_5_3_mc.dispatchEvent(mouseDown)

        FOR REPLAY, COMPUTER IS NOT PLAYING.
        >>> marije.root.game_over_mc.white_computer_mc.enter_mc.dispatchEvent(mouseDown)

        white computer button is not blinking.
        >>> marije.root.game_over_mc.white_computer_mc.enter_mc.currentLabel
        'none'
        >>> marije.root.game_over_mc.white_computer_mc.enter_mc.gotoAndPlay('none')
        >>> time.sleep(wait)
    >>> mouse_down_and_sleep(marije, marije.root.game_over_mc.start_mc, wait)
    >>> mouse_down_and_sleep(marije, marije.root._3_3_mc, wait)
    >>> comment = marije.root.comment_mc._txt.text
    >>> if not comment.startswith('THIS CASTLE ONLY CLAIMS'):
    ...     comment
    >>> mouse_down_and_sleep(marije, marije.root._2_2_mc, wait)
    >>> mouse_down_and_sleep(marije, marije.root._2_2_mc, wait)
    >>> mouse_down_and_sleep(computer_marije, computer_marije.root._1_2_mc, wait)

    if white, then do not get black's news, so white does not see tutor.
    >>> computer_marije.root.comment_mc.currentLabel
    'none'
    >>> marije.pb()
    ,,,,,
    ,,O,,
    ,,X,,
    ,,,,,
    ,,,,,
    >>> mouse_down_and_sleep(marije, marije.root._2_1_mc, wait)
    >>> mouse_down_and_sleep(marije, marije.root._1_1_mc, wait)
    >>> mouse_down_and_sleep(marije, marije.root._1_3_mc, wait)

    Marije guesses this castle is okay.
    >>> marije.root.bad_move_mc.currentLabel
    'none'
    >>> mouse_down_and_sleep(marije, marije.root._2_3_mc, wait)

    Marije sees this castle is bad.
    >>> marije.root.bad_move_mc.currentLabel
    'show'

    Marije sees this castle is bad, so is forbidden.
    Although SGF only covers top-left octant,
    History is mapped onto top-left octant.
    >>> mouse_down_and_sleep(marije, marije.root._2_3_mc, wait)
    >>> marije.pb()
    ,,,,,
    ,,O,,
    ,,X,,
    ,,,,,
    ,,,,,
    >>> marije.root.bad_move_mc.currentLabel
    'show'
    >>> mouse_down_and_sleep(marije, marije.root._1_1_mc, wait)
    >>> mouse_down_and_sleep(marije, marije.root._1_1_mc, wait)

    >>> marije.root.comment_mc.close_btn.dispatchEvent(mouseDown)
    >>> computer_marije.root.comment_mc.close_btn.dispatchEvent(mouseDown)
    >>> time.sleep(wait)
    >>> marije.root.comment_mc.currentLabel
    'none'
    >>> computer_marije.root.comment_mc.currentLabel
    'none'
    >>> mouse_down_and_sleep(computer_marije, computer_marije.root._2_1_mc, wait)

    Marije sees comments on white's move.
    White sees same comments as black.
    >>> marije.root.comment_mc.currentLabel
    'comment'
    >>> computer_marije.root.comment_mc.currentLabel
    'comment'
    >>> marije.root.comment_mc._txt.text
    'DRAGONS ARE FIGHTING!  CAN YOU FIGHT BACK?'
    >>> computer_marije.root.comment_mc._txt.text
    'DRAGONS ARE FIGHTING!  CAN YOU FIGHT BACK?'
    >>> marije.pb()
    ,,,,,
    ,XO,,
    ,OX,,
    ,,,,,
    ,,,,,
    >>> marije.root.bad_move_mc.currentLabel
    'show'
    >>> mouse_down_and_sleep(marije, marije.root._3_1_mc, wait)
    >>> marije.root.bad_move_mc.currentLabel
    'show'

    #TODO:
    #Match symmetrical board (different order of symmetrical moves).
    #Marije guesses this castle is okay.
    #>>> marije.root.bad_move_mc.currentLabel
    #'none'
    #>>> mouse_down_and_sleep(marije, marije.root._3_1_mc, wait)
    #>>> mouse_down_and_sleep(computer_marije, computer_marije.root._0_1_mc, wait)
    #>>> marije.pb()
    #,O,,,
    #,XO,,
    #,OX,,
    #,X,,,
    #,,,,,
    #>>> mouse_down_and_sleep(marije, marije.root._1_0_mc, wait)
    #>>> mouse_down_and_sleep(marije, marije.root._2_0_mc, wait)
    #>>> mouse_down_and_sleep(marije, marije.root._1_0_mc, wait)
    #>>> mouse_down_and_sleep(marije, marije.root._1_0_mc, wait)
    #>>> mouse_down_and_sleep(computer_marije, computer_marije.root._3_2_mc, wait)
    #>>> mouse_down_and_sleep(marije, marije.root._2_3_mc, wait)
    #>>> mouse_down_and_sleep(marije, marije.root._2_3_mc, wait)
    #>>> mouse_down_and_sleep(computer_marije, computer_marije.root._1_3_mc, wait)
    #>>> mouse_down_and_sleep(marije, marije.root._3_3_mc, wait)
    #>>> mouse_down_and_sleep(marije, marije.root._3_3_mc, wait)
    #>>> mouse_down_and_sleep(computer_marije, computer_marije.root._4_1_mc, wait)
    #>>> mouse_down_and_sleep(marije, marije.root._3_0_mc, wait)
    #>>> mouse_down_and_sleep(marije, marije.root._3_0_mc, wait)
    #>>> marije.pb()
    #,O,,,
    #XXOO,
    #,OXX,
    #XXOX,
    #,O,,,
    #>>> computer_marije.root.pass_mc.dispatchEvent(mouseDown)
    '''



def rotate_add_stone_example():
    '''Marije builds a wall.
        >>> code_unit.inline_examples(
        ...     ethan_lukasz_begin_example.__doc__, 
        ...     locals(), globals(), 
        ...     verify_examples = False)
        >>> wait = 4.0 / black._speed
        >>> sloth = 1.0 / black._speed
    
        >>> marije = black
        >>> computer_marije = white

    >>> marije.root.lobby_mc.main_mc._07_mc.dispatchEvent(mouseDown)
    >>> marije.root.lobby_mc._07_mc.score_rule_mc.dispatchEvent(mouseDown)

        FOR REPLAY, COMPUTER IS NOT PLAYING.
        >>> marije.root.game_over_mc.white_computer_mc.enter_mc.dispatchEvent(mouseDown)

        white computer button is not blinking.
        >>> marije.root.game_over_mc.white_computer_mc.enter_mc.currentLabel
        'none'
        >>> marije.root.game_over_mc.white_computer_mc.enter_mc.gotoAndPlay('none')
        >>> time.sleep(wait)
    >>> mouse_down_and_sleep(marije, marije.root.game_over_mc.start_mc, wait)
    >>> marije.pb()
    ,,,,,
    X,,,,
    ,XXX,
    OOOOO
    ,,,,,
    >>> mouse_down_and_sleep(marije, marije.root._1_3_mc, wait)
    >>> marije.root.bad_move_mc.currentLabel
    'show'

    Marije can build a stone.
    >>> mouse_down_and_sleep(marije, marije.root._2_4_mc, wait)
    >>> marije.root.bad_move_mc.currentLabel
    'none'
    >>> mouse_down_and_sleep(marije, marije.root._2_4_mc, wait)
    >>> marije.root.bad_move_mc.currentLabel
    'none'

    #>>> mouse_down_and_sleep(computer_marije, computer_marije.root._1_2_mc, wait)
    '''

def marije_follow_sgf_example():
    '''On a 3x3 board, Marije captures a scripted dragon.
    Marije sees squares that highlight land.
        >>> code_unit.inline_examples(
        ...     lukasz_begin_example.__doc__, 
        ...     locals(), globals(), 
        ...     verify_examples = False)
        >>> wait = 4.0 / black._speed
        >>> sloth = 1.0 / black._speed
    
        >>> marije = black

    >>> marije.root.lobby_mc.main_mc._00_mc.dispatchEvent(mouseDown)
    >>> time.sleep(wait)
    >>> marije.root.lobby_mc._00_mc.capture_3_3_2_mc.dispatchEvent(mouseDown)
    >>> time.sleep(wait)

    Marije only needs to capture one white stone.
    >>> marije.root.option_mc.first_capture_mc.currentLabel
    'show'
    >>> marije.root.game_over_mc.start_mc.dispatchEvent(mouseDown)
    >>> time.sleep(wait)
    >>> marije.pb()
    ,,,
    ,,,
    ,,,

    White follows the moves listed in the corresponding SGF file.
    >>> marije.root._1_1_mc.dispatchEvent(mouseDown)
    >>> time.sleep(wait)
    >>> marije.root._1_0_mc.square_mc.currentLabel
    'none'
    >>> marije.root._1_2_mc.square_mc.currentLabel
    'none'
    >>> marije.root._2_1_mc.square_mc.currentLabel
    'none'
    >>> marije.root._1_1_mc.dispatchEvent(mouseDown)
    >>> time.sleep(wait)
    >>> marije.pb()
    ,O,
    ,X,
    ,,,

    Marije sees three squares.
    >>> marije.root._1_0_mc.square_mc.currentLabel
    'show'
    >>> marije.root._1_2_mc.square_mc.currentLabel
    'show'
    >>> marije.root._2_1_mc.square_mc.currentLabel
    'show'
    >>> marije.root._1_2_mc.dispatchEvent(mouseDown)
    >>> time.sleep(5 * wait)
    >>> marije.pb()
    ,O,
    ,X%
    ,,,
    >>> marije.root._0_0_mc.square_mc.currentLabel
    'none'
    >>> marije.root._1_0_mc.square_mc.currentLabel
    'show'
    >>> marije.root._1_2_mc.square_mc.currentLabel
    'none'
    >>> marije.root._2_0_mc.square_mc.currentLabel
    'none'
    >>> marije.root._2_1_mc.square_mc.currentLabel
    'show'
    >>> marije.root._1_0_mc.dispatchEvent(mouseDown)
    >>> time.sleep(wait)
    >>> marije.root._1_0_mc.dispatchEvent(mouseDown)

    Ugh.  Flash client appears to update, 
    yet Python does not show latest.  So, let's wait.
    >>> time.sleep(3 * wait)
    >>> from pprint import pprint
    >>> ## pprint(marije.ambassador.receives[-1])
    >>> marije.pb()
    ,O,
    XXO
    ,,,
    >>> marije.root._0_0_mc.square_mc.currentLabel
    'none'
    >>> marije.root._1_0_mc.square_mc.currentLabel
    'none'
    >>> marije.root._1_2_mc.square_mc.currentLabel
    'none'
    >>> marije.root._2_0_mc.square_mc.currentLabel
    'none'
    >>> marije.root._2_1_mc.square_mc.currentLabel
    'none'
    >>> marije.root._0_0_mc.dispatchEvent(mouseDown)
    >>> time.sleep(wait)
    >>> marije.root._0_0_mc.dispatchEvent(mouseDown)
    >>> time.sleep(wait)
    >>> marije.pb()
    XO,
    XXO
    ,O,
    >>> marije.root._0_0_mc.square_mc.currentLabel
    'none'
    >>> marije.root._0_2_mc.square_mc.currentLabel
    'none'
    >>> marije.root._1_2_mc.square_mc.currentLabel
    'none'
    >>> marije.root._2_0_mc.square_mc.currentLabel
    'show'
    >>> marije.root._2_1_mc.square_mc.currentLabel
    'none'

    Marije captures first, and so wins.
    >>> marije.root._0_2_mc.dispatchEvent(mouseDown)
    >>> time.sleep(wait)
    >>> marije.root._0_2_mc.dispatchEvent(mouseDown)
    >>> time.sleep(wait)
    >>> marije.pb()
    X,X
    XXO
    ,O,
    >>> marije.root.game_over_mc.currentLabel
    'win'

    If white moves randomly, the odds of accidentally following is about 0.5%
    >>> (8 * 6 * 4)
    192
    >>> print round(1.0 / (8 * 6 * 4), 3)
    0.005
    '''


def marije_rotated_sgf_example():
    '''On a 3x3 board, Marije captures a scripted dragon.
    Marije sees squares that highlight land.
        >>> code_unit.inline_examples(
        ...     lukasz_begin_example.__doc__, 
        ...     locals(), globals(), 
        ...     verify_examples = False)
        >>> wait = 4.0 / black._speed
        >>> sloth = 1.0 / black._speed
    
        >>> marije = black

    >>> marije.root.lobby_mc.main_mc._00_mc.dispatchEvent(mouseDown)
    >>> time.sleep(wait)

    >>> marije.root.lobby_mc._00_mc.capture_3_3_1_mc.dispatchEvent(mouseDown)
    >>> time.sleep(wait)

    Marije only needs to capture one white stone.
    >>> marije.root.option_mc.first_capture_mc.currentLabel
    'show'
    >>> marije.root.game_over_mc.start_mc.dispatchEvent(mouseDown)
    >>> time.sleep(wait)
    >>> marije.pb()
    ,,,
    ,X,
    ,,O

    White follows the moves listed in the corresponding SGF file.
    >>> marije.root._1_2_mc.dispatchEvent(mouseDown)
    >>> time.sleep(wait)
    >>> marije.pb()
    ,,,
    ,X%
    ,,O
    >>> marije.root._1_2_mc.square_mc.currentLabel
    'none'
    >>> marije.root._2_1_mc.square_mc.currentLabel
    'show'
    >>> marije.root._2_1_mc.dispatchEvent(mouseDown)
    >>> time.sleep(wait)
    >>> marije.pb()
    ,,,
    ,X,
    ,%O
    >>> marije.root._2_1_mc.square_mc.currentLabel
    'none'
    >>> marije.root._1_2_mc.square_mc.currentLabel
    'show'

    >>> marije.root._2_1_mc.dispatchEvent(mouseDown)

    Ugh.  Flash client appears to update, 
    yet Python does not show latest.  So, let's wait.
    >>> time.sleep(3 * wait)
    >>> from pprint import pprint
    >>> ## pprint(marije.ambassador.receives[-1])
    >>> marije.pb()
    ,,,
    ,XO
    ,XO

    Beware, white accidentally followed.
    If white moves randomly, the odds of accidentally following is about 17%
    >>> print round(1.0 / 6, 2)
    0.17

    Odds are about 3% that white accidentally follows again.  
    >>> print round(1.0 / (6 * 6), 2)
    0.03

    To improve confidence from 83% to 97%, I examine again.
    >>> marije.root.menu_mc.lobby_mc.dispatchEvent(mouseDown)
    >>> time.sleep(2 * wait)
    >>> marije.root.lobby_mc._00_mc.capture_3_3_1_mc.dispatchEvent(mouseDown)
    >>> time.sleep(wait)
    >>> marije.root.game_over_mc.start_mc.dispatchEvent(mouseDown)
    >>> time.sleep(wait)
    >>> marije.root._2_1_mc.dispatchEvent(mouseDown)
    >>> time.sleep(wait)
    >>> marije.root._2_1_mc.dispatchEvent(mouseDown)
    >>> time.sleep(3 * wait)
    >>> marije.pb()
    ,,,
    ,XO
    ,XO

    To confirm unrotated matches.  I examine base coordinates.
    >>> marije.root.menu_mc.lobby_mc.dispatchEvent(mouseDown)
    >>> time.sleep(2 * wait)
    >>> marije.root.lobby_mc._00_mc.capture_3_3_1_mc.dispatchEvent(mouseDown)
    >>> time.sleep(wait)
    >>> marije.root.game_over_mc.start_mc.dispatchEvent(mouseDown)
    >>> time.sleep(wait)
    >>> marije.root._1_2_mc.dispatchEvent(mouseDown)
    >>> time.sleep(wait)
    >>> marije.root._1_2_mc.dispatchEvent(mouseDown)
    >>> time.sleep(3 * wait)
    >>> marije.pb()
    ,,,
    ,XX
    ,OO

    So I examine twice.
    To confirm unrotated matches.  I examine base coordinates.
    >>> marije.root.menu_mc.lobby_mc.dispatchEvent(mouseDown)
    >>> time.sleep(2 * wait)
    >>> marije.root.lobby_mc._00_mc.capture_3_3_1_mc.dispatchEvent(mouseDown)
    >>> time.sleep(wait)
    >>> marije.root.game_over_mc.start_mc.dispatchEvent(mouseDown)
    >>> time.sleep(wait)
    >>> marije.root._1_2_mc.dispatchEvent(mouseDown)
    >>> time.sleep(wait)
    >>> marije.root._1_2_mc.dispatchEvent(mouseDown)
    >>> time.sleep(3 * wait)
    >>> marije.pb()
    ,,,
    ,XX
    ,OO
    '''


def marije_opening_note_example():
    '''During setup, Marije sees mission text to capture a dragon.
        >>> code_unit.inline_examples(
        ...     lukasz_begin_example.__doc__, 
        ...     locals(), globals(), 
        ...     verify_examples = False)
        >>> wait = 4.0 / black._speed
        >>> sloth = 1.0 / black._speed
    
        >>> marije = black

    >>> marije.root.lobby_mc.main_mc._00_mc.dispatchEvent(mouseDown)
    >>> time.sleep(wait)

    >>> previous = marije.root.game_over_mc.mission_mc._txt.text
    >>> marije.root.game_over_mc.mission_mc.currentLabel
    'none'
    >>> marije.root.lobby_mc._00_mc.capture_3_3_1_mc.dispatchEvent(mouseDown)
    >>> time.sleep(wait)

    Marije sees intro text.
    >>> marije.root.game_over_mc.currentLabel
    'preview'
    >>> marije.root.game_over_mc.mission_mc.currentLabel
    'opening_note'
    >>> if previous == marije.root.game_over_mc.mission_mc._txt.text:
    ...     previous, marije.root.game_over_mc.mission_mc._txt.text
    
    do not block extra stone.  start.  Marije sees briefing close.  
    >>> marije.root.game_over_mc.start_mc.dispatchEvent(mouseDown)
    >>> time.sleep(wait)
    >>> marije.root.game_over_mc.currentLabel
    'none'
    '''


def laurens_resume_session_example():
    '''Laurens logs in again and resumes lesson.
    >>> # example.log level 20 at Wed Sep 01 20:52:00 2010

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
    >>> laurens.root.currentLabel
    '_3_3'
    >>> laurens.root._2_0_mc.scaleX
    2.5
    >>> mouse_down_and_sleep(laurens, laurens.root.game_over_mc.start_mc, wait)
    >>> time.sleep(sloth * 7.612000)

    >>> del laurens
    >>> del black

    laurens logs in again.
    >>> laurens2 = configuration.globe_class()
    >>> laurens2.setup(configuration.mock_speed, configuration.setup_client)
    >>> set_property(laurens2, laurens2.root.title_mc.username_txt, 'text', 'lukasz')
    >>> time.sleep(wait)
    >>> set_property(laurens2, laurens2.root.title_mc.password_txt, 'text', 'l')
    >>> time.sleep(wait)
    >>> laurens2.root._2_0_mc.scaleX
    1.0
    >>> mouse_down_and_sleep(laurens2, laurens2.root.title_mc.start_btn,
    ...     wait)

    >>> laurens2.root.title_mc.start_btn.dispatchEvent(mouseDown)
    >>> time.sleep(2 * wait)

    laurens resumes.
    >>> laurens2.root.currentLabel
    '_3_3'
    >>> laurens2.root._2_0_mc.scaleX
    2.5
    >>> laurens2.ambassador.receives
    '''

def laurens_preview_play_example():
    '''Laurens previews comment.  Laurens plays and sees comment only once.
    >>> # example.log level 20 at Wed Sep 01 20:52:00 2010

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

    Laurens previews and sees comment, then plays and does not see it again.
    >>> laurens.root._1_2_mc.dispatchEvent(mouseDown)
    >>> time.sleep(wait)
    >>> laurens.root.comment_mc.currentLabel
    'comment'
    >>> laurens.root.comment_mc.none_mc.dispatchEvent(mouseDown)
    >>> time.sleep(wait)
    >>> laurens.root.comment_mc.currentLabel
    'none'
    >>> laurens.root._1_2_mc.dispatchEvent(mouseDown)
    >>> time.sleep(wait)
    >>> laurens.root.comment_mc.currentLabel
    'none'
    
    after clearing preview, user no longer has record 
    of what state the client is in.  
    to cull redundant news, we need to preserve client state.
    and comment, even if closed, should not be sent again.
    '''

def andrew_no_empty_block_example():
    '''Andrew starts hunting.  He sees no empty blocks.
    >>> # example.log level 20 at Mon Sep 06 16:04:09 2010

        >>> code_unit.inline_examples(
        ...     lukasz_begin_example.__doc__, 
        ...     locals(), globals(), 
        ...     verify_examples = False)
        >>> wait = 4.0 / black._speed
        >>> sloth = 1.0 / black._speed
    
        >>> andrew = black

    >>> andrew.root.level_mc.none_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 6.328000)
    >>> andrew.root.lobby_mc.main_mc._00_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 1.359000)
    >>> andrew.root.lobby_mc._00_mc.capture_rule_side_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 1.042000)
    >>> time.sleep(sloth * 4.225000)
    >>> andrew.root.option_mc.empty_block_mc.currentLabel
    'none'
    >>> mouse_down_and_sleep(andrew, andrew.root.game_over_mc.start_mc, wait)
    >>> andrew.root._0_2_mc.empty_block_east_mc.currentLabel
    'none'
    >>> andrew.root._0_2_mc.empty_block_north_mc.currentLabel
    'none'
    >>> andrew.root._0_2_mc.empty_block_west_mc.currentLabel
    'none'

    The client received no empty blocks.
    >>> for r in andrew.ambassador.receives:
    ...     r.get('_0_2_mc')
    ...     
    >>> for r in andrew.ambassador.receives[-1].get('sequence', []):
    ...     r.get('_0_2_mc')
    ...     
    >>> for r in andrew.ambassador.receives[-2].get('sequence', []):
    ...     r.get('_0_2_mc')
    ...     
    '''

def andrew_no_top_move_example():
    '''Andrew starts hunting.  He previews.  He sees no top move.
    >>> # example.log level 20 at Mon Sep 06 16:04:09 2010

        >>> code_unit.inline_examples(
        ...     lukasz_begin_example.__doc__, 
        ...     locals(), globals(), 
        ...     verify_examples = False)
        >>> wait = 4.0 / black._speed
        >>> sloth = 1.0 / black._speed
    
        >>> andrew = black

    >>> andrew.root.level_mc.none_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 6.328000)
    >>> andrew.root.lobby_mc.main_mc._00_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 1.359000)
    >>> andrew.root.lobby_mc._00_mc.capture_rule_side_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 1.042000)
    >>> time.sleep(sloth * 4.225000)
    >>> andrew.root.top_move_mc.currentLabel
    'none'
    >>> mouse_down_and_sleep(andrew, andrew.root.game_over_mc.start_mc, wait)
    >>> import pdb; pdb.set_trace(); andrew.root._1_1_mc.dispatchEvent(mouseDown)
    >>> time.sleep(wait)
    >>> import intersection_mc
    >>> intersection_mc.children_label_equals(andrew.intersection_mc_array, 'top_move_mc', 'white')
    []
    >>> andrew.root._0_1_mc.top_move_mc.currentLabel
    'none'
    >>> andrew.root._1_0_mc.top_move_mc.currentLabel
    'none'
    >>> for r in andrew.ambassador.receives[-1].get('sequence', []):
    ...     r.get('_0_1_mc')
    ...     r.get('_1_0_mc')
    ...     
    >>> for r in andrew.ambassador.receives[-2].get('sequence', []):
    ...     r.get('_0_1_mc')
    ...     r.get('_1_0_mc')
    ...     
    '''

def moonhyoung_start_white_tiger_example():
    '''Moonhyoung starts white tiger problem.
    >>> moonhyoung, wait = setup_example(configuration, 
    ...     ('moonhyoung', 'park') )
    >>> sloth = 1.0 / moonhyoung._speed
    >>> moonhyoung.root.lobby_mc._14_mc.white_tiger_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 4.321650)
    >>> moonhyoung.root.currentLabel
    '_9_9'
    >>> moonhyoung.root.game_over_mc.currentLabel
    'preview'
    '''



def robby_start_mission_example():
    '''Robby starts a problem and another.
    >>> robby, wait = setup_example(configuration, 
    ...     ('temporary', 'temporary') )
    >>> sloth = 1.0 / robby._speed

    PLACEHOLDER:
    intro:  quickly see setup all at once, unsequenced
    build
    sgf comment behind preview screen
    quit
    different board size than before
    intro:  quickly see setup all at once, unsequenced
    start
    build

    TODO:
    intro:  do not see or hear setup or cursor or comment.  do see intro
    do see board size
    board size
    start
    quickly see setup all at once, unsequenced
    build
    quit
    different board size than before
    intro:  do not see or hear setup or cursor or comment.  do see intro
    do see board size
    start
    quickly see setup all at once, unsequenced
    build
    >>> robby.root.comment_mc.none_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 3.726000)
    >>> robby.root.sgf_comment_mc.none_mc.currentLabel
    'none'
    >>> robby.root.lobby_mc._00_mc.capture_3_3_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 3.726000)
    >>> robby.root.sgf_comment_mc.currentLabel
    'comment'
    >>> robby.root.currentLabel
    '_3_3'
    >>> mouse_down_and_sleep(robby, robby.root.game_over_mc.start_mc, wait)
    >>> time.sleep(sloth * 2.928000)
    >>> robby.root.sgf_comment_mc.currentLabel
    'comment'
    >>> mouse_down_and_sleep(robby, robby.root._1_1_mc, wait)
    >>> time.sleep(sloth * 2.247000)
    >>> robby.root.menu_mc.toggle_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 4.559000)
    >>> robby.root.menu_mc.lobby_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 1.340000)
    >>> robby.root.lobby_mc._00_mc.capture_5_5_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 4.559000)
    >>> robby.root.sgf_comment_mc.currentLabel
    'comment'
    >>> robby.root.currentLabel
    '_5_5'
    >>> mouse_down_and_sleep(robby, robby.root.game_over_mc.start_mc, wait)
    >>> time.sleep(sloth * 2.928000)
    >>> robby.root.sgf_comment_mc.currentLabel
    'comment'
    >>> mouse_down_and_sleep(robby, robby.root._2_2_mc, wait)
    >>> time.sleep(sloth * 2.247000)
    '''

def robby_try_again_example():
    '''Robby clicks a bad move.  He tries again and plays a good move.
    >>> robby, wait = setup_example(configuration, 
    ...     ('temporary', 'temporary') )
    >>> sloth = 1.0 / robby._speed
    >>> robby.root.lobby_mc.main_mc._00_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 4.581000)
    >>> robby.root.lobby_mc._00_mc.capture_block_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 5.911000)
    >>> mouse_down_and_sleep(robby, robby.root.game_over_mc.start_mc, wait)
    >>> time.sleep(sloth * 3.140000)
    >>> mouse_down_and_sleep(robby, robby.root._0_0_mc, wait)
    >>> time.sleep(sloth * 3.140000)
    >>> mouse_down_and_sleep(robby, robby.root._1_0_mc, wait)
    >>> robby.pb()
    ,O,
    XX,
    ,O,
    '''

def robby_cannot_pass_example():
    '''Robby passes in a lesson where that is not allowed.  Then he moves.
    >>> robby, wait = setup_example(configuration, 
    ...     ('temporary', 'temporary') )
    >>> sloth = 1.0 / robby._speed
    >>> robby.root.lobby_mc.main_mc._00_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 4.581000)
    >>> robby.root.lobby_mc._00_mc.capture_block_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 5.911000)
    >>> mouse_down_and_sleep(robby, robby.root.game_over_mc.start_mc, wait)
    >>> time.sleep(sloth * 3.140000)
    >>> robby.root.bad_move_mc.currentLabel
    'none'
    >>> mouse_down_and_sleep(robby, robby.root.pass_mc, wait)
    >>> robby.pb()
    ,O,
    ,X,
    ,,,
    >>> robby.root.bad_move_mc.currentLabel
    'show'
    >>> time.sleep(sloth * 3.140000)
    >>> mouse_down_and_sleep(robby, robby.root._1_0_mc, wait)
    >>> robby.pb()
    ,O,
    XX,
    ,O,
    '''

def jerry_lose_prize_example():
    '''White captures Jerry.  Jerry loses and gains no experience.
        >>> code_unit.inline_examples(
        ...     ethan_lukasz_begin_example.__doc__, 
        ...     locals(), globals(), 
        ...     verify_examples = False)
        >>> wait = 4.0 / black._speed
        >>> sloth = 1.0 / black._speed
        >>> jerry = black
        >>> computer_jerry = white
    >>> jerry.root.level_mc.none_mc.dispatchEvent(mouseDown)
    >>> time.sleep(wait)
    >>> jerry.root.level_mc.currentLabel
    'none'
    >>> jerry.root.lobby_mc.main_mc._00_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 4.484000)
    >>> jerry.root.lobby_mc._00_mc.capture_5_5_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 4.146000)
        >>> jerry.root.game_over_mc.white_computer_mc.enter_mc.dispatchEvent(mouseDown)
    >>> time.sleep(sloth * 3.089000)
    >>> mouse_down_and_sleep(jerry, jerry.root.game_over_mc.start_mc, wait)
    >>> time.sleep(sloth * 2.608000)
    >>> mouse_down_and_sleep(jerry, jerry.root._2_2_mc, wait)
    >>> mouse_down_and_sleep(computer_jerry, computer_jerry.root._2_3_mc, wait)
    >>> time.sleep(sloth * 1.795000)
    >>> mouse_down_and_sleep(jerry, jerry.root._2_4_mc, wait)
    >>> mouse_down_and_sleep(computer_jerry, computer_jerry.root._1_2_mc, wait)
    >>> time.sleep(sloth * 1.394000)
    >>> mouse_down_and_sleep(jerry, jerry.root._1_1_mc, wait)
    >>> mouse_down_and_sleep(computer_jerry, computer_jerry.root._3_2_mc, wait)
    >>> time.sleep(sloth * 1.767000)
    >>> mouse_down_and_sleep(jerry, jerry.root._1_3_mc, wait)
    >>> jerry.root.level_mc.currentLabel
    'none'
    >>> import pdb; pdb.set_trace(); mouse_down_and_sleep(computer_jerry, computer_jerry.root._2_1_mc, wait)
    >>> jerry.root.game_over_mc.currentLabel
    'lose'
    >>> jerry.root.level_mc.currentLabel
    'none'
    '''


