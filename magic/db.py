# -*- coding: utf-8 -*-
"""
A database class to save and access parsed data
"""

import abc
import sqlite3 as lite
from magic import logging, DEBUG_DATABASE, DEBUG_TABLE, FILEDB_DIR

logger = logging.getLogger('database')

class DB(object):
    """Generic db abstraction"""

    dbname = DEBUG_DATABASE
    tablename = DEBUG_TABLE
    connection = None

    def __init__(self, database):
        # Init
        super(DB, self).__init__()
        # Arguments
        if database != None:
            self.dbname = database
        # Db connection
        logger.debug("Db istance")
        self.connect()

    @abc.abstractmethod
    def connect(self):
        """ Abstract connection """
        return

    def get_table(self):
        return self.tablename

class DBlite(DB):
    """ Implementation of database via sqlite3 library """

    cursor = None
    sqlfile = 'noname'

    def __init__(self, database):
        # Parent constructor
        super(DBlite, self).__init__(database)

    def connect(self):

        # Operations
        self.sqlfile = FILEDB_DIR + '/' + self.dbname + '.db'

        # connect
        try:
            self.connection = lite.connect(self.sqlfile)
            logger.info("Db file: " + self.sqlfile)
            self.cursor = self.connection.cursor()
        except lite.Error as e:
            raise BaseException("No sql lite connection", e)
        finally:
            logger.info("Connected: " + self.connection.__repr__())

    def get_dbfile(self):
        return self.sqlfile

    def get_content(self):
        # Query
        query = "SELECT * FROM " + self.tablename
        self.cursor.execute(query)
        data = []
        for row in self.cursor.fetchall():
            data.append(row)

        return data