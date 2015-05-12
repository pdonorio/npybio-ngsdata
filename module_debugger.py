# -*- coding: utf-8 -*-
""" Using a module to parse data """

# Init the magic
from magic.config import conf
from magic.app import App

# Configuration
input_file = "input/test/test_annovar.hg19.tsv"
conf.add_field("Chr")
conf.add_field("Start")
conf.add_field("End")

# Do it
data = App(input_file, conf).run()
print(data)
