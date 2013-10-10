# Shared client-server configuration
from pyamf import AMF3
object_encoding = AMF3
amf_host = 'localhost'
amf_port = 8000
policy_file = 'socket-policy.xml'
policy_port = 843

import logging
verbose = 'warning'
logging_levels = {'critical': logging.CRITICAL,
              'error': logging.ERROR,
              'warning': logging.WARNING,
              'info': logging.INFO,
              'debug': logging.DEBUG}
log_level = logging_levels[verbose]

