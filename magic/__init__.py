# -*- coding: utf-8 -*-

# Constants
EMPTY_VALUE = '-'
DEBUG_DATABASE = 'testing'
DEBUG_TABLE = 'testing'
DEBUG_LIMIT = 10

# Logger
import logging
FORMAT = '%(asctime)-15s [%(name)-10s|%(levelname)-8s] %(message)s'
logging.basicConfig(level=logging.DEBUG, format=FORMAT)
