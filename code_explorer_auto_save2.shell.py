Python 2.5.1 (r251:54863, Apr 18 2007, 08:51:08) [MSC v.1310 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> shell.other.autoCompleteIncludeSingle = True
>>> 
>>> 
>>> 
>>> shell.other.autoCompleteIncludeDouble = True
>>> 
>>> 
>>> 
>>> from pprint import pprint
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> # !start python code_explorer.py --import client.py --snippet snippet
>>> 
>>> 
>>> 
>>> # import actionscript; actionscript = reload(actionscript); from actionscript import *
>>> 
>>> 
>>> 
>>> # import remote_control; remote_control = reload(remote_control); from remote_control import *
>>> 
>>> 
>>> 
>>> # import embassy; embassy = reload(embassy); from embassy import *
>>> 
>>> 
>>> 
>>> # import client; client = reload(client); from client import *
>>> 
>>> 
>>> 
>>> shell.other.autoCompleteIncludeSingle = True
>>> 
>>> 
>>> 
>>> shell.other.autoCompleteIncludeDouble = True
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> run_examples(shell, setup_remote_control_snippet.__doc__)
>>> 
>>> 
>>> # Start server, before Flash client
>>> 
>>> 
>>> 
>>> configuration.subprocess_gateway = subprocess_gateway_file
>>> 
>>> 
>>> 
>>> configuration.setup_client = setup_amf_client
>>> 
>>> 
>>> 
>>> configuration.mock_speed = 1
>>> 
>>> 
>>> 
>>> configuration.verbose = 'info'
>>> 
>>> 
>>> 
>>> configuration.setup_client = setup_flash_master
>>> 
>>> 
>>> 
>>> configuration.globe_class = master_class
>>> 
>>> 
>>> 
>>> configuration.simulate_lag = 0.0
>>> 
>>> 
>>> 
>>> set_property = slave_set_property
>>> 
>>> 
>>> 
>>> dispatch_event = slave_dispatch_event
>>> 
>>> 
>>> 
>>> mouse_down_and_sleep = slave_mouse_down_and_sleep
>>> 
>>> 
>>> 
>>> mouse_down_and_news = slave_mouse_down_and_news
>>> 
>>> 
>>> 
>>> gateway_process = configuration.subprocess_gateway(configuration.amf_host, 'embassy.py', configuration.verbose)
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> # run_examples(shell, profile_doctest.__doc__)
>>> 
>>> 
>>> 
>>> # run_examples(shell, restart_example.__doc__)
>>> 
>>> 
>>> 
>>> # run_examples(shell, white_computer_example.__doc__)
>>> 
>>> 
>>> 
>>> # run_examples(shell, connect_5_5_example.__doc__)
>>> 
>>> 
>>> 
>>> # run_examples(shell, board_7_7_example.__doc__)
>>> 
>>> 
>>> 
>>> # run_examples(shell, board_5_5_example.__doc__)
>>> 
>>> 
>>> 
>>> # run_examples(shell, board_3_3_example.__doc__)
>>> 
>>> 
>>> 
>>> # run_examples(shell, ethan_andre_example.__doc__)
>>> 
>>> 
>>> 
>>> # run_examples(shell, ethan_michael_example.__doc__)
>>> 
>>> 
>>> 
>>> # run_examples(shell, capture_example.__doc__)
>>> 
>>> 
>>> 
>>> # run_examples(shell, master_save_stage_example.__doc__)
>>> 
>>> 
>>> 
>>> # run_examples(shell, ethan_mathijs_example.__doc__)
>>> 
>>> 
>>> 
>>> # run_examples(shell, critical_example.__doc__)
>>> 
>>> 
>>> 
>>> # run_examples(shell, ethan_joris_start_example.__doc__)
>>> 
>>> 
>>> 
>>> # run_examples(shell, real_time_example.__doc__)
>>> 
>>> 
>>> 
>>> # run_examples(shell, real_time_stress_example.__doc__)
>>> 
>>> 
>>> 
>>> # run_examples(shell, echo.__doc__)
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> # Moonhyoung connects his stones, sees defense.
>>> 
>>> 
>>> 
>>> #     Mouse over and sees essential stones of his defense.
>>> 
>>> 
>>> 
>>> code_unit.inline_examples(
...     
...     
...     
...         ethan_lukasz_begin_example.__doc__,
...     
...     
...     
...         locals(), globals(),
...     
...     
...     
...         verify_examples = False)
WARNING:root:AmfSocketClient connecting to socket server on localhost:5900
WARNING:root:AmfSocketClient connected to server.
ERROR:root:update_family_tree: root property? sequence = [{'comment_mc': {'_txt': {'text': u'HELLO.  TO START, CLICK LEVEL 1.'}, 'currentLabel': u'comment'}, 'time_txt': {'text': u'16580'}}, {'level_mc': {'_txt': {'text': u'36'}, 'currentLabel': u'up', 'progress_mc': {'currentLabel': u'_43'}}, 'time_txt': {'text': u'17080'}}]
ERROR:root:dispatch_family_tree: root property? sequence = [{'comment_mc': {'_txt': {'text': u'HELLO.  TO START, CLICK LEVEL 1.'}, 'currentLabel': u'comment'}, 'time_txt': {'text': u'16580'}}, {'level_mc': {'_txt': {'text': u'36'}, 'currentLabel': u'up', 'progress_mc': {'currentLabel': u'_43'}}, 'time_txt': {'text': u'17080'}}]
WARNING:root:AmfSocketClient connecting to socket server on localhost:5900
WARNING:root:AmfSocketClient connected to server.
ERROR:root:update_family_tree: root property? sequence = [{'comment_mc': {'_txt': {'text': u'HELLO.  TO START, CLICK LEVEL 1.'}, 'currentLabel': u'comment'}, 'time_txt': {'text': u'20613'}}, {'level_mc': {'_txt': {'text': u'5'}, 'currentLabel': u'up', 'progress_mc': {'currentLabel': u'_79'}}, 'time_txt': {'text': u'21113'}}]
ERROR:root:dispatch_family_tree: root property? sequence = [{'comment_mc': {'_txt': {'text': u'HELLO.  TO START, CLICK LEVEL 1.'}, 'currentLabel': u'comment'}, 'time_txt': {'text': u'20613'}}, {'level_mc': {'_txt': {'text': u'5'}, 'currentLabel': u'up', 'progress_mc': {'currentLabel': u'_79'}}, 'time_txt': {'text': u'21113'}}]
>>> 
>>> 
>>> 
>>> wait = 4.0 / black._speed
>>> 
>>> 
>>> 
>>> sloth = 1.0 / black._speed
>>> 
>>> 
>>> 
>>> moonhyoung = black
>>> 
>>> 
>>> 
>>> computer_moonhyoung = white
>>> 
>>> 
>>> 
>>> time.sleep(sloth * 1.553000)
>>> 
>>> 
>>> 
>>> moonhyoung.root.lobby_mc.main_mc._10_mc.dispatchEvent(mouseDown)
>>> 
>>> 
>>> 
>>> time.sleep(sloth * 1.573000)
>>> 
>>> 
>>> 
>>> moonhyoung.root.lobby_mc._10_mc.defend_mc.dispatchEvent(mouseDown)
>>> 
>>> 
>>> 
>>> time.sleep(sloth * 1.084000)
ERROR:root:upgrade:  i did not expect old_value: [{'comment_mc': {'_txt': {'text': u'HELLO.  TO START, CLICK LEVEL 1.'}, 'currentLabel': u'comment'}, 'time_txt': {'text': u'16580'}}, {'level_mc': {'_txt': {'text': u'36'}, 'currentLabel': u'up', 'progress_mc': {'currentLabel': u'_43'}}, 'time_txt': {'text': u'17080'}}],  value: [{'time_txt': {'text': u'18580'}, '_1_0_mc': {'currentLabel': u'white'}}, {'time_txt': {'text': u'19580'}, '_1_1_mc': {'currentLabel': u'white'}}, {'_1_2_mc': {'currentLabel': u'white'}, 'time_txt': {'text': u'20580'}}, {'time_txt': {'text': u'21580'}, '_1_3_mc': {'currentLabel': u'white'}}, {'time_txt': {'text': u'22580'}, '_1_4_mc': {'currentLabel': u'white'}}, {'_2_0_mc': {'currentLabel': u'black'}, 'time_txt': {'text': u'23580'}}, {'time_txt': {'text': u'24580'}, '_2_1_mc': {'currentLabel': u'black'}}, {'time_txt': {'text': u'25580'}, '_2_3_mc': {'currentLabel': u'black'}}, {'time_txt': {'text': u'26580'}, '_2_4_mc': {'currentLabel': u'black'}}, {'time_txt': {'text': u'26580'}, '_1_0_mc': {'progress_mc': {'currentLabel': u'white_start'}}}, {'time_txt': {'text': u'26705'}, 'cursor_mc': {'act_mc': {'currentLabel': u'busy'}, 'currentLabel': u'none'}}, {'time_txt': {'text': u'27205'}, 'turn_veil_mc': {'currentLabel': u'other'}}, {'time_txt': {'text': u'27330'}, 'turn_mc': {'currentLabel': u'black', 'white_user_txt': {'text': u'computer_lukasz'}, 'black_user_txt': {'text': u'lukasz'}}}, {'_2_0_mc': {'progress_mc': {'currentLabel': u'black_complete'}}, 'time_txt': {'text': u'27330'}}, {'time_txt': {'text': u'27330'}, '_2_1_mc': {'progress_mc': {'currentLabel': u'black_complete'}}}, {'time_txt': {'text': u'27330'}, '_2_3_mc': {'progress_mc': {'currentLabel': u'black_complete'}}}, {'time_txt': {'text': u'27330'}, '_2_4_mc': {'progress_mc': {'currentLabel': u'black_complete'}}}, {'time_txt': {'text': u'27830'}, 'game_over_mc': {'_5_5_mc': {'confirm_mc': {'dispatchEvent': u'mouseDown'}}}}]
ERROR:root:update_family_tree: root property? sequence = [{'time_txt': {'text': u'18580'}, '_1_0_mc': {'currentLabel': u'white'}}, {'time_txt': {'text': u'19580'}, '_1_1_mc': {'currentLabel': u'white'}}, {'_1_2_mc': {'currentLabel': u'white'}, 'time_txt': {'text': u'20580'}}, {'time_txt': {'text': u'21580'}, '_1_3_mc': {'currentLabel': u'white'}}, {'time_txt': {'text': u'22580'}, '_1_4_mc': {'currentLabel': u'white'}}, {'_2_0_mc': {'currentLabel': u'black'}, 'time_txt': {'text': u'23580'}}, {'time_txt': {'text': u'24580'}, '_2_1_mc': {'currentLabel': u'black'}}, {'time_txt': {'text': u'25580'}, '_2_3_mc': {'currentLabel': u'black'}}, {'time_txt': {'text': u'26580'}, '_2_4_mc': {'currentLabel': u'black'}}, {'time_txt': {'text': u'26580'}, '_1_0_mc': {'progress_mc': {'currentLabel': u'white_start'}}}, {'time_txt': {'text': u'26705'}, 'cursor_mc': {'act_mc': {'currentLabel': u'busy'}, 'currentLabel': u'none'}}, {'time_txt': {'text': u'27205'}, 'turn_veil_mc': {'currentLabel': u'other'}}, {'time_txt': {'text': u'27330'}, 'turn_mc': {'currentLabel': u'black', 'white_user_txt': {'text': u'computer_lukasz'}, 'black_user_txt': {'text': u'lukasz'}}}, {'_2_0_mc': {'progress_mc': {'currentLabel': u'black_complete'}}, 'time_txt': {'text': u'27330'}}, {'time_txt': {'text': u'27330'}, '_2_1_mc': {'progress_mc': {'currentLabel': u'black_complete'}}}, {'time_txt': {'text': u'27330'}, '_2_3_mc': {'progress_mc': {'currentLabel': u'black_complete'}}}, {'time_txt': {'text': u'27330'}, '_2_4_mc': {'progress_mc': {'currentLabel': u'black_complete'}}}, {'time_txt': {'text': u'27830'}, 'game_over_mc': {'_5_5_mc': {'confirm_mc': {'dispatchEvent': u'mouseDown'}}}}]
ERROR:root:dispatch_family_tree: root property? sequence = [{'time_txt': {'text': u'18580'}, '_1_0_mc': {'currentLabel': u'white'}}, {'time_txt': {'text': u'19580'}, '_1_1_mc': {'currentLabel': u'white'}}, {'_1_2_mc': {'currentLabel': u'white'}, 'time_txt': {'text': u'20580'}}, {'time_txt': {'text': u'21580'}, '_1_3_mc': {'currentLabel': u'white'}}, {'time_txt': {'text': u'22580'}, '_1_4_mc': {'currentLabel': u'white'}}, {'_2_0_mc': {'currentLabel': u'black'}, 'time_txt': {'text': u'23580'}}, {'time_txt': {'text': u'24580'}, '_2_1_mc': {'currentLabel': u'black'}}, {'time_txt': {'text': u'25580'}, '_2_3_mc': {'currentLabel': u'black'}}, {'time_txt': {'text': u'26580'}, '_2_4_mc': {'currentLabel': u'black'}}, {'time_txt': {'text': u'26580'}, '_1_0_mc': {'progress_mc': {'currentLabel': u'white_start'}}}, {'time_txt': {'text': u'26705'}, 'cursor_mc': {'act_mc': {'currentLabel': u'busy'}, 'currentLabel': u'none'}}, {'time_txt': {'text': u'27205'}, 'turn_veil_mc': {'currentLabel': u'other'}}, {'time_txt': {'text': u'27330'}, 'turn_mc': {'currentLabel': u'black', 'white_user_txt': {'text': u'computer_lukasz'}, 'black_user_txt': {'text': u'lukasz'}}}, {'_2_0_mc': {'progress_mc': {'currentLabel': u'black_complete'}}, 'time_txt': {'text': u'27330'}}, {'time_txt': {'text': u'27330'}, '_2_1_mc': {'progress_mc': {'currentLabel': u'black_complete'}}}, {'time_txt': {'text': u'27330'}, '_2_3_mc': {'progress_mc': {'currentLabel': u'black_complete'}}}, {'time_txt': {'text': u'27330'}, '_2_4_mc': {'progress_mc': {'currentLabel': u'black_complete'}}}, {'time_txt': {'text': u'27830'}, 'game_over_mc': {'_5_5_mc': {'confirm_mc': {'dispatchEvent': u'mouseDown'}}}}]
>>> 
>>> 
>>> 
>>> time.sleep(sloth * 1.489000)
>>> 
>>> 
>>> 
>>> moonhyoung.root.game_over_mc.white_computer_mc.enter_mc.dispatchEvent(mouseDown)
>>> 
>>> 
>>> 
>>> mouse_down_and_sleep(moonhyoung, moonhyoung.root.game_over_mc.start_mc, wait)
ERROR:root:upgrade:  i did not expect old_value: [{'comment_mc': {'_txt': {'text': u'HELLO.  TO START, CLICK LEVEL 1.'}, 'currentLabel': u'comment'}, 'time_txt': {'text': u'20613'}}, {'level_mc': {'_txt': {'text': u'5'}, 'currentLabel': u'up', 'progress_mc': {'currentLabel': u'_79'}}, 'time_txt': {'text': u'21113'}}],  value: [{'time_txt': {'text': u'34504'}, 'game_over_mc': {'white_computer_mc': {'enter_mc': {'currentLabel': u'none'}, 'currentLabel': u'none'}}}]
ERROR:root:update_family_tree: root property? sequence = [{'time_txt': {'text': u'34504'}, 'game_over_mc': {'white_computer_mc': {'enter_mc': {'currentLabel': u'none'}, 'currentLabel': u'none'}}}]
ERROR:root:dispatch_family_tree: root property? sequence = [{'time_txt': {'text': u'34504'}, 'game_over_mc': {'white_computer_mc': {'enter_mc': {'currentLabel': u'none'}, 'currentLabel': u'none'}}}]
ERROR:root:upgrade:  i did not expect old_value: [{'comment_mc': {'_txt': {'text': u'HELLO.  TO START, CLICK LEVEL 1.'}, 'currentLabel': u'comment'}, 'time_txt': {'text': u'16580'}}, {'level_mc': {'_txt': {'text': u'36'}, 'currentLabel': u'up', 'progress_mc': {'currentLabel': u'_43'}}, 'time_txt': {'text': u'17080'}}],  value: [{'time_txt': {'text': u'28455'}, 'cursor_mc': {'act_mc': {'currentLabel': u'busy'}, 'currentLabel': u'none'}}, {'time_txt': {'text': u'28955'}, 'turn_veil_mc': {'currentLabel': u'other'}}, {'time_txt': {'text': u'29080'}, 'turn_mc': {'currentLabel': u'black'}}, {'time_txt': {'text': u'29580'}, 'game_over_mc': {'currentLabel': u'none', 'start_mc': {'currentLabel': u'none'}}}]
ERROR:root:update_family_tree: root property? sequence = [{'time_txt': {'text': u'28455'}, 'cursor_mc': {'act_mc': {'currentLabel': u'busy'}, 'currentLabel': u'none'}}, {'time_txt': {'text': u'28955'}, 'turn_veil_mc': {'currentLabel': u'other'}}, {'time_txt': {'text': u'29080'}, 'turn_mc': {'currentLabel': u'black'}}, {'time_txt': {'text': u'29580'}, 'game_over_mc': {'currentLabel': u'none', 'start_mc': {'currentLabel': u'none'}}}]
ERROR:root:dispatch_family_tree: root property? sequence = [{'time_txt': {'text': u'28455'}, 'cursor_mc': {'act_mc': {'currentLabel': u'busy'}, 'currentLabel': u'none'}}, {'time_txt': {'text': u'28955'}, 'turn_veil_mc': {'currentLabel': u'other'}}, {'time_txt': {'text': u'29080'}, 'turn_mc': {'currentLabel': u'black'}}, {'time_txt': {'text': u'29580'}, 'game_over_mc': {'currentLabel': u'none', 'start_mc': {'currentLabel': u'none'}}}]
>>> 
>>> 
>>> 
>>> moonhyoung.root.comment_mc.none_mc.dispatchEvent(mouseDown)
>>> 
>>> 
>>> 
>>> time.sleep(sloth * 3.219000)
ERROR:root:upgrade:  i did not expect old_value: [{'comment_mc': {'_txt': {'text': u'HELLO.  TO START, CLICK LEVEL 1.'}, 'currentLabel': u'comment'}, 'time_txt': {'text': u'20613'}}, {'level_mc': {'_txt': {'text': u'5'}, 'currentLabel': u'up', 'progress_mc': {'currentLabel': u'_79'}}, 'time_txt': {'text': u'21113'}}],  value: [{'comment_mc': {'none_mc': {'currentLabel': u'none'}, 'currentLabel': u'none'}, 'time_txt': {'text': u'36506'}}]
ERROR:root:update_family_tree: root property? sequence = [{'comment_mc': {'none_mc': {'currentLabel': u'none'}, 'currentLabel': u'none'}, 'time_txt': {'text': u'36506'}}]
ERROR:root:dispatch_family_tree: root property? sequence = [{'comment_mc': {'none_mc': {'currentLabel': u'none'}, 'currentLabel': u'none'}, 'time_txt': {'text': u'36506'}}]
>>> 
>>> 
>>> 
>>> time.sleep(sloth * 2.613000)
>>> 
>>> 
>>> 
>>> mouse_down_and_sleep(moonhyoung, moonhyoung.root._2_2_mc, wait)
>>> 
>>> 
>>> 
>>> computer_moonhyoung.root.pass_mc.dispatchEvent(mouseDown)
>>> 
>>> 
>>> 
>>> moonhyoung.root.comment_mc.none_mc.dispatchEvent(mouseDown)
>>> 
>>> 
>>> 
>>> time.sleep(sloth * 8.528000)
>>> 
>>> 
>>> 
>>> #
>>> 
>>> 
>>> 
>>> #     Mouse over.  See marks on essential stones in pattern.
>>> 
>>> 
>>> 
>>> moonhyoung.root['_2_2_mc']['currentLabel']
'empty_black'
>>> 
>>> 
>>> 
>>> # Expected:
>>> 
>>> 
>>> 
>>> ## 'black'
>>> 
>>> 
>>> 
>>> moonhyoung.root['info_mc']['decoration_mc']['pattern_txt']['text']
''
>>> 
>>> 
>>> 
>>> # Expected:
>>> 
>>> 
>>> 
>>> ## ''
>>> 
>>> 
>>> 
>>> moonhyoung.root['_1_2_mc']['mark_mc']['currentLabel']
'none'
>>> 
>>> 
>>> 
>>> # Expected:
>>> 
>>> 
>>> 
>>> ## 'none'
>>> 
>>> 
>>> 
>>> moonhyoung.root._2_2_mc.dispatchEvent(mouseOver)
>>> 
>>> 
>>> 
>>> time.sleep(sloth * 1.528000)
>>> 
>>> 
>>> 
>>> moonhyoung.root['info_mc']['decoration_mc']['pattern_txt']['text']
''
>>> 
>>> 
>>> 
>>> # Expected:
>>> 
>>> 
>>> 
>>> ## 'CONNECT'
>>> 
>>> 
>>> 
>>> moonhyoung.root['_1_2_mc']['mark_mc']['currentLabel']
'none'
>>> 
>>> 
>>> 
>>> # Expected:
>>> 
>>> 
>>> 
>>> ## 'show'
>>> 
>>> 
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
>>> 