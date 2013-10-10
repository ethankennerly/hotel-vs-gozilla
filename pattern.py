#!/usr/bin/python
# -*- coding: utf-8 -*-
'''Find local patterns of black and pieces in Go.
Match Patterns
My ideas and patterns, 
mostly from experience and Learn to Play Go by Janice Kim, 
following simpler formatting conventions in GnuGo patterns.db
For example, see extra_stone_example
'''
__author__ = 'Ethan Kennerly'

from board import *



center_3_3_board_text = '''
,,,
,X,
,,,
'''
center_3_3_board = text_to_array(center_3_3_board_text)
center_3_3_pattern_text = '''
Pattern formation_center_3_3

#####
#?.?#
#.*.#
#?.?#
#####

:+,C
'''


pre_jump_board_text = '''
,,,,,,,,,
,,,,,,,,,
,,,,,,X,,
,,,,,,,,,
,,,,,,,,,
,,O,,,,,,
,,,,,,,,,
,,,,,,,,,
,,,,,,,,,
'''
pre_jump_board = text_to_array(pre_jump_board_text)
jump_board_text = '''
,,,,,,,,,
,,,,,,,,,
,,,,X,X,,
,,,,,,,,,
,,,,,,,,,
,,O,,,,,,
,,,,,,,,,
,,,,,,,,,
,,,,,,,,,
'''
jump_board = text_to_array(jump_board_text)
jump_board2_text = '''
,,,,,,,,,
,,,,,,,,,
,,,,X,X,,
,,,,X,,,,
,,,,,,,,,
,,O,,,,,,
,,,,,,,,,
,,,,,,,,,
,,,,,,,,,
'''
jump_board2 = text_to_array(jump_board2_text)
jump_pattern_text = '''
Pattern formation_jump

???
oOo
...
?*?
???

:|,C,shape(5)
'''
jump_attack_board_text = '''
,,,,,,,,,
,,,,,,,,,
,,,,O,X,,
,,,,,,,,,
,,,,,,,,,
,,O,,,,,,
,,,,,,,,,
,,,,,,,,,
,,,,,,,,,
'''
jump_attack_board = text_to_array(jump_attack_board_text)
jump_attack_board2_text = '''
,,,,,,,,,
,,,,,,,,,
,,,,O,X,,
,,,,,,X,,
,,,,,,,,,
,,O,,,,,,
,,,,,,,,,
,,,,,,,,,
,,,,,,,,,
'''
jump_attack_board2 = text_to_array(jump_attack_board2_text)
jump_attack_pattern_text = '''
Pattern formation_jump_attack

?X?
...
o*o
?o?

:|,C,shape(5)
'''

peep_board_text = '''
,,,,,,,,,
,,,,,O,,,
,,,,,,X,,
,,,,,O,,,
,,,,,,,,,
,,O,,,,,,
,,,,,,,,,
,,,,,,,,,
,,,,,,,,,
'''
peep_board = text_to_array(peep_board_text)
peep_5_5_board_text = '''
,,,,,
O,O,,
X,X,,
,OX,,
,X,,,
'''
peep_5_5_board = text_to_array(peep_5_5_board_text)
preview_peep_5_5_board_text = '''
,,,,,
,,,,,
%,X,,
,O,,,
,,,,,
'''
preview_peep_5_5_board = text_to_array(preview_peep_5_5_board_text)
fumble_peep_5_5_board_text = '''
,,,,,
,,,,,
X,X,,
,O,,,
,,,,,
'''
fumble_peep_5_5_board = text_to_array(fumble_peep_5_5_board_text)
peep_pattern_text = '''
Pattern formation_peep

ooo
X.X
?*?
???

:|,C,shape(5)
'''


cut_board_text = '''
,,,,,,,,,
,,,,,O,,,
,,,,,XX,,
,,,,,O,,,
,,,,,,,,,
,,O,,,,,,
,,,,,,,,,
,,,,,,,,,
,,,,,,,,,
'''
cut_board = text_to_array(cut_board_text)
cut_5_5_board_text = '''
,,,,,
,,,,,
XOX,,
,O,,,
,,,,,
'''
cut_5_5_board = text_to_array(cut_5_5_board_text)

cut_pattern_text = '''
Pattern formation_cut

ooo
X*X
?O?
?o?

:|,C,shape(5)
'''



jump_underneath_board_text = '''
,,,,,,,
,,,OX,,
,O,,,X,
,XXOOX,
,,OOXO,
,X,XX,X
,,,,,X,
'''
jump_underneath_board = text_to_array(jump_underneath_board_text)
jump_underneath_pattern_text = '''
Pattern formation_jump_underneath

#???
#???
#oO?
#..X
#o*?
#???

:8,C
'''


monkey_peep_board_text = '''
,O,O,
,,OXO
XOX,,
,OX,,
,,X,,
'''
monkey_peep_board = text_to_array(monkey_peep_board_text)
monkey_peep_pattern_text = '''
Pattern formation_monkey_peep

#??
#.o
#..
#*X
#oO

:8,C
'''


connect_board_text = '''
,,,,,,,,,
,,,,,,X,,
,,,,,OX,,
,,,,O,X,,
,,,,,,,,,
,,O,X,,,,
,,OX,,,,,
,,OOO,,,,
,,,,,,,,,
'''
connect_board = text_to_array(connect_board_text)
connect_pattern_text = '''
Pattern formation_connect

??X??
oO*Oo
?.x.?

:|,C,shape(5)
'''

diagonal_board_text = '''
,,,,,,,,,
,,,,,X,,,
,,,,,,X,,
,,,,,,,,,
,,,,,,,,,
,,,,,,,,,
,,,,,,,,,
,,,,,,,,,
,,,,,,,,,
'''
diagonal_board = text_to_array(diagonal_board_text)
diagonal_board2_text = '''
,,,,,,,,,
,,,,,X,,,
,,,,,,X,,
,,,,,,X,,
,,,,,,,,,
,,,,,,,,,
,,,,,,,,,
,,,,,,,,,
,,,,,,,,,
'''
diagonal_board2 = text_to_array(diagonal_board2_text)
diagonal_pattern_text = '''
Pattern formation_diagonal

?.O
?*.
???

:/,C,shape(3)
'''

michael_crawl_board_text = '''
,,,,,,,,,
,,,,,,,,,
,,XXOXXX,
,,,XXOOX,
,,XOO,,XX
,,XO,,OOX
XXOXO,,,,
XOOXO,,,,
,,,XO,,,,
'''
michael_crawl_board = text_to_array(michael_crawl_board_text)
crawl_pattern_text = '''
Pattern formation_crawl

oXO
.*o
###

:8,C
'''



diagonal_attack_board_text = '''
,,,,,,,,,
,,,,,O,,,
,,,,,,X,,
,,,,,,,,,
,X,,,,,,,
,O,,,,,,,
,,X,,,,,,
,,,,,,,,,
,,,,,,,,,
'''
diagonal_attack_board = text_to_array(diagonal_attack_board_text)
diagonal_attack_pattern_text = '''
Pattern formation_diagonal_attack
??o?
?.Xo
o*.?
?o??

:/,C,shape(3)
'''


shoulder_hit_board_text = '''
,,,,,,,
,,,,,,,
,,X,,,,
,,,,,,,
,,O,,,,
,X,,O,,
,,,,,,,
'''
shoulder_hit_board = text_to_array(shoulder_hit_board_text)
shoulder_hit_2_board_text = '''
,,,,,,,
,,O,,,,
,,,X,,,
,,,,,,,
,,,O,,,
,,X,,O,
,,,,,,,
'''
shoulder_hit_2_board = text_to_array(shoulder_hit_2_board_text)
shoulder_hit_pattern_text = '''
Pattern formation_shoulder_hit
####
????
?.X?
o*o?
?o??

:8,C
'''


perch_board_text = '''
,,,,,,,
,,,,,,,
,,X,O,,
,,,,,,,
,,O,,,,
,X,,O,,
,,,,,,,
'''
perch_board = text_to_array(perch_board_text)
perch_5_5_board_text = '''
,,,,,
,X,,,
,,O,,
,,,,,
,,,,,
'''
perch_5_5_board = text_to_array(perch_5_5_board_text)
perch_pattern_text = '''
Pattern formation_perch

#####
?????
?...?
?.*.?
??.??

:|,C
'''


diagonal_cut_half_board_text = '''
,,,,,,,,,
,,,,,,O,,
,,,,,,XO,
,,,,,,X,,
,,,,,,,,,
,,,,,,,,,
,,,,,,,,,
,,,,,,,,,
,,,,,,,,,
'''
diagonal_cut_half_board = text_to_array(diagonal_cut_half_board_text)
foolish_diagonal_cut_half_board_text = '''
,,,,,,,,,
,,,,,,O,,
,,,,,OX,,
,,,,,,,,,
,,,,,,,,,
,,,,,,,,,
,,,,,,,,,
,,,,,,,,,
,,,,,,,,,
'''
foolish_diagonal_cut_half_board = text_to_array(foolish_diagonal_cut_half_board_text)
strong_diagonal_cut_half_board_text = '''
,,,,,,,,,
,,,,,,,,,
,,,,,O,,,
,,,,,XO,,
,,,,OX,,,
,,,,XX,,,
,,O,,,,,,
OX,,,,,,,
,OO,,,,,,
'''
strong_diagonal_cut_half_board = text_to_array(strong_diagonal_cut_half_board_text)
lonely_diagonal_cut_half_board_text = '''
,,,,,,,,,
,,,,X,,,,
,,X,,XX,,
,,X,O,,,,
,OOX,,O,,
,,,O,XOX,
,,XOOOX,,
,,,OX,O,,
,X,,,,,,,
'''
lonely_diagonal_cut_half_board = text_to_array(lonely_diagonal_cut_half_board_text)

rescuing_diagonal_cut_half_board_text = '''
,,,,,,,,,
,,,,,,,,,
,,XXOXX,,
,,,XXOO,,
,,XOO,,,,
,,XO,,O,,
,,,XO,,,,
,,OX,,,,,
,,,,,,,,,
'''
rescuing_diagonal_cut_half_board = text_to_array(rescuing_diagonal_cut_half_board_text)


michael_diagonal_cut_half_board_text = '''
,,,,,,,,,
,,,,,,,,,
,,XXOXXX,
,,,XXOOX,
,,XOO,,XX
,,XO,,OOX
XXOXO,,,O
XOOXO,,,,
,,,XO,,,,
'''
michael_diagonal_cut_half_board = text_to_array(michael_diagonal_cut_half_board_text)

diagonal_cut_half_pattern_text = '''
Pattern formation_diagonal_cut_half

????
?oo?
X.o?
*X??
O???

:8,C,shape(3)
'''

peep_diagonal_board_text = '''
,,,,,,,,,
,,,,XO,,,
,,X,,XX,,
,,X,O,,,,
,,,,,,O,,
,X,X,XOX,
,,O,,,X,,
,OX,,,O,,
,,,,,,,,,
'''
peep_diagonal_board = text_to_array(peep_diagonal_board_text)
peep_diagonal_pattern_text = '''
Pattern formation_peep_diagonal

xxo?
?XOo
?.Xx
?*??
?o??

:8,C,shape(3)
'''



michael_diagonal_cut_board_text = '''
,,,,,,,,,
,,,,,,,,,
,,X,OXX,,
,,,XXO,,,
,,,,O,,,,
,,X,,,O,,
,,,,O,,,,
,,,,,,,,,
,,,,,,,,,
'''
michael_diagonal_cut_board = text_to_array(michael_diagonal_cut_board_text)

andre_diagonal_cut_board_text = '''
,,,,,,,,,
,,X,,,,,,
,,,,X,,,,
,OOOXX,,,
,X,XO,X,,
,,XX,,O,,
,,,,O,,,,
,,,X,,X,,
,,,,,,,,,
'''
andre_diagonal_cut_board = text_to_array(andre_diagonal_cut_board_text)

michael_tail_diagonal_cut_board_text = '''
,,,,,,,,,
,,,,,,,,,
,,XXOXXX,
,,,XXOO,,
,,XOO,,,,
,,XO,,O,,
,,OXO,,,,
,,OX,,,,,
,,,X,,,,,
'''
michael_tail_diagonal_cut_board = text_to_array(michael_tail_diagonal_cut_board_text)

diagonal_cut_but_tiger_yawn_board_text = '''
,,,,,
,XOO,
,OXX,
,,,,,
,,,,,
'''
diagonal_cut_but_tiger_yawn_board = text_to_array(diagonal_cut_but_tiger_yawn_board_text)

diagonal_cut_but_tiger_yawn_4_3_board_text = '''
,,,,,,,
,,,,,,,
,,,XO,,
,,,XO,,
,,XXO,,
,,XOX,,
,,,O,,,
'''
diagonal_cut_but_tiger_yawn_4_3_board = text_to_array(diagonal_cut_but_tiger_yawn_4_3_board_text)


diagonal_cut_pattern_text = '''
Pattern formation_diagonal_cut

??????
?xxoo?
?oXO??
?o*X??
??O?x?
??????

:8,C
'''



diagonal_connect_board_text = '''
,,,,,,,,,
,,,,,,,,,
,,,,OXX,,
,,,,,OX,,
,,,,,OX,,
,,,X,O,,,
,XO,,,,,,
,XXX,,,,,
,,,,,,,,,
'''
diagonal_connect_board = text_to_array(diagonal_connect_board_text)
diagonal_connect56_board_text = '''
,,,,,,,,,
,,,,X,,,,
,,X,,,X,,
,,X,O,,,,
,OO,,,O,,
,,,O,XX,,
,,XOOOX,,
,,,OX,,,,
,X,,,,,,,
'''
diagonal_connect56_board = text_to_array(diagonal_connect56_board_text)
diagonal_connect67_board_text = '''
,,,,,,,,,
,,,,X,,,,
,,X,,,X,,
,,X,O,,,,
,OO,,,O,,
,,,O,XOX,
,,XOOOXX,
,,,OX,,,,
,X,,,,,,,
'''
diagonal_connect67_board = text_to_array(diagonal_connect67_board_text)

diagonal_connect_pattern_text = '''
Pattern formation_diagonal_connect

o???
oOXx
x*Ox
xxoo

:8,C,shape(3)
'''



block_board_text = '''
,,,,,,,,,
,,,,,,,,,
,,XXOXXX,
,,,XXOOX,
,,XOO,,X,
,,XO,,OO,
,,OXO,,,,
,,OX,,,,,
,,,X,,,,,
'''
block_board = text_to_array(block_board_text)
block_5_5_board_text = '''
,,,,,
,XX,,
,,O,,
,,,,,
,,,,,
'''
block_5_5_board = text_to_array(block_5_5_board_text)


press_4_3_board_text = '''
,,,,,,,
,,,,,,,
,,,,,,,
,,,XO,,
,,,XO,,
,,X,,,,
,,,,,,,
'''
press_4_3_board = text_to_array(press_4_3_board_text)

block_pattern_text = '''
Pattern formation_block

??X.
?O*.
?...

:8,C
'''
#??X.
#?O*.
#?...
#????

press_pattern_text = '''
Pattern formation_press

o...
o?X.
?O*.
?..?
????

:8,C
'''

tiger_mouth_board_text = '''
,,,,,,,,,
,,,,X,X,,
,XO,OX,,,
,,XO,OX,,
,XO,,OX,,
,,,X,O,,,
XO,,,,,,,
,XXX,,,,,
X,,,,,,,,
'''
tiger_mouth_board = text_to_array(tiger_mouth_board_text)

ezra_tiger_mouth_board_text = '''
,O,,,
,,OX,
XOX,,
,OX,,
,,,,,
'''
ezra_tiger_mouth_board = text_to_array(ezra_tiger_mouth_board_text)

andre_tiger_mouth_board_text = '''
,,,,,,,,,
,,X,,,,,,
,,,XX,,,,
,OOOOX,,,
,X,XO,X,,
,,XXOXO,,
,,,,OX,,,
,,,X$,X,,
,,,,,,,,,
'''
andre_tiger_mouth_board = text_to_array(andre_tiger_mouth_board_text)


tiger_mouth_pattern_text = '''
Pattern formation_tiger_mouth

???
xOx
*.O
o.?

:8,C,shape(3)
'''

tiger_jaw_pattern_text = '''
Pattern formation_tiger_jaw

?x?
x*x
O.O
o.?

:|,C,shape(3)
'''


danger_tiger_mouth_pattern_text = '''
Pattern formation_danger_tiger_mouth

?X?
XOX
*.O
?.?

:8,C,shape(3)
'''

danger_tiger_jaw_pattern_text = '''
Pattern formation_danger_tiger_jaw

?X?
X*X
O.O
o.?

:8,C,shape(3)
'''


knight_board_text = '''
,,,,,,,,,
,,,,,,,,,
,,,,,,X,,
,,,,X,,,,
,,,,,,,X,
,,,,,,,,,
,,,,,,,,,
,,,,,,,,,
,,,,,,,,,
'''
knight_board = text_to_array(knight_board_text)
knight_pattern_text = '''
Pattern formation_knight

????
?oO?
?..o
?*.o
????

:8,C,shape(4)
'''


andre_knight_underneath_board_text = '''
,,,,,,,,,
,,X,,,,,,
,,,,X,,,,
,XO,,,,,,
,X,,O,X,,
,,X,,,O,,
,,,,O,,,,
,,,X,,X,,
,,,,,,,,,
'''
andre_knight_underneath_board = text_to_array(andre_knight_underneath_board_text)
knight_underneath_pattern_text = '''
Pattern formation_knight_underneath

#ooO?
#o..?
#o*??
#????

:8,C
'''

knight_attack_board_text = '''
,,,,,,,,,
,,,,,,,,,
,,,,,,X,,
,,,,O,,,,
,,,,,,,O,
,,,,,,,,,
,,,,,,,,,
,,,,,,,,,
,,,,,,,,,
'''
knight_attack_board = text_to_array(knight_attack_board_text)
knight_attack_pattern_text = '''
Pattern formation_knight_attack

?xX.
?..o
o*.o
?o??

:8,C,shape(4)
'''

andre_chariot_attack_board_text = '''
,,,,,,,,,
,,X,,,,,,
,,,,X,,,,
,OO,,,,,,
,X,,O,X,,
,,X,,,O,,
,,,,O,,,,
,,,X,,X,,
,,,,,,,,,
'''
andre_chariot_attack_board = text_to_array(andre_chariot_attack_board_text)
chariot_attack_pattern_text = '''
Pattern formation_chariot_attack

?xX?
?..o
o*Oo
????

:8,C
'''

peep_knight_board_text = '''
,,,,,,,,,
,,,,,,,,,
,,X,,,X,,
,,,,O,,,,
,O,,,,O,,
,,,O,,,,,
,,X,,,X,,
,,,,X,,,,
,,,,,,,,,
'''
peep_knight_board = text_to_array(peep_knight_board_text)
peep_knight_pattern_text = '''
Pattern formation_peep_knight

??xX?
o*..o
??X.o
?????

:8,C,shape(4)
'''

knight_cut_half_board_text = '''
,,,,,,,,,
,,,,,,,,,
,,X,,,X,,
,,,,O,,,,
,O,,,,O,,
,,,O,,,,,
,,XO,,X,,
,,,,X,,,,
,,,,,,,,,
'''
knight_cut_half_board = text_to_array(knight_cut_half_board_text)
knight_cut_half_pattern_text = '''
Pattern formation_knight_cut_half

?xX
O*.
?X.
???

:8,C,shape(4)
'''

kyung_knight_cut_half_board = text_to_array('''
,,,,,,,,,
,,,,,,,,,
,,,,$,,,,
,,,,O,,,,
,,,XO,,,,
,,,X,,,,,
,,,,,,,,,
,,,,,,,,,
,,,,,,,,,
''')
knight_cut_half2_pattern_text = '''
Pattern formation_knight_cut_half2

???
?OX
o*.
?X.
???

:8,C,shape(4)
'''


leap_board_text = '''
,,,,,,,,,
,,,,,,,,,
,,,X,,X,,
,,,,,,,,,
,,,,,,,,,
,,O,,,,,,
,,,,,,,,,
,,,,,,,,,
,,,,,,,,,
'''
leap_board = text_to_array(leap_board_text)
leap_pattern_text = '''
Pattern formation_leap

???
oOo
...
...
?*?
???

:|,C,shape(5)
'''
leap_attack_board_text = '''
,,,,,,,,,
,,,,,,,,,
,,,O,,X,,
,,,,,,,,,
,,,,,,,,,
,,O,,,,,,
,,,,,,,,,
,,,,,,,,,
,,,,,,,,,
'''
leap_attack_board = text_to_array(leap_attack_board_text)
leap_attack_pattern_text = '''
Pattern formation_leap_attack

?X?
...
...
o*o
?o?

:|,C,shape(5)
'''

high_perch_board_text = '''
,,,,,,,
,,,,,,,
,,,,,,,
,,,X,,,
,,,,,,,
,,,,,,,
,,,,,,,
'''
high_perch_board = text_to_array(high_perch_board_text)
high_perch_pattern_text = '''
Pattern formation_high_perch

#######
???????
??...??
?.....?
?..*..?
?.....?
???????
???????

:|,C
'''



quarter_field_board_text = '''
,,,,,,,,,
,,,,,,,,,
,,,,O,X,,
,,,,,,,,,
,,,,,,O,,
,,O,,,,,,
,,,X,,,,,
,,,,,,,,,
,,,,,,,,,
'''
quarter_field_board = text_to_array(quarter_field_board_text)
quarter_field_pattern_text = '''
Pattern formation_quarter_field

?...?
?...?
?o*o?
??.??

:|,C,shape(8)
'''

field_board_text = '''
,,,,,,,,,
,,,,,,,,,
,,,,,,X,,
,,,,,,,,,
,,,O,,,,,
,,,,,,,,,
,,,,,,,,,
'''
field_board = text_to_array(field_board_text)
field_pattern_text = '''
Pattern formation_field

.....
.....
..*..
.....
.....

:+,C,shape(15)
'''


fence_pattern_text = '''
Pattern formation_fence

??X.
?O*o
?...
?...

:8,C
'''

tiger_lick_pattern_text = '''
Pattern formation_tiger_lick

???
o.o
*X.
oO?
???

:8,A
'''

open_tiger_yawn_board = text_to_array('''
,,,,,
,,X,,
,XO,,
,,,,,
,,,,,
''')
open_tiger_yawn_pattern_text = '''
Pattern formation_open_tiger_yawn

###
o.o
*..
XO?
???

:8,A
'''

ezra_tiger_yawn_board_text = '''
,,,,,
,,OX,
XOX,,
,OX,,
,,,,,
'''
ezra_tiger_yawn_board = text_to_array(ezra_tiger_yawn_board_text)

mathijs_tiger_yawn_board_text = '''
,,,,,,,,,
,,,,,,,,,
,,X,OOX,,
,,,,OXX,,
,,XO,OXO,
,,O,,O,X,
,,X,O,XO,
,,,OX,,,,
,,,,,,,,,
'''
mathijs_tiger_yawn_board = text_to_array(mathijs_tiger_yawn_board_text)

tiger_yawn_pattern_text = '''
Pattern formation_tiger_yawn

###
o.o
*X.
oO?
???

:8,A
'''


tiger_chomp_board_text = '''
,,,,,
,,OXO
,,XO,
,,OX,
,,,O,
'''
tiger_chomp_board = text_to_array(tiger_chomp_board_text)
tiger_chomp_pattern_text = '''
Pattern formation_tiger_chomp

###
o.o
*XO
?O?

:8,A
'''

tiger_chomp_3_1_board_text = '''
,,,,,
,OXX,
,OX,X
,XOX,
,,,O,
'''
tiger_chomp_3_1_board = text_to_array(tiger_chomp_3_1_board_text)

marc_cut_self_3_5_board_text = '''
,,,,,,,
,,,,,,,
,,,,,,,
,,,XOX,
,,,,O,,
,,X,,,,
,,,,,,,
'''
marc_cut_self_3_5_board = text_to_array(marc_cut_self_3_5_board_text)

territory_dead_defend_board = text_to_array('''
X,XO,
,XOOO
OO,X,
XXX,,
OO,X,
''')

territory_dead_defend_7_7_board = text_to_array('''
,OX,X,X
O,O,XX,
OOOOOOO
OXXXXX,
OX,,,,,
XX,,,,,
,X,,,,,
''')


from smart_go_format import history_to_text, get_color_row_column

def territory_dead_defend_example():
    r'''Kyung previews letting white cut him apart.
    >>> pattern_dictionary = get_pattern_dictionary(pattern_texts)

    Match pattern even for dead stone.
    >>> get_matches(pattern_dictionary,
    ...     territory_dead_defend_board, 1, 1)
    [['formation_diagonal', 'rotate_270']]

    Match pattern even for dead stone.
    >>> get_matches(pattern_dictionary,
    ...     territory_dead_defend_7_7_board, 1, 5)
    [['formation_diagonal', 'rotate_0']]
    '''

# eye pattern
eye_line_3_board_text = '''
,,,,,
,,,,,
OOOOO
XXXXO
,O,XO
'''
eye_line_3_board = text_to_array(eye_line_3_board_text)
eye_line_3_pattern_text = '''
Pattern formation_eye_line_3

#XXXX
#.*.X
#####

:8,A
'''


# End of patterns and examples



# Pattern matching


pattern_mark_dictionary = {
        'X':  enemy,
        'O':  ally,
        # if i don't write an example that requires the code, and i don't write the code, then all code has an example.
        '?':  are_we_on_board,
        '.':  am_i_empty_but_not_you,
        '*':  identical,
        'o':  ally_or_empty,
        'x':  enemy_or_empty,
        '#':  am_i_off_board_but_not_you,
        #' ':  are_we_on_board,  # if space is preserved.
    }


no_symmetry_rotates = ['rotate_0', 'rotate_90', 
    'rotate_180', 'rotate_270', 
    'row_reflect_rotate_0', 'row_reflect_rotate_90', 
    'row_reflect_rotate_180', 'row_reflect_rotate_270']

axis_1_rotates = ['rotate_0', 'rotate_90', 
    'rotate_180', 'rotate_270']

cross_rotates = ['rotate_0']

symmetry_rotates = {
        '|':  axis_1_rotates,
        '-':  axis_1_rotates,
        '/':  axis_1_rotates,
        '+':  cross_rotates,
        '8':  no_symmetry_rotates,
        }



def get_rotates(symmetry):
    if symmetry not in symmetry_rotates:
            print 'get_rotates:  Am I prepared to transform along this symmetry %s' % symmetry
    rotates = symmetry_rotates.get(symmetry, [])
    return rotates



def get_matches(pattern_dictionary, 
        board, last_row, last_column):
    r'''Useful for last or next position.
    >>> pattern_dictionary = get_pattern_dictionary(pattern_texts)
    >>> history = [{'black': (2, 6)}, 
    ...     {'white': (5, 2)}, 
    ...     {'black': (2, 4)}]
    >>> print history_to_text(history)
      0 1 2 3 4 5 6 7 8 
    0 . . . . . . . . . 
    1 . . . . . . . . . 
    2 . . . . X2. X0. . 
    3 . . . . . . . . . 
    4 . . . . . . . . . 
    5 . . O1. . . . . . 
    6 . . . . . . . . . 
    7 . . . . . . . . . 
    8 . . . . . . . . . 
    >>> last_event = history[-1]
    >>> get_color_row_column(last_event)
    ('black', 2, 4)
    >>> last_color, last_row, last_column = \
    ...     get_color_row_column(last_event)
    >>> matches = get_matches(pattern_dictionary,
    ...       jump_board,  last_row,   last_column)
    >>> if not ['formation_jump', 'rotate_90'] in matches:  matches

    >>> matches = get_matches(pattern_dictionary, jump_board, 2, 4)
    >>> if not ['formation_jump', 'rotate_90'] in matches:  matches
    >>> get_matches(pattern_dictionary, jump_board, 2, 2)
    []
    >>> get_matches(pattern_dictionary, jump_board, 5, 4)
    []
    >>> get_matches(pattern_dictionary, jump_board, 2, 8)
    []
    >>> get_matches(pattern_dictionary, jump_board, 5, 8)
    []
    >>> get_matches(pattern_dictionary, jump_board, 2, 0)
    []
    >>> get_matches(pattern_dictionary, jump_board, 5, 0)
    []
    >>> matches = get_matches(pattern_dictionary, pre_jump_board, 2, 6)
    >>> get_matches(pattern_dictionary, pre_jump_board, 2, 5)
    []
    >>> get_matches(pattern_dictionary, pre_jump_board, 2, 4)
    []

    Match knight
    >>> matches = get_matches(pattern_dictionary, knight_board, 2, 6) 
    >>> if not ['formation_knight', 'row_reflect_rotate_0'] in matches or not ['formation_knight', 'row_reflect_rotate_90'] in matches:  matches

    Match knight_underneath
    >>> 'formation_knight_underneath' in pattern_dictionary.keys()
    True
    >>> matches = get_matches(pattern_dictionary, andre_knight_underneath_board, 3, 1) 
    >>> if not ['formation_knight_underneath', 'rotate_0'] in matches:  matches

    Match knight_peep
    >>> matches = get_matches(pattern_dictionary, peep_knight_board, 5, 3) 
    >>> if not ['formation_peep_knight', 'rotate_90'] in matches:  matches

    Match knight_cut_half
    >>> matches = get_matches(pattern_dictionary, knight_cut_half_board, 6, 3) 
    >>> if not ['formation_knight_cut_half', 'rotate_90'] in matches:  matches

    Match diagonal
    >>> matches = get_matches(pattern_dictionary, diagonal_board,  
    ...     2, 6)
    >>> if not ['formation_diagonal', 'rotate_270'] in matches:  matches
    
    Match optional diagonal
    >>> matches = get_matches(pattern_dictionary, diagonal_board2,  
    ...     2, 6)
    >>> if not ['formation_diagonal', 'rotate_270'] in matches:  matches
    
    Match crawl
    >>> matches = get_matches(pattern_dictionary, michael_crawl_board,  
    ...     5, 8)
    >>> if not ['formation_crawl', 'rotate_270'] in matches:  matches
    
    Match diagonal_attack
    >>> matches = get_matches(pattern_dictionary, diagonal_attack_board,  
    ...     2, 6)
    >>> if not ['formation_diagonal_attack', 'rotate_270'] in matches:  matches
    
    Match diagonal_attack
    >>> 'formation_diagonal_attack' in pattern_dictionary.keys()
    True
    >>> matches = get_matches(pattern_dictionary, diagonal_attack_board,  
    ...     6, 2)
    >>> if not ['formation_diagonal_attack', 'rotate_270'] in matches:  matches
    
    Match shoulder_hit
    >>> 'formation_shoulder_hit' in pattern_dictionary.keys()
    True
    >>> matches = get_matches(pattern_dictionary, shoulder_hit_board,  
    ...     4, 2)
    >>> if not ['formation_shoulder_hit', 'rotate_180'] in matches:  matches
    >>> matches = get_matches(pattern_dictionary, shoulder_hit_board,  
    ...     5, 1)
    >>> if ['formation_shoulder_hit', 'rotate_0'] in matches:  matches
    >>> matches = get_matches(pattern_dictionary, shoulder_hit_2_board,  
    ...     4, 3)
    >>> if not ['formation_shoulder_hit', 'rotate_180'] in matches:  matches
    >>> matches = get_matches(pattern_dictionary, shoulder_hit_2_board,  
    ...     2, 3)
    >>> if not ['formation_shoulder_hit', 'row_reflect_rotate_180'] in matches:  matches
    
    Match perch
    >>> 'formation_perch' in pattern_dictionary.keys()
    True
    >>> matches = get_matches(pattern_dictionary, perch_board,  
    ...     2, 4)
    >>> if not ['formation_perch', 'rotate_0'] in matches:  matches
    >>> if not ['formation_perch', 'rotate_90'] in matches:  matches
    >>> matches = get_matches(pattern_dictionary, perch_board,  
    ...     4, 2)
    >>> if ['formation_perch', 'rotate_180'] in matches:  matches
    >>> if ['formation_perch', 'rotate_270'] in matches:  matches
    >>> matches = get_matches(pattern_dictionary, perch_5_5_board,  
    ...     2, 2)
    >>> if not ['formation_perch', 'rotate_90'] in matches:  matches
    >>> if not ['formation_perch', 'rotate_180'] in matches:  matches

    do not match diagonal_cut_half on second line
    >>> matches = get_matches(pattern_dictionary, diagonal_cut_half_board,  
    ...     2, 6)
    >>> if ['formation_diagonal_cut_half', 'rotate_0'] in matches:  matches
    
    Match strong diagonal_cut_half
    >>> matches = get_matches(pattern_dictionary, strong_diagonal_cut_half_board,  
    ...     3, 5)
    >>> if not ['formation_diagonal_cut_half', 'rotate_0'] in matches:  matches
    
    Match foolish diagonal_cut_half
    >>> matches = get_matches(pattern_dictionary, foolish_diagonal_cut_half_board,  
    ...     2, 6)
    >>> ## if not ['formation_diagonal_cut_half', 'rotate_270'] in matches:  matches
    >>> if 'formation_diagonal_cut_half' in [form for form, rote in matches]:  matches
    
    Do not match lonely diagonal_cut_half
    >>> matches = get_matches(pattern_dictionary, lonely_diagonal_cut_half_board,  
    ...     4, 3)
    >>> if 'formation_diagonal_cut_half' in [form for form, rote in matches]:  matches
    
    Match rescuing diagonal_cut_half
    >>> matches = get_matches(pattern_dictionary, rescuing_diagonal_cut_half_board,  
    ...     5, 3)
    >>> if not 'formation_diagonal_cut_half' in [form for form, rote in matches]:  matches
    
    Match michael diagonal_cut_half
    >>> matches = get_matches(pattern_dictionary, michael_diagonal_cut_half_board,  
    ...     5, 8)
    >>> if not 'formation_diagonal_cut_half' in [form for form, rote in matches]:  matches

    Does not match alternates.
    >>> matches = get_matches(pattern_dictionary, michael_diagonal_cut_half_board,  
    ...     4, 8)
    >>> if 'formation_diagonal_cut_half' in [form for form, rote in matches]:  matches
    
    Match peep_diagonal
    >>> matches = get_matches(pattern_dictionary, peep_diagonal_board,  
    ...     3, 4)
    >>> if not ['formation_peep_diagonal', 'rotate_0'] in matches:  matches
    >>> matches = get_matches(pattern_dictionary, peep_diagonal_board,  
    ...     5, 1)
    >>> if not ['formation_peep_diagonal', 'row_reflect_rotate_0'] in matches:  matches
    
    Match michael diagonal_cut
    >>> matches = get_matches(pattern_dictionary, michael_diagonal_cut_board,  
    ...     2, 5)
    >>> if not 'formation_diagonal_cut' in [form for form, rote in matches]:  matches
    
    Match andre diagonal_cut
    >>> matches = get_matches(pattern_dictionary, andre_diagonal_cut_board,  
    ...     3, 4)
    >>> if not 'formation_diagonal_cut' in [form for form, rote in matches]:  matches
    
    Match michael_tail diagonal_cut
    >>> matches = get_matches(pattern_dictionary, michael_tail_diagonal_cut_board,  
    ...     6, 2)
    >>> if not 'formation_diagonal_cut' in [form for form, rote in matches]:  matches
    
    Does not match diagonal_cut_but_tiger_yawn
    >>> matches = get_matches(pattern_dictionary, diagonal_cut_but_tiger_yawn_board,  
    ...     1, 2)
    >>> if 'formation_diagonal_cut' in [form for form, rote in matches]:  matches

    Does not match diagonal_cut_but_tiger_yawn_4_3
    >>> matches = get_matches(pattern_dictionary, diagonal_cut_but_tiger_yawn_4_3_board,  
    ...     4, 3)
    >>> if 'formation_diagonal_cut' in [form for form, rote in matches]:  matches
    
    Match diagonal_connect
    >>> matches = get_matches(pattern_dictionary, diagonal_connect_board,  
    ...     2, 6)
    >>> if not ['formation_diagonal_connect', 'rotate_180'] in matches:  matches
    
    Match diagonal_connect
    >>> matches = get_matches(pattern_dictionary, diagonal_connect56_board,  
    ...     5, 6)
    >>> if not ['formation_diagonal_connect', 'rotate_180'] in matches:  matches
    
    Match diagonal_connect
    >>> matches = get_matches(pattern_dictionary, diagonal_connect67_board,  
    ...     6, 7)
    >>> if not ['formation_diagonal_connect', 'rotate_270'] in matches:  matches
    
    Match block
    >>> 'formation_block' in pattern_dictionary.keys()
    True
    >>> matches = get_matches(pattern_dictionary, block_board,  
    ...     5, 7)
    >>> if not ['formation_block', 'rotate_0'] in matches:
    ...     matches
    >>> matches = get_matches(pattern_dictionary, andre_chariot_attack_board,  
    ...     3, 1)
    >>> if not ['formation_block', 'rotate_180'] in matches:
    ...     matches
    >>> matches = get_matches(pattern_dictionary, block_5_5_board,  
    ...     1, 2)
    >>> if not ['formation_block', 'row_reflect_rotate_0'] in matches:
    ...     matches

    Match press
    >>> matches = get_matches(pattern_dictionary, press_4_3_board,  
    ...     4, 3)
    >>> if not ['formation_press', 'rotate_90'] in matches:
    ...     matches
    
    Match tiger_mouth
    >>> matches = get_matches(pattern_dictionary, tiger_mouth_board,  
    ...     1, 6)
    >>> if not ['formation_tiger_mouth', 'row_reflect_rotate_90'] in matches:  matches

    Match tiger_mouth in example game that Ezra played.
    >>> matches = get_matches(pattern_dictionary, ezra_tiger_mouth_board,  
    ...     0, 1)
    >>> if not ['formation_tiger_mouth', 'rotate_90'] in matches:  matches

    Match tiger_mouth in example game that Andre played.
    >>> matches = get_matches(pattern_dictionary, andre_tiger_mouth_board,  
    ...     7, 4)
    >>> if not ['formation_tiger_mouth', 'rotate_0'] in matches:  matches

    Match tiger_jaw
    >>> matches = get_matches(pattern_dictionary, tiger_mouth_board,  
    ...     2, 5)
    >>> if not ['formation_tiger_jaw', 'rotate_270'] in matches:  matches

    Match optional jump
    >>> matches = get_matches(pattern_dictionary, jump_board2,  
    ...     2, 6) # doctest: +NORMALIZE_WHITESPACE
    >>> if not ['formation_jump', 'rotate_270'] in matches:  matches

    Match jump_attack
    >>> matches = get_matches(pattern_dictionary, jump_attack_board,  
    ...     2, 6) # doctest: +NORMALIZE_WHITESPACE
    >>> if not ['formation_jump_attack', 'rotate_270'] in matches:
    ...     matches

    Match optional jump_attack
    >>> matches = get_matches(pattern_dictionary, jump_attack_board2,  
    ...     2, 6) # doctest: +NORMALIZE_WHITESPACE
    >>> if not ['formation_jump_attack', 'rotate_270'] in matches:
    ...     matches

    Match peep
    >>> matches = get_matches(pattern_dictionary, peep_board,  
    ...     2, 6)
    >>> if not ['formation_peep', 'rotate_270'] in matches:
    ...     matches
    >>> matches = get_matches(pattern_dictionary, peep_5_5_board,  
    ...     3, 1)
    >>> if not ['formation_peep', 'rotate_0'] in matches:
    ...     matches
    >>> matches = get_matches(pattern_dictionary, fumble_peep_5_5_board,  
    ...     3, 1)
    >>> if not ['formation_peep', 'rotate_0'] in matches:
    ...     matches

    Match cut
    >>> matches = get_matches(pattern_dictionary, cut_board,  
    ...     2, 5)
    >>> if not ['formation_cut', 'rotate_270'] in matches:
    ...     matches

    Match cut
    >>> matches = get_matches(pattern_dictionary, cut_5_5_board,  
    ...     2, 1)
    >>> if not ['formation_cut', 'rotate_0'] in matches:
    ...     matches

    Match connect
    >>> matches = get_matches(pattern_dictionary, connect_board,  
    ...     2, 6)
    >>> if not ['formation_connect', 'rotate_270'] in matches:
    ...     matches
    >>> matches = get_matches(pattern_dictionary, connect_board,  
    ...     6, 2)
    >>> if not ['formation_connect', 'rotate_90'] in matches:
    ...     matches

    Match jump_underneath
    >>> 'formation_jump_underneath' in pattern_dictionary.keys()
    True
    >>> matches = get_matches(pattern_dictionary, jump_underneath_board,  
    ...     5, 1)
    >>> if not ['formation_jump_underneath', 'rotate_0'] in matches:
    ...     matches
    >>> matches = get_matches(pattern_dictionary, jump_underneath_board,  
    ...     3, 1)

    Jump underneath is not safe from corner where opponent can pin or double cut.
    >>> if ['formation_jump_underneath', 'row_reflect_rotate_0'] in matches:
    ...     matches

    Match monkey_peep
    >>> 'formation_monkey_peep' in pattern_dictionary.keys()
    True
    >>> matches = get_matches(pattern_dictionary, monkey_peep_board,  
    ...     1, 4)
    >>> if not ['formation_monkey_peep', 'rotate_180'] in matches:
    ...     matches

    Match knight_attack
    >>> matches = get_matches(pattern_dictionary, knight_attack_board, 2, 6)
    >>> if not ['formation_knight_attack', 'row_reflect_rotate_0'] in matches or not ['formation_knight_attack', 'row_reflect_rotate_90'] in matches:
    ...     matches
    
    Match chariot_attack
    >>> 'formation_chariot_attack' in pattern_dictionary.keys()
    True
    >>> matches = get_matches(pattern_dictionary, andre_chariot_attack_board, 3, 1)
    >>> if not ['formation_chariot_attack', 'rotate_0'] in matches:
    ...     matches
    
    Match leap
    >>> matches = get_matches(pattern_dictionary, leap_board,  
    ...     2, 6) # doctest: +NORMALIZE_WHITESPACE
    >>> if not ['formation_leap', 'rotate_270'] in matches:
    ...     matches

    Match leap_attack
    >>> matches = get_matches(pattern_dictionary, leap_attack_board,  
    ...     2, 6) # doctest: +NORMALIZE_WHITESPACE
    >>> if not ['formation_leap_attack', 'rotate_270'] in matches:
    ...     matches

    Match field
    >>> matches = get_matches(pattern_dictionary, field_board, 2, 6)
    >>> if not ['formation_field', 'rotate_0'] in matches:
    ...     matches

    Match quarter_field
    >>> 'formation_quarter_field' in pattern_dictionary.keys()
    True
    >>> matches = get_matches(pattern_dictionary, quarter_field_board, 2, 6)
    >>> if not ['formation_quarter_field', 'rotate_0'] in matches:
    ...     matches
    >>> if not ['formation_quarter_field', 'rotate_90'] in matches:
    ...     matches

    Match high_perch
    >>> 'formation_high_perch' in attack_pattern_dictionary.keys()
    True
    >>> matches = get_matches(pattern_dictionary, high_perch_board, 3, 3)
    >>> if not ['formation_high_perch', 'rotate_0'] in matches:
    ...     matches

    #DEPRECATED, patterns not taught on 3x3.
    #Match center_3_3
    #>>> 'formation_center_3_3' in attack_pattern_dictionary.keys()
    #True
    #>>> matches = get_matches(pattern_dictionary, center_3_3_board, 1, 1)
    #>>> if not ['formation_center_3_3', 'rotate_0'] in matches:
    #...     matches

    Match fence
    >>> 'formation_fence' in pattern_dictionary.keys()
    True
    >>> matches = get_matches(pattern_dictionary, quarter_field_board, 2, 6)
    >>> if ['formation_fence', 'rotate_0'] in matches:
    ...     matches
    >>> matches = get_matches(pattern_dictionary, block_board, 5, 7)
    >>> if not ['formation_fence', 'rotate_0'] in matches:
    ...     matches
    >>> matches = get_matches(pattern_dictionary, andre_chariot_attack_board, 3, 1)
    >>> if ['formation_fence', 'rotate_180'] in matches:
    ...     matches

    Match open_tiger_yawn
    >>> matches = get_matches(pattern_dictionary, open_tiger_yawn_board, 2, 1)
    >>> if not ['formation_open_tiger_yawn', 'rotate_270'] in matches:
    ...     matches
    
    Match tiger_lick
    >>> matches = get_matches(pattern_dictionary, open_tiger_yawn_board, 2, 1)
    >>> if not ['formation_tiger_lick', 'row_reflect_rotate_0'] in matches:
    ...     matches

    Match tiger_yawn
    >>> matches = get_matches(pattern_dictionary, ezra_tiger_yawn_board, 1, 3)
    >>> if not ['formation_tiger_yawn', 'row_reflect_rotate_180'] in matches:
    ...     matches
    >>> matches = get_matches(pattern_dictionary, mathijs_tiger_yawn_board, 7, 3)
    >>> if not ['formation_tiger_yawn', 'row_reflect_rotate_0'] in matches:
    ...     matches
    >>> matches = get_matches(pattern_dictionary, mathijs_tiger_yawn_board, 5, 2)
    >>> names = [name for name, rote in matches]
    >>> if 'formation_tiger_yawn' in names:
    ...     matches
    >>> matches = get_matches(pattern_dictionary, mathijs_tiger_yawn_board, 5, 7)
    >>> if not ['formation_tiger_yawn', 'rotate_90'] in matches:
    ...     matches
    >>> if not ['formation_tiger_yawn', 'row_reflect_rotate_270'] in matches:
    ...     matches

    Match tiger_chomp
    >>> matches = get_matches(pattern_dictionary, tiger_chomp_board, 1, 2)
    >>> if not ['formation_tiger_chomp', 'rotate_0'] in matches:
    ...     matches
    >>> if ['formation_tiger_chomp', 'row_reflect_rotate_270'] in matches:
    ...     matches
    >>> matches = get_matches(pattern_dictionary, tiger_chomp_board, 1, 2)
    >>> if not ['formation_tiger_chomp', 'rotate_0'] in matches:
    ...     matches

    Beware:  Even if any stone is in danger, still matches.
    >>> matches = get_matches(pattern_dictionary, tiger_chomp_board, 4, 3)
    >>> names = [name for name, rote in matches]
    >>> if not 'formation_tiger_chomp' in names:
    ...     matches

    Match eye_line_3
    >>> 'formation_eye_line_3' in eye_pattern_dictionary.keys()
    True
    >>> matches = get_matches(eye_pattern_dictionary, eye_line_3_board, 4, 1)
    >>> if not ['formation_eye_line_3', 'rotate_0'] in matches:
    ...     matches
    '''
    matches = []
    for name, transformations in pattern_dictionary.items():
        rotates = get_rotates(transformations['symmetry'])
        for rotate in rotates:
            match_marks = transformations[rotate]['match']
            origin_row, origin_column = transformations[rotate]['origin']
            if is_exact_match(match_marks, 
                    origin_row, origin_column,
                    board,  last_row,   last_column):
                matches.append([name, rotate])
    return matches


def get_ally_offset_matches(pattern_dictionary, 
        board, last_row, last_column):
    r'''Useful for last or next position.
    >>> pattern_dictionary = get_pattern_dictionary(pattern_texts)

    Does not match alternates.
    Only if no match at position with any rotation, 
    match alternate stone of diagonal_cut_half
    Only returns first alternate match.
    >>> matches = get_matches(pattern_dictionary, michael_diagonal_cut_half_board,  
    ...     4, 8)
    >>> if 'formation_diagonal_cut_half' in [form for form, rote in matches]:  matches
    >>> rc_matches = get_ally_offset_matches(pattern_dictionary, michael_diagonal_cut_half_board,  
    ...     4, 8)
    >>> if not 'formation_diagonal_cut_half' in [form for form, rote in rc_matches.get( (5, 8), [])]:  rc_matches
    '''
    rc_matches = {}
    for name, transformations in pattern_dictionary.items():
        rotates = get_rotates(transformations['symmetry'])
        matched_alternate = False
        for rotate in rotates:
            match_marks = transformations[rotate]['match']
            ally_offsets = transformations[rotate]['ally_offsets']
            origin_row, origin_column = transformations[rotate]['origin']
            for r, c in ally_offsets:
                alternate_row = last_row + r
                alternate_column = last_column + c
                if in_bounds(board, alternate_row, alternate_column):
                    if is_exact_match(match_marks, 
                            origin_row, origin_column,
                            board,  alternate_row,   alternate_column):
                        rc_matches[(alternate_row, alternate_column)] = \
                                [[name, rotate]]
                        matched_alternate = True
                        break
            if matched_alternate:
                break
    return rc_matches



def find_allies_in_danger(board, row, column):
    '''List coordinates that are same color with only one liberty left.
    >>> emergencies = find_allies_in_danger(tiger_chomp_board, 4, 3)
    >>> print text_mask(emergencies, grid = tiger_chomp_board)
    ,,,,,
    ,,OXO
    ,,X#,
    ,,OX,
    ,,,O,
    >>> emergencies = find_allies_in_danger(tiger_chomp_board, 3, 3)
    >>> print text_mask(emergencies, grid = tiger_chomp_board)
    ,,,,,
    ,,O#O
    ,,#O,
    ,,O#,
    ,,,O,
    '''
    dangers = find_danger(board)
    mark = board[row][column]
    is_color = see_same_color(mark)
    allies_in_danger = [(r, c) for r, c in dangers 
        if is_color(board[r][c])]
    return allies_in_danger


ally_danger = '!'

def get_valid_matches(pattern_dictionary, board, last_row, last_column):
    '''Does not match cells in danger.
    Matches not cancelled in a dictionary of row, column.
    >>> rc_matches = get_valid_matches(pattern_dictionary, tiger_mouth_board,  
    ...     2, 1)
    >>> rc_matches
    {}
    >>> at_2_1 = rc_matches.get((2, 1))
    >>> if at_2_1 and 'formation_tiger_mouth' in [form for form, rote in at_2_1]:  rc_matches

    >>> rc_matches = get_valid_matches(pattern_dictionary, tiger_chomp_board, 4, 3)
    >>> matches = rc_matches.get((4, 3), [])
    >>> names = [name for name, rote in matches]
    >>> if 'formation_tiger_chomp' in names:
    ...     matches
    
    Does not match alternates.
    Only if no match at position with any rotation, 
    match alternate stone of diagonal_cut_half
    Only returns first alternate match.
    >>> matches = get_matches(pattern_dictionary, michael_diagonal_cut_half_board,  
    ...     4, 8)
    >>> if 'formation_diagonal_cut_half' in [form for form, rote in matches]:  matches
    >>> rc_matches = get_valid_matches(pattern_dictionary, michael_diagonal_cut_half_board,  
    ...     4, 8)
    >>> if not 'formation_diagonal_cut_half' in [form for form, rote in rc_matches.get( (5, 8), [])]:  rc_matches
    '''
    emergencies = find_allies_in_danger(board, last_row, last_column)
    emergency_board = map_at_position(lambda i: ally_danger, 
        board, emergencies)
    matches = get_matches(pattern_dictionary, 
        emergency_board, last_row, last_column)
    #- cancel_matches(matches, pattern_cancels)
    if matches:
        row_column_matches = {(last_row, last_column): matches}
    else:
        row_column_matches = get_ally_offset_matches(pattern_dictionary, 
            emergency_board, last_row, last_column)
    return row_column_matches


def get_info_sequence_news_2_2():
    return {
        'info': {
            '_2_2_mc': [{
                    '_1_2_mc': {'mark_mc': {'currentLabel': 'show'}},
                    '_2_1_mc': {'circle_mc': {'currentLabel': 'show'}},
                    '_2_2_mc': {'square_mc': {'currentLabel': 'show'}},
                    '_2_3_mc': {'circle_mc': {'currentLabel': 'show'}},
                    'info_mc': {'decoration_mc': {'pattern_txt': {'text': 'CONNECT'}}}
            }]
        }
    }


from remote_control import upgrade
def get_info_sequence_news(pattern_dictionary, row_column_patterns_rotates):
    '''Info sequence to show marks from matches.
    For example, Moonhyoung connects at 2, 2.
    >>> row_column_patterns_rotates = {(2, 2): [['formation_connect', 'rotate_0']]}
    >>> from pprint import pprint
    >>> if not get_info_sequence_news(pattern_dictionary, row_column_patterns_rotates) == get_info_sequence_news_2_2():
    ...     pprint(get_info_sequence_news_2_2())
    ...     pprint(get_info_sequence_news(pattern_dictionary, row_column_patterns_rotates))
    '''
    news = {}
    for row_column, patterns_rotates in row_column_patterns_rotates.items():
        r, c = row_column
        intersection_name = '_%s_%s_mc' % (r, c)
        sequence = []
        for pattern, rotate in patterns_rotates:
            pattern_name = pattern.replace('formation_', '').upper()
            marks = {
                intersection_name: {'square_mc': {'currentLabel': 'show'}},
                'info_mc': {'decoration_mc': {'pattern_txt': {
                    'text': pattern_name}}}
            }
            # from pprint import pprint
            # pprint(pattern_dictionary[pattern][rotate])
            matches = pattern_dictionary[pattern][rotate]['match']
            origin_r, origin_c = pattern_dictionary[pattern][rotate]['origin']
            allies = {}
            for match_r, match_row in enumerate(matches):
                for match_c, match in enumerate(match_row):
                    if ally == match:
                        absolute_r = r + match_r - origin_r
                        absolute_c = c + match_c - origin_c
                        ally_name = '_%s_%s_mc' % (absolute_r, absolute_c)
                        allies[ally_name] = {'circle_mc': {'currentLabel': 'show'}}
                    elif enemy == match:
                        absolute_r = r + match_r - origin_r
                        absolute_c = c + match_c - origin_c
                        ally_name = '_%s_%s_mc' % (absolute_r, absolute_c)
                        allies[ally_name] = {'mark_mc': {'currentLabel': 'show'}}
            marks = upgrade(marks, allies)
            sequence.append(marks)
        news = upgrade(news, {'info': {intersection_name: sequence}})
    return news


def find_extends(board, borders, explored):
    '''Return extends and explored coordinates.
    >>> find_extends(peep_5_5_board, [(2, 0)], [])
    ([(1, 0), (2, 1), (3, 0)], [(2, 0), (1, 0), (2, 1), (3, 0)])
    '''
    extends = []
    def extend(board, row, column):
        return [b for b in find_beside(board, row, column)
            if b not in explored and b not in borders]
    for row, column in borders:
        if (row, column) not in explored:
            explored.append((row, column))
        new = extend(board, row, column)
        extends.extend(new)
        explored.extend(new)
    return extends, explored


def find_nearest(compare, board, row, column):
    '''Find nearest that matches cell comparison.
    >>> board = peep_5_5_board
    >>> row, column = (2, 0)
    >>> find_nearest(enemy, board, row, column)
    [(1, 0)]
    >>> find_nearest(ally, board, row, column)
    [(2, 2)]
    >>> board = fumble_peep_5_5_board
    >>> find_nearest(enemy, board, row, column)
    [(3, 1)]
    '''
    me = board[row][column]
    extends = [(row, column)]
    explored = []
    found = []
    while extends:
        extends, explored = find_extends(board, extends, explored)
        for r, c in extends:
            if compare(me, board[r][c]):
                found.append( (r, c) )
        if found:
            break
    return found


def get_nearest_enemy_matches(pattern_dictionary, 
        board, row, column):
    '''Match first valid nearest to position.  
    Enemy peeps.
    >>> matches = get_matches(attack_pattern_dictionary, fumble_peep_5_5_board,  
    ...     3, 1)
    >>> if not ['formation_peep', 'rotate_0'] in matches:
    ...     matches

    Player has no match.
    >>> get_matches(attack_pattern_dictionary, fumble_peep_5_5_board, 2, 0)
    []

    Nearest enemy peeps.
    >>> nearest_enemy_matches = get_nearest_enemy_matches(pattern_dictionary,
    ...     fumble_peep_5_5_board, 2, 0)
    >>> if not ['formation_peep', 'rotate_0'] in nearest_enemy_matches.get( (3, 1), [] ):
    ...     nearest_enemy_matches

    Useful to show bad move when player has no match.
    >>> get_matches(pattern_dictionary, marc_cut_self_3_5_board, 3, 5)
    []
    >>> nearest_enemy_matches = get_nearest_enemy_matches(attack_pattern_dictionary,
    ...     marc_cut_self_3_5_board, 3, 5)
    >>> if not ['formation_cut', 'rotate_0'] in nearest_enemy_matches.get( (3, 4), [] ):
    ...     nearest_enemy_matches

    Does not see in preview.
    >>> nearest_enemy_matches = get_nearest_enemy_matches(pattern_dictionary, 
    ...     preview_peep_5_5_board, 2, 0)
    >>> if not ['formation_peep', 'rotate_0'] in nearest_enemy_matches.get( (3, 1), [] ):
    ...     nearest_enemy_matches
    {}
    '''
    nearest_enemy_matches = {}
    enemies = find_nearest(enemy, board, row, column)
    for r, c in enemies:
        matches = get_valid_matches(pattern_dictionary, board, r, c)
        if matches:
            nearest_enemy_matches.update(matches)
            break
    return nearest_enemy_matches


def kyung_knight_cut_half2_example():
    r'''Kyung previews letting white cut him apart.
    >>> pattern_dictionary = get_pattern_dictionary(pattern_texts)

    During preview, match knight_cut_half2
    >>> matches = get_matches(pattern_dictionary,
    ...     kyung_knight_cut_half_board, 3, 4) 
    >>> if not ['formation_knight_cut_half2', 'rotate_180'] in matches:  
    ...     matches

    Match enemy's knight_cut_half2
    >>> get_matches(pattern_dictionary,
    ...     kyung_knight_cut_half_board, 2, 4) 
    []

    Adjacent enemy already cuts half of knight's connection.
    >>> nearest_enemy_matches = get_nearest_enemy_matches(pattern_dictionary,
    ...     kyung_knight_cut_half_board, 2, 4)
    >>> if not ['formation_knight_cut_half2', 'rotate_180'] \
    ...         in nearest_enemy_matches.get( (3, 4), [] ):
    ...     nearest_enemy_matches
    '''
    

def is_exact_match(match_marks, origin_row, origin_column, 
        board, last_row, last_column):
    r'''Does the block of the board match this rotation of the pattern?
    >>> history = [{'black': (2, 6)}, 
    ...     {'white': (5, 2)}, 
    ...     {'black': (2, 4)}]
    >>> print history_to_text(history)
      0 1 2 3 4 5 6 7 8 
    0 . . . . . . . . . 
    1 . . . . . . . . . 
    2 . . . . X2. X0. . 
    3 . . . . . . . . . 
    4 . . . . . . . . . 
    5 . . O1. . . . . . 
    6 . . . . . . . . . 
    7 . . . . . . . . . 
    8 . . . . . . . . . 
    >>> last_event = history[-1]
    >>> get_color_row_column(last_event)
    ('black', 2, 4)
    >>> last_color, last_row, last_column = \
    ...     get_color_row_column(last_event)
    >>> name, pattern, attributes = get_name_pattern_attributes(
    ...     jump_pattern_text)
    >>> match_marks = get_match_marks(pattern)
    >>> origin_row, origin_column = get_origin_row_column(pattern)
    >>> is_exact_match(match_marks, origin_row, origin_column,
    ...                jump_board,  last_row,   last_column)
    False
    >>> is_exact_match(match_marks, origin_row, origin_column,
    ...                jump_board,  last_row,   0)
    False
    >>> is_exact_match(match_marks, origin_row, origin_column,
    ...                jump_board,  last_row,   0)
    False
    '''
    if not in_bounds(board, last_row, last_column):
        print 'is_exact_match:  I am not prepared for last_move off_board:  %s, %s' % (last_row, last_column)
        return False
    you = board[last_row][last_column]
    board_row = last_row - origin_row
    board_column = last_column - origin_column
    board_row_max = board_row + len(match_marks)
    # XXX hard to read
    board_row_range = range(board_row, board_row_max)
    for match_row, row in zip(match_marks, board_row_range):
        board_column_max = board_column + len(match_row)
        board_column_range = range(board_column, board_column_max)
        for match, column in zip(match_row, board_column_range):
            if in_bounds(board, row, column):
                mark = board[row][column]
            else:
                mark = off_board
            if not match(mark, you):
                return False
    return True

    
def get_name_pattern_attributes(pattern_text):
    '''What is the name, pattern, and attributes of this simple db?
    >>> name, pattern, attributes = get_name_pattern_attributes(
    ...     jump_pattern_text)
    >>> name
    'formation_jump'
    >>> pattern
    ['???', 'oOo', '...', '?*?', '???']
    >>> attributes
    ['|', 'C', 'shape(5)']
    >>> name, pattern, attributes = get_name_pattern_attributes(
    ...     knight_pattern_text)
    >>> name
    'formation_knight'
    '''
    lines = text_to_lines(pattern_text)
    name = lines.pop(0).lstrip('Pattern')
    attributes = []
    pattern = lines
    for line in lines:
        if line.startswith(':'):
            pattern.remove(line)
            attributes.extend( line.strip(':').split(',') )
    return name, pattern, attributes


def get_origin_row_column(pattern):
    '''Which row and and column is the first '*' found?
    >>> name, pattern, attributes = get_name_pattern_attributes(
    ...     jump_pattern_text)
    >>> get_origin_row_column(pattern)
    (3, 1)
    >>> get_origin_row_column(rotate_90(pattern))
    (1, 1)
    '''
    for row, line in enumerate(pattern):
        if '*' in line:
            # no index for tuple
            # www.diveintopython.org/getting_to_know_python/tuples.html
            column = list(line).index('*')
            origin_row, origin_column = row, column
            return origin_row, origin_column


def get_offsets(compare, pattern, origin):
    '''How many rows and columns is each compare from the origin?
    >>> name, pattern, attributes = get_name_pattern_attributes(
    ...     jump_pattern_text)
    >>> origin = get_origin_row_column(pattern)
    >>> origin
    (3, 1)

    Does not prune symmetries.
    >>> offsets = get_offsets(ally, pattern, origin)
    >>> offsets
    [(2, 0)]

    Go from compare to origin.
    >>> compare_at = (0, 1)
    >>> compare_at[0] + offsets[0][0], compare_at[1] + offsets[0][1]
    (2, 1)

    May include origin.
    >>> offsets = get_offsets(identical, pattern, origin)
    >>> offsets
    [(0, 0)]
    '''
    compare_offsets = []
    for row, line in enumerate(pattern):
        for column, pattern_mark in enumerate(line):
            #if origin != (row, column):
            if compare == pattern_mark_dictionary[pattern_mark]:
                offset = origin[0] - row, origin[1] - column
                compare_offsets.append(offset)
    return compare_offsets


def get_match_coordinates(compare, pattern, row, column):
    '''Coordinates that match comparison in the pattern.
    >>> compare = am_i_empty_but_not_you
    >>> pattern = defend_pattern_dictionary['formation_field']['rotate_0']['pattern']
    >>> row, column = (2, 2)
    >>> coordinates = get_match_coordinates(compare, pattern, row, column)
    >>> coordinates
    [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (2, 0), (2, 1), (2, 3), (2, 4), (3, 0), (3, 1), (3, 2), (3, 3), (3, 4), (4, 0), (4, 1), (4, 2), (4, 3), (4, 4)]
    >>> row, column = (5, 1)
    >>> pattern = pattern_dictionary['formation_jump_underneath']['rotate_0']['pattern']
    >>> get_match_coordinates(ally, pattern, row, column)
    [(3, 1)]
    '''
    origin = get_origin_row_column(pattern)
    offsets = get_offsets(compare, pattern, origin)
    coordinates = [(row - r, column - c) for r, c in offsets]
    coordinates.sort()
    return coordinates


decoration_dictionary = {
    'profit': [am_i_empty_but_not_you],
    'defend': [am_i_empty_but_not_you, ally_or_empty, enemy_or_empty],
    'attack': [am_i_empty_but_not_you, ally_or_empty, enemy_or_empty],
    #'attack': [am_i_empty_but_not_you, ally_or_empty, enemy_or_empty],
    #'defend': [ally, am_i_empty_but_not_you, identical],
    #'attack': [enemy, am_i_empty_but_not_you, identical],
}

def get_matches_coordinates(compares, patterns_rotates, row, column):
    '''Coordinates that match comparison in the patterns.
    >>> row, column = (5, 1)
    >>> matches = get_matches(pattern_dictionary, jump_underneath_board,  
    ...     row, column)
    >>> matches
    [['formation_jump_underneath', 'rotate_0'], ['formation_jump_underneath', 'row_reflect_rotate_270']]
    >>> get_matches_coordinates([ally], matches, row, column)
    [(3, 1), (5, 3)]
    >>> get_matches_coordinates([am_i_empty_but_not_you], matches, row, column)
    [(4, 0), (4, 1), (5, 2), (6, 2)]
    >>> get_matches_coordinates([ally, am_i_empty_but_not_you, identical], matches, row, column)
    [(3, 1), (4, 0), (4, 1), (5, 1), (5, 2), (5, 3), (6, 2)]
    '''
    decorations = []
    for pattern_name, rotate in patterns_rotates:
        pattern = pattern_dictionary[pattern_name][rotate]['pattern']
        for compare in compares:
            new_decorations = get_match_coordinates(
                   compare, pattern, row, column)
            new_decorations = [decoration for decoration in new_decorations 
                    if decoration not in decorations]
            decorations.extend(new_decorations)
    decorations.sort()
    return decorations


def are_empty(board, coordinates):
    '''Empty coordinates that do not match mark.
    >>> board = jump_underneath_board
    >>> coordinates = [(3, 1), (4, 0), (4, 1), (5, 1), (5, 2), (5, 3), (6, 2)]
    >>> are_empty(board, coordinates) 
    [(4, 0), (4, 1), (5, 2), (6, 2)]
    '''
    return [(r, c) for r, c in coordinates 
            if is_empty(board[r][c])]
    
def get_match_marks(pattern):
    '''Generate pattern functions from shorthand text diagram.
    >>> name, pattern, attributes = get_name_pattern_attributes(
    ...     jump_pattern_text)
    >>> match_marks = get_match_marks(pattern)
    '''
    match_marks = []
    for row in pattern:
        match_marks.append( [] )
        for pattern_mark in row:
            is_pattern = pattern_mark_dictionary[pattern_mark]
            match_marks[-1].append(is_pattern)
    return match_marks



def rotate_examples():
    '''Rotate a board image.
    Ragged tables are truncated.
    >>> prevent_diagonal_cut_pattern = [['O', '*'], ['X', 'O']]
    >>> rotate_0(prevent_diagonal_cut_pattern)
    [['O', '*'], ['X', 'O']]
    >>> rotate_90(prevent_diagonal_cut_pattern)
    [('X', 'O'), ('O', '*')]
    >>> rotate_90(rotate_90(prevent_diagonal_cut_pattern))
    [('O', 'X'), ('*', 'O')]
    >>> rotate_180(prevent_diagonal_cut_pattern)
    [('O', 'X'), ('*', 'O')]
    >>> rotate_90(rotate_90(rotate_90(prevent_diagonal_cut_pattern)))
    [('*', 'O'), ('O', 'X')]
    >>> rotate_270(prevent_diagonal_cut_pattern)
    [('*', 'O'), ('O', 'X')]
    >>> rotate_90(rotate_90(rotate_90(rotate_90(prevent_diagonal_cut_pattern))))
    [('O', '*'), ('X', 'O')]

    String form of pattern okay too.
    >>> prevent_diagonal_cut = [['O', '*'], ['X', 'O']]
    >>> pb(prevent_diagonal_cut)
    O*
    XO
    >>> pb(rotate_90(prevent_diagonal_cut))
    XO
    O*

    Reflect enables covering all eight variants
    for patterns with no symmetry.
    >>> extend = [['.', 'X'], ['*', 'O']]
    >>> pb(rotate_0(extend))
    .X
    *O
    >>> pb(rotate_90(extend))
    *.
    OX
    >>> pb(rotate_180(extend))
    O*
    X.
    >>> pb(rotate_270(extend))
    XO
    .*
    >>> pb(row_reflect_rotate_0(extend))
    *O
    .X
    >>> pb(row_reflect_rotate_90(extend))
    .*
    XO
    >>> pb(row_reflect_rotate_180(extend))
    X.
    O*
    >>> pb(row_reflect_rotate_270(extend))
    OX
    *.
    >>> connect = [['.', '.'], ['*', 'O'], ['O', 'X']]
    >>> pb(connect)
    ..
    *O
    OX
    >>> pb(rotate_90(connect))
    O*.
    XO.
    >>> numbers = [range(3), range(3, 6), range(6, 9), range(9, 6, -1)]
    >>> pb(numbers)
    012
    345
    678
    987
    >>> pb(rotate_90(numbers))
    9630
    8741
    7852
    >>> pb(row_reflect_rotate_90(numbers))
    0369
    1478
    2587
    '''

def row_reflect_rotate_0(pattern):
    '''
    >>> pattern = ['?O?', '...', '.*.', '?.?']
    >>> row_reflect_rotate_0(pattern)
    ['?.?', '.*.', '...', '?O?']
    '''
    upside_down = []
    for row in pattern:  
        upside_down.insert(0, row)
    return upside_down

def rotate_0(table):
    return table

def rotate_90(table):
    # I saw Chad Miller's post on this neat hack with zip.
    return zip(*row_reflect_rotate_0(table))

def rotate_180(table):
    return rotate_90(rotate_90(table))

def rotate_270(table):
    return row_reflect_rotate_0(zip(*table))

def row_reflect_rotate_90(table):
    return rotate_90(row_reflect_rotate_0(table))

def row_reflect_rotate_180(table):
    return rotate_180(row_reflect_rotate_0(table))

def row_reflect_rotate_270(table):
    return rotate_270(row_reflect_rotate_0(table))

def get_pattern_dictionary(pattern_texts):
    '''Generate four rotations of vertical or horizontal symmetry patterns.
    >>> pattern_dictionary = get_pattern_dictionary(pattern_texts)
    >>> matches = get_matches(defend_pattern_dictionary,
    ...       jump_board, 2, 6)
    >>> if not ['formation_jump', 'rotate_270'] in matches:  matches
    >>> matches = get_matches(pattern_dictionary,
    ...       jump_board, 2, 6)
    >>> 4 < len(matches)
    True
    >>> len(matches) < 10
    True
    >>> pattern_dictionary['formation_jump']['rotate_0']['origin']
    (3, 1)
    >>> pattern_dictionary['formation_jump']['rotate_0'].get('ally_offsets')
    [(2, 0)]
    >>> pattern_dictionary['formation_jump']['rotate_90'].get('ally_offsets')
    [(0, -2)]
    '''
    pattern_dictionary = {}
    for pattern_text in pattern_texts:
        name, pattern, attributes = get_name_pattern_attributes(
            pattern_text)
        symmetry = attributes.pop(0)
        classification = attributes.pop(0)
        values = attributes
        pattern_dictionary[name] = {
                'symmetry':  symmetry,
                'classification':  classification,
                'values':  values
                }
        for rotate in get_rotates(symmetry):
            rotated_pattern = eval(rotate)(pattern)
            match_marks = get_match_marks(rotated_pattern)
            origin = get_origin_row_column(rotated_pattern)
            ally_offsets = get_offsets(ally, rotated_pattern, origin)
            # insert ally offsets
            pattern_dictionary[name][rotate] = {
                'pattern': rotated_pattern,
                'match': match_marks,
                'origin':  origin,
                'ally_offsets': ally_offsets,
                }
    return pattern_dictionary


# only need to generate this once per game
pattern_dictionary = {}
pattern_texts = []

profit_pattern_texts = [
    #field_pattern_text,
    #quarter_field_pattern_text,
    #fence_pattern_text,
]
profit_pattern_dictionary = get_pattern_dictionary(profit_pattern_texts)
pattern_dictionary.update(profit_pattern_dictionary)
pattern_texts.extend(profit_pattern_texts)

defend_pattern_texts = [
    jump_pattern_text,
    connect_pattern_text,
    jump_underneath_pattern_text,
    monkey_peep_pattern_text,
    knight_pattern_text,
    knight_underneath_pattern_text,
    diagonal_pattern_text,
    crawl_pattern_text,
    diagonal_connect_pattern_text,
    block_pattern_text,
    tiger_mouth_pattern_text,
    tiger_jaw_pattern_text,
    leap_pattern_text,
    # was profit
    field_pattern_text,
    quarter_field_pattern_text,
    center_3_3_pattern_text,
    fence_pattern_text,
    open_tiger_yawn_pattern_text,
    #danger_tiger_jaw_pattern_text,
    #danger_tiger_mouth_pattern_text,
]
defend_pattern_dictionary = get_pattern_dictionary(defend_pattern_texts)
pattern_dictionary.update(defend_pattern_dictionary)
pattern_texts.extend(defend_pattern_texts)

attack_pattern_texts = [
    jump_attack_pattern_text,
    peep_pattern_text,
    cut_pattern_text,
    peep_knight_pattern_text,
    knight_cut_half_pattern_text,
    knight_cut_half2_pattern_text,
    knight_attack_pattern_text,
    chariot_attack_pattern_text,
    shoulder_hit_pattern_text,
    press_pattern_text,
    perch_pattern_text,
    high_perch_pattern_text,
    diagonal_attack_pattern_text,
    diagonal_cut_half_pattern_text,
    peep_diagonal_pattern_text,
    diagonal_cut_pattern_text,
    leap_attack_pattern_text,
    tiger_yawn_pattern_text,
    tiger_lick_pattern_text,
    tiger_chomp_pattern_text,
]
attack_pattern_dictionary = get_pattern_dictionary(attack_pattern_texts)
pattern_dictionary.update(attack_pattern_dictionary)
pattern_texts.extend(attack_pattern_texts)

eye_pattern_texts = [
    eye_line_3_pattern_text,
]
eye_pattern_dictionary = get_pattern_dictionary(eye_pattern_texts)
# pattern_dictionary.update(eye_pattern_dictionary)
# pattern_texts.extend(eye_pattern_texts)


import code_unit
snippet = '''
# !start python code_explorer.py --import pattern.py --snippet snippet
import pattern; pattern = reload(pattern); from pattern import *
code_unit.doctest_unit(get_matches)
'''
if __name__ == '__main__':
    from optparse import OptionParser
    parser = OptionParser()
    parser.add_option("--unit", default="",
        dest="unit", help="unit to doctest [default: %default]")
    (options, args) = parser.parse_args()
    if options.unit:
        unit = eval(options.unit)
        code_unit.doctest_unit(unit)
    else:
        units = globals().values()
        ## units.remove(setup_example)
        code_unit.doctest_units(units)
    

