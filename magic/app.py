# -*- coding: utf-8 -*-
""" App to parse easily biodata """

from magic.db import DBlite
from magic.shell import PyShell as bash

class App(object):
    """ Using the magic """

    def __init__(self, finput, config):
        super(App, self).__init__()
        self.finput = finput
        self.config = config

    def run(self):
        """ Running the pipeline """

        # Reading from a TSV
        self.config.tsv_source(self.finput)
        # Writing to a sqlite file db
        db = DBlite("mydb")
        self.config.dblite_target(db)
        # Write configuration
        self.config.dump_configuration()
        # Execute parser
        bash(self.config.get_command())
        # Return data
        return db.get_content()
