import datetime
from entities.timer import Timer

class Task:

    def __init__(self, name: str, frequency: datetime.timedelta):

        '''Task-olioista vastaava luokka'''

        self.name = name
        self.frequency = frequency
        self.timer = Timer(frequency)

    def __str__(self) -> str:
        return f"name: {self.name}, seconds: {self.frequency.seconds}"
        