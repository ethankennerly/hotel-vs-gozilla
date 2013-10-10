#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
Utilities for importing and doctesting modules.
'''
__author__ = 'Ethan Kennerly'

import doctest
import sys
import time

def round2(number, precision):
    '''Round number to whole number and fraction / 2^precision.
    Useful for doctest, because floats often don't round with round(...)!
    >>> round2(55.51, 1)
    55.5
    >>> round2(0.70, 2)
    0.75
    
    Because of maximum precision, maximum resolution is 16.
    >>> round2(-4.99, 16)
    -4.9900054931640625
    
    round2 is less precision than actual float, but has no annoying tail.
    >>> -44.99
    -44.990000000000002

    >>> try:
    ...    round2(round2, 1)
    ...    print 'should assert!'
    ... except AssertionError:
    ...    pass
    '''
    assert 0 <= precision and precision <= 16, 'precision of bounds'
    assert int(precision) == precision, 'precision must equal a whole number'
    assert type(number) == float or type(number) == int, 'number must be int or float'
    integer = int(number)
    divisor = 2**precision
    fraction = number - integer
    numerator = float(int(round(fraction * divisor)))
    return numerator / divisor + integer


def round2_for(sequence, precision):
    '''Round each element in sequence to power of 2 and return as list.
    >>> round2_for((0.0, -0.13077017664909363, 0.0), 8)
    [0.0, -0.12890625, 0.0]
    >>> round2_for((0.0, -0.13077017664909363, 0.0), 1)
    [0.0, 0.0, 0.0]
    >>> round2_for((0.0, -0.13077017664909363, 0.0), 2)
    [0.0, -0.25, 0.0]
    '''
    return [round2(number, precision) for number in sequence]


def represent(data, max = 256):
    text = data.__repr__()
    if max < len(text):
        text = text[:max] + '...'
    return text


def basefilename( path ):
    ''' Filename without the path or extension.
    >>> path = u'C:\\learnkorean\\source\\dance.py'
    >>> basefilename( path )
    u'dance'
    >>> basefilename( 'a.b.c.d.e' )
    'a.b.c.d'
    '''
    import os
    basename = os.path.basename( path )
    basefilename = os.path.splitext( basename )[0]
    return basefilename


def import_file( path, locals=locals(), globals=globals(), this_namespace=False ):
    '''Import module at the file in the absolute path.
    >>> import_file( 'C:\Python25\Lib\copy.py', locals(), globals() )
    <module 'copy' from 'C:\Python25\lib\copy.pyc'>
    >>> copy.name
    'CodeType'

    Import to this current namespace
    >>> import_file( 'C:\Python25\Lib\copy.py', locals(), globals(), this_namespace = True ) == __name__
    True
    >>> type(deepcopy)
    <type 'function'>

    Import into child namespace.
    >>> module = import_file( 'C:\Python25\Lib\copy.py', locals(), globals(), this_namespace = False )
    >>> type(module)
    <type 'module'>
    >>> del module
    '''
    import os
    path = os.path.abspath(path)
    dirname = os.path.dirname(path)
    if dirname not in sys.path:
        sys.path.append( dirname )
    os.chdir( dirname )
    module_name = basefilename(path)
    if not this_namespace:
        try:
            exec( 'import ' + module_name, locals, globals )
            return eval( module_name, locals, globals )
        except:
            print 'import failed', module_name, path
            exec( 'import ' + module_name, locals, globals )
    else:
        try:
            exec( 'from ' + module_name + ' import *', locals, globals )
            return __name__
        except:
            print 'from import failed', module_name, path
            exec( 'from ' + module_name + ' import *', locals, globals )
            return module_name


def reload_file(module_file):
    '''Import and reload module file into current namespace.
    >>> module = reload_file('random.py')
    >>> module.__name__
    'random'
    >>> type(module)
    <type 'module'>
    '''
    module = import_file(module_file)
    return reload(module)


def test(path, verbose = False):
    '''Test documented function examples in the module of the file path.
    >>> test( 'code_unit_test.py' ) # doctest: +ELLIPSIS
    <BLANKLINE>
      code_unit_test starts tests. ...
      code_unit_test finished tests. ...
    <BLANKLINE>

    Infinite loop if test test test ... ?
    #>>> test( __file__ )
    '''
    #print
    #print 'file', path
    module_name = basefilename(path)
    module = import_file(path)
    #module = eval(module_name)

    print log_head(module_name)
    doctest.testmod(module, verbose = verbose)
    print log_foot(module_name)


def _doctest_passes():
    '''Silent trivial function with a doctest to test doctest_object.
    >>> _doctest_passes()
    '''

class _example_class(object):
    def _doctest_passes(self):
        '''Silent trivial function with a doctest to test doctest_object.
        >>> _doctest_passes()
        '''

def log_head(unit):
    now = time.asctime(time.localtime(time.time()))
    string = '\n'
    string += '  %s starts tests.    %s' % (unit, now)
    return string


def log_foot(unit):
    now = time.asctime(time.localtime(time.time()))
    return    '  %s finished tests.  %s\n' % (unit, now) 


def doctest_unit(unit, verbose = False, log = True):
    '''Quietly doctest a single, standalone unit in current namespace.
    >>> doctest_unit(_doctest_passes, verbose = False, log = False)
    >>> doctest_unit(_example_class._doctest_passes, verbose = False, log = False)

    Can test a whole module, too, which current retains namespace.  
    But there is no context for this if module is run in current namespace.
    #>>> doctest_unit(code_unit, verbose = False, log = False)
    
    Verbose passes to doctest.  Log wraps output with date/time.
    Doctest complains object not found when defined in a doctest.
    #>>> def a():  '>>> a()';  return None
    #>>> doctest_unit(a)
    '''
    if not is_function_or_class(unit):
        print 'doctest_unit:  This unit is not a class', unit
        return
    if not hasattr(unit, '__name__'):
        print 'doctest_unit:  unit', unit, 'has no __name__.'
        return
    if log:
        print log_head(unit.__name__)
    tests = doctest.DocTestFinder().find(unit)
    runner = doctest.DocTestRunner(verbose = verbose)
    for test in tests:
        runner.run(test)
    if 1 <= runner.failures or verbose:
        runner.summarize(verbose = True)
    if log:
        print log_foot(unit.__name__)



import inspect
def is_function_or_class(object):
    '''
    >>> is_function_or_class(_doctest_passes)
    True
    >>> is_function_or_class(_example_class._doctest_passes)
    True
    >>> is_function_or_class(inspect)
    False
    '''
    return inspect.isfunction(object) or inspect.isclass(object) \
            or inspect.ismethod(object)


def test_example(examples_text, globals_dict):
    '''notify if example was inconsistent.
    >>> def f():  '>>> ___a = 1'
    >>> failures, tests = test_example(f.__doc__, globals())
    >>> failures
    0
    >>> def g():  
    ...     """An inconsistent example.
    ...     >>> ___b = 2
    ...     >>> ___b
    ...     1
    ...     """
    >>> failures, tests = test_example(g.__doc__, globals()) # doctest: +ELLIPSIS
    **************...
    File "...code_unit.py", line 3, in An inconsistent example.
    Failed example:
        ___b
    Expected:
        1
    Got:
        2
    >>> failures, tests
    (1, 2)
    '''
    import doctest
    parser = doctest.DocTestParser()
    test = parser.get_doctest(examples_text,
        globals_dict, examples_text.splitlines()[0], __file__, 0)
    runner = doctest.DocTestRunner()
    return runner.run(test)


class null_output_class(object):
    def write(self, s):
        pass
    
def suppress_stdout_demo():
    '''
    >>> suppress_stdout_demo()
    see first
    see last
    '''
    save_stdout = sys.stdout
    print 'see first'
    sys.stdout = null_output_class()
    print 'no see me'
    sys.stdout = save_stdout
    print 'see last'
    

def inline_examples(examples_text, 
        locals_dict, globals_dict, 
        verify_examples = True):
    r'''Run examples as if in this context.
    Useful to inspect regression and construct by example.
    No output is shown when running.
    >>> def f(x):  '>>> ___a = 1'
    >>> inline_examples(f.__doc__, locals(), globals())
    >>> ___a
    1
    >>> del ___a

    #>>> inline_examples(inline_examples.__doc__, 
    #...     locals(), globals())

    Notify if example is incosistent and do not run.
    >>> def g():  
    ...     """An inconsistent example.
    ...     >>> ___b = 2
    ...     >>> ___b
    ...     1
    ...     """
    >>> inline_examples(g.__doc__, locals(), globals()) # doctest: +ELLIPSIS
    ****************...
    File "...code_unit.py", line 3, in An inconsistent example.
    Failed example:
        ___b
    Expected:
        1
    Got:
        2
    '''
    failures = 0
    if verify_examples:
        failures, tests = test_example(examples_text, 
                globals_dict)
    if 0 == failures:
        save_stdout = sys.stdout
        sys.stdout = null_output_class()
        script = doctest.script_from_examples(examples_text)
        exec(script, locals_dict, globals_dict)
        sys.stdout = save_stdout


def doctest_units(units, verbose = False, log = True, namespace = None):
    '''Test only functions and classes.
    Arguments are passed to doctest_unit.
    >>> doctest_units([doctest, partial_wrapper], log = False)

    If nothing to test, do nothing.
    >>> doctest_units([], log = False)

    Do not test 'from import function' or other modules.
    Those other modules may have test setups that you have not performed.
    >>> from functools import partial
    >>> doctest_units([partial], log = True, namespace = __name__)
    >>> doctest_units([doctest, partial], log = True, namespace = __name__)
    
    Useful to test everything in current namespace.
    #>>> doctest_units(globals().values())
    Avoid recursive tests.  The following can cause infinite loop:
    #>>> doctest_units([doctest_units], log = False)
    '''
    units = filter(is_function_or_class, units)
    if namespace:
        namespace = basefilename(namespace)
        units = filter(lambda unit:  unit.__module__ == namespace, units)
    if not len(units):
        return
    summary = str(len(units)) + ' units [' \
            + str(units[0].__name__) + ' ... ' \
            + str(units[-1].__name__) + ']'
    if log:
        print log_head(summary)
        if not verbose:
            print '  ' + '__ ' * len(units)
            print ' ',
    for unit in units:
        doctest_unit(unit, verbose, log = False)
        if log and not verbose:
            print '^^',
    if log:
        print
        print log_foot(summary)


def test_file_args(path, args, 
        locals_dict, globals_dict):
    '''Test all units in globals or command line options:
    --unit unit_name_in_file
    --debug unit_name_in_file
    >>> import sys
    
    Actual code_unit globals creates infinite loop of doctesting.
    So a mock globals is passed.
    >>> import code_unit_test
    >>> globals_dict = code_unit_test.__dict__ # mock globals()  
    >>> sys_argv = ['./code_unit_test.py']  # mock sys.argv
    >>> test_file_args(sys_argv[0], 
    ...     sys_argv, locals(), globals_dict) # doctest: +ELLIPSIS, +NORMALIZE_WHITESPACE
    <BLANKLINE>
      1 units [add_one ... add_one] starts tests. ...
      __ 
      ^^ 
      1 units [add_one ... add_one] finished tests. ...
    <BLANKLINE>
    >>> sys_argv = ['./code_unit_test.py', '--unit', 'add_one']  # mock sys.argv
    >>> test_file_args(sys_argv[0], 
    ...     sys_argv, locals(), globals()) # doctest: +ELLIPSIS
    <BLANKLINE>
      add_one starts tests. ...
      add_one finished tests. ...
    <BLANKLINE>

    TODO:  Why does doctest debug throw error?
    >>> sys_argv = ['./code_unit_test.py', '--debug', 'add_one']  # mock sys.argv
    >>> test_file_args(sys_argv[0], sys_argv,
    ...     locals(), globals())  # doctest: +SKIP
    '''
    unit_arg = False
    debug_arg = False
    for arg in args:
        if '--unit' == arg:
            unit_arg = True
        elif unit_arg:
            module = import_file(
                    path, locals_dict, globals_dict)
            module_name = basefilename(path)
            exec( 'from ' + module_name + ' import ' + arg )
            unit = eval(arg)
            doctest_unit(unit)
            unit_arg = False
            break
        if '--debug' == arg:
            debug_arg = True
        elif debug_arg:
            import doctest
            module = import_file(
                    path, locals_dict, globals_dict)
            module_name = basefilename(path)
            doctest.debug(module, 
                    module_name+'.'+ arg, True)
            unit_arg = False
            break
    else:
        units = globals_dict.values()
        doctest_units(units)


def partial_wrapper(function, *arguments, **keyword_arguments):
    '''Return partial application with arguments in docstring.
    >>> range(0, 10)
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    >>> range10 = partial_wrapper(range, 0, 10)
    >>> range10()
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    Additional arguments may be passed during the call.
    >>> range(0, 10, 2)
    [0, 2, 4, 6, 8]
    >>> range10(2)
    [0, 2, 4, 6, 8]

    Updates wrapper docstring to show arguments first:
    >>> print range10.__doc__
    partial arguments:  (0, 10)
    partial keywords:  {}
    range([start,] stop[, step]) -> list of integers
    <BLANKLINE>
    Return a list containing an arithmetic progression of integers.
    range(i, j) returns [i, i+1, i+2, ..., j-1]; start (!) defaults to 0.
    When step is given, it specifies the increment (or decrement).
    For example, range(4) returns [0, 1, 2, 3].  The end point is omitted!
    These are exactly the valid indices for a list of 4 elements.

    Omits module for Boost.  Example:
    #>>> step = partial_wrapper(walk.addTime, 0.1)
    '''
    # XXX if in global namespace on python 2.4.3 complain
    import functools
    wrapped_function = functools.partial(function, 
            *arguments, **keyword_arguments)
    if hasattr(wrapped_function, '__module__'):
        wrapped_function = functools.update_wrapper(
                wrapped_function, function)
    else:
        wrapped_function = functools.update_wrapper(
                wrapped_function, function, 
                assigned=('__name__', '__doc__'))
    wrapped_function.__doc__ = \
        'partial arguments:  ' + str(arguments) + '\n' \
        + 'partial keywords:  ' + str(keyword_arguments) + '\n' \
        + str(wrapped_function.__doc__)
    return wrapped_function


def dict_diff(old, new, new_only = False):
    r'''Useful for doctest.
    Adapted from liw.fi at stackoverlow.com python-dict-update-diff
    >>> dict_diff({'a': 1, 'b': 2, 'c': 4},
    ...           {'b': 2, 'a': 1, 'c': 4})
    >>> difference = dict_diff(
    ...           {'foo': 1, 'bar': 2, 'yo': 4},
    ...           {'foo': 0, 'foobar': 3, 'yo': 4})
    >>> expected = {'added': {'foobar': 3},
    ...      'changed': {'foo': {'old': 1, 'new': 0}},
    ...      'removed': {'bar': 2}}
    >>> print_diff(expected, difference)

    Optionally, only report news.
    >>> difference = dict_diff(
    ...           {'foo': {'x': {'xx': 11, 'yy': 0}, 'y': 0}, 'bar': 2, 'yo': 4},
    ...           {'foo': {'x': {'xx': 22, 'yy': 0}, 'y': 1}, 'foobar': 3, 'yo': 4},
    ...             new_only = True)
    >>> expected = {'added': {'foobar': 3},
    ...      'changed': {'foo': {'x': {'xx': 22}, 'y': 1}},
    ...      'removed': {'bar': 2}}
    >>> print_diff(expected, difference)
    '''
    error = []
    if type(old) != dict:
        print 'dict_diff: old is not a dictionary', old
        error.append(a)
    if type(new) != dict:
        print 'dict_diff: new is not a dictionary', new
        error.append(new)
    if error:
        return error
    removed = {}
    added = {}
    changed = {}
    for key, value in old.iteritems():
        if key not in new:
            removed[key] = value
        elif new[key] != value:
            if new_only:
                changed = {key: new[key]}
            else:
                changed[key] = {'old': old[key], 'new': new[key]}
    for key, value in new.iteritems():
        if key not in old:
            added[key] = value
    if removed or added or changed:
        diff = {}
        if removed:
            diff['removed'] = removed
        if added:
            diff['added'] = added
        if changed:
            diff['changed'] = changed
        return diff


def print_diff(old, new):
    difference = dict_diff(old, new)
    if difference:
        import pprint
        pprint.pprint(difference)
        print 'old:'
        pprint.pprint(old)
        print 'new:'
        pprint.pprint(new)


def timeit_inline(minimum_time, function, *args, **kwargs):
    '''Unlike timeit, this times inline.  
    Precise to 1/256 but not accurate like timeit.
    >>> a = 10000
    >>> b = 2
    >>> def f(a):  global b; b = 3; return a + 1
    >>> timeit_inline(0, f, a)
    0.0
    >>> b
    3
    '''
    precision = 256 # power of 2 for accurate rounding
    t0 = time.clock()
    function(*args, **kwargs)
    t1 = time.clock()
    if minimum_time <= timeit_inline:
        return float(int(t1 * precision) \
            - int(t0 * precision)) / precision
    
def eval_file( file_path ):
    '''Open and evaluate a file as Python code.'''
    data = eval( open( file_path, 'r' ).read() ) 
    return data


global _global_variable
_global_variable = 1


def test_global_variables():
    '''Demonstrate global variables for doctest.
    >>> __name__ == '__main__'
    True
    >>> __name__ == 'doctest_test'
    False
    >>> _global_variable
    1
    >>> _global_variable_if_main
    2
    '''
    global _global_variable
    return _global_variable


def wait(seconds):
    '''Wait for a bit.  I used this to prevent threaded doctest from closing window.
    >>> wait(0)
    >>> wait(2)
    Waiting for 2 seconds (or Ctrl-C)
    . .
    '''
    seconds = int(seconds)
    if seconds:
        print 'Waiting for', seconds, 'seconds (or Ctrl-C)'
        time_passed = 0
        try:
            while time_passed < int(seconds):
                time.sleep(1)
                time_passed += 1
                print '.',
                if 0 == (time_passed % 60):
                    print
        except KeyboardInterrupt:
            print 'Keyboard interrupted at %s seconds' % seconds



from threading import Thread
class concurrent(Thread):
    '''Non-blocking, deferrable like a function object.
    >>> def after_two_seconds_add(a, b):  
    ...     time.sleep(2)
    ...     print a + b
    ...     return a + b
    >>> concurrent_add = concurrent(
    ...     after_two_seconds_add, 1, 1)
    >>> concurrent_add.start()
    >>> time.sleep(1)
    >>> time.sleep(1)
    2
    >>> concurrent_add = concurrent(
    ...     after_two_seconds_add, 2, 2)
    >>> concurrent_add.start()
    >>> time.sleep(1)
    >>> time.sleep(1)
    4
    '''
    def __init__(self, function, *args, **kwargs):
        Thread.__init__(self)
        self.function = function
        self.args = args
        self.kwargs = kwargs
    def run(self):
        try:
            self.function(*self.args, **self.kwargs)
        except:
            print 'concurrent exception %s, %s, %s' \
                    % (self.function, self.args, self.kwargs)
            import sys
            import traceback
            traceback.print_exception(*sys.exc_info())
            self.function(*self.args, **self.kwargs)
            raise


def concurrently(function):
    '''Convert a blocking function to non-blocking.
    >>> def after_two_seconds_add(a, b):  
    ...     time.sleep(2)
    ...     print a + b
    ...     return a + b
    >>> concurrently_add = concurrently(
    ...     after_two_seconds_add)
    >>> concurrently_add(1, 1)
    >>> time.sleep(1)
    >>> time.sleep(1)
    2
    
    >>> concurrently_add(2, 2)
    >>> time.sleep(1)
    >>> time.sleep(1)
    4
    '''
    def _concurrent(*args, **kwargs):
        concurrent_function = concurrent(
                function, *args, **kwargs)
        concurrent_function.start()
    return _concurrent




if __name__ == '__main__':
    global _global_variable_if_main
    _global_variable_if_main = 2
    import sys
    test_file_args('code_unit.py', sys.argv, locals(), globals())
    # doctest_units(globals().values())
    #Pdb doesn't like __file__, so substitute file path.
    #test(__file__)
    #test('code_unit.py')

