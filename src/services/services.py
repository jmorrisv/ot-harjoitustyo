from datetime import datetime, timedelta
from repositories.task_repository import TaskRepository
from entities.task import Task

class InvalidNameError(Exception):
    pass

class InvalidFrequencyError(Exception):
    pass

class Services:

    '''Luokka, joka vastaa sovelluksen toimintojen toteuttamisesta.'''

    def __init__(self):

        '''Luokan konstruktori, joka määrittelee tietokantaa käyttävän luokan.'''

        self.task_repository = TaskRepository()


    def _invalid_name(self, name):
        if len(name) <= 0 or name[-1] == "!":
            return False
        return True

    def _check_freq(self, days, seconds):
        if days != float(days) or seconds != float(seconds):
            return False
        if days < 0 or seconds < 0:
            return False
        if days == 0:
            if seconds == 0:
                return False
        return True


    def get_all_tasks(self):

        '''Hakee listan tallennetuista tehtävistä ja tiedon niiden likaisuudesta.

        Returns:
            Tehtävien nimet listana. Likaiset tehtävät ensin, perässään huutomerkki.
        '''

        task_list = []

        dirty_tasks_list = self.task_repository.fetch_dirty_tasks_in_list()
        clean_tasks_list = self.task_repository.fetch_clean_tasks_in_list()

        for task in dirty_tasks_list:
            task_list.append(task.name + " !")

        for task in clean_tasks_list:
            task_list.append(task.name)

        return task_list


    def add_new_task(self, name: str="No name", days: float=0, seconds: float=0):

        '''Luo uuden tehtävän ja lisää sen tietokantaan.

        Args:
            name: Tehtävän nimi merkkijonona.
            days: Tehtävän toistuvuus päivinä.
            seconds: Tehtävän toistuvuus sekunteina.

        Raises:
            InvalidNameError: Jos tehtävälle ei anneta nimeä, tai nimi loppuu merkkiin '!'
            InvalidFrequencyError: Jos toistuvuus on määritelty virheellisesti.
        '''

        if not self._invalid_name(name):
            raise InvalidNameError("Plese give your task a name. Last caharacter can't be '!'!")

        if not self._check_freq(days, seconds):
            raise InvalidFrequencyError(
                "Days or seconds must be numbers, at least one of them over 0."
                )

        task = Task(name, timedelta(days=days, seconds=seconds))

        self.task_repository.write_new_task(task)


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
