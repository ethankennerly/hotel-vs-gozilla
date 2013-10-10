# Configure client and server for development or public service

import os
nt_gtp_path = os.path.join(os.getcwd(), 
                         os.path.dirname(__file__),
                         'gnugo-3.8.exe')
environ = {
    'posix': {
        'amf_host': '114.202.247.104',
        'gtp_path': '/usr/local/bin/gnugo'},
    'nt': {
        'amf_host': 'localhost',
        'gtp_path': nt_gtp_path}
}

if not environ.get(os.name):
    print 'configuration.py: which environment is this?'
    
# client
amf_port = 5900
amf_host = environ[os.name]['amf_host']
# # remote
# amf_host = environ['posix']['amf_host']

# server
gtp_path = environ[os.name]['gtp_path']
gtp_host = 'localhost'
gtp_port = 5903
# flash always checks policy on port 843
policy_port = 843
policy_file = 'socket-policy.xml'

