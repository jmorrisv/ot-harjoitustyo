import os
import sqlite3

DATABASE_FILENAME =  "data.sqlite"

dirname = os.path.dirname(__file__)

DATABASE_FILE_PATH = os.path.join(dirname, DATABASE_FILENAME)

connection = sqlite3.connect(DATABASE_FILE_PATH)
connection.row_factory = sqlite3.Row

def get_database_connection():

    '''Hakee yhteyden tietokantaan.'''

    return connection
