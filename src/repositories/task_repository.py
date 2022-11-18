import os

dirname = os.path.dirname(__file__)
data_file_path = os.path.join(dirname, "data.csv")

class TaskRepository:

    """Luokka joka vastaa tiedon tallentamisesta tietokantaan ja sen hakemisesta."""

    def __init__(self, file_path):

        """Luokan konstruktori.
        
        Args:
            file_path: Polku tiedostoon, johon luodut Taskit tallennetaan.
        """

        self._file_path = file_path

    def read(self):

        """"Lukee Taskit tiedostosta listaksi.
        Returns:
            Palauttaa Task-olioita sisältävän listan.
        """

        tasks = []

        with open(self._file_path) as file:
            for row in file:
                row = row.replace("\n", "")
                parts = row.split(";")

                task_id = parts[0]
                name = parts[1]
            
                tasks.append(name, task_id)
                
        return tasks

    def create(self, task):
        """Tallentaa uuden Taskin tiedostoon.

        Args:
            task: Tallennettava kohde Task-oliona.

        Returns:
            Tallennettu kohde Task-oliona.
        """

        tasks = self.read()
        tasks.append(task)
        self._write(tasks)
        return task

    def _write(self, tasks):
        with open(self._file_path, "w") as file:
            for task in tasks:
                row = f"{task.id};{task.name}"
                file.write(row+"\n")


task_repository = TaskRepository(data_file_path)
        