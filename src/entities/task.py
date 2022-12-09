import datetime
from entities.timer import Timer

class Task:

    '''Tehtävistä vastaava luokka.
    
    Attributes:
        name: Tehtävän nimi.
        frequency: Tehtävän toistuvuus.
    '''

    def __init__(self, name: str, frequency: datetime.timedelta):

        '''Luokan konstruktori, joka luo uuden tehtävän.
        
        Args:
            name: Tehtävän nimi.
            frequency: Tehtävän toistuvuus.
        '''

        self.name = name
        self.frequency = frequency
        self.timer = Timer(frequency)

    def __str__(self) -> str:

        ''' Esittää tehtävän tiedot merkkijonona.
        
        Returns:
            Merkkijono, joka kertoo tehtävän nimen ja toistuvuuden sekunneissa.
        '''

        return f"name: {self.name}, seconds: {self.frequency.seconds}"
        