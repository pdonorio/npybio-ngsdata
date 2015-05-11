# -*- coding: utf-8 -*-
"""
A database class to save and access parsed data
"""

import abc, os
import sqlite3 as lite
from magic import logging, DEBUG_DATABASE, DEBUG_TABLE, FILEDB_DIR

logger = logging.getLogger('database')

# Check dir and create
if not os.path.exists(FILEDB_DIR):
    try:
        os.makedirs(FILEDB_DIR)
    except OSError:
        logger.error("Failed to create dir '" + FILEDB_DIR + "'")

class db(object):
    """Generic db abstraction"""

    dbname = DEBUG_DATABASE
    tablename = DEBUG_TABLE
    connection = None

    def __init__(self, database):
        # Init
        super(db, self).__init__()
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

class dblite(db):
    """ Implementation of database via sqlite3 library """

    cursor = None
    sqlfile = 'noname'

    def __init__(self, database):
        # Parent constructor
        super(dblite, self).__init__(database)

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

    def get_content(self):
        # Query
        query = "SELECT * FROM " + self.tablename
        self.cursor.execute(query)
        for i in self.cursor.fetchall():
            #DEBUG
            print(i)
