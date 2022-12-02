from database_connection import get_database_connection

def drop_table(connection):

    '''Poistaa mahdollisen olemassaolevan tietokantataulun'''

    cursor = connection.cursor()

    cursor.execute('''DROP TABLE IF EXISTS tasks''')
    connection.commit()

def create_table(connection):

    '''Luo uuden taulun.'''

    cursor = connection.cursor()

    cursor.execute('''
                CREATE TABLE tasks(
                    name text primary key,
                    frequency_s integer,
                    end_time text
                    )
                ''')

    connection.commit()

def initialize_db():

    '''Alustaa tietokantataulun.'''

    connection = get_database_connection()

    drop_table(connection)
    create_table(connection)

if __name__ == "__main__":
    initialize_db()
