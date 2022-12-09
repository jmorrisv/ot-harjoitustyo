import unittest
import datetime
import time
from entities.timer import Timer

class TestTimer(unittest.TestCase):
    def setUp(self):

        ''' Asettaa testiajastimen, jossa on aikaa 1 sekunti. '''

        self.timer = Timer(datetime.timedelta(seconds=1))


    def test_set(self):

        '''Testaa, että ajastin asettaa päättymisajan oikein.'''

        end_time = self.timer.set(datetime.datetime(2022, 12, 1, 12, 23))

        self.assertEqual(end_time, datetime.datetime(2022, 12, 1, 12, 23, 1))


    def test_timer_dirty(self):

        '''Testaa, että ajastin palauttaa oikein likaisuuden.'''

        now = datetime.datetime.now()
        set = self.timer.set(now)
        time.sleep(1.1)
        
        self.assertEqual(self.timer.timer(set), False)

    
    def test_timer_clean(self):

        '''Testaa, että ajastin palauttaa oikein puhtauden.'''

        now = datetime.datetime.now()
        set = self.timer.set(now)
        time.sleep(0.5)
        
        self.assertEqual(self.timer.timer(set), True)
