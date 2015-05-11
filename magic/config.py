# -*- coding: utf-8 -*-
"""
Generator for YAML file.
Needed from mETL package to parse the data.
"""

from magic import logging, YAML_EXTENSION, DEBUG_YAMLFILE
# UHM
#import yaml

logger = logging.getLogger('configurator')

class ConfGen(object):
    """ A class to recover data and generate the config file """

    data = {}
    yaml_fname = DEBUG_YAMLFILE

    def __init__(self, filename=None):
        super(ConfGen, self).__init__()
        if filename != None:
            self.yaml_fname = filename

        logger.debug("Configuration in '" + self.yaml_fname + "'")

    def tsv_source(self, fields):
        """ Complete the request configuration via static data """
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

        # Check errors?

        with open(self.yaml_fname + YAML_EXTENSION, 'w') as outfile:
            outfile.write(yaml.dump(self.data, default_flow_style=False))

# #!head {yfile} -n 3
# out = !! wc -l {yfile}
# print "Your configuration inside file '" + yfile + "' reaches " + out.s.split(" ")[0] + " lines"
