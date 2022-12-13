import datetime

class Timer:

    ''' Ajan laskemisesta huolehtiva luokka.

    Attributes:
        frequency: Tehtävän toistuvuus.
    '''

    def __init__(self, frequency=datetime.timedelta):

        '''Luokan konstruktori, joka luo uuden ajastimen.

        Args:
            frequency: Tehtävän toistuvuus.
        '''

        self.freq = frequency


    def set(self, start_time=datetime.datetime):

        '''Asettaa tai nollaa ajastimen.

        Args:
            start_time: Ajastimen aloitusaika.

        Returns:
            Ajastimen loppumisaika.
        '''

        end_time = start_time + self.freq

        return end_time


    def timer(self, end_time=datetime.datetime):

        '''Tarkistaa, onko ajastimen aika kulunut.

        Args:
            end_time: Ajastimen loppumisaika.

        Returns:
            False, jos ajastin on kulunut loppuun, muussa tapauksessa True.
        '''

        now = datetime.datetime.now()

        if end_time <= now:
            return False

        return True
