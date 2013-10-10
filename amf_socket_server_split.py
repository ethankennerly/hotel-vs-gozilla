from amf_socket_server_test import *

r'''
06/18/2010 Fri 
21:02
Example session:

WARNING:root:Running Socket AMF gateway on localhost:5900
WARNING:root:Running Policy file socket-policy.xml server on localhost:843
WARNING:root:write_to_file: path: ./log/1.amf
WARNING:root:TestAmfSocketProtocol greet: path: log/greet/0.amf
WARNING:root:TestAmfSocketProtocol greet: path: log/greet/1.amf
WARNING:root:TestAmfSocketProtocol greet: path: log/greet/2.amf
WARNING:root:sending '\n\x0b\x01\x11title_'...'e_mc\n\x01\x04\x06\x11r'
WARNING:root:sending 'esponse\x01\x01\x01'...'\x01\x04\x06\x10\x01\x08\n\x01\x04
\x06'
WARNING:root:sending '\x06\x01\x01\x0f_0_6_m'...'\x08\n\x01\x04\x06\x06\x01\x01\
x01\n'
WARNING:root:write_to_file: path: ./log/2.amf
'''

class split_protocol(greets_protocol):
    # split = None
    split = 1198
    split_remainder = None

    def on_receive(self, message):
        if self.on_connect_greets or self.split_remainder:
            if self.split and not self.split_remainder:
                greeting_amf = self.read_greet()
                while self.on_connect_greets:
                    socket_trims_separator_byte = self.read_greet()[1:]
                    greeting_amf = greeting_amf + socket_trims_separator_byte
            elif self.split_remainder:
                greeting_amf = self.split_remainder
            else:
                greeting_amf = ''
            if self.split and self.split < len(greeting_amf):
                self.split_remainder = greeting_amf[self.split:]
                greeting_amf = greeting_amf[0:self.split]
            elif self.split and len(greeting_amf) <= self.split:
                self.split_remainder = None
            self.transport.write(greeting_amf)
            head = greeting_amf[0:10].__repr__()
            tail = greeting_amf[-10:].__repr__()
            logging.warn('sending %s...%s' % (head, tail))
        else:
            AmfSocketProtocol.on_receive(self, message)

AmfSocketFactory.protocol = split_protocol

if __name__ == '__main__':
    run_server()

