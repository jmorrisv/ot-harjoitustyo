import unittest
from repositories.task_repository import TaskRepository
from entities.task import Task

class TestTaskRepository(unittest.TestCase):
    def setUp(self) -> None:
        self.task_repository = TaskRepository
        self.task = Task("Tehtävä", 0, 0, 0, 30)

    def test_create(self):
        self.task_repository.write_new_task(self.task)
        tasks = self.task_repository.read()

        self.assertEqual(len(tasks), 1)