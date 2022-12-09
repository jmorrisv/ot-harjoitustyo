import unittest
from repositories.task_repository import TaskRepository
from entities.task import Task
from datetime import timedelta
import initialize_db

class TestTaskRepository(unittest.TestCase):
    def setUp(self) -> None:
        self.task_repository = TaskRepository()
        self.task = Task("Tehtävä", timedelta(seconds=100))
        initialize_db.initialize_db()

    def test_create(self):

        "Testaa, että uusi tehtävä tulee listalle."
        
        self.task_repository.write_new_task(self.task)
        tasks = self.task_repository.fetch_all_tasks_in_list()

        self.assertEqual(len(tasks), 1)