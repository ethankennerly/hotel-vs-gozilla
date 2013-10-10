#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
Relay from GnuGo to Flash Client through Smart Go Format
gtp:  Go Text Protocol
amf:  ActionScript Messaging Format
sgf:  Smart Go Format (Smart Game Format subset for this Go)
'''
__author__ = 'Ethan Kennerly'


from deck import draw
import copy
import sgflib
import text
sgf_pass = 'tt'
sgf_passes = [sgf_pass, '']
sgf_resign = 'Resign'
sgf_resign2 = 'Resign'
sgf_comment = 'C'
sgf_result = 'RE'
sgf_game = 'GM'
sgf_size = 'SZ'
sgf_sizes = ['3', '5', '7', '9']
sgf_go_game = '1'
sgf_cross = 'MA'
sgf_circle = 'CR'
sgf_triangle = 'TR'
sgf_square = 'SQ'
sgf_black = 'B'
sgf_white = 'W'
sgf_add_black = 'AB'
sgf_add_white = 'AW'
sgf_play = 'PL'

sgf_copy_list = ['BR', 'WR']
sgf_not_supported = ['KM', 'PW', 'ST', 'FF', 'VW', 'CA', 'AP', 'DT',
        'PB', 'RO', 'EV', 'GC', 'PC']

sgf_hide = sgf_cross
sgf_unhide = sgf_circle

sgf_color_node_dictionary = {
    sgf_play: 'play',
}

sgf_pass_dictionary = {
    sgf_pass:   'pass',
    'R':    'resign',
    'Resign':   'resign',
    #'1':    'go',
        }

sgf_move_dictionary = {
    sgf_black:    'black',
    sgf_white:    'white',
}

sgf_add_stone_dictionary = {
    sgf_add_black:    'add_black',
    sgf_add_white:    'add_white',
    sgf_square:       'square',
}

add_colors = {'add_black': 'black', 'add_white': 'white'}
add_stones = {'add_black': sgf_add_black, 'add_white': sgf_add_white}

sgf_hide_dictionary = {
    sgf_hide:    'hide',
    sgf_unhide:    'unhide',
}

sgf_text_dictionary = {
    'ON': 'opening_note',
}
sgf_int_dictionary = {
    'HA': 'handicap',
}

def set_comment(node, comment_text):
    comment = node.makeProperty(sgf_comment, [comment_text])
    node.addProperty(comment)
    return node

def annotate(node, id, row, column):
    coordinate = get_coordinates(row, column)
    property = node.makeProperty(id, [coordinate])
    node.addProperty(property)
    return node

def get_coordinates(row, column):
    #                  012345678
    sgf_coordinates = 'abcdefghijklmnopqrstuvwxyz'
    sgf_position = sgf_coordinates[column] \
            + sgf_coordinates[row]
    return sgf_position

def get_position(sgf_coordinate):
    '''
    >>> get_position('ba')
    (0, 1)
    '''
    #                  012345678
    sgf_coordinates = 'abcdefghijklmnopqrstuvwxyz'
    row = sgf_coordinates.index(sgf_coordinate[1])
    column = sgf_coordinates.index(sgf_coordinate[0])
    return row, column

def get_sgf_color(color):
    sgf_color = color.capitalize()[0]
    return sgf_color

def get_node(tree, color, row, column):
    '''
    >>> tree = sgflib.GameTree(nodelist=None, variations=None)
    >>> node = get_node(tree, 'white', 0, 1)
    >>> print node
    ;W[ba]
    '''
    sgf_color = get_sgf_color(color)
    sgf_position = get_coordinates(row, column)
    node = tree.makeNode([sgflib.Property(
        sgf_color, [sgf_position])])
    return node

def add_move(node, color, row, column):
    sgf_color = get_sgf_color(color)
    sgf_position = get_coordinates(row, column)
    node.addProperty( sgflib.Property(
        sgf_color, [sgf_position] ) )
    return node

def add_position(node, sgf_tag, row, column):
    '''Add a positional property to a node.
    >>> tree = sgflib.GameTree(nodelist=None, variations=None)
    >>> node = tree.makeNode([])
    >>> node = add_position(node, sgf_add_black, 1, 2)
    >>> print node
    ;AB[cb]
    >>> node = append_position(node, sgf_add_black, 2, 2)
    >>> print node
    ;AB[cb][cc]

    Cannot add if property already exists.
    >>> node = add_position(node, sgf_add_black, 2, 3)
    Traceback (most recent call last):
      ...
    DuplicatePropertyError
    >>> print node
    ;AB[cb][cc]
   
    So add once, then append.
    >>> history = [{'size': 5, 'add_black': [(1, 2), (2, 2), (2, 3)]}]
    >>> print get_sgf_tree(history)
    (;GM[1]SZ[5]AB[cb][cc][dc])
    '''
    sgf_position = get_coordinates(row, column)
    node.addProperty( sgflib.Property(
        sgf_tag, [sgf_position] ) )
    return node

def append_move(node, color, row, column):
    sgf_color = get_sgf_color(color)
    sgf_position = get_coordinates(row, column)
    node[sgf_color].data.append(sgf_position)
    return node

def append_position(node, sgf_tag, row, column):
    sgf_position = get_coordinates(row, column)
    node[sgf_tag].data.append(sgf_position)
    return node

def get_custom_node(tree, id, row, column):
    '''
    >>> tree = sgflib.GameTree(nodelist=None, variations=None)
    >>> node = get_custom_node(tree, sgf_cross, 0, 1)
    >>> print node
    ;MA[ba]
    '''
    sgf_position = get_coordinates(row, column)
    node = tree.makeNode([sgflib.Property(
        id, [sgf_position])])
    return node


def get_property(id, row, column):
    sgf_position = get_coordinates(row, column)
    property = sgflib.Property(id, [sgf_position])
    return property


def sgf_comment_example():
    r'''You can add a comment to a node and read it.
    >>> tree = sgflib.GameTree(nodelist=None, variations=None)
    >>> node = tree.makeNode([sgflib.Property('W', ['ba'])])
    >>> node = get_node(tree, 'white', 0, 1)
    >>> print node
    ;W[ba]
    >>> comment = node.makeProperty('C', [str(node)])
    >>> node.addProperty(comment)

    I guess each character is escaped to avoid node confusion?
    >>> print node
    ;W[ba]C[;W[ba\]]

    For a sane view:
    >>> ''.join(node.data['C'].data)
    ';W[ba]'
    '''


intersection_news_dictionary = {
    'decoration_mc': {
        'black_attack': [sgf_cross],
        'black_defend': [sgf_circle],
        'white_attack': [sgf_triangle],
        'white_defend': [sgf_square],
    },
    'formation_mc': {
        'black_attack': [sgf_cross],
        'black_attack_defend': [sgf_cross, sgf_circle],
        'black_defend': [sgf_circle],
        'white_attack': [sgf_triangle],
        'white_attack_defend': [sgf_triangle, sgf_square],
        'white_defend': [sgf_square],
    }
}

import re
def news_to_property(node, news):
    r'''Convert Flash remote control news into SGF property.
    >>> news = {'_0_2_mc': {'decoration_mc': {'currentLabel': 'black_attack'}}}
    >>> tree = sgflib.GameTree(nodelist=None, variations=None)
    >>> node = tree.makeNode([])
    >>> print node
    ;
    >>> node = news_to_property(node, news)
    >>> print node
    ;MA[ca]

    Multiple marks.
    >>> black_attack_decoration = {'decoration_mc': {'currentLabel': 'black_attack'}}
    >>> black_attack2 = {'_0_2_mc': black_attack_decoration, '_0_3_mc': black_attack_decoration}
    >>> node = tree.makeNode([])
    >>> print node
    ;
    >>> node = news_to_property(node, black_attack2)
    >>> print node
    ;MA[ca][da]

    Multiple marks of formation.
    >>> white_attack_formation = {'formation_mc': {'currentLabel': 'white_attack'}}
    >>> white_attack2 = {'_1_2_mc': white_attack_formation, '_1_3_mc': white_attack_formation}
    >>> node = tree.makeNode([])
    >>> print node
    ;
    >>> node = news_to_property(node, white_attack2)
    >>> print node
    ;TR[cb][db]

    Mark combo formation.
    >>> white_attack_formation = {'formation_mc': {'currentLabel': 'white_attack_defend'}}
    >>> white_attack2 = {'_1_2_mc': white_attack_formation, '_1_3_mc': white_attack_formation}
    >>> node = tree.makeNode([])
    >>> print node
    ;
    >>> node = news_to_property(node, white_attack2)
    >>> print node
    ;TR[cb][db]SQ[cb][db]
    '''
    def is_intersection(name):
        intersection_name_pattern = re.compile('^_[0-9]_[0-9]_mc$')
        if intersection_name_pattern.match(name):
            return True
        return False
    # XXX circular import
    from intersection_mc import get_row_column
    sorted_news_items = news.items()
    sorted_news_items.sort()
    for name, value in sorted_news_items:
        if is_intersection(name):
            for parent, child in intersection_news_dictionary.items():
                if value.has_key(parent):
                    value_child = value[parent]
                    if value_child.has_key('currentLabel'):
                        for label, ids in child.items():
                            if label == value_child.get('currentLabel'):
                                row, column = get_row_column(name)
                                sgf_position = get_coordinates(row, column)
                                for id in ids:
                                    if not node.has_key(id):
                                        property = sgflib.Property(id, [sgf_position])
                                        node.addProperty(property)
                                    else:
                                        property = node[id]
                                        property.append(sgf_position)
    return node

def get_sgf_tree(history, size = 9):
    r'''Supports black, white, hide, unhide, pass, resign.
    >>> print get_sgf_tree([])
    (;GM[1]SZ[9])
    >>> print get_sgf_tree([{'black': (0, 1)}])
    (;GM[1]SZ[9];B[ba])
    >>> print get_sgf_tree([{'black': (0, 1), 'hide': [(0, 1)]}])
    (;GM[1]SZ[9];MA[ba])

    Add black stone.
    >>> print get_sgf_tree([{'add_black': [(1, 2)], 'size': 5}])
    (;GM[1]SZ[5]AB[cb])
    
    Unhide before play.
    append hide as a null move comment.
    two passes in a row would end game.
    >>> print get_sgf_tree([{'black': (0, 1), 'hide': [(0, 1)]}, 
    ...     {'white': (1, 0)},
    ...     {'black': (0, 0)},
    ...     {'white': (1, 1), 'unhide': [(0, 1), (1, 2)]}  ]) #doctest: +NORMALIZE_WHITESPACE
    (;GM[1]SZ[9];MA[ba];W[ab];B[aa];B[ba][cb]CR[ba][cb]W[bb])
    
    >>> print get_sgf_tree([{'white': 'pass'}]) 
    (;GM[1]SZ[9];W[tt])
    >>> print get_sgf_tree([{'white': 'resign'}]) 
    (;GM[1]SZ[9]RE[B+Resign])
    >>> print get_sgf_tree([{'black': (0, 1), 'extra_stone_gift': '_1'}])
    (;GM[1]SZ[9];B[ba]C[extra_stone_gift _1])
    >>> unhide = [{'black_last_move': [(4, 3)], 'black': (4, 3), 'empty': [(3, 3)], 'unhide': [(3, 2)]}]
    >>> print get_sgf_tree(unhide)
    (;GM[1]SZ[9];B[cd][de]CR[cd])

    3x3 board
    >>> print get_sgf_tree([{'black': (0, 1), 'hide': [(0, 1)]}], size = 3)
    (;GM[1]SZ[3];MA[ba])

    Insert news
    
    Extra stone news embedded in comment.
    Size event updates board size and overwrites size parameter.
    >>> embedded_extra_stone_comment = "(;GM[1]SZ[5];B[ba]C[{'extra_stone_gift_mc': {'currentLabel': '_1'}}])"
    >>> ## history = get_history( parse(embedded_extra_stone_comment) )
    >>> history = [{'size': 5}, {'news': {'extra_stone_gift_mc': {'currentLabel': '_1'}}, 'black': (0, 1)}]
    >>> history[0]
    {'size': 5}
    >>> history[1].get('news')
    {'extra_stone_gift_mc': {'currentLabel': '_1'}}
    >>> sgf_tree = get_sgf_tree(history)
    >>> if not str(sgf_tree) == embedded_extra_stone_comment:
    ...     print sgf_tree

    black_attack decoration news saved as mark and comment.
    >>> black_attack_decoration = {'decoration_mc': {'currentLabel': 'black_attack'}}
    >>> black_attack = {'_0_2_mc': black_attack_decoration}
    >>> history = [{'size': 5}, {'news': black_attack, 'black': (0, 1)}]
    >>> sgf_tree = get_sgf_tree(history)
    >>> print sgf_tree
    (;GM[1]SZ[5];B[ba]MA[ca]
    C[{'_0_2_mc': {'decoration_mc': {'currentLabel': 'black_attack'}}}])

    black_attack decoration note saved as mark.
    >>> black_attack_decoration = {'decoration_mc': {'currentLabel': 'black_attack'}}
    >>> black_attack = {'_0_2_mc': black_attack_decoration}
    >>> history = [{'size': 5}, {'note': black_attack, 'black': (0, 1)}]
    >>> sgf_tree = get_sgf_tree(history)
    >>> print sgf_tree
    (;GM[1]SZ[5];B[ba]MA[ca])
    '''
    tree = sgflib.GameTree(nodelist=None, variations=None)
    #>>> print node
    ##;GM[1]SZ[9]
    if not history or 'size' not in history[0]:
        node = tree.makeNode([])
        go_property = sgflib.Property(sgf_game, [sgf_go_game])
        node.addProperty(go_property)
        if history:
            length = history[0].get('size', size)
        else:
            length = size
        size_property = sgflib.Property('SZ', [str(length)])
        node.addProperty(size_property)
        tree.append(node)
    #>>> print tree
    ##(;GM[1]SZ[9])
    colors = 'black', 'white'
    for event in history:
        node = tree.makeNode([])
        append_node = False
        if history and 'size' in event.keys():
            append_node = True
            go_property = sgflib.Property(sgf_game, [sgf_go_game])
            node.addProperty(go_property)
            length = history[0].get('size', size)
            size_property = sgflib.Property('SZ', [str(length)])
            node.addProperty(size_property)
            #- node = tree.makeNode([sgflib.Property(sgf_game, [sgf_go_game]), 
            #-     size_property])
            #- node = tree.makeNode([sgflib.Property(sgf_game, [sgf_go_game]), 
            #-     size_property])
        #elif history[0] == event:
        #    append_node = True
        #    size_property = sgflib.Property('SZ', [str(size)])
            #- node = tree.makeNode([sgflib.Property(sgf_game, [sgf_go_game]), 
            #-     size_property])
        if 'unhide' in event.keys():
            append_node = True
            unhides = event['unhide']
            coordinates = [ get_coordinates(*unhide)
                for unhide in unhides ]
            play_property = sgflib.Property(sgf_black, 
                    copy.deepcopy(coordinates))
            node.addProperty(play_property)
            unhide_property = sgflib.Property(sgf_unhide, 
                    copy.deepcopy(coordinates))
            node.addProperty(unhide_property)
        for add_key in add_colors:
            if add_key in event.keys():
                add_color = add_colors[add_key]
                append_node = True
                rows_colors = event[add_key]
                sgf_tag = add_stones[add_key]
                for row, column in rows_colors:
                    if not sgf_tag in node.data:
                        node = add_position(node, sgf_tag, row, column)
                    else:
                        node = append_position(node, sgf_tag, row, column)
        for color in colors:
            if color in event.keys():
                append_node = True
                move = event[color]
                if 'pass' == move:
                    pass_property = sgflib.Property(
                            get_sgf_color(color), [sgf_pass])
                    node.addProperty(pass_property)
                elif 'resign' == move:
                    if 'black' == color:
                        winner = 'white'
                    else:
                        winner = 'black'
                    sgf_result = 'RE'
                    result = '%s+%s' %  \
                            (get_sgf_color(winner), sgf_resign)
                    tree[0].addProperty(
                        sgflib.Property(sgf_result, 
                            [result]) )
                    append_node = False
                else:
                    #node = get_node(tree, color, row, column)
                    row, column = event[color]
                    hides = event.get('hide', [])
                    for hide in hides:
                        if (row, column) == hide:
                            annotate(node, sgf_hide, row, column)
                    if not hides:
                        if not get_sgf_color(color) in node.data:
                            add_move(node, color, row, column)
                        else:
                            append_move(node, color, row, column)
        if event.has_key('news'):
            news = event['news']
            node = news_to_property(node, news)
            news_string = str(news)
            comment = node.makeProperty(sgf_comment, 
                [news_string])
            node.addProperty(comment)
        if event.has_key('note'):
            note = event['note']
            node = news_to_property(node, note)
        # XXX deprecate gift in favor of news?
        event_gift_list = []
        for gift in 'extra_stone_gift', 'hide_gift', 'extra_stone':
            if gift in event:
                event_gift_list.append( '%s %s' % (gift, event[gift]) )
        if event_gift_list:
            append_node = True
            comment = node.makeProperty(sgf_comment, 
                event_gift_list)
            node.addProperty(comment)
        if append_node:
            tree.append(node)
    #>>> print tree
    ##(;GM[1]SZ[9];W[aa])
    #>>> str(tree)
    ##'(;GM[1]SZ[9];W[aa];W[ab])'
    return tree

def save_sgf(history, path, size = 9):
    '''
    >>> print get_sgf_tree([{'white': 'pass'}]) 
    (;GM[1]SZ[9];W[tt])
    >>> sgf = get_sgf_tree([{'white': 'pass'}])
    >>> save_sgf([{'white': 'pass'}], 'sgf/__tmp.sgf')
    >>> print text.load('sgf/__tmp.sgf')
    (;GM[1]SZ[9];W[tt])

    3x3 board
    >>> print get_sgf_tree([{'white': 'pass'}], size = 3) 
    (;GM[1]SZ[3];W[tt])
    >>> sgf = get_sgf_tree([{'white': 'pass'}], size = 3)
    >>> save_sgf([{'white': 'pass'}], 'sgf/__tmp.sgf', size = 3)
    >>> print text.load('sgf/__tmp.sgf')
    (;GM[1]SZ[3];W[tt])
    '''
    sgf_tree = get_sgf_tree(history, size = size)
    text.save(path, str(sgf_tree))


def parse(sgf_tree_text):
    '''Text of one game to SGF tree.
    >>> print parse('(;GM[1]SZ[9];B[ba])')
    (;GM[1]SZ[9];B[ba])
    '''
    parser = sgflib.SGFParser(str(sgf_tree_text))
    collection = parser.parseOneGame()
    return collection


many_faces_of_go_sgf_text = '''(;
GM[1]FF[4]VW[]AP[Many Faces of Go:11.0]
SZ[5]
HA[0]
ST[2]
DT[2010-04-29]
KM[0.0]CA[UTF-8];B[cc];W[dc];B[cd];W[dd];B[cb];W[db];B[ce];W[de]
;B[ca];W[da]
C[Did black WIN or LOSE?

WIN
LOSE]
LB[ec:LOSE][bc:WIN]
)'''

go_gui_sgf_text = '''(;FF[4]CA[UTF-8]AP[GoGui:1.1.10]SZ[5]
KM[0]DT[2010-05-01]
;B[db];W[cc];B[cb];W[bc];B[bb];W[dc];B[eb];W[ec];B[ab];W[ac]
C[THIS CAKE IS CUT.  DID WE WIN OR LOSE?]LB[cd:LOSE][ca:WIN])'''

from text import windows_to_unix
def extract_news(comment):
    r'''Extract single news from comment.  Return news and rest of comment.
    >>> extract_news('\r\nI WILL EAT YOUR CAKE!')
    (None, '\r\nI WILL EAT YOUR CAKE!')

    Does not interpret incomplete news.
    >>> extract_news("\r\n{'liberty_mc': {'currentLabel':I WILL EAT YOUR CAKE!")
    (None, "\r\n{'liberty_mc': {'currentLabel':I WILL EAT YOUR CAKE!")

    Strip new lines and spaces.
    >>> news_comment = "   {'liberty_mc': {'currentLabel': 'show'}}  \r\nETHAN:  NOW I HAVE A FORK, SO I WILL EAT YOUR CAKE!"
    >>> news, comment = extract_news(news_comment)
    >>> news
    {'liberty_mc': {'currentLabel': 'show'}}
    >>> comment
    'ETHAN:  NOW I HAVE A FORK, SO I WILL EAT YOUR CAKE!'

    Strip new lines afterward.
    >>> comment_news = "ETHAN:  NOW I HAVE A FORK, SO I WILL EAT YOUR CAKE!\r\n{'liberty_mc': {'currentLabel': 'show'}}"
    >>> news, comment = extract_news(comment_news)
    >>> news
    {'liberty_mc': {'currentLabel': 'show'}}
    >>> comment
    'ETHAN:  NOW I HAVE A FORK, SO I WILL EAT YOUR CAKE!'

    Convert Windows to Unix newlines in between.
    >>> comment_news = "ETHAN:  NOW I HAVE A FORK, \r\nSO I WILL EAT YOUR CAKE!\r\n{'liberty_mc': {'currentLabel': \r\n'show'}}"
    >>> news, comment = extract_news(comment_news)
    >>> news
    {'liberty_mc': {'currentLabel': 'show'}}
    >>> comment
    'ETHAN:  NOW I HAVE A FORK, \nSO I WILL EAT YOUR CAKE!'

    Return comment only.
    >>> comment_only = "ETHAN:  NOW I HAVE A FORK, SO I WILL EAT YOUR CAKE!"
    >>> news, comment = extract_news(comment_only)
    >>> news
    >>> comment
    'ETHAN:  NOW I HAVE A FORK, SO I WILL EAT YOUR CAKE!'

    >>> bad = "{'a': 0}{'b': 1}"
    >>> extract_news(bad)
    Traceback (most recent call last):
      ...
    SyntaxError: invalid syntax
    '''
    nowhere = -1
    start = comment.find('{')
    end = comment.rfind('}')
    if nowhere == start or nowhere == end:
        return (None, comment)
    news_text = comment[start:end+1]
    without_news = comment.replace(news_text, '').strip(' \r\n').rstrip(' \r\n')
    news_unix = windows_to_unix(news_text)
    without_news = windows_to_unix(without_news)
    return eval(news_unix), without_news


def get_history(sgf_tree):
    r'''Convert SGF text into python game format history.
    Supports black, white, hide, unhide, pass, resign.
    >>> get_history( parse('') )
    []
    >>> get_history( parse('(;GM[1]SZ[9];B[ba])') )
    [{'size': 9}, {'black': (0, 1)}]
    >>> get_history( parse('(;GM[1]SZ[9];MA[ba])') )
    [{'size': 9}, {'black': (0, 1), 'hide': [(0, 1)]}]

    Unhide before play.
    append hide as a null move comment.
    two passes in a row would end game.
    >>> hide_unhide_sgf = parse('(;GM[1]SZ[9];MA[ba];W[ab];B[aa];B[ba][cb]CR[ba][cb]W[bb])')
    >>> get_history( hide_unhide_sgf ) # doctest: +NORMALIZE_WHITESPACE
    [{'size': 9}, {'black': (0, 1), 'hide': [(0, 1)]}, {'white': (1, 0)}, {'black': (0, 0)}, {'white': (1, 1), 'unhide': [(0, 1), (1, 2)]}]
    >>> get_history( parse('(;GM[1]SZ[9];W[tt])') )
    [{'size': 9}, {'white': 'pass'}]
    >>> get_history( parse('(;GM[1]SZ[9]RE[B+Resign])') )
    [{'size': 9}, {'white': 'resign'}]
    
    Extra stone news embedded in comment.
    >>> embedded_extra_stone_comment = "(;GM[1]SZ[9];B[ba]C[{'extra_stone_gift_mc': {'currentLabel': '_1'}}])"
    >>> history = get_history( parse(embedded_extra_stone_comment) )
    >>> history[0]
    {'size': 9}
    >>> history[1].get('news')
    {'extra_stone_gift_mc': {'currentLabel': '_1'}}

    #- Deprecate or modify to news?
    #- >>> get_history( parse('(;GM[1]SZ[9];B[ba]C[extra_stone_gift _1])') )
    #- [{'size': 9}, {'black': (0, 1), 'extra_stone_gift': '_1'}]

    Parse Many Faces of Go header.
    >>> get_history( parse(many_faces_of_go_sgf_text) )[0]
    {'handicap': 0, 'size': 5}

    Parse GoGui header.
    >>> get_history( parse(go_gui_sgf_text) )[0]
    {'size': 5}

    GoGui pass.
    >>> get_history( parse('(;GM[1]SZ[9];W[])') )
    [{'size': 9}, {'white': 'pass'}]

    News embedded in comment.
    >>> news_in_comment = "(;GM[1]SZ[3]C[{'liberty_mc': {'currentLabel': 'show'}}\n\nETHAN:  NOW I HAVE A FORK, SO I WILL EAT YOUR CAKE!];B[ab])"
    >>> history = get_history( parse(news_in_comment) )
    >>> len(history)
    2
    >>> history[0].get('news')
    {'liberty_mc': {'currentLabel': 'show'}}
    >>> history[0].get('size')
    3
    >>> history[1].get('black')
    (1, 0)

    SGF comment --> strip news --> event['comment']
    >>> history[0].get('comment')
    'ETHAN:  NOW I HAVE A FORK, SO I WILL EAT YOUR CAKE!'
    >>> history[0].get('news')
    {'liberty_mc': {'currentLabel': 'show'}}

    >>> sgf_text = text.load('sgf/beginner/capture_3_3.sgf')
    >>> history = get_history( parse(sgf_text) )
    >>> if not history[0].get('news').get('option_mc').get('first_capture_mc') == {'currentLabel': 'show'}:
    ...     import pprint; pprint.pprint(history)
    >>> news_in_last_comment = "(;GM[1]SZ[3];B[ab];W[ba]C[{'liberty_mc': {'currentLabel': 'show'}}    \n\nETHAN:  NOW I HAVE A FORK, SO I WILL EAT YOUR CAKE!])"
    >>> news_in_last_sgf = parse(news_in_last_comment)
    >>> history = get_history(news_in_last_sgf)
    >>> len(history)
    3
    >>> if not history[-1].get('news') == {'liberty_mc': {'currentLabel': 'show'}}:
    ...     from pprint import pprint as pp; pp(history)
    >>> if not history[-1].get('comment') == 'ETHAN:  NOW I HAVE A FORK, SO I WILL EAT YOUR CAKE!':
    ...     from pprint import pprint as pp; pp(history)

    Comment in first node.
    >>> sgf_hello = '(;C[hello])'
    >>> get_history( parse(sgf_hello) )
    [{'comment': 'hello'}]

    Black rank
    >>> get_history( sgf_from_file('sgf/test_opening_note.sgf') )[0]['BR']
    '49k'
    '''
    history = []
    if not sgf_tree:
        return history
    end = []
    for node in sgf_tree:
        event = {}
        if sgf_game in node.keys() or sgf_size in node.keys():
            # header
            for property in node:
                if sgf_game == property.id:
                    if sgf_go_game != property.data[0]:
                        print 'get_history:  I only parse Go games, not:  %s in %s' \
                                % (property, node)
                elif sgf_size == property.id:
                    if property.data[0] not in sgf_sizes:
                        print 'get_history:  I only parse sizes %s, not:  %s in %s' \
                                % (sgf_sizes, property, node)
                    event['size'] = int(property.data[0])
                elif sgf_result == property.id:
                    result = property.data[0]
                    if result.startswith(sgf_black):
                        if result.endswith(sgf_resign) or result.endswith(sgf_resign2):
                            end.append( {'white': 'resign'} )
                    elif result.startswith(sgf_white):
                        if result.endswith(sgf_resign) or result.endswith(sgf_resign2):
                            end.append( {'black': 'resign'} )
                    else:
                        print 'get_history:  what do i do with this result?  %s in %s' % (property, node)
                elif sgf_comment == property.id:
                    comment = property.data[0]
                    event = _insert_news(event, comment)
                elif property.id in sgf_add_stone_dictionary:
                    event = _insert_add_stone(event, property)
                elif property.id in sgf_color_node_dictionary:
                    event = _insert_color_node(event, property)
                elif property.id in sgf_not_supported:
                    pass
                elif property.id in sgf_text_dictionary:
                    pass
                elif property.id in sgf_int_dictionary:
                    pass
                elif property.id in sgf_copy_list:
                    event[property.id] = property.data[0]
                else:
                    print 'get_history:  what do i do with this id?  %s' % (property.id)
        else:
            for property in node:
                event = _insert_hide_black(event, property)
            for property in node:
                event = _insert_move(event, property)
            for property in node:
                event = _insert_gift(event, property)
            for property in node:
                if sgf_comment == property.id:
                    comment = property.data[0]
                    event = _insert_news(event, comment)
            for property in node:
                event = _insert_add_stone(event, property)
            for property in node:
                event = _insert_color_node(event, property)
        event = get_text(event, node)
        event = get_int(event, node)
        if event:
            history.append(event)
    history.extend(end)
    return history


def kyu_to_level(kyu_text):
    '''Convert go kyu to level: (50 - kyu).
    >>> kyu_to_level('49k')
    1
    >>> kyu_to_level('55k')
    -5
    >>> kyu_to_level('1k')
    49
    >>> kyu_to_level('9k')
    41
    >>> kyu_to_level(9)
    Traceback (most recent call last):
      ...
    AttributeError: 'int' object has no attribute 'rstrip'
    '''
    kyu = int(kyu_text.rstrip('k'))
    return 50 - kyu
   
def sgf_file_to_black_level(sgf_file):
    '''Extract level information from file.
    >>> sgf_file_to_black_level('sgf/test_opening_note.sgf')
    1
    '''
    history = sgf_to_history(sgf_file)
    if history:
        head = history[0]
        if head:
            if 'BR' in head:
                return kyu_to_level(head['BR'])
    
def get_text(event, node):
    '''Text field from SGF converts to corresponding in PGF.
    >>> sgf_text = text.load('sgf/test_opening_note.sgf')
    >>> sgf_tree = parse(sgf_text)
    >>> node = sgf_tree[0]
    >>> event = get_text({}, node)
    >>> event.has_key('opening_note')
    True
    >>> history = get_history( parse(sgf_text) )
    >>> if not history[0].get('opening_note'):
    ...     import pprint; pprint.pprint(history)
    '''
    for property in node:
        if property.id in sgf_text_dictionary:
            pgf_id = sgf_text_dictionary[property.id]
            event[pgf_id] = property[0]
    return event

def get_int(event, node):
    '''int field from SGF converts to corresponding in PGF.
    >>> sgf_text = text.load('sgf/test_eight_sides_black_9_9.sgf')
    >>> sgf_tree = parse(sgf_text)
    >>> node = sgf_tree[0]
    >>> event = get_int({}, node)
    >>> event['handicap']
    3
    >>> history = get_history( parse(sgf_text) )
    >>> if not history[0].get('handicap') == 3:
    ...     import pprint; pprint.pprint(history)
    '''
    for property in node:
        if property.id in sgf_int_dictionary:
            pgf_id = sgf_int_dictionary[property.id]
            event[pgf_id] = int(property[0])
    return event

import os
def sgf_to_history(file):
    '''
    >>> history = sgf_to_history('sgf/beginner/count_5_5.sgf')
    >>> history = sgf_to_history('sgf/NO_SUCH.sgf')
    sgf_from_file: file not found
    >>> history
    []
    '''
    sgf = sgf_from_file(file)
    if sgf:
        return get_history(sgf)
    else:
        return []


def sgf_from_file(file):
    '''
    >>> sgf = sgf_from_file('sgf/beginner/count_5_5.sgf')
    >>> print sgf[0]['FF']
    FF[4]
    >>> history = sgf_from_file('sgf/NO_SUCH.sgf')
    sgf_from_file: file not found
    >>> history
    '''
    if os.path.exists(file):
        sgf_text = text.load(file)
        return parse(sgf_text)
    else:
        print 'sgf_from_file: file not found'

def _insert_move(dictionary, property):
    '''After unhide, so unhidden are not duplicated as moves.
    >>> _insert_move({}, property) #doctest: +SKIP
    {'black': (0, 1)}
    '''
    if str(property.id) in sgf_move_dictionary:
        key = sgf_move_dictionary.get(property.id)
        sgf_move = property.data[0]
        if sgf_move in sgf_passes:
            dictionary[key] = 'pass'
        else:
            position = get_position(sgf_move)
            if position not in dictionary.get('unhide', []):
                dictionary[key] = position
    return dictionary


def _insert_add_stone(event, property):
    '''Add black stones in head.
    >>> from pprint import pprint
    >>> pprint(   get_history( parse('(;GM[1]SZ[5]AB[aa][ab][ba])') )   )
    [{'add_black': [(0, 0), (1, 0), (0, 1)], 'size': 5}]
    
    Add black stones later.
    >>> pprint(   get_history( parse('(;GM[1]SZ[9];AB[aa][ab][ba])') )   )
    [{'size': 9}, {'add_black': [(0, 0), (1, 0), (0, 1)]}]
    >>> pprint(   get_history( parse('(;GM[1]SZ[7];AB[aa][ab][ba])') )   )
    [{'size': 7}, {'add_black': [(0, 0), (1, 0), (0, 1)]}]
    >>> pprint(   get_history( parse('(;GM[1]SZ[5];AB[aa][ab][ba])') )   )
    [{'size': 5}, {'add_black': [(0, 0), (1, 0), (0, 1)]}]
    >>> pprint(   get_history( parse('(;GM[1]SZ[3];AB[aa][ab][ba])') )   )
    [{'size': 3}, {'add_black': [(0, 0), (1, 0), (0, 1)]}]

    Mark squares.
    >>> pprint(   get_history( parse('(;GM[1]SZ[3];SQ[aa][ab][ba])') )   )
    [{'size': 3}, {'square': [(0, 0), (1, 0), (0, 1)]}]
    '''
    if str(property.id) in sgf_add_stone_dictionary:
        key = sgf_add_stone_dictionary.get(property.id)
        sgf_moves = property.data
        for sgf_move in sgf_moves:
            position = get_position(sgf_move)
            if not event.has_key(key):
                event[key] = []
            event[key].append(position)
    return event

def _insert_color_node(event, property):
    '''Set black or white to play
    >>> from pprint import pprint
    >>> pprint(   get_history( parse('(;GM[1]SZ[5]AB[aa][ab][ba]PL[B])') )   )
    [{'add_black': [(0, 0), (1, 0), (0, 1)], 'play': 'black', 'size': 5}]
    >>> pprint(   get_history( parse('(;GM[1]SZ[5]AW[aa][ab][ba]PL[W])') )   )
    [{'add_white': [(0, 0), (1, 0), (0, 1)], 'play': 'white', 'size': 5}]
    >>> pprint(   get_history( parse('(;GM[1]SZ[5];AB[aa][ab][ba]PL[B])') )   )
    [{'size': 5}, {'add_black': [(0, 0), (1, 0), (0, 1)], 'play': 'black'}]
    '''
    if str(property.id) in sgf_color_node_dictionary:
        key = sgf_color_node_dictionary.get(property.id)
        sgf_colors = property.data
        for sgf_color in sgf_colors:
            color = sgf_move_dictionary[sgf_color]
            event[key] = color
    return event

def _insert_hide_black(dictionary, property):
    id = str(property.id)
    if id in sgf_hide_dictionary:
        if sgf_hide == id:
            hide = sgf_hide_dictionary.get(property.id) 
            position = get_position(property.data[0])
            draw(dictionary, hide, position)
            dictionary['black'] = position
        elif sgf_unhide == id:
            unhide = sgf_hide_dictionary.get(property.id) 
            positions = [ get_position(sgf_coordinate)
                for sgf_coordinate in property.data ]
            draw(dictionary, unhide, *positions)
    return dictionary


def _insert_gift(dictionary, property):
    '''Deprecate or modify to news?'''
    if str(property.id) == sgf_comment:
        key = sgf_move_dictionary.get(property.id)
        comments = property.data
        for comment in comments:
            for gift in 'extra_stone_gift', 'hide_gift', 'extra_stone':
                if comment.startswith(gift):
                    gift_name, value = comment.split(' ')
                    dictionary[gift_name] = value
    return dictionary

def _insert_news(event, comment):
    news, comment_without_news = extract_news(comment)
    if news:
        event['news'] = news
    if comment_without_news:
        event['comment'] = comment_without_news
    return event


def sgf_to_pgf(sgf_tree):
    r'''
    Tree of smart game format, using native data types of python.
    sgf  ([] ; []     (;[] )   (;[] )   )
    pgf  [{} , {} ,   [ {} ] , [ {} ]   ]

    smart game format
    >>> sgf = parse("""(;C[hello]
    ... (;B[aa]C[corner];W[ba])
    ... (;B[ab]C[side](;W[bb])(;W[bc]))   
    ... (;B[]C[pass]))""")
    
    python game format
    >>> pgf = [{'comment':'hello'}, 
    ... [{'black': (0, 0), 'comment': 'corner'}, {'white': (0, 1)}], 
    ... [{'black': (1, 0), 'comment': 'side'}, [{'white': (1, 1)}], [{'white': (2, 1)}]],
    ... [{'black': 'pass', 'comment': 'pass'}]]

    >>> from pprint import pprint
    >>> if not pgf == sgf_to_pgf(sgf):
    ...     print 'expected:'; pprint(pgf); print 'got:'; pprint(sgf_to_pgf(sgf))
    >>> sgf_to_pgf(sgf)[1][1]
    {'white': (0, 1)}

    Without and with variation.
    >>> sgf_to_pgf( parse('') )
    []
    >>> sgf_to_pgf( parse('(;GM[1]SZ[5];B[aa];W[ab])') )
    [{'size': 5}, {'black': (0, 0)}, {'white': (1, 0)}]
    >>> sgf_to_pgf( parse('(;GM[1]SZ[5];(;B[aa];W[ab])(;B[ae];W[ad]))') )
    [{'size': 5}, [{'black': (0, 0)}, {'white': (1, 0)}], [{'black': (4, 0)}, {'white': (3, 0)}]]
    '''
    pgf_tree = get_history(sgf_tree)
    if pgf_tree:
        for variant in sgf_tree.variations:
            considered = sgf_to_pgf(variant)
            pgf_tree.append(considered)
    return pgf_tree

def sgf_file_to_pgf(file):
    '''
    >>> history = sgf_file_to_pgf('sgf/beginner/capture_3_3.sgf')
    >>> history = sgf_file_to_pgf('sgf/NO_SUCH.sgf')
    sgf_file_to_pgf: file not found
    >>> history
    []
    '''
    history = []
    if os.path.exists(file):
        sgf_text = text.load(file)
        history = sgf_to_pgf(parse(sgf_text))
    else:
        print 'sgf_file_to_pgf: file not found'
    return history


def behead(tree):
    '''
    >>> behead([])
    []
    >>> behead([{'size': 5}])
    []
    >>> behead([{'black': (0, 0), 'size': 5}])
    []
    >>> behead([{'size': 5}, {'black': (0, 0)}])
    [{'black': (0, 0)}]
    >>> behead([{'black': (0, 0)}])
    [{'black': (0, 0)}]
    '''
    if tree:
        possible_head = tree[0]
        if possible_head.has_key('size'):
            return tree[1:]
    return tree




def plumb(nested_list):
    '''First non-list in list
    >>> plumb([1])
    1
    >>> plumb([[3], [2]])
    3
    >>> plumb([])
    >>> plumb(4)
    4
    '''
    element = nested_list
    if element:
        while type([]) == type(element):
            element = element[0]
        return element

def get_match(pgf_event, pgf_node):
    '''If size or position of event matches first node, return that node.
    >>> pgf_history = [{'size': 5}, {'black': (2, 2)}, {'white': (1, 2)}]
    >>> pgf_tree = [{'size': 5, 'comment': 'where?'}, [{'black': (2, 2)}, {'white': (1, 2)}], [{'black': (0, 0), 'comment': '?'}]]
    >>> get_match(pgf_history[0], pgf_tree[0])['comment']
    'where?'
    >>> get_match(pgf_history[1], pgf_tree[1])
    get_match:  expect pgf_node to be a dictionary
    >>> get_match(pgf_history[1], pgf_tree[1][0])
    {'black': (2, 2)}
    >>> pgf_tree = sgf_to_pgf(sgf_from_file('sgf/test_capture_3_3.sgf'))
    >>> get_match({'black': (0, 0)}, pgf_tree[3][0])['black']
    (0, 0)
    >>> get_match({'black': (0, 0)}, pgf_tree[3])
    get_match:  expect pgf_node to be a dictionary

    Pass matches any unspecified.
    >>> pgf_tree[2][0]['black']
    'pass'
    >>> get_match({'black': (0, 1)}, pgf_tree[2][0])['black']
    'pass'
    >>> get_match({'black': (0, 1)}, pgf_tree[2])
    get_match:  expect pgf_node to be a dictionary

    Match essences, add_black, add_white
    >>> pgf_history = [{'add_black': [(1, 1)], 'add_white': [(0, 0)], 'size': 3}, {'black': (0, 1)}]
    >>> pgf_tree = [{'size': 3, 'comment': 'where?', 'add_black': [(1, 1)], 'add_white': [(2, 2)]}, [[{'black': (1, 2)}], [{'black': (0, 1)}]]]
    >>> get_match(pgf_history[0], pgf_tree[0])
    '''
    if type({}) != type(pgf_node):
        print 'get_match:  expect pgf_node to be a dictionary'
        return
    matched = None
    # node_event = plumb(pgf_node)
    for k in essences:
        if pgf_event.has_key(k) and pgf_node.has_key(k):
            if pgf_event.get(k) == pgf_node.get(k):
                matched = k
            elif 'pass' == pgf_node.get(k):
                matched = k
            else:
                return
    if matched:
        return pgf_node

def pass_last(branches):
    '''Placing pass last, modifying the branches in place.
    >>> pgf_tree = sgf_to_pgf(sgf_from_file('sgf/test_capture_3_3.sgf'))
    >>> pgf_tree[-1][0]['black']
    (2, 0)
    >>> pass_last(pgf_tree)
    >>> pgf_tree[-1][0]['black']
    'pass'

    Passing is before a tuple, so sorting the tree may be insufficient.
    >>> 'pass' < (8, 8)
    True
    >>> pgf_tree.sort() 
    >>> pgf_tree[-1][0]['black']
    'pass'
    >>> pgf_tree.insert(1, [{'black': 'pass'}])
    >>> pgf_tree.sort() 
    >>> pgf_tree[-1][0]['black']
    'pass'
    >>> pgf_tree[1][0]['black']
    'pass'
    >>> ## from pprint import pprint
    >>> ## pprint(pgf_tree)

    Other elements are not sorted.
    '''
    branch_indexes = range(len(branches))
    branch_indexes.reverse()
    for b in branch_indexes:
        branch = branches[b]
        node_event = plumb(branch)
        colors = ['black', 'white']
        for color in colors:
            if 'pass' == node_event.get(color):
                passed = branches.pop(b)
                branches.append(passed)
                break
        

def get_node_on_path(pgf_history, pgf_tree):
    '''get node of history that has a path in the tree.
    And remaining tree.
    >>> pgf_tree = sgf_to_pgf(sgf_from_file('sgf/test_node_on_path.sgf'))
    >>> pgf_history = sgf_to_pgf(parse( '(;GM[1]SZ[3])' ))
    >>> event, remaining = get_node_on_path(pgf_history, pgf_tree)
    >>> event
    {}
    >>> pgf_history = sgf_to_pgf(parse( '(;GM[1]SZ[5])' ))
    >>> event, remaining = get_node_on_path(pgf_history, pgf_tree)
    >>> event['size']
    5
    >>> pgf_history = sgf_to_pgf(parse( '(;GM[1]SZ[5];B[cc])' ))
    >>> event, remaining = get_node_on_path(pgf_history, pgf_tree)
    >>> event['black']
    (2, 2)
    >>> pgf_history = sgf_to_pgf(parse( '(;GM[1]SZ[5];B[cc];W[cb])' ))
    >>> pgf_history
    [{'size': 5}, {'black': (2, 2)}, {'white': (1, 2)}]
    >>> pgf_history[1]['black']
    (2, 2)
    >>> pgf_tree[1][0]['black']
    (2, 2)
    >>> event, remaining = get_node_on_path(pgf_history, pgf_tree)
    >>> remaining[0][0]
    {'black': (1, 1)}
    >>> if not event.has_key('comment'):  event
    >>> if event.has_key('bad_move_mc'):  event
    >>> pgf_history = sgf_to_pgf(parse( '(;GM[1]SZ[5];B[cc];W[cb];B[bb];W[bc];B[db];W[ab];B[ca];W[ba];B[cb])' ))
    >>> event, remaining = get_node_on_path(pgf_history, pgf_tree)
    >>> event
    {'black': (1, 2)}
    >>> len(remaining)
    1
    >>> remaining[0]['white']
    'pass'
    >>> pgf_history = sgf_to_pgf(parse( '(;GM[1]SZ[5];B[cc];W[cb];B[bb];W[bc];B[db];W[ab];B[ca];W[ba];B[aa])' ))
    >>> event, remaining = get_node_on_path(pgf_history, pgf_tree)
    >>> event
    {'black': (0, 0)}
    >>> old_pgf_tree = sgf_to_pgf(sgf_from_file('sgf/test_node_on_path.sgf'))
    >>> if not pgf_tree == old_pgf_tree:  
    ...     from pprint import pprint
    ...     pprint(old_pgf_tree)
    ...     pprint(pgf_tree)

    Different subbranch
    >>> pgf_history = sgf_to_pgf(parse( '(;GM[1]SZ[5];B[cc];W[cb];B[bb];W[bc];B[db];W[ab];B[aa])' ))
    >>> event, remaining = get_node_on_path(pgf_history, pgf_tree)
    >>> event['comment']
    'THE CORNER IS IN DANGER.  EXPLORE MORE.'
    >>> event, remaining = get_node_on_path(pgf_history, pgf_tree)
    >>> event['black']
    (0, 0)
    >>> old_pgf_tree = sgf_to_pgf(sgf_from_file('sgf/test_node_on_path.sgf'))
    >>> if not pgf_tree == old_pgf_tree:  
    ...     from pprint import pprint
    ...     pprint(old_pgf_tree)
    ...     pprint(pgf_tree)

    >>> pgf_tree = sgf_to_pgf(sgf_from_file('sgf/test_capture_3_3.sgf'))
    
    Pass in tree matches any move by that color, in history,
    except if an exact node matches.
    >>> pgf_history = sgf_to_pgf(parse( '(;GM[1]SZ[3];B[bb];W[ab])' ))
    >>> from pprint import pprint
    >>> pprint(pgf_history)
    [{'size': 3}, {'black': (1, 1)}, {'white': (1, 0)}]
    >>> event, remaining = get_node_on_path(pgf_history, pgf_tree)
    >>> if not event['news'].has_key('tutor_mc'):  event
    >>> pgf_history = sgf_to_pgf(parse( '(;GM[1]SZ[3];B[bb];W[ab];B[ba])' ))
    >>> event, remaining = get_node_on_path(pgf_history, pgf_tree)
    >>> if not event['news'].has_key('tutor_mc'):  event
    >>> pgf_history = sgf_to_pgf(parse( '(;GM[1]SZ[3];B[bb];W[ab];B[ba];W[aa])' ))
    >>> event, remaining  = get_node_on_path(pgf_history, pgf_tree)
    >>> if not event['news'].has_key('tutor_mc'):  event
    
    If beyond tree, return no event.
    >>> pgf_tree = sgf_to_pgf(sgf_from_file('sgf/test_node_on_path.sgf'))
    >>> pgf_history = sgf_to_pgf(parse( '(;GM[1]SZ[5];B[bb];W[bc];B[db];W[ab];B[ba];W[aa];B[bc])' ))
    >>> event, remaining = get_node_on_path(pgf_history, pgf_tree)
    >>> event
    {}
    >>> remaining
    []

    Beware that in history, size must be included or inserted.
    >>> pgf_tree = sgf_to_pgf(sgf_from_file('sgf/test_capture_3_3.sgf'))
    >>> event, remaining = get_node_on_path([{'black': (0, 0)}], pgf_tree)
    >>> event
    {}
    >>> event, remaining = get_node_on_path([{'size': 3}, {'black': (0, 0)}], pgf_tree)
    >>> event['black']
    (0, 0)
    >>> event, remaining = get_node_on_path([{'black': (0, 1)}], pgf_tree)
    >>> event, remaining = get_node_on_path([{'size': 3}, {'black': (0, 1)}], pgf_tree)
    >>> event['black']
    'pass'
    
    Size must match in the history.
    >>> pgf_tree = sgf_to_pgf(sgf_from_file('sgf/test_capture_3_3.sgf'))
    >>> event, remaining = get_node_on_path([{'black': (0, 0)}], pgf_tree)
    >>> event
    {}
    >>> event, remaining = get_node_on_path([{'size': 3}, {'black': (0, 0)}], pgf_tree)
    >>> event['black']
    (0, 0)
    >>> event, remaining = get_node_on_path([{'size': 5}, {'black': (0, 0)}], pgf_tree)
    >>> event
    {}
    '''
    remaining = pgf_tree
    match = {}
    for e, event in enumerate(pgf_history):
        if not remaining:
            match = {}
            break
        if type([]) != type(remaining[0]):
            next = remaining[0]
            match = get_match(event, next)
            if not match:
                match = {}
                break
            remaining = remaining[1:]
        else:
            pass_last(remaining)
            for branch in remaining:
                match, leftover = get_node_on_path(pgf_history[e:], branch)
                if match:
                    return match, leftover
            else:
                remaining = leftover
    return match, remaining


def reflect(row, column, size):
    '''reflect coordinates across horizontal axis.
    >>> reflect(2, 2, 5)
    (2, 2)
    >>> reflect(2, 1, 5)
    (2, 3)
    >>> reflect(2, 1, 9)
    (2, 7)
    '''
    return row, size - column - 1

def rotate_90(row, column, size):
    '''
    >>> rotate_90(0, 0, 3)
    (0, 2)

    0   1    *  -1  =   (0*-1 + 1*-1) = -1
    -1   0      -1      (-1*-1 + 0*-1)   1
    http://www.euclideanspace.com/maths/algebra/matrix/orthogonal/rotation/index.htm
    0   1    *  x  =   (0*x + 1*y) = -1
    -1   0      y      (-1*x + 0*y)   1
    '''
    pivot = (size - 1) / 2
    x = row - pivot
    y = column - pivot
    #rx = (0 * x + 1 * y)
    #ry = (-1 * x + 0 * y)
    rx = y
    ry = 0 - x
    return rx + pivot, ry + pivot

def rotate(row, column, size, quarter_turns = 1):
    '''positive number of quarter turns.
    rotate coordinates clockwise.
    >>> rotate(0, 0, 3)
    (0, 2)
    >>> rotate(0, 0, 3, 2)
    (2, 2)
    >>> rotate(0, 0, 3, 3)
    (2, 0)
    >>> rotate(0, 0, 3, 4)
    (0, 0)
    
    >>> rotate(2, 2, 5)
    (2, 2)
    >>> rotate(2, 1, 5)
    (1, 2)
    >>> rotate(2, 1, 9)
    (1, 6)
    >>> rotate(2, 1, 5, 4)
    (2, 1)
    '''
    r, c = row, column
    for quarter_turn in range(quarter_turns):
        r, c = rotate_90(r, c, size)
    return r, c

def rotate_180(row, column, size):
    return rotate(row, column, size, 2)

def rotate_270(row, column, size):
    return rotate(row, column, size, 3)

#def reflect_rotate_90(row, column, size):
#    r, c = reflect(row, column, size)
#    return rotate_90(r, c, size)

#def reflect_rotate_180(row, column, size):
#    r, c = reflect(row, column, size)
#    return rotate_180(r, c, size)

#def reflect_rotate_270(row, column, size):
#    r, c = reflect(row, column, size)
#    return rotate_270(r, c, size)

def rotate_0(row, column, size):
    return row, column

def transpose(row, column, size = 9):
    '''
    >>> transpose(0, 1, 3)
    (1, 0)
    '''
    return column, row

def compose(first, second):
    '''Compose two transforms.
    >>> reflect_90 = compose(reflect, rotate_90)
    >>> reflect_90(1, 2, 3)
    (0, 1)
    >>> reflect_90(0, 0, 3)
    (2, 2)
    '''
    def composition(row, column, size):
        row, column = first(row, column, size)
        return second(row, column, size)
    return composition

#symmetry_transforms = [
#    rotate_0,
#    rotate_90,
#    rotate_180,
#    rotate_270,
#    reflect,
#    reflect_rotate_90,
#    reflect_rotate_180,
#    reflect_rotate_270,
#]

symmetry_transforms = [
    rotate_0,
    rotate_90,
    rotate_180,
    rotate_270,
]

reflects = [compose(reflect, transform)
        for transform in symmetry_transforms]
symmetry_transforms.extend(reflects)
#transposes = [compose(transpose, transform)
#        for transform in symmetry_transforms]
#symmetry_transforms.extend(transposes)


essences = ['black', 'white', 'size', 'add_black', 'add_white']
def summarize(pgf_history):
    '''To trim fat and lighten load, 
    streamline history to size, black, white keys.
    >>> pgf_text = text.load('smart_go_format_test_fat.pgf.py')
    >>> if not 256 <= len(pgf_text):  pgf_text
    >>> pgf_history = eval(pgf_text)
    >>> from pprint import pprint
    >>> pprint(summarize(pgf_history))
    [{'size': 5},
     {'black': (2, 2)},
     {'white': (1, 2)},
     {'black': (1, 1)},
     {'white': (2, 1)},
     {'black': (3, 1)}]
    >>> pgf_text = text.load('smart_go_format_test_add_stone.pgf.py')
    >>> if not 256 <= len(pgf_text):  pgf_text
    >>> pgf_history = eval(pgf_text)
    >>> pprint(summarize(pgf_history))
    [{'add_black': [(1, 0), (2, 1), (2, 2), (2, 3)],
      'add_white': [(3, 0), (3, 1), (3, 2), (3, 3), (3, 4)],
      'size': 5}]
    '''
    slim_pgf = []
    for event in pgf_history:
        salient = {}
        for essence in essences:
            if essence in event:
                salient[essence] = event[essence]
        slim_pgf.append(salient)
    return slim_pgf


position_keys = ['black', 'white']
position_list_keys = ['add_black', 'add_white', 'square']
def get_symmetry(size, event, transform):
    '''Transform coordinates in an event.
    >>> get_symmetry(3, {'square': [(1, 0)]}, rotate_90)
    {'square': [(0, 1)]}
    >>> get_symmetry(5, {'black': (1, 0)}, rotate_180)
    {'black': (3, 4)}
    >>> get_symmetry(5, {'black': (1, 0)}, symmetry_transforms[-1])
    {'black': (0, 1)}
    >>> get_symmetry(3, {'black': 'pass'}, rotate_180)
    {'black': 'pass'}
    >>> get_symmetry(3, {'black': 'resign'}, rotate_180)
    {'black': 'resign'}
    '''
    for position in position_keys:
        if event.has_key(position) and 'pass' != event[position] \
                and 'resign' != event[position]:
            row, column = event[position]
            event[position] = transform(row, column, size)
    for position_list in position_list_keys:
        if event.has_key(position_list):
            event[position_list] = [transform(row, column, size) 
                for row, column in event[position_list] ]
    return event

def get_size(pgf_history, size = 9):
    '''Length of one edge of board.
    >>> get_size([])
    9
    >>> get_size([{'size': 3}])
    3
    >>> get_size([{'size': 5}, {'black': (1, 0)}])
    5
    '''
    if pgf_history:
        head = pgf_history[0]
        if head.has_key('size'):
            size = head.get('size')
    return size

import copy
def get_symmetries(pgf_history):
    '''
    mirror across horizontal
    rotate original and mirror 3 times
    store all eight in list
    sort list
    return first in list
    >>> symmetries = get_symmetries([{'size': 3}, {'square': [(1, 0)]}])

    Original
    >>> symmetries[0][1]['square']
    [(1, 0)]

    Rotate 90 clockwise
    >>> symmetries[1][1]['square']
    [(0, 1)]

    Reflect horizontal and rotate 90 counterclockwise
    >>> symmetries[-1][1]['square']
    [(0, 1)]

    Reflect horizontal
    >>> history = [{'size': 5}, {'black': (2, 2)}, {'white': (2, 1)}, {'black': (1, 2)}]
    >>> symmetries = get_symmetries(history)
    >>> symmetries[4][-2]
    {'white': (2, 3)}
    >>> symmetries[4][-1]
    {'black': (1, 2)}
    '''
    symmetries = []
    if pgf_history:
        size = get_size(pgf_history, 9)
        for transform in symmetry_transforms:
            symmetry = copy.deepcopy(pgf_history)
            for e, event in enumerate(symmetry):
                symmetry[e] = get_symmetry(size, symmetry[e], transform)
            symmetries.append( symmetry )
            #symmetry = copy.deepcopy(pgf_history)
            #for e, event in enumerate(symmetry):
            #    symmetry[e] = get_symmetry(size, event, transform)
            #symmetries.append( symmetry )
    return symmetries

def get_lowest_history(pgf_history):
    '''History that maps to top-left octant
    which is first in row, column sort.
    >>> pgf_history = sgf_to_pgf(parse( '(;GM[1]SZ[5];B[cc];W[cb])' ))
    >>> pgf_history
    [{'size': 5}, {'black': (2, 2)}, {'white': (1, 2)}]
    >>> get_lowest_history(pgf_history)
    [{'size': 5}, {'black': (2, 2)}, {'white': (1, 2)}]
    >>> pgf_history = sgf_to_pgf(parse( '(;GM[1]SZ[5];B[cc];W[bc])' ))
    >>> pgf_history
    [{'size': 5}, {'black': (2, 2)}, {'white': (2, 1)}]
    >>> get_lowest_history(pgf_history)
    [{'size': 5}, {'black': (2, 2)}, {'white': (1, 2)}]

    >>> pgf_history = sgf_to_pgf(parse( '(;GM[1]SZ[5];B[cc];W[bc];B[aa])' ))
    >>> pgf_history
    [{'size': 5}, {'black': (2, 2)}, {'white': (2, 1)}, {'black': (0, 0)}]
    >>> get_lowest_history(pgf_history)
    [{'size': 5}, {'black': (2, 2)}, {'white': (1, 2)}, {'black': (0, 0)}]
    >>> pgf_history = sgf_to_pgf(parse( '(;GM[1]SZ[5];B[cc];W[bc];B[ae])' ))
    >>> get_lowest_history(pgf_history)
    [{'size': 5}, {'black': (2, 2)}, {'white': (1, 2)}, {'black': (0, 0)}]

    Only black and white positions.
    Does not yet support add black or add white or marks.
    >>> pgf_history = [{'size': 5}, {'black': (2, 2)}, {'white': (1, 2)}, 
    ...     {'black': (1, 1)}, {'white': (2, 1)}, {'black': (3, 1)}]

    Does not find symmetrical board variants (moves in different order).
    Whereas, the last move (1, 3) is lower and is a symmetrical board.
    >>> from pprint import pprint
    >>> pprint( get_lowest_history(pgf_history) )
    [{'size': 5},
     {'black': (2, 2)},
     {'white': (1, 2)},
     {'black': (1, 1)},
     {'white': (2, 1)},
     {'black': (3, 1)}]

    Does rotate add_black and add_white.    
    >>> pgf_text = text.load('smart_go_format_test_add_stone.pgf.py')
    >>> pgf_history = summarize(eval(pgf_text))
    >>> pprint( get_lowest_history(pgf_history) )
    [{'add_black': [(0, 1), (1, 2), (2, 2), (3, 2)],
      'add_white': [(0, 3), (1, 3), (2, 3), (3, 3), (4, 3)],
      'size': 5}]
    '''
    symmetries = get_symmetries(pgf_history)
    symmetries.sort()
    lowest_history = symmetries[0]
    return lowest_history

#def get_lowest_tree(pgf_tree):
#    '''Recursively get subtree until flat history and reassemble.
#    Then sort.
#    >>> pgf_tree = sgf_to_pgf(sgf_from_file('sgf/test_add_stone.sgf'))
#    >>> from pprint import pprint
#    >>> pprint( get_lowest_tree(pgf_tree)[0]['add_black'] )
#    [(0, 1), (1, 2), (2, 2), (3, 2)]
#    '''
#    return pgf_tree

def get_node_on_any_path(pgf_history, pgf_tree):
    '''Rotated history also matches lowest octant SGF.
    >>> pgf_tree = sgf_to_pgf(sgf_from_file('sgf/test_node_on_path.sgf'))
    >>> pgf_history = sgf_to_pgf(parse( '(;GM[1]SZ[5];B[cc];W[bc])' ))
    >>> event = get_node_on_any_path(pgf_history, pgf_tree)
    >>> if not event.has_key('comment'):  event
    >>> if event.has_key('bad_move_mc'):  event
    >>> pgf_history = sgf_to_pgf(parse( '(;GM[1]SZ[5];B[cb])' ))
    >>> event = get_node_on_any_path(pgf_history, pgf_tree)
    >>> if not event.has_key('comment'):  event
    >>> if not event['news'].has_key('bad_move_mc'):  event
    >>> pgf_history = sgf_to_pgf(parse( '(;GM[1]SZ[5];B[cc];W[bc];B[cb])' ))
    >>> event = get_node_on_any_path(pgf_history, pgf_tree)
    >>> if not event.has_key('comment'):  event
    >>> if not event['news'].has_key('bad_move_mc'):  event

    Summarize history.  However, does not detect symmetrical board.
    >>> pgf_text = text.load('smart_go_format_test_fat.pgf.py')
    >>> pgf_history = eval(pgf_text)
    >>> get_node_on_any_path(pgf_history, pgf_tree)
    {}

    History is matched to lowest python game format tree.
    Only black and white positions and add black or add white.
    >>> pgf_text = text.load('smart_go_format_test_add_stone.pgf.py')
    >>> pgf_history = summarize(eval(pgf_text))
    >>> from pprint import pprint
    >>> pprint( pgf_history )
    [{'add_black': [(1, 0), (2, 1), (2, 2), (2, 3)],
      'add_white': [(3, 0), (3, 1), (3, 2), (3, 3), (3, 4)],
      'size': 5}]
    >>> pgf_history.append({'black': (2, 4)})
    >>> pgf_tree = sgf_to_pgf(sgf_from_file('sgf/test_add_stone.sgf'))
    >>> get_node_on_any_path(pgf_history, pgf_tree).get('news')

    >>> pgf_tree = sgf_to_pgf(sgf_from_file('sgf/test_node_on_path.sgf'))
    >>> pgf_history = sgf_to_pgf(parse( '(;GM[1]SZ[5];B[bb])' ))
    >>> event = get_node_on_any_path(pgf_history, pgf_tree)
    >>> event['comment'] #doctest: +ELLIPSIS
    'THIS CASTLE ONLY CLAIMS ...
    >>> pgf_history = sgf_to_pgf(parse( '(;GM[1]SZ[5];B[dd])' ))
    >>> event = get_node_on_any_path(pgf_history, pgf_tree)
    >>> if not event['comment'].startswith('THIS CASTLE ONLY CLAIMS'):
    ...     pprint(event)
    >>> pgf_history = sgf_to_pgf(parse( '(;GM[1]SZ[5];B[bd])' ))
    >>> event = get_node_on_any_path(pgf_history, pgf_tree)
    >>> if not event['comment'].startswith('THIS CASTLE ONLY CLAIMS'):
    ...     pprint(event)
    >>> pgf_history = sgf_to_pgf(parse( '(;GM[1]SZ[5];B[db])' ))
    >>> event = get_node_on_any_path(pgf_history, pgf_tree)
    >>> if not event['comment'].startswith('THIS CASTLE ONLY CLAIMS'):
    ...     pprint(event)

    If history is mirrored, flip square mark in event.
    >>> pgf_tree = sgf_to_pgf(sgf_from_file('sgf/test_mark_square.sgf'))
    >>> pgf_history = sgf_to_pgf(parse( '(;GM[1]SZ[3];B[bb];W[ba];B[cb])' ))
    >>> event = get_node_on_any_path(pgf_history, pgf_tree)
    >>> if (1, 0) not in event['square']:
    ...     pprint(event)
    '''
    summary = summarize(pgf_history)
    symmetries = get_symmetries(summary)
    def match_any(node):
        return 'pass' == node.get('black') or 'pass' == node.get('white')
    node = {}
    for s, symmetry in enumerate(symmetries):
        candidate, remaining = get_node_on_path(symmetry, pgf_tree)
        if candidate:
            transform = symmetry_transforms[s]
            size = get_size(symmetry, size = 9)
            original = copy.deepcopy(candidate)
            original = get_symmetry(size, original, transform)
            if not match_any(original):
                node = original
                break
            else:
                node = original
    return node


def get_node_on_rotated_tree_example():
    '''Match rotated SGF tree.
    >>> from pprint import pprint
    >>> pgf_tree = sgf_to_pgf(sgf_from_file('sgf/test_bottom_square.sgf'))
    >>> pgf_history = [{'size': 3, 'add_black': [(1, 1)], 'add_white': [(2, 2)]}, {'black': (2, 1)}]
    >>> event = get_node_on_any_path(pgf_history, pgf_tree)
    >>> if (1, 2) not in event['square']:
    ...     pprint(event)
    >>> if event.has_key('news') and 'bad_move_mc' in event.get('news'):  event

    Rotate next move.
    >>> next = next_move(pgf_history, pgf_tree)
    >>> if not next.get('white') == (1, 2):  
    ...     pprint(next)
    '''


def next_move(pgf_history, pgf_tree):
    '''First move after history that python game tree prescribes, if any.
    In game tree, pass represents any move.
    >>> pgf_tree = sgf_to_pgf(sgf_from_file('sgf/test_next_move.sgf'))
    >>> pgf_history = sgf_to_pgf(parse( '(;GM[1]SZ[3])' ))
    >>> next_move(pgf_history, [])
    {}
    >>> next = next_move(pgf_history, pgf_tree)
    >>> if not next.get('black') == (1, 1):  next, pgf_tree
    >>> pgf_history = sgf_to_pgf(parse( '(;GM[1]SZ[3];B[bb])' ))
    >>> next = next_move(pgf_history, pgf_tree)
    >>> if not next.get('white') == (0, 1):  next, pgf_tree
    >>> pgf_history = sgf_to_pgf(parse( '(;GM[1]SZ[3];B[bb];W[ba])' ))
    >>> next = next_move(pgf_history, pgf_tree)
    >>> if not next.get('black') == (1, 0):  next, pgf_tree
    >>> pgf_history = sgf_to_pgf(parse( '(;GM[1]SZ[3];B[bb];W[ba];B[ab])' ))
    >>> next = next_move(pgf_history, pgf_tree)
    >>> if not next.get('white') == (1, 2):  next, pgf_tree
    
    Rotate next move.
    >>> from pprint import pprint
    >>> pgf_tree = sgf_to_pgf(sgf_from_file('sgf/test_bottom_square.sgf'))
    >>> pgf_history = [{'size': 3, 'add_black': [(1, 1)], 'add_white': [(2, 2)]}, {'black': (2, 1)}]
    >>> next = next_move(pgf_history, pgf_tree)
    >>> if not next.get('white') == (1, 2):  
    ...     pprint(next)
    '''
    summary = summarize(pgf_history)
    symmetries = get_symmetries(summary)
    def match_any(node):
        return 'pass' == node.get('black') or 'pass' == node.get('white')
    node = {}
    remaining = []
    next = {}
    transform = None
    for s, symmetry in enumerate(symmetries):
        candidate, remaining = get_node_on_path(symmetry, pgf_tree)
        if candidate:
            node = candidate
            transform = symmetry_transforms[s]
            if not match_any(candidate):
                break
    else:
        remaining = []
    if remaining:
        next = plumb(remaining)
        size = get_size(symmetry, size = 9)
        original = copy.deepcopy(next)
        next = get_symmetry(size, original, transform)
    return next


def next_move_file(pgf_history, sgf_file, color):
    '''Next move from file by that color.
    >>> pgf_history = sgf_to_pgf(parse( '(;GM[1]SZ[3];B[bb];W[ba])' ))
    >>> next_move_file(pgf_history, 'sgf/test_next_move.sgf', 'black')
    (1, 0)
    >>> next_move_file(pgf_history, 'sgf/test_next_move.sgf', 'white')
    '''
    pgf_tree = sgf_to_pgf(sgf_from_file(sgf_file))
    event = next_move(pgf_history, pgf_tree)
    if color in event:
        return event[color]
    

from remote_control import upgrade
def merge_news(pgf_event):
    '''To tell the user about an SGF event,
    combine comment and news in PGF into remote control news.
    >>> pgf_tree = sgf_to_pgf(sgf_from_file('sgf/test_node_on_path.sgf'))
    >>> pgf_history = sgf_to_pgf(parse( '(;GM[1]SZ[5])' ))
    >>> event = get_node_on_any_path(pgf_history, pgf_tree)
    >>> news = merge_news(event)
    >>> news['comment_mc']['currentLabel']
    'comment'
    >>> if not news.get('option_mc').get('first_capture_mc'):
    ...     news
    >>> news['option_mc']['first_capture_mc']['currentLabel']
    'none'

    >>> pgf_history = sgf_to_pgf(parse( '(;GM[1]SZ[5];B[cc];W[bc])' ))
    >>> event = get_node_on_any_path(pgf_history, pgf_tree)
    >>> news = merge_news(event)
    >>> news['comment_mc']['currentLabel']
    'comment'
    >>> news.get('option_mc')

    >>> pgf_tree = sgf_to_pgf(sgf_from_file('sgf/test_capture_3_3.sgf'))
    >>> pgf_history = sgf_to_pgf(parse( '(;GM[1]SZ[3];B[bb])' ))
    >>> event = get_node_on_any_path(pgf_history, pgf_tree)
    >>> news = merge_news(event)
    >>> news.has_key('tutor_mc')
    True
    '''
    reply = {}
    if pgf_event.has_key('comment'):
        comment = pgf_event['comment']
        comment_news = {
            'comment_mc': {
                'currentLabel': 'comment',
                '_txt': {
                    'text': comment
                }
            }
        }
        reply = upgrade(reply, comment_news)
    if pgf_event.has_key('news'):
        news = pgf_event['news']
        reply = upgrade(reply, news)
    return reply

def get_next_events(pgf):
    '''List of events that immediately follow.
    >>> pgf = [{'comment': 'hello'}, 
    ... [{'black': (0, 0), 'comment': 'corner'}, {'white': (0, 1)}], 
    ... [{'black': (1, 0), 'comment': 'side'}, [{'white': (1, 1)}], [{'white': (2, 1)}]],
    ... [{'black': 'pass', 'comment': 'pass'}]]
    >>> from pprint import pprint
    >>> header = pgf.pop(0)
    >>> pprint(get_next_events(pgf))
    [{'black': (0, 0), 'comment': 'corner'},
     {'black': (1, 0), 'comment': 'side'},
     {'black': 'pass', 'comment': 'pass'}]
    >>> pprint(get_next_events([{}]))
    [{}]
    >>> pprint(get_next_events({}))
    [{}]
    '''
    next_events = []
    #if pgf and type([]) == type(pgf):
    #    pgf.pop(0)
    if pgf is not None:
        next = pgf
        if type([]) == type(pgf):
            next = pgf[0]
        if type([]) != type(next):
            next_events.append(next)
            return next_events
        for next in pgf:
            while type([]) == type(next):
                next = next[0]
            next_events.append(next)
    return next_events

# history of moves in Python-friendly list of dictionaries.
from board import black, white

def get_color_row_column(event):
    '''
    >>> get_color_row_column({'black':  (7, 2)})
    ('black', 7, 2)
    '''
    for color in 'black', 'white':
        if color in event:
            row, column = event.get(color)
            return color, row, column

history_marks = r'0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()-=_+[]{}<>/?'

def set_event_mark_row_column(turn, event, event_board):
    move = None
    for color in 'black', 'white':
        if color in event:
            move = event[color]
            break
    if move and 'resign' != move and 'pass' != move:
        mark = eval(color)
        event_mark = mark + history_marks[turn]
        row, column = move
        event_board[row][column] = event_mark
    return event_board

    
def history_to_text(history):
    '''9x9 text board from history of up to 80 moves.
    Does not mark hidden.
    >>> history = sgf_to_history('sgf/beginner/count_5_5.sgf')
    >>> print history_to_text(history)
      0 1 2 3 4 
    0 . . X8O9. 
    1 . . X4O5. 
    2 . . X0O1. 
    3 . . X2O3. 
    4 . . X6O7. 

    Pass and resign are not recorded.
    >>> history.append({'white':  'pass'})
    >>> history.append({'white':  'resign'})
    >>> print history_to_text(history)
      0 1 2 3 4 
    0 . . X8O9. 
    1 . . X4O5. 
    2 . . X0O1. 
    3 . . X2O3. 
    4 . . X6O7. 

    Does not support add-black, or add-white.
    >>> history = sgf_to_history('sgf/test_territory_dead_defend_gogui.sgf')
    >>> print history_to_text(history)
      0 1 2 3 4 
    0 . . . . . 
    1 . . . . . 
    2 . . . . . 
    3 . . . . . 
    4 . . . . . 
    '''
    if len(history_marks) < len(history):
        print 'history_to_text:  I only have marks for %i moves' \
                % history_marks
    event_board = []
    length = 9
    beginning = 0
    if 'size' in history[0]:
        length = history[0]['size']
        if 2 <= len(history):
            beginning = 1
        else:
            beginning = 0
    for row in range(length):
        event_board.append( ['. '] * length )
    for turn, event in enumerate(history[beginning:]):
        event_board = set_event_mark_row_column(
                turn, event, event_board)
    event_board_text = '  '
    for i in range(length):
        event_board_text += '%i ' % i
    for r, row in enumerate(event_board):
        event_board_text += '\n' + str(r) + ' ' + ''.join(row)
    return event_board_text


wallis_history_text = ''' 0 1 2 3 4 5 6 7 8 
0 XX. . . XBOAOCOEXH
1 . XD. OGXvOyXzXFXT
2 . . X2X5OwX7X1XROS
3 . . XtOYOuXlXVXnOQ
4 . . Xj. OiXhOkOmOU
5 . . X9. OcOgXbXpOq
6 XL. X0XfXdOeX3Oo. 
7 XNXJXxO8OMOaXrOs. 
8 XPOKOIOOO6. OW. . '''

from board import text_to_array, pb, doctest_board
def history_text_to_board(history_text):
    '''Convert history text of board to a board.
    >>> pb(history_text_to_board(wallis_history_text))
    X...XOOOX
    .X.OXOXXX
    ..XXOXXXO
    ..XOOXXXO
    ..X.OXOOO
    ..X.OOXXO
    X.XXXOXO.
    XXXOOOXO.
    XOOOO.O..
    '''
    board_text = ''
    for line in history_text.splitlines()[1:]:
        for i in range(2, len(line), 2):
            board_text += line[i]
        board_text += '\n'
    return text_to_array(board_text)


def sgf_file_to_board(sgf_file):
    '''Does not support add black or add white.
    >>> sgf_file_to_board('territory_dead_defend.sgf')
    sgf_from_file: file not found
    >>> add_board = sgf_file_to_board('sgf/beginner/territory_dead_defend_gogui.sgf')
    >>> print doctest_board(add_board)
    ,,,,,
    ,,,,,
    ,,,,,
    ,,,,,
    ,,,,,
    
    Actually it is more like:
    X,XO,
    ,,OOO
    OO,XX
    XXX,,
    OO,X,
    '''
    history = sgf_to_history(sgf_file)
    if history:
        history_text = history_to_text(history)
        board = history_text_to_board(history_text)
        return board

def history_to_tuple(history):
    '''Convert to tuple, which is easier to parse.
    >>> play_history = [{'black': (1, 1)}, {'white': (0, 2)}, {'black': (0, 1)}, {'white': (2, 1)}, {'black': (1, 0)}, {'white': (2, 2)}, {'black': (2, 0)}]
    >>> history_to_tuple(play_history)
    [(1, 1, 'black'), (0, 2, 'white'), (0, 1, 'black'), (2, 1, 'white'), (1, 0, 'black'), (2, 2, 'white'), (2, 0, 'black')]
    '''
    tuples = []
    for event in history:
        for color in ('black', 'white'):
            if event.get(color):
                r, c = event.get(color)
                tuples.append( (r, c, color) )
    return tuples


import code_unit
snippet = '''
# !start python code_explorer.py --snippet snippet --import smart_go_format.py
import smart_go_format; smart_go_format = reload(smart_go_format); from smart_go_format import *
# code_unit.doctest_unit(get_history)
'''

if __name__ == '__main__':
    import sys
    code_unit.test_file_args('./smart_go_format.py', sys.argv,
            locals(), globals())

