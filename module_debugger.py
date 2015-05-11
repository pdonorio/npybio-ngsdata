# -*- coding: utf-8 -*-

from magic.db import DBlite
DBlite("mydb")

from magic.config import ConfGen
conf = ConfGen()
conf.add_field("Chr")
conf.add_field("Start")
conf.add_field("End")
print(conf.fields)

import magic.shell
print("Shell")
