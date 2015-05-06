# -*- coding: utf-8 -*-

# Constants
EMPTY_VALUE = '-'
DEBUG_DATABASE = 'test'
DEBUG_TABLE = 'tester'
DEBUG_LIMIT = 10

INPUT_DIR = 'input'
CONF_DIR = 'conf'
FILEDB_DIR = 'fsql'

# Logger
import logging
FORMAT = '%(asctime)-15s [%(name)-10s|%(levelname)-8s] %(message)s'
logging.basicConfig(level=logging.DEBUG, format=FORMAT)