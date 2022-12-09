from datetime import datetime, timedelta
from repositories.task_repository import TaskRepository
from entities.task import Task

class Services:

    '''Luokka, joka vastaa sovelluksen toimintojen toteuttamisesta.'''

    def __init__(self):

        '''Luokan konstruktori, joka määrittelee tietokannan.'''

        self.task_repository = TaskRepository()


    def get_all_tasks(self):

        '''Hakee listan tallennetuista tehtävistä ja tiedon niiden likaisuudesta.

        Returns:
            Tehtävien nimet listana. Likaiset tehtävät ensin, perässään huutomerkki.
        '''

        task_list = []

        dirty_tasks_list = self.task_repository.fetch_dirty_tasks_in_list()
        clean_tasks_list = self.task_repository.fetch_clean_tasks_in_list()

        for task in dirty_tasks_list:
            task_list.append(f"{task.name} !")

        for task in clean_tasks_list:
            task_list.append(f"{task.name}")

        return task_list


    def add_new_task(self, name: str, seconds: float):

        '''Luo uuden tehtävän ja lisää sen tietokantaan.

        Args:
            name: Tehtävän nimi merkkijonona.
            seconds: Tehtävän toistuvuus sekunteina.
        '''

        task = Task(name, timedelta(seconds=seconds))

        self.task_repository.write_new_task(task)


    def print_tasks(self):

        '''Tulostaa kaikki tehtävät.'''

        print("Tasks:")
        for task in self.get_all_tasks():
            print(task)


    def mark_done(self, task_name: str):

        '''Merkitsee tehtävän puhtaaksi ja aloittaa sen ajastimen alusta.

        Args:
            task_name: Tehtävän nimi merkkijonona.
        '''

        all_tasks = self.task_repository.fetch_all_tasks_in_list()
        time = datetime.now()

        for task in all_tasks:
            if task.name == task_name:
                self.task_repository.delete_task(task.name)

                task.timer.set(time)

                self.task_repository.write_new_task(task)
