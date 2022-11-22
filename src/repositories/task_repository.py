from config import TASKS_FILE_PATH
from task import Task
import csv
import datetime

class TaskRepository:

    def __init__(self, file_path=TASKS_FILE_PATH):

        '''Luokka, joka lukee tietoa tietokannasta
        ja tallentaa tietoa tietokantaan.'''

        self._file_path = file_path
        
    def fetch_task_list(self):

        "Palauttaa kaikki tehtävät listana"

        tasks = []

        with open(self._file_path) as file:
            csv_reader = csv.Reader(file, delimiter=',')

            for row in csv_reader:
                name = row[0]
                freq_d = int(row[1])
                freq_h = int(row[2])
                freq_m = int(row[3])
                freq_s = int(row[4])
                frequency = datetime.timedelta(days = freq_d, hours = freq_h, minutes = freq_m, seconds = freq_s)
                
                task = Task(name, frequency)
                tasks.append(task)

        return tasks

    def write_new_task(self, task: Task):

        '''Lisää uuden tehtävän tietokantaan.'''

        tasks = self.fetch_task_list()
        tasks.append(task)

        with open(self._file_path) as file:
            csv_writer = csv.writer(file)

            for task in tasks:
                csv_writer.writerow(task)
