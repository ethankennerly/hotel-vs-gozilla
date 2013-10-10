#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Manipulate Flash compatible intersection_mc and referee board.
'''
__author__ = 'Ethan Kennerly'

#from remote_control import upgrade
from remote_control import *
from user_as import get_intersection_name # XXX few dependencies needed.
from user_as import logging, logging_levels, log_level, globe_class
import referee


# Convert Flash intersection_mc  to referee board

def get_row_column(intersection_name):
    '''Row and column of the name of an intersection movie clip.
    >>> get_row_column('_3_2_mc')
    (3, 2)
    >>> get_row_column('_4_8_strike_mc')
    (4, 8)
    >>> get_row_column('')
    Traceback (most recent call last):
      ...
    AssertionError: get_row_column: what is intersection? ''
    '''
    assert intersection_name, "get_row_column: what is intersection? '%s'" \
            % intersection_name
    row = int(intersection_name[1])
    column = int(intersection_name[3])
    return row, column

def get_intersection_color(intersection_mc):
    '''black, white, or None.
    >>> marije = globe_class()
    >>> marije.create(1)
    >>> marije.root._0_0_mc.gotoAndPlay('preview_hide_black')
    >>> get_intersection_color(marije.root._0_0_mc)
    'black'
    >>> marije.root._0_1_mc.gotoAndPlay('question_black')
    >>> get_intersection_color(marije.root._0_1_mc)
    'black'
    >>> marije.root._1_0_mc.gotoAndPlay('play_black')
    >>> get_intersection_color(marije.root._1_0_mc)
    'black'
    >>> marije.root._1_2_mc.gotoAndPlay('black')
    >>> get_intersection_color(marije.root._1_2_mc)
    'black'
    >>> marije.root._2_4_mc.gotoAndPlay('white')
    >>> get_intersection_color(marije.root._2_4_mc)
    'white'
    >>> marije.root._8_5_mc.gotoAndPlay('empty_black')
    >>> get_intersection_color(marije.root._8_5_mc)
    '''
    if intersection_mc.currentLabel.startswith('empty'):
        return
    for color in ['black', 'white']:
        if intersection_mc.currentLabel.endswith(color):
            return color

def intersection_mc_to_text(intersection_mc):
    '''
    >>> user = globe_class()
    >>> user.create(1)
    >>> user.root._0_0_mc.gotoAndPlay('preview_hide_black')
    >>> intersection_mc_to_text(user.root._0_0_mc)
    '['
    '''
    label = intersection_mc.currentLabel
    board_mark = referee.label_to_mark(label)
    return board_mark


from remote_control import get_note
def get_decoration_note(intersection_mc_array):
    '''
    >>> judith = globe_class()
    >>> judith.create()
    >>> news = get_decoration_note(judith.intersection_mc_array)
    >>> len(news.keys())
    81
    '''
    news = {}
    for row in intersection_mc_array:
        for intersection_mc in row:
            note = get_note(intersection_mc.decoration_mc, 'currentLabel')
            news = upgrade(news, note)
    return news


def flash_to_text(intersection_mc_array):
    '''Convert movieclips into board text, which referee can read.
    >>> joris = globe_class()
    >>> joris.create()
    >>> len(joris.intersection_mc_array)
    9
    >>> print flash_to_text(joris.intersection_mc_array)
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    '''
    board_text = ''
    for row in intersection_mc_array:
        if board_text:
            board_text += '\n'
        for intersection_mc in row:
            board_text += intersection_mc_to_text(intersection_mc)
    return board_text


def news_to_board(news):
    '''Convert news to a board.
    >>> from lesson import sgf_to_history, _may_add_stone, get_board_setup
    >>> from super_users import to_resize_board
    >>> history = sgf_to_history('sgf/test_score_rule_territory.sgf')
    >>> news = _may_add_stone(history[0])
    >>> news, size = get_board_setup(history, news)
    >>> resize_news = to_resize_board(9, size)
    >>> news = upgrade(news, resize_news)
    >>> board = news_to_board(news)
    >>> referee.pb(board)
    ,,XXX
    XXXXX
    XXOOO
    XXO,O
    ,,,O,
    '''
    from super_user import user_class
    user = user_class()
    user.create()
    user.setup_events()
    user.revise(news)
    text = flash_to_text(user.intersection_mc_array)
    board = referee.text_to_array(text)
    return board

def board_to_news(board, intersection_mc_array, player_color):
    '''return news of color or empty (or hidden to black color)
    >>> referee.is_black_hidden(referee.play_hide_black_board[2][1])
    True

    Beware, converts play_hide_black to hide_black.
    >>> from super_user import user_class
    >>> user = user_class()
    >>> user.create(1)
    >>> news = board_to_news(referee.play_hide_black_board, 
    ...     user.intersection_mc_array, 'black')
    >>> news.get('_2_1_mc').get('currentLabel')
    'hide_black'

    Beware, does not rehide a hidden stone that white somehow sees.
    >>> board = referee.hide_suicide_board

    Giving white the news to black would reveal hidden.
    >>> black_board_news = board_to_news(board, user.intersection_mc_array, 'black')
    >>> olds = imitate_news(user.root, black_board_news)
    >>> user.pb()
    ,X,,XOOO,
    X,,,XO,OX
    ,,,,XOOXX
    XX,,XXOXX
    OXXXXOXXX
    OOOXX,XXX
    ,,,OO/OOX
    XO,,,,,OO
    O,O,,,,,,
    >>> white_board_news = board_to_news(board, user.intersection_mc_array, 'white')
    >>> white_board_news.get('_6_5_mc')
    >>> olds = imitate_news(user.root, white_board_news)
    >>> user.pb()
    ,X,,XOOO,
    X,,,XO,OX
    ,,,,XOOXX
    XX,,XXOXX
    OXXXXOXXX
    OOOXX,XXX
    ,,,OO/OOX
    XO,,,,,OO
    O,O,,,,,,
    '''
    news = {}
    for row in range(len(board)):
        for column in range(len(board[row])):
            intersection_mc = intersection_mc_array[row][column]
            if referee.is_black_hidden( board[row][column] ):
                if 'black' == player_color \
                        and not 'hide_black' == intersection_mc.currentLabel:
                    intersection_item = {intersection_mc.name:  
                        {'currentLabel':  'hide_black'}}
                    news = upgrade(news, intersection_item)
            elif referee.is_color(board[row][column], 'black'):
                if not 'black' == intersection_mc.currentLabel:
                    intersection_item = {intersection_mc.name:  
                        {'currentLabel':  'black'}}
                    news = upgrade(news, intersection_item)
            elif referee.is_color(board[row][column], 'white'):
                if not 'white' == intersection_mc.currentLabel:
                    intersection_item = {intersection_mc.name:  
                        {'currentLabel':  'white'}}
                    news = upgrade(news, intersection_item)
            elif referee.is_empty(board[row][column]):
                if not intersection_mc.currentLabel.startswith('empty_'):
                    empty = 'empty_' + player_color
                    intersection_item = {intersection_mc.name:  
                        {'currentLabel':  empty}}
                    news = upgrade(news, intersection_item)
            else:
                logging.error('board_to_news: what is this? %s' \
                        % board[row][column])
    return news

# End convert flash intersection_mc to referee board


# intersection_mc board algorithms

def get_intersection_block_news(row, column, label):
    '''News to set all four blocks to label.
    >>> news = get_intersection_block_news(0, 8, 'suicide')
    >>> news.get('_0_8_mc').get('block_north_mc')
    {'currentLabel': 'suicide'}
    '''
    intersection_name = get_intersection_name(row, column)
    intersection_item = {
            intersection_name: {
                'block_north_mc': {'currentLabel': label},
                'block_east_mc': {'currentLabel': label},
                'block_south_mc': {'currentLabel': label},
                'block_west_mc': {'currentLabel': label}
            }
        }
    return intersection_item

def get_intersection_news(row, column, owner, label):
    '''News to set all four dragon_statuss to label.
    >>> news = get_intersection_news(0, 8, 'dragon_status_mc', 'critical')
    >>> news.get('_0_8_mc').get('dragon_status_mc')
    {'currentLabel': 'critical'}
    >>> news = get_intersection_news(1, 7, 'vital_point_mc', 'defense_point')
    >>> news.get('_1_7_mc').get('vital_point_mc')
    {'currentLabel': 'defense_point'}
    >>> news = get_intersection_news(1, 8, 'suicide_mc', 'black')
    >>> news.get('_1_8_mc').get('suicide_mc')
    {'currentLabel': 'black'}
    '''
    intersection_name = get_intersection_name(row, column)
    intersection_item = {
            intersection_name: {
                owner: {'currentLabel': label},
            }
        }
    return intersection_item


def get_help(intersection_mc):
    '''Help about an intersection.  
    >>> user = globe_class()
    >>> user.create(1)
    >>> intersection_mc = user.root._0_0_mc
    >>> get_help(intersection_mc)
    {'help_mc': {'currentLabel': 'none'}}
    >>> intersection_mc.gotoAndPlay('black')
    >>> get_help(intersection_mc)
    {'help_mc': {'currentLabel': 'none'}}

    help about notice.
    >>> intersection_mc.block_north_mc.gotoAndPlay('black_block')
    >>> get_help(intersection_mc)
    {'help_mc': {'currentLabel': 'block'}}
    
    help about warning.
    >>> intersection_mc.block_north_mc.gotoAndPlay('black_warning')
    >>> intersection_mc.block_west_mc.gotoAndPlay('black_warning')
    >>> get_help(intersection_mc)
    {'help_mc': {'currentLabel': 'warning'}}
    
    help about danger.
    >>> intersection_mc.block_north_mc.gotoAndPlay('white_danger')
    >>> intersection_mc.block_west_mc.gotoAndPlay('white_danger')
    >>> intersection_mc.block_south_mc.gotoAndPlay('white_danger')
    >>> get_help(intersection_mc)
    {'help_mc': {'currentLabel': 'danger'}}
    
    help about dead.
    >>> intersection_mc.territory_mc.gotoAndPlay('white_dead')
    >>> get_help(intersection_mc)
    {'help_mc': {'currentLabel': 'dead'}}

    help about suicide.  
    >>> intersection_mc.suicide_mc.gotoAndPlay('black')
    >>> get_help(intersection_mc)
    {'help_mc': {'currentLabel': 'suicide_black'}}
    >>> intersection_mc.suicide_mc.gotoAndPlay('white')
    >>> get_help(intersection_mc)
    {'help_mc': {'currentLabel': 'suicide_white'}}

    #+ help about hidden
    '''
    colors = ['black', 'white']
    suicide_severities = ['black', 'white']
    for severity in suicide_severities:
        if severity == intersection_mc.suicide_mc.currentLabel:
                return {'help_mc': {'currentLabel': 'suicide_' + severity}}
    territory_severities = ['dead']
    for color in colors:
        for severity in territory_severities:
            color_severity = color + '_' + severity
            if color_severity == intersection_mc.territory_mc.currentLabel:
                return {'help_mc': {'currentLabel': severity}}
    def _any_block(intersection_mc, label):
        return label == intersection_mc.block_north_mc.currentLabel \
                or label == intersection_mc.block_east_mc.currentLabel \
                or label == intersection_mc.block_south_mc.currentLabel \
                or label == intersection_mc.block_west_mc.currentLabel
    block_severities = ['danger', 'warning', 'block']
    for color in colors:
        for severity in block_severities:
            label = color + '_' + severity
            if _any_block(intersection_mc, label):
                return {'help_mc': {'currentLabel': severity}}
    return {'help_mc': {'currentLabel': 'none'}}


def get_intersection_formation_news(intersection_mc, pattern, rotate):
    parent_name = pattern + '_mc'
    child_name = rotate + '_mc'
    rotate_news = {parent_name: {
        'x': intersection_mc.x, 'y': intersection_mc.y,
        child_name: 
            {'response_mc': {'currentLabel':  'response'} }
            }
    }
    return rotate_news


def get_children(movie_clip):
    child_count = movie_clip.numChildren
    return [movie_clip.getChildAt(c)
            for c in range(child_count)]

def get_response_rotate_names(formation_mc):
    '''Help find a formation that was just triggered.
    >>> user = globe_class()
    >>> user.create(1)
    >>> user.setup_events()
    >>> user.root.formation_shoulder_hit_mc.rotate_180_mc.response_mc.gotoAndPlay('response')
    >>> get_response_rotate_names(user.root.formation_shoulder_hit_mc)
    ['rotate_180_mc']
    '''    
    rotates = get_children(formation_mc)
    response_rotates = [rotate for rotate in rotates
        if 'response' == rotate.response_mc.currentLabel]
    addresses = [rotate.name
            for rotate in response_rotates]
    addresses.sort()
    return addresses


def get_remove_decoration_news(intersection_mc_array):
    '''
    >>> user = globe_class()
    >>> user.create(1)
    >>> get_remove_decoration_news(user.intersection_mc_array)
    {}
    >>> user.root._0_0_mc.decoration_mc.gotoAndPlay('white_attack')
    >>> get_remove_decoration_news(user.intersection_mc_array)
    {'_0_0_mc': {'decoration_mc': {'currentLabel': 'none'}}}
    '''
    news = {}
    label = 'none'
    for r, row in enumerate(intersection_mc_array):
        for c, intersection_mc in enumerate(row):
            if label != intersection_mc.decoration_mc.currentLabel:
                remove_decoration_news = get_intersection_news(
                        r, c, 'decoration_mc', label)
                news = upgrade(news, remove_decoration_news)
    return news

from referee import text_to_array, find_capture, find_danger, get_color
def in_danger(intersection_mc_array, intersection_mc):
    '''in_danger, but would not capture (disallows throw-in).
    revert move and comment.
    >>> from super_user import user_class
    >>> laurens = globe_class()
    >>> laurens.create(1)
    >>> laurens.setup_events()
    >>> laurens.root._0_1_mc.gotoAndPlay('white')
    >>> laurens.root._0_0_mc.gotoAndPlay('play_black')
    >>> laurens.pb()
    *O,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    >>> danger, danger_reply = in_danger(laurens.intersection_mc_array, laurens.root._0_0_mc)
    >>> danger
    True
    >>> danger_reply.has_key('comment_mc')
    True
    
    Revert intersection
    >>> danger_reply['_0_0_mc']['currentLabel']
    'empty_black'
    
    TODO:  Central place to revert cursor.
    >>> danger_reply['cursor_mc']['act_mc']['currentLabel']
    'play'
    '''
    danger, danger_reply = False, {}
    board_text = flash_to_text(intersection_mc_array)
    board = text_to_array(board_text)
    new_mark = intersection_mc_to_text(intersection_mc)
    row, column = get_row_column(intersection_mc.name)
    captures = find_capture(board, (row, column))
    if not captures:
        dangers = find_danger(board)
        if (row, column) in dangers:
            danger = True
            color = get_color(board[row][column])
            comment_news = {
                intersection_mc.name: {
                    'currentLabel': 'empty_%s' % color
                }, 
                'comment_mc': {
                    'currentLabel': 'comment',
                    '_txt': {
                        'text': 'WE WOULD BE SURROUNDED! TRY ANOTHER PLACE.'
                    }
                },
                'cursor_mc': {
                    'act_mc': {
                        'currentLabel': 'play'
                    }
                }
            }
            danger_reply = upgrade(danger_reply, comment_news)
    return danger, danger_reply


from remote_control import family_tree
def get_connected_news(intersection_mc_array, new_board):
    '''Return color-specific news to set connected shape labels.
    >>> laurens = globe_class()
    >>> laurens.create(1)
    >>> news = get_connected_news(laurens.intersection_mc_array, referee.board_lines)
    >>> news.get('_3_3_mc').get('black_shape_mc').get('currentLabel')
    '_0100'
    >>> news.get('_3_3_mc').get('white_shape_mc')

    If changing connection, then copy and paste decendents in shape.
    >>> laurens.root._3_3_mc.black_shape_mc.defend_mc.gotoAndPlay('show')
    >>> laurens.root._3_3_mc.black_shape_mc.attack_mc.defend_mc.gotoAndPlay('show')
    >>> laurens.root._3_3_mc.black_shape_mc.attack_mc.gotoAndPlay('show')
    >>> laurens.root._4_2_mc.black_shape_mc.attack_mc.gotoAndPlay('show')
    >>> news = get_connected_news(laurens.intersection_mc_array, referee.board_lines)
    >>> news['_3_3_mc']['black_shape_mc']['currentLabel']
    '_0100'

    Defend not implemented yet.
    >>> news['_3_3_mc']['black_shape_mc'].get('defend_mc')
    >>> news['_3_3_mc']['black_shape_mc']['attack_mc'].get('defend_mc')

    Iff any previous attack, attack refers to new connection.
    >>> news['_3_3_mc']['black_shape_mc']['attack_mc']['currentLabel']
    '_0100'
    >>> news['_3_4_mc']['black_shape_mc'].get('attack_mc')

    Iff new attack, attack refers to newly placed stone.
    >>> news['_4_2_mc']['black_shape_mc']['attack_mc']['currentLabel']
    '_0000'

    Attack and defend not implemented for white.
    >>> news['_1_1_mc']['white_shape_mc']['currentLabel']
    '_0110'
    >>> news['_1_1_mc']['white_shape_mc'].get('attack_mc')

    If not changing connection, then do not resend shape or decendents.
    >>> olds = imitate_news(laurens.root, news)
    >>> laurens.root._3_3_mc.gotoAndPlay('black')
    >>> laurens.root._3_3_mc.black_shape_mc.gotoAndPlay('_0100')
    >>> laurens.root._0_0_mc.gotoAndPlay('black')
    >>> news = get_connected_news(laurens.intersection_mc_array, referee.board_lines)
    >>> news.get('_3_3_mc')

    Attack updates to removed stone at 0, 0.
    >>> news['_0_0_mc']['black_shape_mc']['attack_mc']['currentLabel']
    'none'
    '''
    connected = referee.get_connected(new_board)
    labels = referee.get_labels(connected)
    news = {}
    for r, row in enumerate(labels):
        for c, label in enumerate(row):
            #if (3, 3) == (r, c):
            #    import pdb; pdb.set_trace();
            color = referee.get_color(new_board[r][c])
            intersection_name = get_intersection_name(r, c)
            if 'empty' != color:
                shape_name = '%s_shape_mc' % color
                shape_mc = intersection_mc_array[r][c][shape_name]
                if label != shape_mc.currentLabel:
                    #family_article = family_tree(shape_mc)
                    #family_news = {
                    #    intersection_name: {
                    #        shape_name: family_article
                    #    }
                    #}
                    #news = upgrade(news, family_news)
                    shape_news = get_intersection_news(r, c, shape_name, label)
                    news = upgrade(news, shape_news)
                if 'white' != color:
                    if not color == intersection_mc_array[r][c].currentLabel \
                            or label != shape_mc.currentLabel:
                        def _upgrade_shape(news, upgrade_name):
                            try:
                                old_attack = shape_mc[upgrade_name].currentLabel
                            except:
                                import pdb; pdb.set_trace();
                            if 'none' != old_attack:
                                upgrade_news = {
                                    intersection_name: {
                                        shape_name: {
                                            upgrade_name: {
                                                'currentLabel': label
                                            }
                                        }
                                    }
                                }
                                news = upgrade(news, upgrade_news)
                        _upgrade_shape(news, 'attack_mc')
                        #+ _upgrade_shape(news, 'defend_mc')
            elif 'empty' == color and not intersection_mc_array[r][c]\
                    .currentLabel.startswith(color):
                old_color = intersection_mc_array[r][c].currentLabel 
                old_shape_name = '%s_shape_mc' % old_color
                attack_news = {
                    intersection_name: {
                        old_shape_name: {
                            'attack_mc': {
                                'currentLabel': 'none'
                            }
                        }
                    }
                }
                news = upgrade(news, attack_news)
    return news



from pattern import get_info_sequence_news
def get_match_news(match, pattern_dictionary, decoration_name,
        intersection_mc_array, new_board, row, column):
    '''
    >>> user = globe_class()
    >>> user.create(1)
    >>> intersection_mc = user.root._0_0_mc
    >>> board_text = flash_to_text(user.intersection_mc_array)
    >>> new_board = referee.text_to_array(board_text)
    >>> get_match_news(referee.get_valid_matches, referee.defend_pattern_dictionary, 'defend', user.intersection_mc_array, new_board, 0, 0)
    see_same_color:  what color is ","?
    {}

    May show decoration.
    >>> user.root._2_2_mc.gotoAndPlay('black')
    >>> user.root._1_1_mc.gotoAndPlay('black')
    >>> user.root._2_4_mc.gotoAndPlay('empty_black')
    >>> intersection_mc = user.intersection_mc_array[2][2]
    >>> show_decoration = False
    >>> board_text = flash_to_text(user.intersection_mc_array)
    >>> new_board = referee.text_to_array(board_text)
    >>> news = get_match_news(referee.get_valid_matches, referee.defend_pattern_dictionary, 'defend', user.intersection_mc_array, new_board, 2, 2)
    >>> news.get('_2_1_mc')
    {'decoration_mc': {'currentLabel': 'black_defend'}}
    >>> user.root.decoration_mc.gotoAndPlay('show')
    >>> show_decoration = True
    >>> board_text = flash_to_text(user.intersection_mc_array)
    >>> new_board = referee.text_to_array(board_text)
    >>> news = get_match_news(referee.get_valid_matches, referee.defend_pattern_dictionary, 'defend', user.intersection_mc_array, new_board, 2, 2)
    >>> if not news.get('_2_1_mc'):  
    ...     from pprint import pprint; pprint(news)

    Attach info sequence.
    Imitate news must disregard this info.
    >>> from pprint import pprint
    >>> sequence = news['info']['_2_2_mc']
    >>> for figure in sequence:
    ...     pattern_name = figure['info_mc']['decoration_mc']['pattern_txt']['text']
    ...     if 'DIAGONAL' == pattern_name:
    ...         circle_label = figure['_1_1_mc']['circle_mc']['currentLabel']
    ...         if not 'show' == circle_label:
    ...             pprint(figure)
    >>> ## pprint(news['info']['_2_2_mc'])
    
    Enemy attack decoration only neutralizes attack decoration.
    >>> user.root._1_1_mc.gotoAndPlay('white')
    >>> board_text = flash_to_text(user.intersection_mc_array)
    >>> new_board = referee.text_to_array(board_text)
    >>> news = get_match_news(referee.get_valid_matches, referee.attack_pattern_dictionary, 'attack', user.intersection_mc_array, new_board, 2, 2)
    >>> [key for key in news.keys() if key.startswith('formation_')]
    []
    >>> from pprint import pprint
    >>> olds = imitate_news(user.root, news)
    >>> user.root._1_2_mc.decoration_mc.currentLabel
    'black_attack'
    >>> user.root._2_3_mc.decoration_mc.currentLabel
    'black_attack'
    >>> user.root._2_3_mc.decoration_mc.gotoAndPlay('black_attack')
    >>> user.root._3_3_mc.gotoAndPlay('white')
    >>> user.pb()
    ,,,,,,,,,
    ,O,,,,,,,
    ,,X,,,,,,
    ,,,O,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    '''
    row_column_patterns_rotates = match(
        pattern_dictionary, 
        new_board, row, column)
    match_news = {}
    if row_column_patterns_rotates:
        info = get_info_sequence_news(pattern_dictionary, row_column_patterns_rotates)
        match_news = upgrade(match_news, info)
        for row_column, patterns_rotates in row_column_patterns_rotates.items():
            r, c = row_column
            formation_enabled = False
            if formation_enabled:
                pattern_intersection_mc = intersection_mc_array[r][c]
                for pattern, rotate in patterns_rotates:
                    news = get_intersection_formation_news(
                            pattern_intersection_mc, pattern, rotate)
                    match_news = upgrade(match_news, news)
            if decoration_name:
                decorations = referee.get_matches_coordinates(
                        referee.decoration_dictionary[decoration_name], 
                        patterns_rotates, r, c)
                decorations = referee.are_empty(new_board, decorations)
                ## print 'decorations: ', decorations
                match_mark = new_board[r][c]
                color = referee.get_color(match_mark)
                partner_color = referee.opposite(color)
                for deco_row, deco_column in decorations:
                    label = color + '_' + decoration_name
                    decoration_mc = intersection_mc_array[
                            deco_row][deco_column].decoration_mc
                    # neutralize
                    if decoration_mc.currentLabel.startswith(
                            partner_color):
                        label = 'none'
                    #if 'attack' == decoration_name \
                    #        and decoration_mc.currentLabel.endswith(
                    #                decoration_name):
                    #    continue
                    if 'profit' == decoration_name:
                        if not decoration_mc.currentLabel.startswith(
                                partner_color):
                            continue
                    if label != decoration_mc.currentLabel:
                        decoration_news = get_intersection_news(
                            deco_row, deco_column, 
                            'decoration_mc', label)
                        match_news = upgrade(match_news, decoration_news)
    return match_news

def upgrade_stone_news(attack, defend, new_board, color, row, column, news):
    '''
    >>> from pprint import pprint

    Summarize formation as color, attack, defend or attack and defend.
    >>> news = {}
    >>> new_board = referee.board_lines
    >>> upgrade_stone_news(True, False, new_board, 'white', 0, 0, news)
    >>> if not 'white_attack' == news['_0_0_mc']['formation_mc']['currentLabel']:
    ...     pprint(news)

    Summarize formation at stone.
    >>> upgrade_stone_news(False, True, new_board, 'black', 2, 2, news)
    >>> if not 'black_defend' == news['_2_2_mc']['formation_mc']['currentLabel']:  
    ...     pprint(news)

    Previous news is retained
    >>> if not news.has_key('_0_0_mc'):  
    ...     pprint(news)

    Attack defend and combo formation is shown at place played.
    >>> upgrade_stone_news(True, True, new_board, 'white', 3, 3, news)
    >>> if not 'white_attack_defend' == news['_3_3_mc']['formation_mc']['currentLabel']:
    ...     pprint(news)

    Combination of attack and defend is also shown.
    Rather than independent ('attack' and 'defend'), there is 'attack_defend', 
    because combo sounds and animations must be combined too.
    >>> news['_1_4_mc'] = {'currentLabel': 'black'}
    >>> upgrade_stone_news(True, True, new_board, 'black', 1, 4, news)
    >>> if not 'black_attack_defend' == news['_1_4_mc']['formation_mc']['currentLabel']:
    ...     pprint(news)

    Show defend at shape.
    >>> if not 'show' == news['_1_4_mc']['black_shape_mc']['defend_mc']['currentLabel']:
    ...     pprint(news)

    Show attack shape at shape.
    >>> if not '_0000' == news['_1_4_mc']['black_shape_mc']['attack_mc']['currentLabel']:
    ...     pprint(news)

    Attack shape (battlement) has defend component (pillar) nested into it.
    >>> if not 'show' == news['_1_4_mc']['black_shape_mc']['attack_mc']['defend_mc']['currentLabel']:
    ...     pprint(news)
    >>> news['_1_4_mc']['currentLabel']
    'black'
    '''
    if attack or defend:
        if attack and defend:
            label = color + '_' + 'attack_defend'
        elif attack:
            label = color + '_' + 'attack'
        elif defend:
            label = color + '_' + 'defend'
        formation_news = get_intersection_news(
                row, column, 'formation_mc', label)
        news = upgrade(news, formation_news)
        if defend:
            intersection_name = get_intersection_name(row, column)
            child_name = color + '_shape_mc'
            connected = referee.get_connected(new_board)
            labels = referee.get_labels(connected)
            label = labels[row][column]
            defend_news = {
                intersection_name: {
                    child_name: {
                        'attack_mc': {
                            'defend_mc': {
                                'currentLabel': 'show'
                            }
                        },
                        'defend_mc': {
                            'currentLabel': 'show'
                        },
                    }
                }
            }
            news = upgrade(news, defend_news)
        if attack:
            intersection_name = get_intersection_name(row, column)
            child_name = color + '_shape_mc'
            connected = referee.get_connected(new_board)
            labels = referee.get_labels(connected)
            label = labels[row][column]
            attack_news = {
                intersection_name: {
                    child_name: {
                        'attack_mc': {
                            'currentLabel': label
                        },
                    }
                }
            }
            news = upgrade(news, attack_news)



def get_formation_news(new_board, intersection_mc_array, intersection_mc,
        show_profit, show_defend, show_attack, show_decoration):
    '''
    >>> user = globe_class()
    >>> user.create(1)
    >>> intersection_mc = user.root._0_0_mc
    >>> board_text = flash_to_text(user.intersection_mc_array)
    >>> new_board = referee.text_to_array(board_text)
    >>> get_formation_news(new_board, user.intersection_mc_array, intersection_mc, True, True, True, True)
    see_same_color:  what color is ","?
    see_same_color:  what color is ","?
    see_same_color:  what color is ","?
    {}

    If intersection and board differ, board takes precedence.
    >>> intersection_mc = user.root._2_2_mc
    >>> intersection_mc.gotoAndPlay('play_white')
    >>> board_text = flash_to_text(user.intersection_mc_array)
    >>> new_board = referee.text_to_array(board_text)
    >>> news = get_formation_news(new_board, user.intersection_mc_array, intersection_mc, True, True, False, False)

    #Formation enabled
    #>>> news.has_key('formation_field_mc')
    #True

    If intersection is empty, print error.
    >>> partner = globe_class()
    >>> partner.create(1)
    >>> user.root._2_2_mc.gotoAndPlay('empty_black')
    >>> user.root._2_4_mc.gotoAndPlay('black')
    >>> board_text = flash_to_text(user.intersection_mc_array)
    >>> new_board = referee.text_to_array(board_text)
    >>> intersection_mc = partner.root._2_2_mc
    >>> intersection_mc.gotoAndPlay('play_white')
    >>> news = get_formation_news(new_board, user.intersection_mc_array, intersection_mc, False, False, True, False)
    see_same_color:  what color is ","?

    May show decoration.
    >>> user.root._2_2_mc.gotoAndPlay('black')
    >>> user.root._1_1_mc.gotoAndPlay('black')
    >>> user.root._2_4_mc.gotoAndPlay('empty_black')
    >>> intersection_mc = user.intersection_mc_array[2][2]
    >>> show_decoration = False
    >>> board_text = flash_to_text(user.intersection_mc_array)
    >>> new_board = referee.text_to_array(board_text)
    >>> news = get_formation_news(new_board, user.intersection_mc_array, intersection_mc, True, True, True, show_decoration)
    >>> news.get('_2_1_mc')

    Even if do not show decoration, do show decorated stone.
    >>> news['_2_2_mc']['black_shape_mc']
    {'defend_mc': {'currentLabel': 'show'}, 'attack_mc': {'defend_mc': {'currentLabel': 'show'}}}

    >>> user.root.decoration_mc.gotoAndPlay('show')
    >>> show_decoration = True
    >>> board_text = flash_to_text(user.intersection_mc_array)
    >>> new_board = referee.text_to_array(board_text)
    >>> news = get_formation_news(new_board, user.intersection_mc_array, intersection_mc, True, True, True, show_decoration)
    >>> if not news.get('_2_1_mc'):  
    ...     from pprint import pprint; pprint(news)

    Summarize formation at stone.
    >>> from pprint import pprint
    >>> if not 'black_defend' == news['_2_2_mc']['formation_mc']['currentLabel']:  
    ...     pprint(news)

    >>> intersection_mc = user.intersection_mc_array[3][3]
    >>> intersection_mc.gotoAndPlay('white')
    >>> board_text = flash_to_text(user.intersection_mc_array)
    >>> new_board = referee.text_to_array(board_text)
    >>> news = get_formation_news(new_board, user.intersection_mc_array, intersection_mc, True, True, True, show_decoration)

    Attack defend and combo formation is shown at place played.
    >>> if not news.get('_3_3_mc').get('formation_mc') == {'currentLabel': 'white_attack_defend'}:
    ...     pprint(news)

    Combination of attack and defend is also shown.
    Rather than independent ('attack' and 'defend'), there is 'attack_defend', 
    because combo sounds and animations must be combined too.
    >>> intersection_mc = user.intersection_mc_array[1][4]
    >>> intersection_mc.gotoAndPlay('black')
    >>> board_text = flash_to_text(user.intersection_mc_array)
    >>> new_board = referee.text_to_array(board_text)
    >>> news = get_formation_news(new_board, user.intersection_mc_array, intersection_mc, True, True, True, show_decoration)
    >>> if not news.get('_1_4_mc').get('formation_mc') == {'currentLabel': 'black_attack_defend'}:
    ...     pprint(news)

    Undo part of this combo.
    >>> user.root._4_2_mc.decoration_mc.gotoAndPlay('black_attack')
    >>> user.root._5_2_mc.decoration_mc.gotoAndPlay('black_defend')
    >>> user.root._1_4_mc.gotoAndPlay('empty_black')
    >>> intersection_mc = user.intersection_mc_array[3][3]
    >>> board_text = flash_to_text(user.intersection_mc_array)
    >>> new_board = referee.text_to_array(board_text)

    To check pattern, new board is used rather than user intersection 
    which is not going to be updated until publishing all news in one batch.
    Thus, new board is correct after capture; whereas client is out of date.
    >>> user.root._1_1_mc.gotoAndPlay('empty_black')
    >>> user.root._2_2_mc.gotoAndPlay('empty_black')
    >>> user.root._3_3_mc.gotoAndPlay('empty_black')
    >>> user.root._3_4_mc.gotoAndPlay('empty_black')
    >>> news = get_formation_news(new_board, user.intersection_mc_array, intersection_mc, True, True, True, show_decoration)
    >>> news.get('_4_2_mc')
    {'decoration_mc': {'currentLabel': 'none'}}
    >>> news.get('_5_2_mc')
    {'decoration_mc': {'currentLabel': 'none'}}

    If no match for self, then do not show nearest enemy,
    and curse the position.
    >>> user.root._0_0_mc.gotoAndPlay('black')
    >>> user.root._2_2_mc.gotoAndPlay('white')
    >>> user.root._0_1_mc.decoration_mc.gotoAndPlay('none')
    >>> user.root._1_2_mc.decoration_mc.gotoAndPlay('none')
    >>> board_text = flash_to_text(user.intersection_mc_array)
    >>> new_board = referee.text_to_array(board_text)
    >>> intersection_mc = user.intersection_mc_array[0][0]
    >>> news = get_formation_news(new_board, user.intersection_mc_array, intersection_mc, True, True, True, show_decoration)
    >>> news.get('_1_2_mc')

    {'decoration_mc': {'currentLabel': 'white_attack'}}

    Summarize formation as color, attack, defend or attack and defend.
    >>> from pprint import pprint
    >>> if news.get('_0_0_mc') == {'formation_mc': {'currentLabel': 'white_attack_curse'}}:
    ...     pprint(news)

    # TODO
    #Decoration disappears next turn.
    #>>> olds = imitate_news(user.root, news)
    #>>> news = get_formation_news(new_board, user.intersection_mc_array, intersection_mc, True, True, True, show_decoration)
    #>>> if not 'none' == news['_1_2_mc']['decoration_mc']['currentLabel']:  
    #...     from pprint import pprint; pprint(news)

    See user_interface_example.py:formation_example.
    For decorations see playtest.py:ezra_begins_example.
    '''
    news = {}
    #new_board_text = flash_to_text(intersection_mc_array)
    #new_board = referee.text_to_array(new_board_text)
    #row, column = get_row_column(intersection_mc.name)
    #mark = eval('referee.%s' % intersection_mc.currentLabel)
    #new_board[row][column] = mark
    row, column = get_row_column(intersection_mc.name)
    mark = new_board[row][column]
    def upgrade_matches(match, news, new_board, row, column):
        if show_profit:
            profit = get_match_news(match, referee.profit_pattern_dictionary,
                    'profit', intersection_mc_array, new_board, row, column)
            if show_decoration:
                news = upgrade(news, profit)
        if show_defend:
            defend = get_match_news(match, referee.defend_pattern_dictionary,
                    'defend', intersection_mc_array, new_board, row, column)
            if show_decoration:
                news = upgrade(news, defend)
        else:
            defend = None
        if show_attack:
            attack = get_match_news(match, referee.attack_pattern_dictionary,
                    'attack', intersection_mc_array, new_board, row, column)
            if show_decoration:
                news = upgrade(news, attack)
        else:
            attack = None
        color = referee.get_color(mark)
        upgrade_stone_news(attack, defend, new_board, color, row, column, news)
    upgrade_matches(referee.get_valid_matches, news, new_board, row, column)
    #if not news:
    #    if show_attack:
    #        attack = get_match_news(referee.get_nearest_enemy_matches,
    #                referee.attack_pattern_dictionary, 'attack', 
    #                intersection_mc_array, new_board, row, column)
    #        if attack:
    #            news = upgrade(news, attack)
    #            color = referee.get_color(mark)
    #            partner_color = referee.opposite(color)
    #            label = partner_color + '_' + 'attack_curse'
    #            formation_news = get_intersection_news(
    #                row, column, 'formation_mc', label)
    #            news = upgrade(news, formation_news)
    if show_decoration:
        label = 'none'
        decoration_mc = intersection_mc_array[row][column].decoration_mc
        if label != decoration_mc.currentLabel:
            remove_decoration_news = get_intersection_news(
                    row, column, 'decoration_mc', label)
            news = upgrade(news, remove_decoration_news)
    return news


def any_label_equals(intersection_mc_array, label):
    for row in intersection_mc_array:
        for intersection_mc in row:
            if label == intersection_mc.currentLabel:
                return True
    return False

def children_label_equals(intersection_mc_array, child_name, label):
    children = []
    for row in intersection_mc_array:
        for intersection_mc in row:
            if label == intersection_mc[child_name].currentLabel:
                children.append(intersection_mc.name)
    return children

def label_from_to(intersection_mc_array, from_label, to_label):
    news = {}
    for row in intersection_mc_array:
        for intersection_mc in row:
            if from_label == intersection_mc.currentLabel:
                news[intersection_mc.name] = {
                        'currentLabel': to_label}
    return news

def child_label_from_to(intersection_mc_array, child_name, from_label, to_label):
    '''News to change child of intersection from old to new label.
    >>> stephen = globe_class()
    >>> stephen.create(1)
    >>> stephen.root._1_2_mc.top_move_mc.gotoAndPlay('white')
    >>> child_label_from_to(stephen.intersection_mc_array, 'top_move_mc', 'white', 'none')
    {'_1_2_mc': {'top_move_mc': {'currentLabel': 'none'}}}
    '''
    news = {}
    for row in intersection_mc_array:
        for intersection_mc in row:
            if from_label == intersection_mc[child_name].currentLabel:
                news[intersection_mc.name] = {
                    child_name: {
                        'currentLabel': to_label
                    }
                }
    return news

def update_child_label(intersection_mc_array, coordinates, 
        child_name, to_label, from_labels = []):
    '''News that will change child of an intersection.
    >>> kyung = globe_class()
    >>> kyung.create(1)
    >>> coordinates = [(2, 4), (3, 5)]
    >>> kyung.root._2_4_mc.formation_mc.gotoAndPlay('white_attack_curse')
    >>> update_child_label(kyung.intersection_mc_array, 
    ...     coordinates, 'formation_mc', 'none')
    {'_2_4_mc': {'formation_mc': {'currentLabel': 'none'}}}

    If 'from_labels', then only update those.  
    I use this to remove dead marks.
    >>> coordinates = [(2, 4), (3, 5)]
    >>> kyung.root._2_4_mc.territory_mc.gotoAndPlay('black_dead')
    >>> kyung.root._3_5_mc.territory_mc.gotoAndPlay('white')
    >>> update_child_label(kyung.intersection_mc_array, 
    ...     coordinates, 'territory_mc', 'none', ['black_dead', 'white_dead'])
    {'_2_4_mc': {'territory_mc': {'currentLabel': 'none'}}}
    '''
    news = {}
    for row, column in coordinates:
        from_label = intersection_mc_array[row][column][child_name].currentLabel
        if from_labels and from_label not in from_labels:
            continue
        if to_label != from_label:
            intersection_name = get_intersection_name(row, column)
            news[intersection_name] = {
                child_name: {
                    'currentLabel': to_label
                }
            }
    return news

def child_label_to(coordinates, child_name, to_label):
    '''News that will change (perhaps redundantly) child of an intersection.
    >>> coordinates = [(0, 0)]
    >>> child_label_to(coordinates, 'block_north_mc', 'none')
    {'_0_0_mc': {'block_north_mc': {'currentLabel': 'none'}}}
    '''
    news = {}
    for row, column in coordinates:
        intersection_name = get_intersection_name(row, column)
        news[intersection_name] = {
            child_name: {
                'currentLabel': to_label
            }
        }
    return news

def child_labels_to(coordinates, child_labels):
    '''Sequence of child labels.
    >>> child_labels = {
    ...     'block_north_mc': 'none',
    ...     'block_east_mc': 'east'}
    >>> news = child_labels_to([(0, 0), (0, 1)], child_labels)
    >>> from pprint import pprint
    >>> pprint(news)
    {'_0_0_mc': {'block_east_mc': {'currentLabel': 'east'},
                 'block_north_mc': {'currentLabel': 'none'}},
     '_0_1_mc': {'block_east_mc': {'currentLabel': 'east'},
                 'block_north_mc': {'currentLabel': 'none'}}}
    '''
    news = {}
    for child_name, label in child_labels.items():
        child_news = child_label_to(coordinates, child_name, label)
        news = upgrade(news, child_news)
    return news


    
    
def intersections_do(coordinates, property, label):
    news = {}
    for r, c in coordinates:
        name = get_intersection_name(r, c)
        news[name] = {property: label}
    return news

def many(client, rows, function, *args):
    coordinates = [(r, c) for r in rows for c in range(9)]
    news = function(coordinates, *args)
    client.publish(news)
    import time
    time.sleep(1.0/2)
    
def blit(client, function, *args):
    for repeat in range(3):
        start = repeat * 3
        stop = start + 3
        many(client, range(start, stop), function, *args)
    

def blit_example():
    '''
    >>> blit(child_label_to, 'territory_mc', 'none')
    >>> blit(child_label_to, 'liberty_north_mc', 'none')
    >>> blit(child_label_to, 'liberty_south_mc', 'none')
    >>> blit(child_label_to, 'liberty_east_mc', 'none')
    >>> blit(child_label_to, 'liberty_west_mc', 'none')
    >>> blit(set_coordinate_news, 'suicide_mc', 'none')
    >>> blit(intersections_do, 'currentLabel', 'empty_black')
    >>> blit(intersections_do, 'currentLabel', 'none')

    frame rate still about 12.
    '''


def get_repeat_item(intersection_name, color):
    '''
    >>> repeats = referee.find_repeats(referee.before_ko_board, referee.start_ko_board, 'white')
    >>> repeats
    [(0, 0)]
    >>> repeat_news = get_repeat_item('_0_0_mc', 'white')
    >>> repeat_news.get('_0_0_mc').get('block_north_mc')
    {'currentLabel': 'repeat'}
    '''
    label = 'repeat'
    empty = 'empty_' + color
    return {
        intersection_name: {
                'currentLabel': empty,
                'block_north_mc': {'currentLabel': label},
                'block_east_mc': {'currentLabel': label},
                'block_south_mc': {'currentLabel': label},
                'block_west_mc': {'currentLabel': label}
        },
        'help_mc':  {'currentLabel': label}
    }
    



def get_repeat_news(previous_board, board, color, user):
    '''List all repeats on board.
    >>> previous_board = referee.before_ko_board
    >>> board = referee.start_ko_board
    >>> color = 'white'
    >>> repeats = referee.find_repeats(previous_board, board, color)
    >>> repeats
    [(0, 0)]
    >>> laurens = globe_class()
    >>> laurens.create()
    >>> repeat_news = get_repeat_news(previous_board, board, color, laurens)
    >>> repeat_news.get('_0_0_mc').get('block_north_mc')
    {'currentLabel': 'repeat'}

    Notify intersections no longer in repeat.
    >>> laurens.root._0_1_mc.block_north_mc.gotoAndPlay('repeat')
    >>> repeat_news = get_repeat_news(previous_board, board, color, laurens)
    >>> repeat_news.get('_0_1_mc').get('block_south_mc')
    {'currentLabel': 'none'}
    >>> repeat_news.get('_0_0_mc').get('block_south_mc')
    {'currentLabel': 'repeat'}
    '''
    repeats = referee.find_repeats(previous_board, board, color)
    intersection_names = [get_intersection_name(row, column)
        for row, column in repeats]
    news = {}
    for intersection_name in intersection_names:
        # XXX could probably refactor to just refer to intersection_mc_array
        # XXX then do not need user at all.
        if 'repeat' != user.root[intersection_name].block_north_mc.currentLabel:
            repeat_news = get_repeat_item(intersection_name, color)
            news = upgrade(news, repeat_news)
    # no longer repeating.
    currently = get_block_north_coordinates(user.intersection_mc_array, 
                'repeat')
    expired_repeats = [old_repeat for old_repeat in currently
                if old_repeat not in repeats]
    for row, column in expired_repeats:
        # XXX would be nice to revert
        intersection_news = get_intersection_block_news(
                row, column, 'none')
        news = upgrade(news, intersection_news)
    return news


def get_block_north_coordinates(intersection_mc_array, label):
    '''Coordinate of each intersection whose north block matches the label.
    >>> laurens = globe_class()
    >>> laurens.create()
    >>> get_block_north_coordinates(laurens.intersection_mc_array, 'repeat')
    []
    >>> all = get_block_north_coordinates(laurens.intersection_mc_array, 'none')
    >>> len(all)
    81
    '''    
    coordinates = []
    for r, row in enumerate(intersection_mc_array):
        for c, intersection_mc in enumerate(row):
            if label == intersection_mc.block_north_mc.currentLabel:
                coordinate = (r, c)
                coordinates.append(coordinate)
    return coordinates


danger_board_text = '''
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
danger_board = referee.text_to_array(danger_board_text)
danger_2_board = referee.text_to_array('''
O,,,,,,,,
X,,,,,,,,
,,,,,,,,,
,,,,,,,,,
,,,,,,,,,
,,,,,,,,,
,,,,,,,,,
,,,,,,,,,
,,,,,,,,,
''')


def get_block_news(intersection_mc_array, new_board):
    '''Sides in danger.
    >>> ezra = globe_class()
    >>> ezra.create(1)
    >>> from pprint import pprint
    >>> news = get_block_news(ezra.intersection_mc_array, danger_board)

    Does not show block at guarded (0, 7).
    >>> pprint(news)
    {'_0_6_mc': {'block_east_mc': {'currentLabel': 'white_warning'},
                 'block_north_mc': {'currentLabel': 'white_warning'}},
     '_0_8_mc': {'block_east_mc': {'currentLabel': 'white_danger'},
                 'block_north_mc': {'currentLabel': 'white_danger'},
                 'block_west_mc': {'currentLabel': 'white_danger'}},
     '_1_6_mc': {'block_east_mc': {'currentLabel': 'white_warning'},
                 'block_south_mc': {'currentLabel': 'white_warning'}},
     '_3_8_mc': {'block_east_mc': {'currentLabel': 'white_danger'},
                 'block_north_mc': {'currentLabel': 'white_danger'},
                 'block_west_mc': {'currentLabel': 'white_danger'}},
     '_4_8_mc': {'block_east_mc': {'currentLabel': 'white_danger'},
                 'block_west_mc': {'currentLabel': 'white_danger'}}}

    If unconditionally_alive, do not show any block there.
    >>> judith = ezra
    >>> judith.root._0_6_mc.unconditional_status_mc.gotoAndPlay('white_alive')
    >>> judith.root._0_7_mc.unconditional_status_mc.gotoAndPlay('black_alive')
    >>> judith.root._0_8_mc.unconditional_status_mc.gotoAndPlay('white_dead')
    >>> news = get_block_news(judith.intersection_mc_array, danger_board)
    >>> pprint(news)
    {'_0_8_mc': {'block_east_mc': {'currentLabel': 'white_danger'},
                 'block_north_mc': {'currentLabel': 'white_danger'},
                 'block_west_mc': {'currentLabel': 'white_danger'}},
     '_1_6_mc': {'block_east_mc': {'currentLabel': 'white_warning'},
                 'block_south_mc': {'currentLabel': 'white_warning'}},
     '_3_8_mc': {'block_east_mc': {'currentLabel': 'white_danger'},
                 'block_north_mc': {'currentLabel': 'white_danger'},
                 'block_west_mc': {'currentLabel': 'white_danger'}},
     '_4_8_mc': {'block_east_mc': {'currentLabel': 'white_danger'},
                 'block_west_mc': {'currentLabel': 'white_danger'}}}

    Filter out notices and warnings that are guarded.
    Do not filter danger.
    >>> laurens = globe_class()
    >>> laurens.create(1)
    >>> laurens.confirm_board_size('_3_3')
    >>> danger_board = [[',', ',', ','], [',', 'X', 'X'], ['$', 'O', ',']]
    >>> news = get_block_news(laurens.intersection_mc_array, danger_board)
    >>> news['_2_0_mc']['block_south_mc']['currentLabel']
    'black_danger'
    >>> guard_board = [[',', ',', ','], [',', 'X', 'X'], ['$', ',', ',']]
    >>> news = get_block_news(laurens.intersection_mc_array, guard_board)
    >>> news.get('_2_0_mc')
    '''
    block_news = {}
    # block:  filter blocks to 3 or fewer liberties
    blocks = referee.get_blocks(new_board)
    notices = referee.find_notice(new_board)
    warnings = referee.find_warning(new_board)
    dangers = referee.find_danger(new_board)
    remove_unconditionally_alive(intersection_mc_array, 
            blocks, notices, warnings, dangers)
    notices = referee.remove_guarded(new_board, notices, dangers)
    warnings = referee.remove_guarded(new_board, warnings, dangers)
    for r, row in enumerate(blocks):
        for b, block in enumerate(row):
            if (r, b) in dangers:
                block_names = {False: 'none', True: 'danger'}
                blocks[r][b] = [block_names[n] for n in blocks[r][b]]
            elif (r, b) in warnings:
                block_names = {False: 'none', True: 'warning'}
                blocks[r][b] = [block_names[n] for n in blocks[r][b]]
            elif (r, b) in notices:
                block_names = {False: 'none', True: 'block'}
                blocks[r][b] = [block_names[n] for n in blocks[r][b]]
            else:
                blocks[r][b] = ['none', 'none', 'none', 'none']
    for r, row in enumerate(intersection_mc_array):
        for c, intersection_mc in enumerate(row):
            sides = ['north', 'east', 'south', 'west']
            for s, side in enumerate(sides):
                side_name = 'block_%s_mc' % side
                before_block = intersection_mc[side_name].currentLabel
                now_block = blocks[r][c][s]
                if now_block != 'none':
                    color = referee.get_color(new_board[r][c])
                    now_block = color + '_' + now_block
                if now_block != before_block:
                    side_news = {intersection_mc.name:  
                                {side_name:  {'currentLabel':  now_block}}}
                    side_log = 'get_block_news: %s' % side_news
                    logging.debug(side_log)
                    block_news = upgrade(block_news, side_news)
    return block_news


def get_strike_news(intersection_mc_array, new_board, root, row, column, captures):
    '''Sides in danger.  Only show for groups at or beside striking stone.
    >>> emmet = globe_class()
    >>> emmet.create(1)
    >>> from pprint import pprint
    >>> no_captures = []
    >>> news = get_strike_news(emmet.intersection_mc_array, danger_board, emmet.root, 0, 7, no_captures)
    >>> pprint(news)
    {'_0_6_strike_mc': {'east_mc': {'currentLabel': 'white_warning'},
                        'north_mc': {'currentLabel': 'white_warning'}},
     '_0_8_strike_mc': {'east_mc': {'currentLabel': 'white_danger'},
                        'north_mc': {'currentLabel': 'white_danger'},
                        'west_mc': {'currentLabel': 'white_danger'}},
     '_1_6_strike_mc': {'east_mc': {'currentLabel': 'white_warning'},
                        'south_mc': {'currentLabel': 'white_warning'}}}

    If unconditionally_alive, do not show any strike there.
    >>> judith = emmet
    >>> judith.root._0_6_mc.unconditional_status_mc.gotoAndPlay('white_alive')
    >>> judith.root._1_6_mc.unconditional_status_mc.gotoAndPlay('white_alive')
    >>> judith.root._0_8_mc.unconditional_status_mc.gotoAndPlay('white_dead')
    >>> news = get_strike_news(judith.intersection_mc_array, danger_board, judith.root, 0, 7, no_captures)
    >>> pprint(news)
    {'_0_8_strike_mc': {'east_mc': {'currentLabel': 'white_danger'},
                        'north_mc': {'currentLabel': 'white_danger'},
                        'west_mc': {'currentLabel': 'white_danger'}}}

    And captures.
    >>> captures = [(2, 7)]
    >>> news = get_strike_news(judith.intersection_mc_array, danger_board, judith.root, 1, 7, captures)
    >>> pprint(news)
    {'_2_7_strike_mc': {'east_mc': {'currentLabel': 'white_capture'},
                        'north_mc': {'currentLabel': 'white_capture'},
                        'south_mc': {'currentLabel': 'white_capture'},
                        'west_mc': {'currentLabel': 'white_capture'}}}

    Reset unstrikes to none.
    >>> judith.root._1_6_strike_mc.west_mc.gotoAndPlay('white_danger')
    >>> news = get_strike_news(judith.intersection_mc_array, danger_board, judith.root, 1, 7, captures)
    >>> pprint(news)
    {'_1_6_strike_mc': {'west_mc': {'currentLabel': 'none'}},
     '_2_7_strike_mc': {'east_mc': {'currentLabel': 'white_capture'},
                        'north_mc': {'currentLabel': 'white_capture'},
                        'south_mc': {'currentLabel': 'white_capture'},
                        'west_mc': {'currentLabel': 'white_capture'}}}
    
    Self-captures as retaliate.
    >>> captures = [(2, 7)]
    >>> import copy
    >>> self_capture_board = copy.deepcopy(danger_board)
    >>> self_capture_board[2][7] = referee.white
    >>> referee.pb(self_capture_board)
    ,,,,,,OXO
    ,,,,,,OX,
    ,,,,,,XOX
    ,,,,,,XXO
    ,,,,,,,XO
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    ,,,,,,,,,
    >>> news = get_strike_news(judith.intersection_mc_array, self_capture_board, judith.root, 2, 7, captures)
    >>> pprint(news)
    {'_0_7_strike_mc': {'east_mc': {'currentLabel': 'black_danger'},
                        'north_mc': {'currentLabel': 'black_danger'},
                        'west_mc': {'currentLabel': 'black_danger'}},
     '_1_6_strike_mc': {'west_mc': {'currentLabel': 'none'}},
     '_1_7_strike_mc': {'south_mc': {'currentLabel': 'black_danger'},
                        'west_mc': {'currentLabel': 'black_danger'}},
     '_2_7_strike_mc': {'east_mc': {'currentLabel': 'white_capture_retaliate'},
                        'north_mc': {'currentLabel': 'white_capture_retaliate'},
                        'south_mc': {'currentLabel': 'white_capture_retaliate'},
                        'west_mc': {'currentLabel': 'white_capture_retaliate'}},
     '_2_8_strike_mc': {'east_mc': {'currentLabel': 'black_danger'},
                        'south_mc': {'currentLabel': 'black_danger'},
                        'west_mc': {'currentLabel': 'black_danger'}}}

    acceptance test:  laurens_guard_example
    '''
    strike_news = {}
    # strike:  filter strikes to 3 or fewer liberties
    strikes = referee.get_blocks(new_board)
    notices = referee.find_constrained_attackers(new_board, 3, row, column)
    warnings = referee.find_constrained_attackers(new_board, 2, row, column)
    dangers = referee.find_constrained_attackers(new_board, 1, row, column)
    liberty_labels = {1: 'danger_retaliate', 2: 'warning_retaliate', 3: 'notice_retaliate'}
    at_risk_group = referee.find_region(new_board, row, column)
    liberties = referee.find_liberty_of_set(new_board, at_risk_group)
    liberty_count = len(liberties)
    if 1 <= liberty_count and liberty_count <= 3:
        liberty_label = liberty_labels[liberty_count]
    else:
        liberty_label = None
        at_risk_group = []
    remove_unconditionally_alive(intersection_mc_array, 
            strikes, notices, warnings, dangers, at_risk_group)
    notices = referee.remove_guarded(new_board, notices, dangers)
    warnings = referee.remove_guarded(new_board, warnings, dangers)
    if at_risk_group and 2 <= liberty_count:
        at_risk_group = referee.remove_guarded(new_board, at_risk_group, dangers)
    for r, strike_row in enumerate(strikes):
        for b, strike in enumerate(strike_row):
            if (r, b) in dangers:
                strike_names = {False: 'none', True: 'danger'}
                strikes[r][b] = [strike_names[n] for n in strikes[r][b]]
            elif (r, b) in warnings:
                strike_names = {False: 'none', True: 'warning'}
                strikes[r][b] = [strike_names[n] for n in strikes[r][b]]
            elif (r, b) in notices:
                strike_names = {False: 'none', True: 'notice'}
                strikes[r][b] = [strike_names[n] for n in strikes[r][b]]
            elif (r, b) in at_risk_group:
                strike_names = {False: 'none', True: liberty_label}
                strikes[r][b] = [strike_names[n] for n in strikes[r][b]]
            else:
                strikes[r][b] = ['none', 'none', 'none', 'none']
    # insert captures of exterior sides only
    mark = new_board[row][column]
    color = referee.get_color(mark) 
    if (row, column) in captures:
        capture_label = '%s_capture_retaliate' % color
    else:
        opposite_color = referee.opposite(color)
        capture_label = '%s_capture' % opposite_color
    capture_sides = referee.find_exterior_side_of_region(new_board, captures, capture_label)
    for r in range(len(new_board)):
        for c in range(len(new_board[r])):
            sides = ['north', 'east', 'south', 'west']
            intersection_name = '_%i_%i_strike_mc' % (r, c)
            strike_mc = root[intersection_name]
            for s, side in enumerate(sides):
                side_name = '%s_mc' % side
                before_strike = strike_mc[side_name].currentLabel
                now_strike = strikes[r][c][s]
                if now_strike != 'none':
                    color = referee.get_color(new_board[r][c])
                    now_strike = color + '_' + now_strike
                elif now_strike == 'none' and (r, c) in capture_sides:
                    capture_side = capture_sides[(r, c)][s]
                    now_strike = capture_side
                if now_strike != before_strike:
                    side_news = {strike_mc.name:  
                                {side_name:  {'currentLabel':  now_strike}}}
                    side_log = 'get_strike_news: %s' % side_news
                    logging.debug(side_log)
                    strike_news = upgrade(strike_news, side_news)
    return strike_news


def remove_unconditionally_alive(intersection_mc_array, *coordinate_lists):
    '''filter out unconditionally alive'''
    unconditionally_alives = []
    for r, row in enumerate(intersection_mc_array):
        for c, intersection_mc in enumerate(row):
            label = intersection_mc.unconditional_status_mc.currentLabel
            if 'black_alive' == label or 'white_alive' == label:
                alive = (r, c)
                unconditionally_alives.append(alive)
                for coordinate_list in coordinate_lists:
                    if alive in coordinate_list:
                        coordinate_list.remove(alive)


def set_block_news(coordinates, label):
    '''set all blocks to label.
    must be performed after get_block_news
    For example, if dragon may be critical with more than 3 liberties.
    >>> news = set_block_news([(7, 0), (7, 1), (7, 2), (7, 3), (8, 3)], 'danger')
    >>> news.get('_8_3_mc').get('block_north_mc')
    {'currentLabel': 'danger'}
    >>> news.get('_7_2_mc').get('block_south_mc')
    {'currentLabel': 'danger'}
    '''
    block_news = {}
    for row, column in coordinates:
        coordinate_news = get_intersection_block_news(row, column, label)
        block_news = upgrade(block_news, coordinate_news)
    return block_news

def upgrade_side_news(side_format, news, intersection_mc, sides):
    '''Stuff changed sides of a single intersection.
    >>> code_unit.doctest_unit(get_liberty_news, verbose=False, log=False)
    '''
    directions = ['north', 'east', 'south', 'west']
    for d, direction in enumerate(directions):
        side_name = side_format % direction
        logging.debug(side_name)
        before_liberty = intersection_mc[side_name].currentLabel
        now_liberty = sides[d]
        if now_liberty != before_liberty:
            side_news = {intersection_mc.name:  
                        {side_name:  {'currentLabel':  now_liberty}}}
            side_log = 'upgrade_side_news: %s' % side_news
            logging.debug(side_log)
            news = upgrade(news, side_news)

def get_liberty_news(intersection_mc_array, new_board):
    '''Liberties at warnings.
    >>> ezra = globe_class()
    >>> ezra.create(1)
    >>> from pprint import pprint
    >>> news = get_liberty_news(ezra.intersection_mc_array, danger_board)
    >>> pprint(news)
    {'_0_5_mc': {'liberty_east_mc': {'currentLabel': 'white_warning'}},
     '_1_5_mc': {'liberty_east_mc': {'currentLabel': 'white_warning'}},
     '_1_8_mc': {'liberty_north_mc': {'currentLabel': 'white_danger'},
                 'liberty_south_mc': {'currentLabel': 'black_warning'},
                 'liberty_west_mc': {'currentLabel': 'black_warning'}},
     '_2_7_mc': {'liberty_east_mc': {'currentLabel': 'black_warning'},
                 'liberty_north_mc': {'currentLabel': 'black_warning'}},
     '_5_8_mc': {'liberty_north_mc': {'currentLabel': 'white_danger'}}}

    If unconditionally_alive, do not show any liberty there.
    >>> judith = ezra
    >>> judith.root._0_6_mc.unconditional_status_mc.gotoAndPlay('white_alive')
    >>> judith.root._1_6_mc.unconditional_status_mc.gotoAndPlay('white_alive')
    >>> judith.root._0_7_mc.unconditional_status_mc.gotoAndPlay('black_alive')
    >>> judith.root._1_7_mc.unconditional_status_mc.gotoAndPlay('black_alive')
    >>> judith.root._0_8_mc.unconditional_status_mc.gotoAndPlay('white_dead')
    >>> news = get_liberty_news(judith.intersection_mc_array, danger_board)
    >>> pprint(news)
    {'_1_8_mc': {'liberty_north_mc': {'currentLabel': 'white_danger'},
                 'liberty_south_mc': {'currentLabel': 'black_warning'}},
     '_2_7_mc': {'liberty_east_mc': {'currentLabel': 'black_warning'}},
     '_5_8_mc': {'liberty_north_mc': {'currentLabel': 'white_danger'}}}

    If liberty warning goes away, notify.
    >>> olds = imitate_news(judith.root, news)
    >>> danger_board[2][7] = referee.black
    >>> news = get_liberty_news(judith.intersection_mc_array, danger_board)
    >>> pprint(news)
    {'_1_8_mc': {'liberty_south_mc': {'currentLabel': 'none'}},
     '_2_7_mc': {'liberty_east_mc': {'currentLabel': 'none'}}}

    If notice and danger from same coordinate, both appear.
    >>> michael = ezra
    >>> michael.create(1)
    >>> news = get_liberty_news(michael.intersection_mc_array, danger_2_board)
    >>> pprint(news)
    {'_0_1_mc': {'liberty_west_mc': {'currentLabel': 'white_danger'}},
     '_1_1_mc': {'liberty_west_mc': {'currentLabel': 'black_warning'}},
     '_2_0_mc': {'liberty_north_mc': {'currentLabel': 'black_warning'}}}
    >>> olds = imitate_news(michael.root, news)
    >>> danger_2_board[0][2] = referee.black
    >>> news = get_liberty_news(michael.intersection_mc_array, danger_2_board)
    >>> pprint(news)
    {'_0_1_mc': {'liberty_east_mc': {'currentLabel': 'black_notice'}},
     '_0_3_mc': {'liberty_west_mc': {'currentLabel': 'black_notice'}},
     '_1_2_mc': {'liberty_north_mc': {'currentLabel': 'black_notice'}}}
    '''
    notices = referee.find_notice(new_board)
    warnings = referee.find_warning(new_board)
    dangers = referee.find_danger(new_board)
    remove_unconditionally_alive(intersection_mc_array, 
            notices, warnings, dangers)
    notice_sides = referee.find_liberty_side_of_set(new_board, notices, '_notice')
    warning_sides = referee.find_liberty_side_of_set(new_board, warnings, '_warning')
    def merge(notice_sides, warning_sides):
        for warning, sides in warning_sides.items():
            if warning in notice_sides:
                for s, side in enumerate(notice_sides[warning]):
                    if 'none' == side:
                        notice_sides[warning][s] = warning_sides[warning][s]
            else: 
                notice_sides[warning] = warning_sides[warning]
    merge(notice_sides, warning_sides)
    danger_sides = referee.find_liberty_side_of_set(new_board, dangers, '_danger')
    merge(notice_sides, danger_sides)
    
    liberty_news = {}
    for r, row in enumerate(intersection_mc_array):
        for c, intersection_mc in enumerate(row):
            warned = False
            notice = notice_sides.get( (r, c) )
            if notice:
                upgrade_side_news('liberty_%s_mc', liberty_news, 
                        intersection_mc, notice)
                warned = True
            #warning = warning_sides.get( (r, c) )
            #if warning:
            #    upgrade_intersection_liberty_news(liberty_news, r, c, warning)
            #    warned = True
            #danger = danger_sides.get( (r, c) )
            #if danger:
            #    upgrade_intersection_liberty_news(liberty_news, r, c, danger)
            #    warned = True
            if not warned:
                safe = ['none', 'none', 'none', 'none']
                #- upgrade_intersection_liberty_news(liberty_news, r, c, safe)
                upgrade_side_news('liberty_%s_mc', liberty_news, 
                        intersection_mc, safe)
    #for r_c, sides in notice_sides.items():
    #    r, c = r_c
    #    upgrade_intersection_liberty_news(liberty_news, r, c, sides)
    #for r_c, sides in warning_sides.items():
    #    r, c = r_c
    #    upgrade_intersection_liberty_news(liberty_news, r, c, sides)
    #for r_c, sides in danger_sides.items():
    #    r, c = r_c
    #    upgrade_intersection_liberty_news(liberty_news, r, c, sides)
    return liberty_news


def set_dragon_status_news(coordinates, label):
    '''set all dragon_statuss to label.
    must be performed after get_dragon_status_news
    dragon may be critical with more than 3 liberties.
    >>> news = set_dragon_status_news([(7, 0), (7, 1), (7, 2), (7, 3), (8, 3)], 'critical')
    >>> news.get('_8_3_mc').get('dragon_status_mc')
    {'currentLabel': 'critical'}
    >>> news.get('_7_2_mc').get('dragon_status_mc')
    {'currentLabel': 'critical'}
    '''
    dragon_status_news = {}
    for row, column in coordinates:
        coordinate_news = get_intersection_news(row, column, 'dragon_status_mc', label)
        dragon_status_news = upgrade(dragon_status_news, coordinate_news)
    return dragon_status_news



def get_coordinates(intersection_mc_array, child_mc_name, label):
    '''Coordinate of each intersection whose north block matches the label.
    >>> laurens = globe_class()
    >>> laurens.create()
    >>> get_coordinates(laurens.intersection_mc_array, 'suicide_mc', 'white')
    []
    >>> all = get_coordinates(laurens.intersection_mc_array, 'suicide_mc', 'none')
    >>> len(all)
    81
    '''    
    coordinates = []
    for r, row in enumerate(intersection_mc_array):
        for c, intersection_mc in enumerate(row):
            if label == intersection_mc[child_mc_name].currentLabel:
                coordinate = (r, c)
                coordinates.append(coordinate)
    return coordinates


def set_coordinate_news(coordinates, owner, label):
    '''set all owner in intersection to label.
    >>> set_coordinate_news([], 'dragon_status_mc', 'critical')
    {}
    >>> news = set_coordinate_news([(7, 0), (7, 1), (7, 2), (7, 3), (8, 3)], 'dragon_status_mc', 'critical')
    >>> news.get('_8_3_mc').get('dragon_status_mc')
    {'currentLabel': 'critical'}
    >>> news.get('_7_2_mc').get('dragon_status_mc')
    {'currentLabel': 'critical'}
    >>> news = set_coordinate_news([(8, 1)], 'vital_point_mc', 'defense_point')
    >>> news.get('_8_1_mc').get('vital_point_mc')
    {'currentLabel': 'defense_point'}
    '''
    news = {}
    for row, column in coordinates:
        coordinate_news = get_intersection_news(row, column, owner, label)
        news = upgrade(news, coordinate_news)
    return news



def get_suicide_news(board, user):
    '''Show added or removed suicide.  Overwrites block_*_mc.
    >>> laurens = globe_class()
    >>> laurens.create()
    >>> news = get_suicide_news(referee.suicide_board, laurens)
    >>> news.get('_0_8_mc').get('suicide_mc')
    {'currentLabel': 'black'}
    >>> news.get('_0_8_mc').get('block_north_mc')
    >>> news.get('_0_8_mc').get('block_east_mc')
    >>> news.get('_0_8_mc').get('block_south_mc')
    >>> news.get('_0_8_mc').get('block_west_mc')
    >>> news.get('_0_0_mc').get('suicide_mc')
    {'currentLabel': 'white'}
    >>> news.get('_0_0_mc').get('block_north_mc')
    >>> news.get('_0_0_mc').get('block_east_mc')
    >>> news.get('_0_0_mc').get('block_south_mc')
    >>> news.get('_0_0_mc').get('block_west_mc')

#    refer to previous news to not spam old news.
#    >>> olds = imitate_news(laurens.root, news)
#    >>> laurens.root['_0_8_mc'].block_north_mc.currentLabel
    'suicide'
#    >>> laurens.root['_0_0_mc'].block_north_mc.currentLabel
    'suicide_white'
#    >>> news2 = get_suicide_news(referee.suicide_board, laurens)
#    >>> news2.get('_0_8_mc')
#    >>> news2.get('_0_0_mc')
    '''
    news = {}
    for color in 'black', 'white':
        suicides = referee.predict_suicides(board, color)
        #if 'black' == color:
        #    label = 'black'
        #elif 'white' == color:
        #    label = 'black'
        ## XXX could be done without user, just intersection_mc_array?
        currently = get_coordinates(user.intersection_mc_array, 
                'suicide_mc', color)
        for row, column in suicides:
            intersection_news = get_intersection_news(
                    row, column, 'suicide_mc', color)
            news = upgrade(news, intersection_news)
        rescued = [suicide for suicide in currently
                if suicide not in suicides]
        for row, column in rescued:
            # XXX would be nice to revert
            intersection_news = get_intersection_news(
                    row, column, 'suicide_mc', 'none')
            news = upgrade(news, intersection_news)
    return news


import copy
def get_empty_block_news(intersection_mc_array, new_board, color):
    '''
    before you move, if you build here, how many liberties will you have?
    imagine play.  update new_board.  then...
        if facing empty land, green.
            _0_0_mc.empty_block_north_mc:liberty
        if facing your castle, green with road.
            _0_0_mc.empty_block_north_mc:you
        if facing mountain:  beige.
            _0_0_mc.empty_block_north_mc:block
        if facing enemy castle, beige.  
            _0_0_mc.empty_block_north_mc:block
    >>> yuji = globe_class()
    >>> yuji.create(1)
    >>> from pprint import pprint

    YUJI CAN SEE EMPTY BLOCKS.
    >>> ## property_diff(black, black.root.option_mc.empty_block_mc, 'currentLabel', 'show')
    >>> new_board_text = flash_to_text(yuji.intersection_mc_array)
    >>> new_board = text_to_array(new_board_text)
    >>> news = get_empty_block_news(yuji.intersection_mc_array, new_board, 'black')
    >>> if not news.get('_0_0_mc'):
    ...     news
    >>> news.get('_0_0_mc').get('empty_block_north_mc')
    {'currentLabel': 'block'}
    >>> news.get('_0_0_mc').get('empty_block_east_mc')
    {'currentLabel': 'liberty'}

    new_board supersedes intersection_mc_array
    >>> new_board_text = flash_to_text(yuji.intersection_mc_array)
    >>> new_board = text_to_array(new_board_text)
    >>> new_board[1][1] = referee.black
    >>> news = get_empty_block_news(yuji.intersection_mc_array, new_board, 'black')
    >>> if not news.get('_0_1_mc'):
    ...     news
    >>> if not news.get('_0_1_mc').get('empty_block_south_mc') == {'currentLabel': 'you'}:
    ...     pprint(news.get('0_1_mc'))
    '''
    news = {}
    for r, row in enumerate(intersection_mc_array):
        for c, intersection_mc in enumerate(row):
            if_play_board = referee.play_and_update(new_board, color, r, c)
            empty_blocks = referee.get_empty_blocks(if_play_board)
            sides = empty_blocks[r][c]
            upgrade_side_news('empty_block_%s_mc', news, 
                    intersection_mc, sides)
    return news

def get_score_news(old_score, score):
    label = '_%i' % score
    score_str = '%i' % score
    change = score - old_score
    if 5 <= change:
        change_str = '+%i' % change
        change_label = 'positive'
    elif -5 <= change:
        change_str = '%i' % change
        change_label = 'neutral'
    else:
        change_str = '%i' % change
        change_label = 'negative'
    news = {
        'score_mc': {
            'bar_mc': {
                'currentLabel': label, 
                'territory_txt': {'text': score_str},
                'marker_mc': {
                    'currentLabel': change_label, 
                    'change_txt': {'text': change_str} 
                }
            }
        }
    }
    return news


def get_profit_news(intersection_mc_array, row, column, profit):
    '''See profit on new castle.
    preview 1,1
    Moonhyoung sees no double roof at 1,1.
    >>> from super_user import user_class
    >>> black = user_class()
    >>> black.create(1)
    >>> moonhyoung = black
    >>> black.root._1_1_mc.black_shape_mc.defend_mc.profit_mc.currentLabel
    'none'
    >>> news = get_profit_news(black.intersection_mc_array, 1, 1, 5)
    >>> news.get('_1_1_mc')

    Moonhyoung sees no double roof at 2,2.
    >>> news.get('_2_2_mc')

    Moonhyoung sees profit of +24
    >>> news = get_profit_news(black.intersection_mc_array, 2, 2, 24)

    Moonhyoung sees double roof at 2,2.
    >>> news['_2_2_mc']['black_shape_mc']['defend_mc']['profit_mc']['currentLabel']
    'show'

    play. Moonhyoung sees double roof at 2,2.
    >>> black.root._2_2_mc.black_shape_mc.defend_mc.profit_mc.gotoAndPlay('show')
    >>> news = get_profit_news(black.intersection_mc_array, 2, 2, 24)
    >>> news.get('_2_2_mc')

    White plays.
    >>> black.root._2_1_mc.gotoAndPlay('white')

    Fifteen is not enough for double roof.  +20 is minimum.
    >>> news = get_profit_news(black.intersection_mc_array, 1, 2, 15)
    >>> news.get('_1_2_mc')

    Moonhyoung still sees double roof on previously profitable castle.
    >>> news.get('_2_2_mc')
    >>> black.root._2_2_mc.black_shape_mc.defend_mc.profit_mc.currentLabel
    'show'

    Moonhyoung turns the corner and sees double roof.
    >>> news = get_profit_news(black.intersection_mc_array, 1, 1, 33)
    >>> news.get('_1_2_mc')
    >>> news['_1_1_mc']['black_shape_mc']['defend_mc']['profit_mc']['currentLabel']
    'show'
    >>> news.get('_2_2_mc')
    
    Preview elsewhere.  Moonhyoung does not see previous double roof.
    Beware:  you must revert preview.
    >>> black.root._1_1_mc.black_shape_mc.defend_mc.profit_mc.gotoAndPlay('show')
    >>> black.root._1_1_mc.black_shape_mc.defend_mc.profit_mc.gotoAndPlay('none')
    >>> news = get_profit_news(black.intersection_mc_array, 3, 1, 33)
    >>> news.get('_1_1_mc')
    >>> news['_3_1_mc']['black_shape_mc']['defend_mc']['profit_mc']['currentLabel']
    'show'
    >>> news.get('_2_2_mc')
    '''
    news = {}
    if 20 <= profit:
        new_label = 'show'
        intersection_mc = intersection_mc_array[row][column]
        profit_mc = intersection_mc.black_shape_mc.defend_mc.profit_mc
        old_label = profit_mc.currentLabel
        if new_label != old_label:
            intersection_name = get_intersection_name(row, column)
            profit_news = {
                intersection_name: {
                    'black_shape_mc': {
                        'defend_mc': {
                            'profit_mc': {
                                'currentLabel': new_label
                            }
                        }
                    }
                }
            }
            news = upgrade(news, profit_news)
    return news

def get_territory_news(intersection_mc_array, new_labels):
    '''How has each intersection on the board changed ownership?
    >>> user = globe_class()
    >>> user.create()
    >>> import go_text_protocol
    >>> territory_values = go_text_protocol.get_territory_values(go_text_protocol.wallis_territory_text)
    >>> territory_labels = go_text_protocol.get_territory_labels(territory_values)
    >>> news = get_territory_news(user.intersection_mc_array, territory_labels)
    >>> news.get('_0_2_mc')
    {'territory_mc': {'currentLabel': 'black'}}

    Only changes are included.
    >>> len(news)
    30
    '''
    territory_now = {}
    simulcast = zip(enumerate(intersection_mc_array), new_labels)
    for (r, old_row), new_row in simulcast:
        simultaneous = zip(enumerate(old_row), new_row)
        for (c, intersection_mc), new_label in simultaneous:
            old_label = intersection_mc.territory_mc.currentLabel
            if old_label != new_label:
                name = get_intersection_name(r, c)
                territory_now[name] = {'territory_mc': {
                    'currentLabel': new_label}}
    return territory_now
    


def get_last_move_news(intersection_mc_array, color, row, column): 
    '''Snap and play last move.  
    >>> laurens = globe_class()
    >>> laurens.create()
    >>> news = get_last_move_news(laurens.intersection_mc_array, 'black', 0, 1)
    >>> news.get('_0_0_mc')
    >>> news.get('_0_1_mc').get('last_move_mc')
    {'currentLabel': 'black'}
    >>> olds = imitate_news(laurens.root, news)
    >>> news = get_last_move_news(laurens.intersection_mc_array, 'white', 0, 2)
    >>> news.get('_0_1_mc')
    >>> news.get('_0_2_mc').get('last_move_mc')
    {'currentLabel': 'white'}

    Clear previous.
    >>> olds = imitate_news(laurens.root, news)
    >>> news = get_last_move_news(laurens.intersection_mc_array, 'black', 0, 3)
    >>> news.get('_0_1_mc').get('last_move_mc')
    {'currentLabel': 'none'}
    >>> news.get('_0_2_mc')
    >>> news.get('_0_3_mc').get('last_move_mc')
    {'currentLabel': 'black'}
    '''
    clear_news = child_label_from_to(intersection_mc_array, 'last_move_mc', 
            color, 'none')
    intersection_name = get_intersection_name(row, column)
    last_move_news = {
        intersection_name: {
            'last_move_mc': {
                'currentLabel': color
            }
        }
    }
    last_move_news = upgrade(clear_news, last_move_news)
    return last_move_news


def get_first_intersection(intersections, message, label = None):
    '''
    >>> root = get_example_stage()
    >>> intersections = get_intersection_array(root)
    >>> _mc = get_first_intersection(intersections, {'_0_0_mc': {}})
    >>> isMovieClip(_mc)
    True
    >>> _mc = get_first_intersection(intersections, {'_2_9_mc': {}})
    >>> first_mc = get_first_intersection(intersections, {'_1_1_mc': {}, '_1_0_mc': {}})
    >>> if not first_mc.name == '_1_0_mc':
    ...     first_mc.name, intersections[1][0].name

    Optionally require label
    >>> play_news = {'_1_1_mc': {'currentLabel': 'black'}, '_1_0_mc': {'currentLabel': 'empty_black'}}
    >>> first_mc = get_first_intersection(intersections, play_news,
    ...     label = 'black')
    >>> if not first_mc.name == '_1_1_mc':
    ...     first_mc.name, intersections[1][1].name
    '''
    for row in intersections:
        for intersection in row:
            for name, here in message.items():
                if intersection.name == name:
                    if not label or label == here.get('currentLabel'):
                        return intersection

def get_intersection_names(intersection_mc_array):
    '''Names in row order.
    >>> moonhyoung = user_class()
    >>> moonhyoung.create()
    >>> names = get_intersection_names(moonhyoung.intersection_mc_array)
    >>> names[0]
    '_0_0_mc'
    >>> names[1]
    '_0_1_mc'
    >>> names[9]
    '_1_0_mc'
    '''
    return [intersection_mc.name 
            for row in intersection_mc_array 
                for intersection_mc in row]



def update_progress_news(intersection_mc_array, play_news):
    '''server update progress. if no build, insert nothing.
    >>> rene = globe_class()
    >>> rene.create(1.0/8)
    >>> intersections = rene.intersection_mc_array
    >>> from pprint import pprint
    >>> pprint({})
    {}
    >>> play_news = {'_1_1_mc': {}, '_1_0_mc': {}}
    >>> pprint(update_progress_news(intersections, play_news))
    {'_1_0_mc': {}, '_1_1_mc': {}}
    
    rene moves black.  rene sees progress start.
    rene moves white.  rene sees progress start.
    >>> play_news = {'_1_1_mc': {'currentLabel': 'black'}, '_1_0_mc': {'currentLabel': 'empty_black'}}
    >>> pprint(update_progress_news(intersections, play_news))
    {'_1_0_mc': {'currentLabel': 'empty_black'},
     '_1_1_mc': {'currentLabel': 'black',
                 'progress_mc': {'currentLabel': 'black_start'}}}

    when black turn, complete progress at any black stone in progress
    when white turn, complete progress at any white stone in progress
    sequence complete progress after turn
    >>> intersections[0][0].progress_mc.gotoAndPlay('black_start')
    >>> intersections[0][0].progress_mc.currentLabel
    'black_start'
    >>> intersections[0][0].progress_mc.gotoAndPlay('black_start')
    >>> pprint(update_progress_news(intersections, {}))
    {}
    >>> play_news = {'turn_mc': {'currentLabel': 'black'}}
    >>> intersections[0][0].progress_mc.currentLabel
    'black_start'
    >>> intersections[0][0].progress_mc.gotoAndPlay('black_start')
    >>> intersections[0][0].progress_mc.currentLabel
    'black_start'
    >>> pprint(update_progress_news(intersections, play_news))
    {'_0_0_mc': {'progress_mc': {'currentLabel': 'black_complete'}},
     'turn_mc': {'currentLabel': 'black'}}

    Making a move of same color is converted to complete.
    >>> intersections[0][0].progress_mc.gotoAndPlay('none')
    >>> intersections[0][0].progress_mc.currentLabel
    'none'
    >>> play_news = {'_0_0_mc': {'currentLabel': 'black'}, 'turn_mc': {'currentLabel': 'white'}}
    >>> pprint(update_progress_news(intersections, play_news))
    {'_0_0_mc': {'currentLabel': 'black',
                 'progress_mc': {'currentLabel': 'black_start'}},
     'turn_mc': {'currentLabel': 'white'}}
    >>> play_news = {'_0_0_mc': {'currentLabel': 'black'}, 'turn_mc': {'currentLabel': 'black'}}
    >>> pprint(update_progress_news(intersections, play_news))
    {'_0_0_mc': {'currentLabel': 'black',
                 'progress_mc': {'currentLabel': 'black_complete'}},
     'turn_mc': {'currentLabel': 'black'}}
    '''
    for color in ['black', 'white']:
        start = '%s_start' % color
        complete = '%s_complete' % color
        intersection_mc = get_first_intersection(intersection_mc_array, 
                play_news, label = color)
        if intersection_mc:
            play_news[intersection_mc.name]['progress_mc'] \
                    = {'currentLabel': start}
        if 'turn_mc' in play_news:
            if color == play_news['turn_mc'].get('currentLabel'):
                complete_news = child_label_from_to(intersection_mc_array, 
                    'progress_mc', start, complete)
                play_news = upgrade(play_news, complete_news)
                intersection_names = get_intersection_names(intersection_mc_array)
                for intersection_name in intersection_names:
                    intersection_news = play_news.get(intersection_name)
                    if intersection_news:
                        label = intersection_news.get('currentLabel')
                        if color == label:
                            complete_news = {intersection_name: {
                                'progress_mc': {'currentLabel': complete}}}
                            play_news = upgrade(play_news, complete_news)

    return play_news

# End intersection_mc board algorithms

# Test
from user_as import globe_class, imitate_news

import code_unit
snippet = '''
import intersection_mc; intersection_mc = reload(intersection_mc); from intersection_mc import *
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
    

