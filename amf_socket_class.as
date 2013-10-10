package
{
	/** Simple AMF socket client that sends and receives an "Object".
        Adapted by Ethan Kennerly from PythonSocket.as which was:
	 * Copyright (c) 2007-2009 The PyAMF Project.
	 * See LICENSE.txt for details.
     * and AS3 socket reference:
     * http://help.adobe.com/en_US/AS3LCR/Flash_10.0/flash/net/Socket.html#writeObject()
	 */
	 
	import flash.errors.IOError;
	import flash.errors.EOFError;
	import flash.events.Event;
	import flash.events.IOErrorEvent;
	import flash.events.ProgressEvent;
	import flash.events.SecurityErrorEvent;
	import flash.net.ObjectEncoding;
	import flash.net.Socket;
	import flash.system.Capabilities;
    import flash.utils.ByteArray;
	
	[Event(name="connected", type="flash.events.Event")]
	[Event(name="disconnected", type="flash.events.Event")]
	[Event(name="logUpdate", type="flash.events.Event")]
	/**
	 * Socket connection to read and write raw binary data.
	 * 
	 * @see http://livedocs.adobe.com/flex/3/langref/flash/net/Socket.html
	 * @since 0.1.0
	 */	
	public class amf_socket_class extends Socket
	{
		public  var log		    		: String;
		public  var is_alive    		: Boolean;
		public  var packet_count    	: int = 0;
		private var _host				: String;
		private var _port				: int;
		public  var result				: Object = {};
		public  var on_receive;
		public  var on_timeout;
		public  var on_log; 
		public  var prof; 
        public  var receives:Array = new Array();
        public  var reading:Boolean = false;
        public var byte_array:ByteArray = new ByteArray();
        public var in_progress:ByteArray = new ByteArray();
		
		public static const CONNECTED	: String = "connected";
		public static const DISCONNECTED: String = "disconnected";
		public static const LOG_UPDATE	: String = "logUpdate";
		
		public function amf_socket_class(
            host:String='localhost', port:int=8000, 
            on_receive_callback=null, on_timeout_callback=null, 
            on_log_callback = null, profiler = null)
		{
            // file:///C:/Program%20Files%20(x86)/Common%20Files/Adobe/Help/en_US/AS3LCR/Flash_10.0/index.html
            // It is strongly advised to use the constructor form without parameters , 
            // then add any event listeners, 
            // then call the connect method with host and port parameters. 
            // This sequence guarantees that all event listeners will work properly.
			super();
			
			_host = host;
			_port = port;
			log = "Using Flash Player " + Capabilities.version + "\n";
			
			objectEncoding = ObjectEncoding.AMF3;
			//objectEncoding = ObjectEncoding.AMF0;
			configureListeners();
            on_receive = on_receive_callback;
            on_timeout = on_timeout_callback;
            on_log = on_log_callback;
            prof = profiler;
			
			logger("Connecting to socket server on " + _host + ":" + _port);
            connect(host, port);
		}
	
		private function configureListeners():void 
		{
	        addEventListener(Event.CLOSE, closeHandler);
	        addEventListener(Event.CONNECT, connectHandler);
	        addEventListener(IOErrorEvent.IO_ERROR, ioErrorHandler);
	        addEventListener(SecurityErrorEvent.SECURITY_ERROR, securityErrorHandler);
	        addEventListener(ProgressEvent.SOCKET_DATA, readResponse);
	    }
	
	    private function try_writeObject(object:Object):void 
	    {
	        try {
	            this.writeObject(object);
	        }
	        catch(e:IOError) {
	        	switch (e.errorID) {
	        		case 2002:
	        			// reconnect when connection timed out
	        			if (!connected) {
                            on_timeout();
	        				logger("Reconnecting...");
	        				connect( _host, _port );
	        			}
	        			break;
	        			
	        		default:
	        			logger(e.toString());
	        			break;
	        	}
	        }
	    }
        
	    public function send(object:Object):void 
	    {
	        // logger("send:  " + object.toString() );
            try_writeObject(object);
	        flush();
	    }
	
	    private function readResponse(event:ProgressEvent):void 
        {
            packet_count ++;
        //}
        //
	    //public function updateResponse():void 
	    //{
//             prof.beginProfiling();
//             prof.begin( "readResponse", true );
			// var result:Object = this.readObject();
            // Your code must access bytesAvailable 
            // to ensure that sufficient data is available 
            // before trying to read it with one of the read methods.
            // file:///C:/Program%20Files%20(x86)/Common%20Files/Adobe/Help/en_US/AS3LCR/Flash_10.0/index.html
            reading = true;
            //- if (! bytesAvailable) {
	        //-     logger("readResponse:  no bytesAvailable?  " + "\n" + status);
            //- }
            if (1 <= bytesAvailable) {
                var data:String = "";
                //- var attempt:uint = 0;
                var valid = true;
                var utf:String = "";
                var error_message:String = "";
                var debugging = false;
            //- if (attempt < 800000 && bytesAvailable) {
            // while (attempt < 800000 && bytesAvailable) {
                var status:String = 'bytesAvailable = ' + bytesAvailable;
                    //- + '; bytesLoaded = ' + bytesLoaded;
                    //- + '; attempt = ' + attempt;
                // Append broken or multiple messages to end of previous.
                // So do not byte_array.clear();
                if (debugging && byte_array) {
                    //? error_message = 'before readUTFBytes';
                    error_message = 'before readBytes';
                    error_message += '\n  byte_array.position: ' 
                        + byte_array.position + '';
                    error_message += '\n  byte_array.length: ' 
                        + byte_array.length + '';
                    error_message += '\n  byte_array.bytesAvailable: ' 
                        + byte_array.bytesAvailable + '';
                    logger(error_message); 
                }
                // ? why is socket bytes 2660, but byte array is 2667 bytes?
                // ? is utfbytes inserting 7 bytes?  
                // ? would it help to readBytes instead of  UTFBytes?
                // readBytes(bytes:ByteArray, offset:uint = 0, length:uint = 0):void
                // file:///C:/Program%20Files%20(x86)/Common%20Files/Adobe/Help/en_US/AS3LCR/Flash_10.0/flash/net/Socket.html#readBytes()
//                 prof.begin("bytesAvailable");
                byte_array.position = byte_array.length;
                this.readBytes(byte_array, byte_array.position, bytesAvailable);
                if (debugging && byte_array) {
                    utf = byte_array.toString().substring(0, 40);
                    var bytes_available_message:String = 'utf available part:\n' 
                        + utf + '...';
                    logger(bytes_available_message);
                }
                // in_progress = new ByteArray();
                in_progress.writeBytes(byte_array); // write to <-- from
                in_progress.position = 0;
                var offset = in_progress.position;
//                 prof.end("bytesAvailable");
                //? byte_array.writeUTFBytes( 
                //?     this.readUTFBytes(this.bytesAvailable) );
                while (valid && 1 <= in_progress.bytesAvailable) {
                    // result = null;
                    if (debugging && byte_array) {
                        error_message = 'before readObject';
                        error_message += '\n  byte_array.position: ' 
                            + byte_array.position + '';
                        error_message += '\n  byte_array.length: ' 
                            + byte_array.length + '';
                        error_message += '\n  byte_array.bytesAvailable: ' 
                            + byte_array.bytesAvailable + '';
                        logger(error_message); 
                    }
                    if (debugging && in_progress) {
                        error_message = 'before readObject';
                        error_message += '\n  in_progress.position: ' 
                            + in_progress.position + '';
                        error_message += '\n  in_progress.length: ' 
                            + in_progress.length + '';
                        error_message += '\n  in_progress.bytesAvailable: ' 
                            + in_progress.bytesAvailable + '';
                        logger(error_message); 
                    }
                    //- byte_array.position = 0;
                    //- result = byte_array.readObject();
                    offset = in_progress.position;
//                     prof.begin("readObject");
                    try {
                        result = in_progress.readObject();
                    }
                    catch (error:RangeError) {
                        error_message = error + '\n  ' + error.message;
                        valid = false;
                        byte_array = new ByteArray();
                        // write to <-- from
                        byte_array.writeBytes(in_progress, offset); 
                    }
                    catch (error:EOFError) {
                        error_message = error + '\n  ' + error.message 
                            + ' End of file was encountered.';
                        // http://www.adobe.com/livedocs/flash/9.0/ActionScriptLangRefV3/runtimeErrors.html
                        // http://www.adobe.com/livedocs/flash/9.0/ActionScriptLangRefV3/flash/utils/IDataOutput.html
                        valid = false;
                        // player (version 9?) complains that clear is not supported.  http://stackoverflow.com/questions/1411156/how-to-determine-when-a-method-or-property-was-added-to-a-flash-player-or-flex-sd
                        // Retain remainder
                        // byte_array.clear();
                        byte_array = new ByteArray();
                        // write to <-- from
                        byte_array.writeBytes(in_progress, offset); 
                    }
//                     prof.end("readObject");
                    if (! valid) {
                        if (null != result) {
                            error_message += '\n  result: "' + result.toString() 
                                + '"';
                        }
                        if (debugging && byte_array) {
                            error_message += '\n  byte_array.position: ' 
                                + byte_array.position + '';
                            error_message += '\n  byte_array.length: ' 
                                + byte_array.length + '';
                            error_message += '\n  byte_array.bytesAvailable: ' 
                                + byte_array.bytesAvailable + '';
                        }
                        if (debugging && in_progress) {
                            error_message += '\n  in_progress.position: ' 
                                + in_progress.position + '';
                            error_message += '\n  in_progress.length: ' 
                                + in_progress.length + '';
                            error_message += '\n  in_progress.bytesAvailable: ' 
                                + in_progress.bytesAvailable + '';
                        }
                        if (debugging && byte_array.bytesAvailable) {
                            utf = byte_array.toString();
                            error_message += '\n  byte_array availabe: "' + utf + '"';
                        }
                        if (debugging && in_progress.bytesAvailable) {
                            utf = in_progress.toString();
                            error_message += '\n  in_progress available: "' + utf + '"';
                        }
                        logger(error_message); 
                    }
                    //- attempt += 1;
                    if (debugging) {
                        logger("readResponse:  status:  " + status);
                    }
                    if (valid && null != result) {
                        // This is where you place your event handling.
                        if (null != on_receive ) {
//                             prof.begin("on_receive");
                            receives.push(result);
                            if (debugging) {
                                logger( receives.length.toString() 
                                    // + ":" + attempt.toString() 
                                    + " readResponse:  result = " + result.toString());
                                utf = in_progress.toString().substring(
                                        in_progress.position, 
                                        in_progress.position + 40);
                                //var end_index = byte_array.position + 40;
                                //var part = byte_array.toString().substring(
                                //    byte_array.position, end_index);
                                logger( receives.length.toString() 
                                    + " readResponse:  readObject remainder part:\n" 
                                    + utf + "...");
                            }
                            on_receive(result);
                            if (debugging
                                    && 0 == byte_array.position
                                    && 0 == byte_array.length
                                    && 0 == byte_array.bytesAvailable) {
                                trace("start debugging here");
                            }
//                             prof.end("on_receive");
                        }
                        var objects_are_separated = false;
                        if (objects_are_separated && 1 <= in_progress.bytesAvailable)
                        {
                            // Eat up the object separator char to avoid the
                            // "RangeError: Error #2006: The supplied index is out of bounds".
                            // Bob Sullivan, http://blog.smartlogicsolutions.com/2008/08/27/serialization-errorbug-when-using-bytearray-readobject-iexternalizable-class/
                            var separator = in_progress.readByte();
                            error_message = 'readResponse: separator: ' 
                                + separator;
                            if (null != separator) {
                                error_message += ' "' + separator.toString() + '"';
                            }
                            if (debugging && in_progress) {
                                error_message += '\n  in_progress.position: ' 
                                    + in_progress.position + '';
                                error_message += '\n  in_progress.length: ' 
                                    + in_progress.length + '';
                                error_message += '\n  in_progress.bytesAvailable: ' 
                                    + in_progress.bytesAvailable + '';
                            }
                            logger(error_message); 
                        }
                        // Clear buffer and retain remainder.
                        // byte_array.clear();
                        byte_array = new ByteArray();
                        // byte_array.writeBytes(in_progress); // write to <-- from
                    }
                    else if (null == result){
                        logger("readResponse:  readObject = null?  " + result 
                            + '\n  ' + status);
                    }
                    else {
                        logger("readResponse:  readObject not valid?  " 
                            + result.toString() 
                            + '\n  ' + status);
                    }
                }
            }
            //- if (800000 <= attempt) {
            //-     logger("readResponse:  attempt = " + attempt);
            //- }
            in_progress = new ByteArray();
            reading = false;
//             prof.end( "readResponse" );
//             prof.endProfiling();
	    }
		
	    private function logger(msg:String):void
		{
//             prof.begin("logger");
			var newMsg:String = msg + "\n";
			log += newMsg;
            if (on_log) {
                on_log(msg);
                trace(msg);
            }
			dispatchEvent(new Event(LOG_UPDATE));
//             prof.end("logger");
		}
		
	    private function connectHandler(event:Event):void 
	    {
	        logger("Connected to server.");
	        
	        dispatchEvent(new Event(CONNECTED));
	    }
	    
	    private function closeHandler(event:Event):void 
	    {
	        logger("Connection closed.");
	        
	        dispatchEvent(new Event(DISCONNECTED));
	    }
	
	    private function ioErrorHandler(event:IOErrorEvent):void 
	    {
	        logger("ioErrorHandler: " + event.text);
	    }
	
	    private function securityErrorHandler(event:SecurityErrorEvent):void 
	    {
	        logger("securityErrorHandler: " + event.text);
	    }
			
	}
}
