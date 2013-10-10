from amf_socket_client import *

def split_example():
    r'''Send a message to server.
    >>> from test_network import subprocess_gateway
    >>> gateway_process = subprocess_gateway(file = 'amf_socket_server_split.py')
    >>> def pass_this(news):
    ...     pass
    >>> client = AmfSocketClient(on_receive = pass_this)
    >>> client.connect('localhost', 5900)

    Soon, the server acknowledges the connection.
    >>> time.sleep(2)
    >>> client.receives[-1]
    {'gateway_mc': {'currentLabel': u'connect'}}

    Only when necessary to debug,
    Test protocol writes raw AMF data it sent, one file per message in /log/#.amf
    Protocol is volatile, so the numbering may restart and overwrite frequently.

    After connection message, if enabled, send greeting.
    >>> from amf_socket_server_split import split_protocol
    >>> split_protocol.on_connect_greets
    ['log/greet/0.amf', 'log/greet/1.amf', 'log/greet/2.amf']

    I used this to test an archived message.
    >>> client.send({0: 0})
    >>> time.sleep(1.0 / 4)
    >>> client.send({1: 1})
    >>> time.sleep(1.0 / 4)
    >>> client.send({2: 2})
    >>> time.sleep(1.0 / 4)
    >>> len(client.receives)
    4
    >>> client.receives[-1]

    Unlike Flash, during a single server protocol send,
    this AMF client only receives single message from server.
    
    Disconnect, so that listener will go away.
    >>> client.is_alive = False
    '''


