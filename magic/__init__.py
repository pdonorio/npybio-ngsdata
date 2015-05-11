# -*- coding: utf-8 -*-

# Constants
EMPTY_VALUE = '-'
DEBUG_LIMIT = 10
DEBUG_DATABASE = 'test'
DEBUG_TABLE = 'tester'
DEBUG_YAMLFILE = 'config.example'
YAML_EXTENSION = '.yml'

INPUT_DIR = 'input'
CONF_DIR = 'conf'
FILEDB_DIR = 'fsql'

# Logger
import logging
FORMAT = '%(asctime)-15s [%(name)-10s|%(levelname)-8s] %(message)s'
logging.basicConfig(level=logging.DEBUG, format=FORMAT)

def print_file(filename):
    """ Quickly read file """

    with open(filename, encoding='utf-8') as f:
        return f.read()
