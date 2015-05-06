# -*- coding: utf-8 -*-
"""
A database class to save and access parsed data
"""

import abc
import sqlite3 as lite
from magic import logging

logger = logging.getLogger('database')

class db(object):
    """Generic db abstraction"""

    dbname = 'test'
    connection = None

    def __init__(self, database=None):
        # Init
        super(db, self).__init__()
        # Arguments
        if database != None:
            self.dbname = database
        self.dbname = database

        ## Loggin tests...
        # logger.info("Test")
        # print logger
        # print "Connect?"

    @abc.abstractmethod
    def connect(self):
        """ Abstract connection """
        return

class dblite(db):
    """ Implementation of database via sqlite3 library """

    cursor = None
    sqlfile = 'noname'

    def __init__(self, database):
        # Parent constructor
        super(dblite, self).__init__(database)

    def connect(self):

        # Operations
        self.sqlfile = self.dbname + ".sql"

        # connect
        try:
            self.connection = lite.connect(self.sqlfile)
            self.cursor = self.connection.cursor()
        except lite.Error, e:
            raise BaseException("No sql lite connection", e)
        finally:
            print "Connected"
