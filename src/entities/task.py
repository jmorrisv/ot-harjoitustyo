import uuid

class Task:
    """Siivottavaa kohdetta kuvaava luokka
    
    Attributes:
        subject: Merkkijono, joka kuvaa siivottavaa kohdetta
        frequency_d: Kokonaisluku, joka kuvaa siivousvälin päiviä
        frequency_h: Kokonaisluku, joka kuvaa siivousvälin tunteja
        frequency_m: Kokonaisluku, joka kuvaa siivousvälin minuutteja
        dirty: Boolean-arvo, joka kuvaa kohteen likaisuutta
        task_id: Merkkijono, joka kuvaa kohteen id:tä
    """

    def __init__(self, subject, frequency_d=0, frequency_h=0, frequency_m=0, dirty=False, task_id=None):
        """Luokan konstruktori, joka luo uuden kohteen.

        Args:
            subject: Merkkijono, joka kuvaa siivottavaa kohdetta
            frequency_d:
                Vapaaehtoinen, oletusarvoltaan 0.
                Kokonaisluku, joka kuvaa siivousvälin päiviä
            frequency_h:
                Vapaaehtoinen, oletusarvoltaan 0.
                Kokonaisluku, joka kuvaa siivousvälin tunteja
            frequency_m:
                Vapaaehtoinen, oletusarvoltaan 0.
                Kokonaisluku, joka kuvaa siivousvälin minuutteja
            dirty:
                Vapaaehtoinen, oletusarvoltaan False.
                Boolean-arvo, joka kuvaa kohteen likaisuutta
            task_id:
                Vapaaehtoinen, oletusarvoltaan generoitu uuid.
                Merkkijono, joka kuvaa kohteen id:tä.
        """

        self.subject = subject
        self.frequency_d = frequency_d
        self.frequency_h = frequency_h
        self.frequency_m = frequency_m
        self.dirty = dirty
        self.task_id = task_id or str(uuid.uuid4())