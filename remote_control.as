// remote_control.as
// Minimal Flash remote control protocol for prototyping gameplay
// 
// Author Ethan Kennerly    Examples:  http://finegamedesign.com
// 
// This is intended to be simple, to minimize client bugs.
// A dictionary is passed with name of object 
// and only its absolutely essential properties:  name, currentLabel, text, x, y.
// 
// include this file, instead of import to access and pollute root and stage.


var globe = this;

/*
function hasName(display_object) {
    if (! display_object) {
        return false;
    }
    return 0 != display_object.name.indexOf('instance');
}
*/

function hasName(display_object){
    /*Does the display object have no name?
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
    */
    if (! display_object){
        return false;
    } // if
    if ('' == display_object.name){
        return false;
    } // if
    return (0 != display_object.name.indexOf('instance') )
} // function hasName

function unicode_to_string(value){
    /*ActionScript only.
    >>> unicode_to_string_as('lobby')
    'lobby'
    >>> unicode_to_string_as(1)
    1
    >>> unicode_to_string_as('xa0')
    'xa0'
    >>> unicode_to_string_as(u'xa0')
    u'xa0'
    */
    return value;
} // function unicode_to_string



function isInteractiveObject(owner) {
    if (! owner) {
        return false;
    }
    return owner is InteractiveObject;
}

function isMovieClip(owner) {
    if (! owner) {
        return false;
    }
    return owner is MovieClip;
}

function isTextField(owner) {
    if (! owner) {
        return false;
    }
    return owner is TextField;
}

function isMovieTextButton(owner) {
    if (! owner) {
        return false;
    }
    return owner is SimpleButton
        || owner is MovieClip
        || owner is TextField;
}

function note(owner, name, value) {
    // XXX Gotcha ActionScript interprets {a: b} as {'a': b}
    var news = {};
    news[name] = value;
    var eldest = owner;
    var context = {};
    while (eldest.parent && eldest.parent.parent) {   // XXX update .py!
        context = {};
        context[eldest.name] = news;
        news = context;
        eldest = eldest.parent;
    }
    return news;
}

function get_note(owner, name) {
    var value = owner[name]; 
    return note(owner, name, value);
}

function text_or_number(value) {
    return typeof(value) == typeof('') 
        || typeof(value) == typeof("") 
        || typeof(value) == typeof(1)
        || typeof(value) == typeof(0.5)
        || value == null || value == undefined;
}

function resembles_dictionary(owner) {
    return typeof(owner) == typeof({}) || owner is Object;
}

function upgrade(old, news) {
    for (var key in news) {
        var old_value = old[key];
        var value = news[key];
        if (key == 'title_mc' && old_value != undefined) {
            var breakpoint = true;
        }
        if (old_value != value) {
            if (old[key] == null || old[key] == undefined) {
                old[key] = value;
            }
            else if (text_or_number(old[key]) && text_or_number(value)){
                old[key] = value;
            }
            else if (resembles_dictionary(old[key]) 
                        &&  resembles_dictionary(value) ){
                old[key] = upgrade(old[key], value);
            }
            else {
                trace('info: upgrade:  i did not expect old_value: '
                        + old_value.toString()
                        + ',  value: ' + value.toString());
            }
        }
    }
    return old;
}


function insert_label_and_position(movie_clip, message) {
    // integer is smaller though less accurate than float
    // breaks animation on clip.
    message['currentLabel'] = movie_clip.currentLabel;
    message['x'] = int(movie_clip.x);
    message['y'] = int(movie_clip.y);
    return message;
}

function insert_label(movie_clip, message) {
    message['currentLabel'] = movie_clip.currentLabel;
    return message;
}

function _family_tree(root, message, describe) {
    //'''Recursively transcribe dictionary of text and movie clips.
    if (! hasName(root)) {
        var pass:Boolean = true;
    }
    else if (isTextField(root)) {
        message['text'] = root.text;
    }
    else if (isMovieClip(root)) {
        message = describe(root, message);
        for (var c = 0; c < root.numChildren; c ++) {
            var child = root.getChildAt(c);
            if (hasName(child)) {
                var child_message = {};
                message[child.name] = child_message;
                _family_tree(child, child_message, describe);
            }
        }
    }
    return message;
}

function family_tree(root){ 
    _family_tree(root, {}, insert_label);
}

function compose_root(describe, ... named_txt_or_mc_array) {
    // sends multiple objects (at root level only)
    // TODO:  for children to stay children, cite ancestors
    var message = {};
    for (var s = 0; s < named_txt_or_mc_array.length; s++ ){
        var named_txt_or_mc = named_txt_or_mc_array[s];
        var object_dict = _family_tree(globe.root[named_txt_or_mc.name],
            {}, describe);
        if ({} != object_dict) {
            var object_name = named_txt_or_mc.name;
            message[object_name] = object_dict;
        }
    }
    return message;
}


function is_simple_property(property){
    /*Is this a position || scale?
    >>> is_simple_property('x')
    True
    >>> is_simple_property('scaleY')
    True
    >>> is_simple_property('z')
    False
    */
    var simple_properties = ['scaleX', 'scaleY', 'x', 'y'];
    for (var p = 0; p < simple_properties.length; p++){
        var simple = simple_properties[p];
        if (simple == property){
            return true;
        } // if
    } // for
    return false;
} // function is_simple_property




function update_family_tree(display_object, news){
    /*Recursively update from dictionary of text && movie clips.
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
    >>> if ! news == reverted{
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
    >>> if ! news == reverted{
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
    >>> if ! news == reverted{
    ...     news
    ...     reverted

    If no such parameter, log error.
    >>> old_log_level = trace("getLogger:" + ).level
    >>> trace("getLogger:" + ).setLevel(trace("CRITICAL)
    >>> no_such = {'gateway_mc': {'free_lunch': 'avocado'}}
    >>> old = update_family_tree:" + root, no_such)
    >>> trace("getLogger:" + ).setLevel(old_log_level)

    Ignore dispatchEvent
    Do ! dispatch a mouse event.  Only a few MouseEvents supported.
    >>> event = {'title_mc':  {'start_btn':  {'dispatchEvent':  'mouseDown'}}}
    >>> olds = update_family_tree(root, event)

    Do ! dispatch press to a movie clip.
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

    Update scaleX && scaleY.
    >>> scale = {'_0_0_mc': {'scaleX':  2.5, 'scaleY': 2.5}}
    >>> olds = update_family_tree(root, scale)
    >>> root._0_0_mc.scaleX
    2.5
    >>> root._0_0_mc.scaleY
    2.5
    
    // i do ! need parent.
    //Adopt an orphan && rebrand its label.
    //>>> root['gateway_mc'].currentLabel
    //'password'
    //>>> adoption = {'gateway_mc':  {'parent':  '_1_0_mc', 'currentLabel': 'response'}}
    //>>> old = update_family_tree(root, adoption)
    //>>> root['_1_0_mc']['gateway_mc'].currentLabel
    //'response'
    //>>> root['gateway_mc']
    //<type 'exceptions.ReferenceError'>
    */
    var olds = {};
    for (var property in news){
        var value = news[property];
        if (! display_object){
            var missing_news = 'update_family_tree: display_object === missing ' 
                    + property.toString() + ', news: ' + news.toString();
            trace("error:" + missing_news);
            continue;
        } // if
        if (property == 'dispatchEvent'){
            continue;
        } // if
        if (isMovieClip(display_object)){
            if (property == 'currentLabel'){
                if (value != display_object[property]){
                    olds[property] = display_object[property];
                } // if
                var label = value;
                label = unicode_to_string(label);
                display_object.gotoAndPlay(label);
            } else if (is_simple_property(property)){
                //// XXX *>_<*  Gotcha!  when code controls a movie clip 
                // (to place at x,y position for example, 
                // this breaks the animation on that clip, such as gotoAndPlay
                if (value != display_object[property]){
                    olds[property] = display_object[property];
                } // if
                display_object[property] = value;
            } else{
                var child = display_object.getChildByName(property);
                if (child){
                    if (isMovieTextButton(display_object[property])){
                        var changes = update_family_tree(
                                display_object[property], value);
                        if (changes){
                            olds[property] = changes;
                        } // if
                    } // if
                } else{
                    trace("error:" + 'update_family_tree: ' + property.toString()
                        + '? = ' + value.toString());
                } // if
            } // if
        } else if (isTextField(display_object)){
            if (property == 'text'){
                if (value != display_object[property]){
                    olds[property] = display_object[property];
                } // if
                var text = value;
                text = unicode_to_string(text);
                display_object[property] = text;
            } // if
        } // if
    } // for
    trace("debug:" + 'update_family_tree:  olds=' + olds.toString());
    return olds;
} // function update_family_tree


function dispatch_family_tree(display_object, news){
    /*
    >>> root = get_example_stage()

    Dispatch a mouse event.  Only a few MouseEvents supported.
    >>> event = {'title_mc':  {'start_btn':  {'dispatchEvent':  'mouseDown'}}}
    >>> dispatch_family_tree(root, event)
    trace_event: mouseDown

    Cannot revert dispatching an event.
    Therefore, all necessary results should be 
    embedded into x, y, || label of movie clip || text.
    >>> none = {'title_mc':  {'start_btn':  {'dispatchEvent':  'none'}}}
    >>> dispatch_family_tree(root, none)
    
    Dispatch press to a movie clip.
    >>> root.title_mc.addEventListener(MouseEvent.MOUSE_DOWN, trace_event)
    >>> press_title = {'title_mc':  {'dispatchEvent':  'mouseDown'}}
    >>> dispatch_family_tree(root, press_title)
    trace_event: mouseDown

    Update scaleX && scaleY quietly.
    >>> scale = {'_0_0_mc': {'scaleX':  2.5, 'scaleY': 2.5}}
    >>> olds = dispatch_family_tree(root, scale)
    */
    // Easier to convert to ActionScript than:  property, value in news.items()
    for (var property in news){
        var value = news[property];
        if (! display_object){
            var missing_news = 'update_family_tree: display_object === missing ' 
                    + property.toString() + ', news: ' + news.toString();
            trace("error:" + missing_news);
            continue;
        } // if
        if (property == 'dispatchEvent'){
            var event_type = value;
            // XXX Gotcha ActionScript requires 'new MouseEvent(...)' 
            // but does ! bark while compiling.  at runtime{
            // TypeError: Error //1034: Type Coercion failed: 
            // cannot convert "mouseDown" to flash.events.MouseEvent.
            var event = new MouseEvent(event_type);
            // XXX Gotcha ActionScript ReferenceError: Error //1074: 
            // Illegal write to read-only property currentTarget 
            // on flash.events.MouseEvent.
            //- event.currentTarget = display_object
            display_object.dispatchEvent(event);
            continue;
        } // if
        if (isMovieClip(display_object)){
            if (property != 'currentLabel' 
                    && ! is_simple_property(property)){
                var child = display_object.getChildByName(property);
                if (child){
                    if (isMovieTextButton(display_object[property])){
                        dispatch_family_tree(
                                display_object[property], value);
                    } // if
                } else{
                    trace("error:" + 'dispatch_family_tree: ' + property.toString()
                        + '? = ' + value.toString());
                } // if
            } // if
        } // if
    } // for
} // function dispatch_family_tree



function imitate_news(root, news, log_news = null){
    /*Read news && act.
    if no news, do nothing.
    } // if
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

    Other fields ! in news are ! removed.
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
    >>> function p(cite, news):  print cite, news
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
    */
    if (news !== null && resembles_dictionary(news)){
        if (null != log_news){
            log_news('imitate_news', news);
        } // if
        // trace("info:" + 'imitate_news: %s' % get_keywords(news))
        // trace("debug:" + 'imitate_news:  ' + news.toString());
        var info = {'none': true};
        if (undefined != news['info']){
            info = news['info'];
            delete news['info'];
        } // if
        var olds = update_family_tree(root, news);
        dispatch_family_tree(root, news);
        if ({'none': true} != info){
            news['info'] = info;
        } // if
        return olds;
    } else if (news !== null && ! resembles_dictionary(news)){
        // XXX log writes to stderr so doctest does ! catch it.
        trace('imitate_news:  i expect a dictionary');
        //trace('imitate_news:  i expect a dictionary ! ' 
        //        + code_unit.represent(news) );
        if (null != log_news){
            log_news('cannot imitate_news', news);
        } // if
    } // if
} // function imitate_news


















/* stable backup before info 2010-12-02 
function update_family_tree(display_object, news) {
    // '''Recursively update from dictionary of text and movie clips.
    for (var property in news) {
//         prof.begin( "news_node" );
        var value = news[property];
        if (! display_object) {
            trace('update_family_tree missing ' + property);
            continue;
        }
        if (property == 'dispatchEvent') {
            var event_type = value;
            var event = new MouseEvent(event_type);
            // XXX Gotcha ActionScript ReferenceError: Error #1074: 
            // Illegal write to read-only property currentTarget 
            // on flash.events.MouseEvent.
            // event.currentTarget = display_object;
            display_object.dispatchEvent(event);
            continue;
        }
        if (isMovieClip(display_object)) {
            if (property == 'currentLabel') {
                var label = value;
                trace('update_family_tree: ' + display_object.name 
                    + ' gotoAndPlay: ' + label);
//                 prof.begin( "news_gotoAndPlay" );
                display_object.gotoAndPlay(label);
//                 prof.end( "news_gotoAndPlay" );
            }
            else if (property == 'parent') {
                var old_parent = display_object.parent;
                if (old_parent) {
                    var new_parent_name = value;
                    var new_parent = display_object.root[new_parent_name];
                    // After removing, the child will have no root or parent.
                    old_parent.removeChild(display_object);
                    new_parent.addChild(display_object);
                }
                else {
                    var orphan = 'update_family_tree: child is missing parent '
                            + property.toString() + ', news: ' + news.toString();
                    trace('error:' + orphan);
                }
            }
            // *>_<*	snap!  when code controls a movie clip 
            // (to place at x,y position for example, 
            // this breaks timeline animation on that clip.
            else if (property == 'x') {
                display_object.x = value;
            }
            else if (property == 'y') {
                display_object.y = value;
            }
            else if (isMovieTextButton(display_object[property])) {
                update_family_tree(display_object[property], value);
            }
        }
        else if (isTextField(display_object)) {
            if (property == 'text') {
                var text = value;
                display_object[property] = text;
            }
        }
//         prof.end( "news_node" );
    }
    return display_object;
}



function imitate_news(root, news, log_news_function = null) {
    //if (news) {
    //    log_news('imitate_news', news);
        // trace('imitate_news: ' + get_keywords(news));
        // trace('imitate_news:  ' + news.toString() );
    //    root = update_family_tree(root, news);
    //}
    //return root;
    if (news != null && resembles_dictionary(news)) {
        // if (null != log_news_function) {
        //     log_news_function('imitate_news', news);
        // }
        trace('debug: imitate_news: ' + news.toString());
        var olds = update_family_tree(root, news);
        return olds;
    }
    else if (news != null && ! resembles_dictionary(news)) {
        trace('imitate_news:  i expect a dictionary not ' + news.toString());
        if (log_news_function) {
            log_news_function('cannot imitate_news', news);
        }
    }
}
stable backup before info 2010-12-02 */



function sort_words(text) {
    var words = text.split(' ');
    words.sort();
    var sorted_text = ' '.concat(words);
    return sorted_text;
}



function get_keywords(news){
    /*Summarize && sort news by top-level keys && labels.
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
    */
    var log_str = '';
    for (var name in news){
        if ('currentLabel' == name && news[name] !== null){
            log_str += ':' + news[name].toString();
        } else if (news[name]){
            if (news[name] is Object){
                log_str += ' ' + name;
                for (var item in news[name]){
                    if ('currentLabel' == item 
                            && news[name][item] != null){
                        log_str += ':' + news[name][item].toString();
                    } // if
                } // for
            } // if
        } // if
    } // for
    return sort_words(log_str);
} // function get_keywords







