from database_connection import get_database_connection

def drop_table(connection):

    '''Poistaa mahdollisen olemassaolevan tietokantataulun'''

    cursor = connection.cursor()

    cursor.execute('''drop table if exists tasks;''')
    connection.commit()

def create_table(connection):

    '''Luo uuden taulun.'''

    cursor = connection.cursor()

    cursor.execute('''
                create table tasks(
                    name text primary key,
                    frequency_d integer,
                    frequency_h integer,
                    frequency_m integer
                    );
                ''')
        
    connection.commit()

def initialize_db():

    '''Alustaa tietokantataulun.'''

    connection = get_database_connection()
    
    drop_table(connection)
    create_table(connection)

if __name__ == "__main__":
    initialize_db()