import unittest
import time
from services.services import Services, InvalidNameError, InvalidFrequencyError
import initialize_db

class TestServices(unittest.TestCase):
    def setUp(self) -> None:
        initialize_db.initialize_db()
        self.services = Services()

        self.services.add_new_task("Tehtävä1", 1, 1, 1, 0)
        self.services.add_new_task("Tehtävä2", 0, 0, 0, 0.5)
        

    def test_add_new(self):
        list = self.services.get_all_tasks()
        self.assertEqual(len(list), 2)


    def test_add_no_name(self):
        with self.assertRaises(InvalidNameError):
            self.services.add_new_task("", 0, 0, 30, 0)

    
    def test_add_invalid_name(self):
        with self.assertRaises(InvalidNameError):
            self.services.add_new_task("Tehtävä!", 0, 0, 30, 0)


    def test_add_no_frequency(self):
        with self.assertRaises(InvalidFrequencyError):
            self.services.add_new_task("Tehtävä", 0, 0, 0, 0)

        
    def test_add_negative_frequency(self):
        with self.assertRaises(InvalidFrequencyError):
            self.services.add_new_task("Tehtävä", 0, 0, -1, 1)


    def test_add_string_as_frequency(self):
        with self.assertRaises(InvalidFrequencyError):
            self.services.add_new_task("Tehtävä", 0, 0, "nolla", 1)


    def test_dirty_tasks_right(self):
        time.sleep(0.5)
        list = self.services.get_all_tasks()
        dirty = list[0]

        self.assertEqual(dirty, "Tehtävä2 !")


    def test_clean_tasks_right(self):
        time.sleep(0.5)
        list = self.services.get_all_tasks()
        clean = list[1]

        self.assertEqual(clean, "Tehtävä1")
