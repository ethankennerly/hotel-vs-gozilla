Python 2.5.1 (r251:54863, Apr 18 2007, 08:51:08) [MSC v.1310 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> 
>>> 
>>> 
>>> os.chdir('../lifeanddeath')
>>> 
>>> from ambassador import *
>>> 
>>> verbose = True
>>> 
>>> ambassador = ambassador_class()
>>> 
>>> ambassador.verbose = verbose
>>> 
>>> ambassador.referee.verbose = verbose
>>> 
>>> services['gtp'] = ambassador.gtp
>>> 
>>> services['ask'] = ambassador.act_black
>>> 
>>> services['printsgf'] = ambassador.printsgf
>>> 
>>> services['hide'] = ambassador.hide_black
>>> 
>>> services['configure'] = ambassador.referee.configure
>>> 
>>> services['set_level'] = ambassador.referee.set_level
>>> 
>>> services['validate'] = referee.validate
>>> 
>>> services['show_board'] = ambassador.referee.show_board
>>> 
>>> services['echo'] = ambassador.echo
>>> 
>>> services['execute'] = ambassador.execute
>>> 
>>> services['evaluate'] = ambassador.evaluate
>>> 
>>> httpd = create(ambassador)
>>> 
>>> host = run_it(httpd)
>>> 
>>> host.start()
>>> 
>>> # time.sleep(1)
>>> 
>>> # run_examples(shell, setup_score_example.__doc__)
>>> 
>>> setup_client()
ambassador.act_black( {'showboard': True} )
,,,,,,,,,
,,,,,,,,,
,,,,,,,,,
,,,,,,,,,
,,,,,,,,,
,,,,,,,,,
,,,,,,,,,
,,,,,,,,,
,,,,,,,,,
  0 1 2 3 4 5 6 7 8 
0 . . . . . . . . . 
1 . . . . . . . . . 
2 . . . . . . . . . 
3 . . . . . . . . . 
4 . . . . . . . . . 
5 . . . . . . . . . 
6 . . . . . . . . . 
7 . . . . . . . . . 
8 . . . . . . . . . 
referee.notify( {'clear_board': True,
 'set_turn': 'black',
 'star': [(2, 2), (2, 6), (6, 2), (6, 6)]} )
validate( {'hide_gift': [u'_0', u'_1', u'_2', u'_3'], 'help': [u'none', u'first_move', u'star', u'extra_stone_gift', u'extra_stone', u'danger', u'warning', u'suicide', u'suicide_white', u'block', u'score', u'dead'], 'game_over': [u'none', u'win', u'draw', u'lose'], 'glass': [u'none', u'block'], 'undo_gift': [], 'extra_stone_gift': [u'_0', u'_1']} )
validate missing:  {'undo_gift': [1, 25], 'error': ['undo_gift']}
Ethan - - [01/Dec/2009 12:03:55] "POST / HTTP/1.1" 200 155
17668
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> import os
>>> import sys
>>> # workaround for absolute pathnames
>>> # in sys.path (see model.py)
>>> if sys.path[0] not in ('', '.'):
...         sys.path.insert(0, '')
...     
>>> import wx
>>> from PythonCard import dialog, util
>>> bg = pcapp.getCurrentBackground()
>>> self = bg
>>> comp = bg.components
>>> news = ambassador.act_black({'load_board': 
...         'score_white_by_18_board_text'})
ambassador.act_black( {'load_board': 'score_white_by_18_board_text'} )
notify_genmove:  did you know black nor white has this turn?   None
,,XOO,,,,
,,,XOO,,,
,,X,XO,,,
,,,XXO,,,
,,XXO,,,,
,,,XO,,,,
,XXOO,O,,
XXOO,,,,,
XOO,,,,,,
  0 1 2 3 4 5 6 7 8 
0 . . . . . . . . . 
1 . . . . . . . . . 
2 . . . . . . . . . 
3 . . . . . . . . . 
4 . . . . . . . . . 
5 . . . . . . . . . 
6 . . . . . . . . . 
7 . . . . . . . . . 
8 . . . . . . . . . 
referee.notify( {'black': [(0, 2),
           (1, 3),
           (2, 2),
           (2, 4),
           (3, 3),
           (3, 4),
           (4, 2),
           (4, 3),
           (5, 3),
           (6, 1),
           (6, 2),
           (7, 0),
           (7, 1),
           (8, 0)],
 'clear_board': True,
 'suicide_white': [(2, 3)],
 'territory': [['neutral',
                'neutral',
                'neutral',
                'neutral',
                'neutral',
                'neutral',
                'neutral',
                'neutral',
                'neutral'],
               ['neutral',
                'neutral',
                'neutral',
                'neutral',
                'neutral',
                'neutral',
                'neutral',
                'neutral',
                'neutral'],
               ['neutral',
                'neutral',
                'neutral',
                'neutral',
                'neutral',
                'neutral',
                'neutral',
                'neutral',
                'neutral'],
               ['neutral',
                'neutral',
                'neutral',
                'neutral',
                'neutral',
                'neutral',
                'neutral',
                'neutral',
                'neutral'],
               ['neutral',
                'neutral',
                'neutral',
                'neutral',
                'neutral',
                'neutral',
                'neutral',
                'neutral',
                'neutral'],
               ['neutral',
                'neutral',
                'neutral',
                'neutral',
                'neutral',
                'neutral',
                'neutral',
                'neutral',
                'neutral'],
               ['neutral',
                'neutral',
                'neutral',
                'neutral',
                'neutral',
                'neutral',
                'neutral',
                'neutral',
                'neutral'],
               ['neutral',
                'neutral',
                'neutral',
                'neutral',
                'neutral',
                'neutral',
                'neutral',
                'neutral',
                'neutral'],
               ['neutral',
                'neutral',
                'neutral',
                'neutral',
                'neutral',
                'neutral',
                'neutral',
                'neutral',
                'neutral']],
 'warning': [(0, 2), (1, 3)],
 'white': [(0, 3),
           (0, 4),
           (1, 4),
           (1, 5),
           (2, 5),
           (3, 5),
           (4, 4),
           (5, 4),
           (6, 3),
           (6, 4),
           (6, 6),
           (7, 2),
           (7, 3),
           (8, 1),
           (8, 2)]} )
>>> pb(ambassador.referee.board)
Traceback (most recent call last):
  File "<input>", line 1, in <module>
NameError: name 'pb' is not defined
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
>>> news = ambassador.act_black({'genmove': 'white'})
ambassador.act_black( {'genmove': 'white'} )
ambassador._listen_gtp( ['genmove white'] )
ambassador.gtp( 'loadsgf sgf/_update_gnugo.sgf 999' )
ambassador.gtp( 'genmove white' )
referee.act_white_gtp('genmove white', '= E5\n\n')
notify_genmove:  did you know black nor white has this turn?   None
,,XOO,,,,
,,,XOO,,,
,,X,XO,,,
,,,XXO,,,
,,XXO,,,,
,,,XO,,,,
,XXOO,O,,
XXOO,,,,,
XOO,,,,,,
  0 1 2 3 4 5 6 7 8 
0 . . . . . . . . . 
1 . . . . . . . . . 
2 . . . . . . . . . 
3 . . . . . . . . . 
4 . . . . . . . . . 
5 . . . . . . . . . 
6 . . . . . . . . . 
7 . . . . . . . . . 
8 . . . . . . . . . 
referee.notify( {'already_at': [(4, 4)], 'error': 'already_at', 'white': [(4, 4)]} )
referee._why_not_play(white, 4, 4) # occupied O
referee._genmove_white('genmove white', '= E5\n\n') # reason not to play:  {'white': [(4, 4)], 'already_at': [(4, 4)], 'error': 'already_at'}
referee._genmove_white:  GnuGo or I am mistaken.  pass.  {'territory_labels': [['neutral', 'neutral', 'neutral', 'neutral', 'neutral', 'neutral', 'neutral', 'neutral', 'neutral'], ['neutral', 'neutral', 'neutral', 'neutral', 'neutral', 'neutral', 'neutral', 'neutral', 'neutral'], ['neutral', 'neutral', 'neutral', 'neutral', 'neutral', 'neutral', 'neutral', 'neutral', 'neutral'], ['neutral', 'neutral', 'neutral', 'neutral', 'neutral', 'neutral', 'neutral', 'neutral', 'neutral'], ['neutral', 'neutral', 'neutral', 'neutral', 'neutral', 'neutral', 'neutral', 'neutral', 'neutral'], ['neutral', 'neutral', 'neutral', 'neutral', 'neutral', 'neutral', 'neutral', 'neutral', 'neutral'], ['neutral', 'neutral', 'neutral', 'neutral', 'neutral', 'neutral', 'neutral', 'neutral', 'neutral'], ['neutral', 'neutral', 'neutral', 'neutral', 'neutral', 'neutral', 'neutral', 'neutral', 'neutral'], ['neutral', 'neutral', 'neutral', 'neutral', 'neutral', 'neutral', 'neutral', 'neutral', 'neutral']], 'ambassador': <ambassador.ambassador_class object at 0x036977F0>, 'verbose': True, 'white_rank': -14, 'extra_stone_black': 0, 'news_time': 0, 'gift_function': {'hide_gift': <bound method referee_class._give_hide of <referee.referee_class object at 0x037655F0>>, 'extra_stone_gift': <bound method referee_class._give_extra_stone of <referee.referee_class object at 0x037655F0>>}, 'moves': [], 'extra_stone_max': 1, 'previous_territory_labels': [[None, None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None, None]], 'previous_danger': [], 'previous_stone_dictionary': {'white': [(0, 3), (0, 4), (1, 4), (1, 5), (2, 5), (3, 5), (4, 4), (5, 4), (6, 3), (6, 4), (6, 6), (7, 2), (7, 3), (8, 1), (8, 2)], 'black': [(0, 2), (1, 3), (2, 2), (2, 4), (3, 3), (3, 4), (4, 2), (4, 3), (5, 3), (6, 1), (6, 2), (7, 0), (7, 1), (8, 0)]}, 'extra_stone_gift': 0, 'previous_hidden': {}, 'black': 'human', 'board': [[',', ',', 'X', 'O', 'O', ',', ',', ',', ','], [',', ',', ',', 'X', 'O', 'O', ',', ',', ','], [',', ',', 'X', ',', 'X', 'O', ',', ',', ','], [',', ',', ',', 'X', 'X', 'O', ',', ',', ','], [',', ',', 'X', 'X', 'O', ',', ',', ',', ','], [',', ',', ',', 'X', 'O', ',', ',', ',', ','], [',', 'X', 'X', 'O', 'O', ',', 'O', ',', ','], ['X', 'X', 'O', 'O', ',', ',', ',', ',', ','], ['X', 'O', 'O', ',', ',', ',', ',', ',', ',']], 'stone_dictionary': {}, 'black_rank': -39, 'white': 'computer', 'previous_turn': None, 'more': None, 'turns_in_a_row_max': 4, 'hide_max': 3, 'hide_gift': 0, 'previous_warning': [(0, 2), (1, 3)], 'undo_gift': 1, 'move_colors': [], 'news': {}, 'now': {}, 'secret_gifts': ['extra_stone_gift', 'extra_stone_gift', 'extra_stone_gift', 'extra_stone_gift', 'extra_stone_gift', 'extra_stone_gift', 'extra_stone_gift', 'extra_stone_gift', 'extra_stone_gift', 'extra_stone_gift', 'extra_stone_gift', 'extra_stone_gift'], 'hidden': {}, 'present': {'suicide_white': [(2, 3)]}, 'turn': None, 'previous_genmove': None, 'history': [{}]}
Traceback (most recent call last):
  File "<input>", line 1, in <module>
  File "C:\project\lifeanddeath\ambassador.py", line 1395, in act_black
    return self._notify_gtp(client_request)
  File "C:\project\lifeanddeath\ambassador.py", line 1400, in _notify_gtp
    self._listen_gtp(gtp_commands)
  File "C:\project\lifeanddeath\ambassador.py", line 1422, in _listen_gtp
    gtp_command, gtp_response)
  File "C:\project\lifeanddeath\referee.py", line 4766, in act_white_gtp
    gtp_command, gtp_response)
  File "C:\project\lifeanddeath\referee.py", line 4617, in _genmove_white
    self.log_move(color, 'pass')
  File "C:\project\lifeanddeath\referee.py", line 4421, in log_move
    if 'pass' == self.history[-2].get(opposite(color)):
IndexError: list index out of range
>>> # white sees empty board.
>>> ambassador.referee.load('sgf/score_9x9_white_by_18.sgf')
Traceback (most recent call last):
  File "<input>", line 1, in <module>
  File "C:\project\lifeanddeath\referee.py", line 3953, in load
    history = sgf_to_history(file)
  File "C:\project\lifeanddeath\referee.py", line 5896, in sgf_to_history
    def sgf_to_history(file):
  File "C:\project\python\text.py", line 11, in load
    file = codecs.open(os.path.abspath(path), 'r', 'utf-8')
  File "C:\Python25\lib\codecs.py", line 817, in open
    file = __builtin__.open(filename, mode, buffering)
IOError: [Errno 2] No such file or directory: 'C:\\project\\lifeanddeath\\sgf\\score_9x9_white_by_18.sgf'
>>> dialog.openFileDialog()
