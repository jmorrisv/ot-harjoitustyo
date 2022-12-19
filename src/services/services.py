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


    def _check_name(self, name):
        if len(name) <= 0 or name[-1] == "!":
            return False
        task_name_list = []
        for task in self.task_repository.fetch_all_tasks_in_list():
            task_name_list.append(task.name)
        if name in task_name_list:
            return False
        return True


    def _check_freq(self, months, weeks, days, seconds):
        try:
            months = float(months)
            weeks = float(weeks)
            days = float(days)
            seconds = float(seconds)
        except ValueError:
            return False
        if months < 0 or weeks <0 or days < 0 or seconds < 0:
            return False
        if months == 0 and weeks == 0 and days == 0 and seconds == 0:
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


    def add_new_task(
        self, name: str="No name",months: float=0, weeks: float=0, days: float=0, seconds: float=0
        ):

        '''Luo uuden tehtävän ja lisää sen tietokantaan.

        Args:
            name: Tehtävän nimi merkkijonona.
            months: Tehtävän toistuvuus kuukausina.
            weeks: Tehtävän toistuvuus viikkoina.
            days: Tehtävän toistuvuus päivinä.
            seconds: Tehtävän toistuvuus sekunteina.

        Raises:
            InvalidNameError: Jos tehtävälle ei anneta nimeä,nimi on jo listalla
                tai se loppuu merkkiin '!'
            InvalidFrequencyError: Jos toistuvuus on määritelty virheellisesti.
        '''

        if not self._check_name(name):
            raise InvalidNameError(
                '''Please give your task a name. Check that it's not already on the list.
                Also note that the last character can't be '!'!'''
                )

        if not self._check_freq(months, weeks, days, seconds):
            raise InvalidFrequencyError(
                "Frequency values must be numbers, at least one of them over 0."
                )

        days += (months*30)+(weeks*7)

        task = Task(name, timedelta(days=days, seconds=seconds))

        self.task_repository.write_new_task(task)


    def show_task(self, task_name: str):

        '''Näyttää yksittäisen tehtävän tiedot.

        Args:
            task_name: Tehtävän nimi merkkijonona.

        Returns:
            Tehtävän nimi, toistuvuus, päättymisaika ja jäljellä oleva aika
            nelirivisenä merkkijonona.
        '''

        task_info = self.task_repository.fetch_one_task(task_name)
        name = task_info[0]
        frequency = task_info[1]
        end_time = task_info[2]
        remaining_time = end_time - datetime.now()
        if remaining_time <= timedelta(days=0, seconds=0):
            remaining_time = 0

        return f"{name}\n\nFrequency: {frequency}\n\nDue: {end_time}\n\nTime remaining: {remaining_time}"


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


    def delete_task(self, task_name: str):

        '''Poistaa tehtävän tietokannasta.

        Args:
            task_name: Tehtävän nimi merkkijonona.
        '''

        self.task_repository.delete_task_permanently(task_name)
