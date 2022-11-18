import unittest
from repositories.task_repository import task_repository
from entities.task import Task

class TestTaskRepository(unittest.TestCase):
    def setUp(self) -> None:
        self.task1 = Task("test 1")

    def test_create(self):
        task_repository.create(self.task1)
        tasks = task_repository.read()

        self.assertEqual(len(tasks), 1)