import datetime
from entities.task import Task
import database_connection

conn = database_connection.get_database_connection()

class TaskRepository:

    '''Luokka, joka lukee tietoa tietokannasta ja tallentaa tietoa tietokantaan.

    Attributes:
        connection: Valmiiksi määritelty yhteys sovelluksen tietokantaan.
    '''

    def __init__(self, connection=conn):

        '''Luokan konstruktori, joka luo tietokantayhteyden.

        Args:
            connection: Valmiiksi määritelty yhteys sovelluksen tietokantaan.
        '''

        self.connection = connection


    def write_new_task(self, task: Task):

        '''Lisää uuden tehtävän tietokantaan.

        Args:
            task: Lisättävä tehtävä Task-oliona.
        '''

        name = task.name
        freq_d = task.frequency.days
        freq_s = task.frequency.seconds
        start_time = datetime.datetime.now()
        end_time = task.timer.set(start_time)

        cursor = self.connection.cursor()
        cursor.execute(
            "INSERT INTO tasks (name, frequency_d, frequency_s, end_time) VALUES (?, ?, ?, ?)",
            (name, freq_d, freq_s, end_time, ))
        self.connection.commit()


    def fetch_all_tasks_in_list(self):

        '''Hakee tallennetut tehtävät listana.

        Returns:
            Kaikki tehtävät listana.
        '''

        tasks = []

        cursor = self.connection.cursor()
        rows = cursor.execute("SELECT * FROM tasks").fetchall()

        for row in rows:
            name = row[0]
            freq_d = float(row[1])
            freq_s = float(row[2])

            task = Task(name, datetime.timedelta(days=freq_d, seconds=freq_s))
            tasks.append(task)

        return tasks


    def fetch_dirty_tasks_in_list(self):

        '''Hakee listan likaisista kohteista.

        Returns:
            Tehtävät, joiden aika on kulunut umpeen, listana.
        '''

        dirty_tasks = []

        cursor = self.connection.cursor()
        rows = cursor.execute("SELECT * FROM tasks").fetchall()

        for row in rows:
            name = row[0]
            freq_d = float(row[1])
            freq_s = float(row[2])
            end_time = datetime.datetime.strptime(row[3], '%Y-%m-%d %H:%M:%S.%f')

            task = Task(name, datetime.timedelta(days=freq_d, seconds=freq_s))
            clean_or_not = task.timer.timer(end_time)

            if not clean_or_not:
                dirty_tasks.append(task)

        return dirty_tasks


    def fetch_clean_tasks_in_list(self):

        '''Hakee listan likaisista kohteista.

        Returns:
            Tehtävät, joissa on kyselyhetkellä aikaa jäljellä, listana.
        '''

        clean_tasks = []

        cursor = self.connection.cursor()
        rows = cursor.execute("SELECT * FROM tasks").fetchall()

        for row in rows:
            name = row[0]
            freq_d = float(row[1])
            freq_s = float(row[2])
            end_time = datetime.datetime.strptime(row[3], '%Y-%m-%d %H:%M:%S.%f')


            task = Task(name, datetime.timedelta(days=freq_d, seconds=freq_s))
            clean_or_not = task.timer.timer(end_time)

            if clean_or_not:
                clean_tasks.append(task)

        return clean_tasks


    def delete_task(self, task_name: str):

        '''Poistaa tehtävän tietokannasta.

        Args:
            task_name: Tehtävän nimi merkkijonona.
        '''

        cursor = self.connection.cursor()
        cursor.execute("DELETE FROM tasks WHERE name = ?", (task_name, ))
