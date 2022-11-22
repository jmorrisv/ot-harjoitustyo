import datetime

class Task:

    def __init__(self, name: str, frequency: datetime.timedelta):

        '''Task-olioista vastaava luokka'''

        self.name = name
        self.frequency = frequency