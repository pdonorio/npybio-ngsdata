# -*- coding: utf-8 -*-
""" Executor of shell commands """

import six, re, subprocess as shell
from magic import logging

logger = logging.getLogger('shell')


class PyShell(object):
    """A handler for command processing via unix bash/shell"""

    cmd = []

    def __init__(self, command):
        super(PyShell, self).__init__()
        self.add_command(command)
        self.execute()

    def add_command(self, command):
        """ Split a command to be executed via python subprocess """

        if not isinstance(command, six.string_types):
            raise BaseException("Command must be string. Error with: "+ command)

        for piece in re.compile("\s+").split(command):
            self.cmd.append(piece)

    def execute(self, cmd=None):
        """ Test """

        # Proc via current shell
        if cmd == None:
            cmd = self.cmd

        cmdstring = " ".join(cmd)
        logger.info("Executing:\t" + cmdstring)

        proc = shell.Popen(cmd, \
            #cwd=MAIN_DIR, \
            stdout=shell.PIPE, stderr=shell.PIPE)
        out, err = proc.communicate()
        out = out.decode(encoding='UTF-8')

        # Handle output
        if proc.returncode == 0:
            if out != None and out != "":
                logger.info("Comm output: " + out.__str__())
        else:
            msg = "Could not process shell command:\n" + cmdstring + "\n" + \
                ". Error: " + err.__str__()
            logger.critical(msg)
            raise BaseException(msg)

