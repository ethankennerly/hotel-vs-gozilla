/* export_and_duplicate_recursively.jsfl   Ethan Kennerly   finegamedesign.com 
For each named movie clip, text, or button of the selected elements, 
up to maximum depth, export dictionary of name, current label, text.

    for current example see remote_control.py
    '''To test AppData.../Commands/export_stage_dictionary.jsfl:
    Open AppData.../Commands/rename_and_duplicate_recursively.fla
    Root timeline.  Command -> example_stage.py
    Exports element types:  movie clip, text, and button.
    
    >>> file_name = 'rename_and_duplicate_recursively.fla.stage.py'
    >>> stage = eval(open(file_name, 'r').read())
    >>> stage['currentLabel']
    'start'
    >>> stage['old_2_mc']['currentLabel']
    ''
    >>> stage['old_2_mc']['old_square_library_item']['currentLabel']
    'square'
    >>> stage['old_2_mc']['old_square_library_item']['t_txt']['text']
    'T'
    >>> stage['old_2_mc']['command_btn']
    {}
    >>> stage['locked_mc']['currentLabel']
    ''

    Example of a stage:
    {'old_1_mc': {'currentLabel': '', 'old_square_library_item': {'currentLabel': 'square', 't_txt': {'text': 'T'}}, 'command_btn': {}, 'old_circle_library_item': {'currentLabel': ''}, 'old_circle_mc': {'currentLabel': ''}, 'old_square_mc': {'currentLabel': 'square', 't_txt': {'text': 'T'}}}, 'old_0_mc': {'currentLabel': '', 'old_square_library_item': {'currentLabel': 'square', 't_txt': {'text': 'T'}}, 'command_btn': {}, 'old_circle_library_item': {'currentLabel': ''}, 'old_circle_mc': {'currentLabel': ''}, 'old_square_mc': {'currentLabel': 'square', 't_txt': {'text': 'T'}}}, 'old_2_mc': {'currentLabel': '', 'old_square_library_item': {'currentLabel': 'square', 't_txt': {'text': 'T'}}, 'command_btn': {}, 'old_circle_library_item': {'currentLabel': ''}, 'old_circle_mc': {'currentLabel': ''}, 'old_square_mc': {'currentLabel': 'square', 't_txt': {'text': 'T'}}}}
    '''

*/

var max_depth = 9;

var directory = "file:///c|/project/lifeanddeath/";
var dom = fl.getDocumentDOM();
//var file_name = dom.name;
//var file_uri = directory + file_name + '.stage.py'; 
fl.trace('dom.path = ' + dom.path);
var uri = dom.path;
uri = uri.replace(/:/g, '|');
uri = uri.replace(/\\/g, "/");
var file_uri = 'file:///' + uri + '.stage.py'; 
// fl.trace('file_uri = ' + file_uri);

function get_timestamp(a_date) {
    timestamp = '';
    timestamp += a_date.getFullYear();
    timestamp += a_date.getMonth();
    timestamp += a_date.getDate();
    timestamp += a_date.getHours();
    timestamp += a_date.getMinutes();
    timestamp += a_date.getSeconds();
    return timestamp;
}

if (FLfile.exists(file_uri)) {
    var modified = FLfile.getModificationDateObj(file_uri);
    var destination = file_uri + '.' + get_timestamp(modified) + '.py';
    fl.trace('file_uri backup = ' + destination);
    FLfile.copy(file_uri, destination);
}
var stage_text = '';

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

var exported = {};

function recursively_export(dom, dad, element, indent, depth) {
    if ("text" == element.elementType) {
        if (hasName(element)){
            dad[element.name] = {};
            dad[element.name]['text'] = element.getTextString();
            stage_text += indent + "'" + element.name + "': {'text': '" + element.getTextString() + "'}," + '\n';
        }
    }
    else if ("symbol" == element.instanceType) {
        var item = null;
        if (hasName(element)){
            stage_text += indent + "'" + element.name + "': {" + '\n';
            dad[element.name] = {};
            item = element.libraryItem;
            if (null != item) {
                //fl.trace(indent + "item.name: " + item.name 
                //    + "; item.itemType: " + item.itemType);
                if ("movie clip" == item.itemType) {
                    var a = 0;
                }
                else if ("button" == item.itemType) {
                    item = null;
                }
                else {
                    item = null;
                }
            }
            else {
                stage_text += indent + "item is null" + '\n';
            }
        }
        else {
            var a = 0;
        }
        if (1 <= depth && item != null) {
            indent += "    ";
            depth -= 1;
            var timeline = item.timeline;
            var frame_name = get_first_frame_name(timeline);
            dad[element.name]['currentLabel'] = frame_name;
            stage_text += indent + "'currentLabel': '" + frame_name.toString() + "'," + '\n';
            var elements = get_elements_at_first_frame(timeline);
            validate_unique_names(item.name, elements);
            for (var e = 0; e < elements.length; e++) {
                var child_element = elements[e];
                recursively_export(dom, dad[element.name], 
                    child_element, indent, depth);
            }
        }
        else if (depth <= 0) {
            fl.trace('max_depth = ' + max_depth.toString() + '; depth = ' + depth + '; element.name = ' + element.name);
        }
        if (hasName(element)){
            stage_text += indent + "}, # " + element.name + '\n';
        }
    }
}

function validate_unique_names(prefix, elements) {
    var unique_names = [];
    var unique = true;
    for (var e = 0; e < elements.length; e++) {
        var element = elements[e];
        if (hasName(element)) {
            var this_unique = true;
            for (var u = 0; u < unique_names.length; u++) {
                var unique_name = unique_names[u];
                if (element.name == unique_name) {
                    fl.trace('  ! validate_unique_names:  identical name: ' + prefix + ': ' + element.name);
                    unique = false;
                    this_unique = false;
                }
            }
            if (this_unique) {
                unique_names.push(element.name);
            }
        }
    }
    return unique;
}

function get_first_frames(timeline){
    var first_frames = [];
    var layers = timeline.layers;
    for (var l = 0; l < layers.length; l++) {
        var layer = layers[l];
        var frames = layer.frames;
        var f = 0;
        var frame = frames[f];
        // folder does not have a frame
        if (null != frame) {
            first_frames.push(frame);
        }
    }
    return first_frames;
}

function get_elements_at_first_frame(timeline){
    var elements = [];
    var frames = get_first_frames(timeline);
    for (var f = 0; f < frames.length; f++ ) {
        var frame = frames[f];
        var frame_elements = frame.elements;
        for (var e = 0; e < frame_elements.length; e++) {
            var element = frame_elements[e];
            elements.push(element);
        }
    }
    return elements;
}

function get_first_frame_name(timeline) {
    var frame_name = "";
    var frames = get_first_frames(timeline);
    for (var f = 0; f < frames.length; f++ ) {
        var frame = frames[f];
        if ("" != frame.name) {
            frame_name = frame.name;
            // stage_text += indent + "'currentLabel': '" + frame_name.toString() + "'," + '\n';
            break;
        }
    }
    // if ("" == frame_name) {
    //     stage_text += indent + "'currentLabel': '" + frame_name.toString() + "'," + '\n';
    // }
    return frame_name;
}

function export_stage() {
    stage_text += '# ' + file_uri + '\n';
    stage_text += '#     max_depth = ' + max_depth.toString() + '\n';
    var dom = fl.getDocumentDOM();
    // dom.selectAll();
    // var selection = dom.selection;
    // var timeline = dom.getTimeline();
    var timeline = dom.timelines[0];
    elements = get_elements_at_first_frame(timeline);
    validate_unique_names('root', elements);
    if (! (2 <= elements.length) ) {
        stage_text += "export_stage:  HUH?  expected:  2 <= elements.length, got: " + elements.length + '\n';
    }
    stage_text += '{' + '\n';
    var frame_name = get_first_frame_name(timeline);
    stage_text += "    'currentLabel': '" + frame_name + "'," + '\n';
    for (var s = 0; s < elements.length; s++) {
        var element = elements[s];
        recursively_export(dom, exported, element, "    ", max_depth);
    }
    stage_text += '}' + '\n';
    stage_text += '# end ' + file_uri + '\n';
    // fl.outputPanel.save(file_uri);
    FLfile.write(file_uri, stage_text);
    fl.trace(file_uri + "; inspect that each child matches your expectations without omission or redundancy.");
    alert(file_uri + "; inspect that each child matches your expectations without omission or redundancy.");
}

// fl.outputPanel.clear();
export_stage();


