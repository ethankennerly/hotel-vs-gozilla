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
>>> [].index('a')
Traceback (most recent call last):
  File "<input>", line 1, in <module>
ValueError: list.index(x): x not in list
>>> 'a' in []
False
>>> 