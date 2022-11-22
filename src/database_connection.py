import os
import sqlite3
from config import DATABASE_FILENAME

dirname = os.path.dirname(__file__)

print(os.path.join(dirname, "..", "data", DATABASE_FILENAME))

connection = sqlite3.connect(os.path.join(dirname, "..", "data", DATABASE_FILENAME))
connection.row_factory = sqlite3.Row

def get_database_connection():
    
    '''Hakee yhteyden tietokantaan.'''

    return connection