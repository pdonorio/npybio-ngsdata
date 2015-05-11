# -*- coding: utf-8 -*-
"""
Generator for YAML file.
Needed from mETL package to parse the data.
"""

import yaml
from magic import logging, YAML_EXTENSION, DEBUG_YAMLFILE

logger = logging.getLogger('configurator')

class ConfGen(object):
    """ A class to recover data and generate the config file """

    data = {}
    fields = []
    yaml_fname = DEBUG_YAMLFILE

    def __init__(self, filename=None):
        super(ConfGen, self).__init__()
        if filename != None:
            self.yaml_fname = filename

        logger.debug("Configuration in '" + self.yaml_fname + "'")

    def add_field(self, fieldname, mytype='String', label=None):
        if label == None:
            label = fieldname
        self.fields.append({ \
            'map': fieldname, 'name': fieldname, 'type': mytype})
        logger.debug("Adding field '" + fieldname + "'")

    def tsv_source(self, fields=None):
        """ Complete the request configuration via static data """

        if fields == None:
            fields = self.fields

        self.data['source'] = { \
            'resource': self.yaml_fname, \
            'fields': fields, \
            'source': 'TSV', 'headerRow': 0, 'skipRows': 1}

    def dblite_target(self, sqlclass):
        """ Static configuration to output to sqllite """
        self.data['target'] = {
            'type': 'Database', 'createTable': 'true', 'replaceTable': 'true', 'truncateTable': 'true',
            'table': sqlclass.get_table(), \
            'url': 'sqlite:///' + sqlclass.get_dbfile()}

    def dump_configuration(self):
        """ Dumps the configuration array into the needed file """

        with open(self.yaml_fname + YAML_EXTENSION, 'w') as outfile:
            outfile.write(yaml.dump(self.data, \
                #encoding=('utf-8'), \
                default_flow_style=False))

