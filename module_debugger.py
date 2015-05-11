# -*- coding: utf-8 -*-

from magic.db import DBlite
DBlite("mydb")

from magic.config import ConfGen
conf = ConfGen()
conf.add_field("Chr")
conf.add_field("Start")
conf.add_field("End")

conf.tsv_source()
conf.dump_configuration()
# it works

from magic import print_file
print(print_file(conf.get_file()))

# import magic.shell
# print("Shell")
