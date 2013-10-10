// options

this.stage.showDefaultContextMenu = false;

// Movie clip remote control protocol

include "remote_control.as";

import flash.utils.getTimer;




function insert_credentials(message) {
    var username = globe.root.title_mc.username_txt.text;
    var password = globe.root.title_mc.password_txt.text;
    var master = globe.root.title_mc.master_txt.text;
    var slave = globe.root.title_mc.slave_txt.text;
    var news = {
            'title_mc': {
                'username_txt': {'text': username},
                'password_txt': {'text': password},
                'master_txt': {'text': master},
                'slave_txt': {'text': slave}
            }
        };
    message = upgrade(message, news);
    return message;
}

function show_menu_info(mouse_event){
    /*Describe the go problem.
    >>> marije = globe_class()
    >>> marije.create(1)
    >>> marije.ambassador = echo_protocol_class()
    >>> target = marije.root.lobby_mc._00_mc.capture_3_3_mc
    >>> target.info_txt.text = ''
    >>> target.info_txt.text = 'Surround a fire.'
    >>> marije.root.info_mc.currentLabel
    'none'
    >>> marije.root.info_mc._txt.text
    ''
    >>> mouse_event = MouseEvent(MouseEvent.MOUSE_OVER)
    >>> mouse_event.currentTarget = target
    >>> marije.show_menu_info(mouse_event)
    >>> marije.root.info_mc.currentLabel
    'show'
    >>> marije.root.info_mc._txt.text
    'Surround a fire.'
    >>> target2 = marije.root.lobby_mc._00_mc.capture_3_3_1_mc
    >>> target2.info_txt.text = ''
    >>> target2.info_txt.text = 'Surround a second fire.'
    >>> mouse_event.currentTarget = target2
    >>> marije.show_menu_info(mouse_event)
    >>> marije.root.info_mc.currentLabel
    'show'
    >>> marije.root.info_mc._txt.text
    'Surround a second fire.'

    Also hide info.
    >>> mouse_event = MouseEvent(MouseEvent.MOUSE_OUT)
    >>> mouse_event.currentTarget = target2
    >>> marije.hide_menu_info(mouse_event)
    >>> marije.root.info_mc.currentLabel
    'none'
    >>> marije.root.info_mc._txt.text
    ''
    */
    var target_mc = mouse_event.currentTarget;
    var info = target_mc.info_txt.text;
    if (info && 2 <= info.length){
        globe.root.info_mc.gotoAndPlay('show');
        globe.root.info_mc._txt.text = info;
    } // if
} // function show_menu_info

function hide_menu_info(mouse_event){
    /*For example, see show_menu_info.
    */
    globe.root.info_mc.gotoAndPlay('none');
    globe.root.info_mc._txt.text = '';
} // function hide_menu_info

function board_listens_to_mouse(intersection_mc_array){

    /*
    >>> user = globe_class()
    >>> user.create(1)
    >>> user.root._0_0_mc.mouseEnabled
    True
    >>> user.root._0_0_mc.decoration_mc.mouseEnabled
    True
    >>> user.board_listens_to_mouse(user.intersection_mc_array)
    >>> user.root._0_0_mc.mouseEnabled
    True
    >>> user.root._0_0_mc.decoration_mc.mouseEnabled
    False
    >>> user.root._0_0_mc.decoration_mc.mouseChildren
    False

    XXX HACK TODO update every doctest referring 
    from _0_0_mc to _0_0_mc._btn.
    >>> user.root._0_0_mc.mouseEnabled
    True

    Do ! disable mouseChildren of object that does ! have that property.
    >>> shape = InteractiveObject()
    >>> shape.name = 'shape'
    >>> hasattr(shape, 'mouseChildren')
    False
    >>> user.root._0_0_mc.addChild(shape)
    >>> user.board_listens_to_mouse(user.intersection_mc_array)
    >>> hasattr(user.root._0_0_mc.shape, 'mouseChildren')
    False
    >>> user.root._0_0_mc.shape.mouseEnabled
    False

    Disable mouseChildren on strikes.
    >>> user.root._0_0_strike_mc.mouseEnabled
    False
    >>> user.root._0_0_strike_mc.mouseChildren
    False
    
    Mouse over intersection triggeres show info.
    >>> robby = globe_class()
    >>> robby.create(1)
    >>> robby.ambassador = echo_protocol_class()
    >>> robby.setup_events()
    >>> robby.root._2_6_mc.gotoAndPlay('black')
    >>> robby.root._2_6_mc.black_shape_mc.attack_mc.gotoAndPlay('_0000')
    >>> robby.root._2_6_mc.black_shape_mc.defend_mc.gotoAndPlay('show')
    >>> robby.root._2_6_mc.dispatchEvent(mouseOver)
    >>> robby.root.info_mc.currentLabel
    'show'
    >>> robby.root.info_mc.stone_mc.currentLabel
    'black'
    >>> robby.root.info_mc.decoration_mc.currentLabel
    'black_attack_defend'
    >>> robby.root._0_0_mc.dispatchEvent(mouseOver)
    >>> robby.root.info_mc.currentLabel
    'none'
    >>> robby.root.info_mc.stone_mc.currentLabel
    'none'
    >>> robby.root.info_mc.decoration_mc.currentLabel
    'none'

    Mouse out hides info box.
    >>> robby.root._2_6_mc.dispatchEvent(mouseOver)
    >>> robby.root.info_mc.currentLabel
    'show'
    >>> robby.root.info_mc.stone_mc.currentLabel
    'black'
    >>> robby.root.info_mc.decoration_mc.currentLabel
    'black_attack_defend'
    >>> robby.root._2_6_mc.dispatchEvent(mouseOut)
    >>> robby.root.info_mc.currentLabel
    'none'
    >>> robby.root.info_mc.stone_mc.currentLabel
    'none'
    >>> robby.root.info_mc.decoration_mc.currentLabel
    'none'
    */
    for (var row = 0; row < intersection_mc_array.length; row++){
        for (var column = 0; column < intersection_mc_array[row].length; column++){
            //try{
            var intersection = intersection_mc_array[row][column];
            //except{
            //    import pdb; pdb.set_trace();
            var child_count = intersection.numChildren;
            for (var c = 0; c < child_count; c++){
                var child = intersection.getChildAt(c);
                if (isInteractiveObject(child)){
                    child.mouseEnabled = false;
                } // if
                if (isMovieClip(child)){
                    child.mouseChildren = false;
                } // if
            } // for
            //intersection.territory_mc.mouseEnabled = false
            //intersection.territory_mc.mouseChildren = false
            //intersection.block_north_mc.mouseEnabled = false
            //intersection.block_north_mc.mouseChildren = false
            //intersection.block_east_mc.mouseEnabled = false
            //intersection.block_east_mc.mouseChildren = false
            //intersection.block_south_mc.mouseEnabled = false
            //intersection.block_south_mc.mouseChildren = false
            //intersection.block_west_mc.mouseEnabled = false
            //intersection.block_west_mc.mouseChildren = false
            //intersection.hide_mc.mouseEnabled = false
            //intersection.hide_mc.mouseChildren = false
            //intersection.star_mc.mouseEnabled = false
            //intersection.star_mc.mouseChildren = false
            //intersection.question_mc.mouseEnabled = false
            //intersection.question_mc.mouseChildren = false
            //intersection.overlay_mc.mouseEnabled = false

            intersection.overlay_mc.mouseChildren = true;
            intersection.overlay_mc._btn.mouseEnabled = true;
            // XXX HACK TODO update every doctest referring 
            // from _0_0_mc to _0_0_mc._btn.
            intersection.mouseEnabled = false;  // HACK uncomment in ActionScript only.
            intersection.addEventListener(
                    MouseEvent.MOUSE_DOWN, globe.play_stone);
            intersection.addEventListener(
                    MouseEvent.MOUSE_OVER, globe.show_info);
            intersection.addEventListener(
                    MouseEvent.MOUSE_OUT, globe.hide_info);
            var strike_name = '_' + row.toString() 
                    + '_' + column.toString() + '_strike_mc';
            var strike_mc = globe.root[strike_name];
            strike_mc.mouseEnabled = false;
            strike_mc.mouseChildren = false;
        } // for
    } // for
    globe.root.help_mc.mouseEnabled = false;
    globe.root.help_mc.mouseChildren = false;
} // function board_listens_to_mouse




function set_board_visible(intersection_mc_array, visible){
	for (var row:uint = 0; row < intersection_mc_array.length; row++) {
		for (var column:uint = 0; column < intersection_mc_array[row].length; column++) {
            var intersection_mc = intersection_mc_array[row][column];
            intersection_mc.visible = visible;
            var strike_name = '_' + row.toString() + '_' + column.toString() + '_strike_mc';
            var strike_mc = globe.root[strike_name];
            strike_mc.visible = visible;
        }
    }
}

function get_keep_child_list(root) {
    var keep_list = new Array();
    var name;
    var length = 9;
    for (var row = 0; row < length; row ++) {
        for (var column = 0; column < length; column ++) {
            name = get_intersection_name(row, column);
            if (root.getChildByName(name)) {
                keep_list.push(root[name]);
            }
            else {
                trace('get_keep_child_list: missing ' + name);
            }
        }
    }
    var keeps = new Array('fps_window', 'gateway_mc', 'title_mc', 'lobby_mc', 'pass_mc', 'game_over_mc',
        'extra_stone_gift_mc', 'hide_gift_mc');
    for (var k = 0; k < keeps.length; k ++) {
        var keep = keeps[k];
        if (root.getChildByName(keep)) {
            keep_list.push(root[keep]);
        }
        else {
            trace('get_keep_child_list: missing ' + keep);
        }
    }
    return keep_list;
}



function remove_child_except(parent_mc, keep_child_list) {
    trace('remove_child_except: '); 
    var remove_array = new Array();
    for (var c = 0; c < parent_mc.numChildren; c++) {
        var child_mc = parent_mc.getChildAt(c);
        var keep = false;
        for (var k = 0; k < keep_child_list.length; k ++) {
            var keep_mc = keep_child_list[k];
            if (keep_mc.name == child_mc.name) {
                keep = true;
                trace('    keep: ' + child_mc.name); 
            }
        }
        if (! keep) {
            // parent_mc.removeChild(child_mc);
            remove_array.push(child_mc);
            trace('    remove_child: ' + child_mc.name); 
        }
    }
    for (var r = 0; r < remove_array.length; r++) {
        var remove_mc = remove_array[r];
        parent_mc.removeChild(remove_mc);
    }
}

// HACK:  On goto first frame children are added back.
function remove_child_from_intersections(parent_mc){
    var length = 9;
    for (var row = 0; row < length; row ++) {
        for (var column = 0; column < length; column ++) {
            var intersection_name = get_intersection_name(row, column);
            var intersection_mc = parent_mc.getChildByName(intersection_name);
            for (var c2 = 0; c2 < intersection_mc.numChildren; c2++) {
                var intersection_child_mc = intersection_mc.getChildAt(c2);
                intersection_mc.removeChild(intersection_child_mc);
            }
        }
    }
}

/*
// ActionScript profiler

import profiler.*;

ProfilerConfig.Width = stage.stageWidth;
ProfilerConfig.ShowMinMax = true;
var prof:Profiler = new Profiler( 10 * this.stage.frameRate );
*/

// addChild( prof );
// // lifeanddeath.as, amf_socket_class.as, remote_control.as:  prof.begin ... prof.end 

// Frame Rate counter and graph
// var fps_window = new fpsWindow();
// fps_window.name = 'fpsWindow';
// addChild(fps_window);

// Untested HACK to measure performance of rendering
var keep_child_list = get_keep_child_list(globe.root);

function trace_target(mouse_event) {
    trace('trace_target target='     + mouse_event.target.name
        + '; currentTarget=' + mouse_event.currentTarget.name);
}


function rstrip_string(string, strip) {
    var splits = string.split(strip);
    var splits_length = splits.length;
    var stripped = string;
    if (2 <= splits_length) {
        if ('' == splits[splits_length - 1]) {
            splits.pop();
            stripped = splits.join('');  // != .py
        }
    }
    return stripped;
}


function get_play_stone_news(intersection_mc, eat_mc, preview_enabled){
    /*Next state for stone.
    Start preview, which server increments to question.
    >>> joris = globe_class()
    >>> joris.create()
    >>> news = get_play_stone_news(joris.root._0_0_mc, joris.root.eat_mc, True)
    >>> news['cursor_mc']['act_mc']['currentLabel']
    'preview'
    >>> news['_0_0_mc']['currentLabel']
    'preview_black'

    If no preview, then do ! preview.
    >>> news = get_play_stone_news(joris.root._0_0_mc, joris.root.eat_mc, False)
    >>> news['cursor_mc']
    >>> news['_0_0_mc']['currentLabel']
    'play_black'

    If no preview, then do ! preview hide.
    >>> joris.root._0_0_mc.gotoAndPlay('empty_hide_black')
    >>> news = get_play_stone_news(joris.root._0_0_mc, joris.root.eat_mc, False)
    >>> news['cursor_mc']
    >>> news['_0_0_mc']['currentLabel']
    'play_hide_black'

    If ! eating, send that, too.
    >>> if ! news['eat_mc']['currentLabel'] == 'none':  
    ...     news['eat_mc']['currentLabel']

    If 'black' || 'white', return nothing.
    >>> joris.root._0_0_mc.gotoAndPlay('black')
    >>> news = get_play_stone_news(joris.root._0_0_mc, joris.root.eat_mc, False)
    >>> news
    {}

    If eating, do ! send eating.
    >>> joris.root.eat_mc.act_mc.gotoAndPlay('eat')
    >>> news = get_play_stone_news(joris.root._0_0_mc, joris.root.eat_mc, False)
    >>> news['eat_mc']
    >>> joris.root.eat_mc.act_mc.gotoAndPlay('none')

    If looping animation (ending with '_repeat'), then convert to entry label.
    >>> from pprint import pprint
    >>> joris.root._0_0_mc.gotoAndPlay('question_black_repeat')
    >>> news = get_play_stone_news(joris.root._0_0_mc, joris.root.eat_mc, False)
    >>> if ! news['_0_0_mc']['currentLabel'] == 'play_black'{
    ...     pprint(news)

    Do ! convert '_repeat' found elsewhere in label.
    >>> old_log_level = trace()getLogger:.level
    >>> trace()getLogger:.setLevel(trace('CRITICAL)
    >>> joris.root._0_0_mc.gotoAndPlay:question_black_repeat_t')
    >>> news = get_play_stone_news(joris.root._0_0_mc, joris.root.eat_mc, False)
    >>> if news['_0_0_mc']{
    ...     pprint(news)
    >>> trace()getLogger:.setLevel(old_log_level)

    rene moves black.  rene sees start progress immediately
    >>> rene = globe_class()
    >>> rene.create()
    >>> news = get_play_stone_news(rene.root._0_0_mc, rene.root.eat_mc, False)
    >>> news['_0_0_mc']['progress_mc']['currentLabel']
    'black_setup'
    
    rene moves white.  rene sees start progress immediately
    >>> rene.root._0_0_mc.gotoAndPlay('empty_white')
    >>> news = get_play_stone_news(rene.root._0_0_mc, rene.root.eat_mc, False)
    >>> news['_0_0_mc']['progress_mc']['currentLabel']
    'white_setup'
    */
    trace('info:get_play_stone_news:  starting at ' + intersection_mc.name);
    var label = null;
    var cursor_label = null;
    var news = {};
    var intersection_label = rstrip_string(intersection_mc.currentLabel, '_repeat');
    var progress_news = {};
    if ('empty_black' == intersection_label){
        if (preview_enabled){
            label = 'preview_black';
            cursor_label = 'preview';
        } else{
            label = 'play_black';
            progress_news[intersection_mc.name] = 
                {'progress_mc': {'currentLabel':  'black_setup'}};
            news = upgrade(news, progress_news);
        } // if
    } else if ('question_black' == intersection_label){
        label = 'play_black';
        progress_news[intersection_mc.name] = 
            {'progress_mc': {'currentLabel':  'black_setup'}};
        news = upgrade(news, progress_news);
    } else if ('empty_white' == intersection_label){
        label = 'play_white';
        progress_news[intersection_mc.name] = 
            {'progress_mc': {'currentLabel':  'white_setup'}};
        news = upgrade(news, progress_news);
    } else if ('empty_hide_black' == intersection_label){
        if (preview_enabled){
            label = 'preview_hide_black';
            cursor_label = 'preview';
        } else{
            label = 'play_hide_black';
            progress_news[intersection_mc.name] = 
                {'progress_mc': {'currentLabel':  'black_setup'}};
            news = upgrade(news, progress_news);
        } // if
    } else if ('question_hide_black' == intersection_label){
        label = 'play_hide_black';
        progress_news[intersection_mc.name] = 
            {'progress_mc': {'currentLabel':  'black_setup'}};
        news = upgrade(news, progress_news);
    } else if ('black' == intersection_label 
            || 'white' == intersection_label){
        // label = intersection_label;
        var a = 0;
    } else{
        trace('error:get_play_stone_news:  what do i do? ' + intersection_mc.name 
                + ' : ' + intersection_label);
    } // if
    if (label){
        var label_news = {};
        label_news[intersection_mc.name] = {'currentLabel':  label};
        if ('none' == eat_mc.act_mc.currentLabel){
            label_news['eat_mc'] = {};
            label_news['eat_mc']['act_mc'] = {'currentLabel':  eat_mc.act_mc.currentLabel};
        } // if
        news = upgrade(news, label_news);
    } // if
    if (cursor_label){
        news = upgrade(news,
                {'cursor_mc':  {'act_mc': {'currentLabel':  cursor_label}}} );
    } // if
    return news;
} // function get_play_stone_news




function count_item(container){
    /*How many items are in the container?
    ActionScript does ! respond like Python to:  {} != object
    >>> count_item({'a': 0})
    1
    >>> count_item(2)
    Traceback (most recent call last){
      ...
    TypeError: 'int' object is ! iterable
    >>> count_item(null)
    0
    */
    var count = 0;
    if (null != container){
        for (var key in container){
            count += 1;
        } // for
    } // if
    return count;
} // function count_item


function remove_preview_news(intersection_mc_array, intersection_mc){
    /*
    press an intersection, moving into a preview.  
    look for intersections that may be in preview.  revert these.
    >>> laurens = globe_class()
    >>> laurens.create(1)
    >>> laurens.setup_events()
    >>> laurens.root._0_0_mc.gotoAndPlay('preview_black')
    >>> remove_news = remove_preview_news(laurens.intersection_mc_array, 
    ...     laurens.root._0_1_mc)
    >>> from pprint import pprint
    >>> if ! remove_news.get('_0_0_mc'){
    ...     pprint(remove_news)
    >>> remove_news.get('_0_0_mc').get('currentLabel')
    'empty_black'
    >>> laurens.root._0_1_mc.gotoAndPlay('question_black')
    >>> remove_news = remove_preview_news(laurens.intersection_mc_array,
    ...     laurens.root._0_1_mc)
    >>> from pprint import pprint
    >>> if remove_news.get('_0_1_mc'){
    ...     pprint(remove_news)
    >>> remove_news.get('_0_1_mc')
    */
    var news = {};
    for (var row = 0; row < intersection_mc_array.length; row++){
        for (var column = 0; column < intersection_mc_array[row].length; column++){
            var remove_intersection_mc = intersection_mc_array[row][column];
            if (intersection_mc != remove_intersection_mc){
                if ('preview_black' == remove_intersection_mc.currentLabel 
                        || 'question_black' == remove_intersection_mc.currentLabel){
                    var empty = note(remove_intersection_mc, 
                            'currentLabel', 'empty_black');
                    news = upgrade(news, empty);
                } // if
            } // if
        } // for
    } // for
    return news;
} // function remove_preview_news


function play_stone(mouse_event){
    /*
    press an intersection, moving into a preview.  
    look for intersections that may be in preview.  revert these.
    >>> laurens = globe_class()
    >>> laurens.create(1)
    >>> laurens.ambassador = echo_protocol_class()
    >>> laurens.setup_events()
    >>> laurens.root.preview_gift_mc.enabled_mc.gotoAndPlay('show')
    >>> mouse_event = MouseEvent(MouseEvent.MOUSE_DOWN)
    >>> mouse_event.currentTarget = laurens.root._0_0_mc
    >>> laurens.play_stone(mouse_event)
    >>> laurens.root._0_0_mc.currentLabel
    'preview_black'

    Until server says ! busy.
    >>> laurens.root.cursor_mc.act_mc.gotoAndPlay('none')
    >>> mouse_event.currentTarget = laurens.root._0_1_mc
    >>> laurens.play_stone(mouse_event)
    >>> laurens.root._0_0_mc.currentLabel
    'empty_black'

    Do ! send emptied intersection to server.
    >>> laurens.ambassador.sends[-1]['_0_0_mc']

    Moonhyoung prefers to play immediately.
    >>> moonhyoung = laurens
    >>> moonhyoung.root.preview_gift_mc.enabled_mc.gotoAndPlay('none')
    >>> mouse_event = MouseEvent(MouseEvent.MOUSE_DOWN)

    Until server says ! busy.
    >>> moonhyoung.root.cursor_mc.act_mc.gotoAndPlay('none')
    >>> mouse_event.currentTarget = moonhyoung.root._0_0_mc
    >>> moonhyoung.play_stone(mouse_event)
    >>> moonhyoung.root._0_0_mc.currentLabel
    'play_black'

    Do ! resend stone in progress.  Do log an error.
    >>> old_log_level = trace()getLogger:.level
    >>> trace()getLogger:.setLevel(trace('CRITICAL)
    >>> before = laurens.ambassador.sends.length
    >>> laurens.root._0_1_mc.gotoAndPlay:play_black')
    >>> laurens.play_stone(mouse_event)
    >>> if ! before == laurens.ambassador.sends.length{
    ...     laurens.ambassador.sends[-1]
    >>> trace()getLogger:.setLevel(old_log_level)

    If busy, do ! send click.
    >>> robby = moonhyoung
    >>> robby.root._0_0_mc.gotoAndPlay('empty_black')
    >>> robby.root._0_1_mc.gotoAndPlay('empty_black')
    >>> robby.root.cursor_mc.act_mc.gotoAndPlay('none')
    >>> robby.root.cursor_mc.act_mc.currentLabel
    'none'
    >>> mouse_event.currentTarget = robby.root._0_0_mc
    >>> robby.play_stone(mouse_event)
    >>> robby.root.cursor_mc.act_mc.currentLabel
    'busy'
    >>> robby.root._0_0_mc.currentLabel
    'play_black'
    >>> robby.ambassador.sends[-1]['cursor_mc']['act_mc']['currentLabel']
    'busy'
    >>> mouse_event.currentTarget = robby.root._0_1_mc
    >>> robby.play_stone(mouse_event)
    >>> robby.root.cursor_mc.act_mc.currentLabel
    'busy'
    >>> robby.root._0_0_mc.currentLabel
    'play_black'
    >>> robby.root._0_1_mc.currentLabel
    'empty_black'

    Until server says ! busy.
    >>> robby.root.cursor_mc.act_mc.gotoAndPlay('none')
    >>> robby.root._0_0_mc.gotoAndPlay('black')
    >>> mouse_event.currentTarget = robby.root._0_1_mc
    >>> robby.play_stone(mouse_event)
    >>> robby.root.cursor_mc.act_mc.currentLabel
    'busy'
    >>> robby.root._0_0_mc.currentLabel
    'black'
    >>> robby.root._0_1_mc.currentLabel
    'play_black'
    */
    var olds = {};
    var busy = {};
    if ('busy' == globe.root.cursor_mc.act_mc.currentLabel){
        busy = {'help_mc': {'currentLabel': 'busy'}};
        olds = imitate_news(globe.root, busy);
        return;
    } // if
    busy = {'cursor_mc': {'act_mc': {'currentLabel': 'busy'}}};
    // olds = imitate_news(globe.root, busy);
    var intersection_mc = mouse_event.currentTarget;
    var remove_news = remove_preview_news(globe.intersection_mc_array,
            intersection_mc);
    olds = imitate_news(globe.root, remove_news);
    var preview_enabled = 'show' == globe.root 
            .preview_gift_mc.enabled_mc.currentLabel
    var play_news = get_play_stone_news(intersection_mc, 
            globe.root.eat_mc, preview_enabled);        
    if (1 <= count_item(play_news)){
        // log_news('play_stone', play_news);
        play_news = upgrade(play_news, busy);
        globe.publish(play_news);
    } // if
} // function play_stone



function get_hide_info_news(){
    return {'info_mc': {
        'currentLabel': 'none',
        'stone_mc': {'currentLabel': 'none'},
        'decoration_mc': {'currentLabel': 'none'},
        'territory_mc': {'currentLabel': 'none'},
        'top_move_mc': {'currentLabel': 'none'},
        'profit_mc': {'currentLabel': 'none'},
        'block_mc': {'currentLabel': 'none'},
        'dragon_status_mc': {'currentLabel': 'none'},
        '_txt': {'text': ''}
        }
    };
} // function get_hide_info_news


function show_info(mouse_event){
    /*Show info about the stone at the target intersection.
    >>> robby = globe_class()
    >>> robby.create(1)
    >>> robby.ambassador = echo_protocol_class()
    >>> robby.root._2_6_mc.gotoAndPlay('black')
    >>> robby.root._2_6_mc.black_shape_mc.attack_mc.gotoAndPlay('_0000')
    >>> robby.root._2_6_mc.black_shape_mc.defend_mc.gotoAndPlay('show')
    >>> robby.root._2_6_mc.black_shape_mc.defend_mc.profit_mc.gotoAndPlay('show')
    >>> robby.root._2_6_mc.territory_mc.gotoAndPlay('black_dead')
    >>> robby.root._2_6_mc.dragon_status_mc.gotoAndPlay('black_attack')
    >>> robby.root._2_6_mc.block_south_mc.gotoAndPlay('black_block')
    >>> robby.root.info_mc.currentLabel
    'none'
    >>> robby.root.info_mc.stone_mc.currentLabel
    'none'
    >>> robby.root.info_mc.decoration_mc.currentLabel
    'none'
    >>> robby.root.info_mc.profit_mc.currentLabel
    'none'
    >>> robby.root.info_mc.territory_mc.currentLabel
    'none'
    >>> robby.root.info_mc.block_mc.currentLabel
    'none'
    >>> robby.root.info_mc.dragon_status_mc.currentLabel
    'none'
    >>> mouse_event = MouseEvent(MouseEvent.MOUSE_OVER)
    >>> mouse_event.currentTarget = robby.root._2_6_mc
    >>> robby.show_info(mouse_event)
    >>> robby.root.info_mc.currentLabel
    'show'
    >>> robby.root.info_mc.stone_mc.currentLabel
    'black'
    >>> robby.root.info_mc.decoration_mc.currentLabel
    'black_attack_defend'
    >>> robby.root.info_mc.profit_mc.currentLabel
    'show'
    >>> robby.root.info_mc.territory_mc.currentLabel
    'black_dead'
    >>> robby.root.info_mc.block_mc.currentLabel
    'black_block'
    >>> robby.root.info_mc.dragon_status_mc.currentLabel
    'black_attack'
    >>> mouse_event.currentTarget = robby.root._0_0_mc
    >>> robby.show_info(mouse_event)
    >>> robby.root.info_mc.currentLabel
    'none'
    >>> robby.root.info_mc.stone_mc.currentLabel
    'none'
    >>> robby.root.info_mc.decoration_mc.currentLabel
    'none'
    >>> robby.root.info_mc.profit_mc.currentLabel
    'none'
    >>> robby.root.info_mc.territory_mc.currentLabel
    'neutral'
    >>> robby.root.info_mc.dragon_status_mc.currentLabel
    'none'

    Also hide info.
    >>> mouse_event = MouseEvent(MouseEvent.MOUSE_OVER)
    >>> mouse_event.currentTarget = robby.root._2_6_mc
    >>> robby.show_info(mouse_event)
    >>> robby.root.info_mc.currentLabel
    'show'
    >>> robby.root.info_mc.stone_mc.currentLabel
    'black'
    >>> robby.root.info_mc.decoration_mc.currentLabel
    'black_attack_defend'
    >>> robby.root.info_mc.territory_mc.currentLabel
    'black_dead'
    >>> robby.root.info_mc.block_mc.currentLabel
    'black_block'
    >>> robby.root.info_mc.dragon_status_mc.currentLabel
    'black_attack'
    >>> robby.root.info_mc._txt.text = 'Surround the fire.'
    >>> mouse_event = MouseEvent(MouseEvent.MOUSE_OUT)
    >>> mouse_event.currentTarget = robby.root._2_6_mc
    >>> robby.hide_info(mouse_event)
    >>> robby.root.info_mc.currentLabel
    'none'
    >>> robby.root.info_mc._txt.text
    ''
    >>> robby.root.info_mc.stone_mc.currentLabel
    'none'
    >>> robby.root.info_mc.decoration_mc.currentLabel
    'none'
    >>> robby.root.info_mc.territory_mc.currentLabel
    'none'
    >>> robby.root.info_mc.profit_mc.currentLabel
    'none'
    >>> robby.root.info_mc.block_mc.currentLabel
    'none'
    >>> robby.root.info_mc.dragon_status_mc.currentLabel
    'none'

    Reuse decoration for shape && place on board.
    >>> robby.root._6_2_mc.decoration_mc.gotoAndPlay('white_defend')
    >>> robby.root._6_2_mc.territory_mc.gotoAndPlay('white')
    >>> robby.root._6_2_mc.top_move_mc.gotoAndPlay('white')
    >>> mouse_event = MouseEvent(MouseEvent.MOUSE_OVER)
    >>> mouse_event.currentTarget = robby.root._6_2_mc
    >>> robby.show_info(mouse_event)
    >>> robby.root.info_mc.currentLabel
    'show'
    >>> robby.root.info_mc.stone_mc.currentLabel
    'none'
    >>> robby.root.info_mc.decoration_mc.currentLabel
    'white_defend'
    >>> robby.root.info_mc.territory_mc.currentLabel
    'white'
    >>> robby.root.info_mc.top_move_mc.currentLabel
    'white'
    >>> robby.hide_info(mouse_event)
    >>> robby.root.info_mc.top_move_mc.currentLabel
    'none'
    */
    var intersection_mc = mouse_event.currentTarget;
    var label = intersection_mc.currentLabel;
    var info_label = 'none';
    var stone_label = 'none';
    var decoration_label = 'none';
    var profit_label = 'none';
    var territory_label = intersection_mc.territory_mc.currentLabel;
    var top_move_label = intersection_mc.top_move_mc.currentLabel;
    var dragon_status_label = intersection_mc.dragon_status_mc.currentLabel;
    var block_label = 'none';
    if ('black' == label || 'white' == label){
        info_label = 'show';
        stone_label = label;
        if ('black' == label){
            var tags = '';
            var shape_mc = intersection_mc[label + '_shape_mc'];
            var attack_label = shape_mc.attack_mc.currentLabel;
            if ('none' != attack_label){
                tags = tags + '_attack';
            } // if
            var defend_label = shape_mc.defend_mc.currentLabel;
            if ('none' != defend_label){
                tags = tags + '_defend';
            } // if
            if ('' != tags){
                decoration_label = label + tags
            } // if
            profit_label = shape_mc.defend_mc.profit_mc.currentLabel;
        } // if
        if ('none' != intersection_mc.block_north_mc.currentLabel){
            block_label = intersection_mc.block_north_mc.currentLabel;
        } // if
        if ('none' != intersection_mc.block_east_mc.currentLabel){
            block_label = intersection_mc.block_east_mc.currentLabel;
        } // if
        if ('none' != intersection_mc.block_south_mc.currentLabel){
            block_label = intersection_mc.block_south_mc.currentLabel;
        } // if
        if ('none' != intersection_mc.block_west_mc.currentLabel){
            block_label = intersection_mc.block_west_mc.currentLabel;
        } // if
    } else{
        if ('none' != territory_label && 'neutral' != territory_label){
            info_label = 'show';
        } // if
        if ('none' != intersection_mc.decoration_mc.currentLabel){
            info_label = 'show';
            decoration_label = intersection_mc.decoration_mc.currentLabel;
        } // if
        if ('none' != intersection_mc.top_move_mc.currentLabel){
            info_label = 'show';
        } // if
    } // if
    globe.root.info_mc.gotoAndPlay(info_label);
    globe.root.info_mc.stone_mc.gotoAndPlay(stone_label);
    globe.root.info_mc.decoration_mc.gotoAndPlay(decoration_label);
    globe.root.info_mc.territory_mc.gotoAndPlay(territory_label);
    globe.root.info_mc.top_move_mc.gotoAndPlay(top_move_label);
    globe.root.info_mc.profit_mc.gotoAndPlay(profit_label);
    globe.root.info_mc.block_mc.gotoAndPlay(block_label);
    globe.root.info_mc.dragon_status_mc.gotoAndPlay(dragon_status_label);
    globe.show_info_sequence(mouse_event);
} // function show_info

function hide_info(mouse_event){
    /*For example, see show info.
    */
    globe.imitate( get_hide_info_news() );
    globe.hide_info_sequence(mouse_event);
} // function hide_info






function show_info_sequence(mouse_event){
    /*Moonhyoung sees info of intersection.
    >>> moonhyoung = globe_class()
    >>> moonhyoung.create()
    >>> from pattern import get_info_sequence_news_2_2
    >>> news = get_info_sequence_news_2_2()
    >>> //// olds = imitate_news(moonhyoung.root, news)
    >>> //// moonhyoung.info = upgrade(moonhyoung.info, news['info'])

    Upgrade info.   On mouse over 2,2, see mark at 1,2.
    >>> news = get_info_sequence_news_2_2()
    >>> moonhyoung.info['info_mc']
    >>> moonhyoung.push_news(news)
    >>> moonhyoung.info['_2_2_mc'][0]['info_mc']['decoration_mc']['pattern_txt']['text']
    'CONNECT'
    >>> moonhyoung.info['_2_2_mc'][0]['_1_2_mc']['mark_mc']['currentLabel']
    'show'

    >>> mouse_event = MouseEvent(MouseEvent.MOUSE_OVER)
    >>> mouse_event.currentTarget = moonhyoung.root._2_2_mc
    >>> moonhyoung.root.info_mc.decoration_mc.pattern_txt.text
    ''
    >>> moonhyoung.root._1_2_mc.mark_mc.currentLabel
    'none'
    >>> moonhyoung.show_info_sequence(mouse_event)
    >>> moonhyoung.update(None)
    >>> moonhyoung.root.info_mc.decoration_mc.pattern_txt.text
    'CONNECT'
    >>> moonhyoung.root._1_2_mc.mark_mc.currentLabel
    'show'

    Upon mouse out, set the mark && info pattern text to nothing.
    >>> moonhyoung.hide_info_sequence(mouse_event)
    >>> moonhyoung.update(None)
    >>> moonhyoung.root.info_mc.decoration_mc.pattern_txt.text
    ''
    >>> moonhyoung.root._1_2_mc.mark_mc.currentLabel
    'none'

    Show info calls show info sequence.  
    >>> moonhyoung.push_news(news)
    >>> moonhyoung.show_info(mouse_event)
    >>> moonhyoung.update(None)
    >>> moonhyoung.root.info_mc.decoration_mc.pattern_txt.text
    'CONNECT'
    >>> moonhyoung.root._1_2_mc.mark_mc.currentLabel
    'show'

    Hide info calls hide info sequence.  
    >>> moonhyoung.ambassador = echo_protocol_class()
    >>> moonhyoung.hide_info(mouse_event)
    >>> moonhyoung.update(None)
    >>> moonhyoung.root.info_mc.decoration_mc.pattern_txt.text
    ''
    >>> moonhyoung.root._1_2_mc.mark_mc.currentLabel
    'none'

    If multiple info, cycle every 2 seconds.
    >>> second_mark = {'_0_2_mc': {'mark_mc': {'currentLabel': 'show'}}}
    >>> moonhyoung.info['_2_2_mc'].push(second_mark)
    >>> moonhyoung.show_info_sequence(mouse_event)
    >>> moonhyoung.update(None)
    >>> moonhyoung.root._1_2_mc.mark_mc.currentLabel
    'show'
    >>> moonhyoung.root._0_2_mc.mark_mc.currentLabel
    'none'
    >>> time.sleep(2)
    >>> // moonhyoung.show_info_sequence(mouse_event)
    >>> moonhyoung.update(None)
    >>> moonhyoung.root._1_2_mc.mark_mc.currentLabel
    'none'
    >>> moonhyoung.root._0_2_mc.mark_mc.currentLabel
    'show'
    >>> time.sleep(2)
    >>> // moonhyoung.show_info_sequence(mouse_event)
    >>> moonhyoung.update(None)
    >>> moonhyoung.root._1_2_mc.mark_mc.currentLabel
    'show'
    >>> moonhyoung.root._0_2_mc.mark_mc.currentLabel
    'none'
    */
    var intersection_mc = mouse_event.currentTarget;
    var sequence = globe.info[intersection_mc.name];
    if (sequence && 1 <= sequence.length){
        globe.info_sequence = sequence
    } // if
} // function show_info_sequence

function _get_info_sequence(sequence){
    /*For example, see show_info_sequence
    */
    if (sequence && 1 <= sequence.length){
        var index = int(getTimer() / 2000) % sequence.length;
        var news = sequence[index];
        var reverted = imitate_news(globe.root, globe.info_olds);
        var olds = imitate_news(globe.root, news);
        globe.info_olds = olds;
    } // if
} // function _get_info_sequence

function hide_info_sequence(mouse_event){
    /*For example, see show_info_sequence
    */
    if (globe.info_olds){
        var olds = imitate_news(globe.root, globe.info_olds);
        globe.info_olds = {};
        globe.info_sequence = [];
    } // if
} // function hide_info_sequence







function login(mouse_event){
    var news = {
        'gateway_mc': {
            'currentLabel': 'enter'
        }
    };
    globe.publish(news);
}

function enter_level_1(mouse_event){
    var news = {
        'lobby_mc': {
            'level_1_mc': {
                'currentLabel': 'enter'
            }
        }
    };
    globe.publish(news);
}

function create_table(mouse_event){
    var news = {
        'lobby_mc': {
            'create_mc': {
                'currentLabel': 'enter'
            }
        }
    }
    globe.publish(news);
}

function join_table(mouse_event){
    var news = {
        'lobby_mc': {
            'join_mc': {
                'currentLabel': 'enter'
            }
        }
    };
    globe.publish(news);
}

function start_game(mouse_event){
    var news = {
        'game_over_mc': {
            'start_mc': {
                'currentLabel': 'enter'
            }
        }
    };
    globe.publish(news);
}

function extra_stone(mouse_event) {
    var news = {'extra_stone_gift_mc':  {
        'use_mc': {'currentLabel':  'enter'}
        }
    };
    globe.publish(news);
}

function hide(mouse_event) {
    var news = {'hide_gift_mc':  {
        'use_mc': {'currentLabel':  'enter'}
        }
    };
    globe.publish(news);
}


//function do_pass(mouse_event) {
//    trace('info: do_pass:  starting');
//    var news = note(mouse_event.currentTarget, 'currentLabel', 'enter');
//    globe.publish(news);
//}

function toggle_option(mouse_event) {
    trace('info: toggle_option:  starting');
    var news = {};
    var enter_news = note(mouse_event.currentTarget, 'currentLabel', 'enter');
    globe.revise(enter_news);
    news = upgrade(news, enter_news);
    var event_news = note(mouse_event.currentTarget, 'dispatchEvent', mouse_event.type);
    news = upgrade(news, event_news)
    var my_news = globe.insert_credentials(news);
    globe.ambassador.send(my_news);
}


function board_3_3(mouse_event) {
    trace('info: board_3_3:  starting');
    var news = note(mouse_event.currentTarget, 'currentLabel', 'enter');
    globe.publish(news);
}

function confirm_board_3_3(mouse_event) {
    globe.confirm_board_size('_3_3');
}

function board_5_5(mouse_event) {
    trace('info: board_5_5:  starting');
    var news = note(mouse_event.currentTarget, 'currentLabel', 'enter');
    globe.publish(news);
}

function confirm_board_5_5(mouse_event) {
    globe.confirm_board_size('_5_5');
}

function board_7_7(mouse_event) {
    trace('info: board_7_7:  starting');
    var news = note(mouse_event.currentTarget, 'currentLabel', 'enter');
    globe.publish(news);
}

function confirm_board_7_7(mouse_event) {
    globe.confirm_board_size('_7_7');
}

function board_9_9(mouse_event) {
    trace('info: board_9_9:  starting');
    var news = note(mouse_event.currentTarget, 'currentLabel', 'enter');
    globe.publish(news);
}

function confirm_board_9_9(mouse_event) {
    globe.confirm_board_size('_9_9');
}



function confirm_board_size(size){
    /*Constrain && snap intersections to the board.
    >>> laurens = globe_class()
    >>> laurens.create()
    >>> laurens.setup_events()
    >>> laurens.ambassador = echo_protocol_class()
    >>> laurens.confirm_board_size('_5_5')
    >>> laurens.intersection_mc_array.length
    5
    >>> laurens.root.currentLabel
    '_5_5'

    Snap intersections.
    >>> laurens.root._0_0_mc.x
    100

    Do ! leave lobby.
    >>> laurens.root.gotoAndPlay('lobby')
    >>> laurens.confirm_board_size('_9_9')
    >>> laurens.root.currentLabel
    'lobby'
    */
    trace('info:confirm_board'+ size +':  starting');
    // ActionScript gotcha [1] --> .charAt(1)
    size = String(size);
    var length = int(size.charAt(1)); 
    globe.intersection_mc_array = get_intersection_array(
            globe.root, length);
    var size_news = {};
    // ActionScript gotcha {a: 1} == {'a': 1}
    size_news[size + '_mc'] = {
        'enter_mc': {
            'currentLabel': 'none'
        }
    }
    var news = {
        'game_over_mc': size_news
    }
    if ('lobby' != globe.root.currentLabel){
        news['currentLabel'] = size;
    } // if
    globe.revise(news);
    globe.snap_intersections(length);
} // function confirm_board_size
    //- globe.publish_x_y(globe.intersection_mc_array)

function snap_intersections(intersection_per_line, stage_pixel = 600,
        original_pixel_per_space = 60, offstage = 1000, 
        max_intersection_per_line = 9){
    /*Snap intersection && strike.  Move excess off-stage.
    >>> moonhyoung = globe_class()
    >>> moonhyoung.create(1)
    >>> moonhyoung.snap_intersections(9, 600)
    >>> moonhyoung.root._0_0_mc.x
    60
    >>> moonhyoung.root._0_0_mc.y
    60
    >>> moonhyoung.root._8_8_mc.x
    540
    >>> moonhyoung.root._8_8_mc.y
    540
    >>> moonhyoung.root._8_8_mc.scaleX
    1.0
    >>> moonhyoung.root._8_8_mc.scaleY
    1.0
    >>> moonhyoung.snap_intersections(3, 600)
    >>> moonhyoung.root._0_0_mc.x
    150
    >>> moonhyoung.root._0_0_mc.y
    150
    >>> moonhyoung.root._8_8_mc.x
    1000
    >>> moonhyoung.root._8_8_mc.y
    1000
    >>> moonhyoung.root._8_8_mc.scaleX
    2.5
    >>> moonhyoung.root._8_8_mc.scaleY
    2.5
    */
    var gutters = 1;
    var pixel_per_space = stage_pixel 
            / (intersection_per_line + gutters);
    var scale = Number(pixel_per_space) / original_pixel_per_space;
    for (var row = 0; row < max_intersection_per_line; row++){
        var y = offstage;
        if (row < intersection_per_line){
            y = pixel_per_space + (pixel_per_space * row);
        } // if
        for (var column = 0; column < max_intersection_per_line; column++){
            var x = offstage;
            if (column < intersection_per_line){
                x = pixel_per_space + (pixel_per_space * column);
            } // if
            var name = '_' + row.toString() + '_' + column.toString() + '_mc';
            var _mc = globe.root[name];
            _mc.x = x;
            _mc.y = y;
            _mc.scaleX = scale;
            _mc.scaleY = scale;
            var strike_name = '_' + row.toString() 
                    + '_' + column.toString() + '_strike_mc';
            var strike_mc = globe.root[strike_name];
            strike_mc.x = x;
            strike_mc.y = y;
            strike_mc.scaleX = scale;
            strike_mc.scaleY = scale;
        } // for
    } // for
} // function snap_intersections






function setup_move_movieclip(){
    // can movieclip still play inside?  watch a capture at 0,0.  yes. 
    globe.root._0_0_mc.x = 100;
    globe.root._0_0_mc.y = 100;
    globe.root._0_0_mc.scale = 1;
    globe.root._0_0_strike_mc.x = 100;
    globe.root._0_0_strike_mc.y = 100;
    globe.root._0_0_strike_mc.scale = 1;
}

function problem(mouse_event) {
    var problem_name = mouse_event.currentTarget.parent.name;
    var news = get_problem_news(problem_name);
    globe.revise(news);
    var event_news = note(mouse_event.currentTarget, 'dispatchEvent', mouse_event.type);
    news = upgrade(news, event_news);
    var my_news = globe.insert_credentials(news);
    globe.ambassador.send(my_news);
    //- globe.publish(news);
}


function _publish_event(mouse_event, news) {
    var mc_name = mouse_event.currentTarget.name;
    var mc_news = note(mouse_event.currentTarget, 
        'currentLabel', 'enter');
    news = upgrade(news, mc_news);
    globe.revise(news);
    var event_news = note(mouse_event.currentTarget, 
        'dispatchEvent', mouse_event.type);
    news = upgrade(news, event_news);
    var my_news = globe.insert_credentials(news);
    globe.ambassador.send(my_news);
}

function parent_goto_mc_name(mouse_event) {
    globe._publish_event(mouse_event, {});
}

var author_parent_goto_mc_name:Function = parent_goto_mc_name;
var remove_table:Function = parent_goto_mc_name;
var toggle_menu:Function = parent_goto_mc_name;
var problem_name:Function = parent_goto_mc_name;
var grandparent_goto_mc_name = parent_goto_mc_name;
var great_grandparent_goto_mc_name = parent_goto_mc_name;
var do_pass = parent_goto_mc_name;


function chat_input(mouse_event) {
    var chat_news = get_note(globe.root.chat_input_txt, 'text');
    globe._publish_event(mouse_event, chat_news);
}

function on_press_enter_chat_input(keyboard_event) {
    if (Keyboard.ENTER == keyboard_event.keyCode) {
        var mouseDown = new MouseEvent(MouseEvent.MOUSE_DOWN);
        globe.root.chat_input_mc.dispatchEvent(mouseDown);
        // globe.chat_input(mouse_event);
    }
}

function white_computer(mouse_event) {
    var news = {
        'game_over_mc': {
            'white_computer_mc': {
                'enter_mc': {'currentLabel': 'enter'}
            }
        }
    };
    globe.publish(news);
}

function enter_lobby(mouse_event) {
    var news = {
        'lobby_mc': {
            'enter_mc': {'currentLabel': 'enter'}
        }
    };
    globe.publish(news);
}

function activate_clock(mouse_event) {
    trace('info: activate_clock:  starting');
    var news = {
        'clock_mc': {
            'enter_mc': {'currentLabel': 'enter'}
        }
    };
    globe.publish(news);
}

function publish(news) {
    var now = getTimer();
    var time_news = {'title_mc': {'time_txt': {'text': now.toString()}}};
    news = upgrade(news, time_news);
    push_news(news);

    var my_news = globe.insert_credentials(news);
    globe.ambassador.send(my_news);
}

function save_one_child(root, child_list){
    /*At end, revert original master, slave, but ! username || password.
    >>> laurens = globe_class()
    >>> laurens.create()
    >>> laurens.setup_events()
    >>> laurens.ambassador = print_protocol_class()
    >>> laurens.root.title_mc.username_txt.text = 'laurens'
    >>> laurens.root.title_mc.password_txt.text = 'l'
    >>> laurens.root.title_mc.master_txt.text = '777'
    >>> laurens.root.title_mc.slave_txt.text = '666'

    >>> old_log_level = trace()getLogger:.level
    >>> trace()getLogger:.setLevel(trace(lCRITICAL)

    If nothing, do nothing && return empty list.
    >>> laurens.save_one_child:aurens.root, []) //doctest: +ELLIPSIS
    []

    If nothing, do nothing && return empty list.
    >>> laurens.save_one_child(laurens.root, [None]) //doctest: +ELLIPSIS
    []

    Revert master && return popped list.
    >>> laurens.save_one_child(laurens.root, [MovieClip()]) //doctest: +ELLIPSIS
    {...'master_txt': {'text': 'master'}...
    []

    Do ! transmit log_txt && return popped list.
    >>> laurens.save_one_child(laurens.root, [MovieClip()]) //doctest: +ELLIPSIS
    {...'log_txt': {'text': 'log'}...
    []
        
    Do ! transmit log_txt, which may be too large || contain indecipherable characters.
    >>> messy_log_txt = TextField()
    >>> messy_log_txt.name = 'log_txt'
    >>> messy_log_txt.text = '161 readResponse:  result = [object Object]rreadResponse:  status:  rbytesAvailable = 143; event.bytesLoaded = 143; attempt = 0rimitate completersend:  [object Object]r160 readResponse:  result = [object Object]rreadResponse:  status:  rbytesAvailable = 143; event.bytesLoaded = 143;'
    
    >>> laurens.save_one_child(laurens.root, [messy_log_txt, MovieClip()]) //doctest: +ELLIPSIS
    {...'log_txt': {'text': 'log'}...
    [<actionscript.MovieClip object at 0x...>]

    >>> trace()getLogger:.setLevel(old_log_level)
    */
    if (0 == count_item(child_list)){
        return [];
    } // if
    var news = globe.insert_credentials({});
    var child = child_list.shift(); // XXX .as --> child_list.shift()
    var save_child = {};
    if (null == child){
        globe.update_log('error ' + child.toString());
        trace('error:save_one_child: empty ' + child.toString());
        return child_list;
    } else if ('log_txt' == child.name){
        save_child['log_txt'] = {};
        save_child['log_txt']['text'] = 'log';
    } else{
        trace('info:save_one_child: ' + child.name);
        save_child = compose_root(insert_label_and_position, child);
    } // if
    news = upgrade(news, save_child);
    var save = {};
    if (1 <= child_list.length){
        root['save_mc'].gotoAndPlay('entering');
        save = compose_root(insert_label, root['save_mc']);
    } else{
        root['save_mc'].gotoAndPlay('enter');
        save = compose_root(insert_label_and_position, 
            root['save_mc']);
        save = insert_label_and_position(root, save);
        save = upgrade(save, globe.original_stage);
    } // if
    news = upgrade(news, save);
    globe.ambassador.send(news);
    return child_list;
} // function save_one_child

// set each theme_mc inside each intersection.


function set_theme(intersection_mc_array, theme_label){
    // theme_txt.text = theme_label; // XXX infinite loop!
	for (var row:uint = 0; row < intersection_mc_array.length; row++) {
		for (var column:uint = 0; column < intersection_mc_array[row].length; column++) {
            var intersection_mc = intersection_mc_array[row][column];
            gotoAndPlayLabel(intersection_mc.overlay_mc, theme_label);
            if (undefined != intersection_mc.black_shape_mc.theme_mc) {
                // The 30 basic connected shapes do not have theme yet.
                if ("basic" != theme_label 
                        || "_0000" == intersection_mc.black_shape_mc.currentLabel) {
                    gotoAndPlayLabel(intersection_mc.black_shape_mc.theme_mc, theme_label);
                }
            } 
            else {
                trace("set_theme:  I cannot find theme_mc " 
                    + theme_label 
                    + " at " + row + ", " + column);
            }
            if (undefined != intersection_mc.white_shape_mc.theme_mc) {
                // The 30 basic connected shapes do not have theme yet.
                if ("basic" != theme_label 
                        || "_0000" == intersection_mc.white_shape_mc.currentLabel) {
                    gotoAndPlayLabel(intersection_mc.white_shape_mc.theme_mc, theme_label);
                }
            } 
            else {
                trace("set_theme:  I cannot find theme_mc " 
                    + theme_label 
                    + " at " + row + ", " + column);
            }
            // territory mark
            if (undefined != intersection_mc.territory_mc.theme_mc) {
                gotoAndPlayLabel(intersection_mc.territory_mc.theme_mc, theme_label);
            }
            /*
            gotoAndPlayLabel(intersection_mc.hide_mc.theme_mc, 
                    theme_label);
            gotoAndPlayLabel(intersection_mc.star_mc.theme_mc,  
                    theme_label);
            gotoAndPlayLabel(intersection_mc.block_north_mc.theme_mc, theme_label);
            gotoAndPlayLabel(intersection_mc.block_east_mc.theme_mc, theme_label);
            gotoAndPlayLabel(intersection_mc.block_south_mc.theme_mc, theme_label);
            gotoAndPlayLabel(intersection_mc.block_west_mc.theme_mc, theme_label);
            */
            // XXX HACK:
            for (var c = 0; c < intersection_mc.decoration_mc.numChildren; c++) {
                var child_mc = intersection_mc.decoration_mc.getChildAt(c);
                if ('theme_mc' == child_mc.name) {
                    gotoAndPlayLabel(child_mc, theme_label);
                }
            }
        }
    }
    //- gotoAndPlayLabel(board_mc.theme_mc, theme_label);
    //- gotoAndPlayLabel(theme_mc, theme_label);
    //- gotoAndPlayLabel(turn_mc.theme_mc, theme_label);
    gotoAndPlayLabel(turn_mc.black_theme_mc, theme_label);
    gotoAndPlayLabel(turn_mc.white_theme_mc, theme_label);
    //- gotoAndPlayLabel(black_last_move_mc.theme_mc, theme_label);
    //- gotoAndPlayLabel(white_last_move_mc.theme_mc, theme_label);
    gotoAndPlayLabel(extra_stone_gift_mc.theme_mc, theme_label);
    gotoAndPlayLabel(hide_gift_mc._1, theme_label);
    //- gotoAndPlayLabel(hide_gift_mc._2, theme_label);
    //- gotoAndPlayLabel(hide_gift_mc._3, theme_label);
    //- gotoAndPlayLabel(game_over_mc.score_mc.hide_gift_mc, 
    //-         theme_label);
    //- gotoAndPlayLabel(game_over_mc.score_mc.undo_gift_mc, 
    //-         theme_label);
    // XXX cannot access child of SimpleButton
    // gotoAndPlayLabel(undo_gift_btn.theme_mc, theme_label);
}

// on click button, switch theme button's name
function set_theme_to_my_name(mouse_event:MouseEvent){
    var theme_name = mouse_event.currentTarget.name;
    trace("set_theme_to_my_name:  " + theme_name);
    set_theme(intersection_mc_array, theme_name);
    //- update(null);
    theme_txt.text = theme_name;
}


// HACK:  lazily set theme instance to current theme.
// usage:  in function layer:
// (this.root as MovieClip).snap_theme(this);
function snap_theme(movie_clip){
    if (movie_clip && movie_clip.root) {
        var root_mc = (movie_clip.root as MovieClip);
        if (null != root_mc.theme_txt) {
            var theme_name = root_mc.theme_txt.text;
            if (movie_clip.currentLabel != theme_name) {
	            movie_clip.gotoAndPlay(theme_name);
            }
        }
    }
}

basic.addEventListener(MouseEvent.MOUSE_DOWN, set_theme_to_my_name);
cake.addEventListener(MouseEvent.MOUSE_DOWN, set_theme_to_my_name);
traditional.addEventListener(MouseEvent.MOUSE_DOWN, set_theme_to_my_name);
cake_take.addEventListener(MouseEvent.MOUSE_DOWN, set_theme_to_my_name);
castle.addEventListener(MouseEvent.MOUSE_DOWN, set_theme_to_my_name);

function set_theme_txt(text_event){
    // on input text, set theme.
    trace("set_theme_txt:  " + text_event.text);
    set_theme(intersection_mc_array, text_event.text);
}


function save_stage(mouse_event) {
    //'''Because 96 kB leads server to complain of error, save in parts.'''
    trace('save_stage:  starting');
    globe.save_list = new Array();
    for (var c = 0; c < globe.root.numChildren; c++) {
        var child = globe.root.getChildAt(c);
        globe.save_list.push(child);
    }
    globe.save_list = globe.save_one_child(globe.root, globe.save_list);
}


function load_stage(mouse_event) {
    trace('load_stage:  starting');
    globe.root['load_mc'].gotoAndPlay('entering');
    var message = compose_root(globe.credentials, globe.root['load_mc']);
    globe.ambassador.send(message);
}


function setup_formations(){
    /*Formations get in the way of mouse click so they are turned off.
    >>> laurens = globe_class()
    >>> laurens.create()
    >>> laurens.setup_formations()

    //disable formations
    //>>> laurens.root.formation_connect_mc.mouseEnabled
    //False
    //>>> laurens.root.formation_connect_mc.mouseChildren
    //False
    //>>> laurens.root.formation_perch_mc.mouseEnabled
    //False
    //>>> laurens.root.formation_perch_mc.mouseChildren
    //False
    */
    var child_count = globe.root.numChildren;
    for (var c = 0; c < child_count; c++){
        var child = globe.root.getChildAt(c);
        // py:indexOf === as:indexOf
        if (0 == child.name.indexOf('formation')){
            child.mouseEnabled = false;
            child.mouseChildren = false;
        } // if
    } // for
} // function setup_formations
    //globe.root.formation_connect_mc.mouseEnabled = false
    //globe.root.formation_connect_mc.mouseChildren = false
    //globe.root.formation_diagonal_attack_mc.mouseEnabled = false
    //globe.root.formation_diagonal_attack_mc.mouseChildren = false
    //globe.root.formation_diagonal_connect_mc.mouseEnabled = false
    //globe.root.formation_diagonal_connect_mc.mouseChildren = false
    //globe.root.formation_diagonal_cut_half_mc.mouseEnabled = false
    //globe.root.formation_diagonal_cut_half_mc.mouseChildren = false
    //globe.root.formation_diagonal_mc.mouseEnabled = false
    //globe.root.formation_diagonal_mc.mouseChildren = false
    //globe.root.formation_field_mc.mouseEnabled = false
    //globe.root.formation_field_mc.mouseChildren = false
    //globe.root.formation_jump_attack_mc.mouseEnabled = false
    //globe.root.formation_jump_attack_mc.mouseChildren = false
    //globe.root.formation_jump_mc.mouseEnabled = false
    //globe.root.formation_jump_mc.mouseChildren = false
    //globe.root.formation_knight_attack_mc.mouseEnabled = false
    //globe.root.formation_knight_attack_mc.mouseChildren = false
    //globe.root.formation_knight_cut_half_mc.mouseEnabled = false
    //globe.root.formation_knight_cut_half_mc.mouseChildren = false
    //globe.root.formation_knight_mc.mouseEnabled = false
    //globe.root.formation_knight_mc.mouseChildren = false
    //globe.root.formation_leap_attack_mc.mouseEnabled = false
    //globe.root.formation_leap_attack_mc.mouseChildren = false
    //globe.root.formation_leap_mc.mouseEnabled = false
    //globe.root.formation_leap_mc.mouseChildren = false
    //globe.root.formation_peep_diagonal_mc.mouseEnabled = false
    //globe.root.formation_peep_diagonal_mc.mouseChildren = false
    //globe.root.formation_peep_knight_mc.mouseEnabled = false
    //globe.root.formation_peep_knight_mc.mouseChildren = false
    //globe.root.formation_peep_mc.mouseEnabled = false
    //globe.root.formation_peep_mc.mouseChildren = false
    //globe.root.formation_quarter_field_mc.mouseEnabled = false
    //globe.root.formation_quarter_field_mc.mouseChildren = false
    //globe.root.formation_tiger_jaw_mc.mouseEnabled = false
    //globe.root.formation_tiger_jaw_mc.mouseChildren = false
    //globe.root.formation_tiger_mouth_mc.mouseEnabled = false
    //globe.root.formation_tiger_mouth_mc.mouseChildren = false

function setup_events(){
    /*Archive original stage.
    >>> code_unit.doctest_unit(globe_class.save_one_child, log = false);
    */
    globe.original_stage = compose_root(insert_label_and_position,
            globe.root['title_mc']);
    delete globe.original_stage['title_mc']['username_txt'];
    delete globe.original_stage['title_mc']['password_txt'];
    globe.root.log_txt.text = 'log'
    var news_log = compose_root(insert_label_and_position,
            globe.root['log_txt']);
    globe.original_stage = upgrade(globe.original_stage, news_log);
    globe.root.gotoAndPlay('login');
    globe.root.score_mc.bar_mc.gotoAndPlay('_0');
    globe.root.score_mc.bar_mc.marker_mc.capture_mc.gotoAndPlay('_0');
    globe.root.score_mc.bar_mc.marker_mc.change_txt.text = '0'
    globe.root.gateway_mc.none_mc.addEventListener(
            MouseEvent.MOUSE_DOWN, globe.parent_goto_mc_name);
    globe.root.comment_mc.none_mc.addEventListener(
            MouseEvent.MOUSE_DOWN, globe.parent_goto_mc_name);
    globe.root.chat_input_mc.addEventListener(
            MouseEvent.MOUSE_DOWN, globe.chat_input);
    globe.root.title_mc.start_btn.addEventListener(
            MouseEvent.MOUSE_DOWN, globe.login);
    globe.root.lobby_mc.level_1_mc.enter_btn.addEventListener(
            MouseEvent.MOUSE_DOWN, globe.enter_level_1);
    globe.root.lobby_mc.create_mc.addEventListener(
            MouseEvent.MOUSE_DOWN, globe.create_table);
    globe.root.lobby_mc.join_mc.enter_btn.addEventListener(
            MouseEvent.MOUSE_DOWN, globe.join_table);
    globe.root.game_over_mc.start_mc.addEventListener(
            MouseEvent.MOUSE_DOWN, globe.start_game);
    globe.root.game_over_mc.score_mc.lobby_mc.addEventListener(
            MouseEvent.MOUSE_DOWN, globe.remove_table);
    globe.root.save_mc.addEventListener(
            MouseEvent.MOUSE_DOWN, globe.save_stage);
    globe.root.load_mc.addEventListener(
            MouseEvent.MOUSE_DOWN, globe.load_stage);
    //- globe.root.turn_mc.white_mc.enter_btn.addEventListener(
    //-         MouseEvent.MOUSE_DOWN, globe.become_white);
    globe.root.extra_stone_gift_mc.use_mc.addEventListener(
            MouseEvent.MOUSE_DOWN, globe.extra_stone);
    globe.root.hide_gift_mc.use_mc.addEventListener(
            MouseEvent.MOUSE_DOWN, globe.hide);
    globe.root.pass_mc.addEventListener(
            MouseEvent.MOUSE_DOWN, globe.do_pass);
    globe.root.suicide_mc.enter_mc.addEventListener(
            MouseEvent.MOUSE_DOWN, globe.toggle_option);
    globe.root.option_mc.score_mc.enter_mc.addEventListener(
            MouseEvent.MOUSE_DOWN, globe.toggle_option);
    globe.root.option_mc.computer_pass_mc.enter_mc.addEventListener(
            MouseEvent.MOUSE_DOWN, globe.toggle_option);
    globe.root.option_mc.first_capture_mc.enter_mc.addEventListener(
            MouseEvent.MOUSE_DOWN, globe.toggle_option);
    globe.root.clock_mc.enter_mc.enter_btn.addEventListener(
            MouseEvent.MOUSE_DOWN, globe.activate_clock);
    globe.root.level_mc.none_mc.addEventListener(
            MouseEvent.MOUSE_DOWN, globe.parent_goto_mc_name);
    globe.root.theme_txt.addEventListener(
            TextEvent.TEXT_INPUT, globe.set_theme_txt);
    globe.root.cursor_mc.mouseEnabled = false;
    globe.root.cursor_mc.mouseChildren = false;
    //- globe.root.black_last_move_mc.mouseEnabled = false;
    //- globe.root.black_last_move_mc.mouseChildren = false;
    //- globe.root.white_last_move_mc.mouseEnabled = false;
    //- globe.root.white_last_move_mc.mouseChildren = false;
    globe.root.eat_mc.mouseEnabled = false;
    globe.root.eat_mc.mouseChildren = false;
    globe.root.addEventListener(MouseEvent.MOUSE_MOVE, globe.follow);
    globe.root.addEventListener(MouseEvent.MOUSE_DOWN, globe.mouse_shield);
    globe.setup_formations();
    globe.board_listens_to_mouse(globe.intersection_mc_array);
    globe.listen_to_game_over();
    globe.listen_to_lobby();
    globe._finish_flash_setup();
    globe.root.addEventListener(Event.ENTER_FRAME, globe.update);
} // function setup_events




function listen_to_parent(parent_name){
    /*May also listen to mouseOver || mouseOut.
        on mouse over{
            if opening note && length greater than || equal to 2{
                copy opening note from info_txt.text to info_mc._txt.text
                show info
            } // if
        on mouse out{
            if show info{
                hide info
            } // if
    >>> marije = globe_class()
    >>> marije.create()
    >>> marije.setup_events()
    >>> marije.ambassador = echo_protocol_class()
    >>> target = marije.root.lobby_mc._00_mc.capture_3_3_mc
    >>> target.info_txt.text = 'Surround a fire.'
    >>> marije.root.info_mc.currentLabel
    'none'
    >>> target.dispatchEvent(mouseOver)
    >>> marije.root.info_mc.currentLabel
    'show'
    >>> marije.root.info_mc.currentLabel
    'show'
    >>> target.dispatchEvent(mouseOut)
    >>> marije.root.info_mc.currentLabel
    'none'

    On click lobby, notify server.
    >>> marije.root.lobby_mc.main_mc._00_mc.dispatchEvent(mouseDown)
    >>> marije.ambassador.sends[-1]['lobby_mc']['main_mc']['_00_mc']['dispatchEvent']
    'mouseDown'
    >>> marije.root.lobby_mc._00_mc.main_mc.dispatchEvent(mouseDown)
    >>> marije.ambassador.sends[-1]['lobby_mc']['_00_mc']['main_mc']['dispatchEvent']
    'mouseDown'
    */
    globe.root.lobby_mc.main_mc[parent_name].addEventListener(
            MouseEvent.MOUSE_DOWN, globe.grandparent_goto_mc_name);
    globe.root.lobby_mc[parent_name].main_mc.addEventListener(
            MouseEvent.MOUSE_DOWN, globe.grandparent_goto_mc_name);
    children_listen_to_mouse(globe.root.lobby_mc[parent_name], 
            MouseEvent.MOUSE_DOWN, globe.problem_name, 'main_mc');
    children_listen_to_mouse(globe.root.lobby_mc[parent_name], 
            MouseEvent.MOUSE_OVER, globe.show_menu_info, 'main_mc');
    children_listen_to_mouse(globe.root.lobby_mc[parent_name], 
            MouseEvent.MOUSE_OUT, globe.hide_menu_info, 'main_mc');
} // function listen_to_parent



function listen_to_lobby(){
    globe.listen_to_parent('_00_mc');
    globe.listen_to_parent('_04_mc');
    globe.listen_to_parent('_07_mc');
    globe.listen_to_parent('_10_mc');
    globe.listen_to_parent('_14_mc');
    globe.listen_to_parent('_20_mc');
    globe.root.lobby_mc.main_mc.multiplayer_mc.addEventListener(
            MouseEvent.MOUSE_DOWN, globe.grandparent_goto_mc_name);
    globe.root.lobby_mc._main_mc.addEventListener(
            MouseEvent.MOUSE_DOWN, globe.parent_goto_mc_name);
    globe.root.lobby_mc.main_mc.login_mc.addEventListener(
            MouseEvent.MOUSE_DOWN, globe.great_grandparent_goto_mc_name);
    globe.root.lobby_mc.enter_mc.addEventListener(
            MouseEvent.MOUSE_DOWN, globe.enter_lobby);
    globe.root.menu_mc.toggle_mc.addEventListener(
            MouseEvent.MOUSE_DOWN, globe.toggle_menu);
    globe.root.menu_mc.lobby_mc.addEventListener(
            MouseEvent.MOUSE_DOWN, globe.remove_table);
} // function listen_to_lobby
    //globe.root.lobby_mc.multiplayer_mc.main_mc.addEventListener(
    //        MouseEvent.MOUSE_DOWN, globe.grandparent_goto_mc_name);
    //globe.root.lobby_mc._00_mc.capture_5_5_mc.addEventListener(
    //        MouseEvent.MOUSE_DOWN, globe.problem_name);
    //globe.root.lobby_mc._00_mc.capture_3_3_mc.addEventListener(
    //        MouseEvent.MOUSE_DOWN, globe.problem_name);
    //globe.root.lobby_mc._00_mc.dominate_3_3_mc.addEventListener(
    //        MouseEvent.MOUSE_DOWN, globe.problem_name);
    //globe.root.lobby_mc._00_mc.dominate_5_5_mc.addEventListener(
    //        MouseEvent.MOUSE_DOWN, globe.problem_name);
    //globe.root.lobby_mc._00_mc.score_5_5_mc.addEventListener(
    //        MouseEvent.MOUSE_DOWN, globe.problem_name);
    //globe.root.lobby_mc._10_mc.extra_stone_5_5_mc.addEventListener(
    //        MouseEvent.MOUSE_DOWN, globe.problem_name);
    //globe.root.lobby_mc._10_mc.extra_stone_5_5_2_mc.addEventListener(
    //        MouseEvent.MOUSE_DOWN, globe.problem_name);
    //globe.root.lobby_mc._10_mc.extra_stone_7_7_mc.addEventListener(
    //        MouseEvent.MOUSE_DOWN, globe.problem_name);
    //globe.root.lobby_mc._10_mc.extra_stone_7_7_2_mc.addEventListener(
    //        MouseEvent.MOUSE_DOWN, globe.problem_name);
    //globe.root.lobby_mc._10_mc.extra_stone_7_7_3_mc.addEventListener(
    //        MouseEvent.MOUSE_DOWN, globe.problem_name);
    //globe.root.lobby_mc._10_mc.extra_stone_7_7_4_mc.addEventListener(
    //        MouseEvent.MOUSE_DOWN, globe.problem_name);
    //globe.root.lobby_mc._10_mc.extra_stone_9_9_mc.addEventListener(
    //        MouseEvent.MOUSE_DOWN, globe.problem_name);
    //globe.root.lobby_mc._10_mc.extra_stone_9_9_2_mc.addEventListener(
    //        MouseEvent.MOUSE_DOWN, globe.problem_name);
    //globe.root.lobby_mc._10_mc.extra_stone_9_9_3_mc.addEventListener(
    //        MouseEvent.MOUSE_DOWN, globe.problem_name);
    //globe.root.lobby_mc._20_mc.hide_5_5_mc.addEventListener(
    //        MouseEvent.MOUSE_DOWN, globe.problem_name);
    //globe.root.lobby_mc._20_mc.hide_7_7_mc.addEventListener(
    //        MouseEvent.MOUSE_DOWN, globe.problem_name);
    //globe.root.lobby_mc._00_mc.capture_3_3_mc.addEventListener(
    //        MouseEvent.MOUSE_DOWN, globe.problem);
    //globe.root.lobby_mc._00_mc.capture_5_5_mc.addEventListener(
    //        MouseEvent.MOUSE_DOWN, globe.problem);
    //globe.root.lobby_mc._00_mc.dominate_3_3_mc.addEventListener(
    //        MouseEvent.MOUSE_DOWN, globe.problem);
    //globe.root.lobby_mc._00_mc.dominate_5_5_mc.addEventListener(
    //        MouseEvent.MOUSE_DOWN, globe.problem);
    //globe.root.lobby_mc._00_mc.score_5_5_mc.addEventListener(
    //        MouseEvent.MOUSE_DOWN, globe.problem);
    //globe.root.lobby_mc._00_mc.extra_stone_7_7_mc.addEventListener(
    //        MouseEvent.MOUSE_DOWN, globe.problem);
    //globe.root.lobby_mc._00_mc.extra_stone_7_7_2_mc.addEventListener(
    //        MouseEvent.MOUSE_DOWN, globe.problem);
    //globe.root.lobby_mc._00_mc.extra_stone_9_9_mc.addEventListener(
    //        MouseEvent.MOUSE_DOWN, globe.problem);
    //globe.root.lobby_mc._00_mc.hide_5_5_mc.addEventListener(
    //        MouseEvent.MOUSE_DOWN, globe.problem);
    //globe.root.lobby_mc._00_mc.hide_7_7_mc.addEventListener(
    //        MouseEvent.MOUSE_DOWN, globe.problem);
    //- globe.root.lobby_mc.single_player_mc.addEventListener(
    //-         MouseEvent.MOUSE_DOWN, globe.parent_goto_mc_name);




function listen_to_game_over(){
    globe.root.game_over_mc._3_3_mc.enter_mc.addEventListener(
            MouseEvent.MOUSE_DOWN, globe.board_3_3);
    globe.root.game_over_mc._3_3_mc.confirm_mc.addEventListener(
            MouseEvent.MOUSE_DOWN, globe.confirm_board_3_3);
    globe.root.game_over_mc._5_5_mc.enter_mc.addEventListener(
            MouseEvent.MOUSE_DOWN, globe.board_5_5);
    globe.root.game_over_mc._5_5_mc.confirm_mc.addEventListener(
            MouseEvent.MOUSE_DOWN, globe.confirm_board_5_5);
    globe.root.game_over_mc._7_7_mc.enter_mc.addEventListener(
            MouseEvent.MOUSE_DOWN, globe.board_7_7);
    globe.root.game_over_mc._7_7_mc.confirm_mc.addEventListener(
            MouseEvent.MOUSE_DOWN, globe.confirm_board_7_7);
    globe.root.game_over_mc._9_9_mc.enter_mc.addEventListener(
            MouseEvent.MOUSE_DOWN, globe.board_9_9);
    globe.root.game_over_mc._9_9_mc.confirm_mc.addEventListener(
            MouseEvent.MOUSE_DOWN, globe.confirm_board_9_9);
    globe.root.game_over_mc.white_computer_mc.enter_mc.addEventListener(
            MouseEvent.MOUSE_DOWN, globe.white_computer);
    globe.root.game_over_mc.extra_stone_available_mc._0_mc.addEventListener(
            MouseEvent.MOUSE_DOWN, globe.author_parent_goto_mc_name);
    globe.root.game_over_mc.extra_stone_available_mc._1_mc.addEventListener(
            MouseEvent.MOUSE_DOWN, globe.author_parent_goto_mc_name);
    globe.root.game_over_mc.extra_stone_available_mc._2_mc.addEventListener(
            MouseEvent.MOUSE_DOWN, globe.author_parent_goto_mc_name);
    globe.root.game_over_mc.extra_stone_available_mc._3_mc.addEventListener(
            MouseEvent.MOUSE_DOWN, globe.author_parent_goto_mc_name);
    globe.root.game_over_mc.extra_stone_available_mc._4_mc.addEventListener(
            MouseEvent.MOUSE_DOWN, globe.author_parent_goto_mc_name);
    globe.root.game_over_mc.extra_stone_available_mc._5_mc.addEventListener(
            MouseEvent.MOUSE_DOWN, globe.author_parent_goto_mc_name);
    globe.root.game_over_mc.extra_stone_available_mc._6_mc.addEventListener(
            MouseEvent.MOUSE_DOWN, globe.author_parent_goto_mc_name);
    globe.root.game_over_mc.extra_stone_available_mc._7_mc.addEventListener(
            MouseEvent.MOUSE_DOWN, globe.author_parent_goto_mc_name);
    globe.root.game_over_mc.extra_stone_available_mc._8_mc.addEventListener(
            MouseEvent.MOUSE_DOWN, globe.author_parent_goto_mc_name);
    globe.root.game_over_mc.extra_stone_available_mc._9_mc.addEventListener(
            MouseEvent.MOUSE_DOWN, globe.author_parent_goto_mc_name);
    globe.root.game_over_mc.hide_available_mc._0_mc.addEventListener(
            MouseEvent.MOUSE_DOWN, globe.author_parent_goto_mc_name);
    globe.root.game_over_mc.hide_available_mc._1_mc.addEventListener(
            MouseEvent.MOUSE_DOWN, globe.author_parent_goto_mc_name);
    globe.root.game_over_mc.hide_available_mc._2_mc.addEventListener(
            MouseEvent.MOUSE_DOWN, globe.author_parent_goto_mc_name);
    globe.root.game_over_mc.hide_available_mc._3_mc.addEventListener(
            MouseEvent.MOUSE_DOWN, globe.author_parent_goto_mc_name);
    globe.root.game_over_mc.hide_available_mc._4_mc.addEventListener(
            MouseEvent.MOUSE_DOWN, globe.author_parent_goto_mc_name);
    globe.root.game_over_mc.hide_available_mc._5_mc.addEventListener(
            MouseEvent.MOUSE_DOWN, globe.author_parent_goto_mc_name);
    globe.root.game_over_mc.hide_available_mc._6_mc.addEventListener(
            MouseEvent.MOUSE_DOWN, globe.author_parent_goto_mc_name);
    globe.root.game_over_mc.hide_available_mc._7_mc.addEventListener(
            MouseEvent.MOUSE_DOWN, globe.author_parent_goto_mc_name);
    globe.root.game_over_mc.hide_available_mc._8_mc.addEventListener(
            MouseEvent.MOUSE_DOWN, globe.author_parent_goto_mc_name);
    globe.root.game_over_mc.hide_available_mc._9_mc.addEventListener(
            MouseEvent.MOUSE_DOWN, globe.author_parent_goto_mc_name);
} // function listen_to_game_over
    



/*
//function setup_events(globe) {
//    globe.original_stage = compose_root(insert_label_and_position,
//            globe.root['title_mc']);
//    delete globe.original_stage['title_mc']['username_txt'];
//    delete globe.original_stage['title_mc']['password_txt'];
//    globe.root.gotoAndPlay('login');
//    globe.root.score_mc.bar_mc.gotoAndPlay('_0');
//    globe.root.score_mc.bar_mc.marker_mc.capture_mc.gotoAndPlay('_0');
//    globe.root.score_mc.bar_mc.marker_mc.change_txt.text = '0';
//    globe.root.log_txt.text = '';
//    globe.root.gateway_mc.none_mc.addEventListener(
//            MouseEvent.MOUSE_DOWN, globe.parent_goto_none);
//    globe.root.comment_mc.none_mc.addEventListener(
//            MouseEvent.MOUSE_DOWN, globe.parent_goto_none);
//    globe.root.chat_input_mc.addEventListener(
//            MouseEvent.MOUSE_DOWN, globe.chat_input);
//    globe.title_mc.start_btn.addEventListener(
//            MouseEvent.MOUSE_DOWN, globe.login);
//    globe.root.lobby_mc.level_1_mc.enter_btn.addEventListener(
//            MouseEvent.MOUSE_DOWN, globe.enter_level_1);
//    globe.root.lobby_mc.create_mc.addEventListener(
//            MouseEvent.MOUSE_DOWN, globe.create_table);
//    globe.root.lobby_mc.join_mc.enter_btn.addEventListener(
//            MouseEvent.MOUSE_DOWN, globe.join_table);
//    globe.root.game_over_mc.start_mc.addEventListener(
//            MouseEvent.MOUSE_DOWN, start_game);
//    globe.root.save_mc.addEventListener(
//            MouseEvent.MOUSE_DOWN, save_stage);
//    globe.root.load_mc.addEventListener(
//            MouseEvent.MOUSE_DOWN, load_stage);
//    //- globe.root.turn_mc.white_mc.enter_btn.addEventListener(
//    //-        MouseEvent.MOUSE_DOWN, globe.become_white);
//    globe.root.extra_stone_gift_mc.use_mc.addEventListener(
//            MouseEvent.MOUSE_DOWN, globe.extra_stone);
//    globe.root.hide_gift_mc.use_mc.addEventListener(
//            MouseEvent.MOUSE_DOWN, globe.hide);
//    globe.root.pass_mc.addEventListener(
//            MouseEvent.MOUSE_DOWN, globe.do_pass);
//    globe.root.suicide_mc.enter_mc.addEventListener(
//            MouseEvent.MOUSE_DOWN, globe.toggle_option);
//    globe.root.option_mc.score_mc.enter_mc.addEventListener(
//            MouseEvent.MOUSE_DOWN, globe.toggle_option);
//    globe.root.option_mc.computer_pass_mc.enter_mc.addEventListener(
//            MouseEvent.MOUSE_DOWN, globe.toggle_option);
//    globe.root.option_mc.first_capture_mc.enter_mc.addEventListener(
//            MouseEvent.MOUSE_DOWN, globe.toggle_option);
//    globe.root.clock_mc.enter_mc.enter_btn.addEventListener(
//            MouseEvent.MOUSE_DOWN, globe.activate_clock);
//    globe.root.game_over_mc._3_3_mc.enter_mc.addEventListener(
//            MouseEvent.MOUSE_DOWN, globe.board_3_3);
//    globe.root.game_over_mc._3_3_mc.confirm_mc.addEventListener(
//            MouseEvent.MOUSE_DOWN, globe.confirm_board_3_3);
//    globe.root.game_over_mc._5_5_mc.enter_mc.addEventListener(
//            MouseEvent.MOUSE_DOWN, globe.board_5_5);
//    globe.root.game_over_mc._5_5_mc.confirm_mc.addEventListener(
//            MouseEvent.MOUSE_DOWN, globe.confirm_board_5_5);
//    globe.root.game_over_mc._7_7_mc.enter_mc.addEventListener(
//            MouseEvent.MOUSE_DOWN, globe.board_7_7);
//    globe.root.game_over_mc._7_7_mc.confirm_mc.addEventListener(
//            MouseEvent.MOUSE_DOWN, globe.confirm_board_7_7);
//    globe.root.game_over_mc._9_9_mc.enter_mc.addEventListener(
//            MouseEvent.MOUSE_DOWN, globe.board_9_9);
//    globe.root.game_over_mc._9_9_mc.confirm_mc.addEventListener(
//            MouseEvent.MOUSE_DOWN, globe.confirm_board_9_9);
//    globe.root.lobby_mc.main_mc._00_mc.addEventListener(
//            MouseEvent.MOUSE_DOWN, globe.grandparent_goto_mc_name);
//    globe.root.lobby_mc.main_mc._10_mc.addEventListener(
//            MouseEvent.MOUSE_DOWN, globe.grandparent_goto_mc_name);
//    //globe.root.lobby_mc.multiplayer_mc.main_mc.addEventListener(
//    //        MouseEvent.MOUSE_DOWN, globe.grandparent_goto_mc_name);
//    globe.root.lobby_mc.main_mc.login_mc.addEventListener(
//            MouseEvent.MOUSE_DOWN, globe.great_grandparent_goto_mc_name);
//    globe.root.lobby_mc._00_mc.main_mc.addEventListener(
//            MouseEvent.MOUSE_DOWN, globe.grandparent_goto_mc_name);
//    globe.root.lobby_mc._00_mc.capture_3_3_mc.addEventListener(
//            MouseEvent.MOUSE_DOWN, globe.problem_name);
//    globe.root.lobby_mc._00_mc.capture_5_5_mc.addEventListener(
//            MouseEvent.MOUSE_DOWN, globe.problem_name);
//    globe.root.lobby_mc._00_mc.dominate_3_3_mc.addEventListener(
//            MouseEvent.MOUSE_DOWN, globe.problem_name);
//    globe.root.lobby_mc._00_mc.dominate_5_5_mc.addEventListener(
//            MouseEvent.MOUSE_DOWN, globe.problem_name);
//    globe.root.lobby_mc._00_mc.score_5_5_mc.addEventListener(
//            MouseEvent.MOUSE_DOWN, globe.problem_name);
//    globe.root.lobby_mc._00_mc.extra_stone_7_7_mc.addEventListener(
//            MouseEvent.MOUSE_DOWN, globe.problem_name);
//    globe.root.lobby_mc._00_mc.extra_stone_7_7_2_mc.addEventListener(
//            MouseEvent.MOUSE_DOWN, globe.problem_name);
//    globe.root.lobby_mc._00_mc.extra_stone_9_9_mc.addEventListener(
//            MouseEvent.MOUSE_DOWN, globe.problem_name);
//    globe.root.lobby_mc._00_mc.hide_5_5_mc.addEventListener(
//            MouseEvent.MOUSE_DOWN, globe.problem_name);
//    globe.root.lobby_mc._00_mc.hide_7_7_mc.addEventListener(
//            MouseEvent.MOUSE_DOWN, globe.problem_name);
//    //- globe.root.lobby_mc.single_player_mc.addEventListener(
//    //-         MouseEvent.MOUSE_DOWN, globe.parent_goto_mc_name);
//    globe.root.lobby_mc._main_mc.addEventListener(
//            MouseEvent.MOUSE_DOWN, globe.parent_goto_mc_name);
//    globe.root.game_over_mc.white_computer_mc.enter_mc.addEventListener(
//            MouseEvent.MOUSE_DOWN, globe.white_computer);
//    globe.root.game_over_mc.extra_stone_available_mc._0_mc.addEventListener(
//            MouseEvent.MOUSE_DOWN, globe.author_parent_goto_mc_name);
//    globe.root.game_over_mc.extra_stone_available_mc._1_mc.addEventListener(
//            MouseEvent.MOUSE_DOWN, globe.author_parent_goto_mc_name);
//    globe.root.game_over_mc.extra_stone_available_mc._2_mc.addEventListener(
//            MouseEvent.MOUSE_DOWN, globe.author_parent_goto_mc_name);
//    globe.root.game_over_mc.extra_stone_available_mc._3_mc.addEventListener(
//            MouseEvent.MOUSE_DOWN, globe.author_parent_goto_mc_name);
//    globe.root.game_over_mc.extra_stone_available_mc._4_mc.addEventListener(
//            MouseEvent.MOUSE_DOWN, globe.author_parent_goto_mc_name);
//    globe.root.game_over_mc.extra_stone_available_mc._5_mc.addEventListener(
//            MouseEvent.MOUSE_DOWN, globe.author_parent_goto_mc_name);
//    globe.root.game_over_mc.extra_stone_available_mc._6_mc.addEventListener(
//            MouseEvent.MOUSE_DOWN, globe.author_parent_goto_mc_name);
//    globe.root.game_over_mc.extra_stone_available_mc._7_mc.addEventListener(
//            MouseEvent.MOUSE_DOWN, globe.author_parent_goto_mc_name);
//    globe.root.game_over_mc.extra_stone_available_mc._8_mc.addEventListener(
//            MouseEvent.MOUSE_DOWN, globe.author_parent_goto_mc_name);
//    globe.root.game_over_mc.extra_stone_available_mc._9_mc.addEventListener(
//            MouseEvent.MOUSE_DOWN, globe.author_parent_goto_mc_name);
//    globe.root.game_over_mc.hide_available_mc._0_mc.addEventListener(
//            MouseEvent.MOUSE_DOWN, globe.author_parent_goto_mc_name);
//    globe.root.game_over_mc.hide_available_mc._1_mc.addEventListener(
//            MouseEvent.MOUSE_DOWN, globe.author_parent_goto_mc_name);
//    globe.root.game_over_mc.hide_available_mc._2_mc.addEventListener(
//            MouseEvent.MOUSE_DOWN, globe.author_parent_goto_mc_name);
//    globe.root.game_over_mc.hide_available_mc._3_mc.addEventListener(
//            MouseEvent.MOUSE_DOWN, globe.author_parent_goto_mc_name);
//    globe.root.game_over_mc.hide_available_mc._4_mc.addEventListener(
//            MouseEvent.MOUSE_DOWN, globe.author_parent_goto_mc_name);
//    globe.root.game_over_mc.hide_available_mc._5_mc.addEventListener(
//            MouseEvent.MOUSE_DOWN, globe.author_parent_goto_mc_name);
//    globe.root.game_over_mc.hide_available_mc._6_mc.addEventListener(
//            MouseEvent.MOUSE_DOWN, globe.author_parent_goto_mc_name);
//    globe.root.game_over_mc.hide_available_mc._7_mc.addEventListener(
//            MouseEvent.MOUSE_DOWN, globe.author_parent_goto_mc_name);
//    globe.root.game_over_mc.hide_available_mc._8_mc.addEventListener(
//            MouseEvent.MOUSE_DOWN, globe.author_parent_goto_mc_name);
//    globe.root.game_over_mc.hide_available_mc._9_mc.addEventListener(
//            MouseEvent.MOUSE_DOWN, globe.author_parent_goto_mc_name);
//    globe.root.lobby_mc.enter_mc.addEventListener(
//            MouseEvent.MOUSE_DOWN, globe.enter_lobby);
//    globe.root.menu_mc.toggle_mc.addEventListener(
//            MouseEvent.MOUSE_DOWN, globe.toggle_menu);
//    globe.root.menu_mc.lobby_mc.addEventListener(
//            MouseEvent.MOUSE_DOWN, globe.remove_table);
//    globe.root.theme_txt.addEventListener(
//            TextEvent.TEXT_INPUT, set_theme_txt);
//	globe.root.cursor_mc.mouseEnabled = false;
//	globe.root.cursor_mc.mouseChildren = false;
//    //- globe.root.black_last_move_mc.mouseEnabled = false;
//    //- globe.root.black_last_move_mc.mouseChildren = false;
//    //- globe.root.white_last_move_mc.mouseEnabled = false;
//    //- globe.root.white_last_move_mc.mouseChildren = false;
//    globe.root.eat_mc.mouseEnabled = false;
//    globe.root.eat_mc.mouseChildren = false;
//	// globe.root.addEventListener(MouseEvent.MOUSE_MOVE, globe.follow);
//	globe.root.addEventListener(MouseEvent.MOUSE_DOWN, globe.mouse_shield);
//	// stage.addEventListener(MouseEvent.MOUSE_MOVE, follow);
//	// stage.addEventListener(MouseEvent.MOUSE_MOVE, follow);
//    board_listens_to_mouse(globe.intersection_mc_array);
//    setup_formations(globe);
//    globe.root.addEventListener(Event.ENTER_FRAME, globe.deliver_news);
//}
*/

function _finish_flash_setup() {
    // not supported in python client:
	//- Mouse.hide();
    set_theme(globe.intersection_mc_array, theme_txt.text);
    //debug mouse input:
	//?? globe.root.addEventListener(MouseEvent.MOUSE_DOWN, 
    //??    trace_objects_under_mouse);

    // HACK:  not in user_as.py
    globe.root.chat_input_txt.addEventListener(KeyboardEvent.KEY_DOWN,
        globe.on_press_enter_chat_input)
    // HACK:  measure frame rate during replay without seeing intersections.
    // set_board_visible(globe.intersection_mc_array, false);
    // remove_child_except(globe.root, keep_child_list);
}



function follow(mouse_event:MouseEvent){
	globe.root.cursor_mc.x = int(globe.root.mouseX);
	globe.root.cursor_mc.y = int(globe.root.mouseY);
	globe.root.mouse_shield_mc.x = int(globe.root.mouseX);
	globe.root.mouse_shield_mc.y = int(globe.root.mouseY);
    // mouse_event.updateAfterEvent();
}

function get_mouse_shield_news(root) {
    if ('shield' != root.mouse_shield_mc.currentLabel) {
        return {
            'mouse_down_mc': {
                    'currentLabel': 'shield', 
                    'x': root.mouseX, 
                    'y': root.mouseY },
            'mouse_shield_mc': {
                    'currentLabel': 'shield' }
            };
    }
    else {
        return {
            'mouse_down_mc': {
                    'currentLabel': 'shield'},
            'mouse_shield_mc': {
                    'currentLabel': 'shield'}
            }
    }
}


function mouse_shield(mouse_event:MouseEvent){
    var news = get_mouse_shield_news(globe.root);
    push_news(news);
    // imitate_news(globe.root, news);
    // double publish may collide with a network message.
}

function get_problem_news(problem_name) {
    var news = {
        'lobby_mc': {}
    };
    news['lobby_mc'][problem_name] = { 
                'enter_mc': {'currentLabel': 'enter'}
            };
    return news;
}

function get_children(parent_mc, exclude_name){
    /*
    >>> joris = globe_class()
    >>> joris.create()
    >>> joris.setup_events()
    >>> joris.ambassador = echo_protocol_class()
    >>> from pprint import pprint
    >>> unnamed_mc = MovieClip()
    >>> unnamed_mc.name = 'instance1443'
    >>> joris.root.lobby_mc._20_mc.addChild(unnamed_mc)
    >>> children = get_children(joris.root.lobby_mc._20_mc, 'main_mc')
    >>> if ! 5 <= children.length:  children
    >>> if unnamed_mc in children:  children
    >>> [c.name for (var c in children if c.name == 'main_mc'])
    []
    */
    var children = [];
    var child_count = parent_mc.numChildren;
    for (var c = 0; c < child_count; c++){
        var child_mc = parent_mc.getChildAt(c);
        if (isMovieClip(child_mc) && hasName(child_mc)){
            if (exclude_name != child_mc.name){
                children.push(child_mc);
            } // if
        } // if
    } // for
    return children;
} // function get_children



function children_listen_to_mouse(parent_mc, event, respond, exclude_name){
    /*All children except the excluded listen to mouse down.
    >>> joris = globe_class()
    >>> joris.create()
    >>> joris.setup_events()
    >>> joris.ambassador = echo_protocol_class()
    >>> from pprint import pprint
    >>> unnamed_mc = MovieClip()
    >>> unnamed_mc.name = 'instance1443'
    >>> joris.root.lobby_mc._20_mc.addChild(unnamed_mc)
    >>> children_listen_to_mouse(joris.root.lobby_mc._20_mc, 
    ...     MouseEvent.MOUSE_DOWN, joris.problem_name, 'main_mc')
    >>> old_log_level = trace()getLogger:.level
    >>> trace()getLogger:.setLevel(trace(mCRITICAL)
    >>> unnamed_mc.dispatchEvent:ouseDown)
    >>> trace()getLogger:.setLevel(old_log_level)
    >>> if joris.ambassador.sends{
    ...     joris.ambassador.sends[-1]['lobby_mc']

    Link all menu items in stage except back to main.
    >>> joris.root.lobby_mc._20_mc.hide_7_7_mc.dispatchEvent(mouseDown)
    >>> joris.root.lobby_mc._20_mc.extra_hide_7_7_mc.dispatchEvent(mouseDown)
    >>> single_player_news = joris.ambassador.sends[-1]
    >>> pprint(single_player_news['lobby_mc'])
    {'_20_mc': {'extra_hide_7_7_mc': {'currentLabel': 'enter',
                                      'dispatchEvent': 'mouseDown'}}}

    May also listen to mouseOver || mouseOut.
    >>> marije = joris
    >>> children_listen_to_mouse(marije.root.lobby_mc._00_mc, 
    ...     MouseEvent.MOUSE_OVER, marije.show_menu_info, 'main_mc')
    >>> target = marije.root.lobby_mc._00_mc.capture_3_3_mc
    >>> target.info_txt.text = 'Surround a fire.'
    >>> marije.root.info_mc.currentLabel
    'none'
    >>> target.dispatchEvent(mouseOver)
    >>> marije.root.info_mc.currentLabel
    'show'
    >>> children_listen_to_mouse(marije.root.lobby_mc._00_mc, 
    ...     MouseEvent.MOUSE_OUT, marije.hide_menu_info, 'main_mc')
    >>> marije.root.info_mc.currentLabel
    'show'
    >>> target.dispatchEvent(mouseOut)
    >>> marije.root.info_mc.currentLabel
    'none'
    */
    var children = get_children(parent_mc, exclude_name);
    for (var c = 0; c < children.length; c++){
        var child_mc = children[c];
        child_mc.addEventListener(event, respond);
    } // for
} // function children_listen_to_mouse






function revise(news) {
    //+ var olds = imitate_news(globe.root, news, globe.log_news);
    var olds = imitate_news(globe.root, news, null);
    globe.olds_list.push(olds);
}

function echo_once_or_imitate(news) {
    if (undefined != news['gateway_mc']) {
        if (undefined != news['gateway_mc']['ready_time_txt']) {
            if ('log' == news['gateway_mc']['ready_time_txt']['text']) {
                delete news['gateway_mc'];
                //+ log_news('log', news);
                return;
            }
            else if ('echo_once' == news['gateway_mc']['ready_time_txt']['text']) {
                delete news['gateway_mc'];
                //+ log_news('echo_once', news);
                globe.ambassador.send(news);
                return;
            }
        }
    }
    globe.imitate(news);
}

function imitate(news){
    // globe.log_news('imitate', news);
    globe.revise(news);
    var is_alive = globe.is_alive();
    trace('debug:globe.is_alive ' + is_alive.toString());
    trace('debug:globe.ambassador.is_alive ' + globe.ambassador.is_alive.toString());
    globe.ambassador.is_alive = globe.is_alive();
    if (is_alive){
        if ('entering' == globe.root['save_mc'].currentLabel){
            globe.save_list = globe.save_one_child(globe.root, globe.save_list);
        } else if ('entering' == globe.root['load_mc'].currentLabel){
            // XXX Gotcha ActionScript requires 'new MouseEvent' 
            // but does ! bark while compiling
            var mouse_event = new MouseEvent(MouseEvent.MOUSE_DOWN);
            globe.load_stage(mouse_event);
        } // if
    } // if
} // function imitate



function log_news(cite, news){
    /*In reverse order, push keys in news && their labels to text field.
    >>> //// gateway_process = subprocess_gateway(amf_host, 'embassy.py', verbose)
    >>> laurens = globe_class()
    >>> laurens.create()
    >>> //// laurens.setup(mock_speed, setup_client)
    >>> laurens.setup_events() // clear the log.  XXX redudant with setup?
    >>> laurens.ambassador = print_protocol_class()
    >>> laurens.root.title_mc.username_txt.text = 'laurens'
    >>> laurens.imitate({'_1_0_mc': {'currentLabel': 'black'}, '_0_0_mc': {'currentLabel': 'black'}})
    >>> print laurens.root.log_txt.text
    imitate_news: laurens: _0_0_mc:black _1_0_mc:black
    log
    */
    var keywords = get_keywords(news);
    var my_keywords = globe.root.title_mc.username_txt.text + ':' + keywords;
    globe.update_log(cite + ': ' + my_keywords);
} // function log_news


function push_news(news){
    /*Route news to reading list || sequence || info.
    >>> import config
    >>> defaults = config.setup_defaults()
    >>> configuration = config.borg(defaults)
    >>> configuration.instant = False
    >>> moonhyoung = globe_class()
    >>> moonhyoung.create()
    >>> moonhyoung.ambassador = print_protocol_class()
    >>> moonhyoung.news_list
    []
    >>> moonhyoung.sequence_list
    []

    Enable sequence.
    >>> //// configuration.instant = False
    >>> moonhyoung.instant
    False

    Ignore empty sequence.
    >>> news = {'sequence': []}
    >>> moonhyoung.push_news(news)
    
    sequence a timed event.
    >>> event = note(moonhyoung.root._3_3_mc, 'currentLabel', 'question_black')
    >>> timed_event = upgrade(event, {'time_txt': {'text': '256000'}})
    >>> sequence = [timed_event]
    >>> news = {'sequence': sequence}
    >>> moonhyoung.push_news(news)
    >>> now = getTimer()
    >>> if ! now < 256000:  now
    >>> moonhyoung.news_list
    []
    >>> moonhyoung.sequence_list.length
    1
    >>> moonhyoung.sequence_list[0][0]['time_txt']['text']
    '256000'
    >>> moonhyoung.sequence_list[0][0]['_3_3_mc']['currentLabel']
    'question_black'
    >>> moonhyoung.root.gotoAndPlay('table')
    >>> moonhyoung.push_news({'currentLabel': 'lobby'})

    Upon push, available news === NOT imitated.
    >>> rene = moonhyoung
    >>> rene.news_list
    [{'currentLabel': 'lobby'}]
    >>> rene.root.currentLabel
    'table'
    >>> rene.sequence_list.length
    1

    Upon receiving first event with sequence key, 
    client flushes the preceding sequence.
    When I revert the client, I also clear the old sequence.
    >>> from pprint import pprint
    >>> pprint(moonhyoung.sequence_list)
    [[{'_3_3_mc': {'currentLabel': 'question_black'},
       'time_txt': {'text': '256000'}}]]
    >>> moonhyoung.root._3_3_mc.currentLabel
    'empty_black'
    >>> news = {'sequence': [{'sequence': []}, 
    ...     {'currentLabel': 'table', 'time_txt': {'text': '256000'}}]}
    >>> moonhyoung.push_news(news)
    >>> pprint(moonhyoung.sequence_list)
    [[{'_3_3_mc': {'currentLabel': 'question_black'},
       'time_txt': {'text': '256000'}}],
     [{'sequence': []}, {'currentLabel': 'table', 'time_txt': {'text': '256000'}}]]
    >>> moonhyoung.root._3_3_mc.currentLabel
    'empty_black'
    >>> moonhyoung.update(None)
    >>> getTimer() < 256000
    True
    >>> pprint(moonhyoung.sequence_list)
    [[{'currentLabel': 'table', 'time_txt': {'text': '256000'}}]]
    >>> moonhyoung.root._3_3_mc.currentLabel
    'question_black'

    Optionally imitate now.
    >>> configuration.instant = True
    >>> moonhyoung = globe_class()
    >>> moonhyoung.create()
    >>> moonhyoung.ambassador = print_protocol_class()
    >>> event = note(moonhyoung.root._3_3_mc, 'currentLabel', 'question_black')
    >>> timed_event = upgrade(event, {'time_txt': {'text': '256000'}})
    >>> sequence = [timed_event]
    >>> news = {'sequence': sequence}
    >>> moonhyoung.push_news(news)
    >>> now = getTimer()
    >>> if ! now < 256000:  now
    >>> moonhyoung.news_list
    []
    >>> moonhyoung.sequence_list
    [[{'_3_3_mc': {'currentLabel': 'question_black'}, 'time_txt': {'text': '256000'}}]]
    >>> moonhyoung.root._3_3_mc.currentLabel
    'empty_black'
    >>> moonhyoung.update(None)
    >>> moonhyoung.sequence_list
    []
    >>> moonhyoung.root._3_3_mc.currentLabel
    'question_black'

    >>> configuration.instant = True
    >>> laurens = globe_class()
    >>> laurens.create()
    >>> laurens.ambassador = print_protocol_class()
    >>> news = get_laurens_question_black_sequenced_news()
    >>> laurens.push_news(news)
    >>> laurens.root._2_2_mc.currentLabel
    'empty_black'
    >>> laurens.update(None)
    >>> laurens.root._2_2_mc.currentLabel
    'question_black'

    >>> code_unit.doctest_unit(globe_class.show_info_sequence, log = False)

    Clear info.
    >>> moonhyoung.info = {'_2_2_mc': []}
    >>> moonhyoung.push_news({'info': {'delete': true}})
    >>> moonhyoung.info
    {}
    */
    // globe.log_news('push_news', news);
    if (news is Object){
        var old = false;
        if (undefined != news['sequence']){
            var sequence = news['sequence'];
            if (1 <= sequence.length){
                globe.sequence_list.push(sequence);
                old = true;
            } // if
            delete news['sequence'];
        } // if
        if (1 <= count_item(news)){
            globe.news_list.push(news);
            old = true;
        } // if
        if (undefined != news['info']){
            var breakpoint = true;
        } // if
        // ActionScript gotcha:  never {'info': {}} != news['info']
        if (undefined != news['info']){
            if (true == news['info']['delete']){
                globe.info = {};
            } else{
                globe.info = upgrade(globe.info, news['info']);
            } // if
        } // if
    } else{
        trace('push_news: what === this? ' + news);
    } // if
} // function push_news


function deliver_news(event){
    /*Imitate first news in list.  
    TODO:  Synchronize this ActionScript && Python method.
    >>> ethan = globe_class()
    >>> ethan.create()
    >>> ethan.root.addEventListener(Event.ENTER_FRAME, ethan.deliver_news)
    >>> ethan.ambassador = print_protocol_class()
    >>> news = {'currentLabel': 'table'}
    >>> ethan.news_list.push(news)
    >>> ethan.root.dispatchEvent(enterFrame)
    >>> ethan.root.currentLabel
    'table'
    >>> ethan.news_list
    []
    >>> news = {'currentLabel': 'lobby'}
    >>> news2 = {'gateway_mc': {'currentLabel': 'enter'}}
    >>> ethan.news_list.push(news)
    >>> ethan.news_list.push(news2)
    >>> ethan.root.dispatchEvent(enterFrame)
    >>> ethan.root.currentLabel
    'lobby'
    >>> ethan.root.gateway_mc.currentLabel
    'enter'
    >>> ethan.news_list
    []
    */
    var news = {};
    while (globe && globe.news_list && 1 <= globe.news_list.length 
            && globe.ambassador){
        news = globe.news_list.shift();
        globe.imitate(news);
    } // while
} // function deliver_news

function follow_sequences(event){
    return globe._follow_sequences(globe.instant);
} // function follow_sequences

function _follow_sequences(instant){
    /*If time for (var news in sequence, imitate then discard the news.
    Time === client age in milliseconds, as in getTimer.
    >>> import config
    >>> defaults = config.setup_defaults()
    >>> configuration = config.borg(defaults)
    >>> configuration.instant = False
    
    >>> moonhyoung = globe_class()
    >>> moonhyoung.create()
    >>> moonhyoung.root.addEventListener(Event.ENTER_FRAME, moonhyoung.follow_sequences)
    >>> moonhyoung.ambassador = print_protocol_class()
    >>> now = getTimer()
    >>> event = ){}
    >>> event = note(moonhyoung.root._3_3_mc, 'currentLabel', 'question_black')
    >>> timed_event = upgrade(event, {'time_txt': {'text': now + 250.toString()}})
    >>> sequence = [timed_event]

    Do ! upgrade news, as that would recursively reference the sequence.
    >>> //// news = upgrade(event, {'sequence': sequence})
    >>> moonhyoung.sequence_list.push(sequence)
    >>> moonhyoung.root.dispatchEvent(enterFrame)
    >>> moonhyoung.root._3_3_mc.currentLabel
    'empty_black'
    >>> moonhyoung.sequence_list.length
    1
    >>> time.sleep(0.25)
    >>> moonhyoung.root.dispatchEvent(enterFrame)
    >>> moonhyoung.root._3_3_mc.currentLabel
    'question_black'
    >>> moonhyoung.sequence_list.length
    0

    If no timestamp, then consume immediately.
    >>> news = {}
    >>> news = upgrade(news, note(moonhyoung.root._3_3_mc, 'currentLabel', 'black') )
    >>> sequence = [news]
    >>> moonhyoung.sequence_list.push(sequence)
    >>> moonhyoung.root.dispatchEvent(enterFrame)
    >>> moonhyoung.root._3_3_mc.currentLabel
    'black'
    >>> moonhyoung.sequence_list.length
    0
    
    If 0 || any timestamp before age in client, then consume immediately.
    >>> news = {}
    >>> news = upgrade(news, note(moonhyoung.root._3_3_mc, 'currentLabel', 'black') )
    >>> news = upgrade(news, {'time_txt': {'text': 0.toString()}})
    >>> sequence = [news]
    >>> moonhyoung.sequence_list.push(sequence)
    >>> moonhyoung.root.dispatchEvent(enterFrame)
    >>> moonhyoung.root._3_3_mc.currentLabel
    'black'
    >>> moonhyoung.sequence_list.length
    0

    If multiple sequenced events are overdue, consume each overdue.
    >>> moonhyoung.root._3_3_mc.gotoAndPlay('none')
    >>> moonhyoung.root._3_2_mc.decoration_mc.gotoAndPlay('none')
    >>> moonhyoung.root._3_1_mc.decoration_mc.gotoAndPlay('none')
    >>> news = {}
    >>> news = upgrade(news, note(moonhyoung.root._3_3_mc, 'currentLabel', 'black') )
    >>> news = upgrade(news, {'time_txt': {'text': 0.toString()}})
    >>> news2 = note(moonhyoung.root._3_2_mc.decoration_mc, 'currentLabel', 'black_attack')
    >>> news2 = upgrade(news2, {'time_txt': {'text': 1.toString()}})
    >>> news3 = note(moonhyoung.root._3_1_mc.decoration_mc, 'currentLabel', 'black_attack')
    >>> news3 = upgrade(news3, {'time_txt': {'text': 900000.toString()}})
    >>> sequence = [news, news2, news3]
    >>> moonhyoung.sequence_list.push(sequence)
    >>> moonhyoung.root.dispatchEvent(enterFrame)
    >>> moonhyoung.root._3_3_mc.currentLabel
    'black'
    >>> moonhyoung.root._3_2_mc.decoration_mc.currentLabel
    'black_attack'
    >>> moonhyoung.root._3_1_mc.decoration_mc.currentLabel
    'none'
    >>> moonhyoung.sequence_list.length
    1

    Optionally, immediately imitate sequenced events.
    >>> configuration.instant = True
    >>> moonhyoung = globe_class()
    >>> moonhyoung.create()
    >>> moonhyoung.ambassador = print_protocol_class()
    >>> moonhyoung.news_list = []
    >>> moonhyoung.sequence_list = []
    >>> event = note(moonhyoung.root._3_3_mc, 'currentLabel', 'question_black')
    >>> timed_event = upgrade(event, {'time_txt': {'text': '1000'}})
    >>> sequence = [timed_event]
    >>> moonhyoung.sequence_list.push(sequence)
    >>> moonhyoung.follow_sequences(enterFrame)
    >>> moonhyoung.news_list
    []
    >>> moonhyoung.sequence_list
    []
    >>> moonhyoung.root._3_3_mc.currentLabel
    'question_black'

    >>> code_unit.doctest_unit(globe_class.push_news, log = False)
    */
    if (1 <= globe.sequence_list.length){
        var previous = globe.sequence_list[0];
        var sequence = globe.sequence_list[0];
        var time = 0;
        var time_txt = '0';
        var news = {};
        // ActionScript gotcha:  for..in does ! guarantee access in same order.
        // for..in && for each..in
        // http://www.kirupa.com/forum/showpost.php?s=7ec39a65b4a290ca1d6c8b7cd43cf0a1&p=1923917&postcount=137
        for (var s = 0; s < globe.sequence_list.length; s++){
            sequence = globe.sequence_list[s];
            time = 0;
            while (1 <= sequence.length && (instant 
                    || time <= getTimer()) ){
                if (sequence[0]['sequence'] is Array){
                    sequence.shift();
                    for (var pre = 0; pre < s; pre++){
                        previous = globe.sequence_list[pre];
                        while (1 <= previous.length){
                            news = previous.shift();
                            globe.imitate(news);
                        } // while
                    } // for
                } // if
                time_txt = sequence[0]['time_txt'];
                if (null != time_txt){
                    time = int(time_txt['text']);
                } // if
                if (instant || time <= getTimer()){
                    news = sequence.shift();
                    globe.imitate(news);
                } // if
            } // while
        } // for
        var new_sequence_list = [];
        for (var n = 0; n < globe.sequence_list.length; n++){
        } // for
    } // if
} // function _follow_sequences

function update(event){
    /*deliver news && follow sequences.  update info sequence.
    >>> moonhyoung = globe_class()
    >>> moonhyoung.create()
    >>> moonhyoung.update(null)
    */
    globe.deliver_news(event);
    globe.follow_sequences(event);
    globe._get_info_sequence(globe.info_sequence);
} // function update
    

function is_alive(){
    if (globe && globe.root){
        if ('exit' == globe.root.gateway_mc.currentLabel){
            trace('info:exit == root.gateway_mc.currentLabel');
            return false;
        } // if
    } else{
        return false;
    } // if
    return true;
} // function is_alive



    
// end port from client.py 


import amf_socket_class;

// Start your engine!

// Board

// === get_intersection_array
var intersection_mc_array:Array = new Array(
		[_0_0_mc, _0_1_mc, _0_2_mc, _0_3_mc, _0_4_mc, _0_5_mc, _0_6_mc, _0_7_mc, _0_8_mc],
		[_1_0_mc, _1_1_mc, _1_2_mc, _1_3_mc, _1_4_mc, _1_5_mc, _1_6_mc, _1_7_mc, _1_8_mc],
		[_2_0_mc, _2_1_mc, _2_2_mc, _2_3_mc, _2_4_mc, _2_5_mc, _2_6_mc, _2_7_mc, _2_8_mc],
		[_3_0_mc, _3_1_mc, _3_2_mc, _3_3_mc, _3_4_mc, _3_5_mc, _3_6_mc, _3_7_mc, _3_8_mc],
		[_4_0_mc, _4_1_mc, _4_2_mc, _4_3_mc, _4_4_mc, _4_5_mc, _4_6_mc, _4_7_mc, _4_8_mc],
		[_5_0_mc, _5_1_mc, _5_2_mc, _5_3_mc, _5_4_mc, _5_5_mc, _5_6_mc, _5_7_mc, _5_8_mc],
		[_6_0_mc, _6_1_mc, _6_2_mc, _6_3_mc, _6_4_mc, _6_5_mc, _6_6_mc, _6_7_mc, _6_8_mc],
		[_7_0_mc, _7_1_mc, _7_2_mc, _7_3_mc, _7_4_mc, _7_5_mc, _7_6_mc, _7_7_mc, _7_8_mc],
		[_8_0_mc, _8_1_mc, _8_2_mc, _8_3_mc, _8_4_mc, _8_5_mc, _8_6_mc, _8_7_mc, _8_8_mc]
        );

function get_intersection_name(row, column) {
    var name = '_' + row.toString() + '_' + column.toString() + '_mc';
    return name;
}

function get_intersection_array(root, length = 9) {
    var intersections = [];
    var name;
    for (var row = 0; row < length; row ++) {
        intersections.push( [] );
        for (var column = 0; column < length; column ++) {
            name = get_intersection_name(row, column);
            if (root.getChildByName(name)) {
                intersections[intersections.length - 1].push(root[name]);
            }
        }
    }
    return intersections;
}

this.credentials = this.root['title_mc'];
this.save_list = new Array();
this.info = {};
this.info_olds = {};
this.info_sequence = {};
// var theme_name:String = "cake_take";
// var theme_name:String = "traditional";

globe.setup_events();


// Network

function on_timeout() {
    globe.root.gateway_mc.gotoAndPlay("timeout");
}

function update_log(message) {
//     prof.begin("update_log");
    globe.root.log_txt.text = message + '\n' + globe.root.log_txt.text;  // performance:  
    var a:Boolean = false;
//     prof.end("update_log");
}

//- function close_gateway_message(mouse_event:MouseEvent) {
//-     globe.root.gateway_mc.gotoAndPlay("none");
//- }

//- gateway_mc.none_mc.addEventListener(MouseEvent.MOUSE_DOWN, 
//-         close_gateway_message);

function parent_goto_none(mouse_event) {
    var display_object = mouse_event.currentTarget;
    if (undefined != display_object.parent) {
        var news = note(display_object.parent, 'currentLabel', 'none');
        globe.publish(news);
    }
}

include "configuration.as";


var original_stage = {};
var news_list:Array = new Array();
var sequence_list:Array = new Array();
var olds_list:Array = new Array();
var instant = false;





var ambassador = new amf_socket_class(
        globe.gateway_mc.host_txt.text, int(globe.gateway_mc.port_txt.text), 
        this.push_news, this.on_timeout,
//        this.amf_host, this.amf_port, this.push_news, this.on_timeout,
        this.update_log, this.prof);

// HACK: reconnect button to test same client local and internet.
globe.gateway_mc.connect_mc.addEventListener(MouseEvent.MOUSE_DOWN, globe.reconnect);
function reconnect(mouse_event) {
    if (globe.ambassador.connected) {
        globe.ambassador.close(); }
    globe.ambassador.connect(
        globe.gateway_mc.host_txt.text, 
        int(globe.gateway_mc.port_txt.text) );
}

// echo test.  see client.echo
//var ambassador = new amf_socket_class(
//        this.host, this.amf_port, this.echo_once_or_imitate, this.on_timeout,
//        this.update_log);

// functions not python:

import flash.display.Sprite;
import flash.geom.Point;
import flash.ui.Keyboard;




function trace_objects_under_mouse(mouse_event:MouseEvent){
    var x = globe.root.mouseX;
    var y = globe.root.mouseY;
    var mouse_pt:Point = new Point(x, y);
    var objects:Array = globe.root.getObjectsUnderPoint(mouse_pt); 
    trace('under mouse ('+ x + ', ' + y +') are '+ objects.length +' objects:'); 
    for (var o = 0; o < objects.length; o ++) {
        var object = objects[o];
        var log = '';
        var ancestry = object.name;
        if (object is DisplayObject) {
            var younger = object;
            var elder = younger.parent;
            var indent = '';
            var lineage:Array = new Array([]);
            while (younger.parent) {
                younger = elder;
                elder = younger.parent;
                lineage.push(younger);
            }
            var properties = '';            
            for (y = lineage.length - 1; 0 <= y; y --) {
                younger = lineage[y];
                ancestry = younger.name + '.';
                properties += '\n' + indent + ancestry;
                if (younger is InteractiveObject) {
                    properties += '  mouseEnabled = ' + younger.mouseEnabled.toString();
                    // properties += '\n' + indent + '    visible = ' + younger.visible.toString();
                    // properties += '\n' + indent + '    alpha = ' + younger.alpha.toString();
                }
                if (younger is DisplayObjectContainer) {
                    properties += '  mouseChildren=' + younger.mouseChildren.toString();
                }
                if (younger is DisplayObject) {
                    if (y < lineage.length - 2 && y <= 1){
                        elder = lineage[y+1];
                        if (elder is DisplayObjectContainer) {
                            properties += '  index=' 
                                + elder.getChildIndex(younger).toString();
                        }
                    }
                }
                indent += '    ';
            }
            log += properties;
        }
        trace(log);
    }
}



// add_help, remove_help, help_about_me:  
// Lookup help by movieClip label.
function help_about_me(mouse_event:MouseEvent){
    trace("help_about_me:  " + mouse_event.target.name 
        + ":" + mouse_event.target.currentLabel);
    var topic = mouse_event.target.currentLabel;
    gotoAndPlayLabel(help_mc, topic);
}

// after frame 1
// (root as MovieClip).add_help(this);
function add_help(me) {
	me.addEventListener(MouseEvent.MOUSE_OVER, help_about_me)
    // if child then target may be nested.
	me.mouseChildren = false;
	me.mouseEnabled = true;
}


// after frame 1
// (root as MovieClip).remove_help(this);
function remove_help(me) {
	me.removeEventListener(MouseEvent.MOUSE_OVER, help_about_me)
	me.mouseChildren = false;
	me.mouseEnabled = false;
}




// TODO Which of the following code do I need?

// www.flashdev.ca/article/trace-objects
function object_to_string(an_object):String {
    var object_string = an_object.classname;
       // + " " 
       // + (an_object.super.classname 
       //         ? an_object.super.classname : "object");
    for (var property in an_object){
        object_string += property + ": " + an_object[property] + ", ";
    }
    return object_string;
}


// Label

/*
example:
frame 1: setup
frame 2: reset
frame 3: user_select_version
frame 5: play
frame 15: move_tutorial
frame 115: lose_tutorial
frame 215: start_play
frame 244: select_version
frame 245: you_win
frame 256: you_lose
*/
function trace_labels(a_mc){
    var labels:Array = a_mc.currentLabels;    
    for (var i:uint = 0; i < labels.length; i++) {
        var label:FrameLabel = labels[i];
        trace("frame " + label.frame + ": " + label.name);
    }
}


// Flash silently ignores missing labels.  So this brings attention.
function has_label(a_mc, name):Boolean{
    var labels:Array = a_mc.currentLabels;
    for (var i:uint = 0; i < labels.length; i++) {
        if (name == labels[i].name) {
            return true;
        }
    }
    return false;
}

// If not already there, goto and play a label.
function gotoAndPlayLabel(a_mc /*:MovieClip, :DisplayObjectContainer*/,
        label:String){
    if (label != a_mc.currentLabel) {
        if (! has_label(a_mc, label)){
            var name = a_mc.name;
            if (undefined != a_mc.parent) {
                name = a_mc.parent.name + "." + name;
            }
            trace("gotoAndPlayLabel:  label not found " 
                + name + ":" + label 
                + " in " + a_mc.currentLabels);
        }
        //if (a_mc.constructor != MovieClip) {
        //    trace("gotoAndPlayLabel:  This is not a MovieClip:  " + a_mc.name + ".  It is " + a_mc.constructor + " label " + label);
        //}
        a_mc.gotoAndPlay(label);
    }
}

function create_null_functor():Function{
    var do_nothing:Function = function():void {
        var a = 0;
    }
    return do_nothing;
}

// function create_gotoAndPlayLabel_functor(a_mc, label_str) {
function create_goto_functor(a_mc, label_str):Function {
    var do_gotoAndPlayLabel:Function = function():void {
        gotoAndPlayLabel(a_mc, label_str);
    }
    return do_gotoAndPlayLabel;
}



function gotoAndPlayFrom(a_mc, old_label, new_label) {
    if (old_label == a_mc.currentLabel) {
        gotoAndPlayLabel(a_mc, new_label);
    }
}


function gotoAndPlay_if_not(a_mc, not_label, new_label) {
    if (not_label != a_mc.currentLabel) {
        gotoAndPlayLabel(a_mc, new_label);
    }
} 

function do_all(do_this, mc_array){
	for (var row:uint = 0; row < mc_array.length; row++) {
		for (var column:uint = 0; column < mc_array[row].length; column++) {
            do_this(mc_array[row][column]);
        }
    }
}

function do_all_this_way(do_this, mc_array, this_way){
	for (var row:uint = 0; row < mc_array.length; row++) {
		for (var column:uint = 0; column < mc_array[row].length; column++) {
            do_this(mc_array[row][column], this_way);
        }
    }
}

function do_all_these_ways(do_this, mc_array,
        this_way, and_this_way){
	for (var row:uint = 0; row < mc_array.length; row++) {
		for (var column:uint = 0; column < mc_array[row].length; column++) {
            do_this(mc_array[row][column], this_way, and_this_way);
        }
    }
}

// lookup in dictionary

function respond_all(action, grid, 
        news, trigger_key){
    if (undefined != news[trigger_key]) {
        return do_all(action, grid);
    }
}
function respond_at(action, grid, news, trigger_key){
    if (undefined != news[trigger_key]) {
        return do_at(action,
            grid, news[trigger_key]);
    }
}
function respond_at_this_way(action, grid, 
        news, trigger_key, this_way){
    if (undefined != news[trigger_key]) {
        return do_at_this_way(action, grid,
            news[trigger_key], this_way);
    }
}
function respond(action, news, trigger_key){
    if (undefined != news[trigger_key]) {
        return action(news[trigger_key]);
    }
}


/*
for each in 2D array:  if old, then goto new

for btn in intersection_btn_array:
	if old:
		gotoAndPlay new
*/
function gotoAndPlay_if(old_label, new_label, mc_array:Array){
	for (var row:uint = 0; row < mc_array.length; row++) {
		for (var column:uint = 0; column < mc_array[row].length; column++) {
            gotoAndPlayFrom(mc_array[row][column], old_label, new_label);
		}
	}
}

function goto_nextFrame(this_event:Event){
	nextFrame();
}

function count_label(a_label, mc_array:Array):int{
	var count:int = 0;
	for (var row:uint = 0; row < mc_array.length; row++) {
		for (var column:uint = 0; column < mc_array[row].length; column++) {
			if (a_label == mc_array[row][column].currentLabel) {
				count += 1;
			}
		}
	}
	return count;
}

// set particular text if in news.
function set_this_text(parent_mc, name, news) {
        if (undefined != news[name] && null != news[name]) {
            var a_txt = parent_mc.getChildByName(name);
            if (null != a_txt) {
                a_txt.text = news[name];
            }
            else {
                trace("set_this_text:  txt not found for " + name);
            }
        }
}

// set dynamic text in a movieClip.
function set_text(parent_mc, news) {
    for (var name in news) {
        set_this_text(parent_mc, name, news);
    }
}

// Functions over 2D array
/*
def do_at(grid, positions, do_this):
    '''
    >>> def p(i):  return i
    >>> do_at(clear_board, [(0, 0)], p)
    ['.']
    '''
    return [do_this(grid[row][column]) 
        for row, column in positions]
*/

function do_at(do_this, grid, positions){
    var filtered:Array = [];
    for (var p:uint = 0; p < positions.length; p ++ ){
        var row:uint = positions[p][0];
        var column:uint = positions[p][1];
        filtered.push( do_this(grid[row][column]) );
    }
    return filtered;
}

function do_at_this_way(do_this, grid, positions, this_way){
    var filtered:Array = [];
    for (var p = 0; p < positions.length; p ++ ){
        var row:uint = positions[p][0];
        var column:uint = positions[p][1];
        filtered.push( do_this(grid[row][column], this_way) );
    }
    return filtered;
}


/*
def do_at_these_ways(do_this, grid, positions, *these_ways):
    '''
    >>> def p(i, n, m):  return i * n * m
    >>> do_at_these_ways(p, clear_board, [(0, 0)], 3, 2)
    ['......']
    '''
    return [do_this(grid[row][column], *these_ways)
        for row, column in positions]
*/
function do_at_these_ways(
        do_this, grid, positions, this_way, and_this_way){
    var filtered:Array = [];
    for (var p = 0; p < positions.length; p ++ ){
        var row:uint = positions[p][0];
        var column:uint = positions[p][1];
        filtered.push( do_this(grid[row][column], 
                this_way, and_this_way) );
    }
    return filtered;
}

// Global Point

// Transform position of nested movie clip to global coordinate space.
function get_global_point(parent_mc, // :MovieClip or :Stage
        nested_mc:MovieClip) {
    var local_point:flash.geom.Point = new flash.geom.Point(
        nested_mc.x, nested_mc.y);
    var global_point = parent_mc.localToGlobal(local_point);
    return global_point;
}

// Did the splash movie clip hit the position of nested movie clip?
function hitTestPoint_nested(
        splash_mc:MovieClip, 
        parent_mc, // :MovieClip, :DisplayObjectContainer, or :Stage
        nested_mc:MovieClip, shapeFlag:Boolean): Boolean{
    var target_point = get_global_point(parent_mc, nested_mc);
    var hit:Boolean = splash_mc.hitTestPoint(
            target_point.x, target_point.y, shapeFlag);
    return hit;
}

// Snap source_mc to global position of target_mc.
// Return source_mc to be clear that the variable is modified.
// TODO:  global rotation, scale
function snap(source_mc:MovieClip, target_mc /*:MovieClip, DisplayObjectContainer*/):MovieClip {
    var target:flash.geom.Point = get_global_point(
            target_mc.parent, target_mc);
    source_mc.x = target.x;
    source_mc.y = target.y;
    // TODO:  global rotation, scale
    source_mc.rotation = target_mc.rotation;
    source_mc.scaleX = target_mc.scaleX;
    source_mc.scaleY = target_mc.scaleY;
    return source_mc;
}



// Simple MovieClip database

/*
var mc_dictionary = {
        //- "extra_stone_gift":  extra_stone_gift_mc,
        //'formation_jump':  formation_jump_mc.rotate_0_mc.respnse_mc,
        // 'formation_jump_response':  formation_jump_mc.rotate_270_mc.response_mc,  // XXX Does not validate other formation examples.
	    "game_over":  game_over_mc,
	    "gateway":  gateway_mc,
	    // "glass":  glass_mc,
        "help":  help_mc,
        "hide_gift":  hide_gift_mc,
        "pass_white_mc":  pass_white_mc,
        // "undo_gift":  undo_gift_mc,
        "root":  this.root
        // XXX each intersection is different.
        // "territory":  intersection_0_0_mc.territory_mc // "dead", "black", "white", "neutral"
    }
*/

/*-
var formation_dictionary = {
        'formation_diagonal':  formation_diagonal_mc,
        'formation_diagonal_attack':  formation_diagonal_attack_mc,
        'formation_field':  formation_field_mc,
        'formation_jump':  formation_jump_mc,
        'formation_jump_attack':  formation_jump_attack_mc,
        'formation_knight':  formation_knight_mc,
        'formation_knight_attack':  formation_knight_attack_mc,
        'formation_leap':  formation_leap_mc,
        'formation_leap_attack':  formation_leap_attack_mc
}
-*/

// Play the rotated formation's response
/*
%>_<	place field pattern, then another one second later.  does not restart the animation.  
	^_^	each time a pattern is matched, restart that pattern's animation.
*/
/*-
function follow_formation_news(news:Object) {
    for (var name in formation_dictionary) {
        if (news[name] != undefined) {
            var row_column_rotates = news[name];
            var formation_mc = formation_dictionary[name];
            for (var i = 0; i< row_column_rotates.length; i ++) {
                var row_column_rotate = row_column_rotates[i];
                var row = row_column_rotate.shift();
                var column = row_column_rotate.shift();
                snap(formation_mc, intersection_mc_array
                        [row][column]);
                var rotate = row_column_rotate.shift();
                var rotated_formation_mc = 
                    formation_mc.getChildByName(rotate);
                rotated_formation_mc.response_mc.gotoAndPlay(
                    "response");
                //gotoAndPlayLabel(
                //    rotated_formation_mc.response_mc,
                //    "response");
                // XXX too much on screen?  when animation done remove from stage?  make invisible?
            }
        }
    }
}

function follow_news(news:Object, about:String) {
    if (news[about] != undefined) {
        if ("game_over" == about) {
            trace("follow_news( news, " + about + ");"); 
        }
	    gotoAndPlayLabel( mc_dictionary[about], 
            news[about] );
    }
}

function follow_this_news(news:Object, mc_dictionary:Object) {
    for (var about in mc_dictionary) {
        follow_news(news, about);
    }
}
-*/

// >>> get_labels(mc_dictionary);
// {"game_over":  ["none", "win"]}
function get_labels(mc_dictionary){
    var label_dictionary = {};
    for (var title in mc_dictionary) {
        var names:Array = new Array();
        var labels:Array = mc_dictionary[title].currentLabels;
        for (var index = 0; index < labels.length; index++) {
            names.push(labels[index].name);
        }
        label_dictionary[title] = names;
    }
    return label_dictionary;
}

// function test_get_labels()
//t.obj(  get_labels(mc_dictionary),  
//        "get_labels(mc_dictionary)");
// {"game_over":  ["none", "win"]}


// or, more simply:  this.visible = false;
function set_trigger_visible(parent_mc, is_visible){ 
    for (var kid:uint = 0; kid < parent_mc.numChildren; kid++) {
        var child_mc = parent_mc.getChildAt(kid).trigger_mc;
        child_mc.visible = is_visible;
    }
}

/*-
var formation_array:Array = new Array(
    formation_knight_mc,
    formation_knight_attack_mc,
    formation_jump_mc,
    formation_jump_attack_mc,
    formation_diagonal_mc,
    formation_diagonal_attack_mc
    );
-*/



var previous_stone_count:int = 0;
var stone_count:int = 0;
var white_stone_count:int = 0;
var black_stone_count:int = 0;
var previous_white_stone_count:int = 0;
var previous_black_stone_count:int = 0;

var focus_array:Array = new Array();


// basic theme changes the shape of the cell when it connects.
function update_shape(mc_array, theme_name){
    if ("cake" == theme_name 
            || "traditional" == theme_name
            || "cake_take" == theme_name ) {
        set_static_shape(mc_array);
    } else if ("basic" == theme_name) {
        update_connected(mc_array);
    }
}


function set_static_shape(mc_array){
	var count:int = 0;
	for (var row:uint = 0; row < mc_array.length; row++) {
		for (var column:uint = 0; column < mc_array[row].length; column++) {
            var label:String = '_0000';
            var cell = mc_array[row][column];
            cell.black_shape_mc.gotoAndPlay(label);
            cell.white_shape_mc.gotoAndPlay(label);
        }
    }
}

//based on lifeanddeath.py:get_connected + get_labels
function update_connected(mc_array){
	var count:int = 0;
	for (var row:uint = 0; row < mc_array.length; row++) {
		for (var column:uint = 0; column < mc_array[row].length; column++) {
            var label:String = '_';
            var cell = mc_array[row][column];
            if ("black" == cell.currentLabel
                    || "white" == cell.currentLabel) {
                // north, east, south, west
                if (0 == row) {
                    label += '0';
                }
                else if (cell.currentLabel == mc_array[row-1][column].currentLabel) {
                    label += '1';
                }
                else {
                    label += '0';
                }
                if (mc_array[row].length - 1 == column) {
                    label += '0';
                }
                else if (cell.currentLabel == mc_array[row][column+1].currentLabel) {
                    label += '1';
                }
                else {
                    label += '0';
                }
                if (mc_array.length - 1 == row) {
                    label += '0';
                }
                else if (cell.currentLabel == mc_array[row+1][column].currentLabel) {
                    label += '1';
                }
                else {
                    label += '0';
                }
                if (0 == column) {
                    label += '0';
                }
                else if (cell.currentLabel == mc_array[row][column-1].currentLabel) {
                    label += '1';
                }
                else {
                    label += '0';
                }
                cell.black_shape_mc.gotoAndPlay(label);
                cell.white_shape_mc.gotoAndPlay(label);
            }
		}
	}
}



//based on lifeanddeath.py:get_blocks
function update_blocks(mc_array){
    /**/
	var count:int = 0;
	for (var row:uint = 0; row < mc_array.length; row++) {
		for (var column:uint = 0; column < mc_array[row].length; column++) {
            var label:String = '_';
            var cell = mc_array[row][column];
            if ("black" == cell.currentLabel
                    || "white" == cell.currentLabel) {
                var opposite = "black";
                if ("black" == cell.currentLabel) {
                    opposite = "white";
                }
                // (north, east, south, west)
                // north
                if (0 == row) {
                    gotoAndPlayFrom(cell.block_north_mc, "none", "block");
                }
                else if (opposite == mc_array[row-1][column].currentLabel) {
                    gotoAndPlayFrom(cell.block_north_mc, "none", "block");
                }
                else {
                    cell.block_north_mc.gotoAndPlay('none');
                }
                // east
                if (mc_array[row].length - 1 == column) {
                    gotoAndPlayFrom(cell.block_east_mc, "none", "block");
                }
                else if (opposite == mc_array[row][column+1].currentLabel) {
                    gotoAndPlayFrom(cell.block_east_mc, "none", "block");
                }
                else {
                    cell.block_east_mc.gotoAndPlay('none');
                }
                // south
                if (mc_array.length - 1 == row) {
                    gotoAndPlayFrom(cell.block_south_mc, "none", "block");
                }
                else if (opposite == mc_array[row+1][column].currentLabel) {
                    gotoAndPlayFrom(cell.block_south_mc, "none", "block");
                }
                else {
                    cell.block_south_mc.gotoAndPlay('none');
                }
                // west
                if (0 == column) {
                    gotoAndPlayFrom(cell.block_west_mc, "none", "block");
                }
                else if (opposite == mc_array[row][column-1].currentLabel) {
                    gotoAndPlayFrom(cell.block_west_mc, "none", "block");
                }
                else {
                    cell.block_west_mc.gotoAndPlay('none');
                }
            }
            else { // empty
                gotoAndPlayFrom(cell.block_west_mc, 
                        "block", "none");
                gotoAndPlayFrom(cell.block_west_mc, 
                        "danger", "none");
                gotoAndPlayFrom(cell.block_west_mc, 
                        "warning", "none");
                gotoAndPlayFrom(cell.block_north_mc, 
                        "block", "none");
                gotoAndPlayFrom(cell.block_north_mc, 
                        "danger", "none");
                gotoAndPlayFrom(cell.block_north_mc, 
                        "warning", "none");
                gotoAndPlayFrom(cell.block_east_mc, 
                        "block", "none");
                gotoAndPlayFrom(cell.block_east_mc, 
                        "danger", "none");
                gotoAndPlayFrom(cell.block_east_mc, 
                        "warning", "none");
                gotoAndPlayFrom(cell.block_south_mc, 
                        "block", "none");
                gotoAndPlayFrom(cell.block_south_mc, 
                        "danger", "none");
                gotoAndPlayFrom(cell.block_south_mc, 
                        "warning", "none");
            }
		}
	}
    /**/
}

/*-
function play_stone(intersection, color) {    
    place_stone(intersection, color);
    update_blocks(intersection_mc_array);
    set_intersection_turn();
}
-*/
/*-
function black_last_move(intersection_mc) {
    snap(black_last_move_mc, intersection_mc);
    gotoAndPlayLabel(black_last_move_mc, "place");
}

function white_last_move(intersection_mc) {
    snap(white_last_move_mc, intersection_mc);
    gotoAndPlayLabel(white_last_move_mc, "place");
}

function place_stone(intersection, color) {
    if ("empty" != color) {
        trace("place_stone:  " + intersection.name);
        gotoAndPlayLabel(intersection, color);
        //if ("black" == color) {
        //    snap(black_last_move_mc, intersection);
        //}
        //else if ("white" == color) {
        //    snap(white_last_move_mc, intersection);
        //}
        // focus_array.push(intersection);
        // any_match = update_formation(
        //    intersection_mc_array, 
        //    focus_array,
        //    "black" == color);
    }
    else {
        gotoAndPlayLabel(intersection, 
            color + "_" + turn_mc.currentLabel);
    }
}



function clear_intersection(intersection) {
    gotoAndPlayLabel(intersection,
            "empty_" + turn_mc.currentLabel);
}

// undo when many stones are played only changes turn once.
function play_stone_set(news) {
    respond_all(clear_intersection, intersection_mc_array,
        news, "clear_board");
    respond_at_this_way(place_stone, intersection_mc_array, 
        news, "black", "black");
    respond_at_this_way(place_stone, intersection_mc_array, 
        news, "white", "white");
    respond_at_this_way(place_stone, intersection_mc_array, 
        news, "empty", "empty");

    update_blocks(intersection_mc_array);
    set_intersection_turn();
}


function danger(intersection){
    // trace("danger:  " + intersection.name);
    gotoAndPlay_if_not(intersection.block_north_mc, "none", "danger_start")
    gotoAndPlay_if_not(intersection.block_east_mc, "none", "danger_start")
    gotoAndPlay_if_not(intersection.block_west_mc, "none", "danger_start")
    gotoAndPlay_if_not(intersection.block_south_mc, "none", "danger_start")
}

function end_danger(intersection){
    // trace("end_danger:  " + intersection.name);
    gotoAndPlay_if_not(intersection.block_north_mc, "none", "block")
    gotoAndPlay_if_not(intersection.block_east_mc, "none", "block")
    gotoAndPlay_if_not(intersection.block_west_mc, "none", "block")
    gotoAndPlay_if_not(intersection.block_south_mc, "none", "block")
}


function warning(intersection){
    // trace("warning:  " + intersection.name);
    gotoAndPlay_if_not(intersection.block_north_mc, "none", "warning_start")
    gotoAndPlay_if_not(intersection.block_east_mc, "none", "warning_start")
    gotoAndPlay_if_not(intersection.block_west_mc, "none", "warning_start")
    gotoAndPlay_if_not(intersection.block_south_mc, "none", "warning_start")
}

function end_warning(intersection){
    // trace("end_warning:  " + intersection.name);
    gotoAndPlay_if_not(intersection.block_north_mc, "none", "block")
    gotoAndPlay_if_not(intersection.block_east_mc, "none", "block")
    gotoAndPlay_if_not(intersection.block_west_mc, "none", "block")
    gotoAndPlay_if_not(intersection.block_south_mc, "none", "block")
}


function suicide(intersection){
    gotoAndPlayLabel(intersection.block_north_mc, "suicide_start")
    gotoAndPlayLabel(intersection.block_east_mc, "suicide_start")
    gotoAndPlayLabel(intersection.block_west_mc, "suicide_start")
    gotoAndPlayLabel(intersection.block_south_mc, "suicide_start")
}

function suicide_end(intersection){
    gotoAndPlayFrom(intersection.block_north_mc, "suicide", "none")
    gotoAndPlayFrom(intersection.block_east_mc, "suicide", "none")
    gotoAndPlayFrom(intersection.block_west_mc, "suicide", "none")
    gotoAndPlayFrom(intersection.block_south_mc, "suicide", "none")
}


function suicide_white(intersection){
    gotoAndPlayLabel(intersection.block_north_mc, "suicide_white_start")
    gotoAndPlayLabel(intersection.block_east_mc, "suicide_white_start")
    gotoAndPlayLabel(intersection.block_west_mc, "suicide_white_start")
    gotoAndPlayLabel(intersection.block_south_mc, "suicide_white_start")
}

function suicide_white_end(intersection){
    gotoAndPlayFrom(intersection.block_north_mc, "suicide_white", "none")
    gotoAndPlayFrom(intersection.block_east_mc, "suicide_white", "none")
    gotoAndPlayFrom(intersection.block_west_mc, "suicide_white", "none")
    gotoAndPlayFrom(intersection.block_south_mc, "suicide_white", "none")
}


function mark_territory(intersection, new_label){
    // trace("mark_territory(" + intersection.name + ", " + new_label + ");" );
    gotoAndPlayLabel(intersection.territory_mc, new_label);
}

var territory_marks = ["white", "black", "neutral", "dead"];

function update_territory(territory_news) {
    var grid:Array = intersection_mc_array;
    for (var m = 0; m < territory_marks.length; m++) {
        var mark = territory_marks[m];
        respond_at_this_way(mark_territory, grid, 
            territory_news, mark, mark);
    }
}

function score(score_news) {
    set_text(game_over_mc.score_mc, score_news);
}


function genmove(color) {
        // Ask Python to generate a move.
        ambassador.ask({"genmove":  color});
}

function more(yes) {
    // Ask Python to continue with news
    ambassador.ask({"more":  yes});
}

function level(level_string) {
    lobby_mc.level_txt.text = level_string;
}

function set_this_theme(theme) {
    set_theme(intersection_mc_array, theme);
}
-*/
/*-
// receive array inside of a dictionary
// Place sequence of black or white stones.
function read_news(news){
    trace("read_news(...)");
    // t.obj(  news, "read_news(...)");
    update(null);
    if (undefined != news["busy"]) {
        ambassador.ask({"showboard":  true});
    }
    if (undefined != news["turn_reminder"]) {
        ambassador.ask({"genmove":  "white"});
    }
    play_stone_set(news);
    var grid:Array = intersection_mc_array;
    respond_at(suicide_end, grid, news, "suicide_end");
    respond_at(suicide_white_end, grid, news, "suicide_white_end");
    respond_at(end_warning, grid, news, "warning end");
    respond_at(end_danger, grid, news, "danger end");
    respond_at(suicide, grid, news, "suicide");
    respond_at(suicide_white, grid, news, "suicide_white");
    respond_at(danger, grid, news, "danger");
    respond_at(warning, grid, news, "warning");
    respond_at(hide_black, grid, news, "hide");
    respond_at(unhide_black, grid, news, "unhide");
    respond_at(black_last_move, grid, news, "black_last_move");
    respond_at(white_last_move, grid, news, "white_last_move");
    respond_at(star, grid, news, "star");
    respond_at(unstar, grid, news, "unstar");
    respond(set_turn, news, "turn");
    respond(level, news, "level");
    //- respond(offer_table, news, "offer_table"); 
    respond(more, news, "more");
    respond(genmove, news, "genmove");
    follow_this_news(news, mc_dictionary);
    if ("traditional" != theme_txt.text) {
        follow_formation_news(news);
    }
    respond(update_undo_gift, news, "undo_gift");
    respond(update_territory, news, "territory");
    respond(score, news, "score");
    set_this_text(this.root, "black_name_txt", news);
    set_this_text(this.root, "white_name_txt", news);
    respond(set_this_theme, news, "theme");
    update(null);
}
-*/

/*-
function activate_intersection(mouse_event:MouseEvent){
    var intersection = mouse_event.target.parent.parent;
    trace("activate_intersection:  " + intersection.name);
    if (ambassador.use_server) {
        var coordinates:Array = indexOf2d(intersection_mc_array, intersection);
    }

	if ("empty_black" == intersection.currentLabel){
        if (ambassador.use_server) {
            ambassador.ask({"black":  [coordinates]});
        } else {
            play_stone("black", intersection);
        }
	}
	else if ("empty_white" == intersection.currentLabel){
        if (ambassador.use_server) {
            ambassador.ask({"white":  [coordinates]});
        } else {
            play_stone("white", intersection);
        }
	}
    else if ("empty_hide_black" == intersection.currentLabel){
        ambassador.hide_stone({"black":  [coordinates]});
    }
	else if ("black_capture" == intersection.currentLabel){
		intersection.gotoAndPlay("empty_disabled");
	}
	else if ("white_capture" == intersection.currentLabel){
		intersection.gotoAndPlay("empty_disabled");
	}


}
-*/

/*
undo
formation:  +10
maximum:  50
undo:  -1
hide:  -5

too low:
formation:  +4
maximum:  20
undo:  -1
hide:  -5
*/
/*
function increment_undo(by) {
	if (undo_gift_mc.currentFrame < undo_gift_mc.totalFrames) {
        for (var i = 0; i < by; i++) {
    		undo_gift_mc.nextFrame();
        }
		undo_gift_mc.stop();
	}
}

function decrement_undo(by) {
	if (1 + by <= undo_gift_mc.currentFrame) {        
        for (var i = 0; i < by; i++) {
       		undo_gift_mc.prevFrame();
        }
		undo_gift_mc.stop();
	}
	else {
		undo_gift_mc.gotoAndStop(1);
		undo_gift_mc.stop();
	}
}

undo_gift_mc.gotoAndStop(1);

function update_undo_gift(new_value){
    undo_gift_mc.gotoAndStop(new_value);
}
*/
/*
Undo
When undo available.
*/


/*
function update_enable_undo(){
    if (2 <= undo_gift_mc.currentFrame) {
        undo_gift_btn.visible = true;
    }
    else {
        undo_gift_btn.visible = false;
    }
}


function undo(mouse_event:MouseEvent){
        if (ambassador.use_server) {
            ambassador.ask({"undo":  2});
            // decrement_undo(1);
        } else {
            trace("undo:  The server undoes, but ambassador does not user_server.");
        }
}
*/

//- function pass(mouse_event:MouseEvent){
//-     ambassador.ask({'black':  ['pass']});
//- }

//- undo_gift_btn.addEventListener(MouseEvent.CLICK, undo);
//- pass_btn.addEventListener(MouseEvent.CLICK, pass);

function set_level_10(mouse_event:MouseEvent) {
    ambassador.set_level(10);
    set_theme(intersection_mc_array, "cake_take");
    gotoAndPlay("table");
}

lobby_mc.level_10_btn.addEventListener(MouseEvent.CLICK, set_level_10);

function goto_next(mouse_event:MouseEvent){
    gotoAndPlay(currentFrame + 1);
}

/*
intro_mc.end_intro_btn.addEventListener(MouseEvent.CLICK,
				goto_next);
*/

// http://board.flashkit.com/board/showthread.php?t=757839
function start_btn_click(mouse_event:MouseEvent) {
    //mouse_event.buttonDown = true;
    //title_mc.start_btn.dispatchEvent(mouse_event);
    var m = new MouseEvent(MouseEvent.CLICK);
	//m.buttonDown = true;
    title_mc.start_btn.dispatchEvent(m);
    // m.buttonDown = false;
    // title_mc.start_btn.dispatchEvent(m);
}
title_mc.start_btn_click_btn.addEventListener(MouseEvent.CLICK, start_btn_click);


function exit(mouse_event:MouseEvent) {
    ambassador.exit();
}

lobby_mc.exit_btn.addEventListener(MouseEvent.CLICK, 
        exit);


//- function keep_playing(mouse_event:MouseEvent) {
//-     gotoAndPlayLabel(game_over_mc, "none");
//- }
//- game_over_mc.keep_playing_btn.addEventListener(
//-     MouseEvent.CLICK, keep_playing);
				

//- function start_game(mouse_event:MouseEvent) {
//-     ambassador.start();
//- }
//- game_over_mc.start_btn.addEventListener(
//-     MouseEvent.CLICK, start_game);

function goto_tutorial(mouse_event:MouseEvent){
    ambassador.set_level(1);
    set_theme(intersection_mc_array, "cake_take");
    gotoAndPlay("intro");
}
lobby_mc.tutorial_btn.addEventListener(MouseEvent.CLICK, goto_tutorial);


//- function goto_level_1(mouse_event:MouseEvent){
//-     ambassador.set_level(1);
//-     set_theme(intersection_mc_array, "cake_take");
//-     gotoAndPlay("level_1");
//- }
//- lobby_mc.level_1_mc.enter_btn.addEventListener(MouseEvent.CLICK, goto_level_1);




function goto_level_25(mouse_event:MouseEvent){
    ambassador.set_level(25);
    set_theme(intersection_mc_array, "cake_take");
    gotoAndPlay("table");
}
lobby_mc.level_25_btn.addEventListener(MouseEvent.CLICK, goto_level_25);
function goto_basic(mouse_event:MouseEvent){
    ambassador.set_level(25);
    set_theme(intersection_mc_array, "basic");
    gotoAndPlay("table");
}
lobby_mc.level_25_basic_btn.addEventListener(MouseEvent.CLICK, goto_basic);
function goto_traditional(mouse_event:MouseEvent){
    ambassador.set_level(40);
    set_theme(intersection_mc_array, "traditional");
    gotoAndPlay("table");
}
lobby_mc.level_40_btn.addEventListener(MouseEvent.CLICK, goto_traditional);



/*-
function create(mouse_event:MouseEvent){
    ambassador.create();
}
lobby_mc.create_btn.addEventListener(
    MouseEvent.CLICK, create);
-*/

/*-
function offer_table(name) {
    gotoAndPlayLabel(lobby_mc.join_mc, "join");
    lobby_mc.join_mc.join_txt.text = name;
}

function join(mouse_event:MouseEvent){
    var name = lobby_mc.join_mc.join_txt.text;
    ambassador.join(name);
}
lobby_mc.join_mc.join_btn.addEventListener(
    MouseEvent.CLICK, join);
-*/

function goto_my_name(mouse_event:MouseEvent){
    trace("goto_to_my_name('" + mouse_event.target.name + "')");
    (root as MovieClip).gotoAndPlay(mouse_event.target.name);
}

//lobby.addEventListener(MouseEvent.CLICK, goto_my_name);

/*
function goto_lobby(mouse_event:MouseEvent){
    gotoAndPlay("lobby");
}
function stop_confirm(mouse_event:MouseEvent){
    ambassador.stop("confirm");
}
lobby_btn.addEventListener(MouseEvent.CLICK, stop_confirm);
*/

/*
Hide a stone
undo increases to show button with cake under a tile.

Player clicks cake under a tile.

Time restarts.

Player mouse turns into cake under tile.

Player clicks intersection.

The cake is shown as played under tile.
Shape and liberty blockages are revealed.

White plays there.
Reveal!

*/

/*
function update_enable_hide(){
    if (5 <= undo_gift_mc.currentFrame) {
        hide_gift_mc.visible = true;
    }
    else {
        hide_gift_mc.visible = false;
    }
}
*/
/*-
function start_hide(mouse_event:MouseEvent){
    do_all_these_ways(gotoAndPlayFrom, 
        intersection_mc_array, 
        "empty_black", "empty_hide_black");
    // decrement_undo(3);
}
hide_gift_mc.addEventListener(
        MouseEvent.CLICK, start_hide);
-*/

/*
function start_extra_stone(mouse_event:MouseEvent){
    ambassador.ask({"extra_stone_gift":  extra_stone_gift_mc.currentLabel});
    // decrement_undo(3);
}


extra_stone_gift_mc.addEventListener(
        MouseEvent.CLICK, start_extra_stone);
*/

// see:  activation_intersection

/*-
// {'genmove': 'white', 'black': [8, 3], 'turn': 'white', 'hide': [8, 3]}
function hide_black(intersection_mc){
    gotoAndPlayLabel(intersection_mc.hide_mc, "hide");
}

function unhide_black(intersection_mc){
    gotoAndPlayLabel(intersection_mc.hide_mc, "none");
}

function star(intersection_mc){
    gotoAndPlayLabel(intersection_mc.star_mc, "star");
}

function unstar(intersection_mc){
    gotoAndPlayLabel(intersection_mc.star_mc, "none");
}

// Player sets Computer plays white.


function white_computer(mouse_event:MouseEvent){
    ambassador.configure({'white':  'computer'});
}

function white_human(mouse_event:MouseEvent){
    ambassador.configure({'white':  'human'});
}

white_computer_btn.addEventListener(
        MouseEvent.CLICK, white_computer);

white_human_btn.addEventListener(
        MouseEvent.CLICK, white_human);




// return 2D address as an array (r, c) or (-1, -1) if not found.
function indexOf2d(intersection_mc_array, target_mc):Array{
	for (var row:uint = 0; row < intersection_mc_array.length; row++) {
		for (var column:uint = 0; column < intersection_mc_array[row].length; column++) {
            var intersection = intersection_mc_array[row][column];
            if (target_mc == intersection){
                return new Array(row, column);
            }
        }
    }
    return new Array(-1, -1);
}




function set_intersection_turn(){
	if ("black" == turn_mc.currentLabel) {
		// TODO:  implement in turn_mc.
		gotoAndPlay_if("empty_white", "empty_black", intersection_mc_array);
		gotoAndPlay_if("empty_hide_black", "empty_black", intersection_mc_array);
		//turn_mc.gotoAndPlay("white");
	}
	else if ("white" == turn_mc.currentLabel) {
		// TODO:  implement in turn_mc.
		gotoAndPlay_if("empty_black", "empty_white", intersection_mc_array);
		gotoAndPlay_if("empty_hide_black", "empty_white", intersection_mc_array);
		//turn_mc.gotoAndPlay("black");
	}
	else {
		trace(":(  update:  I was expecting turn_mc to be 'black' or 'white', not " + turn_mc.currentLabel);
	}
}


function set_turn(color){
	if ("black" != color && "white" != color) {
		trace("set_turn:  >_<  I was expecting color to be 'black' or 'white', not " + color);
	}
	turn_mc.gotoAndPlay(color);
	turn_veil_mc.gotoAndPlay(color);
    update_shape(intersection_mc_array, theme_txt.text);
    set_intersection_turn();
}






import flash.net.FileReference;
import flash.net.URLRequest;

function go_loadsgf(file_event:Event){
    ambassador.ask({"loadsgf":  
            "sgf/" + loadsgf_reference.name});
}

function browse_loadsgf(mouse_event:MouseEvent){
    loadsgf_reference.addEventListener(Event.SELECT, go_loadsgf);
    loadsgf_reference.browse();
    // trace("file:  " + loadsgf_reference 
    //    +  "name:  " + loadsgf_reference.name);
}

var loadsgf_reference = new FileReference();
loadsgf_btn.addEventListener(MouseEvent.CLICK, browse_loadsgf);

function go_printsgf(printsgf_event:MouseEvent){
    ambassador.printsgf();
}

/*save overwrites locally and requires downloading data from Python
function save_printsgf(sgf){
    printsgf_reference.save(sgf, "new.sgf");
    // trace("file:  " + printsgf_reference 
    //    +  "name:  " + printsgf_reference.name);
}
*/
/*-
// var printsgf_reference = new FileReference();
printsgf_btn.addEventListener(MouseEvent.CLICK, 
    go_printsgf);

function update_capture()
{
    // TODO:  DEPRECATE capture tool or convert to mark dead or edit mode.
	if ("enabled" == capture_mc.currentLabel) {
		white_stone_count = count_label("white_capture", intersection_mc_array);		
		if (white_stone_count < previous_white_stone_count) {
			capture_mc.black_capture_txt.text = (int(capture_mc.black_capture_txt.text) + 1).toString();
			previous_white_stone_count = white_stone_count;
		}
		black_stone_count = count_label("black_capture", intersection_mc_array);		
		if (black_stone_count < previous_black_stone_count) {
			capture_mc.white_capture_txt.text = (int(capture_mc.white_capture_txt.text) + 1).toString();
			previous_black_stone_count = black_stone_count;
		}		
	}
    update_shape(intersection_mc_array, theme_txt.text);
    update_blocks(intersection_mc_array);
}

function toggle_capture_tool(mouse_event:MouseEvent){
	if ("enabled" == capture_mc.currentLabel) {
		capture_mc.gotoAndPlay("disabled");
		gotoAndPlay_if("white_capture", "white", intersection_mc_array);
		gotoAndPlay_if("black_capture", "black", intersection_mc_array);
		gotoAndPlay_if("empty_disabled", "empty_black", intersection_mc_array);
		set_intersection_turn();
	}
	else if ("disabled" == capture_mc.currentLabel) {
		capture_mc.gotoAndPlay("enabled");
		gotoAndPlay_if("white", "white_capture", intersection_mc_array);
		gotoAndPlay_if("black", "black_capture", intersection_mc_array);
		gotoAndPlay_if("empty_black", "empty_disabled", intersection_mc_array);
		gotoAndPlay_if("empty_white", "empty_disabled", intersection_mc_array);
	}
	else {
		trace(":( toggle_capture_tool:  I expected capture_mc label to be 'enabled' or 'disabled', not " + capture_mc.currentLabel);
	}
}


//
// Flash movie model
//

function set_property(lineage) {
    var inheritance = lineage[lineage.length-1];
    var parent = root;
    for (var c = 0; c < (lineage.length-2); c ++) {
        var child = lineage[c];
        parent = parent[child];
    }
    child = lineage[lineage.length-2];
    parent[child] = inheritance;
}


function test_set_property() {
    trace(root['title_mc']['username_txt']['text']);
    root['title_mc']['username_txt']['text'] = 'user0';
    set_property(['title_mc', 'username_txt', 'text', 'user1']);
}

test_set_property();

function read_property(news) {
    if (undefined != news['set_property']) {
        var lineage = news['set_property'];
        set_property(lineage);
    }
}

-*/

	

