import unittest
from datetime import timedelta
from services.services import Services
from entities.task import Task
import initialize_db

class TestServices(unittest.TestCase):
    def setUp(self) -> None:
        initialize_db.initialize_db()
        self.services = Services()

        self.services.add_new_task("Tehtävä1", 30, 0)
        self.services.add_new_task("Tehtävä2", 0, 30)
        

    def test_add_new(self):

        "Testaa, että uusi tehtävä tulee listalle."

        list = self.services.get_all_tasks()
        self.assertEqual(len(list), 2)


    def dirty_tasks_right(self):

        '''Testaa, että likaiset tehtävät ovat listalla ensin, perässään !'''

        list = self.services.get_all_tasks()
        dirty = list[0]

        self.assertEqual(dirty, "Tehtävä2 !")


    def clean_tasks_right(self):

        '''Testaa, että puhtaat tehtävät ovat listalla viimeisenä.'''

        list = self.services.get_all_tasks()
        clean = list[1]

        self.assertEqual(clean, "Tehtävä1")
