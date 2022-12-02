import datetime
from entities.task import Task
import database_connection

conn = database_connection.get_database_connection()

class TaskRepository:

    def __init__(self, connection=conn):

        '''Luokka, joka lukee tietoa tietokannasta
        ja tallentaa tietoa tietokantaan.'''

        self.connection = connection


    def write_new_task(self, task: Task):

        '''Lisää uuden tehtävän tietokantaan.'''

        name = task.name
        freq_s = task.frequency.seconds
        start_time = datetime.datetime.now()
        end_time = task.timer.set(start_time)

        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO tasks (name, frequency_s, end_time) VALUES (?, ?, ?)", (name, freq_s, end_time))


    def fetch_all_tasks_in_list(self):

        "Palauttaa kaikki tehtävät listana"

        tasks = []

        cursor = self.connection.cursor()
        rows = cursor.execute("SELECT * FROM tasks").fetchall()

        for row in rows:
            name = row[0]
            freq_s = float(row[1])

            task = Task(name, datetime.timedelta(seconds=freq_s))
            tasks.append(task)

        return tasks


    def fetch_dirty_tasks_in_list(self):

        '''Palauttaa listan tehtävistä, joiden aika on kulunut umpeen'''

        dirty_tasks = []

        cursor = self.connection.cursor()
        rows = cursor.execute("SELECT * FROM tasks").fetchall()

        for row in rows:
            name = row[0]
            freq_s = float(row[1])
            end_time = datetime.datetime.strptime(row[2], '%Y-%m-%d %H:%M:%S.%f')

            task = Task(name, datetime.timedelta(seconds=freq_s))
            clean_or_not = task.timer.timer(end_time)

            if not clean_or_not:
                dirty_tasks.append(task)

        return dirty_tasks


    def fetch_clean_tasks_in_list(self):

        '''Palauttaa listan tehtävistä, joiden aika ei ole kulunut umpeen'''

        clean_tasks = []

        cursor = self.connection.cursor()
        rows = cursor.execute("SELECT * FROM tasks").fetchall()

        for row in rows:
            name = row[0]
            freq_s = float(row[1])
            end_time = datetime.datetime.strptime(row[2], '%Y-%m-%d %H:%M:%S.%f')

            task = Task(name, datetime.timedelta(seconds=freq_s))
            clean_or_not = task.timer.timer(end_time)

            if clean_or_not:
                clean_tasks.append(task)

        return clean_tasks


    def delete_task(self, task_name: str):

        '''Poistaa tehtävän tietokannasta'''

        cursor = self.connection.cursor()
        cursor.execute("DELETE FROM tasks WHERE name = ?", (task_name, ))
