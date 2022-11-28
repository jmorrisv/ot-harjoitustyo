from repositories.task_repository import TaskRepository

class Services:
    def __init__(self):

        '''Luokka, joka vastaa sovelluksen toimintojen toteuttamisesta'''

        self.task_repository = TaskRepository()
        self.task_list = self.task_repository.fetch_all_tasks_in_list()

    def get_all_tasks(self):

        '''Tulostaa listan tehtävistä'''

        print(self.task_list)
