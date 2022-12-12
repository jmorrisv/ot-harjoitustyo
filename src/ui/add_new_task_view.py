from tkinter import ttk, constants
from services.services import Services
from ui.tasks_view import TasksView

class AddNewTaskView:

    '''Luokka, joka vastaa tehtävien lisäysnäkymästä.'''

    def __init__(self, root, handle_close, services: Services):
        
        '''Luokan konstruktori, joka luo näkymän.
        
        Args:
            root: Ikkuna, johon näkymä avautuu.
            handle_save: Save-nappulaan liittyvä komento.
            services: Sovelluksen toiminnallisuus.
        '''

        self._root = root
        self._handle_close = handle_close
        self._services = services
        self._frame = None

        self._initialize()

    def pack(self):

        '''Näyttää kaikki näkymän komponentit ikkunassa.'''

        self._frame.pack(fill=constants.X)

    
    def destroy(self):

        '''Tuhoaa kaikki näkymän komponentit.'''

        self._frame.destroy()


    def _initialize(self):

        self._frame = ttk.Frame(master=self._root)
        label = ttk.Label(master=self._frame, text="New task")

        name_label = ttk.Label(master=self._frame, text="Name")
        self.name_entry = ttk.Entry(master=self._frame)

        frequency_label = ttk.Label(master=self._frame, text="Frequency")
        seconds_label = ttk.Label(master=self._frame, text="seconds")
        self.seconds_entry = ttk.Entry(master=self._frame)

        save_button = ttk.Button(master=self._frame, text="Save", command=self._handle_save_button_click)
        close_button = ttk.Button(master=self._frame, text="Close", command=self._handle_close)

        label.grid(column=0, row=0, columnspan=3)
        name_label.grid(column=0, row=1)
        self.name_entry.grid(column=2, row=1)
        frequency_label.grid(column=0, row=2, columnspan=3)
        self.seconds_entry.grid(column=3, row=3)
        seconds_label.grid(column=3, row=4)
        save_button.grid(column=0, row=5, columnspan=3)
        close_button.grid(column=0, row=6, columnspan=3)


    def _handle_save_button_click(self):
        
        name = self.name_entry.get()
        seconds = float(self.seconds_entry.get())
        self._services.add_new_task(name, seconds)
