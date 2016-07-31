#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Multiple user functions that are excluded from Flash client but needed by server.
'''
__author__ = 'Ethan Kennerly'
from super_user import *
import configuration

# single user-other algorithms

def to_resize_board(old_length, new_size):
    '''If at different size, ask client to resize their board.
    >>> resized = to_resize_board(9, '_9_9')
    >>> resized.get('currentLabel')
    >>> resized = to_resize_board(9, '_5_5')
    >>> resized.get('currentLabel')
    '_5_5'
    >>> resized = to_resize_board(5, '_5_5')
    >>> resized.get('currentLabel')
    '''
    reply = {}
    if old_length != int(new_size[1]):
        from actionscript import MouseEvent
        reply = {'currentLabel': new_size,
            'game_over_mc': {
                new_size + '_mc': {
                    'confirm_mc': {
                        'dispatchEvent': MouseEvent.MOUSE_DOWN
                    }
                }
            }
        }
    return reply


class template_borg:
    '''Multiple instances share same state.
    http://code.activestate.com/recipes/66531/'''
    __shared_state = {}
    user = None
    def __init__(self):
        self.__dict__ = self.__shared_state
        if not self.user:
            self.user = globe_class()
            self.user.create(8.0)
            self.user.setup_events()


def to_clear_table(root, old_length, length = 9):
    '''Initial items that differ from current 
        _#_#_mc, turn_mc, game_over_mc, *_last_move_mc, *_gift_mc
        formation_*_mc, len(intersection_mc_array)
        play_history, score_mc.bar_mc, sgf_file_txt, comment_mc
        _#_#_strike_mc, _#_#_mc, gibs_mc, tutor_mc, menu_mc, sgf_file_txt
        clear info and info box.

        TODO:  _#_#_mc.teritory_mc
    >>> user = user_as.globe_class()
    >>> user.create(1)
    >>> user.setup_events()
    >>> from mock_client import echo_protocol_class
    >>> user.ambassador = echo_protocol_class()
    >>> length = len(user.intersection_mc_array)
    >>> to_clear_table(user.root, length)
    {'info': {'info': {}}, 'sequence': [{'sequence': []}]}
    >>> user.root._0_0_mc.gotoAndPlay('white')
    >>> to_clear_table(user.root, length).get('_0_0_mc')
    {'currentLabel': 'empty_black'}
    >>> olds = imitate_news(user.root, to_clear_table(user.root, length))
    
    >>> user.root.turn_mc.gotoAndPlay('white')
    >>> changed = to_clear_table(user.root, length)
    >>> changed.get('turn_mc') or changed
    {'currentLabel': 'black'}

    clear sequence.  for example, see globe_class.push_news
    >>> changed['sequence']
    [{'sequence': []}]
    >>> olds = imitate_news(user.root, to_clear_table(user.root, length))
    
    >>> user.root.turn_mc.white_user_txt.text = 'ethan'
    >>> to_clear_table(user.root, length).get('turn_mc')
    {'white_user_txt': {'text': 'WHITE'}}
    >>> olds = imitate_news(user.root, to_clear_table(user.root, length))
    
    >>> user.root.game_over_mc.gotoAndPlay('setup')

    #- >>> user.root.formation_jump_mc.rotate_0_mc.response_mc.gotoAndPlay('response')
    >>> to_clear_table(user.root, length).get('game_over_mc')
    {'currentLabel': 'none'}
    >>> olds = imitate_news(user.root, to_clear_table(user.root, length))
    >>> len(user.intersection_mc_array)
    9
    
    #- >>> user.root.formation_jump_mc.rotate_0_mc.response_mc.currentLabel
    #- 'none'

    Clear score.
    >>> user.root.score_mc.bar_mc.gotoAndPlay('_9')
    >>> to_clear_table(user.root, length).get('score_mc').get('bar_mc')
    {'currentLabel': '_0'}
    >>> olds = imitate_news(user.root, to_clear_table(user.root, length))
    >>> user.root.score_mc.bar_mc.currentLabel
    '_0'
    >>> user.root.score_mc.bar_mc.marker_mc.capture_mc.currentLabel
    '_0'
    >>> user.root.score_mc.bar_mc.marker_mc.currentLabel
    'neutral'
    >>> user.root.score_mc.bar_mc.marker_mc.change_txt.text
    '0'

    Reset sgf file.
    >>> user.root.sgf_file_txt.text
    ''

    Clear comment, tutor, menu, sgf_file_txt, sgf_path_txt, option_mc, and pass.
    >>> user.root.pass_white_mc.gotoAndPlay('white')
    >>> user.root.menu_mc.gotoAndPlay('show')
    >>> user.root.sgf_file_txt.text = 'sgf/beginner/hide_7_7.sgf'
    >>> user.root.sgf_path_txt.text = '[1]'
    >>> user.root.option_mc.block_mc.gotoAndPlay('show')
    >>> user.root.comment_mc.currentLabel
    'none'
    >>> user.root.tutor_mc.currentLabel
    'none'
    >>> user.root.comment_mc.gotoAndPlay('comment')
    >>> user.root.tutor_mc.gotoAndPlay('start')
    >>> if not user.root.comment_mc._txt.text.startswith('_txt'):
    ...     user.root.comment_mc._txt.text
    >>> user.root.comment_mc._txt.text = 'WELL DONE!'
    >>> user.root._0_0_mc.last_move_mc.gotoAndPlay('black')
    >>> to_clear_comment_news = to_clear_table(user.root, length)
    >>> if not to_clear_comment_news.get('comment_mc').get('_txt').get('text').startswith('_txt'):
    ...     to_clear_comment_news
    >>> if not 'none' == to_clear_comment_news.get('pass_white_mc').get('currentLabel'):
    ...     to_clear_comment_news
    >>> if not 'none' == to_clear_comment_news.get('tutor_mc').get('currentLabel'):
    ...     to_clear_comment_news
    >>> if not 'none' == to_clear_comment_news.get('menu_mc').get('currentLabel'):
    ...     to_clear_comment_news

    Clear last_move
    >>> if not to_clear_comment_news.get('_0_0_mc').get('last_move_mc').get('currentLabel') == 'none':
    ...     to_clear_comment_news
    >>> if not to_clear_comment_news.get('sgf_file_txt').get('text') == '':
    ...     to_clear_comment_news
    >>> if not to_clear_comment_news.get('sgf_path_txt').get('text') == '[]':
    ...     to_clear_comment_news
    >>> if not to_clear_comment_news.get('option_mc').get('block_mc').get('currentLabel') == 'none':
    ...     to_clear_comment_news

    Clear strikes.  Clear gibs.
    >>> user.root._0_0_mc.gibs_mc.gotoAndPlay('black')
    >>> user.root._0_0_strike_mc.north_mc.gotoAndPlay('black_danger')
    >>> user.root.cursor_mc.gotoAndPlay('play')
    >>> user.root.cursor_mc.act_mc.gotoAndPlay('busy')
    >>> to_clear_strike_news = to_clear_table(user.root, length)
    >>> if not to_clear_strike_news.get('_0_0_strike_mc').get('north_mc').get('currentLabel') == 'none':
    ...     to_clear_strike_news
    >>> if not to_clear_strike_news.get('_0_0_mc').get('gibs_mc').get('currentLabel') == 'none':
    ...     to_clear_strike_news

    Clear cursor
    >>> if not to_clear_strike_news.get('cursor_mc').get('currentLabel') == 'none':
    ...     to_clear_strike_news
    >>> if not to_clear_strike_news.get('cursor_mc').get('act_mc').get('currentLabel') == 'none':
    ...     to_clear_strike_news

    clear info and info box.
    >>> moonhyoung = user
    >>> moonhyoung.root.info_mc.decoration_mc.pattern_txt.text = 'FIELD'
    >>> moonhyoung.info = {'_2_2_mc': []}
    >>> to_clear_info_news = to_clear_table(moonhyoung.root, length)
    >>> if not to_clear_info_news['info_mc']['decoration_mc']['pattern_txt']['text'] == '':
    ...     to_clear_info_news
    >>> to_clear_info_news['info']
    {'delete': True}

    For acceptance, see client.py:restart_example
    '''
    old_root = root
    #new_user = template_borg().user
    #new_user = user_as.globe_class()
    #new_user.create(1) # XXX slow
    #new_root = new_user.root
    new_tree = user_as.stage_borg().tree
    changed = {}
    child_names = []
    for row in range(length):
        for column in range(length):
            intersection_name = get_intersection_name(row, column)
            child_names.append(intersection_name)
            intersection_strike_name = '_%i_%i_strike_mc' % (row, column)
            child_names.append(intersection_strike_name)
    child_names.append('turn_mc')
    child_names.append('game_over_mc')
    child_names.append('extra_stone_gift_mc')
    child_names.append('hide_gift_mc')
    child_names.append('score_mc')
    child_names.append('sgf_file_txt')
    child_names.append('play_sgf_mc')
    child_names.append('comment_mc')
    child_names.append('tutor_mc')
    child_names.append('cursor_mc')
    child_names.append('menu_mc')
    child_names.append('pass_white_mc')
    child_names.append('pass_mc')
    child_names.append('option_mc')
    child_names.append('sgf_path_txt')
    child_names.append('info_mc')
    old_children = []
    new_children = []
    old = {}
    for child_name in child_names:
        old_branch = unique_family_tree(old_root[child_name], {})
        if old_branch:
            old = upgrade(old, {child_name: old_branch})
    new = user_as.get_branch(new_tree, child_names)
        #- old_children.append(old_root[child_name])
        #new_children.append(new_root[child_name])
    #- old = user_as.compose_root(user_as.insert_label, *old_children)
    #new = user_as.compose_root(user_as.insert_label, *new_children)
    #mobile_names = []
    #for index in range(new_root.numChildren):
    #    child = new_root.getChildAt(index)
    #    if child.name.startswith('formation'):
    #        mobile_names.append(child.name)
    #- mobile_names.append('white_last_move_mc')
    #- mobile_names.append('black_last_move_mc')
    #old_mobiles = []
    #new_mobiles = []
    #for mobile_name in mobile_names:
    #        old_mobiles.append(old_root[mobile_name])
    #        new_mobiles.append(new_root[mobile_name])
    #mobile_old = user_as.compose_root(user_as.insert_label_and_position, 
    #        *old_mobiles)
    #mobile_new = user_as.compose_root(user_as.insert_label_and_position, 
    #        *new_mobiles)
    #old = upgrade(old, mobile_old)
    #new = upgrade(new, mobile_new)
    changed = user_as.change(old, new)
    size = '_%i_%i' % (length, length)
    resized = to_resize_board(old_length, size)
    changed = upgrade(resized, changed)
    clear_sequence = {'sequence': []}
    changed['sequence'] = [clear_sequence]
    ## import pdb; pdb.set_trace(); 
    clear_info = {'delete': True}
    changed['info'] = clear_info
    return changed



# user-partner algorithms


def get_partner(users, user):
    '''Log error if color is not black or white, and return no partner.
    >>> users = setup_users(1)
    >>> laurens = users.get('laurens')
    >>> old_level = logging.getLogger().level
    >>> get_partner(users, laurens)
    >>> logging.getLogger().setLevel(logging.CRITICAL)
    >>> logging.getLogger().setLevel(old_level)
    >>> users, ethan, mathijs = setup_users_white_black('ethan', 'mathijs')
    >>> ethan == get_partner(users, mathijs)
    True
    '''
    partner_name = None
    color = get_color(user)
    if not color:
        return None
    if 'black' == color:
        partner_name = user.root.turn_mc.white_user_txt.text
    elif 'white' == color:
        partner_name = user.root.turn_mc.black_user_txt.text
    else:
        logging.error('get_partner:  which color is this? %s' % color)
    partner = users.get(partner_name)
    return partner


def set_partner(users, user, partner_name, reciprocate = True):
    '''Set partner and color of partner
    >>> users = setup_users(1)
    >>> user = users.get('joris')
    >>> set_color(user, 'white')
    >>> partner = set_partner(users, user, 'ethan')
    >>> get_color(partner)
    'black'
    >>> set_color(user, 'black')
    >>> partner = set_partner(users, user, 'ethan')
    >>> get_color(partner)
    'white'

    If no color, then become black, and partner:  white.
    >>> andre = users.get('andre')
    >>> partner = set_partner(users, andre, 'lukasz')
    >>> get_color(andre)
    'black'
    >>> get_color(partner)
    'white'

    And set partner to you.
    >>> users.get('lukasz') == get_partner(users, andre)
    True
    '''
    color = get_color(user)
    if not color:
        color = 'black'
        set_color(user, color)
    if 'black' == color:
        user.root.turn_mc.white_user_txt.text = partner_name
        partner_color = 'white'
    elif 'white' == color:
        user.root.turn_mc.black_user_txt.text = partner_name
        partner_color = 'black'
    else:
        logging.error('set_partner: which color?  %s' % color)
    partner = users.get(partner_name)
    set_color(partner, partner_color)
    if not user == get_partner(users, partner):
        # In case of error, prevent infinite loop.
        set_partner(users, partner, user.root.title_mc.username_txt.text,
                reciprocate = False)
    return partner

import copy
def tell(partner, news):
    '''Copy news so original is not modified.
    >>> old_level = logging.getLogger().level
    >>> logging.getLogger().setLevel(logging.CRITICAL)
    >>> tell(None, {})
    >>> logging.getLogger().setLevel(old_level)
    '''
    if partner:
        news = copy.deepcopy(news)
        partner.publish(news)
    else:
        tell_partner_log = 'tell: no partner %s' % (news.keys())
        logging.error(tell_partner_log)
        ## import pdb; pdb.set_trace();

# deprecate for get_partner; tell
#def tell_partner(users, user, color, partner_news):
#    # tell_partner_log = 'tell_partner: %s: %s' % (color, partner_news)
#    # logging.info(tell_partner_log)
#    partner = get_partner(users, user)
#    if partner:
#        tell(partner, partner_news)


def setup_partners():
    user = user_as.globe_class()
    user.create(1)
    partner = user_as.globe_class()
    partner.create(1)
    set_color(user, 'black')
    return user, partner

def setup_board_3_3():
    user, partner = setup_partners()
    user.intersection_mc_array = user_as.get_intersection_array(user.root, 3)
    partner.intersection_mc_array = user_as.get_intersection_array(partner.root, 3)
    import referee
    return user, partner, referee.clear_board_3_3


def get_capture_news(user, partner, intersection_mc):
    '''
    must have already validated move.
    merge black board with last move.
    convert flash to board array and last row and column.
    update board
    convert new board array to flash.
    for each partner, compare each intersection in new board and notify changes.
    >>> user, partner = setup_partners()
    >>> user.root.score_mc.bar_mc.marker_mc.capture_mc.gotoAndPlay('_0')
    >>> board = referee.assassin_board
    >>> board_news = board_to_news(board, user.intersection_mc_array, 'black')
    >>> olds = user_as.imitate_news(user.root, board_news)
    >>> user.pb()
    ,,,,,,,,,
    ,,,,,,,,,
    ,,XX,XX,,
    ,,,,,,,,,
    ,,,XX,,,,
    ,,X,O,X,,
    ,,XXO,X,,
    ,,XO,O,,,
    ,,,/O,,,,
    >>> intersection_mc = user.root._7_4_mc
    >>> intersection_mc.gotoAndPlay('play_black')
    >>> user.root.option_mc.gibs_mc.gotoAndPlay('show')
    >>> partner.root.option_mc.gibs_mc.gotoAndPlay('none')
    >>> news, partner_news, new_board, black_capture_total = get_capture_news(
    ...     user, partner, intersection_mc)
    >>> referee.pb(new_board)
    ,,,,,,,,,
    ,,,,,,,,,
    ,,XX,XX,,
    ,,,,,,,,,
    ,,,XX,,,,
    ,,X,O,X,,
    ,,XXO,X,,
    ,,X,*O,,,
    ,,,XO,,,,
    >>> news.get('_7_3_mc').get('currentLabel')
    'empty_black'
    >>> news.get('_7_4_mc').get('currentLabel')
    'black'
    >>> news.get('_8_3_mc').get('hide_mc').get('currentLabel')
    'reveal'
    >>> partner_news.get('_8_3_mc').get('hide_mc').get('currentLabel')
    'reveal'
    >>> news.get('_8_3_mc').get('currentLabel')
    'black'

    So that GnuGo may score latest SGF.  History reveals the assassin
    >>> user.play_history[-1]
    {'unhide': [(8, 3)]}

    Add to black captures.
    >>> news.get('score_mc').get('bar_mc').get('marker_mc').get('capture_mc').get('currentLabel')
    '_1'

    Optionally, show gibs at each capture.
    >>> news.get('_7_3_mc').get('gibs_mc').get('currentLabel')
    'white'
    >>> partner_news.get('_7_3_mc')
   
    capture on 3x3
    >>> user, partner, board = setup_board_3_3()
    >>> board_news = board_to_news(referee.board_pre_capture_3_3, 
    ...     user.intersection_mc_array, 'black')
    >>> olds = user_as.imitate_news(user.root, board_news)
    >>> user.pb()
    ,,,
    ,,X
    ,,O

    By default, do not warn of liberty shortage.
    If no capture, may still get news.
    >>> intersection_mc = user.root._2_1_mc
    >>> intersection_mc.gotoAndPlay('play_black')
    >>> user.root.option_mc.gibs_mc.gotoAndPlay('show')
    >>> news, partner_news, new_board, black_capture_total = get_capture_news(
    ...     user, partner, intersection_mc)
    >>> news.get('_2_1_mc').get('block_south_mc')
    >>> partner_news.get('_2_1_mc').get('block_south_mc')

    Optionally, warn user of liberty blockage.
    >>> from referee import pb
    >>> user.root.option_mc.block_mc.gotoAndPlay('show')

    Optionally win by first capture but do not check that here.
    >>> user.root.option_mc.first_capture_mc.gotoAndPlay('show')
    >>> user.root._2_2_mc.formation_mc.gotoAndPlay('white_attack_curse')
    >>> user.root._2_2_mc.territory_mc.gotoAndPlay('white_dead')
    >>> news, partner_news, new_board, black_capture_total = get_capture_news(
    ...     user, partner, intersection_mc)
    >>> news.get('_2_1_mc').get('block_south_mc')
    {'currentLabel': 'black_block'}
    >>> partner_news.get('_2_1_mc').get('block_south_mc')
    >>> pb(new_board)
    ,,,
    ,,X
    ,*,
    >>> news.get('game_over_mc')

    At each capture, remove any formation.
    >>> news['_2_2_mc']['formation_mc']['currentLabel']
    'none'
    
    At each capture, remove any dead warning.
    >>> news['_2_2_mc']['territory_mc']['currentLabel']
    'none'
    
    Setup again.
    >>> user, partner, board = setup_board_3_3()
    >>> board_news = board_to_news(referee.board_pre_capture_3_3, 
    ...     user.intersection_mc_array, 'black')
    >>> olds = user_as.imitate_news(user.root, board_news)
    >>> user.pb()
    ,,,
    ,,X
    ,,O

    Optionally, warn partner of liberty blockage.
    >>> user.root.option_mc.block_mc.gotoAndPlay('show')
    >>> intersection_mc = partner.root._1_1_mc
    >>> intersection_mc.gotoAndPlay('play_white')
    >>> news, partner_news, new_board, black_capture_total = get_capture_news(
    ...     user, partner, intersection_mc)
    >>> news.get('_1_2_mc').get('block_west_mc')
    {'currentLabel': 'black_danger'}
    >>> partner_news.get('_1_2_mc').get('block_west_mc')
    >>> pb(new_board)
    ,,,
    ,@X
    ,,O

    Setup again.
    >>> user, partner, board = setup_board_3_3()
    >>> board_news = board_to_news(referee.board_pre_capture_3_3, 
    ...     user.intersection_mc_array, 'black')
    >>> olds = user_as.imitate_news(user.root, board_news)
    >>> user.pb()
    ,,,
    ,,X
    ,,O

    Optionally, warn user and partner of liberty blockage.
    >>> user.root.option_mc.block_mc.gotoAndPlay('show')
    >>> partner.root.option_mc.block_mc.gotoAndPlay('show')
    >>> intersection_mc = partner.root._1_1_mc
    >>> intersection_mc.gotoAndPlay('play_white')
    >>> news, partner_news, new_board, black_capture_total = get_capture_news(
    ...     user, partner, intersection_mc)
    >>> news.get('_1_2_mc').get('block_west_mc')
    {'currentLabel': 'black_danger'}
    >>> partner_news.get('_1_2_mc').get('block_west_mc')
    {'currentLabel': 'black_danger'}
    >>> pb(new_board)
    ,,,
    ,@X
    ,,O

    Include in this liberty side.
    >>> news.get('_0_2_mc') # .get('liberty_south_mc')
    >>> user.root.liberty_mc.gotoAndPlay('show')
    >>> partner.root.liberty_mc.gotoAndPlay('show')
    >>> news, partner_news, new_board, black_capture_total = get_capture_news(
    ...     user, partner, intersection_mc)
    >>> news.get('_0_2_mc').get('liberty_south_mc')
    {'currentLabel': 'black_danger'}
    >>> partner_news.get('_0_2_mc').get('liberty_south_mc')
    {'currentLabel': 'black_danger'}

    Optionally show connected stones.
    >>> user.root.connected_mc.gotoAndPlay('show')
    >>> partner.root.connected_mc.gotoAndPlay('show')
    >>> user.root._1_1_mc.gotoAndPlay('white')
    >>> intersection_mc = partner.root._2_1_mc
    >>> intersection_mc.gotoAndPlay('play_white')
    >>> news, partner_news, new_board, black_capture_total = get_capture_news(
    ...     user, partner, intersection_mc)
    >>> pb(new_board)
    ,,,
    ,OX
    ,@O
    >>> from pprint import pprint
    >>> if not '_1100' == news['_2_1_mc']['white_shape_mc']['currentLabel']:
    ...     pprint(news)

    Connect partner even if user does not connect.
    >>> user.root.connected_mc.gotoAndPlay('none')
    >>> news, partner_news, new_board, black_capture_total = get_capture_news(
    ...     user, partner, intersection_mc)
    >>> pb(new_board)
    ,,,
    ,OX
    ,@O
    >>> from pprint import pprint
    >>> if not partner_news.get('_2_1_mc').get('white_shape_mc').get('currentLabel') == '_1100':
    ...     pprint(partner_news)

    #+ TODO:  enable call of client acceptance tests
    #+ Show suicide
    #+ >>> code_unit.doctest_unit(client.capture_example, log = False)
    '''
    news = {}
    if 'black' == get_color(user):
        intersection_mc_array = user.intersection_mc_array
        partner_news = {}
        play_history = user.play_history
    elif 'black' == get_color(partner):
        intersection_mc_array = partner.intersection_mc_array
        # XXX see client.capture_example: black previews and white moves in real-time.
        partner_news = clear_preview(partner)
        play_history = partner.play_history
    else:
        logging.error('get_capture_news: who is black? %s' % intersection_mc.name)
    board_text = flash_to_text(intersection_mc_array)
    board = referee.text_to_array(board_text)
    new_mark = intersection_mc_to_text(intersection_mc)
    row, column = get_row_column(intersection_mc.name)
    capture_enabled = True
    if not capture_enabled:
        new_board = copy.deepcopy(board)
        new_board[row][column] = new_mark
        black_capture_total = 0
    else:
        # update board
        revealed_board, assassins = referee.foresee_black_assassins(board, 
                new_mark, row, column)
        if assassins:
            for r, c in assassins:
                intersection_name = user_as.get_intersection_name(r, c)
                revealed = {intersection_name:  {'currentLabel': 'black',
                    'hide_mc': {'currentLabel': 'reveal'}}}
                news = upgrade(news, revealed)
                partner_news = upgrade(partner_news, revealed)
                unhide(play_history, r, c)
        new_board = referee.update_board(revealed_board, (row, column))
        # capture score
        captures = referee.find_capture(revealed_board, (row, column))
        if captures:
            if 'black' == get_color(user):
                capture_color = 'white'
                black_capture_count = len(captures)
                capture_score_news, black_capture_total = add_black_capture_news(user, black_capture_count)
                news = upgrade(news, capture_score_news)
            elif 'black' == get_color(partner):
                capture_color = 'black'
                black_capture_count = 0 - len(captures)
                capture_score_news, black_capture_total = add_black_capture_news(partner, black_capture_count)
                partner_news = upgrade(partner_news, capture_score_news)
            else:
                logging.error('get_capture_news: count: who is black? %s' % intersection_mc.name)
            # clear formation
            clear_formation_news = update_child_label(user.intersection_mc_array, captures, 'formation_mc', 'none')
            news = upgrade(news, clear_formation_news)
            partner_clear_formation_news = update_child_label(partner.intersection_mc_array, captures, 'formation_mc', 'none')
            partner_news = upgrade(partner_news, partner_clear_formation_news)
            # clear dead warning
            remove_dead_news = update_child_label(user.intersection_mc_array, 
                captures, 'territory_mc', 'none', 
                ['black_dead', 'white_dead'])
            news = upgrade(news, remove_dead_news)
            partner_remove_dead_news = update_child_label(partner.intersection_mc_array, 
                captures, 'territory_mc', 'none', 
                ['black_dead', 'white_dead'])
            partner_news = upgrade(partner_news, remove_dead_news)
            # gibs
            gibs_enabled = 'show' == user.root.option_mc.gibs_mc.currentLabel
            if gibs_enabled:
                gibs_news = set_coordinate_news(captures, 'gibs_mc', capture_color)
                news = upgrade(news, gibs_news)
            partner_gibs_enabled = 'show' == partner.root.option_mc.gibs_mc.currentLabel
            if partner_gibs_enabled:
                partner_gibs_news = set_coordinate_news(captures, 'gibs_mc', capture_color)
                partner_news = upgrade(partner_news, partner_gibs_news)
        else:
            black_capture_total = 0
    suicide_enabled = 'show' == user.root.suicide_mc.currentLabel
    if suicide_enabled:
    #- if 'black' == get_color(user):
        suicide_news = get_suicide_news(new_board, user)
        news = upgrade(news, suicide_news)
    block_enabled = 'show' == user.root.option_mc.block_mc.currentLabel
    if block_enabled:
        user_block_news = get_block_news(user.intersection_mc_array, new_board)
        news = upgrade(news, user_block_news)
    partner_block_enabled = 'show' == partner.root.option_mc.block_mc.currentLabel
    if partner_block_enabled:
        partner_block_news = get_block_news(partner.intersection_mc_array, new_board)
        partner_news = upgrade(partner_news, partner_block_news)
    liberty_enabled = 'show' == user.root.liberty_mc.currentLabel
    if liberty_enabled:
        user_liberty_news = get_liberty_news(user.intersection_mc_array, new_board)
        news = upgrade(news, user_liberty_news)
    partner_suicide_enabled = 'show' == partner.root.suicide_mc.currentLabel
    if partner_suicide_enabled:
        partner_suicide_news = get_suicide_news(new_board, partner)
        partner_news = upgrade(partner_news, partner_suicide_news)
    partner_liberty_enabled = 'show' == partner.root.liberty_mc.currentLabel
    if partner_liberty_enabled:
        partner_liberty_news = get_liberty_news(partner.intersection_mc_array, new_board)
        partner_news = upgrade(partner_news, partner_liberty_news)
    # for strike_news, modify playtest:emmet_capture_3_3_example
    strike_enabled = 'show' == user.root.strike_mc.currentLabel
    if strike_enabled:
        strike_news = get_strike_news(user.intersection_mc_array, new_board, user.root, row, column, captures)
        news = upgrade(news, strike_news)
    partner_strike_enabled = 'show' == partner.root.strike_mc.currentLabel
    if partner_strike_enabled:
        partner_strike_news = get_strike_news(partner.intersection_mc_array, new_board, partner.root, row, column, captures)
        partner_news = upgrade(partner_news, partner_strike_news)
    connected_enabled = 'show' == user.root.connected_mc.currentLabel
    if connected_enabled:
        connected_news = get_connected_news(user.intersection_mc_array, new_board)
        news = upgrade(news, connected_news)
    partner_connected_enabled = 'show' == partner.root.connected_mc.currentLabel
    if partner_connected_enabled:
        partner_connected_news = get_connected_news(partner.intersection_mc_array, new_board)
        partner_news = upgrade(partner_news, partner_connected_news)
    player_color = get_color(user)
    board_news = board_to_news(new_board, user.intersection_mc_array, 
            player_color)
    news = upgrade(news, board_news)
    partner_color = get_color(partner)
    partner_board_news = board_to_news(new_board, 
            partner.intersection_mc_array, partner_color)
    partner_news = upgrade(partner_news, partner_board_news)
    news_log = 'get_capture_news: user:%s \npartner:%s' % (news, partner_news)
    logging.debug(news_log)
    return news, partner_news, new_board, black_capture_total


# end user-partner algorithms


# multiple users algorithms

def _create_user(users, name, password, speed = 1):
    '''
    >>> users = _create_user({}, 'h1', 'hva1')
    '''
    user = user_class()
    user.create(speed)
#    name.setup_events()
    become_observant(user)
    user.root.title_mc.username_txt.text = name
    user.root.title_mc.password_txt.text = password
    user.users = users
    users[name] = user
    return users


def setup_users(speed, setup_events = True, minimum = False):
    '''
    To be quicker, do not setup events.
    >>> users = setup_users(16.0, setup_events = False)
    >>> users.get('template').root.liberty_mc.currentLabel
    'none'
    >>> users.get('joris').root.option_mc.block_mc.currentLabel
    'show'
    >>> users.get('joris').root.profit_mc.currentLabel
    'show'
    >>> users.get('ethan') != users.get('joris')
    True
    >>> users.get('lukasz') != users.get('joris')
    True
    >>> users.get('moonhyoung').root._1_2_mc._event_type
    
    To be quicker, refers other users of same type.
    >>> users.get('template') == users.get('ethan')
    False
    >>> users.get('intermediate') == users.get('joris')
    True
    >>> users.get('beginner') == users.get('lukasz')
    True
    >>> users.get('beginner') == users.get('lukasz')
    True

    Each user has handle on users.
    >>> lukasz = users.get('lukasz')
    >>> lukasz.users == users
    True

    Steven is level 50, loaded from file.
    >>> steven = users.get('steven')
    >>> steven.root.level_mc._txt.text
    '50'

    Slow to setup events
    >>> import timeit
    >>> timer = timeit.Timer(stmt = 'users = setup_users(16.0)', setup = 'from super_users import setup_users')
    >>> setup_second = timer.timeit(1)
    >>> if not setup_second < 1.0: setup_second

    Temporary user erased each time.
    >>> news = enter(users, users.get('temporary'))
    >>> news.get('currentLabel')
    'lobby'
    '''
    users = {}
    for number in range(0, configuration.guest_max):
        name = 'guest%s' % number
        users = _create_user(users, name, name, speed)
    # setup template
    template = user_class()
    template.create(speed)
#    template.setup_events()
    template.root.title_mc.username_txt.text = 'template'
    template.root.title_mc.password_txt.text = 'template'
    template.users = users
    users['template'] = template
    # setup ethan
    ethan = user_class()
    ethan.create(speed)
    ethan.root.title_mc.username_txt.text = 'ethan'
    ethan.root.title_mc.password_txt.text = 'kennerly'
    ethan.root.level_mc._txt.text = '40'
    ethan.users = users
    users['ethan'] = ethan
    if not minimum:
        users = setup_users_all(users)
    if setup_events:
        already_set = []
        for user in users.values():
            if user not in already_set:
                user.setup_events()
                already_set.append(user)
    return users


def setup_users_all(users):
    # setup joris
    joris = user_class()
    joris.create(speed)
#    joris.setup_events()
    become_observant(joris)
    joris.root.title_mc.username_txt.text = 'joris'
    joris.root.title_mc.password_txt.text = 'dormans'
    joris.root.level_mc._txt.text = '10'
    joris.users = users
    users['joris'] = joris
    users['intermediate'] = joris
    # setup jade
    jade = user_class()
    jade.create(speed)
#    jade.setup_events()
    become_observant(jade)
    jade.root.title_mc.username_txt.text = 'jade'
    jade.root.title_mc.password_txt.text = 'brewer'
    jade.root.level_mc._txt.text = '10'
    jade.users = users
    users['jade'] = jade
    # auto start ethan
    ethan_start = user_class()
    ethan_start.create(speed)
#    ethan_start.setup_events()
    ethan_start.root.title_mc.username_txt.text = 'ethan_start'
    ethan_start.root.title_mc.password_txt.text = 'e'
    ethan_start.users = users
    users['ethan_start'] = ethan_start
    # mathijs
    mathijs = user_class()
    mathijs.create(speed)
#    mathijs.setup_events()
    become_observant(mathijs)
    mathijs.root.title_mc.username_txt.text = 'mathijs'
    mathijs.root.title_mc.password_txt.text = 'debruin'
    mathijs.root.level_mc._txt.text = '10'
    mathijs.users = users
    users['mathijs'] = mathijs
    # setup lukasz
    lukasz = user_class()
    lukasz.create(speed)
#    lukasz.setup_events()
    olds = imitate_news(lukasz.root, get_aware_news())
    lukasz.root.title_mc.username_txt.text = 'lukasz'
    lukasz.root.title_mc.password_txt.text = 'l'
    lukasz.users = users
    users['lukasz'] = lukasz
    # setup steven
    steven = user_class()
    steven.create(speed)
#    steven.setup_events()
    steven.root.title_mc.username_txt.text = 'steven'
    steven.root.title_mc.password_txt.text = 'houbraken'
    load = _load_user_file('steven')
    olds = imitate_news(steven.root, load)
    steven.users = users
    users['steven'] = steven
    # setup laurens
    laurens = user_class()
    laurens.create(speed)
#    laurens.setup_events()
    become_observant(laurens)
    laurens.root.title_mc.username_txt.text = 'laurens'
    laurens.root.title_mc.password_txt.text = 'groenewegen'
    laurens.users = users
    users['laurens'] = laurens
    # setup wout
    wout = user_class()
    wout.create(speed)
#    wout.setup_events()
    become_observant(wout)
    wout.root.title_mc.username_txt.text = 'wout'
    wout.root.title_mc.password_txt.text = 'merbis'
    wout.users = users
    users['wout'] = wout
    # setup kyung
    kyung = user_class()
    kyung.create(speed)
#    kyung.setup_events()
    become_observant(kyung)
    kyung.root.title_mc.username_txt.text = 'kyung'
    kyung.root.title_mc.password_txt.text = 'min'
    kyung.users = users
    users['kyung'] = kyung
    # setup moonhyoung
    moonhyoung = user_class()
    moonhyoung.create(speed)
#    moonhyoung.setup_events()
    become_observant(moonhyoung)
    moonhyoung.root.title_mc.username_txt.text = 'moonhyoung'
    moonhyoung.root.title_mc.password_txt.text = 'park'
    moonhyoung.users = users
    users['moonhyoung'] = moonhyoung
    # setup munhyong # misspelled
    munhyong = user_class()
    munhyong.create(speed)
#    munhyong.setup_events()
    become_observant(munhyong)
    munhyong.root.title_mc.username_txt.text = 'munhyong'
    munhyong.root.title_mc.password_txt.text = 'park'
    munhyong.users = users
    users['munhyong'] = munhyong
    # setup n1
    n1 = user_class()
    n1.create(speed)
#    n1.setup_events()
    become_observant(n1)
    n1.root.title_mc.username_txt.text = 'n1'
    n1.root.title_mc.password_txt.text = 'nexon1'
    n1.users = users
    users['n1'] = n1
    # setup n2
    n2 = user_class()
    n2.create(speed)
#    n2.setup_events()
    become_observant(n2)
    n2.root.title_mc.username_txt.text = 'n2'
    n2.root.title_mc.password_txt.text = 'nexon2'
    n2.users = users
    users['n2'] = n2
    # setup n3
    n3 = user_class()
    n3.create(speed)
#    n3.setup_events()
    become_observant(n3)
    n3.root.title_mc.username_txt.text = 'n3'
    n3.root.title_mc.password_txt.text = 'nexon3'
    n3.users = users
    users['n3'] = n3
    # setup n4
    n4 = user_class()
    n4.create(speed)
#    n4.setup_events()
    become_observant(n4)
    n4.root.title_mc.username_txt.text = 'n4'
    n4.root.title_mc.password_txt.text = 'nexon4'
    n4.users = users
    users['n4'] = n4
    # clone
    users['beginner'] = lukasz
    users['andre'] = lukasz
    users['ezra'] = lukasz
    users['dennis'] = lukasz
    users['michael'] = lukasz
    users['emmet'] = lukasz
    users['stephen'] = lukasz
    # setup computer_lukasz
    computer_lukasz = user_class()
    computer_lukasz.create(speed)
#    computer_lukasz.setup_events()
    computer_lukasz.root.title_mc.username_txt.text = 'computer_lukasz'
    computer_lukasz.root.title_mc.password_txt.text = 'computer_lukasz'
    computer_lukasz.root.level_mc._txt.text = str(gnugo_level)
    computer_lukasz.users = users
    users['computer_lukasz'] = computer_lukasz
    # setup computer_jade
    computer_jade = user_class()
    computer_jade.create(speed)
#    computer_jade.setup_events()
    computer_jade.root.title_mc.username_txt.text = 'computer_jade'
    computer_jade.root.title_mc.password_txt.text = 'computer_jade'
    computer_jade.root.level_mc._txt.text = str(gnugo_level)
    computer_jade.users = users
    users['computer_jade'] = computer_jade
    # setup yuji
    yuji = user_class()
    yuji.create(speed)
#    yuji.setup_events()
    olds = imitate_news(yuji.root, get_aware_news())
    yuji.root.title_mc.username_txt.text = 'yuji'
    yuji.root.title_mc.password_txt.text = 'kuribara'
    yuji.users = users
    users['yuji'] = yuji
    # setup jonathan
    jonathan = user_class()
    jonathan.create(speed)
#    jonathan.setup_events()
    olds = imitate_news(jonathan.root, get_aware_news())
    jonathan.root.title_mc.username_txt.text = 'jonathan'
    jonathan.root.title_mc.password_txt.text = 'zvesper'
    jonathan.users = users
    users['jonathan'] = jonathan
    # setup temporary
    temporary = user_class()
    temporary.create(speed)
#    temporary.setup_events()
    text.save(path_template % 'temporary', '{}')
    temporary.root.title_mc.username_txt.text = 'temporary'
    temporary.root.title_mc.password_txt.text = 'temporary'
    temporary.users = users
    users['temporary'] = temporary
    marije = user_class()
    marije.create(speed)
#    marije.setup_events()
    olds = imitate_news(marije.root, get_aware_news())
    marije.root.title_mc.username_txt.text = 'marije'
    marije.root.title_mc.password_txt.text = 'vandodeweerd'
    marije.users = users
    users['marije'] = marije
    casper = user_class()
    casper.create(speed)
#    casper.setup_events()
    olds = imitate_news(casper.root, get_aware_news())
    casper.root.title_mc.username_txt.text = 'casper'
    casper.root.title_mc.password_txt.text = 'harteveld'
    casper.users = users
    users['casper'] = casper
    henk = user_class()
    henk.create(speed)
#    henk.setup_events()
    olds = imitate_news(henk.root, get_aware_news())
    henk.root.title_mc.username_txt.text = 'henk'
    henk.root.title_mc.password_txt.text = 'mourik'
    henk.users = users
    users['henk'] = henk
    users = _create_user(users, 'h1', 'hva1', speed)
    users = _create_user(users, 'h2', 'hva2', speed)
    users = _create_user(users, 'h3', 'hva3', speed)
    users = _create_user(users, 'h4', 'hva4', speed)
    users = _create_user(users, 'wb1', 'weirdbeard1', speed)
    users = _create_user(users, 'wb2', 'weirdbeard2', speed)
    users = _create_user(users, 'jonghwa', 'kim', speed)
    users = _create_user(users, 'kevin', 'saunders', speed)
    users = _create_user(users, 'jennifer', 'russ', speed)
    return users


def authenticate_user(users, message):
    '''If name and password match, return globe of user.
    >>> users = setup_users(16)
    >>> authenticate_user(users, {})
    >>> capitalized_message = user_as.get_small_tree()

    If not matching, even if case is the only difference, return nothing.
    >>> capitalized_message['title_mc']['username_txt']['text'] = 'Joris'
    >>> capitalized_message['title_mc']['password_txt']['text'] = 'j'
    >>> authenticate_user(users, capitalized_message)
    >>> authentic_message = user_as.get_small_tree()
    >>> authentic_message['title_mc']['username_txt']['text'] = 'joris'
    >>> authentic_message['title_mc']['password_txt']['text'] = 'j'
    >>> user_globe = authenticate_user(users, authentic_message)
    >>> user_globe.root.title_mc.username_txt.text
    'joris'
    '''
    # validate format of username and password
    if not message:
        return
    title_mc = message.get('title_mc')
    if not title_mc:
        return
    username_txt = title_mc.get('username_txt')
    if not username_txt:
        return
    username = username_txt.get('text')
    if not username:
        return
    password_txt = title_mc.get('password_txt')
    if not password_txt:
        return
    password = password_txt.get('text')
    if password is None:
        return
    # match message to authentic message
    user = users.get(username)
    if not user:
        return
    authentic_title_mc = user.root.title_mc
    if not authentic_title_mc:
        return
    authentic_username_txt = authentic_title_mc.username_txt
    if not authentic_username_txt:
        return
    authentic_username = authentic_username_txt.text
    if not authentic_username:
        return
    if not authentic_username == username:
        return
    authentic_password_txt = authentic_title_mc.password_txt
    if authentic_password_txt is None:
        return
    authentic_password = authentic_password_txt.text
    if authentic_password is None:
        return
    if not authentic_password == password:
        return
    return user




def enter_level_1(users, message):
    return {'currentLabel': 'table',
            'game_over_mc': {'currentLabel': 'setup'}}

def create_table(users, message):
    'OBSOLETE?'
    return {'currentLabel': 'table',
            'game_over_mc': {'currentLabel': 'setup'}}


def for_news_get_diff(news, parent, template_parent):
    '''How news corresponding to movie clip differs from template.
    >>> users = setup_users(1.0)
    >>> laurens = users.get('laurens')
    >>> custom_news = get_custom(users, laurens)
    >>> custom_news.get('option_mc').get('block_mc')
    {'currentLabel': 'show'}
    >>> custom_news.get('option_mc').get('prohibit_danger_mc')

    >>> emmet = users.get('emmet')
    >>> custom_news = get_custom(users, emmet)
    >>> custom_news.get('option_mc').get('block_mc')
    {'currentLabel': 'show'}
    >>> custom_news.get('option_mc').get('prohibit_danger_mc')
    {'currentLabel': 'show'}
    '''
    message = {}
    for n in news:
        ## print n
        if type({}) == type(news[n]):
            if parent[n].currentLabel != template_parent[n].currentLabel:
                ## print '  ', parent[n].name, template_parent[n].name
                custom_news = user_as.get_note(parent[n], 'currentLabel')
                message = upgrade(message, custom_news)
            recursive = for_news_get_diff(news[n], parent[n], template_parent[n])
            message = upgrade(message, recursive)
    return message


def get_custom(users, user):
    '''Custom messages for this user.  See enter(...).
    '''
    template = users.get('template')
    message = {}
    new_user = for_news_get_diff(new_user_news, user.root, template.root)
    message = upgrade(message, new_user)
    aware = for_news_get_diff(get_aware_news(), user.root, template.root)
    message = upgrade(message, aware)
    observant = for_news_get_diff(get_observant_news(), user.root, template.root)
    message = upgrade(message, observant)
    return message


from remote_control import text_or_number
def get_properties(parent):
    '''only direct properties
    >>> users = setup_users(1.0, setup_events = False)
    >>> laurens = users.get('laurens')
    >>> get_properties(laurens.root)
    ['currentLabel', 'mouseX', 'mouseY', 'name', 'parent', 'scaleX', 'scaleY', 'x', 'y']
    >>> laurens.root.gotoAndPlay('_3_3')
    >>> get_properties(laurens.root)
    ['currentLabel', 'mouseX', 'mouseY', 'name', 'parent', 'scaleX', 'scaleY', 'x', 'y']
    '''
    managed = ['numChildren']
    properties = [property for property in dir(parent)
        if not property.startswith('_') 
            and text_or_number(parent[property])
            and property not in managed]
    return properties

def get_diff(parent, template_parent):
    '''News of how movie clip or display object differs from template.
    >>> users = setup_users(1.0, setup_events = False)
    >>> laurens = users.get('laurens')
    >>> template = users.get('template')
    >>> diff_news = get_diff(laurens.root, template.root)
    >>> diff_news.get('option_mc').get('block_mc')
    {'currentLabel': 'show'}
    >>> diff_news.get('option_mc').get('prohibit_danger_mc')
    >>> laurens.root.gotoAndPlay('_3_3')
    >>> diff_news = get_diff(laurens.root, template.root)
    >>> diff_news['currentLabel']
    '_3_3'

    >>> emmet = users.get('emmet')
    >>> diff_news = get_diff(emmet.root, template.root)
    >>> diff_news.get('option_mc').get('block_mc')
    {'currentLabel': 'show'}

    TODO:  For quick login, store only diff of user from template.
    '''
    message = {}
    properties = get_properties(parent)
    for property in properties:
        if parent[property] != template_parent[property]:
            custom_news = user_as.get_note(parent, property)
            message = upgrade(message, custom_news)
    if hasattr(parent, 'numChildren'):
        for c in range(parent.numChildren):
            child = parent.getChildAt(c)
            template_child = template_parent.getChildAt(c)
            recursive = get_diff(child, template_child)
            message = upgrade(message, recursive)
    return message


#def get_custom(users, user):
#    '''Custom messages for this user.  See enter(...).
#    '''
#    message = {}
#    template = users.get('template')
#    options = get_observant_news().keys() + get_aware_news().keys()
#    for option in options:
#        if user.root[option].currentLabel != template.root[option].currentLabel:
#            custom_news = user_as.get_note(user.root[option], 'currentLabel')
#            message = upgrade(message, custom_news)
#    return message


from os.path import exists
from client import load
path_template = 'user/%s.news.py'
def _load_user_file(name):
    file_name = path_template % name
    if not exists(file_name):
        return {}
    else:
        logging.info('loading %s' % file_name)
        reply = load(file_name)
        return reply

import text
import pprint
def upgrade_user_file(name, news):
    '''Upgrade user file by news.
    >>> news = _load_user_file('jade')
    >>> news.get('level_mc').get('_txt').get('text')
    '10'
    >>> news.get('level_mc').get('progress_mc')
    >>> progress = {'level_mc': {'progress_mc': {'currentLabel': '_5'}}}
    >>> upgrade_user_file('jade', progress)
    >>> news = _load_user_file('jade')
    >>> news.get('level_mc').get('progress_mc').get('currentLabel')
    '_5'
    >>> news.get('level_mc').get('_txt').get('text')
    '10'
    '''
    olds = _load_user_file(name)
    olds = upgrade(olds, news)
    formatted = pprint.pformat(olds)
    file_name = path_template % name
    text.save(file_name, formatted)

import re
def is_size(label):
    '''
    >>> is_size('_3_3')
    True
    >>> is_size('_5_5')
    True
    >>> is_size('_7_7')
    True
    >>> is_size('_9_9')
    True
    >>> is_size('_9_9_mc')
    False
    '''
    size = re.compile('^_[0-9]_[0-9]$')
    if size.match(label):
        return True
    return False


def table_available_news(users):
    '''Return news that table is available.
    >>> users = setup_users(8.0, setup_events = False)
    >>> kyung = users.get('kyung')
    >>> kyung.root.lobby_mc.join_mc.join_txt.text = 'moonhyoung'
    >>> kyung.root.lobby_mc.join_mc.gotoAndPlay('join')
    >>> table_available_news(users)
    {}
    >>> # kyung.root.title_mc.username_txt.text = 'kyung'
    >>> table_available_news(users)
    {}
    >>> moonhyoung = users.get('moonhyoung')
    >>> # moonhyoung.root.title_mc.username_txt.text = 'moonhyoung'
    >>> moonhyoung.root.lobby_mc.join_mc.join_txt.text = 'moonhyoung'
    >>> moonhyoung.root.lobby_mc.join_mc.gotoAndPlay('join')
    >>> table_available_news(users)
    {'lobby_mc': {'join_mc': {'currentLabel': 'join', 'join_txt': {'text': 'moonhyoung'}}}}
    '''
    def _my_table_name(user):
        table_name = None
        if 'join' == user.root.lobby_mc.join_mc.currentLabel:
            user_name = user.root.title_mc.username_txt.text
            join_name = user.root.lobby_mc.join_mc.join_txt.text
            if user_name == join_name:
                table_name = join_name
        return table_name
    message = {}
    for user in users.values():
        table_name = _my_table_name(user)
        if table_name:
            message['lobby_mc'] = {
                    'join_mc':  {'currentLabel':  'join',
                                'join_txt': {'text': table_name}
                                }
                    }
            break
    return message

# greeting = 'COMMENT? TYPE IN BOX AT BOTTOM'
greeting = 'HELLO.  TO START, CLICK LEVEL 1.'

def enter(users, user, greeting = greeting):
    '''Login.  If user liberty view differs from default, notify client.
    >>> users = setup_users(8.0, setup_events = False)

    client logs in.  no state to load.  
    >>> ethan = users.get('ethan')
    >>> ethan.root.gateway_mc.gotoAndPlay('enter')
    >>> news = enter(users, ethan)
    >>> news.get('currentLabel')
    'lobby'

    Clear gateway message
    >>> news.get('gateway_mc').get('currentLabel')
    'none'
    >>> ethan.revise(news)

    this does not affect news of another player.
    >>> joris = users.get('joris')
    >>> joris.root.gotoAndPlay('login')
    >>> news = enter(users, joris)
    >>> if news.get('liberty_mc'):
    ...     news, joris.root.liberty_mc.currentLabel
    >>> if not news.get('territory_mc') == {'currentLabel': 'show'}:
    ...     news, joris.root.territory_mc.currentLabel
    >>> if not news.get('defend_mc') == {'currentLabel': 'show'}:
    ...     news, joris.root.defend_mc.currentLabel
    >>> if not news.get('attack_mc') == {'currentLabel': 'show'}:
    ...     news, joris.root.attack_mc.currentLabel
    >>> if not news.get('profit_mc') == {'currentLabel': 'show'}:
    ...     news, joris.root.profit_mc.currentLabel
    >>> if not news.get('currentLabel') == 'lobby':
    ...     news, joris.root.currentLabel
    >>> lukasz = users.get('lukasz')
    >>> news = enter(users, lukasz)
    >>> news.get('liberty_mc')
    >>> news.get('territory_mc')
    >>> news.get('defend_mc')
    >>> news.get('attack_mc')

    client logs in.  server loads saved state.
    Might be a very large chunk of data!
    >>> ethan_start = users.get('ethan_start')
    >>> news = enter(users, ethan_start)
    >>> news.get('currentLabel')
    'table'

    Send greeting.
    >>> ethan = users.get('ethan')
    >>> news = enter(users, ethan, 'hello')
    >>> if not news['comment_mc']['_txt'].has_key('text'):
    ...     news['comment_mc']

    if user had logged out, then return to lobby.
    >>> ethan.root.gotoAndPlay('login')
    >>> ethan.root.comment_mc._txt.text = 'a'
    >>> news = enter(users, ethan, 'hello')
    >>> news.get('currentLabel')
    'lobby'

    if user had not logged out, then return.
    >>> ethan.root.gotoAndPlay('_5_5')
    >>> ethan.root.comment_mc._txt.text = 'a'
    >>> news = enter(users, ethan, 'hello')
    >>> news.get('currentLabel')
    '_5_5'

    If user at a board label: dispatch mouse to confirm.
    >>> news['game_over_mc']['_5_5_mc']['confirm_mc']['dispatchEvent']
    'mouseDown'

    If user had comment already, return that.
    >>> news['comment_mc']['_txt']['text']
    'a'

    Send greeting.
    >>> yuji = users.get('yuji')
    >>> news = enter(users, yuji, 'hello')
    >>> if not news['comment_mc']['_txt'].has_key('text'):
    ...     news['comment_mc']

    Do not send greeting.
    >>> news = enter(users, yuji, '')
    >>> if news.get('comment_mc'):
    ...     news['comment_mc']
    '''
    template = users.get('template')
    diff = get_diff(user.root, template.root)
    login_message = {'gateway_mc':  {'currentLabel': 'none'}}
    message = upgrade(diff, login_message)
    name = user.root.title_mc.username_txt.text
    load = _load_user_file(name)
    message = upgrade(load, message)
    if 'login' == message.get('currentLabel') or not message.get('currentLabel'):
        message['currentLabel'] = 'lobby'
    if not message.get('comment_mc'):
        if greeting:
            message['comment_mc'] = {
                'currentLabel': 'comment',
                '_txt': {
                    'text': greeting
                }
            }
    if is_size(message.get('currentLabel')):
        size_name = '%s_mc' % message['currentLabel']
        confirm_board = {
            'game_over_mc': {
                size_name: {
                    'confirm_mc': {
                        'dispatchEvent': 'mouseDown'
                    }
                }
            }
        }
        message = upgrade(message, confirm_board)
    message = upgrade(message, table_available_news(users))
    return message


def setup_users_white_black(white_name, black_name):
    '''White and black have an echo protocol and partners.
    >>> users, ethan, mathijs = setup_users_white_black('ethan', 'mathijs')
    >>> ethan.ambassador.send(1)
    1
    >>> users.get('ethan') == ethan
    True
    >>> users.get('mathijs') == mathijs
    True
    >>> ethan.root.level_mc._txt.text
    '40'
    >>> ethan.root._1_2_mc._event_type
    'mouseDown'

    >>> get_partner(users, ethan) == mathijs
    True

    Runs in less than 1.5 seconds
    >>> import timeit
    >>> stmt_code = 'users = setup_users_white_black("kyung", "moonhyoung")'
    >>> setup_code = 'from super_users import setup_users_white_black'
    >>> timer = timeit.Timer(stmt = stmt_code, setup = setup_code)
    >>> setup_second = timer.timeit(1)
    >>> if not setup_second < 1.25: setup_second
    '''
    users = setup_users(1, setup_events = False)
    from mock_client import echo_protocol_class
    black = users.get(black_name)
    black.setup_events()
    black.ambassador = echo_protocol_class()
    white = users.get(white_name)
    white.setup_events()
    white.ambassador = echo_protocol_class()
    set_color(black, 'black')
    set_color(white, 'white')
    partner = set_partner(users, black, white_name)
    partner2 = get_partner(users, black)
    assert partner == partner2
    partner = set_partner(users, white, black_name)
    partner2 = get_partner(users, white)
    assert partner == partner2
    assert get_color(black) == 'black'
    assert get_color(white) == 'white'
    return users, white, black


def setup_users_partners_ethan_mathijs():
    return setup_users_white_black('ethan', 'mathijs')


def get_author(users, user):
    '''White and black have an echo protocol.
    >>> users, ethan, emmet = setup_users_white_black('ethan', 'emmet')
    >>> emmet == get_author(users, ethan)
    True
    '''
    partner = get_partner(users, user)
    color = get_color(user)
    partner_color = get_color(partner)
    if 'black' == color:
        author = user
    elif 'black' == partner_color:
        author = partner
    else:
        who_is_black_log = 'get_author: who is black? %s,%s' \
                % (color, partner_color)
        logging.error(who_is_black_log)
        ## import pdb; pdb.set_trace();
        return
    return author


def _pass_reply(users, user):
    '''
    >>> code_unit.doctest_unit(update_pass_news, verbose = False, log = False)
    '''
    reply = {'pass_mc': {'currentLabel': 'none'}}
    partner = get_partner(users, user)
    partner_color = get_color(partner)
    if partner_color == user.root.pass_white_mc.currentLabel:
        game_over = {'game_over_mc': {'currentLabel': 'score'},
                'pass_white_mc': {'currentLabel': 'none'}}
        reply = upgrade(reply, game_over)
    else:
        color = get_color(user)
        a_pass = {'pass_white_mc': {'currentLabel': color}}
        reply = upgrade(reply, a_pass)
    return reply

def update_pass_news(users, user, news):
    '''Return partner_reply
    Last passes are marked visually.
    >>> from super_users import setup_users_partners_ethan_mathijs
    >>> users, ethan, emmet = setup_users_partners_ethan_mathijs()
    >>> emmet.root.pass_white_mc.currentLabel
    'none'
    >>> update_pass_news(users, emmet, {})
    (False, {})
    >>> news = {'pass_mc': {'currentLabel': 'enter'}}

    If one player passes, show partner.
    >>> from pprint import pprint
    >>> passed, partner_reply = update_pass_news(users, emmet, news)
    >>> passed
    True
    >>> pprint(partner_reply)
    {'pass_mc': {'currentLabel': 'none'},
     'pass_white_mc': {'currentLabel': 'black'}}

    Update with mouse
    >>> news = {'pass_mc': {'dispatchEvent': 'mouseDown'}}
    >>> from pprint import pprint
    >>> passed, partner_reply = update_pass_news(users, emmet, news)
    >>> passed
    True
    >>> pprint(partner_reply)
    {'pass_mc': {'currentLabel': 'none'},
     'pass_white_mc': {'currentLabel': 'black'}}
    
    If showing previous pass, then reset.
    >>> emmet.root.pass_white_mc.gotoAndPlay('white')
    >>> passed, partner_reply = update_pass_news(users, emmet, {})
    >>> passed
    False
    >>> pprint(partner_reply)
    {'pass_white_mc': {'currentLabel': 'none'}}

    If previous player just passed, and player passes, score and reset.
    >>> emmet.root.pass_white_mc.gotoAndPlay('white')
    >>> passed, partner_reply = update_pass_news(users, emmet, news)
    >>> passed
    True
    >>> pprint(partner_reply)
    {'game_over_mc': {'currentLabel': 'score'},
     'pass_mc': {'currentLabel': 'none'},
     'pass_white_mc': {'currentLabel': 'none'}}

    '''
    passed = False
    reply = {}
    pass_object = news.get('pass_mc')
    if pass_object:
        if 'mouseDown' == pass_object.get('dispatchEvent'):
            passed = True
        if 'enter' == pass_object.get('currentLabel'):
            passed = True
            logging.warn('update_pass_news:  deprecate enter for mouse')
        if passed:
            reply = _pass_reply(users, user)
    elif 'none' != user.root.pass_white_mc.currentLabel:
        reply = {'pass_white_mc': {'currentLabel': 'none'}}
    return passed, reply



def final_score_news(score):
    '''by score: win, lose, or draw.  for black, and white.
    And reset cursors.
    >>> from pprint import pprint
    >>> pprint(final_score_news(1))
    {'cursor_mc': {'act_mc': {'currentLabel': 'none'}, 'currentLabel': 'none'},
     'game_over_mc': {'currentLabel': 'win',
                      'score_mc': {'territory_txt': {'text': '1'}}}}
    >>> pprint(final_score_news(0))
    {'cursor_mc': {'act_mc': {'currentLabel': 'none'}, 'currentLabel': 'none'},
     'game_over_mc': {'currentLabel': 'draw',
                      'score_mc': {'territory_txt': {'text': '0'}}}}
    >>> pprint(final_score_news(-1))
    {'cursor_mc': {'act_mc': {'currentLabel': 'none'}, 'currentLabel': 'none'},
     'game_over_mc': {'currentLabel': 'lose',
                      'score_mc': {'territory_txt': {'text': '-1'}}}}
    '''
    if 1 <= score:
        label = 'win'
    elif 0 == score:
        label = 'draw'
    else:
        label = 'lose'
    score_text = str(score)
    reply = {
        'game_over_mc': {
            'currentLabel': label, 
            'score_mc': {
                'territory_txt': {
                    'text': score_text
                },
            },
        },
        'cursor_mc': {
            'act_mc': {
                'currentLabel': 'none'
            },
            'currentLabel': 'none',
        }
    }
    return reply

def get_clock_news(users, user, clock_object):
    '''Set clock to real-time and turn to each player, 
    so both players can move at the same time.
    >>> users, ethan, mathijs = setup_users_partners_ethan_mathijs()
    >>> clock_object = {'enter_mc': {'currentLabel': 'enter'}}
    >>> get_color(ethan)
    'white'
    >>> news, partner_news = get_clock_news(users, mathijs, clock_object)
    >>> news.get('turn_mc').get('currentLabel')
    'black'
    >>> partner_news.get('turn_mc').get('currentLabel')
    'white'
    '''
    enter_object = clock_object.get('enter_mc')
    if enter_object:
        if 'enter' == enter_object.get('currentLabel'):
            reply = {
                'clock_mc': {
                    'currentLabel': 'time',
                    'enter_mc': {'currentLabel': 'none'}
                }
            } 
            # both players see it is their turn.
            color = get_color(user)
            partner = get_partner(users, user)
            partner_turn = get_your_turn_news(get_color(partner))
            partner_reply = {}
            partner_reply = upgrade(partner_reply, reply)
            partner_reply = upgrade(partner_reply, partner_turn)
            # XXX test
            your_turn = get_your_turn_news(color)
            reply = upgrade(reply, your_turn)
            return reply, partner_reply

def may_resize_board(users, user, news):
    '''To sync client-server intersection arrays, client dispatches resize.
    >>> users, ethan, mathijs = setup_users_partners_ethan_mathijs()
    >>> may_resize_board(users, ethan, {})
    >>> mathijs.root.currentLabel
    'login'
    >>> resized = may_resize_board(users, ethan, {'game_over_mc': {'_3_3_mc': {'enter_mc': {'currentLabel': 'enter'}}}})
    >>> resized != None
    True
    >>> mathijs.root.currentLabel
    '_3_3'
    >>> resized = may_resize_board(users, ethan, {'game_over_mc': {'_5_5_mc': {'enter_mc': {'currentLabel': 'enter'}}}})
    >>> resized != None
    True
    >>> mathijs.root.currentLabel
    '_5_5'
    >>> resized = may_resize_board(users, ethan, {'game_over_mc': {'_7_7_mc': {'enter_mc': {'currentLabel': 'enter'}}}})
    >>> resized != None
    True
    >>> mathijs.root.currentLabel
    '_7_7'
    '''
    game_over_dict = news.get('game_over_mc')
    if game_over_dict:
        for size in ['_3_3', '_5_5', '_7_7', '_9_9']:
            board_size_dict = game_over_dict.get(size + '_mc')
            if board_size_dict:
                enter_dict = board_size_dict.get('enter_mc')
                if 'enter' == enter_dict.get('currentLabel'):
                    old_length = len(user.intersection_mc_array)
                    reply = to_resize_board(old_length, size)
                    partner = get_partner(users, user)
                    tell(partner, reply)
                    user.publish(reply)
                    return reply


def _remove_table(users, user):
    '''
    Users at table return to lobby and clear board.
    All users online no longer see table.
    For examples, see may_use_lobby.
    If not viewing table of that user or partner, 
    do not clear that table's name.
    >>> users, moonhyoung, kyung = setup_users_white_black('moonhyoung', 'kyung')
    >>> moonhyoung.root.lobby_mc.join_mc.join_txt.text
    'FIELD'
    >>> kyung.root.lobby_mc.join_mc.join_txt.text
    'FIELD'
    >>> kyung.root.gotoAndPlay('_3_3')
    >>> news = _remove_table(users, moonhyoung)
    >>> moonhyoung.root.lobby_mc.join_mc.join_txt.text
    'FIELD'
    >>> kyung.root.lobby_mc.join_mc.join_txt.text
    'FIELD'

    Return to lobby and reset lobby button.
    >>> news['currentLabel']
    'lobby'
    >>> news.get('lobby_mc')
    {'enter_mc': {'currentLabel': 'none'}}
    >>> kyung.root.currentLabel
    'lobby'
    '''
    left = {
        'currentLabel': 'lobby',
        'lobby_mc': {
            'enter_mc': {
                'currentLabel': 'none'
            }
        }
    }
    removed = {
        'lobby_mc': {
            'join_mc': {
                'currentLabel': 'none',
                'join_txt': {
                    'text': ''
                }
            }
        }
    }
    length = len(user.intersection_mc_array)
    partner = get_partner(users, user)
    if partner:
        cleared = to_clear_table(partner.root, length)
        cleared = upgrade(cleared, left)
        partner.play_history = []
        partner.board_history = []
        join_text = partner.root.lobby_mc.join_mc.join_txt.text
        user_name = user.root.title_mc.username_txt.text
        partner_name = partner.root.title_mc.username_txt.text
        if join_text == user_name or join_text == partner_name:
            cleared = upgrade(cleared, removed)
        tell(partner, cleared)
    for other_user in users.values():
        if user != other_user:
            if other_user.ambassador:
                join_text = other_user.root.lobby_mc.join_mc.join_txt.text
                user_name = user.root.title_mc.username_txt.text
                if join_text == user_name:
                    tell(other_user, removed)
                if partner:
                    partner_name = partner.root.title_mc.username_txt.text
                    if join_text == partner_name:
                        tell(other_user, removed)
    cleared = to_clear_table(user.root, length)
    cleared = upgrade(cleared, left)
    user.play_history = []
    user.board_history = []
    join_text = user.root.lobby_mc.join_mc.join_txt.text
    user_name = user.root.title_mc.username_txt.text
    if join_text == user_name:
        cleared = upgrade(cleared, removed)
    if partner:
        partner_name = partner.root.title_mc.username_txt.text
        if join_text == partner_name:
            cleared = upgrade(cleared, removed)
    return cleared


def get_partner_news(white_name, black_name):
    white_notice = {
        'turn_mc':  {
            'currentLabel': 'white',
            'black_user_txt': {'text':  black_name},
            'white_user_txt': {'text':  white_name}
        }
    }
    black_notice = {
        'turn_mc':  {
            'currentLabel': 'black',
            'black_user_txt': {'text':  black_name},
            'white_user_txt': {'text':  white_name}
        }
    }
    return white_notice, black_notice


def set_partner_news(users, user, partner_name):
    '''Set partner and return news.
    >>> users = setup_users(1)
    >>> lukasz = users.get('lukasz')
    >>> lukasz_news, ethan_news = set_partner_news(users, lukasz, 'ethan')
    >>> ethan_news.get('turn_mc').get('black_user_txt').get('text')
    'lukasz'
    >>> lukasz_news.get('turn_mc').get('white_user_txt').get('text')
    'ethan'
    >>> ethan = users.get('ethan')
    >>> ethan == get_partner(users, lukasz)
    True
    >>> wait_your_turn(lukasz, 'black', lukasz.root._0_0_mc)
    >>> wait_your_turn(ethan, 'white', ethan.root._0_0_mc)
    '''
    user_name = user.root.title_mc.username_txt.text
    set_partner(users, user, partner_name)
    if get_color(user) == 'white':
        user_news, partner_news = get_partner_news(user_name, partner_name)
    else:
        partner_news, user_news = get_partner_news(partner_name, user_name)
    return user_news, partner_news


def may_use_lobby(users, user, news):
    '''Enter lobby.
    >>> users = setup_users(1)
    >>> users, ethan, andre = setup_users_white_black('ethan', 'andre')
    >>> news = {'lobby_mc': {'enter_mc': {'currentLabel': 'enter'}}}

    Do not modify global get_expert_news()
    >>> expert_news_length = len(str(get_expert_news()))

    >>> reply = may_use_lobby(users, andre, news)
    >>> reply.get('lobby_mc').get('enter_mc')
    {'currentLabel': 'none'}
    >>> reply.get('currentLabel')
    'lobby'

    Make and clear room.
    >>> ethan.root.option_mc.empty_block_mc.gotoAndPlay('show')
    >>> ethan.root.top_move_mc.gotoAndPlay('show')
    >>> ethan.root.lobby_mc.join_mc.currentLabel
    'none'
    >>> create = {'lobby_mc': {'create_mc': {'currentLabel': 'enter'}}}
    >>> created = may_use_lobby(users, ethan, create)
    >>> olds = imitate_news(ethan.root, created)
    >>> ethan.root.lobby_mc.join_mc.currentLabel
    'join'
    >>> ethan.root.lobby_mc.join_mc.join_txt.text
    'ethan'

    Ethan may not setup.
    >>> ethan.root.game_over_mc.currentLabel
    'invite'

    Wout sees menu to exit.
    >>> wout = ethan
    >>> wout.root.menu_mc.currentLabel
    'show'

    creator is expert, so does not see top move.
    Ethan plays white, expert, so does not see top move.
    >>> ethan.root.top_move_mc.currentLabel
    'none'
    >>> ethan.root.option_mc.empty_block_mc.currentLabel
    'none'

    create button resets
    >>> created.get('lobby_mc').get('create_mc').get('currentLabel')
    'none'

    andre sees ethan's table.
    >>> andre.root.lobby_mc.join_mc.currentLabel
    'join'
    >>> andre.root.lobby_mc.join_mc.join_txt.text
    'ethan'

    andre joins ethan's table.
    >>> andre.root.connected_mc.gotoAndPlay('none')
    >>> join = {'lobby_mc': {'join_mc': {'currentLabel': 'enter', 'join_txt': {'text': 'ethan'}}}}
    >>> olds = imitate_news(andre.root, join)
    >>> joined = may_use_lobby(users, andre, join)
    >>> olds = imitate_news(andre.root, joined)
    >>> if not andre.root.currentLabel == 'table':  joined

    Ethan may setup.
    >>> andre.root.game_over_mc.currentLabel
    'setup'
    >>> ethan.root.game_over_mc.currentLabel
    'setup'

    andre becomes observant, so now sees connected.
    >>> andre.root.connected_mc.currentLabel
    'show'

    ethan leaves.
    >>> ethan.play_history.append(1)
    >>> ethan.board_history.append(',')
    >>> leave_table = {'lobby_mc': {'enter_mc': {'currentLabel': 'enter'}}}
    >>> left_table = may_use_lobby(users, ethan, leave_table)
    >>> olds = imitate_news(ethan.root, left_table)
    >>> ethan.root.lobby_mc.join_mc.currentLabel
    'none'
    >>> ethan.root.lobby_mc.join_mc.join_txt.text
    ''
    >>> ethan.play_history
    []
    >>> ethan.board_history
    []
    >>> andre.root.lobby_mc.join_mc.currentLabel
    'none'
    >>> andre.root.lobby_mc.join_mc.join_txt.text
    ''
    >>> andre.root.currentLabel
    'lobby'

    Do not modify global get_expert_news()
    >>> if not expert_news_length == len(str(get_expert_news())):
    ...     expert_news_length, len(str(get_expert_news()))

    For acceptance, see client.py:restart_example
    '''
    lobby_mc = news.get('lobby_mc')
    if lobby_mc:
        enter_mc = lobby_mc.get('enter_mc')
        if enter_mc:
            if 'enter' == enter_mc.get('currentLabel'):
                return _remove_table(users, user)
        level_1_mc = lobby_mc.get('level_1_mc')
        if level_1_mc:
            if 'enter' == level_1_mc.get('currentLabel'):
                reply = enter_level_1(users, news)
                return reply
        create_mc = lobby_mc.get('create_mc')
        if create_mc:
            if 'enter' == create_mc.get('currentLabel'):
                user_name = user.root.title_mc.username_txt.text
                created = {                         
                    'lobby_mc':  {
                        'create_mc': {
                            'currentLabel':  'none'
                        },
                        'join_mc':  {
                            'currentLabel':  'join',
                            'join_txt': {
                                'text': user_name}
                        }
                    }
                }
                reply = {'currentLabel': 'table', 
                        'game_over_mc': {'currentLabel': 'invite'},
                        'menu_mc': {'currentLabel': 'show'},
                        'turn_mc':  {
                            'currentLabel': 'white',
                            'white_user_txt': {'text':  user_name}
                            },
                        }
                empty_color_news = get_empty_color_news(user, 'white')
                reply = upgrade(reply, empty_color_news)
                for other_user in users.values():
                    if user != other_user: 
                        if other_user.ambassador:
                            tell(other_user, created)
                reply = upgrade(reply, created)
                reply = upgrade(get_expert_news(), reply)
                return reply
        join_mc = lobby_mc.get('join_mc')
        if join_mc:
            if 'enter' == join_mc.get('currentLabel'):
                return _join_table(users, user)

def get_area_ratio(board_length):
    '''
    >>> print round(get_area_ratio(3), 2)
    0.02
    >>> print round(get_area_ratio(5), 2)
    0.07
    >>> print round(get_area_ratio(7), 2)
    0.14
    >>> print round(get_area_ratio(9), 2)
    0.22
    >>> print round((9.0 * 9) / (19 * 19), 2)
    0.22
    '''
    spaces = board_length * board_length
    ratio = float(spaces) / (19 * 19)
    return ratio

def get_extra_stone_available(black_level, white_level, board_length = 9):
    '''
    Some say GnuGo level 1 plays about 14 kyu.
    New players lose against GnuGo with 3 extra stone and 5 hide cards.
    Rank difference (white - black):
    9x9 handicap = 19x19 handicap / 4
    
    http://www.cs.umanitoba.ca/~bate/BIG/Sect4p1.html
    http://senseis.xmp.net//HandicapForSmallerBoardSizes

    Level is 50 + (0 - KGS kyu).
    Ethan is about 10k on KGS so about level 40.
    20 / 4 equals about 5 stones handicap on 9x9.  -1 for first move.
    
    Introduce extra stone around level 10.
    >>> get_extra_stone_available(10, 36, 5)
    1
    >>> get_extra_stone_available(12, 36, 7)
    2
    >>> get_extra_stone_available(14, 36, 9)
    3

    Jade and I have played close game at 4 stones handicap on 9x9.
    Jade is about 25-30 kyu worse.
    Jade is about level 10-15.
    Full help raises playing level about 10 (if less than level 20).
    Yet, beginners do not take full advantage of extra stones.

    >>> get_extra_stone_available(10, 36)
    4
    >>> get_extra_stone_available(1, 36)
    6
    >>> get_extra_stone_available(20, 36)
    1
    >>> get_extra_stone_available(26, 36)
    0
    >>> get_extra_stone_available(20, 20)
    0

    Bounds [0..9].
    >>> get_extra_stone_available(40, 10)
    0
    >>> get_extra_stone_available(0, 200)
    9
    
    Small board
    >>> get_extra_stone_available(1, 40, 5)
    2
    >>> get_extra_stone_available(10, 40, 5)
    1
    >>> get_extra_stone_available(10, 40, 7)
    3
    >>> get_extra_stone_available(20, 40, 7)
    1
    >>> get_extra_stone_available(30, 40, 7)
    0
    '''
    ratio = get_area_ratio(board_length)
    difference = white_level - black_level - help_level
    difference *= ratio * extra_stone_to_handicap 
    small_board_handicap = int(difference + 0.75)
    first_move = small_board_handicap - 1
    return min(max(first_move, 0), 9)

def get_hide_available(black_level, white_level, extra_stone, board_length = 9):
    '''After extra stone, balance by hide which is half an extra stone.
    >>> get_hide_available(10, 20, 0)
    0
    >>> get_hide_available(10, 24, 0)
    4

    Joris lost to GnuGo 9x9 with 9 hide stones (joris_hide_9_9_example)
    Is Joris 40-30k?
    Is level 20 appropriate to introduce hide?
    >>> get_hide_available(20, 36, 0, 5)
    2
    >>> get_hide_available(20, 36, 0, 7)
    4
    >>> get_hide_available(20, 36, 0)
    6
    >>> get_hide_available(20, 20, 0)
    0
        
    >>> get_hide_available(16, 36, 0)
    9
    >>> get_hide_available(16, 36, 1)
    3
    >>> get_hide_available(16, 36, 2)
    0


    Smaller board
    >>> get_hide_available(16, 36, 0, 3)
    1
    >>> get_hide_available(16, 36, 0, 5)
    3
    >>> get_hide_available(16, 36, 0, 7)
    6

    Bounds [0..9].
    >>> get_hide_available(40, 10, 0)
    0
    >>> get_hide_available(0, 200, 0)
    9
    '''
    difference = white_level - black_level - help_level
    ratio = get_area_ratio(board_length)
    if extra_stone:
        first_move = 0.5
        difference -= (extra_stone + first_move) / ratio
    difference *= ratio
    difference *= hide_to_handicap
    rounded = int(difference + 0.75)
    return min(max(rounded, 0), 9)




def get_setup_available_news(prefix, available):
    '''Format to news.
    >>> get_setup_available_news('extra_stone', 4)
    {'game_over_mc': {'extra_stone_available_mc': {'currentLabel': '_4'}}}
    >>> get_setup_available_news('extra_stone', 0)
    {'game_over_mc': {'extra_stone_available_mc': {'currentLabel': '_0'}}}
    >>> get_setup_available_news('hide', -1)
    {'game_over_mc': {'hide_available_mc': {'currentLabel': '_-1'}}}
    '''
    label = '_%s' % available
    return {
        'game_over_mc': {
            prefix + '_available_mc': {
                'currentLabel': label
            }
        }
    }


def probably_win(a_level, b_level):
    '''A probably wins.  Adapted from KGS rank math.
    http://www.gokgs.com/help/rmath.html
    My KGS 11 kyu rank as -11 and level 39.

    Me versus me.
    >>> probably_win(-11, -11)
    0.5
    >>> probably_win(39, 39)
    0.5

    Ethan vs TD Houfek
    >>> probably_win(-11, -8)
    0.18242552380635635
    >>> probably_win(39, 42)
    0.18242552380635635

    Ethan versus TD with one stone handicap
    >>> probably_win(-11+1, -8)
    0.2689414213699951

    Ethan vs GnuGo 3.8 level 1
    >>> probably_win(-11, -14)
    0.81757447619364365
    >>> probably_win(39, 36)
    0.81757447619364365

    GnuGo vs Ethan
    >>> probably_win(36, 39)
    0.18242552380635635
    '''
    import math
    e = math.e
    k = 0.5
    return 1 / (1 + e ** (k * (b_level - a_level)))

def get_odds_against(probably):
    '''Break-even betting ratio
    >>> get_odds_against(0.5)
    1.0
    >>> get_odds_against(0.25)
    3.0
    >>> get_odds_against(0.1)
    9.0
    '''
    if probably < 0.001:
        probably = 0.001
    if 0.999 < probably:
        probably = 0.999
    odds_against = (1 - probably) / probably
    return odds_against

extra_stone_to_handicap = 1.25
hide_to_handicap = 2.5
help_level = 5
gnugo_level = 36

def get_effective_level(skill_level, board_length, 
        handicap, extra_stone_available, hide_available, adjust_level):
    '''Percent to add to next level for A winning.
    KGS rank
    >>> get_effective_level(-11, 19, 0, 0, 0, 0)
    -11
    >>> get_effective_level(-11, 19, 4, 0, 0, 0)
    -7
    >>> get_effective_level(-11, 9, 1, 0, 0, 0)
    -7

    Beginner
    >>> get_effective_level(1, 3, 1, 0, 0, 35)
    76
    >>> get_effective_level(1, 3, 1, 0, 0, 5)
    46
    >>> get_effective_level(2, 3, 1, 0, 0, 5)
    47
    >>> get_effective_level(3, 5, 1, 1, 0, 5)
    34
    >>> get_effective_level(6, 5, 2, 0, 0, 5)
    40
    >>> get_effective_level(6, 5, 1, 0, 0, 5)
    25
    >>> get_effective_level(10, 7, 2, 2, 0, 5)
    42
    >>> get_effective_level(10, 7, 1, 2, 0, 5)
    34
    >>> get_effective_level(10, 7, 1, 1, 0, 5)
    28
    >>> get_effective_level(10, 7, 1, 0, 0, 5)
    22
    >>> get_effective_level(10, 9, 1, 1, 0, 5)
    23

    Jade vs Ethan
    >>> get_effective_level(10, 9, 1, 4, 0, 5)
    34

    Ethan vs Jade
    >>> get_effective_level(40, 9, -1, -4, 0, -5)
    16

    Wout vs GnuGo
    >>> get_effective_level(10, 9, 1, 4, 0, 5)
    34
    >>> get_effective_level(36, 9, -1, -4, 0, -5)
    12

    Wout vs GoGui GnuGo
    >>> get_effective_level(10, 9, 4, 0, 0, 0)
    28
    >>> get_effective_level(10, 9, 5, 0, 0, 0)
    32

    hide < extra stone < handicap
    >>> get_effective_level(10, 9, 0, 0, 2, 5)
    19
    >>> get_effective_level(10, 9, 0, 2, 0, 5)
    22
    >>> get_effective_level(10, 9, 2, 0, 0, 5)
    24
    '''
    level = skill_level
    level += adjust_level
    ratio = get_area_ratio(board_length)
    handicap /= ratio
    level += handicap
    extra_stone_available /= ratio
    level += extra_stone_available / extra_stone_to_handicap
    hide_available /= ratio
    level += hide_available / hide_to_handicap
    return int(round(level))

def get_prize(a_level, b_level, board_length, 
        handicap, extra_stone_available, hide_available, adjust_level):
    '''Percent to add to next level for A winning.
    Reward larger board.
    Beginner, easy may increase level
    TODO:  Adjust constraints
    >>> get_prize(1, 36, 3, 1, 0, 0, 15)
    49
    >>> get_prize(2, 36, 3, 1, 0, 0, 10)
    6
    >>> get_prize(2, 36, 5, 1, 1, 0, 15)
    522
    >>> get_prize(3, 36, 5, 1, 1, 0, 10)
    1144
    >>> get_prize(9, 36, 5, 1, 0, 0, 5)
    10373
    
    >>> get_prize(10, 36, 7, 1, 2, 0, 5)
    737
    >>> get_prize(10, 40, 9, 1, 4, 0, 5)
    9013

    Discourage sandbagging
    >>> get_prize(4, 36, 3, 1, 0, 0, 5)
    1
    >>> get_prize(5, 36, 3, 1, 0, 0, 5)
    0
    >>> get_prize(6, 36, 3, 1, 0, 0, 5)
    0

    Discourage high level, easy
    >>> get_prize(39, 36, 9, 1, 0, 0, 0)
    0

    Reward opponent of sandbagger
    >>> get_prize(36, 39, 9, -1, 0, 0, 0)
    318

    Encourage high level, even odds
    >>> get_prize(39, 43, 9, 1, 0, 0, 0)
    7

    High level, hard
    >>> get_prize(39, 46, 9, 1, 0, 0, 0)
    33

    Exploit:  Two beginners beat each other and level each other up.

    Comparable to KGS casual amateur
    >>> get_prize(39, 39, 19, 0, 0, 0, 0)
    33
    >>> get_prize(39, 43, 19, 4, 0, 0, 0)
    33

    Not calibrated for KGS rank
    >>> get_prize(-11, -11, 19, 0, 0, 0, 0)
    'out of bounds'
    >>> get_prize(-11, -7, 19, 4, 0, 0, 0)
    'out of bounds'
    >>> get_prize(-11, -7, 9, 1, 0, 0, 0)
    'out of bounds'

    TODO:  Encourage fully played games, discourage short games or problems.
    '''
    if a_level < 0:
        return 'out of bounds'
    effective_level = get_effective_level(a_level, board_length, 
        handicap, extra_stone_available, hide_available, adjust_level)
    return get_difficulty_prize(effective_level, b_level, board_length)


def get_difficulty_prize(a_level, difficulty_plus_level, board_length):
    '''Prize at level for difficulty plus that level.
    Very little for a small board.
    A lot less at a higher level.
    >>> prize = get_difficulty_prize(1, -9, 3)
    >>> if not 30 <= prize and prize <= 100:  prize
    >>> prize = get_difficulty_prize(1, -4, 3)
    >>> if not 10 <= prize and prize <= 50:  prize
    >>> prize = get_difficulty_prize(2, -4, 3)
    >>> if not 2 <= prize and prize <= 50:  prize
    >>> prize = get_difficulty_prize(3, -4, 3)
    >>> if not 1 <= prize and prize <= 25:  prize
    >>> prize = get_difficulty_prize(1, 1, 3)
    >>> if not 100 <= prize and prize <= 10000:  prize
    >>> prize = get_difficulty_prize(10, 10, 3)
    >>> if not 0 <= prize and prize <= 10:  prize
    >>> prize = get_difficulty_prize(10, 10, 5)
    >>> if not 5 <= prize and prize <= 100:  prize
    >>> prize = get_difficulty_prize(10, 10, 9)
    >>> if not 50 <= prize and prize <= 1000:  prize
    >>> prize = get_difficulty_prize(20, 20, 5)
    >>> if not 0 <= prize and prize <= 10:  prize
    >>> prize = get_difficulty_prize(20, 20, 9)
    >>> if not 50 <= prize and prize <= 200:  prize
    '''
    probably = probably_win(a_level, difficulty_plus_level)
    odds = get_odds_against(probably)
    ratio = get_area_ratio(board_length)
    # odds_factor = 20000000.0 # too high?
    odds_factor = 10000000.0
    return int(odds * odds_factor / (a_level ** 3) * ratio * ratio)
    # return int(odds ** 2 * 10000 / (a_level ** 2))
    # return int(odds ** 2 / (a_level ** 1.125 ** a_level))


def level_up(level, progress_percent):
    '''New level and progress toward next level.
    >>> level_up(1, 100)
    (2, 0)
    >>> level_up(1, 200)
    (2, 25)
    >>> level_up(1, 800)
    (3, 8)
    >>> level_up(1, 10000)
    (4, 10)
    >>> level_up(1, 100000)
    (5, 2)
    '''
    while 100 <= progress_percent:
        level += 1
        progress_percent -= 100
        progress_percent /= (level ** 3)
    return level, progress_percent


def get_prize_arguments(black, white, black_win):
    '''level, board, handicap, adjustment and so on.
    Assume komi no or 0 or 0.5
    >>> code_unit.doctest_unit(get_black_prize_level, log = False)
    '''
    if black_win:
        a_level = int(black.root.level_mc._txt.text)
        b_level = int(white.root.level_mc._txt.text)
        a = 1
    else:
        a_level = int(white.root.level_mc._txt.text)
        b_level = int(black.root.level_mc._txt.text)
        a = -1
    board = get_board(black)
    board_length = len(board)
    game_over_mc = black.root.game_over_mc
    extra_stone_available = int(game_over_mc.extra_stone_available_mc\
            .currentLabel[1:])
    hide_available = int(game_over_mc.hide_available_mc\
            .currentLabel[1:])
    handicap = 1
    problem_file = black.root.sgf_file_txt.text
    if os.path.exists(problem_file):
        history = sgf_to_history(problem_file)
        head = history[0]
        if None is not head.get('handicap'):
            handicap = head.get('handicap')
    adjustment = help_level
    if 'show' == black.root.option_mc.first_capture_mc.currentLabel:
        adjustment += 10
    if 'none' == black.root.option_mc.computer_pass_mc.currentLabel:
        adjustment += 5
    return (a_level, b_level, board_length, 
        a * handicap, a * extra_stone_available, 
            a * hide_available, a * adjustment)


from smart_go_format import sgf_to_history
def get_prize_arguments_file(black_level, problem_file):
    '''Arguments from header of a problem file.
    Assume komi no or 0 or 0.5
    >>> get_prize_arguments_file(1, 'sgf/beginner/capture_block_easy.sgf')
    (1, 36, 3, 2, 0, 0, 20)
    >>> get_prize_arguments_file(1, 'sgf/test_eight_sides_black_9_9.sgf')
    (1, 36, 9, 3, 0, 0, 5)
    >>> get_prize_arguments_file(1, 'sgf/beginner/capture_5_5.sgf')
    (1, 36, 5, 2, 0, 0, 5)
    >>> get_prize_arguments_file(1, 'sgf/beginner/capture_critical.sgf')
    (1, 36, 5, 1, 0, 0, 5)
    '''
    history = sgf_to_history(problem_file)
    head = history[0]
    white_level = 36
    size = head['size']
    handicap = 1 # assume komi no or 0 or 0.5
    if None is not head.get('handicap'):
        handicap = head.get('handicap')
    extra_stone_available = 0
    hide_available = 0
    game_over_mc = head['news'].get('game_over_mc')
    if game_over_mc:
        extra_stone = game_over_mc.get('extra_stone_available_mc')
        if extra_stone:
            extra_stone_available = int(extra_stone['currentLabel'][1:])
        hide = game_over_mc.get('hide_available_mc')
        if hide:
            hide_available = int(hide['currentLabel'][1:])
    adjustment = help_level
    option = head['news'].get('option_mc')
    if option:
        first_capture = option.get('first_capture_mc')
        if first_capture and 'show' == first_capture['currentLabel']:
            adjustment += 10
        computer_pass = option.get('computer_pass_mc')
        if computer_pass and 'none' == computer_pass['currentLabel']:
            adjustment += 5
    return (black_level, white_level, size,
            handicap, extra_stone_available, hide_available, adjustment)

from smart_go_format import sgf_file_to_black_level
from lesson import get_problem_name_file
def get_problem_difficulty(black_level, problem_file):
    '''Difference of effective level and white level.
    >>> get_problem_difficulty(1, 'sgf/beginner/capture_block_easy.sgf')
    -6
    >>> get_problem_difficulty(1, 'sgf/beginner/capture_block.sgf')
    1
    >>> get_problem_difficulty(2, 'sgf/beginner/capture_3_3.sgf')
    -12
    >>> get_problem_difficulty(2, 'sgf/beginner/capture_5_5.sgf')
    3
    >>> get_problem_difficulty(4, 'sgf/beginner/capture_5_5.sgf')
    1
    >>> get_problem_difficulty(6, 'sgf/beginner/capture_5_5.sgf')
    -1
    '''
    # problem_file = get_problem_name_file(problem_name)
    designed_level = sgf_file_to_black_level(problem_file)
    arguments = get_prize_arguments_file(black_level, problem_file)
    if designed_level is not None:
        difficulty = designed_level - black_level
    else:
        effective_level = get_effective_level(arguments[0], *arguments[2:])
        white_level = arguments[1]
        difficulty = white_level - effective_level
    return difficulty

def update_disable_problem_news(black_level, problem_mc):
    '''News to enable challenging or easy and disable hard problems.
    >>> users, white, laurens = setup_users_white_black('computer_lukasz', 'temporary')
    >>> _00_mc = laurens.root.lobby_mc._00_mc

    If all levels are lower than player, and enabled, change nothing.
    >>> news = update_disable_problem_news(10, _00_mc.capture_block_easy_mc)
    >>> news
    {}

    If level is higher, disable.
    >>> black_level = int(laurens.root.level_mc._txt.text)
    >>> news = update_disable_problem_news(10, _00_mc.capture_block_easy_mc)
    >>> news
    {}
    >>> news = update_disable_problem_news(-99, _00_mc.capture_5_5_mc)
    >>> news['lobby_mc']['_00_mc']['capture_5_5_mc'] #doctest: +ELLIPSIS
    {'disabled_mc': {'level_txt': {'text': '...'}, 'currentLabel': 'show'}}

    If Laurens levels up to that difficulty, enable.
    >>> olds = imitate_news(laurens.root, news)
    >>> laurens.root.lobby_mc._00_mc.capture_5_5_mc.disabled_mc.currentLabel
    'show'
    >>> news = update_disable_problem_news(6, _00_mc.capture_5_5_mc)
    >>> news['lobby_mc']['_00_mc']['capture_5_5_mc']
    {'disabled_mc': {'currentLabel': 'none'}}
    >>> ## from pprint import pprint
    >>> ## pprint(news)
    '''
    news = {}
    problem_name = problem_mc.name
    problem_file = get_problem_name_file(problem_name)
    difficulty = get_problem_difficulty(black_level, problem_file)
    article = None
    label = problem_mc.disabled_mc.currentLabel
    if 'none' == label:
        if 1 <= difficulty:
            new_level = black_level + difficulty
            article = {'currentLabel': 'show', 'level_txt': {'text': str(new_level)}}
    elif 'show' == label:
        if difficulty <= 0:
            article = {'currentLabel': 'none'}
    else:
        logging.error('update_disable_problem_news: I did not expect disabled_mc.currentLabel %s' % label) 
    if article:
        news = upgrade(news, 
            {problem_mc.parent.parent.name: {
                problem_mc.parent.name: {problem_name: {
                    'disabled_mc': article}}}})
    return news

def update_menu_info_news(problem_mc):
    '''News to change info of a menu button.
    >>> users, white, marije = setup_users_white_black(
    ...     'computer_lukasz', 'temporary')
    >>> _00_mc = marije.root.lobby_mc._00_mc
    >>> update_menu_info_news(_00_mc.capture_3_3_mc) #doctest: +ELLIPSIS
    {'lobby_mc': {'_00_mc': {'capture_3_3_mc': {'info_txt': {'text': 'HELP! ...'}}}}}
    '''
    from lesson import get_problem_name_file, get_opening_note
    reply = {}
    problem_file = get_problem_name_file(problem_mc.name)
    history = sgf_to_history(problem_file)
    opening_note_news = get_opening_note(history[0])
    if 'game_over_mc' in opening_note_news:
        game_over_news = opening_note_news.get('game_over_mc')
        if 'mission_mc' in game_over_news:
            info = game_over_news['mission_mc']['_txt']['text']
            reply = {
                problem_mc.parent.parent.name: {
                    problem_mc.parent.name: {
                        problem_mc.name: {
                            'info_txt': {'text': info}
                        }
                    }
                }
            }
    return reply

def update_disable_news(black_level, black_parent_mc):
    '''News to enable challenging or easy and disable hard problems.
    >>> users, white, black = setup_users_white_black('computer_lukasz', 'temporary')
    >>> _00_mc = black.root.lobby_mc._00_mc

    If all levels are lower than player, and enabled, change nothing.
    >>> news = update_disable_news(10, _00_mc)
    >>> news
    {}

    If level is higher, disable.
    >>> news = update_disable_news(-99, _00_mc)
    >>> news['lobby_mc']['_00_mc'].get('capture_block_easy_mc')
    {'disabled_mc': {'level_txt': {'text': '-64'}, 'currentLabel': 'show'}}
    >>> news['lobby_mc']['_00_mc']['capture_5_5_mc']
    {'disabled_mc': {'level_txt': {'text': '-13'}, 'currentLabel': 'show'}}
    '''
    news = {}
    problems = get_children(black_parent_mc, 'main_mc')
    for problem_mc in problems:
        news = upgrade(news, 
                update_disable_problem_news(black_level, problem_mc) )
        news = upgrade(news, 
            update_menu_info_news(problem_mc) )
    return news



def update_disable_menu_news(black_level, black_lobby_mc):
    '''News to enable challenging or easy and disable hard problems.
    >>> users, white, black = setup_users_white_black('computer_lukasz', 'temporary')

    Manually inspect the levels for outliers.
    >>> news = update_disable_menu_news(-999, black.root.lobby_mc)
    >>> from pprint import pprint
    >>> pprint(news)

    If all levels are lower than player, and enabled, change nothing.
    >>> news = update_disable_menu_news(40, black.root.lobby_mc)
    >>> news['lobby_mc']['_00_mc']['capture_5_5_mc'].get('disabled_mc')

    If level is higher, disable.
    >>> black_level = int(black.root.level_mc._txt.text)
    >>> news = update_disable_menu_news(-99, black.root.lobby_mc)
    >>> news['lobby_mc']['_00_mc'].get('capture_block_easy_mc').get('disabled_mc') #doctest: +ELLIPSIS
    {'level_txt': {'text': '...'}, 'currentLabel': 'show'}
    >>> news['lobby_mc']['_00_mc']['capture_5_5_mc'].get('disabled_mc') #doctest: +ELLIPSIS
    {'level_txt': {'text': '...'}, 'currentLabel': 'show'}

    If player levels up to that difficulty, enable.
    >>> olds = imitate_news(black.root, news)
    >>> black.root.lobby_mc._00_mc.capture_5_5_mc.disabled_mc.currentLabel
    'show'
    >>> news = update_disable_menu_news(6, black.root.lobby_mc)
    >>> news['lobby_mc']['_00_mc']['capture_5_5_mc'].get('disabled_mc')
    {'currentLabel': 'none'}
    '''
    news = {}
    children = get_children(black_lobby_mc, 'main_mc')
    menu_re = re.compile('_[0-9][0-9]_mc')
    menus = [menu for menu in children if menu_re.match(menu.name)]
    ## print [m.name for m in menus]
    # menus.remove('multiplayer_mc')
    for black_parent_mc in menus:
        news = upgrade(news,
                update_disable_news(black_level, black_parent_mc) )
    return news


from lesson import get_problem_name
from remote_control import get_grandchild_by_name
def get_problem_mc_from_file(user, problem_file):
    '''MovieClip of problem that points to the file name.
    >>> users, ethan, laurens = setup_users_white_black('ethan', 'laurens')
    >>> problem_file = 'sgf/beginner/capture_3_3.sgf'
    >>> laurens.root['lobby_mc']['_00_mc']['capture_3_3_mc'].name
    'capture_3_3_mc'
    >>> mc = get_problem_mc_from_file(laurens, problem_file)
    >>> ## mc # inspect
    >>> if not mc.name == laurens.root['lobby_mc']['_00_mc']['capture_3_3_mc'].name:
    ...     mc, mc.name

    If it exists.
    >>> problem_file = 'sgf/beginner/NO_SUCH.sgf'
    >>> mc = get_problem_mc_from_file(laurens, problem_file)
    >>> mc
    '''
    name = get_problem_name(problem_file)
    if name:
        return get_grandchild_by_name(user.root.lobby_mc, name)


def get_prize_news(black, white, black_score):
    '''Only call if one side wins.  If level up, save level and progress.
    Black is the author.
    Jade wins and levels up.
    >>> users, ethan, jade = setup_users_white_black('ethan', 'jade')
    >>> original_jade = load('user/jade.news.py')

    Jade beats himself on 9x9 with handicap of 1.
    >>> black_news, white_news = get_prize_news(jade, jade, 1)
    >>> black_news
    {}

    Jade's file is updated.
    >>> news = load('user/jade.news.py')
    >>> news['level_mc']['_txt'].get('text')
    '11'
    >>> news.get('currentLabel')
    >>> ## news['level_mc']['progress_mc'].get('currentLabel')

    To teardown and run this example again, revert Jade.
    >>> text.save(path_template % 'jade', str(original_jade))

    Jade beats Ethan and advances 2 levels!
    >>> black_news, white_news = get_prize_news(jade, ethan, 1)
    >>> black_news
    {'level_mc': {'_txt': {'text': '11'}, 'currentLabel': 'up', 'progress_mc': {'currentLabel': '_55'}}}
    >>> white_news
    {}

    Jade's file is updated.  Do not save level up message which would annoy.
    >>> news = load('user/jade.news.py')
    >>> news['level_mc']['_txt'].get('text')
    '11'
    >>> news.get('currentLabel')
    >>> news['level_mc'].get('progress_mc')
    {'currentLabel': '_55'}

    Ethan wins.
    >>> black_news, white_news = get_prize_news(jade, ethan, -1)
    >>> black_news
    {}
    >>> white_news
    {}

    Ethan beats himself on 9x9 with handicap of 1.
    >>> black_news, white_news = get_prize_news(ethan, ethan, 1)
    >>> black_news
    {}

    Jade wins, but only with first capture and computer never pass.
    >>> jade.root.option_mc.first_capture_mc.currentLabel
    'none'
    >>> jade.root.option_mc.computer_pass_mc.currentLabel
    'show'
    >>> jade.root.option_mc.first_capture_mc.gotoAndPlay('show')
    >>> jade.root.option_mc.computer_pass_mc.gotoAndPlay('none')
    >>> black_news, white_news = get_prize_news(jade, ethan, True)
    >>> black_news
    {'level_mc': {'_txt': {'text': '11'}, 'currentLabel': 'up'}}

    Laurens versus problem.
    >>> laurens = jade
    >>> laurens.root.sgf_file_txt.text = 'sgf/beginner/hide_9_9.sgf'
    >>> saved_news = load('user/jade.news.py')
    >>> saved_news.get('lobby_mc')
    >>> black_news, white_news = get_prize_news(laurens, ethan, 5)

    Laurens wins problem: mark menu button with highest score.
    >>> black_news['lobby_mc']['_20_mc']['hide_9_9_mc']['score_txt']['text']
    '$5'
    >>> black_news['level_mc']['_txt']['text']
    '11'

    Save Laurens' score of that problem.
    >>> saved_news = load('user/jade.news.py')
    >>> saved_news['lobby_mc']['_20_mc']['hide_9_9_mc']['score_txt']['text']
    '$5'

    If already score, do not award prize.
    >>> laurens.root.lobby_mc._20_mc.hide_9_9_mc.score_txt.text = '5'
    >>> black_news, white_news = get_prize_news(laurens, ethan, 1)
    >>> black_news.get('lobby_mc')

    multiplayer award by challenge of players
    >>> laurens.root.sgf_file_txt.text = ''
    >>> black_news, white_news = get_prize_news(laurens, ethan, 1)
    >>> black_news['level_mc']['_txt']['text']
    '11'
    >>> black_news.get('lobby_mc')

    To teardown and run this example again, revert file of Jade and Laurens.
    >>> text.save(path_template % 'jade', str(original_jade))
    '''
    black_news, white_news = {}, {}
    problem_file = black.root.sgf_file_txt.text
    black_win = 1 <= black_score
    score_news = {}
    if problem_file:
        problem_mc = get_problem_mc_from_file(black, problem_file)
        scored = problem_mc.score_txt.text
        if scored:
            prize = 0
        else:
            black_level = int(black.root.level_mc._txt.text)
            difficulty = get_problem_difficulty(black_level, problem_file)
            board = get_board(black)
            board_length = len(board)
            prize = get_difficulty_prize(black_level, 
                    difficulty + black_level, board_length)
            if 0 <= prize and 1 <= black_score:
                # final_score = black.root.game_over_mc.score_mc.territory_txt.text
                score_news = {'lobby_mc': {problem_mc.parent.name: {
                    problem_mc.name: {'score_txt': {'text': '$%s' % black_score}}}}}
                black_news = upgrade(black_news, score_news)
    else:
        arguments = get_prize_arguments(black, white, black_win)
        prize = get_prize(*arguments)
    file_news = {}
    if black_win:
        winner = black
        winner_news = black_news
    else:
        winner = white
        winner_news = white_news
    if 1 <= prize:
        winner_level = int(winner.root.level_mc._txt.text)
        previous = int(winner.root.level_mc.progress_mc.currentLabel[1:])
        new_level, progress = level_up(winner_level, previous + prize)
        if winner_level != new_level:
            level_news = {
                'level_mc': {
                    '_txt': {
                        'text': str(new_level)
                    },
                },
            }
            file_news = upgrade(file_news, level_news)
            winner_news = upgrade(winner_news, level_news)
            winner_news['level_mc']['currentLabel'] = 'up'
        if previous != progress:
            progress_label = '_%i' % progress
            progress_news = {
                'level_mc': {
                    'progress_mc': {
                        'currentLabel': progress_label
                    },
                },
            }
            file_news = upgrade(file_news, progress_news)
            winner_news = upgrade(winner_news, progress_news)
    if score_news:
        file_news = upgrade(file_news, score_news)
    if file_news:
        name = winner.root.title_mc.username_txt.text
        upgrade_user_file(name, file_news)
    return black_news, white_news


def insert_prize_news(black_score, users, user, partner, 
        user_reply, partner_reply):
    '''If any prize, upgrade reply.
    Insert score.
    before modifying, modify expectations in:
        jerry_captured_example
        jerry_lose_prize_example
    Computer beats Jerry.  Jerry loses and receives no level up.
    >>> users, computer_jerry, jerry = setup_users_white_black('jade', 'ethan')
    >>> user_news = {}
    >>> partner_news = {}
    >>> insert_prize_news(-1, users, computer_jerry, jerry, user_news, partner_news)
    >>> user_news['game_over_mc']['currentLabel']
    'win'
    >>> partner_news['game_over_mc']['currentLabel']
    'lose'
    >>> partner_news.get('level_mc')
    >>> from pprint import pprint
    >>> ## pprint(user_news)
    >>> ## pprint(partner_news)

    Jerry wins.
    >>> insert_prize_news(2, users, jerry, computer_jerry, user_news, partner_news)
    >>> user_news['game_over_mc']['currentLabel']
    'win'

    # >>> code_unit.doctest_unit(win_example, log = False)
            
    # >>> code_unit.doctest_unit(yuji_capture_3_3_example)
    # >>> code_unit.doctest_unit(yuji_capture_5_5_example)
    '''
    black_news, white_news = {}, {}
    author = get_author(users, user)
    other = get_partner(users, author)
    if author == partner:
        my_score = 0 - black_score
    else:
        my_score = black_score
    user_reply = upgrade(user_reply, final_score_news(my_score))
    partner_reply = upgrade(partner_reply, final_score_news(0 - my_score))
    black_news, white_news = get_prize_news(author, other, black_score)
    if author == user:
        user_reply = upgrade(user_reply, black_news)
        partner_reply = upgrade(partner_reply, white_news)
    elif author == partner:
        user_reply = upgrade(user_reply, white_news)
        partner_reply = upgrade(partner_reply, black_news)
    else:
        logging.error('who is author?')
        import pdb; pdb.set_trace();


def get_black_prize_level(black, white, problem_mc):
    '''Prize awarded if black wins this problem.
    >>> users, white, black = setup_users_white_black('computer_lukasz', 'lukasz')
    >>> yuji = black
    >>> black.root.level_mc._txt.text = '10'
    >>> white.root.level_mc._txt.text = '36'
    >>> _10 = black.root.lobby_mc._10_mc
    >>> _14 = black.root.lobby_mc._14_mc
    >>> _04 = black.root.lobby_mc._04_mc
    >>> _07 = black.root.lobby_mc._07_mc
    >>> get_black_prize_level(black, white, _10.extra_stone_5_5_mc)
    ({}, {})
    >>> get_black_prize_level(black, white, _14.extra_stone_9_9_3_mc)
    ({'level_mc': {'_txt': {'text': '11'}, 'currentLabel': 'up', 'progress_mc': {'currentLabel': '_30'}}}, {})
    >>> black.root.level_mc._txt.text = '1'
    >>> _00 = black.root.lobby_mc._00_mc
    >>> get_black_prize_level(black, white, _00.capture_5_5_mc)
    ({'level_mc': {'_txt': {'text': '2'}, 'currentLabel': 'up', 'progress_mc': {'currentLabel': '_4'}}}, {})
    >>> get_black_prize_level(black, white, _04.dominate_5_5_mc)
    ({'level_mc': {'_txt': {'text': '2'}, 'currentLabel': 'up', 'progress_mc': {'currentLabel': '_4'}}}, {})
    >>> get_black_prize_level(black, white, _07.score_5_5_3_mc)
    ({'level_mc': {'_txt': {'text': '5'}, 'currentLabel': 'up', 'progress_mc': {'currentLabel': '_79'}}}, {})
    '''
    problem_mc.dispatchEvent(mouseDown)
    ## print black.root.sgf_file_txt.text
    from lesson import on_problem_path
    on, news = on_problem_path(black, black.root._0_0_mc)
    black.revise(news)
    ## print on, news, black.root.game_over_mc.extra_stone_available_mc.currentLabel
    return get_prize_news(black, white, True)


def get_children_prize_level(black, white, black_level, black_parent_mc):
    '''Prize dictionary for each problem in menu.
    >>> from pprint import pprint
    >>> users, white, black = setup_users_white_black('computer_lukasz', 'lukasz')
    >>> yuji = black
    >>> white.root.level_mc._txt.text = '36'
    >>> _00_mc = black.root.lobby_mc._00_mc
    >>> pprint(get_children_prize_level(black, white, 1, _00_mc))
    >>> pprint(get_children_prize_level(black, white, 2, _00_mc))
    >>> pprint(get_children_prize_level(black, white, 4, _00_mc))
    >>> pprint(get_children_prize_level(black, white, 6, _00_mc))
    >>> pprint(get_children_prize_level(black, white, 8, _00_mc))
    >>> pprint(get_children_prize_level(black, white, 12, _00_mc))
    >>> _10_mc = black.root.lobby_mc._10_mc
    >>> pprint(get_children_prize_level(black, white, 10, _10_mc))
    >>> pprint(get_children_prize_level(black, white, 12, _10_mc))
    >>> pprint(get_children_prize_level(black, white, 14, _10_mc))
    >>> pprint(get_children_prize_level(black, white, 16, _10_mc))
    >>> pprint(get_children_prize_level(black, white, 18, _10_mc))
    >>> pprint(get_children_prize_level(black, white, 20, _10_mc))
    >>> pprint(get_children_prize_level(black, white, 22, _10_mc))
    >>> _20_mc = black.root.lobby_mc._20_mc
    >>> pprint(get_children_prize_level(black, white, 20, _20_mc))
    >>> pprint(get_children_prize_level(black, white, 22, _20_mc))
    >>> pprint(get_children_prize_level(black, white, 24, _20_mc))
    >>> pprint(get_children_prize_level(black, white, 26, _20_mc))
    >>> pprint(get_children_prize_level(black, white, 28, _20_mc))
    >>> pprint(get_children_prize_level(black, white, 30, _20_mc))
    >>> pprint(get_children_prize_level(black, white, 32, _20_mc))
    '''
    problem_prizes = {}
    black.root.level_mc._txt.text = str(black_level)
    from user_as import get_children
    problems = get_children(black_parent_mc, 'main_mc')
    for problem_mc in problems:
        problem_prizes[problem_mc.name] = {}
        prize = get_black_prize_level(black, white, problem_mc)
        problem_prizes[problem_mc.name]['prize'] = prize
        arguments = get_prize_arguments(black, white, True)
        problem_prizes[problem_mc.name]['arguments'] = arguments
        effective_level = get_effective_level(arguments[0], *arguments[2:])
        problem_prizes[problem_mc.name]['effective_level'] = effective_level
        black_level = arguments[0]
        white_level = arguments[1]
        boost = effective_level - black_level
        difficulty = white_level - boost
        problem_prizes[problem_mc.name]['difficulty'] = difficulty
    return problem_prizes


def get_difficulty(skill_level, opponent_level, board_length, 
        handicap, extra_stone_available, hide_available, adjust_level):
    '''difficulty and estimated probability of winning
    >>> print get_difficulty(1, 36, 3, 1, 0, 0, 20)
    (-24, 0.99999627336071584)
    >>> print get_difficulty(1, 36, 5, 2, 0, 0, 20)
    (-13, 0.9990889488055994)
    >>> print get_difficulty(1, 36, 5, 1, 1, 0, 10)
    (0, 0.62245933120185459)
    >>> print get_difficulty(1, 36, 5, 1, 0, 0, 20)
    (2, 0.37754066879814541)
    '''
    effective_level = get_effective_level(skill_level, board_length, 
            handicap, extra_stone_available, hide_available, adjust_level)
    boost = effective_level - skill_level
    difficulty = opponent_level - boost
    probably = probably_win(effective_level, opponent_level)
    return difficulty, probably

def _join_table(users, user):
    '''see may_use_lobby.  set higher level to white.
    >>> users = setup_users(8)
    >>> ethan = users.get('ethan')
    >>> from user_as import echo_protocol_class
    >>> ethan.ambassador = echo_protocol_class()
    >>> jade = users.get('jade')
    >>> jade.ambassador = echo_protocol_class()

    >>> jade.root.level_mc._txt.text
    '10'
    >>> ethan.root.level_mc._txt.text
    '40'

    To receive one hide, increase level gap:
    >>> jade.root.level_mc._txt.text = '8'
        
    >>> jade.root.gotoAndPlay('table')
    >>> jade.root.game_over_mc.gotoAndPlay('invite')
    >>> ethan.root.lobby_mc.join_mc.join_txt.text = 'jade'
    >>> expert_news_length = len(str(get_expert_news()))
    >>> news = _join_table(users, ethan)
    >>> news.get('turn_mc').get('white_user_txt').get('text')
    'ethan'
    >>> news.get('turn_mc').get('black_user_txt').get('text')
    'jade'
    >>> news.get('_0_0_mc').get('currentLabel')
    'empty_white'

    Goto setup.
    >>> news['game_over_mc']['currentLabel']
    'setup'
    >>> jade.root['game_over_mc']['currentLabel']
    'setup'

    set higher level to expert, lower level to observant.
    >>> jade.root.connected_mc.currentLabel
    'show'
    >>> jade.root.option_mc.block_mc.currentLabel
    'show'
    >>> jade.root._0_0_mc.currentLabel
    'empty_black'

    Ethan plays white, expert, so does not see top move.
    >>> news.get('top_move_mc').get('currentLabel')
    'none'
    >>> news.get('option_mc').get('empty_block_mc').get('currentLabel')
    'none'

    give lower level extra stone
    >>> jade.root.game_over_mc.extra_stone_available_mc.currentLabel
    '_7'
    >>> news.get('game_over_mc').get('extra_stone_available_mc').get('currentLabel')
    '_7'

    give lower level hide
    >>> jade.root.game_over_mc.hide_available_mc.currentLabel
    '_0'
    >>> news.get('game_over_mc').get('hide_available_mc').get('currentLabel')
    '_0'

    Adjust level balance
    >>> jade.root.game_over_mc.balance_mc.black_level_txt.text
    '42'

    Do not modify global get_expert_news()
    >>> if not expert_news_length == len(str(get_expert_news())):
    ...     expert_news_length, len(str(get_expert_news()))
    '''
    join_txt = user.root.lobby_mc.join_mc.join_txt
    #join_txt = join_mc.get('join_txt')
    if join_txt:
        owner_name = join_txt.text
        #owner_name = join_txt.get('text')
        owner = users.get(owner_name)
        if owner and 'table' == owner.root.currentLabel:
            reply = {'currentLabel': 'table', 
                'game_over_mc': {'currentLabel': 'setup'},
                'lobby_mc':  {
                    'join_mc':  {'currentLabel':  'join'}
                },
            }
            user_name = user.root.title_mc.username_txt.text
            owner_level = int(owner.root.level_mc._txt.text)
            user_level = int(user.root.level_mc._txt.text)
            if user_level <= owner_level:
                low_user = user
                high_user = owner
                low_name = user_name
                high_name = owner_name
                low_level = user_level
                high_level = owner_level
            else:
                low_user = owner
                high_user = user
                low_name = owner_name
                high_name = user_name
                low_level = owner_level
                high_level = user_level
            high_news, low_news = get_partner_news(
                high_name, low_name)
            extra_stone = get_extra_stone_available(low_level, high_level)
            extra_stone_news = get_setup_available_news('extra_stone', extra_stone)
            low_news = upgrade(extra_stone_news, low_news)
            high_news = upgrade(extra_stone_news, high_news)

            hide = get_hide_available(low_level, high_level, extra_stone)
            hide_news = get_setup_available_news('hide', hide)
            low_news = upgrade(hide_news, low_news)
            high_news = upgrade(hide_news, high_news)

            low_news = upgrade(get_aware_news(), low_news)
            low_news = upgrade(get_observant_news(), low_news)
            high_news = upgrade(get_expert_news(), high_news)
            empty_color_news = get_empty_color_news(low_user, 'black')
            low_news = upgrade(low_news, empty_color_news)
            empty_color_news = get_empty_color_news(high_user, 'white')
            high_news = upgrade(high_news, empty_color_news)
            if user_level <= owner_level:
                user_news = low_news
                owner_news = high_news
            else:
                owner_news = low_news
                user_news = high_news
            olds = imitate_news(low_user.root, low_news)
            olds = imitate_news(high_user.root, high_news)
            balance_news = adjust_level_balance_news(low_user, high_user)
            user_news = upgrade(user_news, balance_news)
            owner_news = upgrade(owner_news, balance_news)
            reply = upgrade(user_news, reply)
            tell(owner, owner_news)
            return reply


from deck import draw
def reveal_partner_history(users, user, color, intersection_name):
    '''XXX *>_<*   to maintain update_gnugo, obscurely change play_history.
    For my play_history format, see smart_go_format.py'''
    partner = get_partner(users, user)
    row, column = get_row_column(intersection_name)
    play_history = partner.play_history
    unhide(play_history, row, column)
    
def unhide(play_history, row, column):
    if [] == play_history:
        play_history.append({})
    last_event = play_history[-1]
    # last_event[get_color(partner)] = row, column
    draw(last_event, 'unhide', (row, column))

def why_not_play(users, user, intersection_mc, color, olds):
    '''
    wait your turn?
    reveal hidden?
    occupied?
    suicide on black board?
    repeat previous board?
    >>> users = setup_users(16)
    >>> joris_user = users['joris']
    >>> ethan_user = users['ethan']
    >>> set_color(ethan_user, 'black')
    >>> set_color(ethan_user, 'white')
    >>> partner = set_partner(users, ethan_user, 'joris')
    >>> partner = set_partner(users, joris_user, 'ethan')
    >>> clear_white = get_empty_color_news(ethan_user, 'white')
    >>> ethan_user.revise(clear_white)

    >>> news = {'_0_8_mc': {'currentLabel': 'play_black'}}
    >>> olds = user_as.imitate_news(joris_user.root, news)
    >>> why_not_play(users, joris_user, joris_user.root._0_8_mc, 'black', olds)
    {}

    If occupied by white or black, black, cannot play.
    >>> white_there = {'_0_8_mc': {'currentLabel': 'white'}}
    >>> olds = user_as.imitate_news(joris_user.root, white_there)
    >>> why_not_play(users, joris_user, joris_user.root._0_8_mc, 'black', olds)
    {'_0_8_mc': {'currentLabel': 'white'}}
    >>> black_there = {'_0_8_mc': {'currentLabel': 'black'}}
    >>> olds = user_as.imitate_news(joris_user.root, black_there)
    >>> why_not_play(users, joris_user, joris_user.root._0_8_mc, 'black', olds)
    {'_0_8_mc': {'currentLabel': 'black'}}

    If not white's turn, white cannot play,
    even if white has different opinion of who's turn it is.
    >>> not_your_turn = wait_your_turn(ethan_user, 'white', ethan_user.root._5_5_mc)
    >>> why_not = why_not_play(users, ethan_user, ethan_user.root._5_5_mc, 'white', olds)
    >>> if not not_your_turn == why_not:
    ...     not_your_turn, why_not
    >>> news, partner_news = update_turn(joris_user, 'black', {}, {})
    >>> play_white = {'_5_5_mc': {'currentLabel': 'play_white'}}
    >>> olds = user_as.imitate_news(ethan_user.root, play_white)
    >>> why_not = why_not_play(users, ethan_user, ethan_user.root._5_5_mc, 'white', olds)
    >>> if not not_your_turn == why_not:
    ...     not_your_turn, why_not
    
    However, if checking your turn in real-time, you can play.
    >>> clock_object = {'enter_mc': {'currentLabel': 'enter'}}
    >>> clock_news, partner_clock_news = get_clock_news(users, ethan_user, clock_object)
    >>> ethan_user.revise(clock_news)
    >>> joris_user.revise(partner_clock_news)
    >>> # mouse_down_and_sleep(ethan, ethan.root.clock_mc.enter_mc.enter_btn, 1.0 / ethan._speed)
    >>> ethan_user.revise(partner_news)
    >>> play_white = {'_5_5_mc': {'currentLabel': 'play_white'}}
    >>> ethan_user.revise(play_white)
    >>> why_not_play(users, ethan_user, ethan_user.root._5_5_mc, 'white', olds)
    {}

    When it is your turn, you can play.
    >>> olds = user_as.imitate_news(joris_user.root, news)
    >>> why_not_play(users, ethan_user, ethan_user.root._5_5_mc, 'white', olds)
    {}

    On black's board, if occupied by white or black, white, cannot play,
    even if white has different opinion of board.
    >>> white_there = {'_0_8_mc': {'currentLabel': 'white'}}
    >>> olds = user_as.imitate_news(joris_user.root, white_there)
    >>> why_not_play(users, ethan_user, ethan_user.root._0_8_mc, 'white', olds)
    {'_0_8_mc': {'currentLabel': 'white'}}
    >>> black_there = {'_0_8_mc': {'currentLabel': 'black'}}
    >>> olds = user_as.imitate_news(joris_user.root, black_there)
    >>> why_not_play(users, ethan_user, ethan_user.root._0_8_mc, 'white', olds)
    {'_0_8_mc': {'currentLabel': 'black'}}

    On black's board, if occupied by hidden black, white, cannot play.
    >>> from user_as import print_protocol_class, echo_protocol_class
    >>> ethan_user.ambassador = echo_protocol_class()
    >>> joris_user.ambassador = echo_protocol_class()
    >>> hide_there = {'_0_8_mc': {'currentLabel': 'hide_black'}}
    >>> olds = user_as.imitate_news(joris_user.root, hide_there)

    May try again.
    >>> why_not_play(users, ethan_user, ethan_user.root._0_8_mc, 'white', olds)
    {'_0_8_mc': {'currentLabel': 'black', 'hide_mc': {'currentLabel': 'reveal'}}, 'cursor_mc': {'act_mc': {'currentLabel': 'play'}}}

    ... And black play history records unhide for SGF.
    XXX *>_<* I look around for why a stone is not revealed in SGF.  Confused.

    black cannot play, even if black client has corrupted board.
    >>> news, partner_news = update_turn(joris_user, 'white', {}, {})
    >>> black_overwrite = {'_0_8_mc': {'currentLabel': 'play_black'}}
    >>> olds = user_as.imitate_news(joris_user.root, black_overwrite)
    >>> why_not_play(users, joris_user, joris_user.root._0_8_mc, 'white', olds)
    {'_0_8_mc': {'currentLabel': 'black'}}

    If suicide on black's board, cannot play and reveal assassins to both players.
    >>> board = referee.hide_suicide_board
    >>> black_board_news = board_to_news(board, joris_user.intersection_mc_array, 'black')
    >>> olds = user_as.imitate_news(joris_user.root, black_board_news)
    >>> white_board_news = board_to_news(board, joris_user.intersection_mc_array, 'white')
    >>> olds = user_as.imitate_news(ethan_user.root, white_board_news)
    >>> joris_user.root._6_5_mc.currentLabel
    'hide_black'
    >>> ethan_user.root._6_5_mc.currentLabel
    'empty_white'
    >>> joris_user.play_history
    [{'unhide': [(0, 8)]}]

    Message sent to partner.
    >>> ethan_user.ambassador = echo_protocol_class()
    >>> joris_user.ambassador = print_protocol_class()
    >>> why_not = why_not_play(users, ethan_user, ethan_user.root._5_5_mc, 'white', olds) #doctest: +ELLIPSIS
    {'title_mc': {'username_txt': {'text': 'joris'}, 'slave_txt': {'text': 'slave'}, 'password_txt': {'text': 'j'}, 'master_txt': {'text': 'master'}}, '_6_5_mc': {'hide_mc': {'currentLabel': 'reveal'}}, 'sequence': [{'time_txt': {'text': '2500'}, '_6_5_mc': {'currentLabel': 'black'}}]}
    
    And partner play history reveals hidden, so that it may be converted to SGF.
    >>> if not joris_user.play_history[-1] == {'unhide': [(0, 8), (6, 5)]}:
    ...     referee.pb(board)
    ...     joris_user.pb()
    ...     import pprint
    ...     pprint.pprint(joris_user.play_history)

    >>> why_not.get('help_mc')
    {'currentLabel': 'suicide'}
    >>> why_not.get('_5_5_mc')
    {'currentLabel': 'empty_white'}
    >>> why_not.get('_6_5_mc')
    {'currentLabel': 'black', 'hide_mc': {'currentLabel': 'reveal'}}
    >>> joris_user.root._6_5_mc.currentLabel
    'black'

    If suicide for black, black cannot play, 
    and if black can see strike, black sees suicide strike.
    >>> joris_user.pb()
    ,X,,XOOO,
    X,,,XO,OX
    ,,,,XOOXX
    XX,,XXOXX
    OXXXXOXXX
    OOOXX,XXX
    ,,,OOXOOX
    XO,,,,,OO
    O,O,,,,,,
    >>> news, partner_news = update_turn(joris_user, 'white', {}, {})
    >>> black_suicide = {'_1_6_mc': {'currentLabel': 'play_black'}}
    >>> olds = user_as.imitate_news(joris_user.root, black_suicide)
    >>> why_not = why_not_play(users, joris_user, joris_user.root._1_6_mc, 'black', olds)
    >>> why_not.get('_1_6_strike_mc').get('north_mc')
    {'currentLabel': 'black_capture_retaliate'}

    May try again.
    >>> why_not['cursor_mc']['act_mc']['currentLabel']
    'play'

    If no olds, then check existing state.
    >>> why_not = why_not_play(users, joris_user, joris_user.root._0_2_mc, 'black', {})
    >>> why_not
    {}
    
    #+ TODO:  Enable multiple tests in mock.
    #+ >>> code_unit.doctest_unit(client.capture_example)
    #+ >>> code_unit.doctest_unit(client.real_time_example)
    '''
    sorry = {}
    try_again = {'cursor_mc': {'act_mc': {'currentLabel': 'play'}}}
    partner = get_partner(users, user)
    if 'black' == get_color(user):
        author = user
    elif 'black' == get_color(partner):
        author = partner
    else:
        ## import pdb; pdb.set_trace();
        logging.error('why_not_play: for wait your turn who is black? %s' % intersection_mc.name)
        return {'gateway_mc':  
            {'currentLabel': 'what_message'},
            'help_mc':  {'currentLabel': 'color'}}
    authentic_intersection_mc = author.root[intersection_mc.name]
    if 'turn' == author.root.clock_mc.currentLabel:
        not_your_turn = wait_your_turn(author, color, authentic_intersection_mc)
    elif 'time' == author.root.clock_mc.currentLabel:
        not_your_turn = None
        # not_your_turn = wait_your_turn(user, color, authentic_intersection_mc)
    else:
        logging.error('why_not_play: what mode is clock in? %s' % intersection_mc.name)
        return {'gateway_mc':  
            {'currentLabel': 'what_message'},
            'help_mc':  {'currentLabel': 'color'}}
    if not_your_turn:
        sorry = upgrade(sorry, not_your_turn)
        return sorry
    if 'eat' == user.root.eat_mc.act_mc.currentLabel:
        # see client.real_time_example
        empty = 'empty_' + color
        return {
            'help_mc': {
                'currentLabel': 'eat'},
            intersection_mc.name: {
                'currentLabel': empty}
        }
    # occupied
    if 'hide_black' == authentic_intersection_mc.currentLabel:
        sorry = upgrade(sorry, try_again)
        revealed = {intersection_mc.name:  {'currentLabel': 'black',
                'hide_mc': {'currentLabel': 'reveal'}}}
        sorry = upgrade(sorry, revealed)
        reveal_partner_history(users, user, color, intersection_mc.name)
        tell(partner, revealed)
        return sorry
    if 'black' == authentic_intersection_mc.currentLabel \
            or 'white' == authentic_intersection_mc.currentLabel:
        sorry = upgrade(sorry, try_again)
        return user_as.get_note(authentic_intersection_mc, 'currentLabel')
    if user == author:
        if olds:
            old_intersection = olds.get(authentic_intersection_mc.name)
            if old_intersection:
                old_label = old_intersection.get('currentLabel')
                if 'black' == old_label or 'white' == old_label:
                    return {authentic_intersection_mc.name: {
                        'currentLabel': old_label}
                    }
    # end occupied
    intersection_mc_array = author.intersection_mc_array
    pre_board_text = flash_to_text(intersection_mc_array)
    pre_board = referee.text_to_array(pre_board_text)
    row, column = get_row_column(intersection_mc.name)
    if referee.is_suicide(pre_board, color, row, column):
        strike_enabled = 'show' == user.root.strike_mc.currentLabel
        if strike_enabled:
            captures = referee.find_capture(pre_board, (row, column))
            strike_news = get_strike_news(user.intersection_mc_array, 
                    pre_board, user.root, row, column, captures)
            sorry = upgrade(sorry, strike_news)
        empty = 'empty_' + color
        sorry = upgrade(sorry, try_again)
        suicide = {intersection_mc.name: {'currentLabel': empty},
                'help_mc':  {'currentLabel': 'suicide'}}
        sorry = upgrade(sorry, suicide)
        new_mark = referee.label_to_mark(color)
        # reveal assassins
        revealed_board, assassins = referee.foresee_black_assassins(pre_board,
            new_mark, row, column)
        if assassins:
            assassin_news = {}
            for row, column in assassins:
                intersection_name = user_as.get_intersection_name(row, column)
                revealed = {intersection_name:  {'currentLabel': 'black',
                        'hide_mc': {'currentLabel': 'reveal'}}}
                assassin_news = upgrade(assassin_news, revealed)
                reveal_partner_history(users, user, color, intersection_name)
            sorry = upgrade(sorry, assassin_news)
            tell(partner, assassin_news)
            return sorry
    # get_repeat_news:  see client.capture_example
    board_history = author.board_history
    if 2 <= len(board_history) \
            and referee.is_repeat(board_history[-2], pre_board,
                    color, row, column):
        sorry = upgrade(sorry, try_again)
        empty = 'empty_' + color
        label = 'repeat'
        repeat = {
            intersection_mc.name: {
                    'currentLabel': empty,
                    'block_north_mc': {'currentLabel': label},
                    'block_east_mc': {'currentLabel': label},
                    'block_south_mc': {'currentLabel': label},
                    'block_west_mc': {'currentLabel': label}
            },
            'help_mc':  {'currentLabel': label}
        }
        sorry = upgrade(sorry, repeat)
    return sorry

def prepare_stone(users, user, intersection_mc, color, user_news):
    '''prepare or reject stone to play.
    >>> users, ethan, joris = setup_ethan_joris()
    >>> news = {'_0_8_mc': {'currentLabel': 'preview_black'}}
    >>> joris.revise(news)
    >>> ok, news = prepare_stone(users, joris, joris.root._0_8_mc, 'black', news)
    >>> ok
    True
    >>> joris.root._0_8_mc.currentLabel
    'preview_black'
    >>> ethan.root._0_8_mc.currentLabel
    'empty_white'
    >>> news = {'_0_8_mc': {'currentLabel': 'preview_black'}}
    >>> ethan.revise(news)
    >>> ok, news = prepare_stone(users, 
    ...     ethan, ethan.root._0_8_mc, 'white', news)
    >>> ok
    False
    >>> ethan.revise(news)
    >>> if ethan.root._0_8_mc.currentLabel != 'empty_white':
    ...     news
    '''
    news = {}
    #- news = clear_preview(user)
    if user.olds_list:
        olds = user.olds_list[-1]
    else:
        olds = {}
    sorry = why_not_play(users, user, intersection_mc, color, olds)
    if sorry:
        news = upgrade(news, sorry)
        return False, news
    board_text = flash_to_text(user.intersection_mc_array)
    before_log = 'prepare_stone(... %s, %s ...):\n%s' \
            % (intersection_mc.name, color, board_text) 
    logging.info(before_log)
    user.revise(user_news)
    return True, news




def setup_ethan_joris():
    '''setup server users for testing.
    >>> users, ethan, joris = setup_ethan_joris()

    Publish quietly.
    >>> ethan.publish({})
    '''
    users = setup_users(16, setup_events = False)
    joris = users.get('joris')
    ethan = users.get('ethan')
    ethan.ambassador = user_as.echo_protocol_class()
    joris.ambassador = user_as.echo_protocol_class()
    set_color(ethan, 'black')
    set_color(ethan, 'white')
    partner = set_partner(users, ethan, 'joris')
    partner = set_partner(users, joris, 'ethan')
    clear_white = get_empty_color_news(ethan, 'white')
    ethan.revise(clear_white)
    return users, ethan, joris
    
def setup_example_logger(filename = 'example.log', level = logging.INFO):
    '''Log doctest examples to file.
    >>> example_logger = setup_example_logger('_test_example.log', logging.CRITICAL)
    '''
    import time
    import logging.handlers
    example_handler = logging.handlers.RotatingFileHandler(
            filename, mode='a', encoding='utf8')
    example_logger = logging.getLogger(name='example')
    example_logger.addHandler(example_handler)
    example_logger.setLevel(level)
    time_stamp = time.asctime()
    setup_log = '>>> # %s level %i at %s' \
            % (filename, level, time_stamp) 
    example_logger.info(setup_log)
    return example_logger



def get_available_news(prefix, label): 
    return {
        'option_mc': {
            prefix + '_available_mc': {
                'currentLabel': label,
            }
        }
    }

def start_game(users, user, example_logger):
    r'''Joris starts a turn-based game.
    >>> users, ethan, joris = setup_ethan_joris()
    >>> example_logger = setup_example_logger('_test_example.log', logging.CRITICAL)

    If not in setup, error.
    >>> jade = users.get('jade')
    >>> from mock_client import echo_protocol_class
    >>> jade.ambassador = echo_protocol_class()
    >>> jade.root.game_over_mc.start_mc.gotoAndPlay('enter')
    >>> start_game(users, jade, example_logger)
    >>> jade.root.game_over_mc.start_mc.currentLabel
    'none'

    If no partner, reset button.
    >>> jade.root.game_over_mc.gotoAndPlay('setup')
    >>> jade.root.game_over_mc.start_mc.gotoAndPlay('enter')
    >>> start_game(users, jade, example_logger)
    >>> jade.root.game_over_mc.start_mc.currentLabel
    'none'

    To start, Joris must be in setup.
    >>> joris.root.game_over_mc.gotoAndPlay('setup')

    Notify Joris' partner, Ethan.
    >>> ethan.root.game_over_mc.gotoAndPlay('setup')

    Provide extra stone
    Ethan sets four extra stones.
    >>> ethan.root.game_over_mc.extra_stone_available_mc._4_mc.dispatchEvent(mouseDown)

    Provide hide
    Ethan sets one hide for black.
    >>> ethan.root.game_over_mc.hide_available_mc._1_mc.dispatchEvent(mouseDown)

    If on, show score
    >>> joris.root.option_mc.score_mc.gotoAndPlay('show')
    >>> start_game(users, ethan, example_logger)
    >>> ethan.root.game_over_mc.currentLabel
    'none'

    regardless of who presses start, black moves first.
    >>> jade = joris
    >>> is_your_turn(ethan)
    False
    >>> is_your_turn(jade)
    True
    
    Reset start button.
    >>> ethan.root.game_over_mc.start_mc.currentLabel
    'none'
    >>> joris.root.game_over_mc.start_mc.currentLabel
    'none'

    >>> joris.root.score_mc.currentLabel
    'show'

    Joris has four extra stones.
    >>> joris.root.option_mc.extra_stone_available_mc.currentLabel
    '_4'

    In this match Jade may receive no more than one hide.
    >>> jade.root.option_mc.hide_available_mc.currentLabel
    '_1'

    Since Jade has hide, tutor suggests using them rather than extra stone.
    >>> jade.root.sgf_file_txt.text
    'sgf/beginner/hide_tutor.sgf'
    >>> jade.root.sgf_path_txt.text
    '[]'
    '''
    reply = {
        'game_over_mc': {
            'currentLabel': 'none',
            'start_mc': {
                'currentLabel': 'none'} } }
    error_reply = {
        'game_over_mc': {
            'start_mc': {
                'currentLabel': 'none'} } }
    if 'setup' != user.root.game_over_mc.currentLabel \
            and 'preview' != user.root.game_over_mc.currentLabel:
        label_log = 'start_game: %s must be in setup or preview, not %s' \
                % (user.root.title_mc.username_txt.text, 
                        user.root.game_over_mc.currentLabel)
        logging.error(label_log)
        ## import pdb; pdb.set_trace();
        ## return user.publish(reply)
        return user.publish(error_reply)
    start_game_log = write_mouse_down(user, 
            user.root.game_over_mc.start_mc)
    example_logger.info(start_game_log)
    partner_news = {
        'game_over_mc': {
            'currentLabel': 'none',
            'start_mc': {
                'currentLabel': 'none'} } }
    partner = get_partner(users, user)
    if not partner:
        logging.error('start_game:  no partner')
        ## import pdb; pdb.set_trace();
        return user.publish(error_reply)
    # set extra stone
    author = get_author(users, user)
    if not author:
        logging.error('start_game:  no author')
        ## import pdb; pdb.set_trace();
        return user.publish(error_reply)
    if user == author:
        author_news = reply
        reader_news = partner_news
    else:
        author_news = partner_news
        reader_news = reply
    def _available_news(prefix, author, author_news, reader_news):
        '''distribute prefix_available and tutor'''
        available_label = author.root.game_over_mc[prefix + 
                '_available_mc'].currentLabel
        available_news = get_available_news(prefix, available_label)
        author_news = upgrade(author_news, available_news)
        no_available_news = get_available_news(prefix, '_0')
        reader_news = upgrade(reader_news, no_available_news)
        # tutor available.  see hide_lesson_example
        available = int(available_label[1:])
        if 1 <= available and not author.root.sgf_file_txt.text:
            tutor_news = {
                'sgf_file_txt': {'text': 'sgf/beginner/'+prefix+'_tutor.sgf'},
                'sgf_path_txt': {'text': '[]'},
            }
            author_news = upgrade(author_news, tutor_news)
    _available_news('extra_stone', author, author_news, reader_news)
    _available_news('hide', author, author_news, reader_news)

    reply, partner_news = update_turn(user, 'white', reply, partner_news)
    reply = update_empty_block(user, None, get_color(user), reply)
    show_score = user.root.option_mc.score_mc.currentLabel
    if show_score != user.root.score_mc.currentLabel:
        score_news = {'score_mc': {'currentLabel': show_score}}
        reply = upgrade(reply, score_news)
    partner_show_score = partner.root.option_mc.score_mc.currentLabel
    if partner_show_score != partner.root.score_mc.currentLabel:
        partner_score_news = {'score_mc': {'currentLabel': partner_show_score}}
        partner_news = upgrade(partner_news, partner_score_news)
    tell(partner, partner_news)
    ## play sgf file
    #sgf_file = user.root.sgf_file_txt.text
    #if sgf_file and 'sgf_file_txt' != sgf_file:
    #    play_sgf_news = {
    #        'play_sgf_mc': {
    #            'dispatchEvent': user_as.MouseEvent.MOUSE_DOWN
    #        }
    #    }
    #    reply = upgrade(reply, play_sgf_news)
    return user.publish(reply)

# end multiple users algorithms

import code_unit
snippet = '''
# !start python code_explorer.py --import client.py --snippet snippet
import super_users; super_users = reload(super_users); from super_users import *
code_unit.doctest_unit(to_clear_table)
# run_examples(shell, to_clear_table.__doc__)
'''
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
    

