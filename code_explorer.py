#!/usr/bin/python
# -*- coding: utf-8 -*-

'''Proof of concept for a lightweight PythonCard user interface to monitor 
and edit Python code and a running application.  
'''
__author__ = 'Ethan Kennerly'
__date__ = '2008-01-31'

from PythonCard import model, configuration, clipboard
import code_unit
import os


def open_dialog():
    '''Conveniently open file inline.
    >>> open_dialog() #doctest: +SKIP
    '''
    result = dialog.openFileDialog()
    if result.accepted:
        return result.paths[0]


def import_to_global(globals, name):
    '''Import name into global namespace in a way that doctest likes.
    >>> module_name = code_unit.import_file( 'code_unit.py', locals(), globals(), this_namespace = True)
    >>> assert doctest_units
    >>> new_test = import_to_global(globals(), 'doctest_units')
    >>> assert new_test == doctest_units
    '''
    if not name in globals.keys() and name.capitalize() in globals.keys():
        globals[name] = globals[name.capitalize()]
    return globals[name]


def get_history_text(shell_history):
    r'''Reverse a list and join as a multiline string.
    >>> history = ['b', 'a']
    >>> print get_history_text(history)
    a
    b
    <BLANKLINE>

    Live shell history is auto-updated, when commands are typed into shell.
    #>>> get_history_text(shell.other.history)
    #>>> u"a\nb\nshell.other.history = ['b', 'a']\n"
    '''
    history_text = u''
    for index in range(len(shell_history)-1, -1, -1):
            history_text += shell_history[index] + u'\n'
    return history_text


def save_shell_history(shell_history, file_path):
    r'''Save shell history to file.
    >>> history = ['b', 'a']
    >>> history_file_name = 'save_shell_test.history.py'
    >>> save_shell_history(history, history_file_name)
    >>> file = open(history_file_name, 'r')
    >>> print file.read()
    a
    b
    <BLANKLINE>
    >>> file.close()
    >>> import os
    >>> os.remove(history_file_name)
    
    Live shell example.  I don't know how to get 'shell' in doctest:
    #>>> save_shell_history(shell.other.history, 'session_2008-09-06.history.py')
    '''
    file = open(file_path, 'w')
    file.write(get_history_text(shell_history))
    file.close()


def save(shell, file_name='code_explorer.shell.py'):
    '''Save shell input and output with ">>>" prompts.
    #>>> save(shell)
    '''
    shell_text = shell.other.GetText()
    file = open(file_name, 'w')
    file.write(shell_text)
    file.close()
    

def shell_run_lines(shell, code_text):
    r'''Run commands as if typed into shell in sequence.  
    Each command is on a separate line.
    #>>> shell_run_lines(shell, 'print "1"\nprint "2"')
    #automatic#>>> print "1"
    1
    #automatic#>>> print "2"
    2

    Do NOT call directly from clipboard.  This calls recursively.
    #>>> clipboard.setClipboard('print "clipping"')
    #>>> shell_run_lines(shell, clipboard.getClipboard())

    Instead assign clipboard to data.
    '''
    file = open('__temporary__.history.py', 'w')
    file.write(code_text)
    file.close()
    shell.runfile('__temporary__.history.py')
    os.remove('__temporary__.history.py')

run = shell_run_lines


run_snippet_example = \
'''if True:
    print 2
print 3'''

run_snippet2_example = \
'''if True: print 2
print 3'''

run_snippet3_example = \
'''def f(a): print a
print 3'''

def run_snippet(shell, snippet):
    '''Run multiple lines as if typed in shell.
    To avoid pyshell syntax error, inserts extra line when dedenting.
    #>>> run_snippet(shell, run_snippet_example)
    #>>> run_snippet(shell, run_snippet2_example)
    #>>> run_snippet(shell, run_snippet3_example)
    '''
    for line in snippet.split('\n'):
        shell.run('\n')
        shell.run(line)


def run_examples(shell, examples):
    '''run doctest examples as if typed in shell.
    >>> if globals().get('shell'):
    ...     run_examples(shell, run_examples.__doc__, trace_code = False)
    '''
    import doctest
    script = doctest.script_from_examples(examples)
    run_snippet(shell, script)


def run_file_examples(shell, filename):
    '''
    >>> if globals().get('shell'):
    ...     run_file_examples(shell, 'code_explorer_example.txt')
    '''
    import text
    examples_text = text.load(filename)
    run_examples(shell, examples_text)


def debug_snippet(shell, snippet, trace_code = True):
    '''Debug multiple lines as if typed in shell.'''
    import pdb
    for line in snippet.split('\n'):
        if trace_code:
            pdb.set_trace()
        shell.run(line)


def debug_examples(shell, examples, trace_code = True):
    '''Debug doctest examples as if typed in shell.
    >>> if globals().get('shell'):
    ...     debug_examples(shell, debug_examples.__doc__, trace_code = False)
    '''
    import doctest
    script = doctest.script_from_examples(examples)
    debug_snippet(shell, script, trace_code=trace_code)


interactive_debug_doc = r"""
This is an interactive example, where Pdb input is provided by user, so this example does not run as a doctest.
>>> def get_hours():  
...     '''
...     >>> hours = get_hours()
...     >>> hours
...     [0, 1, ..., 22, 23]
...     '''
...     return range(24)
...     
>>> hours_snippet = doctest.script_from_examples(get_hours.__doc__)
>>> debug_snippet(shell, hours_snippet)
> <input>(8)debug_snippet()
(Pdb) c
>>> hours = get_hours()
>>> > <input>(8)debug_snippet()
(Pdb) hours.pop()
23
(Pdb) hours.reverse()
(Pdb) c
>>> hours
[22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
>>> > <input>(8)debug_snippet()
(Pdb) c
>>> # Expected:
>>> > <input>(8)debug_snippet()
(Pdb) c
>>> ## [0, 1, ..., 22, 23]
>>> > <input>(8)debug_snippet()
(Pdb) c
>>> 
>>> 
>>> 

Another interactive example, in which
we stop tracing the code.
>>> debug_snippet(shell, hours_snippet)
> <input>(8)debug_snippet()
(Pdb) c
>>> hours = get_hours()
>>> > <input>(8)debug_snippet()
(Pdb) trace_code
True
(Pdb) trace_code = False
(Pdb) c
>>> hours
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]
>>> 
>>> # Expected:
>>> 
>>> ## [0, 1, ..., 22, 23]
>>> 
>>> 
"""



def shell_run_clipboard(shell):
    '''Run contents of clipboard as shell commands.  
    Careful what you run!
    #>>> clipboard.setClipboard('print "clipping"')
    #>>> shell_run_clipboard(shell)
    #>>> print "clipping"
    #clipping

    It will freeze on inputs that freeze execution, 
    such as rendering Ogre indefinitely.
    '''
    lines_string = clipboard.getClipboard()
    shell_run_lines(shell, lines_string)


from threading import Thread
import time
import shutil
import os
class save_shell_thread_class(Thread):
    '''Auto-save every few seconds.
    Three backup copies, 3 is oldest, 1 is newest.''' 
    def __init__(self, shell, period=10, 
            base_name='code_explorer_auto_save'):
        Thread.__init__(self)
        self.shell = shell
        self.period = period
        self.base_name = base_name
    def run(self):
        # Three backup copies, 3 is oldest, 1 is newest.
        if os.path.exists(self.base_name + '2.shell.py'):
            shutil.copy2(self.base_name + '2.shell.py', 
                self.base_name + '3.shell.py')
        if os.path.exists(self.base_name + '1.shell.py'):
            shutil.copy2(self.base_name + '1.shell.py', 
                self.base_name + '2.shell.py')
        if os.path.exists(self.base_name + '.shell.py'):
            shutil.copy2(self.base_name + '.shell.py', 
                self.base_name + '1.shell.py')
        while self.shell:
            save(self.shell, self.base_name + '.shell.py')
            time.sleep(self.period)

shell_rc = '''
shell.other.autoCompleteIncludeSingle = True
shell.other.autoCompleteIncludeDouble = True
from pprint import pprint
'''

class background_class(model.Background):
    '''PythonCard user interface for exploring code.
    >>> configuration.setOption('showShell', True)
    >>> application = model.Application( background_class )
    >>> background = application.backgrounds[0]
    >>> background.on_initialize(None)
    >>> del background
    >>> del application
    '''
    import_file = None
    snippet_string_variable = None
    example_string_variable = None
    start_rc = 'shell_rc'
    def on_initialize(self, event):
        self.node = None
        self.graphics = None
        self.color = None
        if background_class.import_file:
            self.import_here( 
                    background_class.import_file, locals(), globals() )
        if globals().get('shell'):
            global shell
            save_shell_thread = save_shell_thread_class(shell)
            save_shell_thread.start()
            if background_class.start_rc:
                import time
                time.sleep(1.0 / 8)
                run_snippet(shell, eval(background_class.start_rc))
            if background_class.snippet_string_variable:
                import time
                time.sleep(1.0 / 8)
                run_snippet(shell, 
                    eval(background_class.snippet_string_variable))
            if background_class.example_string_variable:
                import time
                time.sleep(1.0 / 8)
                run_examples(shell, 
                    eval(background_class.example_string_variable).__doc__)

    def import_here(self, file, locals, globals):
        '''Import from file into this namespace.
        TODO:  import relative to calling directory.
        c:/project/lifeanddeath>../python/code_explorer.py --import referee.py'''
        # TODO:  Export to global namespace.  Troubleshoot globals error.
        # Often times, I want to script in the shell in the same namespace.
        # XXX I seem to recall this method must be in PythonCard background.
        #import os
        #if os.path.dirname(file):
        #    os.chdir(os.path.dirname(
        #        os.path.abspath(file)))
        app_module_name = code_unit.import_file( file, locals, globals, 
                this_namespace = True )
        import time
        time.sleep(0.125)
        if 'on_start_shell' in globals and 'shell' in globals:
            run(shell, on_start_shell)

    def on_menuFileImport_select(self, event):
        result = dialog.openFileDialog(
                title='Import * Python module into this namespace', directory='.', wildcard='*.py')
        if result.accepted:
            file = result.paths[0]
            self.import_here(
                    file, locals(), globals())

    def on_import_mouseClick(self, event):
        self.on_menuFileImport_select(event)

    def on_menuFileReload_select(self, event):  
        '''Reload module from a file.
        '''
        result = dialog.openFileDialog(
                title='Reload a Python module', directory='.', wildcard='*.py')
        if result.accepted:
            module_file = result.paths[0]
            code_unit.reload_file(module_file)

    def on_reload_module_mouseClick(self, event):
        self.on_menuFileReload_select(event)

    def on_menuFileSaveShellHistory_select(self, event):  
        '''Save all input to the shell.  
        Useful to prevent retyping and to start making notes for a new function.
        Sometimes errors (like traceback) that appear on a 
        shell input line are also saved, which corrupts loading those files.  
        Inspect the file.
        '''
        if 'shell' not in globals():
            print 'no shell history exists to save'
            return
        result = dialog.saveFileDialog(
                title='Save shell history file (your input only)', 
                directory='.', wildcard='*.history.py')
        if result.accepted:
            shell_file = result.paths[0]
            save_shell_history(shell.other.history, shell_file)

    def on_saveShellHistory_mouseClick(self, event):
        self.on_menuFileSaveShellHistory_select(event)
    
    def on_menuFileSaveShell_select(self, event):  
        if 'shell' not in globals():
            print 'no shell history exists to save'
            return
        result = dialog.saveFileDialog(
                title='Save shell >>> input and output file', 
                directory='.', filename = 'code_explorer.shell.py', 
                wildcard='*.shell.py')
        if result.accepted:
            shell_file = result.paths[0]
            save(shell, shell_file)

    def on_saveShell_mouseClick(self, event):
        self.on_menuFileSaveShell_select(event)

    def on_menuFileLoadShellHistory_select(self, event):  
        '''Conveniently load a saved shell file into the current shell.  
        Useful to recover an example.
        Replaying the shell is stopped by any command that locks control, 
        such as Ogre's root.startRendering(), so when an application runs, 
        no other commands are executed.
        '''
        if 'shell' not in globals():
            print 'no shell exists to load'
            return
        result = dialog.openFileDialog(
                title = 'Load and EXECUTE shell history file', 
                directory = '.', wildcard = '*.history.py')
        if result.accepted:
            shell_file = result.paths[0]
            shell.runfile(shell_file)


def main():
    configuration.setOption('showShell', True)
    configuration.setOption('showDebug', True)
    # Precondition:  Configuration options in configuration.configDict set.
    pythoncard_app = model.Application(background_class)
    pythoncard_app.MainLoop()
    background = pythoncard_app.backgrounds[0]


if __name__ == '__main__':
    # Default behavior when executed directly
    # PythonCard built-in options
    #     -d:  debug
    #     -s:  shell
    from optparse import OptionParser
    parser = OptionParser()
    parser.add_option('-t', '--test', default=False,
        dest='test', help='test me [default: %default]')
    parser.add_option('-i', '--import', default='',
        dest='import_file', help='from module import * [default: %default]')
    parser.add_option('-p', '--snippet', default='',
        dest='snippet', help='run_snippet [default: %default]')
    parser.add_option('-e', '--example', default='',
        dest='example', help='run_examples [default: %default]')
    (options, args) = parser.parse_args()

    if options.import_file:
        background_class.import_file = options.import_file
    if options.snippet:
        background_class.snippet_string_variable = options.snippet
    if options.example:
        background_class.example_string_variable = options.example
    if options.test:
        code_unit.test(__file__)
    else:
        main()

    #import_arg = False
    #snippet_arg = False
    #for arg in sys.argv:
    #    if arg == '--test':
    #        code_unit.test(__file__)
    #        break
    #    elif arg == '--import':
    #        import_arg = True
    #    elif import_arg:
    #        background_class.import_file = arg
    #        import_arg = False
    #    elif arg == '--snippet':
    #        snippet_arg = True
    #    elif snippet_arg:
    #        background_class.snippet_string_variable = arg
    #        snippet_arg = False
    #else:
    #    main()

