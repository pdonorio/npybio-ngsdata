# -*- coding: utf-8 -*-

""" Using a module to parse data """

debug = True

###################################
# Creating the configuration
from magic.config import ConfGen
conf = ConfGen()

###################################
# Add fields
conf.add_field("Chr")
conf.add_field("Start")
conf.add_field("End")

###################################
# Reading from a TSV
input_file = "input/test/test_annovar.hg19.tsv"
conf.tsv_source(input_file)

###################################
# Writing to a sqlite file db
from magic.db import DBlite
db = DBlite("mydb")
conf.dblite_target(db)
# Write configuration
cfile = conf.dump_configuration()

###################################
# Check configuration
if debug:
    from magic import print_file
    print(print_file(cfile))

###################################
# Execute parser
from magic.shell import PyShell as bash
#bash("ls")
bash(conf.get_command())

###################################
# Query
print(db.get_content()[:4])
