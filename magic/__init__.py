# -*- coding: utf-8 -*-

####################################
# Constants
EMPTY_VALUE = '-'
DEBUG_LIMIT = 10
DEBUG_DATABASE = 'test'
DEBUG_TABLE = 'tester'
DEBUG_YAMLFILE = 'config_example'
YAML_COMMAND = '/opt/miniconda/bin/metl' # 'metl'
YAML_EXTENSION = '.yml'

INPUT_DIR = 'input'
FILEDB_DIR = 'fsql'
CONF_DIR = 'conf' # unused?

####################################
# Logger
import logging
FORMAT = '%(asctime)-15s [%(name)-10s|%(levelname)-8s] %(message)s'
logging.basicConfig(level=logging.DEBUG, format=FORMAT)

logger = logging.getLogger('magic')

####################################
def print_file(filename):
    """ Quickly read file """
    with open(filename, encoding='utf-8') as f:
        return f.read()

####################################
# Check dirs and create
import os

dirs = [INPUT_DIR, CONF_DIR, FILEDB_DIR]
for mydir in dirs:

    if not os.path.exists(mydir):
        try:
            os.makedirs(mydir)
            logger.info("Created directory " + mydir)
        except OSError:
            logger.error("Failed to create dir '" + mydir + "'")
