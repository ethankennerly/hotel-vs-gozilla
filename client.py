#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
Mock ActionScript client and examples of Crazy Cake
'''
__author__ = 'Ethan Kennerly'


from user_as import *

# Doctest that enables distributing to client-server.

def property_diff(globe, display_object, property, expected_value):
    r'''Gracefully display illegible characters.
    >>> laurens = configuration.globe_class()
    >>> laurens.create(1)
    >>> laurens.root.lobby_mc.join_mc.join_txt.text = u'JOIN \xa040\r'
    >>> old_log_level = logging.getLogger().level
    >>> logging.getLogger().setLevel(logging.CRITICAL)
    >>> property_diff(laurens, laurens.root.lobby_mc.join_mc.join_txt, 'text', 'JOIN 40')
    u'expected: JOIN 40, got: JOIN \xa040\r'
    >>> logging.getLogger().setLevel(old_log_level)
    '''
    verified = False
    verified = display_object[property] == expected_value
    if not verified:
        error_log = 'property_diff: %s.%s = %s' \
                % (display_object.name, property, 
                        display_object[property].__repr__() )
        logging.error(error_log)
        import pprint
        if log_level <= logging.DEBUG:
            tree = family_tree(display_object, {})
            #pprint.pprint(tree)
            print tree.keys()
        if log_level <= logging.DEBUG and globe.ambassador.receives:
            print 'last receive:'
            pprint.pprint(globe.ambassador.receives[-1])
        ## import pdb; pdb.set_trace();
        return 'expected: %s, got: %s' \
                % (expected_value, display_object[property])

def board_diff(globe, display_object, property, expected_value):
    difference = property_diff(globe, display_object, property, expected_value)
    if difference:
         import embassy
         print embassy.flash_to_text(globe.intersection_mc_array)
    return difference 


def mouse_down_and_sleep(globe, target, second):
    evt = MouseEvent(MouseEvent.MOUSE_DOWN)
    evt.currentTarget = target
    target.dispatchEvent(evt)
    time.sleep(second)




def set_property(globe, owner, name, value): 
    news = note(owner, name, value)
    olds = imitate_news(globe.root, news)
    

def publish_property(globe, owner, name, value): 
    news = note(owner, name, value)
    return globe.publish(news)


#? from lesson import *


# Mock network for consistent doctests.

#- from configuration import *
import amf_socket_client

def setup_amf_client(globe):
    globe.ambassador = amf_socket_client.AmfSocketClient(globe.imitate)
    globe.ambassador.connect(configuration.amf_host, configuration.amf_port)
    return globe.ambassador

def setup_remote_client(globe):
    os_name = 'posix'
    configuration.amf_host = environ[os_name]['amf_host']
    globe.ambassador = amf_socket_client.AmfSocketClient(globe.imitate)
    globe.ambassador.connect(configuration.amf_host, configuration.amf_port)
    return globe.ambassador



# For doctest mock by default, but not if changed and reimported.
#if not globals().get('subprocess_gateway'):
#    # subprocess_gateway = mock_gateway
#    subprocess_gateway = subprocess_gateway_file
#if not globals().get('setup_client'):
#    # setup_client = mock_setup_client
#    setup_client = setup_amf_client
#if not globals().get('mock_speed'):
#    # mock_speed = 8
#    mock_speed = 1
#if not globals().get('verbose'):
#    # verbose = 'warning'
#    verbose = 'info'

## mock_speed = globals().get('mock_speed') or 16
## verbose = globals().get('verbose') or 'warning'




# Examples

def do_setup_user(configuration):
    '''Without setting up client.
    >>> black = do_setup_user(configuration)
    '''
    globe = configuration.globe_class()
    globe.create(configuration.mock_speed)  
    globe.setup_events()
    return globe

def to_clear_table_performance():
    '''Clear table in 1 second or less.
    >>> user = globe_class()
    >>> user.create(1)
    >>> user.setup_events()
    >>> from mock_client import echo_protocol_class
    >>> user.ambassador = echo_protocol_class()
    >>> length = len(user.intersection_mc_array)
    >>> then = time.time()
    >>> from super_users import to_clear_table
    >>> to_clear_table(user.root, length)
    {}
    >>> duration = time.time() - then
    >>> if not duration < 1:
    ...     duration
    '''

def to_clear_table_example():
    '''Clear table in 1 second or less.
    >>> from super_users import to_clear_table
    >>> code_unit.doctest_unit(to_clear_table, log = False)
    '''

def setup_user(configuration, name, password):
    '''
    >>> gateway_process = configuration.subprocess_gateway(
    ...     configuration.amf_host, 'embassy.py', configuration.verbose)
    >>> ethan, wait = setup_user(configuration, 'ethan', 'kennerly')
    >>> ethan.root.currentLabel
    'lobby'
    >>> ethan, wait = setup_user(configuration, 'robby', 'robby')
    setup_user(..., robby, robby) not at lobby, at login
    >>> ethan.root.currentLabel
    'login'
    '''
    black = configuration.globe_class()
    wait = 4.0 / black._speed
    black.setup(configuration.mock_speed, configuration.setup_client)
    black.root.title_mc.username_txt.text = name
    time.sleep(wait)
    black.root.title_mc.password_txt.text = password
    time.sleep(wait)
    black.root.title_mc.start_btn.dispatchEvent(mouseDown)
    time.sleep(wait)
    if not 'lobby' == black.root.currentLabel:
        print 'setup_user(..., %s, %s) not at lobby, at %s' \
                % (name, password, black.root.currentLabel)
    return black, wait

def setup_example(configuration, *names_passwords):
    '''
    >>> jade, wait = setup_example(configuration, ('jade', 'j'))
    >>> jade.root.currentLabel
    'lobby'
    >>> jade.root.level_mc._txt.text
    '10'

    Sort by first name
    >>> ## ethan, jade, wait = setup_example(configuration, ethan = 'kennerly', jade = 'j')
    >>> ethan, jade, wait = setup_example(configuration, 
    ...     ('ethan', 'kennerly'), ('jade', 'j') )
    >>> ethan.root.currentLabel
    'lobby'
    >>> ethan.root.level_mc._txt.text
    '40'
    >>> jade.root.currentLabel
    'lobby'
    >>> jade.root.level_mc._txt.text
    '10'
    '''
    gateway_process = configuration.subprocess_gateway(
        configuration.amf_host, 'embassy.py', configuration.verbose)
    users_wait = []
    for name, password in names_passwords:
        user, wait = setup_user(configuration, name, password)
        users_wait.append(user)
    users_wait.append(wait)
    return users_wait


def setup_temporary_example():
    r'''Quickly login temporary user whose level is erased on login.
    >>> temporary, wait = setup_example(configuration, 
    ...     ('temporary', 'temporary') )
    >>> sloth = 1.0 / temporary._speed
    '''

def ethan_create_table_example():
    '''
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

    Ethan has played before and wants to host a game.
    >>> mouse_down_and_sleep(ethan, ethan.root.lobby_mc.create_mc,
    ...     1.0 / ethan._speed)
    
    Soon, Ethan enters a room.  Ethan sees board.
    >>> property_diff(ethan, ethan.root, 'currentLabel', 'table')

    Soon, white becomes selected, black is not selected.
    >>> property_diff(ethan, ethan.root.turn_mc, 'currentLabel', 'white')

    The white text changes to his name and black text is not his name.
    >>> property_diff(ethan, ethan.root.turn_mc.white_user_txt, 'text', 'ethan')
    >>> property_diff(ethan, ethan.root.turn_mc.black_user_txt, 'text', 'BLACK')
    '''


def ethan_joris_serial_start_example():
    '''Ethan creates a table and Joris joins.  They start.
    >>> code_unit.inline_examples(
    ...     ethan_create_table_example.__doc__, 
    ...     locals(), globals(), 
    ...     verify_examples = False)

    Precondition:  Ethan has already setup a table.
    Joris logs in.
    >>> joris = configuration.globe_class()
    >>> joris.setup(configuration.mock_speed, configuration.setup_client)
    >>> set_property(joris, joris.root.title_mc.username_txt, 'text', 'joris')
    >>> time.sleep(1.0 / joris._speed)
    >>> set_property(joris, joris.root.title_mc.password_txt, 'text', 'dormans')
    >>> time.sleep(1.0 / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root.title_mc.start_btn,
    ...     1.0 / joris._speed)

    Soon, he enters the lobby.
    >>> property_diff(joris, joris.root, 'currentLabel', 'lobby')

    Joris sees Ethan's room.
    >>> property_diff(joris, joris.root['lobby_mc']['join_mc'], 'currentLabel', 
    ...     'join')
    >>> property_diff(joris, joris.root['lobby_mc']['join_mc']['join_txt'], 'text', 
    ...     'ethan')

    Joris clicks Ethan's room.
    >>> mouse_down_and_sleep(joris, joris.root.lobby_mc.join_mc.enter_btn,
    ...     1.0 / joris._speed)

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
   
    Soon, Ethan sees Joris and his name.
    Ethan sees he is playing white by large icon and name.
    >>> time.sleep(1.0 / joris._speed)
    >>> property_diff(ethan, ethan.root['turn_mc'], 'currentLabel', 
    ...     'white')
    >>> property_diff(ethan, ethan.root['turn_mc']['black_user_txt'], 'text', 
    ...     'joris')
    >>> property_diff(ethan, ethan.root['turn_mc']['white_user_txt'], 'text', 
    ...     'ethan')

    Joris has no extra pieces of cake.
    >>> property_diff(joris, joris.root.extra_stone_gift_mc, 
    ...     'currentLabel', '_0')

    Joris clicks button to start the game.
    >>> mouse_down_and_sleep(joris, joris.root.game_over_mc.start_mc, 1.0 / joris._speed)

    Ethan clicks button to start the game.
    #- >>> mouse_down_and_sleep(ethan, ethan.root.game_over_mc.start_mc, 1.0 / ethan._speed)

    Soon, Joris sees it is his turn to move.
    >>> property_diff(joris, joris.root.turn_mc, 'currentLabel', 'black')
    >>> property_diff(joris, joris.root.turn_veil_mc, 'currentLabel', 'you')
    >>> property_diff(joris, joris.root.game_over_mc, 'currentLabel', 'none')

    Ethan sees it is Joris' turn to move.
    >>> property_diff(ethan, ethan.root.turn_mc, 'currentLabel', 'black')
    >>> property_diff(ethan, ethan.root.turn_veil_mc, 'currentLabel', 'other')
    >>> property_diff(ethan, ethan.root.game_over_mc, 'currentLabel', 'none')
    '''


def set_credential(set_property, username, password):
    '''set username and password
    '''
    news = {'title_mc': {
            'username_txt': {
                'text': username
            },
            'password_txt': {
                'text': password
            },
        },
    }
    set_property # ...


def ethan_joris_start_example():
    '''Ethan creates a table and Joris joins.  They start.
    Ethan enters the lobby and creates a multiplayer game.
    >>> gateway_process = configuration.subprocess_gateway(configuration.amf_host, 'embassy.py', configuration.verbose)
    >>> white = configuration.globe_class()
    >>> black = configuration.globe_class()
    >>> ethan = white
    >>> joris = black
    >>> wait = 4.0 / joris._speed
    >>> ethan.setup(configuration.mock_speed, configuration.setup_client)
    >>> time.sleep(wait)

    Joris logs in.
    >>> joris.setup(configuration.mock_speed, configuration.setup_client)
    >>> set_property(ethan, ethan.root.title_mc.username_txt, 'text', 'ethan')
    >>> time.sleep(0.5 / ethan._speed)
    >>> set_property(joris, joris.root.title_mc.username_txt, 'text', 'joris')
    >>> time.sleep(0.5 / ethan._speed)
    >>> set_property(ethan, ethan.root.title_mc.password_txt, 'text', 'kennerly')
    >>> time.sleep(0.5 / ethan._speed)
    >>> set_property(joris, joris.root.title_mc.password_txt, 'text', 'dormans')
    >>> time.sleep(0.5 / ethan._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root.title_mc.start_btn,
    ...     wait)
    >>> mouse_down_and_sleep(joris, joris.root.title_mc.start_btn,
    ...     wait)
    >>> time.sleep(2.0 + wait)

    Soon, he enters the lobby.
    >>> while property_diff(ethan, ethan.root, 'currentLabel', 'lobby'):
    ...     time.sleep(2); print 'ethan not yet in lobby; sleeping 2'
    >>> property_diff(joris, joris.root, 'currentLabel', 'lobby')

    They go to multiplayer.
    >>> ethan.root.lobby_mc.main_mc.multiplayer_mc.dispatchEvent(mouseDown)
    >>> time.sleep(wait)
    >>> joris.root.lobby_mc.main_mc.multiplayer_mc.dispatchEvent(mouseDown)
    >>> time.sleep(wait)

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

    Precondition:  Ethan has already setup a table.
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
    >>> property_diff(joris, joris.root['turn_mc']['black_user_txt'], 'text', 
    ...     'joris')

    Joris sees that Ethan is playing white by name.
    >>> property_diff(joris, joris.root['turn_mc']['white_user_txt'], 'text', 
    ...     'ethan')
   
    Soon, Ethan sees Joris and his name.
    Ethan sees he is playing white by large icon and name.
    >>> time.sleep(wait)
    >>> property_diff(ethan, ethan.root['turn_mc'], 'currentLabel', 
    ...     'white')
    >>> property_diff(ethan, ethan.root['turn_mc']['black_user_txt'], 'text', 
    ...     'joris')
    >>> property_diff(ethan, ethan.root['turn_mc']['white_user_txt'], 'text', 
    ...     'ethan')

    Ethan sets four extra stones.
    >>> ethan.root.game_over_mc.extra_stone_available_mc._4_mc.dispatchEvent(mouseDown)
    >>> time.sleep(wait)

    Ethan sets four hide.
    >>> ethan.root.game_over_mc.hide_available_mc._4_mc.dispatchEvent(mouseDown)
    >>> time.sleep(wait)

    Joris has no extra stones until playing well.
    >>> property_diff(joris, joris.root.extra_stone_gift_mc, 
    ...     'currentLabel', '_0')

    Joris clicks button to start the game.
    >>> mouse_down_and_sleep(joris, joris.root.game_over_mc.start_mc, wait)

    Soon, Joris sees it is his turn to move.
    >>> property_diff(joris, joris.root.turn_mc, 'currentLabel', 'black')
    >>> property_diff(joris, joris.root.turn_veil_mc, 'currentLabel', 'you')
    >>> property_diff(joris, joris.root.game_over_mc, 'currentLabel', 'none')

    Ethan sees it is Joris' turn to move.
    >>> property_diff(ethan, ethan.root.turn_mc, 'currentLabel', 'black')
    >>> property_diff(ethan, ethan.root.turn_veil_mc, 'currentLabel', 'other')
    >>> property_diff(ethan, ethan.root.game_over_mc, 'currentLabel', 'none')
    >>> from pprint import pprint
    >>> ## pprint(ethan.current)
    >>> ## pprint(joris.current)
    '''



def ethan_joris_autostart_example():
    '''Ethan creates a table and Joris joins.  They start.
    Ethan enters the lobby and creates a multiplayer game.
    >>> gateway_process = configuration.subprocess_gateway(configuration.amf_host, 'embassy.py', configuration.verbose)
    >>> ethan = configuration.globe_class()
    >>> joris = configuration.globe_class()
    >>> ethan.setup(configuration.mock_speed, configuration.setup_client)

    Joris logs in.
    >>> joris.setup(configuration.mock_speed, configuration.setup_client)
    >>> set_property(ethan, ethan.root.title_mc.username_txt, 'text', 'ethan_start')
    >>> time.sleep(0.5 / ethan._speed)
    >>> set_property(joris, joris.root.title_mc.username_txt, 'text', 'joris_start')
    >>> time.sleep(0.5 / ethan._speed)
    >>> set_property(ethan, ethan.root.title_mc.password_txt, 'text', 'kennerly')
    >>> time.sleep(0.5 / ethan._speed)
    >>> set_property(joris, joris.root.title_mc.password_txt, 'text', 'dormans')
    >>> time.sleep(1.0 / ethan._speed)
    >>> mouse_down_and_sleep(ethan, ethan.root.title_mc.start_btn,
    ...     0.5 / ethan._speed)
    >>> mouse_down_and_sleep(joris, joris.root.title_mc.start_btn,
    ...     0.5 / joris._speed)

    Server loads saved state.
    change structure.  break the save state.
    >>> time.sleep(2.0 / ethan._speed)

    Soon, Ethan and Joris see board.
    >>> property_diff(ethan, ethan.root, 'currentLabel', 'table')
    >>> property_diff(joris, joris.root, 'currentLabel', 'table')

    >>> property_diff(joris, joris.root['turn_mc']['black_user_txt'], 'text', 
    ...     'joris_start')

    Joris sees that Ethan is playing white by name.
    >>> property_diff(joris, joris.root['turn_mc']['white_user_txt'], 'text', 
    ...     'ethan_start')
   
    Soon, Ethan sees Joris and his name.
    Ethan sees he is playing white by large icon and name.
    >>> property_diff(ethan, ethan.root['turn_mc']['black_user_txt'], 'text', 
    ...     'joris_start')
    >>> property_diff(ethan, ethan.root['turn_mc']['white_user_txt'], 'text', 
    ...     'ethan_start')

    Joris has no extra pieces of cake.
    >>> property_diff(joris, joris.root.extra_stone_gift_mc, 
    ...     'currentLabel', '_0')

    Soon, Joris sees it is his turn to move.
    >>> property_diff(joris, joris.root.turn_mc, 'currentLabel', 'black')
    >>> property_diff(joris, joris.root.turn_veil_mc, 'currentLabel', 'you')
    >>> property_diff(joris, joris.root.game_over_mc, 'currentLabel', 'none')

    Ethan sees it is Joris' turn to move.
    >>> property_diff(ethan, ethan.root.turn_mc, 'currentLabel', 'black')
    >>> property_diff(ethan, ethan.root.turn_veil_mc, 'currentLabel', 'other')
    >>> property_diff(ethan, ethan.root.game_over_mc, 'currentLabel', 'none')
    '''




def login_example():
    r'''Joris fails and then succeeds to login.
    >>> gateway_process = configuration.subprocess_gateway(configuration.amf_host, 'embassy.py', configuration.verbose)
    >>> joris = configuration.globe_class()
    >>> wait = 4.0 / joris._speed
    >>> joris.setup(configuration.mock_speed, configuration.setup_client)
    >>> time.sleep(wait)

    EXT. LOGIN

    At user name text field, Joris mistypes in his name.
    At password, Joris types in his password.
    He clicks the button to start.

    >>> property_diff(joris, joris.root, 'currentLabel', 'login')
    >>> property_diff(joris, joris.root['gateway_mc'], 'currentLabel', 'connect')
    >>> set_property(joris, joris.root.title_mc.username_txt, 'text', 'Joris')
    >>> time.sleep(wait)
    >>> set_property(joris, joris.root.title_mc.password_txt, 'text', 'dormans')
    >>> time.sleep(wait)
    >>> mouse_down_and_sleep(joris, joris.root.title_mc.start_btn, wait)

    Soon, he sees he made a mistake with the name or password.
    >>> property_diff(joris, joris.root, 'currentLabel', 'login')
    >>> property_diff(joris, joris.root['gateway_mc'], 'currentLabel', 'password')
    
    At user name text field, Joris types in his name.
    At password, Joris types in his password.
    He clicks the button to start.

    >>> set_property(joris, joris.root.title_mc.username_txt, 'text', 'joris')
    >>> time.sleep(wait)
    >>> set_property(joris, joris.root.title_mc.password_txt, 'text', 'dormans')
    >>> time.sleep(wait)
    >>> mouse_down_and_sleep(joris, joris.root.title_mc.start_btn, wait)
    >>> time.sleep(max(wait, 2))

    INT. LOBBY

    Soon, he enters the lobby.
    >>> property_diff(joris, joris.root, 'currentLabel', 'lobby')
    >>> property_diff(joris, joris.root['gateway_mc'], 'currentLabel', 'none')

    #- Joris closes the application.
    #- >>> joris.root.gateway_mc.gotoAndPlay('exit')
    '''





def enter_level_1_example():
    '''Concatenate snippets below.  Doctest offsets line numbers
    from this definition.'''

def enter_level_1_snippet():
    '''Joris enters the lobby and starts a game.
    >>> gateway_process = configuration.subprocess_gateway(configuration.amf_host, 'embassy.py', configuration.verbose)
    >>> joris = configuration.globe_class()
    >>> joris.setup(configuration.mock_speed, configuration.setup_client)
    >>> joris.root['title_mc']['username_txt'].text = 'joris'
    >>> joris.root['title_mc']['password_txt'].text = 'dormans'
    >>> dispatchEvent(joris.root, ['title_mc', 'start_btn', MouseEvent.MOUSE_DOWN])
    >>> time.sleep(1.0 / joris._speed)

    This is Joris' first time playing.
    Joris sees button to start a game against the computer at level 1.
    Joris presses this button.  
    >>> dispatchEvent(joris.root, ['lobby_mc', 'level_1_mc', 'enter_btn', MouseEvent.MOUSE_DOWN])

    Soon, Joris enters a room for level 1.  Joris sees board and opponent.
    >>> time.sleep(1.0 / joris._speed)
    >>> if not joris.root['currentLabel'] == 'table':
    ...     print 'joris.root', joris.root['currentLabel']
    ...     print 'joris.ambassador.receives', joris.ambassador.receives[-1]

    >>> if not joris.root['currentLabel'] == 'table':
    ...     print 'joris.root', joris.root['currentLabel']
    ...     print 'joris.ambassador.receives', joris.ambassador.receives[-1]
    '''

def joris_start_snippet():
    '''
    Joris sees button to start.
    >>> property_diff(joris, joris.root.game_over_mc, 'currentLabel', 'setup')

    Joris clicks button to start the game.
    >>> mouse_down_and_sleep(joris, joris.root.game_over_mc.start_mc, 1.0 / joris._speed)

    Soon, Joris sees it is his turn to move.
    >>> property_diff(joris, joris.root.turn_mc, 'currentLabel', 'black')
    >>> property_diff(joris, joris.root.turn_veil_mc, 'currentLabel', 'you')
    >>> property_diff(joris, joris.root.game_over_mc, 'currentLabel', 'none')

    Joris sees an intersection to press.
    >>> property_diff(joris, joris.root._2_5_mc, 'currentLabel', 'empty_black')

    This intersection is to the right and down.
    >>> if not (1 <= joris.root['_2_5_mc'].x and 1 <= joris.root['_2_5_mc'].y):
    ...     joris.root['_2_5_mc'].x, joris.root['_2_5_mc'].y 

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
    >>> if not joris.root.formation_leap_mc.x != joris.root['_2_2_mc'].x:
    ...     joris.root.formation_leap_mc.x, joris.root['_2_2_mc'].x
    >>> mouse_down_and_sleep(joris, joris.root._2_2_mc, 1.0 / joris._speed)
    >>> property_diff(joris, joris.root._2_2_mc, 'currentLabel', 'question_black')

    Joris also sees a field formation about his previewed stone.
    >>> property_diff(joris, joris.root.formation_field_mc.rotate_0_mc.response_mc, 
    ...     'currentLabel', 'response')
    >>> property_diff(joris, joris.root.formation_field_mc, 
    ...     'x', joris.root['_2_2_mc'].x)
    >>> property_diff(joris, joris.root.formation_field_mc, 
    ...     'y', joris.root['_2_2_mc'].y)

    Joris sees no formation between his previews.
    >>> property_diff(joris, joris.root.formation_leap_mc.rotate_90_mc.response_mc, 
    ...     'currentLabel', 'none')
    >>> if not joris.root.formation_leap_mc.x != joris.root['_2_2_mc'].x:
    ...     joris.root.formation_leap_mc.x, joris.root['_2_2_mc'].x
    
    Previous preview disappears.
    >>> property_diff(joris, joris.root._2_5_mc, 'currentLabel', 'empty_black')

    Joris clicks on the upper left corner.
    Soon, Joris previews a black stone appear there.
    >>> mouse_down_and_sleep(joris, joris.root._0_0_mc, 1.0 / joris._speed)
    >>> property_diff(joris, joris.root._0_0_mc, 'currentLabel', 'question_black')

    Joris sees no formation about his previewed stone.
    >>> property_diff(joris, joris.root.formation_field_mc.rotate_0_mc.response_mc, 
    ...     'currentLabel', 'none')
    >>> if not joris.root.formation_field_mc.x != joris.root['_0_0_mc'].x:
    ...     joris.root.formation_field_mc.x, joris.root['_0_0_mc'].x

    #Hard to verify expiring animations.
    #Soon field formation goes away.
    #>>> time.sleep(2.0 / joris._speed)
    #>>> property_diff(joris, joris.root.formation_field_mc.rotate_0_mc.response_mc, 
    #...     'currentLabel', 'none')
    
    Joris clicks on the upper right star point.
    Soon, Joris sees a black stone appear there.
    >>> mouse_down_and_sleep(joris, joris.root._2_5_mc, 1.0 / joris._speed)
    >>> property_diff(joris, joris.root._2_5_mc, 'currentLabel', 'question_black')
    >>> mouse_down_and_sleep(joris, joris.root._2_5_mc, 1.0 / joris._speed)
    >>> property_diff(joris, joris.root._2_5_mc, 'currentLabel', 'black')

    Joris receives one extra pieces of cake.
    >>> property_diff(joris, joris.root.extra_stone_gift_mc, 
    ...     'currentLabel', '_1')

    Joris also sees a field formation about his placed stone.
    >>> property_diff(joris, joris.root.formation_field_mc.rotate_0_mc.response_mc, 
    ...     'currentLabel', 'response')
    >>> property_diff(joris, joris.root.formation_field_mc, 
    ...     'x', joris.root['_2_5_mc'].x)
    >>> property_diff(joris, joris.root.formation_field_mc, 
    ...     'y', joris.root['_2_5_mc'].y)

    Joris cannot play on top of his own stone.
    Joris cannot play when it is not his turn.
    '''

enter_level_1_example.__doc__ = enter_level_1_snippet.__doc__ \
        + joris_start_snippet.__doc__ + '''
    Joris closes the application.
    >>> joris.root.gateway_mc.gotoAndPlay('exit')
    '''


    

def white_computer_example():
    '''
    >>> code_unit.inline_examples(
    ...     ethan_joris_start_example.__doc__, 
    ...     locals(), globals(), 
    ...     verify_examples = False)
    >>> andre = joris
    >>> wait = 4.0

    Joris presses computer.
    >>> import go_text_protocol
    >>> setup_gtp = go_text_protocol.talk(gateway_process.gtp_envoy, 'set_random_seed 0')
    >>> mouse_down_and_sleep(joris, joris.root.game_over_mc.white_computer_mc.enter_mc, wait / joris._speed)
    >>> property_diff(joris, joris.root.game_over_mc.white_computer_mc, 'currentLabel', 'computer')
    >>> mouse_down_and_sleep(joris, joris.root._2_2_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._2_4_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._2_2_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._2_2_mc, 2 * wait / joris._speed)

    The computer moves white.
    >>> joris.pb()
    ,,,,,,,,,
    ,,,,,,,,,
    ,,X,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,O,,
    ,,,,,,,,,
    ,,,,,,,,,
    >>> mouse_down_and_sleep(joris, joris.root._6_2_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._6_4_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._4_4_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._6_2_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._6_2_mc, 2 * wait / joris._speed)

    Joris presses computer.
    >>> mouse_down_and_sleep(joris, joris.root.game_over_mc.white_computer_mc.enter_mc, wait / joris._speed)
    >>> property_diff(joris, joris.root.game_over_mc.white_computer_mc, 'currentLabel', 'none')

    >>> mouse_down_and_sleep(joris, joris.root._4_2_mc, wait / joris._speed)
    >>> mouse_down_and_sleep(joris, joris.root._4_2_mc, 2 * wait / joris._speed)

    The computer does not move white.
    >>> joris.pb()
    ,,,,,,,,,
    ,,,,,,,,,
    ,,X,,,O,,
    ,,,,,,,,,
    ,,X,,,,,,
    ,,,,,,,,,
    ,,X,,,O,,
    ,,,,,,,,,
    ,,,,,,,,,

    '''

from mock_client import *

@memorably
def mock_gateway(amf_host = None, file = 'embassy.py', 
        verbose = 'error'
        # verbose = 'debug'
        ):
    from embassy import go_club_class
    go_club = go_club_class(configuration.mock_speed)
    internet = internet_borg()
    internet.servers[amf_host] = {amf_port: go_club}
    return go_club


# Remote control master-slave doctests

# do lines after circular import not get imported?
import config
defaults = config.setup_defaults()
configuration = config.borg(defaults)
if type('') == type(configuration.subprocess_gateway):
    configuration.subprocess_gateway = eval(configuration.subprocess_gateway)
if type('') == type(configuration.setup_client):
    configuration.setup_client = eval(configuration.setup_client)
if type('') == type(configuration.globe_class):
    configuration.globe_class = eval(configuration.globe_class)


# examples of use
from master import *
from go_rule_example import *
from lesson_example import *
from board_size_example import *
from user_interface_example import *
from go_variant_example import *
from playtest import *
from concurrent_user_example import *
from stress import *

# overwrite example snippet

active_snippet = '''
# run_examples(shell, profile_doctest.__doc__)
# run_examples(shell, restart_example.__doc__)
# run_examples(shell, white_computer_example.__doc__)
# run_examples(shell, connect_5_5_example.__doc__)
# run_examples(shell, board_7_7_example.__doc__)
# run_examples(shell, board_5_5_example.__doc__)
# run_examples(shell, board_3_3_example.__doc__)
# run_examples(shell, ethan_andre_example.__doc__)
# run_examples(shell, ethan_michael_example.__doc__)
# run_examples(shell, capture_example.__doc__)
# run_examples(shell, master_save_stage_example.__doc__)
# run_examples(shell, ethan_mathijs_example.__doc__)
# run_examples(shell, critical_example.__doc__)
# run_examples(shell, ethan_joris_start_example.__doc__)
# run_examples(shell, real_time_example.__doc__)
# run_examples(shell, real_time_stress_example.__doc__)
# run_examples(shell, echo.__doc__)
'''
# run_examples(shell, capture_example.__doc__)
# run_examples(shell, extra_stone_limit_example.__doc__)
# run_examples(shell, last_move_example.__doc__)
# run_examples(shell, ethan_joris_start_example.__doc__)
# run_examples(shell, master_save_stage_example.__doc__)
# run_examples(shell, ethan_joris_start_example.__doc__)
# run_file_examples(shell, '2010-03-31_ethan_laurens_black_wins_by_8_example.log')
# run_examples(shell, white_formation_example.__doc__)
# run_examples(shell, rapid_click_example.__doc__)
# run_examples(shell, stone_help_example.__doc__)
# run_examples(shell, hide_and_capture_example.__doc__)
# run_examples(shell, extra_stone_and_hide_example.__doc__)
# run_examples(shell, capture_example.__doc__)
# run_examples(shell, ethan_joris_start_example.__doc__)

mock_snippet = '''
# !start python code_explorer.py --import client.py --snippet mock_snippet
# import actionscript; actionscript = reload(actionscript); from actionscript import *
# import remote_control; remote_control = reload(remote_control); from remote_control import *
# import embassy; embassy = reload(embassy); from embassy import *
# import client; client = reload(client); from client import *
''' + active_snippet
# run_examples(shell, capture_example.__doc__)
# run_examples(shell, ethan_joris_start_example.__doc__)
# run_examples(shell, setup_preview_capture_example.__doc__)
# run_examples(shell, score_example.__doc__)
# import embassy; embassy = reload(embassy); from embassy import *

snippet = '''
# !start python code_explorer.py --import client.py --snippet snippet
# import actionscript; actionscript = reload(actionscript); from actionscript import *
# import remote_control; remote_control = reload(remote_control); from remote_control import *
# import embassy; embassy = reload(embassy); from embassy import *
# import client; client = reload(client); from client import *
shell.other.autoCompleteIncludeSingle = True
shell.other.autoCompleteIncludeDouble = True

run_examples(shell, setup_remote_control_snippet.__doc__)
''' + active_snippet
# run_examples(shell, formation_example.__doc__)
# run_examples(shell, capture_example.__doc__)
# run_examples(shell, preview_capture_example.__doc__)
# run_examples(shell, ethan_joris_start_example.__doc__)
# run_examples(shell, score_example.__doc__)
# run_examples(shell, liberty_example.__doc__)
# run_examples(shell, ethan_joris_example.__doc__)
# setup_flash()
# setup_flash()
# run_examples(shell, remote_login_snippet.__doc__)

import code_unit


def profile_doctest(unit_name):
    '''Batch file to draw image of graph of doctest.
    Besides standard library, this requires grof2dot and graphviz.
    >>> profile_doctest('ethan_joris_start_example') #doctest: +ELLIPSIS
    <BLANKLINE>
    ...
    '''
    statement = 'code_unit.doctest_unit(%s)' % unit_name
    profile_code(unit_name, statement, locals(), globals())
   

def profile_code(unit_name, statement, locals_dict, globals_dict):
    '''
    >>> statement = 'code_unit.inline_examples(ethan_joris_autostart_example.__doc__, locals(), globals(), verify_examples = False)'
    >>> unit_name = 'ethan_joris_start_example_shell'
    >>> profile_code(unit_name, statement, locals(), globals()) #doctest: +ELLIPSIS
    <BLANKLINE>
    ...
    '''
    unit_base_name = '%s.profile' % unit_name
    unit_file = 'profile/%s' % unit_base_name
    import cProfile
    # run in context of locals() and globals()
    # cProfile.run(statement, filename=unit_file, sort='cum')
    cProfile.runctx(statement, globals_dict, locals_dict, 
            filename = unit_file)
    import pstats
    profile_statistics = pstats.Stats(unit_file)
    profile_statistics.sort_stats('cum').print_stats(40)
    #time.sleep(1)
    #file = open(unit_file, 'rt')
    #file.close()
    #import os
    #path = os.path.abspath('.')
    #address = os.path.join(path, unit_file)
    command = 'gprof2dot.py -f pstats %s > %s.dot' \
            % (unit_base_name, unit_base_name)
    # command += '\r\npause'
    image_file = '%s.png' % unit_base_name
    command += '\r\ndot -Tpng -o %s %s.dot' \
            % (image_file, unit_base_name)
    command += '\r\n%s' % image_file
    batch_file = '%s.bat' % unit_file
    text.save(batch_file, command)
    
    print 'To make graph, run %s; To see graph open %s' \
            % (batch_file, image_file)
    #time.sleep(1)
    #! subprocess.Popen([batch_file])
    # XXX although batch file executes, subprocess yields error:
    '''
    C:\project\lifeanddeath>gprof2dot.py -f pstats C:\project\lifeanddeath\globe_cla
    ss.setup_formations.profile  1>globe_class.setup_formations.profile.dot
    Traceback (most recent call last):
      File "C:\project\lifeanddeath\gprof2dot.py", line 2515, in <module>
        Main().main()
      File "C:\project\lifeanddeath\gprof2dot.py", line 2447, in main
        self.write_graph()
      File "C:\project\lifeanddeath\gprof2dot.py", line 2511, in write_graph
        dot.graph(profile, self.theme)
      File "C:\project\lifeanddeath\gprof2dot.py", line 2245, in graph
        arrowsize = \"%.2f\" % theme.edge_arrowsize(weight),
      File "C:\project\lifeanddeath\gprof2dot.py", line 2273, in edge
        self.attr_list(attrs)
      File "C:\project\lifeanddeath\gprof2dot.py", line 2288, in attr_list
        self.id(value)
      File "C:\project\lifeanddeath\gprof2dot.py", line 2301, in id
        self.write(s)
      File "C:\project\lifeanddeath\gprof2dot.py", line 2323, in write
        self.fp.write(s)
    IOError: [Errno 9] Bad file descriptor
    close failed: [Errno 9] Bad file descriptor
    '''





if __name__ == '__main__':
    parser = config.default_parser(defaults)
    parser.add_option("--profile", default="",
        dest="profile", help="unit to profile doctest [default: %default]")
    parser.add_option('--psyco', dest='psyco', default='',
            help="specialized python compiler for speed without debugging")
    
    import sys
    (options, args) = config.parse_args(parser, sys.argv)
    configuration.set(options.__dict__)
    configuration.subprocess_gateway = eval(configuration.subprocess_gateway)
    configuration.setup_client = eval(configuration.setup_client)
    configuration.globe_class = eval(configuration.globe_class)
    config.setup_logging(configuration.verbose)

    if setup_flash_master == configuration.setup_client:
        # TODO:  Master client class
        set_property = slave_set_property
        dispatch_event = slave_dispatch_event
        mouse_down_and_sleep = slave_mouse_down_and_sleep
        mouse_down_and_news = slave_mouse_down_and_news

    #from optparse import OptionParser
    #parser = OptionParser()
    #parser.add_option("--unit", default="",
    #    dest="unit", help="unit to doctest [default: %default]")
    #parser.add_option("--debug", default="",
    #    dest="debug", help="unit to debug in doctest [default: %default]")
    #parser.add_option('-v', '--verbose', dest='verbose', default='warning',
    #                help="Increase verbosity")
    #parser.add_option("-p", "--port", default=amf_port,
    #    dest="port", help="port number [default: %default]")
    #parser.add_option("--host", default=amf_host,
    #    dest="host", help="host address [default: %default]")
    #parser.add_option("--unit", default="",
    #    dest="unit", help="unit to doctest [default: %default]")
    #parser.add_option("--debug", default="",
    #    dest="debug", help="unit to debug in doctest [default: %default]")
    #parser.add_option("--profile", default="",
    #    dest="profile", help="unit to profile doctest [default: %default]")
    #parser.add_option('-v', '--verbose', dest='verbose', default='warning',
    #                help="Increase verbosity")
    #parser.add_option('--psyco', dest='psyco', default='',
    #                help="specialized python compiler for speed without debugging")
    #parser.add_option("--wait", default="0",
    #    dest="wait", help="wait afterwards to copy results before shell exits [default: %default]")
    #parser.add_option("--mock", default="",
    #    dest="mock", help="mock networking gateway tests locally and quickly, with PDB trace and exception traceback.  argument is speed of mock network (1 == real-time). [default: %default]")
    #(options, args) = parser.parse_args()

    #verbose = options.verbose
    #log_level = logging_levels[options.verbose]
    #logging.basicConfig(level=log_level)

    #amf_host = options.amf_host
    #amf_port = int(options.amf_port)


    #if options.mock:
    #    print '--mock %s' % options.mock
    #    subprocess_gateway = mock_gateway
    #    setup_client = mock_setup_client
    #    mock_speed = options.mock_speed
    #    # mock_speed = int(options.mock)
    #else:
    #    subprocess_gateway = subprocess_gateway_file
    #    setup_client = setup_amf_client
    #    mock_speed = 1
    if options.psyco:
        # if psyco, cannot pdb.set_trace
        print logging.getLogger().level, 'pscyo.full'
        import psyco
        psyco.full()
        '''
          File "C:\project\lifeanddeath\embassy.py", line 293, in place_stone
            import pdb; pdb.set_trace();; ok, news = prepare_stone(users, user, inter
    section_mc, color, user_news)
          File "C:\Python25\lib\bdb.py", line 190, in set_trace
            frame.f_trace = self.trace_dispatch
          File "C:\Python25\Lib\site-packages\psyco\support.py", line 133, in __seta
    ttr__
            raise AttributeError, "Psyco frame objects are read-only"
        AttributeError: Psyco frame objects are read-only
        '''
    # Inspect examples
    if options.unit:
        unit = eval(options.unit)
        code_unit.doctest_unit(unit)
    elif options.debug_unit:
        unit = eval(options.debug_unit)
        import doctest
        doctest.debug_src(unit.__doc__, globs=globals())
    elif options.profile:
        profile_doctest(options.profile)
    elif options.test:
        units = globals().values()
        ## units.remove(setup_example)
        code_unit.doctest_units(units)

    if options.wait:
        code_unit.wait(options.wait)

