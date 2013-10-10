#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Convert a little bit of brittle syntax from Python to ActionScript.
Only filters keywords, pairs, and literals listed below.  
I share algorithms between Python server and ActionScript client.
In vim, I filter the ActionScript compatible Python through this script.

ActionScript references object like python references dictionary
with a few minor inconsistencies, such as '.get',
which is close to ActionScript [], since undefined value may be returned.
For examples, see python3_text and actionscript3_text.

List comprehensions not supported.
    >>> lines = 'globe.schedule_list = [s for s in globe.schedule_list if s]'
    >>> print python_to_actionscript(lines)
    globe.schedule_list = [s for (var s in globe.schedule_list if s])

The cumbersome alternative is shown in python_list_comprehension_text.

Although I could loop over index through a list.
To conveniently loop over a list, I hacked for each in python_for_each_text.

ActionScript gotcha (gotme, at least).
        expect:
            if (schedule[0]['sequence'] != []){
        workaround:
            if (schedule[0]['sequence'] is Array){

I do not support nesting function calls.  
For a faulty example, see actionscript2_text.

Beware!  Garbles list-comprehension:
    [c.name for c in children if c.name == 'main_mc']
To limit garbling, Python "for ... in" must be on single line.


WISHLIST

-1 update_family_tree.  trace spam.  distracted.
    logging.info, logging.error to equivalent trace with log level.
-0 python only code block, commented out in ActionScript
-1 ActionScript Array in Python.  
    (   '(\\S+) in (\\S+)',    '0 <= \\2.indexOf(\\1)'     ),
    new Array()
    [] constructs Array.
"""
__author__ = 'Ethan Kennerly'

keywords = {
    'def': 'function',
    'del': 'delete',
    # Hack: var a = 0;
    'var =': 'var',
    # Hack: a = new Array;
    'new =': 'new',
    'elif': 'else if',
    'is not': '!==',
    'is': '===',
    'not': '!',
    'and': '&&',
    'or': '||',
    'None': 'null',
}

methods = {
    # string : String
    'find': 'indexOf',
    # list : Array
    'append': 'push',
}

pairs = {
    "'''": ['/*', '*/'],
    '"""': ['/*', '*/'],
}

expressions = [
    (   '\\.get\\(([^\\)]+)\\)',    '[\\1]'     ),
    (   'type\\(([^ ]+)\\) == ',    '\\1 is '     ),
    (   'len\\(([^\\)]+)\\)',    '\\1.length'     ),
    (   'str\\(([^\\)]+)\\)',    '\\1.toString()'     ),
    (   'for (\\S+) in range\\(([^\\)]+)\\)',    'for (var \\1 = 0; \\1 < \\2; \\1++)'     ),
    # (   'for each_',    'for each each_'     ),
    (   'for (each_\\S+) in ([^:{]+)',    'for each (var \\1 in \\2)'     ),
    (   'for (\\S+) in ([^:{\\n]+)',    'for (var \\1 in \\2)'     ),
    #(   'logging\\.\\(([^\\(]+)\\((.)',    'trace(\\2\\1:'     ),
    (   'logging\\.([^\\(]+)\\((.)',    'trace("\\1:" + \\2'     ),
]

literals = [
    (   'float('     ,   'Number('        ),
    (   '#'     ,   '//'        ),
    (   ':\n'   ,   '{\n'       ),
    (   'pop(0)'   ,   'shift()'       ),
    (   '(globe, '   ,   '('       ),
    (   '(globe)'   ,   '()'       ),
    (   '(self, '   ,   '('       ),
    (   '(self)'   ,   '()'       ),
    (   '\\'        ,   ''       ),
    (   '//.as:uncomment: ', '' ),
    (   "r'''", "'''" ),
    (   'r"""', '"""' ),
    #(   '\n'   ,   ';\n'      ),
    #(   '(;\n'   ,   '(\n'      ),
    #(   '[;\n'   ,   '[\n'      ),
    #(   '{;\n'   ,   '{\n'      ),
]

python_text = r"""
    def listen_to_lobby(globe):
        '''add event listeners
        >>> listen_to_lobby(globe)

        '''
        globe.root.lobby_mc.main_mc._00_mc.addEventListener(
                MouseEvent.MOUSE_DOWN, globe.grandparent_goto_mc_name);
        #globe.root.lobby_mc.main_mc._10_mc.addEventListener(
        #        MouseEvent.MOUSE_DOWN, globe.grandparent_goto_mc_name);
        del globe.root['lobby_mc']['main_mc'];
        globe.root.cursor_mc.mouseChildren = false;
        var = a = true;
        if (not a and (b or c)):
            a = false or a;

def listen_to_lobby2(globe):
    globe.root.lobby_mc.main_mc._00_mc.addEventListener(
            MouseEvent.MOUSE_DOWN, globe.grandparent_goto_mc_name);
del globe.root['lobby_mc']['_00_mc'];
"""

actionscript_text = r"""
    function listen_to_lobby(){
        /*add event listeners
        >>> listen_to_lobby()

        */
        globe.root.lobby_mc.main_mc._00_mc.addEventListener(
                MouseEvent.MOUSE_DOWN, globe.grandparent_goto_mc_name);
        //globe.root.lobby_mc.main_mc._10_mc.addEventListener(
        //        MouseEvent.MOUSE_DOWN, globe.grandparent_goto_mc_name);
        delete globe.root['lobby_mc']['main_mc'];
        globe.root.cursor_mc.mouseChildren = false;
        var a = true;
        if (! a && (b || c)){
            a = false || a;
        } // if
    } // function listen_to_lobby

function listen_to_lobby2(){
    globe.root.lobby_mc.main_mc._00_mc.addEventListener(
            MouseEvent.MOUSE_DOWN, globe.grandparent_goto_mc_name);
} // function listen_to_lobby2
delete globe.root['lobby_mc']['_00_mc'];
"""

python2_text = r"""
def me(globe):
    r'''Send child indices...'''
    [c.name for c in children if c.name == 'main_mc']
    var = child_count = parent_mc.numChildren;
    for c in range(child_count):
        var = i = string.find("s");
        trace(str(float(len(string))));
        globe.ambassador.sends.append(c);
        #.as:uncomment: trace(i); # HACK AS only
"""

# garbles list-comprehension
actionscript2_text = r'''
function me(){
    /*Send child indices...*/
    [c.name for (var c in children if c.name == 'main_mc'])
    var child_count = parent_mc.numChildren;
    for (var c = 0; c < child_count; c++){
        var i = string.indexOf("s");
        trace(Number(string.length.toString()));
        globe.ambassador.sends.push(c);
        trace(i); // HACK AS only
    } // for
} // function me
'''



python3_text = r'''
    for key in news:
        trace(news[key] \
            + ':' + str(key));
        if (type(news.get(key)) == Object):
            for k in news[key]:
                trace(k);
        elif (key in news):
            trace(news[key]);
        else:
            trace(news);
'''

actionscript3_text = r'''
    for (var key in news){
        trace(news[key] 
            + ':' + key.toString());
        if (news[key] is Object){
            for (var k in news[key]){
                trace(k);
            } // for
        } else if (0 <= news.indexOf(key)){
            trace(news[key]);
        } else{
            trace(news);
        } // if
    } // for
'''

python_list_comprehension_text = r'''
var = new_schedule_list = [];
for s in globe.schedule_list:
    if (1 <= len(s)):
        new_schedule_list.append(s);
globe.schedule_list = new_schedule_list;
'''

actionscript_list_comprehension_text = r'''
var new_schedule_list = [];
for (var s in globe.schedule_list){
    if (1 <= s.length){
        new_schedule_list.push(s);
    } // if
} // for
globe.schedule_list = new_schedule_list;
'''

python_for_each_text = r'''
for each_schedule in globe.schedule_list:
    if (None != each_schedule and each_schedule[0] is not None):
        var = event = each_schedule.pop(0);
        logging.info('schedule:' + str(event));
        # XXX Gotcha ActionScript requires 'new MouseEvent' 
        # but does not bark while compiling
        var = mouse_event = new = MouseEvent(MouseEvent.MOUSE_DOWN);
'''

actionscript_for_each_text = r'''
for each (var each_schedule in globe.schedule_list){
    if (null != each_schedule && each_schedule[0] !== null){
        var event = each_schedule.shift();
        trace("info:" + 'schedule:' + event.toString());
        // XXX Gotcha ActionScript requires 'new MouseEvent' 
        // but does ! bark while compiling
        var mouse_event = new MouseEvent(MouseEvent.MOUSE_DOWN);
    } // if
} // for
'''

def replace_method(string, old, new):
    r'''
    >>> print replace_method('string.find("s")', 'find', 'indexOf')
    string.indexOf("s")
    '''
    return string.replace(old, new)

import re
def replace_keyword(string, old, new):
    r'''
    >>> print replace_keyword('del a', 'del', 'delete')
    delete a
    >>> print replace_keyword('    del a', 'del', 'delete')
        delete a

    Hack declare ActionScript var
    >>> print replace_keyword('var = undefined = None\nvar; a = true;', 'var;', 'var')
    var = undefined = None
    var a = true;
    >>> print replace_keyword('var = a = true;', 'var =', 'var')
    var a = true;

    Hack 'not' and None
    >>> print replace_keyword('if (not a)', 'not', '!')
    if (! a)
    >>> print replace_keyword('if (a != None)', 'None', 'null')
    if (a != null)
    '''
    global_keyword = re.compile('^%s ' % old, re.M)
    keyworded = global_keyword.sub('%s ' % new, string)
    keyworded = keyworded.replace(' %s ' % old, ' %s ' % new)
    # HACK:  (not
    keyworded = keyworded.replace('(%s ' % old, '(%s ' % new)
    keyworded = keyworded.replace(' %s)' % old, ' %s)' % new)
    return keyworded

def replace_expression(string, old, new):
    r'''
    >>> python = 'for (\\S+) in range\\(([^\\)]+)\\)'
    >>> actionscript = 'for (var \\1 = 0; \\1 < \\2; \\1++)'
    >>> print replace_expression('for c in range(child_count):', python, actionscript)
    for (var c = 0; c < child_count; c++):
    '''
    expression = re.compile(old, re.M)
    expressioned = expression.sub(new, string)
    return expressioned

def replace_pair(string, old, news):
    """
    >>> print replace_pair("'''a''', '''b'''", "'''", ['/*', '*/']) 
    /*a*/, /*b*/
    >>> print replace_pair("'''a''', '''b", "'''", ['/*', '*/']) 
    /*a*/, /*b
    """
    paired = string
    while old in paired:
        for new in news:
            if old in paired:
                paired = paired.replace(old, new, 1)
    return paired

# import os
# os.chdir(r'C:/Python25/Tools/Scripts')
import pindent

def bracket_dedent(string):
    r'''
    >>> python = 'def f():\n    pass\n\n'
    >>> print bracket_dedent(python)
    def f(){
        pass
    } // def f
    <BLANKLINE>
    <BLANKLINE>

    Expand tabs to four spaces.
    >>> python = '    def f():\n        (0,\n            1)\n\n'
    >>> print bracket_dedent(python)
        def f(){
            (0,
                1)
        } // def f
    <BLANKLINE>
    <BLANKLINE>

    Beware elif is bracketed.
    >>> python = 'if (0):\n    0\nelif (1):\n    1\nelse:\n    2\n\n'
    >>> print bracket_dedent(python)
    if (0){
        0
    } elif (1){
        1
    } else{
        2
    } // if
    <BLANKLINE>
    <BLANKLINE>

    From:
    http://stackoverflow.com/questions/118643/is-there-a-way-to-convert-indentation-in-python-code-to-braces
    '''
    pindented = pindent.complete_string(string, stepsize=4, tabsize=4, 
            expandtabs=1)
    bracketed = pindented.replace('# end ', '} // ')
    bracketed = bracketed.replace(   ':\n'   ,   '{\n'       )
    bracketed = bracketed.replace('elif', '} elif')
    bracketed = bracketed.replace('else{', '} else{')
    return bracketed


import difflib
def invalid(python_text, actionscript_text):
    '''
    >>> print invalid(python3_text, actionscript3_text)
    None
    >>> print invalid(python_list_comprehension_text, actionscript_list_comprehension_text)
    None
    >>> print invalid(python_for_each_text, actionscript_for_each_text)
    None
    '''
    invalid = ''
    output = python_to_actionscript([python_text, ''])
    if not actionscript_text == output:
        diff = difflib.ndiff(actionscript_text.splitlines(), output.splitlines())
        for d in diff:
            invalid += d + '\n'
    if invalid:
        return invalid

def python_to_actionscript(lines):
    '''
    >>> output = python_to_actionscript([python_text, ''])
    >>> if not actionscript_text == output:
    ...     print 'expected:'
    ...     print actionscript_text
    ...     print 'got:'
    ...     print output
    ...     diff = difflib.ndiff(actionscript_text.splitlines(), output.splitlines())
    ...     for d in diff:
    ...         d
    >>> output2 = python_to_actionscript([python2_text, ''])
    >>> if not actionscript2_text == output2:
    ...     diff = difflib.ndiff(actionscript2_text.splitlines(), output2.splitlines())
    ...     for d in diff:
    ...         d
    >>> output3 = python_to_actionscript([python3_text, ''])
    >>> if not actionscript3_text == output3:
    ...     diff = difflib.ndiff(actionscript3_text.splitlines(), output3.splitlines())
    ...     for d in diff:
    ...         d
    '''
    text = ''.join(lines)
    processed = text
    for python, actionscript in literals:
        processed = processed.replace(python, actionscript)
    #for python, actionscript in preprocess_literals.items():
    #    processed = processed.replace(python, actionscript)
    processed = bracket_dedent(processed)
    for python, actionscript in keywords.items():
        processed = replace_keyword(processed, python, actionscript)
    for python, actionscript in methods.items():
        processed = replace_method(processed, python, actionscript)
    for python, actionscript in pairs.items():
        processed = replace_pair(processed, python, actionscript)
    for python, actionscript in expressions:
        processed = replace_expression(processed, python, actionscript)
    return processed

if '__main__' == __name__:
    import sys
    option = sys.argv[1:]
    if option == ['--test']:
        print '\n\npy2as.py starts testing...'
        import doctest
        doctest.testmod()
        print 'py2as.py finishes testing'
    else:
        lines = sys.stdin.readlines()
        print python_to_actionscript(lines)

