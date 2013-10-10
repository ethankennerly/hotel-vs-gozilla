// Simple go board to illustrate encoding object into AMF over a socket.
// Author:  Ethan Kennerly    http://finegamedesign.com

function move_stone(mouse_event:MouseEvent) {
    mouse_event.currentTarget.x = mouseX;
    mouse_event.currentTarget.y = mouseY;
}

function get_stone(mouse_event:MouseEvent) {
    mouse_event.currentTarget.gotoAndPlay('get');
    var top:int = numChildren - 1;
    var index = getChildIndex((mouse_event.currentTarget) as MovieClip);
    swapChildrenAt(index, top);
    mouse_event.currentTarget.addEventListener(
            MouseEvent.MOUSE_MOVE, move_stone);
}

function put_stone(mouse_event:MouseEvent) {
    mouse_event.currentTarget.gotoAndPlay('putting');
    mouse_event.currentTarget.removeEventListener(
            MouseEvent.MOUSE_MOVE, move_stone);
    mouse_event.currentTarget.gotoAndPlay('put');
}

function stone_addEventListener(){
    var stone_count:uint = 41;
    var color_array:Array = ['black', 'white'];
	for (var c:uint = 0; c < color_array.length; c++) {
        var color = color_array[c];
        for (var s:uint = 0; s < stone_count; s++) {
            var stone_name:String = color + s.toString();
            var stone_mc = root[stone_name];
            stone_mc.addEventListener(
                MouseEvent.MOUSE_DOWN, get_stone);
            stone_mc.addEventListener(
                MouseEvent.MOUSE_UP, put_stone);
        }
    }
    // adobe.com/devnet/actionscript/articles/event_handling_as3_05.html
}

stone_addEventListener();

