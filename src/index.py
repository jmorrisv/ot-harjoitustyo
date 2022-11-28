from datetime import timedelta
from entities.task import Task
from repositories.task_repository import TaskRepository

def main():

    '''Suorittaa ohjelman'''

    task_repository = TaskRepository()
    task = Task("hello world", timedelta(seconds=100))
    task_repository.write_new_task(task)
    print(task_repository.fetch_all_tasks_in_list())


if __name__ == "__main__":
    main()
