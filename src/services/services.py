from datetime import datetime, timedelta
from repositories.task_repository import TaskRepository
from entities.task import Task

class Services:
    def __init__(self):

        '''Luokka, joka vastaa sovelluksen toimintojen toteuttamisesta'''

        self.task_repository = TaskRepository()


    def get_all_tasks(self):

        '''Palauttaa listan tehtävistä. Likaiset tehtävät ensin, perässään huutomerkki.'''

        task_list = []

        dirty_tasks_list = self.task_repository.fetch_dirty_tasks_in_list()
        clean_tasks_list = self.task_repository.fetch_clean_tasks_in_list()

        for task in dirty_tasks_list:
            task_list.append(f"{task.name} !")

        for task in clean_tasks_list:
            task_list.append(f"{task.name}")

        return task_list


    def add_new_task(self, name: str, seconds: float):

        '''Lisää uuden tehtävän'''

        task = Task(name, timedelta(seconds=seconds))

        self.task_repository.write_new_task(task)


    def print_tasks(self):

        '''Tulostaa kaikki tehtävät'''

        print("Tasks:")
        for task in self.get_all_tasks():
            print(task)


    def mark_done(self, task_name: str):

        '''Merkitsee tehtävän siivotuksi ja aloittaa sen ajastimen alusta'''

        all_tasks = self.task_repository.fetch_all_tasks_in_list()
        time = datetime.now()

        for task in all_tasks:
            if task.name == task_name:
                self.task_repository.delete_task(task.name)

                task.timer.set(time)

                self.task_repository.write_new_task(task)
