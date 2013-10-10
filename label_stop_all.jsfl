/* label_stop_all.jsfl    Ethan Kennerly    finegamedesign.com */

function prompt_label_stop_all()
{
    if ( ! fl.getDocumentDOM() || fl.getDocumentDOM().getTimeline() == null) {
        alert("Please select any frame in timeline");
        return false;
    }
    var timeline = fl.getDocumentDOM().getTimeline();
    var start_number_str = prompt("First number?");
    if (start_number_str == null) {
        fl.trace("prompt_label_stop_all:  You cancelled.");
        return false;
    }
 
    //  all frames in this timeline:  rename label to start_number + frame - 1
    fl.trace("label_stop_all('"+ start_number_str +"');");
    var start = parseInt(start_number_str);
    timeline.convertToKeyframes(1, timeline.frameCount);
    for (var i = 0; i < timeline.frameCount; i++) {
	var current = start + i;
	var label = '_' + current.toString();
	timeline.setFrameProperty('labelType', 'name', i);
	timeline.setFrameProperty('name', label, i );
	timeline.setFrameProperty('actionScript', 'stop();', i );
	fl.trace("    label " + label);
    }
 
    alert("Done!")
    return true;
}

prompt_label_stop_all();

