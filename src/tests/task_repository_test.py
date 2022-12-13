import unittest
from repositories.task_repository import TaskRepository
from entities.task import Task
from datetime import timedelta
import initialize_db

class TestTaskRepository(unittest.TestCase):
    def setUp(self) -> None:
        initialize_db.initialize_db()
        self.task_repository = TaskRepository()
        self.task = Task("Tehtävä", timedelta(seconds=100))
        

    def test_create(self):

        "Testaa, että uusi tehtävä tulee listalle."
        
        self.task_repository.write_new_task(self.task)
        tasks = self.task_repository.fetch_all_tasks_in_list()

        self.assertEqual(len(tasks), 1)

    def test_name_and_seconds_right(self):

        "Testaa, että tehtävän nimi ja sekunnit ovat oikein."

        self.assertEqual(str(self.task), "name: Tehtävä, seconds: 100")

    def test_clean_tasks(self):

        "Testaa, että puhtaiden kohteiden lista tulee oikein."

        self.task_repository.write_new_task(self.task)
        list = self.task_repository.fetch_clean_tasks_in_list()

        self.assertEqual(len(list), 1)

    def test_dirty_tasks(self):

        "Testaa, että likaisten kohteiden lista tulee oikein."

        self.task_repository.write_new_task(Task("Tehtävä2", timedelta(seconds=0)))
        list = self.task_repository.fetch_dirty_tasks_in_list()

        self.assertEqual(len(list), 1)
