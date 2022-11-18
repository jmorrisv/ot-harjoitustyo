class TaskRepository:

    """Luokka joka vastaa tiedon tallentamisesta tietokantaan ja sen hakemisesta."""

    def __init__(self, file_path):

        """Luokan konstruktori.
        
        Args:
            file_path: Polku tiedostoon, johon luodut Taskit tallennetaan.
        """

        self._file_path = file_path

    def find_tasks(self):
        
        """Palauttaa kaikki tallennetut Taskit
        
        Returns:
            Palauttaa Task-olioita sisältävän listan.
        """

        return self._read

    def _read(self):
        tasks = []
        self._ensure_file_exists()

        with open(self._file_path, encoding="utf-8") as file:
            for row in file:
                row = row.replace("\n", "")
                parts = row.split(";")

                task_id = parts[0]
                name = parts[1]
                frequency = parts[2]
                




        