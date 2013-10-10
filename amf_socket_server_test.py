#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Conveniently test local server from within an AMF client doctest.

To send specific messages:
    on_connect_greets
To combine all messages into one payload:  
    combine = True
To split each payload into parts:
    split = bytes
To truncate a message:
    truncate = bytes

For example, see amf_socket_client.py: example

Run this file, amf_socket_server_test.py
Open lifeanddeath.fla in Flash CS4.
Debug.  
Type in username 'ethan' and password 'kennery'.
Click start.
If necessary, click again to see other messages.
To reload greet messages, restart server.
'''
__author__ = 'Ethan Kennerly'
from amf_socket_server import *



class greets_protocol(AmfSocketProtocol):
    on_connect_greets = [
            'log/greet/0.amf', 'log/greet/1.amf', 'log/greet/2.amf']
    # truncate = 1198
    truncate = None
    combine = False
    # combine = True

    def on_send(self, message, amf_data):
        write_to_file(amf_data, len(self.sends))

    def read_greet(self):
        path = self.on_connect_greets.pop(0)
        logging.warn('TestAmfSocketProtocol greet: path: %s' % path)
        amf_file = open(path, 'rb')
        greeting_amf = amf_file.read()
        amf_file.close()
        #preserve exact encoding.  dictionary-like members might reencode in different order.
        #greeting_object = amf_socket_client.decode_object(greeting_amf)
        #greeting_amf = amf_socket_client.encode_object(self.encoder, 
        #        greeting_object)
        return greeting_amf

    def on_receive(self, message):
        if self.on_connect_greets:
            greeting_amf = self.read_greet()
            if self.truncate:
                greeting_amf = greeting_amf[0:self.truncate]
            self.transport.write(greeting_amf)
        else:
            AmfSocketProtocol.on_receive(self, message)


AmfSocketFactory.protocol = greets_protocol

if __name__ == '__main__':
    run_server()

