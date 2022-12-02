import datetime

class Timer:
    def __init__(self, frequency=datetime.timedelta):

        '''Ajan laskemisesta huolehtiva luokka'''

        self.freq = frequency


    def set(self, start_time=datetime.datetime):

        '''Asettaa tai nollaa ajastimen'''

        end_time = start_time + self.freq

        return end_time


    def timer(self, end_time=datetime.datetime):

        '''Tarkistaa, onko ajastimen aika kulunut ja palauttaa tiedon siitä, onko kohde puhdas'''

        now = datetime.datetime.now()

        if end_time <= now:
            return False

        return True
