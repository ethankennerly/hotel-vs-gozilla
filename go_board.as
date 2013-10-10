// Simple go board to illustrate encoding object into AMF over a socket.
// Author:  Ethan Kennerly    http://finegamedesign.com

// Movie clip remote control protocol

include "remote_control.as";

// User interface

function mouse_move_stone(mouse_event:MouseEvent) {
    move_stone(root[selected_txt.text]);
}

function get_stone(mouse_event:MouseEvent) {
    var stone_mc = mouse_event.currentTarget; 
    stone_mc.gotoAndPlay('getting');
    selected_txt.text = stone_mc.name;
    stage.addEventListener(
            MouseEvent.MOUSE_MOVE, mouse_move_stone);
    send(ambassador, stone_mc, selected_txt);
}

function put_stone(mouse_event:MouseEvent) {
    var stone_mc = mouse_event.currentTarget; 
    stone_mc.gotoAndPlay('putting');
    stage.removeEventListener(
            MouseEvent.MOUSE_MOVE, mouse_move_stone);
    selected_txt.text = 'PICK STONE';
    send(ambassador, stone_mc);
}

function move_stone(stone_mc) {
    if (stone_mc) {
        stone_mc.x = mouseX;
        stone_mc.y = mouseY;
        if ('every_frame' == send_mc.currentLabel) {
            // beware!  send 24 frames per second spams network and looks laggy
            send(ambassador, stone_mc);  // beware!
        }
    }
}
function toggle_send_every_frame(mouse_event){
    var send_mc = mouse_event.currentTarget;
    if ('every_frame' != send_mc.currentLabel) {
        send_mc.gotoAndPlay('every_frame');        
    }
    else {
        send_mc.gotoAndPlay('after_put');        
    }
    send(ambassador, send_mc);
}
send_mc.addEventListener(MouseEvent.MOUSE_DOWN, 
    toggle_send_every_frame);

function listen_to_mouse(stone_mc, index, stone_mc_array){
    stone_mc.addEventListener(
                MouseEvent.MOUSE_DOWN, get_stone);
    stone_mc.addEventListener(
                MouseEvent.MOUSE_UP, put_stone);
    // adobe.com/devnet/actionscript/articles/event_handling_as3_05.html
}

function get_stone_mc_array(){
    var color_array = ['black', 'white'];
    var stone_count = 41;
    var stone_mc_array = [];
	for (var c:uint = 0; c < color_array.length; c++) {
        var color = color_array[c];
        for (var s:uint = 0; s < stone_count; s++) {
            var stone_name:String = color + s.toString();
            var stone_mc = root[stone_name];
            stone_mc_array.push(stone_mc);
        }
    }
    return stone_mc_array;
}

function get_top(stone_mc, index, stone_mc_array){
    if ("get" == stone_mc.currentLabel) {
        var top:int = numChildren - 1;
        var index = getChildIndex((stone_mc) as MovieClip);
        swapChildrenAt(index, top);
    }
}


var stone_mc_array = get_stone_mc_array();
stone_mc_array.forEach(listen_to_mouse);

function get_top_stone(event) {
    stone_mc_array.forEach(get_top);
}
stage.addEventListener(Event.ENTER_FRAME, get_top_stone);




// Network

function on_timeout() {
    gateway_mc.gotoAndPlay("timeout");
}

function close_gateway_message(mouse_event:MouseEvent) {
    gateway_mc.gotoAndPlay("none");
}

gateway_mc.close_btn.addEventListener(MouseEvent.CLICK, 
        close_gateway_message);

function update_log(message) {
    log_txt.text = message;
}

var ambassador = new amf_socket_class(
        this.host_txt.text, 
        int(this.port_txt.text), 
        this.imitate, this.on_timeout,
        this.update_log);



