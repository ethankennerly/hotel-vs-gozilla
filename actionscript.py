#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Mock ActionScript library
'''
__author__ = 'Ethan Kennerly'

undefined = None
true = True
false = False
null = None

def mock_actionscript_object_example():
    '''In order to model the ActionScript client, 
    and easily port code to ActionScript, there is a mock:
        MovieClip, SimpleButton and TextField.

    Hacked approximation.  not really the same as ActionScript null.
    >>> print undefined
    None

    Refer to attribute or child as dictionary.
    >>> root = get_example_stage()
    >>> root['title_mc']['username_txt']['text']
    'user'
    >>> root['title_mc']['username_txt']['currentLabel']
    <type 'exceptions.ReferenceError'>

    Refer to attribute or child as dictionary.
    >>> root = get_example_stage()
    >>> root['title_mc']['username_txt']['text']
    'user'
    >>> root['title_mc']['username_txt']['text'] = 'joris'
    >>> root['title_mc']['username_txt']['text']
    'joris'
    >>> root['title_mc']['username_txt']['t'] = 'joris'
    Traceback (most recent call last):
      ...
    ReferenceError
    >>> root['title_mc']['username_txt']['t']
    <type 'exceptions.ReferenceError'>

    Refer to attribute or child as dictionary.
    >>> root = get_example_stage()
    >>> root['gateway_mc']['currentLabel']
    'none'
    >>> root['gateway_mc'].currentLabel
    'none'
    >>> root['gateway_mc']['label']
    <type 'exceptions.ReferenceError'>

    Refer to attribute or child as attribute.
    >>> root = get_example_stage()
    >>> root.gateway_mc.currentLabel
    'none'

    Careful, you define attributes that did not exist,
    whereas ActionScript cannot for SimpleButton.
    >>> root.gateway_mc.nonesuch = 2

    Refer to root of an offspring.
    >>> if not root == root.game_over_mc.start_mc.root:
    ...     root.name, root.game_over_mc.start_mc.root.name

    Dispatch event log
    >>> old_log_level = logging.getLogger().level
    >>> logging.getLogger().setLevel(logging.WARNING)
    >>> mouseDown = MouseEvent(MouseEvent.MOUSE_DOWN)
    >>> root.title_mc.start_btn.dispatchEvent(mouseDown)
    trace_event: mouseDown
    >>> logging.getLogger().setLevel(old_log_level)

    Currently if target has no event listener, then 
    unlike Flash, this mock model does NOT bubble event to ancestors.
    >>> button = SimpleButton()
    >>> button.name = 'no_listener_btn'
    >>> root.title_mc.addEventListener(MouseEvent.MOUSE_DOWN, trace_event)
    >>> root.title_mc.dispatchEvent(mouseDown)
    trace_event: mouseDown

    Like Flash, multiple events may be added.
    >>> root.title_mc.addEventListener(MouseEvent.MOUSE_OVER, trace_event)
    >>> root.title_mc.dispatchEvent(mouseDown)
    trace_event: mouseDown
    >>> mouseOver = MouseEvent(MouseEvent.MOUSE_OVER)
    >>> root.title_mc.dispatchEvent(mouseOver)
    trace_event: mouseOver

    Unlike Flash, adding the same event again overwrites that event.
    >>> root.title_mc.addEventListener(MouseEvent.MOUSE_DOWN, trace_event)
    >>> root.title_mc.dispatchEvent(mouseDown)
    trace_event: mouseDown
    >>> def trace_event2(event):  
    ...     print 'trace_event2:', event.type
    >>> root.title_mc.addEventListener(MouseEvent.MOUSE_DOWN, trace_event2)
    >>> root.title_mc.dispatchEvent(mouseDown)
    trace_event2: mouseDown
    >>> root.title_mc.dispatchEvent(mouseOver)
    trace_event: mouseOver

    Mouse out is also supported.
    >>> root.title_mc.addEventListener(MouseEvent.MOUSE_OUT, trace_event)
    >>> mouseOut = MouseEvent(MouseEvent.MOUSE_OUT)
    >>> root.title_mc.dispatchEvent(mouseOut)
    trace_event: mouseOut

    >>> root.title_mc.addChild(button)
    >>> old_log_level = logging.getLogger().level
    >>> logging.getLogger().setLevel(logging.ERROR)
    >>> root.title_mc.no_listener_btn.dispatchEvent(mouseDown)
    >>> logging.getLogger().setLevel(old_log_level)

    Refer to common root.
    >>> root is not None
    True
    >>> if not root == root.root:  
    ...     root, root.root
    >>> root == root.title_mc.root
    True
    >>> root == root.title_mc.no_listener_btn.root
    True

    Master mock python client dispatches setting label or text to Flash slave.
    To reuse the same syntax as setting label or text directly on slave:
    On setting an attribute, if root has callback, then execute:
    with arguments:  owner, property, value.
    >>> root.title_mc.gotoAndPlay('hi')
    >>> root.title_mc.currentLabel
    'hi'
    >>> root.title_mc.username_txt.text = 'yuji'
    >>> root.title_mc.username_txt.text
    'yuji'
    >>> from remote_control import note
    >>> root._on_set = note
    >>> root.title_mc.gotoAndPlay('bye')
    {'title_mc': {'currentLabel': 'bye'}}
    >>> root.title_mc.currentLabel
    'bye'

    Setter never returns.
    >>> root.title_mc.username_txt.text = 'jade'

    And if value is the same, nothing happens.
    >>> def note_string(owner, property, value):
    ...     print 'note: ', note(owner, property, value)
    >>> root._on_set = note_string
    >>> root.title_mc.username_txt.text
    'jade'
    >>> root.title_mc.username_txt.text = 'jade'

    But if value is different, the on_set function is called.
    >>> root.title_mc.username_txt.text = 'yuji'
    note:  {'title_mc': {'username_txt': {'text': 'yuji'}}}
    >>> root.title_mc.username_txt.text
    'yuji'

    Dispatch calls on_set, INSTEAD of responding to event.
    >>> root.title_mc.dispatchEvent(mouseDown)
    note:  {'title_mc': {'dispatchEvent': 'mouseDown'}}

    To see child in PyShell autoCompleteList:
    If uniquely named, child becomes available as an attribute.
    >>> if None is root.title_mc.name:  False
    >>> if None is root.title_mc.no_listener_btn:  False
    >>> if None is root.title_mc.__getattribute__('name'):  False
    >>> if None is root.title_mc.__getattribute__('no_listener_btn'):  False

    To program this easily, do not change the name!
    >>> root.title_mc.no_listener_btn.name = 'a'
    >>> hasattr(root.title_mc, 'a')
    True
    >>> hasattr(root.title_mc, 'no_listener_btn')
    True

    Upon removal, name is removed, if unique and referring to child.
    >>> button = root.title_mc.removeChild(button)
    >>> hasattr(root.title_mc, 'a')
    False

    Beware!  If name changed, old attribute still lingers.
    >>> hasattr(root.title_mc, 'no_listener_btn')
    True
    '''


import time

def getTimer():
    '''milliseconds since import.  emulate flash.utils.getTimer
    >>> now = getTimer()
    >>> if not 1 <= now:  now
    >>> if not type(1) == type(now):  now
    '''
    seconds = time.clock()
    milliseconds = int(seconds * 1000)
    return milliseconds
    
start = getTimer()


Object = dict
Array = list

def object_example():
    '''
    >>> type({})
    <type 'dict'>
    >>> type({}) == Object
    True
    >>> type({'a': 1}) == Object
    True
    >>> type(['a', 1]) == Object
    False
    '''

class String(str):
    r'''Partial mock of ActionScript String
    file:///C:/Program%20Files%20(x86)/Common%20Files/Adobe/Help/en_US/AS3LCR/Flash_10.0/String.html

    Limited to:
    >>> var = s = String('ad\n');
    >>> s.substring(2, 3);
    '\n'
    >>> s.substring(s.length - 1, s.length);
    '\n'
    >>> s.charAt(1);
    'd'
    >>> s
    'ad\n'

    Beware of reassignment.
    >>> s = 'abc'
    >>> s.charAt(2);
    Traceback (most recent call last):
      ...
    AttributeError: 'str' object has no attribute 'charAt'
    >>> s
    'abc'
    >>> s = String('abc')
    >>> s.charAt(2);
    'c'
    >>> s
    'abc'
    '''
    def __init__(self, string):
        str.__init__(string)
        self._string = string
        self.length = len(self._string)
    def charAt(self, index):
        return self._string[index]
    def substring(self, startIndex = 0, endIndex = 0x7ffffff):
        return self._string[startIndex:endIndex]

    



import logging

def get_example_stage():
    self = MovieClip()
    self.name = 'root1'
    title_mc = MovieClip()
    title_mc.name = 'title_mc'
    self.addChild(title_mc)
    username_txt = TextField()
    username_txt.name = 'username_txt'
    username_txt.text = 'user'
    title_mc.addChild(username_txt)
    password_txt = TextField()
    password_txt.name = 'password_txt'
    password_txt.text = 'pass'
    title_mc.addChild(password_txt)
    gateway_mc = MovieClip()
    gateway_mc.name = 'gateway_mc'
    gateway_mc.gotoAndPlay('none')
    self.addChild(gateway_mc)
    start_btn = SimpleButton()
    start_btn.name = 'start_btn'
    start_btn.addEventListener(MouseEvent.MOUSE_DOWN, trace_event)
    title_mc.addChild(start_btn)
    lobby_mc = MovieClip()
    lobby_mc.name = 'lobby_mc'
    self.addChild(lobby_mc)
    lobby_table_mc = MovieClip()
    lobby_table_mc.name = 'level_1_mc'
    lobby_mc.addChild(lobby_table_mc)
    enter_btn = SimpleButton()
    enter_btn.name = 'enter_btn'
    lobby_table_mc.addChild(enter_btn)
    game_over_mc = MovieClip()
    game_over_mc.name = 'game_over_mc'
    game_over_mc.gotoAndPlay('none')
    self.addChild(game_over_mc)
    start_mc = MovieClip()
    start_mc.name = 'start_mc'
    game_over_mc.addChild(start_mc)
    start_btn = SimpleButton()
    start_btn.name = 'start_btn'
    start_mc.addChild(start_btn)
    save_mc = MovieClip()
    save_mc.name = 'save_mc'
    self.addChild(save_mc)
    load_mc = MovieClip()
    load_mc.name = 'load_mc'
    self.addChild(load_mc)
    _0_0_mc = MovieClip()
    _0_0_mc.name = '_0_0_mc'
    self.addChild(_0_0_mc)
    _0_1_mc = MovieClip()
    _0_1_mc.name = '_0_1_mc'
    self.addChild(_0_1_mc)
    _1_0_mc = MovieClip()
    _1_0_mc.name = '_1_0_mc'
    self.addChild(_1_0_mc)
    _1_1_mc = MovieClip()
    _1_1_mc.name = '_1_1_mc'
    self.addChild(_1_1_mc)
    return self


import text
def load(save_file_name):
    r'''
    >>> old_log_level = logging.getLogger().level
    >>> logging.getLogger().setLevel(logging.CRITICAL)
    >>> load('.no_file')
    {'gateway_mc': 'save_not_found'}
    >>> logging.getLogger().setLevel(old_log_level)

    Convert Windows carriage return + line feed to Unix line feed.
    http://www.freenetpages.co.uk/hp/alan.gauld/tutfiles.htm
    http://en.wikipedia.org/wiki/Newline
    >>> windows = '{\r\n\r\n}'
    >>> file = open('user/test_windows_file.news.py', 'w')
    >>> file.write(windows)
    >>> file.close()
    >>> load('user/test_windows_file.news.py')
    {}
    '''
    import os
    if os.path.exists(save_file_name):
        unix_text = text.load(save_file_name)
        message = eval(unix_text) 
    else:
        logging.error('load:  %s file not found' % save_file_name)
        message = {'gateway_mc': 'save_not_found'}
    return message


def trace_event(event):
    '''Easy example of add and dispatch event.  Not native to ActionScript.
    '''
    trace('trace_event: ' + event.type)


# Begin mocking ActionScript functions

def trace(message):
    print message


class Event(object):
    ENTER_FRAME = 'enterFrame'
    def __init__(self, type):
        self.type = type
        self.currentTarget = None
        
class MouseEvent(Event):
    CLICK = 'click'
    MOUSE_DOWN = 'mouseDown'
    MOUSE_OVER = 'mouseOver'
    MOUSE_OUT = 'mouseOut'
    MOUSE_MOVE = 'mouseMove'

class TextEvent(Event):
    TEXT_INPUT = 'textInput'
    def __init__(self, type):
        super(self).__init__(type)
        self.text = ''

class EventDispatcher(object):
    '''Bubble event to eldest ancestor (root).
    '''
    def __init__(self):
        ##- super(EventDispatcher, self).__init__()
        self.events = {}
        self._logger = None
    def addEventListener(self, event_type, respond):
        self.events[event_type] = respond
    def dispatchEvent(self, event):
        if not self.events:
            logging.warn('EventDispatcher.dispatchEvent: ' + self.name + ' has no listener')
        if event.type in self.events:
            # XXX Gotcha ActionScript ReferenceError: Error #1074: 
            # Illegal write to read-only property currentTarget 
            # on flash.events.MouseEvent.
            event.currentTarget = self
            dispatch_log = self.name + '.dispatchEvent(event) # ' + event.type
            logging.info(dispatch_log)
            if self.root:
                if self.root._on_set:
                    self.root._on_set(self, 'dispatchEvent', event.type)
                    return

            self.events[event.type](event)

class InteractiveObject(EventDispatcher):
    '''Because all objects used are InteractiveObject.
    I do not mock DisplayObject.
    Mock mouse position.
    >>> stage = InteractiveObject()
    >>> hasattr(stage, 'mouseX')
    True
    >>> hasattr(stage, 'mouseY')
    True
    >>> hasattr(stage, 'scaleX')
    True
    >>> hasattr(stage, 'scaleY')
    True

    Beware, in ActionScript, mouseX and mouseY are read-only.
    file:///C:/Program%20Files%20(x86)/Common%20Files/Adobe/Help/en_US/AS3LCR/Flash_10.0/flash/display/DisplayObject.html#mouseX
    '''
    def __init__(self):
        super(InteractiveObject, self).__init__()
        self.name = 'instance'
        self.mouseEnabled = true
        self.parent = None
        self.root = self
        self.x = 0
        self.y = 0
        self.mouseX = 0
        self.mouseY = 0
        self.scaleX = 0
        self.scaleY = 0
        self._on_set = None
    # XXX property and get item give me a headache with reference error
    #def _set_name(self, name):
    #    if name != self._name:
            #if self.parent:
            #    attributes = self.parent.__dict__
            #    if attributes.has_key(self._name):
            #        if attributes[self._name] == self:
            #            attributes.pop(self._name)
            #    if hasName(self):
            #        attributes = self.parent.__dict__
            #        if not attributes.has_key(name):
            #            attributes[name] = self
    #        self._name = name
    #name = property(lambda self:  self._name, _set_name)

    def __getitem__(self, item):
        if self.__dict__.has_key(item):
            return self.__dict__[item]
        if hasattr(self, item):
            return getattr(self, item)
        # Flash is lenient with reference errors when getting.
        logging.debug('InteractiveObject.getitem:  ReferenceError %s["%s"]' % (self.name, item))
        ## 
        return ReferenceError
    def __setitem__(self, item, value):
        if self.__dict__.has_key(item):
            self.__dict__[item] = value
        elif hasattr(self, item):
            setattr(self, item, value)
        else:
            logging.info('InteractiveObject.setitem:  ReferenceError %s["%s"]' % (self.name, item))
            raise ReferenceError

class SimpleButton(InteractiveObject):
    '''May dispatchEvent to this.'''


class MovieClip(InteractiveObject):
    def __init__(self):
        super(MovieClip, self).__init__()
        self._currentLabel = None
        self._children = []
        self.mouseChildren = true
        self._moved = false
        self._orphanage = None
    currentLabel = property(lambda self:  self._currentLabel)

    def gotoAndPlay(self, label):
        '''ActionScript gotcha:  Move clip x and y in code.  Then try 'goto*'.  
        No animation of x and y.
        >>> clip = MovieClip()
        >>> clip.currentLabel
        >>> clip.gotoAndPlay('a')
        >>> clip.currentLabel
        'a'
        >>> clip.x = 1
        >>> old_log_level = logging.getLogger().level
        >>> logging.getLogger().setLevel(logging.CRITICAL)
        >>> clip.gotoAndPlay('b')
        >>> clip.currentLabel
        'b'
        >>> logging.getLogger().setLevel(old_log_level)
        '''
        if self._moved:
            moved_log = 'ActionScript gotcha:  After ActionScript has moved %s to %i,%i, timeline cannot move x,y at any label, such as "%s"' \
                    % (self.name, self.x, self.y, label)
            logging.debug(moved_log)
            # if logging.getLogger().level < logging.DEBUG:
            #     import pdb; pdb.set_trace();
        self._currentLabel = label
        if self.root:
            if self.root._on_set:
                return self.root._on_set(self, 'currentLabel', label)
    def _get_numChildren(self):
        if self._orphanage:
            self = remember_children(self, self._orphanage, recurse = False, 
                    update = False)
            self._orphanage = None
        return len(self._children)
    numChildren = property(_get_numChildren)
    def _get_root(self):
        ancestor = self.parent
        while ancestor.parent:
            ancestor = ancestor.parent
        return ancestor
    root = property(_get_root)
    def addChild(self, display_object):
        self._children.append(display_object)
        display_object.parent = self
        display_object.root = display_object.parent.root
        if hasName(display_object):
            if not self.__dict__.has_key(display_object.name):
                self.__dict__[display_object.name] = display_object
    def getChildByName(self, name):
        '''If the movie clip knows an orphanage, 
        and child not found refer to orphanage.
        >>> moonhyoung_root = MovieClip()
        >>> orphanage = {'currentLabel': 'login', 
        ...     '_1_2_mc': {'currentLabel': 'empty_black',
        ...         'territory_mc': {'currentLabel': 'neutral'}}}
        >>> moonhyoung_root._orphanage = orphanage
        >>> moonhyoung_root.getChildAt(0).name
        '_1_2_mc'
        >>> moonhyoung_root.numChildren
        1

        Beware, current label and other properties of root are not updated.
        >>> moonhyoung_root.currentLabel
        >>> moonhyoung_root._1_2_mc.currentLabel
        'empty_black'
        >>> moonhyoung_root._1_2_mc.territory_mc.currentLabel
        'neutral'
        '''
        for child in self._children:
            if name == child.name:
                return child
        if self._orphanage and self._orphanage.has_key(name):
            self = remember_children(self, self._orphanage, recurse = False, 
                    update = False)
            self._orphanage = None
            return self.__dict__[name]
    def getChildAt(self, index):
        if self._orphanage:
            self = remember_children(self, self._orphanage, recurse = False, 
                    update = False)
            self._orphanage = None
        return self._children[index]
    def removeChild(self, orphan):
        for child in self._children:
            if orphan == child:
                self._children.remove(child)
                if self == orphan.parent:
                    orphan.parent = None
                if hasName(orphan):
                    if self.__dict__.has_key(orphan.name):
                        if self.__dict__[orphan.name] == orphan:
                            self.__dict__.pop(orphan)
                return child
        else:
            logging.warn('removeChild:  orphan not found %s in %s' \
                    %(orphan, self) )
            import pdb; pdb.set_trace();
    def __getitem__(self, item):
        if self.__dict__.has_key(item):
            return self.__dict__[item]
        if hasattr(self, item):
            return getattr(self, item)
        child = self.getChildByName(item)
        if child:
            return child
        ## import pdb; pdb.set_trace();
        logging.debug('MovieClip.getitem: ReferenceError %s["%s"]' % (self.name, item))
        return ReferenceError
    def __getattr__(self, item):
        if self.__dict__.has_key(item):
            return self.__dict__[item]
        child = self.getChildByName(item)
        if child:
            return child
        raise AttributeError
    def __setattr__(self, item, value):
        if 'x' == item or 'y' == item:
            self._moved = true
        self.__dict__[item] = value


class TextField(InteractiveObject):
    def __init__(self):
        super(TextField, self).__init__()
        self._text = ''
    def __get_text(self):  
        return self._text
    def __set_text(self, text):
        if self._text is not text:
            self._text = text
            if self.root:
                if self.root._on_set:
                    self.root._on_set(self, 'text', text)
    text = property(__get_text, __set_text)
           

class Array:
    '''Mock ActionScript Array class to conveniently use indexOf.
    Unused?
    >>> simple_properties = new = Array('scaleX', 'scaleY', 'x', 'y');
    >>> simple_properties.indexOf('x');
    2
    >>> simple_properties.indexOf('z');
    -1
    '''
    def __init__(self, *values):
        self._list = list(values)
        ## print self._list
    def indexOf(self, searchElement, startIndex = 0):
        try:
            return self._list.index(searchElement)
        except:
            return -1

# helper functions not native to ActionScript

def hasName(display_object):
    '''Does the display object have no name?
    By default Flash names unnamed instances:  instance...
    >>> hasName(None)
    False
    >>> instance = MovieClip()
    >>> hasName(instance)
    False
    >>> instance.name = 'an_instance'
    >>> hasName(instance)
    True
    >>> instance.name = 'instance23'
    >>> hasName(instance)
    False
    >>> instance.name = ''
    >>> hasName(instance)
    False
    '''
    if (not display_object):
        return false;
    if ('' == display_object.name):
        return false;
    return (0 != display_object.name.find('instance') )
def isMovieClip(owner):
    if not owner:
        return False
    # bizarre non-equality from cyclical import? server-client
    return type(owner) == MovieClip \
            or hasattr(owner, 'gotoAndPlay')
        
def isInteractiveObject(owner):
    if not owner:
        return False
    # bizarre non-equality from cyclical import? server-client
    return type(owner) == InteractiveObject \
            or hasattr(owner, 'mouseEnabled')

def isTextField(owner):
    if not owner:
        return False
    return type(owner) == TextField \
            or hasattr(owner, 'text')

def isSimpleButton(owner):
    if not owner:
        return False
    return type(owner) == SimpleButton \
            or (hasattr(owner, 'name') \
                and owner.name.endswith('_btn'))

def isMovieTextButton(owner):
    if not owner:
        return False
    return isMovieClip(owner) \
            or isTextField(owner) \
            or isSimpleButton(owner)


#.as:uncomment: def unicode_to_string(value):
#.as:uncomment:     r'''ActionScript only.
#.as:uncomment:     >>> unicode_to_string_as('lobby')
#.as:uncomment:     'lobby'
#.as:uncomment:     >>> unicode_to_string_as(1)
#.as:uncomment:     1
#.as:uncomment:     >>> unicode_to_string_as('\xa0')
#.as:uncomment:     '\xa0'
#.as:uncomment:     >>> unicode_to_string_as(u'\xa0')
#.as:uncomment:     u'\xa0'
#.as:uncomment:     '''
#.as:uncomment:     return value;

    
def unicode_to_string(value):
    r'''Not necessary in ActionScript?
    >>> unicode_to_string(u'lobby')
    'lobby'
    >>> unicode_to_string(1)
    1
    >>> unicode_to_string(u'\xa0')
    u'\xa0'
    '''
    converted = value
    if type(u'') == type(value):
        try:
            converting = str(value)
        except:
            pass
        else:
            if value == converting:
                converted = converting
    return converted


def resembles_dictionary(owner):
    '''
    Beware that pyamf uses ASObject, not dictionary.
    >>> import pyamf
    >>> dictionary = {'a': {'b': u'2', 'c': u'3'}}
    >>> as_object = pyamf.ASObject({'a': {'b': u'2', 'c': u'3'}})

    Even though ASObject looks like a dictionary,
    decoded ActionScript object fails dictionary type checks.
    >>> type(as_object) == dict
    False
    >>> resembles_dictionary(as_object)
    True
    >>> dictionary == as_object
    True
    '''
    return type(owner) == type({}) \
            or hasattr(owner, 'has_key')

def remember_children(root, news, create = True, recurse = True, update = True):
    '''Recursively remember children.
    If create, then x,y does not count as moving.

    Optionally do not recurse.
    >>> moonhyoung_root = MovieClip()
    >>> orphanage = {'currentLabel': 'login', 
    ...     '_1_2_mc': {'currentLabel': 'empty_black',
    ...         'territory_mc': {'currentLabel': 'neutral'}}}
    >>> moonhyoung_root = remember_children(moonhyoung_root, orphanage, True, recurse = False)
    >>> moonhyoung_root._orphanage
    >>> moonhyoung_root.currentLabel
    'login'
    >>> moonhyoung_root._1_2_mc.currentLabel
    'empty_black'
    >>> moonhyoung_root._1_2_mc._orphanage == orphanage['_1_2_mc']
    True

    Optionally do not overwrite property.
    >>> moonhyoung_root.gotoAndPlay('lobby')
    >>> moonhyoung_root = remember_children(moonhyoung_root, orphanage, True, recurse = False, update = False)
    >>> moonhyoung_root.currentLabel
    'lobby'

    Do not overwrite even if property is None.
    >>> moonhyoung_root.gotoAndPlay(None)
    >>> moonhyoung_root = remember_children(moonhyoung_root, orphanage, True, recurse = False, update = False)
    >>> moonhyoung_root.currentLabel
    '''
    if not root:
        logging.error('remember_children root missing ' + str(property))
    elif not isMovieClip(root):
        logging.error('remember_children root is not MovieClip ' + str(root))
    else:
        for property, value in news.items():
            if update and property == 'currentLabel':
                label = value
                label = unicode_to_string(label)
                root.gotoAndPlay(label)
            elif update and property == 'x':
                root.x = value
                if create:
                    root._moved = False
            elif update and property == 'y':
                root.y = value
                if create:
                    root._moved = False
            elif property.endswith('_mc') or value \
                    and resembles_dictionary(value) \
                    and value.has_key('currentLabel'):
                baby_mc = MovieClip()
                baby_mc.name = property
                label = value.get('currentLabel')
                label = unicode_to_string(label)
                baby_mc.gotoAndPlay(label)
                root.addChild(baby_mc)
                if recurse:
                    remember_children(baby_mc, value, recurse = recurse)
                else:
                    root._orphanage = None
                    baby_mc._orphanage = value
            elif property.endswith('_txt') or value \
                    and resembles_dictionary(value) \
                    and value.has_key('text'):
                baby_txt = TextField()
                baby_txt.name = property
                baby_txt.text = value.get('text', '')
                baby_txt.text = unicode_to_string(baby_txt.text)
                root.addChild(baby_txt)
            elif property.endswith('_btn'):
                baby_btn = SimpleButton()
                baby_btn.name = property
                root.addChild(baby_btn)
    return root



if __name__ == '__main__':
    print '\n\nactionscript.py starts testing...',
    import doctest
    doctest.testmod()
    print 'complete.'
