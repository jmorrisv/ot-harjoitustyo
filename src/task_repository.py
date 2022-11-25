from task import Task
import database_connection
import datetime
import initialize_db

connection = database_connection.get_database_connection()

class TaskRepository:

    def __init__(self, connection=connection):

        '''Luokka, joka lukee tietoa tietokannasta
        ja tallentaa tietoa tietokantaan.'''

        self.connection = connection
        

    def write_new_task(self, task: Task):

        '''Lisää uuden tehtävän tietokantaan.'''

        name = task.name
        freq_s = task.frequency.seconds

        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO tasks (name, frequency_s) VALUES (?, ?)", (name, freq_s))


    def fetch_all_tasks_in_list(self):

        "Palauttaa kaikki tehtävät listana"

        tasks = []

        cursor = self.connection.cursor()
        rows = cursor.execute("SELECT * FROM tasks").fetchall()

        for row in rows:
            name = row[0]
            print(name)
            freq_s = float(row[1])
            print(freq_s)
            
            task = Task(name, datetime.timedelta(days=freq_s))
            tasks.append(task)
            print(str(task))

        return tasks

task_repository = TaskRepository()
initialize_db.initialize_db()
task = Task("hello world", datetime.timedelta(seconds=100))
task_repository.write_new_task(task)
print(task_repository.fetch_all_tasks_in_list())