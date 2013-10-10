'''Mock remote control of a flash movie clip.'''
__author__ = 'Ethan Kennerly'

import code_unit
# mock some features of ActionScript
from actionscript import *

def export_stage_dictionary_jsfl_example():
    r'''To test AppData.../Commands/export_stage_dictionary.jsfl:
    Open AppData.../Commands/rename_and_duplicate_recursively.fla
    Root timeline.  Command -> example_stage.py
    Exports element types:  movie clip, text, and button.
    
    >>> file_name = r'C:\Users\Ethan\AppData\Local\Adobe\Flash CS4\en\Configuration\Commands\rename_and_duplicate_recursively.fla.stage.py'
    >>> stage = load(file_name)
    >>> stage['currentLabel']
    'start'
    >>> stage['old_1_mc']['currentLabel']
    ''
    >>> stage['old_1_mc']['old_square_library_item']['currentLabel']
    'square'
    >>> stage['old_1_mc']['old_square_library_item']['t_txt']['text']
    'T'
    >>> stage['old_0_mc']['old_square_library_item']['t_txt']['text']
    'T'
    >>> stage['old_1_mc']['old_square_library_item']['t_txt']['text']
    'T'
    >>> stage['old_1_mc']['command_btn']
    {}
    >>> stage['locked_mc']['currentLabel']
    ''

    Beware!  Can have duplicate names, which dictionary silently parses.
    Check Flash trace for error messages.
    >>> stage['old_2_mc'].get('command_btn')

    Example of a stage:
    {'old_1_mc': {'currentLabel': '', 'old_square_library_item': {'currentLabel': 'square', 't_txt': {'text': 'T'}}, 'command_btn': {}, 'old_circle_library_item': {'currentLabel': ''}, 'old_circle_mc': {'currentLabel': ''}, 'old_square_mc': {'currentLabel': 'square', 't_txt': {'text': 'T'}}}, 'old_0_mc': {'currentLabel': '', 'old_square_library_item': {'currentLabel': 'square', 't_txt': {'text': 'T'}}, 'command_btn': {}, 'old_circle_library_item': {'currentLabel': ''}, 'old_circle_mc': {'currentLabel': ''}, 'old_square_mc': {'currentLabel': 'square', 't_txt': {'text': 'T'}}}, 'old_2_mc': {'currentLabel': '', 'old_square_library_item': {'currentLabel': 'square', 't_txt': {'text': 'T'}}, 'command_btn': {}, 'old_circle_library_item': {'currentLabel': ''}, 'old_circle_mc': {'currentLabel': ''}, 'old_square_mc': {'currentLabel': 'square', 't_txt': {'text': 'T'}}}}
   
    >>> from user_as import save_file_name
    >>> stage = load(save_file_name)
    >>> stage['currentLabel']
    'setup'
    >>> stage['lobby_mc']['currentLabel']
    '_main'
    >>> stage = create_stage(save_file_name)
    >>> stage['lobby_mc']['currentLabel']
    '_main'
    >>> stage['lobby_mc']['_00_mc']['capture_3_3_1_mc']['currentLabel']
    'none'

    In .fla, Flash animator sets user default value on first frame.
    The stage is the template for reloading and resetting users.
    For example, in Flash CS4 the score by default is initialized to zero.
    >>> stage['score_mc']['bar_mc']['marker_mc']['capture_mc']['currentLabel']
    '_0'
    >>> stage['score_mc']['bar_mc']['currentLabel']
    '_0'
    '''

def is_example():
    '''What type of InteractiveObject is this?
    >>> _txt = TextField()
    >>> isTextField(_txt)
    True
    >>> _mc = MovieClip()
    >>> isMovieClip(_mc)
    True
    >>> _btn = SimpleButton()
    >>> isSimpleButton(_btn)
    True
    >>> isMovieClip(_txt)
    False
    >>> isTextField(_mc)
    False
    >>> isSimpleButton(_txt)
    False
    >>> isSimpleButton(_mc)
    False
    '''
    

def note(owner, property, value):
    '''
    >>> root = get_example_stage()
    >>> expected_message = {'title_mc':  {'password_txt':  {'text': 'p'}}}
    >>> note(root.title_mc.password_txt, 'text', 'p')
    {'title_mc': {'password_txt': {'text': 'p'}}}
    >>> news = note(root.title_mc.password_txt, 'text', 'p')
    >>> if not news == expected_message:
    ...     news
    ...     expected_message
    '''
    news = {}
    # XXX Gotcha ActionScript interprets {a: b} as {'a': b}
    news[property] = value
    eldest = owner
    context = {}
    while eldest.parent:
        context = {}
        context[eldest.name] = news
        news = context
        eldest = eldest.parent
    return news


def get_note(owner, property):
    '''
    >>> root = get_example_stage()
    >>> get_note(root.title_mc.password_txt, 'text')
    {'title_mc': {'password_txt': {'text': 'pass'}}}
    '''
    value = getattr(owner, property) # .as: owner[property]
    return note(owner, property, value)

def address(owner):
    '''String address specifying owner in the tree.
    >>> root = get_example_stage()
    >>> address(root)
    'root'
    >>> address(root.title_mc)
    'root.title_mc'
    >>> address(root.title_mc.password_txt)
    'root.title_mc.password_txt'
    >>> address(root.title_mc.password_txt.text)
    Traceback (most recent call last):
      ...
    AttributeError: 'str' object has no attribute 'name'
    '''
    def _name(eldest):
        if eldest.name.startswith('root'):
            return 'root'
        else:
            return eldest.name
    eldest = owner
    address = '%s' % _name(eldest)
    while eldest.parent:
        eldest = eldest.parent
        address = '%s.%s' % (_name(eldest), address)
    return address
    
def text_or_number(value):
    '''unicode is not str but equals a string, and initial string may be null.
    >>> u'' == ''
    True
    >>> type(u'') == type('')
    False
    >>> text_or_number(u'')
    True
    >>> text_or_number('')
    True
    >>> text_or_number(None)
    True
    >>> text_or_number(175)
    True
    >>> text_or_number(175.5)
    True
    >>> text_or_number({1: 1})
    False
    >>> text_or_number(String(''))
    True
    '''
    return type(value) == type('') \
            or type(value) == type(u'') \
            or type(value) == type(1) \
            or type(value) == type(0.5) \
            or type(value) == type(String('')) \
            or value is None


def as_object_to_dict(as_object):  
    '''
    >>> import pyamf
    >>> pyamf.ASObject({'a': 1})
    {'a': 1}
    >>> a = pyamf.ASObject({'a': 1})
    >>> as_object_to_dict(a)
    {'a': 1}
    >>> type(a)
    <class 'pyamf.ASObject'>
    >>> type(as_object_to_dict(a))
    <type 'dict'>
    '''
    dict_string = dict.__repr__(as_object)
    return eval(dict_string)



def upgrade(old, news):
    '''Recursively replace old strings (or None) in dictionary 
    except if they are news dictionaries.
    >>> old = {'a':  {'b': '2', 'c': '3'}}
    >>> news = {'a':  {'b': '4'}}
    >>> upgrade(old, news)
    {'a': {'c': '3', 'b': '4'}}
    >>> old = {'cat':  {'hat': 'floppy', 'plate': {'ham': u'green', 'eggs':  u'green'}}}
    >>> news = {'cat':  {'plate': {'ham': u'red'}}}
    >>> upgrade(old, news)
    {'cat': {'plate': {'eggs': u'green', 'ham': u'red'}, 'hat': 'floppy'}}
    >>> news = {'cat':  {'plate': {'ham': None}}}
    >>> upgrade(old, news)
    {'cat': {'plate': {'eggs': u'green', 'ham': None}, 'hat': 'floppy'}}
    >>> upgrade({}, {'a': '1'})
    {'a': '1'}
    >>> upgrade({'a': {'b': u'2'}},  {'a': {}})
    {'a': {'b': u'2'}}
    >>> upgrade({'a': {'b': u'2'}},  {'a': {'b': u'2', 'c': u'3'}})
    {'a': {'c': u'3', 'b': u'2'}}

    Beware that pyamf uses ASObject, not dictionary
    >>> import pyamf
    >>> as_object = pyamf.ASObject({'a': {'b': u'2', 'c': u'3'}})
    >>> upgrade({'a': {'b': u'2'}},  as_object)
    {'a': {'c': u'3', 'b': u'2'}}

    New string or null values on old subdictionaries are ignored.
    >>> old_log_level = logging.getLogger().level
    >>> logging.getLogger().setLevel(logging.CRITICAL)
    >>> upgrade({'a': {'b': u'2'}},  {'a': None})
    {'a': {'b': u'2'}}
    >>> upgrade({'a': {'b': '2'}},  {'a': u'1'})
    {'a': {'b': '2'}}
    >>> upgrade({'a': {'b': {}, 'c': u'3'}},  {'a': {'c': u'1'}})
    {'a': {'c': u'1', 'b': {}}}
    >>> logging.getLogger().setLevel(old_log_level)

    Replace x and y position.
    >>> old_position = {'formation_field_mc': {'x': 1643, 'y': 975}}
    >>> new_position = {'formation_field_mc': {'y': 175, 'x': 175}}
    >>> upgraded = upgrade(old_position, new_position)
    >>> if not new_position == upgraded:  new_position, upgraded

    >>> old_position = {'formation_field_mc': {'rotate_0_mc': {'response_mc': {'currentLabel': u'none'} }, 'x': 1643, 'y': 975}}
    >>> new_position = {'formation_field_mc': {'y': 175, 'x': 175, 'rotate_0_mc': {'response_mc': {'currentLabel': 'response'}}}}
    >>> upgraded = upgrade(old_position, new_position)
    >>> if not new_position == upgraded:  new_position, upgraded
    '''
    for key in news:
        old_value = old.get(key) # .as: old[key]
        value = news[key]
        if old_value != value:
            if not old.get(key):
                old[key] = value
            elif text_or_number(old.get(key)) and text_or_number(value):
                old[key] = value
            elif resembles_dictionary(old.get(key)) and resembles_dictionary(value):
                old[key] = upgrade(old.get(key), value)
            else:
                logging.error('upgrade:  i did not expect old_value: ' \
                        + str(old_value)
                        + ',  value: ' + str(value))
                ## import pdb; pdb.set_trace();
    return old


def insert_label(movie_clip, message):
    '''label of clip.'''
    message['currentLabel'] = movie_clip.currentLabel
    return message


def insert_label_and_position(movie_clip, message):
    '''integer x,y is smaller though less accurate than float.
    Breaks animations on clip.'''
    message['currentLabel'] = movie_clip.currentLabel
    message['x'] = int(movie_clip.x)
    message['y'] = int(movie_clip.y)
    return message


def _family_tree(root, message, describe):
    '''Recursively transcribe dictionary of text and movie clips.
    Include the x and y positions of movieclips, but not of text.
    >>> root = get_example_stage()
    >>> title_family = {'start_btn': {}, 'username_txt': {'text': 'user'}, 'currentLabel': None, 'password_txt': {'text': 'pass'}}
    >>> title_family_xy = {'start_btn': {}, 'username_txt': {'text': 'user'}, 'currentLabel': None, 'password_txt': {'text': 'pass'}, 'x': 0, 'y': 0}
    >>> tree = family_tree(root['title_mc'])
    >>> code_unit.dict_diff(title_family, tree)

    Optionally include xy.
    >>> tree = _family_tree(root['title_mc'], {}, insert_label_and_position)
    >>> code_unit.dict_diff(title_family_xy, tree)

    Strip out nodes that start with 'instance',
    which in Flash is the default name for unnamed MovieClips and so on.
    >>> instance = MovieClip()
    >>> instance.name = 'instance999'
    >>> root['title_mc'].addChild(instance)
    >>> tree = family_tree(root['title_mc'])
    >>> code_unit.dict_diff(title_family, tree)

    The root should therefore have a name.
    >>> tree = family_tree(root)
    >>> 1 <= len(tree)
    True
    '''
    if not hasName(root):
        pass
    elif isTextField(root):
        message['text'] = root.text
    elif isMovieClip(root):
        message = describe(root, message)
        for c in range(root.numChildren):
            child = root.getChildAt(c)
            if hasName(child):
                child_message = {}
                message[child.name] = child_message
                _family_tree(child, child_message, describe)
    return message

def family_tree(root):
    return _family_tree(root, {}, insert_label)

def compose_root(describe, *named_txt_or_mc_array):
    '''aggregate multiple objects (at root level only)
    TODO:  for children to stay children, cite ancestors
    >>> compose_root(insert_label, MovieClip())
    {}
    '''
    message = {}
    for named_txt_or_mc in named_txt_or_mc_array:
        object_dict = _family_tree(named_txt_or_mc, {}, describe)
        if {} != object_dict:
            object_name = named_txt_or_mc.name
            message[object_name] = object_dict
    return message

#def compose_root(*named_txt_or_mc_array):
#    return _compose_root(insert_label, *named_txt_or_mc_array)

#def compose_root_position(*named_txt_or_mc_array):
#    return _compose_root(insert_label_and_position, *named_txt_or_mc_array)


## // how can i send ... array to another function?
#def send_root(ambassador, *named_txt_or_mc_array):
#    '''sends multiple objects (at root level only)
#    TODO:  for children to stay children, cite ancestors
#    >>> from mock_client import echo_protocol_class
#    >>> send_root(echo_protocol_class(), MovieClip())
#    '''
#    message = compose_root(*named_txt_or_mc_array)
#    ambassador.send(message)



def is_simple_property(property):
    '''Is this a position or scale?
    >>> is_simple_property('x')
    True
    >>> is_simple_property('scaleY')
    True
    >>> is_simple_property('z')
    False
    '''
    var = simple_properties = ['scaleX', 'scaleY', 'x', 'y'];
    for p in range(len(simple_properties)):
        var = simple = simple_properties[p];
        if (simple == property):
            return true;
    return false;

def update_family_tree(display_object, news):
    '''Recursively update from dictionary of text and movie clips.
    ActionScript grumbles about reassigning root, so modify display_object in place.
    >>> root = get_example_stage()
    >>> root['gateway_mc']['currentLabel']
    'none'
    >>> news = {'gateway_mc': {'currentLabel': 'password'}}
    >>> olds = update_family_tree(root, news)
    >>> root['gateway_mc']['currentLabel']
    'password'

    Revert
    >>> olds
    {'gateway_mc': {'currentLabel': 'none'}}
    >>> reverted = update_family_tree(root, olds)
    >>> root['gateway_mc']['currentLabel']
    'none'
    >>> if not news == reverted:
    ...     news
    ...     reverted

    Update text.  For easy doctesting, convert legible unicode to string.
    >>> root['title_mc']['username_txt'].text
    'user'
    >>> news = {'title_mc': {'username_txt': {'text': u'joris'}}}
    >>> olds = update_family_tree(root, news)
    >>> root['title_mc']['username_txt'].text
    'joris'

    Revert
    >>> reverted = update_family_tree(root, olds)
    >>> root['title_mc']['username_txt'].text
    'user'
    >>> if not news == reverted:
    ...     news
    ...     reverted

    Update position.
    >>> root['gateway_mc']['x'], root['gateway_mc']['y']
    (0, 0)
    >>> news = {'gateway_mc': {'x': 1, 'y': 2}}
    >>> olds = update_family_tree(root, news)
    >>> root['gateway_mc']['x'], root['gateway_mc']['y']
    (1, 2)

    Revert
    >>> reverted = update_family_tree(root, olds)
    >>> root['gateway_mc']['x'], root['gateway_mc']['y']
    (0, 0)
    >>> if not news == reverted:
    ...     news
    ...     reverted

    If no such parameter, log error.
    >>> old_log_level = logging.getLogger().level
    >>> logging.getLogger().setLevel(logging.CRITICAL)
    >>> no_such = {'gateway_mc': {'free_lunch': 'avocado'}}
    >>> old = update_family_tree(root, no_such)
    >>> logging.getLogger().setLevel(old_log_level)

    Ignore dispatchEvent
    Do not dispatch a mouse event.  Only a few MouseEvents supported.
    >>> event = {'title_mc':  {'start_btn':  {'dispatchEvent':  'mouseDown'}}}
    >>> olds = update_family_tree(root, event)

    Do not dispatch press to a movie clip.
    >>> root.title_mc.addEventListener(MouseEvent.MOUSE_DOWN, trace_event)
    >>> press_title = {'title_mc':  {'dispatchEvent':  'mouseDown'}}
    >>> olds = update_family_tree(root, press_title)

    If nothing changed, then return no olds.
    >>> press_title = {'title_mc':  {'dispatchEvent':  'mouseDown'}}
    >>> label = root.currentLabel
    >>> olds = update_family_tree(root, {'currentLabel': label})
    >>> olds
    {}
    >>> label = root.title_mc.currentLabel
    >>> olds = update_family_tree(root, {'title_mc': {'currentLabel': label}})
    >>> olds
    {}

    Update scaleX and scaleY.
    >>> scale = {'_0_0_mc': {'scaleX':  2.5, 'scaleY': 2.5}}
    >>> olds = update_family_tree(root, scale)
    >>> root._0_0_mc.scaleX
    2.5
    >>> root._0_0_mc.scaleY
    2.5
    
    # i do not need parent.
    #Adopt an orphan and rebrand its label.
    #>>> root['gateway_mc'].currentLabel
    #'password'
    #>>> adoption = {'gateway_mc':  {'parent':  '_1_0_mc', 'currentLabel': 'response'}}
    #>>> old = update_family_tree(root, adoption)
    #>>> root['_1_0_mc']['gateway_mc'].currentLabel
    #'response'
    #>>> root['gateway_mc']
    #<type 'exceptions.ReferenceError'>
    '''
    var = olds = {};
    for property in news:
        var = value = news[property];
        if (not display_object):
            var = missing_news = 'update_family_tree: display_object is missing ' \
                    + str(property) + ', news: ' + str(news);
            logging.error(missing_news);
            continue;
        if (property == 'dispatchEvent'):
            continue;
        if (isMovieClip(display_object)):
            if (property == 'currentLabel'):
                if (value != display_object[property]):
                    olds[property] = display_object[property];
                var = label = value;
                label = unicode_to_string(label);
                display_object.gotoAndPlay(label);
            elif (is_simple_property(property)):
                ## XXX *>_<*	Gotcha!  when code controls a movie clip 
                # (to place at x,y position for example, 
                # this breaks the animation on that clip, such as gotoAndPlay
                if (value != display_object[property]):
                    olds[property] = display_object[property];
                display_object[property] = value;
            else:
                var = child = display_object.getChildByName(property);
                if (child):
                    if (isMovieTextButton(display_object[property])):
                        var = changes = update_family_tree(
                                display_object[property], value);
                        if (changes):
                            olds[property] = changes;
                else:
                    logging.error('update_family_tree: ' + str(property)
                        + '? = ' + str(value));
        elif (isTextField(display_object)):
            if (property == 'text'):
                if (value != display_object[property]):
                    olds[property] = display_object[property];
                var = text = value;
                text = unicode_to_string(text);
                display_object[property] = text;
    logging.debug('update_family_tree:  olds=' + str(olds));
    return olds;


def dispatch_family_tree(display_object, news):
    '''
    >>> root = get_example_stage()

    Dispatch a mouse event.  Only a few MouseEvents supported.
    >>> event = {'title_mc':  {'start_btn':  {'dispatchEvent':  'mouseDown'}}}
    >>> dispatch_family_tree(root, event)
    trace_event: mouseDown

    Cannot revert dispatching an event.
    Therefore, all necessary results should be 
    embedded into x, y, or label of movie clip or text.
    >>> none = {'title_mc':  {'start_btn':  {'dispatchEvent':  'none'}}}
    >>> dispatch_family_tree(root, none)
    
    Dispatch press to a movie clip.
    >>> root.title_mc.addEventListener(MouseEvent.MOUSE_DOWN, trace_event)
    >>> press_title = {'title_mc':  {'dispatchEvent':  'mouseDown'}}
    >>> dispatch_family_tree(root, press_title)
    trace_event: mouseDown

    Update scaleX and scaleY quietly.
    >>> scale = {'_0_0_mc': {'scaleX':  2.5, 'scaleY': 2.5}}
    >>> olds = dispatch_family_tree(root, scale)
    '''
    # Easier to convert to ActionScript than:  property, value in news.items()
    for property in news:
        var = value = news[property];
        if (not display_object):
            var = missing_news = 'update_family_tree: display_object is missing ' \
                    + str(property) + ', news: ' + str(news);
            logging.error(missing_news);
            continue;
        if (property == 'dispatchEvent'):
            var = event_type = value;
            # XXX Gotcha ActionScript requires 'new MouseEvent(...)' 
            # but does not bark while compiling.  at runtime:
            # TypeError: Error #1034: Type Coercion failed: 
            # cannot convert "mouseDown" to flash.events.MouseEvent.
            var = event = new = MouseEvent(event_type);
            # XXX Gotcha ActionScript ReferenceError: Error #1074: 
            # Illegal write to read-only property currentTarget 
            # on flash.events.MouseEvent.
            #- event.currentTarget = display_object
            display_object.dispatchEvent(event);
            continue;
        if (isMovieClip(display_object)):
            if (property != 'currentLabel' \
                    and not is_simple_property(property)):
                var = child = display_object.getChildByName(property);
                if (child):
                    if (isMovieTextButton(display_object[property])):
                        dispatch_family_tree(
                                display_object[property], value);
                else:
                    logging.error('dispatch_family_tree: ' + str(property)
                        + '? = ' + str(value));


def imitate_news(root, news, log_news = None):
    '''Read news and act.
    if no news, do nothing.
    ActionScript grumbles about reassigning root, so modify root in place.

    >>> root = get_example_stage()
    >>> root.gateway_mc.currentLabel
    'none'
    >>> no_news = {}
    >>> olds = imitate_news(root, no_news)
    >>> root.gateway_mc.currentLabel
    'none'
    >>> olds
    {}

    Other fields not in news are not removed.
    >>> new_name = {'title_mc':  {'username_txt':  {'text': 'joris'}}}
    >>> olds = imitate_news(root, new_name)
    >>> root['title_mc']['username_txt']['text']
    'joris'
    >>> root['title_mc']['password_txt']['text']
    'pass'

    May revert.
    >>> reverted = imitate_news(root, olds)
    >>> root['title_mc']['username_txt']['text']
    'user'
    >>> root['title_mc']['password_txt']['text']
    'pass'

    Ignore invalid news.
    >>> imitate_news(root, 'a')
    imitate_news:  i expect a dictionary
    >>> def p(cite, news):  print cite, news
    >>> olds = imitate_news(root, new_name, log_news = p)
    imitate_news {'title_mc': {'username_txt': {'text': 'joris'}}}

    1) Update.  2) Dispatch.
    >>> text_dispatch_news = {'title_mc': {'username_txt': {'text': 'jade'}, 
    ...     'start_btn': {'dispatchEvent': 'mouseDown'}}}
    >>> root.title_mc.start_btn.addEventListener(MouseEvent.MOUSE_DOWN,
    ...     trace_username)
    >>> olds = imitate_news(root, text_dispatch_news)
    jade

    Ignore 'info' yet retain it.
    >>> text_dispatch_news = {'title_mc': {'username_txt': {'text': 'jade'}, 
    ...     'start_btn': {'dispatchEvent': 'mouseDown'}}}
    >>> info = {'info': {'_2_2_mc': []}}
    >>> info_news = upgrade(text_dispatch_news, info)
    >>> olds = imitate_news(root, info_news)
    jade
    >>> info_news['info']
    {'_2_2_mc': []}
    >>> info_news['info'] = {}
    >>> olds = imitate_news(root, info_news)
    jade
    >>> info_news['info']
    {}
    '''
    if (news is not None and resembles_dictionary(news)):
        if (null != log_news):
            log_news('imitate_news', news);
        # logging.info('imitate_news: %s' % get_keywords(news))
        # logging.debug('imitate_news:  ' + str(news));
        var = info = {'none': true};
        if (undefined != news.get('info')):
            info = news.get('info');
            del news['info'];
        var = olds = update_family_tree(root, news);
        dispatch_family_tree(root, news);
        if ({'none': true} != info):
            news['info'] = info;
        return olds;
    elif (news is not None and not resembles_dictionary(news)):
        # XXX log writes to stderr so doctest does not catch it.
        trace('imitate_news:  i expect a dictionary');
        #trace('imitate_news:  i expect a dictionary not ' \
        #        + code_unit.represent(news) );
        if (null != log_news):
            log_news('cannot imitate_news', news);




from text import sort_words

def get_keywords(news):
    '''Summarize and sort news by top-level keys and labels.
    >>> news = {'currentLabel': 'table', '_0_0_mc': {'currentLabel': 'black'}}
    >>> get_keywords(news)
    ':table _0_0_mc:black'
    >>> news = {'currentLabel': None, '_0_0_mc': {'currentLabel': 'black'}}
    >>> get_keywords(news)
    ' _0_0_mc:black'
    >>> news = {'currentLabel': 2, '_0_0_mc': {'currentLabel': 'black'}}
    >>> get_keywords(news)
    ':2 _0_0_mc:black'
    >>> news = {'currentLabel': '', '_0_0_mc': {'currentLabel': 'black'}}
    >>> get_keywords(news)
    ': _0_0_mc:black'

    Only list top level key.
    >>> news = {'lobby_mc': {'_0_mc': {'enter_mc': {'currentLabel': 'enter'}}, 'enter_mc': {'currentLabel': 'enter'}}}
    >>> get_keywords(news)
    ' lobby_mc'

    Ignore other values.
    >>> news = {'_3_3_mc': {'currentLabel': 'question_black'}, 'time': 445}
    >>> get_keywords(news)
    ' _3_3_mc:question_black'
    '''
    var = log_str = '';
    for name in news:
        if ('currentLabel' == name and news[name] is not None):
            log_str += ':' + str(news[name]);
        elif (news[name]):
            if (type(news[name]) == Object):
                log_str += ' ' + name;
                for item in news[name]:
                    if ('currentLabel' == item \
                            and news[name][item] != None):
                        log_str += ':' + str(news[name][item]);
    return sort_words(log_str);


def trace_username(mouse_event):
    name = mouse_event.currentTarget.parent.username_txt.text
    trace(name)


# example mock stage.  
# following functions do not appear in ActionScript client.


def get_small_tree():
    return {
        'currentLabel':  'login',
        'title_mc': {
            'username_txt':  {'text':  'user'},
            'password_txt':  {'text':  'pass'},
            'start_btn':  {},
            'currentLabel':  None, },
        'gateway_mc': {
            'currentLabel':  'none', },
        'x': 0, 
        'y': 0
    }



def remember_family(news):
    '''Create a mock stage from tree.
    >>> remember_family(None)

    Name unnamed root so that it will be parsed.
    >>> remember_family({}).name
    'root1'
    >>> shrub = get_small_tree()
    >>> remember_family(shrub).name
    'root1'

    Convert unicode to string.
    >>> root = remember_family({'currentLabel': u'none'})
    >>> root.currentLabel
    'none'

    Create children.
    >>> root = remember_family(shrub)
    >>> MovieClip == type(root.title_mc)
    True
    >>> root.title_mc.username_txt.text
    'user'

    Not moved yet, so may gotoAndPlay.
    >>> root._moved
    False
    >>> root.currentLabel
    'login'
    >>> root.gotoAndPlay('a')
    >>> root.currentLabel
    'a'
    '''
    if not resembles_dictionary(news):
        return
    root = MovieClip()
    root.name = 'root1'
    root = remember_children(root, news)
    return root



def create_stage(save_file_name):
    '''Mock Flash stage.

    Slow.  Takes more than 0.1 to load client stage.
    >>> import timeit
    >>> setup_code = 'from user_as import save_file_name; from remote_control import create_stage'
    >>> stmt_code = 'root = create_stage(save_file_name)'
    >>> timer = timeit.Timer(stmt = stmt_code, setup = setup_code)
    >>> setup_second = timer.timeit(1)
    >>> if not 0.1 <= setup_second: setup_second
    '''
    tree = load(save_file_name) 
    if tree and tree['gateway_mc'] != 'save_not_found':
        root = remember_family(tree)
    else:
        logging.warn('create_stage:  stage file not found')
        root = get_example_stage()
    return root



# master

def promote_to_master(globe, root):
    '''Remote slave performs operations reports back to master.
    '''
    if not hasName(root):
        pass
    elif isTextField(root):
        print 'todo'
        message['text'] = root.text
    elif isMovieClip(root):
        message = insert_label_and_position(root, message)
        for c in range(root.numChildren):
            child = root.getChildAt(c)
            if hasName(child):
                child_message = {}
                message[child.name] = child_message
                promote_to_master(child, child_message)
    return message


# server only

class stage_borg:
    '''Multiple instances share same state.
    http://code.activestate.com/recipes/66531/'''
    __shared_state = {}
    from user_as import save_file_name
    tree = load(save_file_name) 
    def __init__(self):
        self.__dict__ = self.__shared_state

def refer_to_stage(save_file_name):
    '''
    setup of about 20 users takes about 10 seconds.
    most of get_start_problem_example is spent in setup_users.
        profile/get_start_problem_example.profile.png

    most of this time is creating the movie clips from the stage.
        profile/do_setup_client.profile.png
        remember_children
    in most tests most of these users are not used and most of the clips of a user are not used.

    lazily load movie clip.

    TODO: load stage file into dictionary inside a stage borg.
    TODO: each user refers to stage borg.
    getChildByName
    if child not found, trace lineage.
    look for lineage in dictionary of stage borg.
    if found, then remember that child, but none of its descendents.
    >>> from user_as import save_file_name
    >>> moonhyoung_root = refer_to_stage(save_file_name)
    >>> moonhyoung_root.name
    'root1'
    >>> moonhyoung_root.currentLabel
    'setup'
    >>> moonhyoung_root._1_2_mc.currentLabel
    'empty_black'
    >>> moonhyoung_root._1_2_mc.territory_mc.currentLabel
    'neutral'

    Quick.  Less than 0.1 seconds to load client stage.
    >>> import timeit
    >>> setup_code = 'from user_as import save_file_name; from remote_control import refer_to_stage'
    >>> stmt_code = 'root = refer_to_stage(save_file_name)'
    >>> timer = timeit.Timer(stmt = stmt_code, setup = setup_code)
    >>> setup_second = timer.timeit(10)
    >>> if not setup_second <= 0.99: setup_second
    '''
    stage = stage_borg() 
    tree = stage.tree
    if tree and tree['gateway_mc'] != 'save_not_found':
        root = MovieClip()
        root.name = 'root1'
        root = remember_children(root, tree, recurse = False, update = True)
    else:
        logging.error('create_stage:  stage file not found')
    return root


def unique_family_tree(root, message):
    '''Recursively transcribe dictionary of text and movie clips
    that do not have an orphanage (and so are different from template).
    >>> from user_as import save_file_name
    >>> root = refer_to_stage(save_file_name)
    >>> title_family = {'start_btn': {}, 'username_txt': {'text': 'user'}, 'currentLabel': None, 'password_txt': {'text': 'pass'}}
    >>> tree = unique_family_tree(root['title_mc'], {})
    >>> tree
    {'currentLabel': 'none'}
    
    Strip out nodes that start with 'instance',
    which in Flash is the default name for unnamed MovieClips and so on.
    >>> instance = MovieClip()
    >>> instance.name = 'instance999'
    >>> root['title_mc'].addChild(instance)
    >>> tree = unique_family_tree(root, {})
    >>> tree.get('title_mc')
    {'currentLabel': 'none'}
    >>> tree = unique_family_tree(root['title_mc'], {})
    >>> tree
    {'currentLabel': 'none'}

    include current label.
    >>> root.title_mc.gotoAndPlay('new')
    >>> root.title_mc.currentLabel
    'new'
    >>> tree = unique_family_tree(root['title_mc'], {})
    >>> root.title_mc.currentLabel
    'new'
    >>> tree
    {'currentLabel': 'new'}
    >>> root.title_mc.currentLabel
    'new'

    The root should therefore have a name.
    Text fields do not refer to orphanage, so are always included.
    >>> root.title_mc.username_txt.text = 'moonhyoung'
    >>> root.title_mc.currentLabel
    'new'
    >>> tree = unique_family_tree(root['title_mc'], {})
    >>> from pprint import pprint
    >>> tree['currentLabel']
    'new'
    >>> tree['username_txt']
    {'text': 'moonhyoung'}
    '''
    if not hasName(root):
        pass
    elif isTextField(root):
        message['text'] = root.text
    elif isMovieClip(root):
        #message = describe(root, message)
        message['currentLabel'] = root.currentLabel
        if not root._orphanage:
            child_count = root.numChildren
            for c in range(child_count):
                child = root.getChildAt(c)
                if hasName(child):
                    child_message = unique_family_tree(child, {})
                    if child_message:
                        message[child.name] = child_message
    return message


def _log_text(news, context, texts, logs):
    for key, value in news.items():
        if 'text' == key:
            in_context = False
            for text in texts:
                if text in context:
                    in_context = True
            if in_context:
                entry = '>>> %s.text = "%s"' % (context, value)
                logs.append(entry)
        elif resembles_dictionary(news.get(key)) and resembles_dictionary(value):
            subcontext = '%s.%s' % (context, key)
            _log_text(news.get(key), subcontext, texts, logs)
    
def log_dispatchEvent(news, context, texts):
    r'''dispatchEvent and some text fields.
    Lukasz toggles score.  Server logs.
    >>> news = {'option_mc': {'score_mc': {'enter_mc': {'dispatchEvent': 'mouseDown'}}}}
    >>> log_dispatchEvent(news, 'lukasz.root', [])
    ['>>> lukasz.root.option_mc.score_mc.enter_mc.dispatchEvent(mouseDown)']

    If multiple events, separate by a newline.
    >>> news = {'option_mc': {'score_mc': {'enter_mc': {'dispatchEvent': 'mouseDown'}}, 'prohibit_danger_mc': {'enter_mc': {'dispatchEvent': 'mouseDown'}}}}
    >>> log_dispatchEvent(news, 'lukasz.root', [])
    ['>>> lukasz.root.option_mc.score_mc.enter_mc.dispatchEvent(mouseDown)', '>>> lukasz.root.option_mc.prohibit_danger_mc.enter_mc.dispatchEvent(mouseDown)']

    If watching chat text, log chat text.
    >>> news = {'chat_input_mc': {'currentLabel': 'none', 'dispatchEvent': 'mouseDown'}, 'chat_input_txt': {'text': 'hello'}}
    >>> log_dispatchEvent(news, 'lukasz.root', [])
    ['>>> lukasz.root.chat_input_mc.dispatchEvent(mouseDown)']
    >>> log_dispatchEvent(news, 'lukasz.root', ['chat_input_txt'])
    ['>>> lukasz.root.chat_input_txt.text = "hello"', '>>> lukasz.root.chat_input_mc.dispatchEvent(mouseDown)']
    '''
    logs = []
    _log_text(news, context, texts, logs)
    _log_dispatchEvent(news, context, logs)
    return logs

def _log_dispatchEvent(news, context, logs):
    for key, value in news.items():
        if 'dispatchEvent' == key:
            entry = '>>> %s.dispatchEvent(%s)' % (context, value)
            logs.append(entry)
        elif resembles_dictionary(news.get(key)) \
                and resembles_dictionary(value):
            subcontext = '%s.%s' % (context, key)
            _log_dispatchEvent(news.get(key), subcontext, logs)
    
def change(old, news):
    '''Recursively report changes of old strings (or None) in dictionary 
    except if they are news dictionaries.  Ignore extra old or new members.
    >>> old = {'purse':  {'silver': '2', 'gold': '3'}}
    >>> news = {'purse':  {'gold': '4'}}
    >>> change(old, news)
    {'purse': {'gold': '4'}}
    
    >>> old = {'cat':  {'hat': 'floppy', 'plate': {'ham': u'green', 'eggs':  u'green'}}}
    >>> news = {'cat':  {'plate': {'ham': u'red'}}}
    >>> change(old, news)
    {'cat': {'plate': {'ham': u'red'}}}

    >>> news = {'cat':  {'plate': {'ham': None}}}
    >>> change(old, news)
    {'cat': {'plate': {'ham': None}}}

    Ignore extra new members.
    >>> change({}, {'a': '1'})
    {}
    >>> change({'a': {'b': u'2'}},  {'a': {'b': u'2', 'c': u'3'}})
    {}
    >>> change({'a': {'b': u'2'}},  {'a': {}})
    {}

    Beware that pyamf uses ASObject, not dictionary
    >>> import pyamf
    >>> as_object = pyamf.ASObject({'a': {'b': u'2', 'c': u'3'}})
    >>> change({'a': {'b': u'2'}},  as_object)
    {}

    New string or null values on old subdictionaries are ignored.
    >>> old_log_level = logging.getLogger().level
    >>> logging.getLogger().setLevel(logging.CRITICAL)
    >>> change({'a': {'b': u'2'}},  {'a': None})
    {}
    >>> change({'a': {'b': '2'}},  {'a': u'1'})
    {}
    >>> change({'a': {'b': {}, 'c': u'3'}},  {'a': {'c': u'1'}})
    {'a': {'c': u'1'}}
    >>> logging.getLogger().setLevel(old_log_level)

    Replace x and y position.
    >>> old_position = {'formation_field_mc': {'x': 1643, 'y': 975}}
    >>> new_position = {'formation_field_mc': {'y': 175, 'x': 175}}
    >>> changed = change(old_position, new_position)
    >>> if not new_position == changed:  new_position, changed

    >>> old_position = {'formation_field_mc': {'rotate_0_mc': {'response_mc': {'currentLabel': u'none'} }, 'x': 1643, 'y': 975}}
    >>> new_position = {'formation_field_mc': {'y': 175, 'x': 175, 'rotate_0_mc': {'response_mc': {'currentLabel': 'response'}}}}
    >>> changed = change(old_position, new_position)
    >>> if not new_position == changed:  new_position, changed
    '''
    changed = {}
    for key in old:
        old_value = old.get(key) # .as: old[key]
        value = news.get(key)
        if news.has_key(key) and old_value != value:
            if not old.get(key):
                changed[key] = value
            elif text_or_number(old.get(key)) and text_or_number(value):
                changed[key] = value
            elif resembles_dictionary(old.get(key)) \
                    and resembles_dictionary(value):
                child_changed = change(old.get(key), value)
                if child_changed:
                    changed[key] = child_changed
            else:
                logging.error('change:  i did not expect old_value: ' \
                        + str(old_value)
                        + ',  value: ' + str(value))
                ## import pdb; pdb.set_trace();
    return changed


def get_branch(root, keys):
    r'''Get children of dictionary by names.
    >>> from pprint import pprint
    >>> pprint( get_branch({'a': {'d': 4}, 'b': 2, 'c': 3}, ['a', 'b']) )
    {'a': {'d': 4}, 'b': 2}
    >>> pprint( get_branch({'b': 2}, ['a', 'b']) )
    {'b': 2}
    >>> pprint( get_branch({'c': 3}, ['a', 'b']) )
    {}
    '''
    branches = {}
    for key in keys:
        if key in root:
            branches[key] = root[key]
    return branches


def get_lineage(owner, property):
    '''List of names.
    >>> root = get_example_stage()
    >>> get_lineage(root.title_mc.username_txt, 'text')
    ['title_mc', 'username_txt', 'text']
    '''
    lineage = [property]
    eldest = owner
    def _child_name(eldest):
        if eldest.name.startswith('root'):
            return
        else:
            return eldest.name
    while eldest.parent:
        name = _child_name(eldest)
        if name:
            lineage.insert(0, name)
        eldest = eldest.parent
    return lineage

def get_latest(news, owner, property):
    '''Get label from news at address.  
    If not in news, get from owner's property.
    >>> root = get_example_stage()
    >>> get_latest({}, root.title_mc.username_txt, 'text')
    'user'
    >>> get_latest({'title_mc': {'username_txt': {'text': 'other'}}}, root.title_mc.username_txt, 'text')
    'other'
    '''
    lineage = get_lineage(owner, property)
    parent = news
    for child in lineage:
        if parent.has_key(child):
            parent = parent[child]
    if parent:
        return parent
    return getattr(owner, property) # .as: owner[property]


def get_grandchild_by_name(grandparent, grandchild_name):
    '''First grandchild by that name.
    >>> root = get_example_stage()
    >>> _mc = get_grandchild_by_name(root, 'username_txt')
    >>> _mc.name
    'username_txt'
    >>> _mc.parent.name
    'title_mc'
    >>> get_grandchild_by_name(root, 'usernaam_txt')
    >>> get_grandchild_by_name(root.title_mc, 'usernaam_txt')
    '''
    for p in range(grandparent.numChildren):
        parent = grandparent.getChildAt(p)
        if hasattr(parent, 'getChildByName'):
            grandchild = parent.getChildByName(grandchild_name)
            if grandchild:
                return grandchild
        #for gc in range(parent.numChildren):
        #    grandchild = grandparent.getChildAt(gc)
        #    print grandchild.name
        #    if grandchild.name == grandchild_name:
        #        return grandchild



if __name__ == '__main__':
    import code_unit
    import sys
    code_unit.test_file_args('./remote_control.py', sys.argv,
            locals(), globals())
#+    print
#+    print
#+    print
#+    print 'remote_control.py starts testing ...',
#+    import doctest
#+    doctest.testmod()
#+    print '... and finishes testing.'
#+    print

