from tkinter import ttk, constants, messagebox
from services.services import Services, InvalidFrequencyError, InvalidNameError
from ui.tasks_view import TasksView

class AddNewTaskView:

    '''Luokka, joka vastaa tehtävien lisäysnäkymästä.'''

    def __init__(self, root, handle_close, services: Services):
        
        '''Luokan konstruktori, joka luo näkymän.
        
        Args:
            root: Ikkuna, johon näkymä avautuu.
            handle_close: Close-nappulaan liittyvä komento.
            services: Sovelluksen toiminnallisuus.
        '''

        self._root = root
        self._handle_close = handle_close
        self._services = services
        self._frame = None

        self._initialize()

    def pack(self):

        '''Näyttää kaikki näkymän komponentit ikkunassa.'''

        self._frame.pack(fill=constants.BOTH)

    
    def destroy(self):

        '''Tuhoaa kaikki näkymän komponentit.'''

        self._frame.destroy()


    def _initialize(self):

        self._frame = ttk.Frame(master=self._root)
        label = ttk.Label(master=self._frame, text="New task", font=("Arial", 15))

        name_label = ttk.Label(master=self._frame, text="Name")
        self.name_entry = ttk.Entry(master=self._frame)

        frequency_label = ttk.Label(master=self._frame, text="Frequency")
        days_label = ttk.Label(master=self._frame, text="days")
        self.days_entry = ttk.Entry(master=self._frame)
        seconds_label = ttk.Label(master=self._frame, text="seconds")
        self.seconds_entry = ttk.Entry(master=self._frame)

        save_button = ttk.Button(master=self._frame, text="Save", command=self._handle_save_button_click)
        close_button = ttk.Button(master=self._frame, text="Close", command=self._handle_close)

        label.grid(column=0, row=0, columnspan=2, padx=5, pady=5)
        name_label.grid(column=0, row=1, padx=1, pady=10)
        self.name_entry.grid(column=1, row=1, padx=1, pady=10)

        frequency_label.grid(column=0, row=2, columnspan=3, padx=5, pady=5)
        self.days_entry.grid(column=0, row=3, padx=5, pady=5)
        self.seconds_entry.grid(column=1, row=3, padx=5, pady=5)
        days_label.grid(column=0, row=4, padx=5, pady=1)
        seconds_label.grid(column=1, row=4, padx=5, pady=1)

        save_button.grid(column=0, row=5, columnspan=2, padx=5, pady=10)
        close_button.grid(column=0, row=6, columnspan=2, padx=5, pady=5)


    def _handle_save_button_click(self):
        
        name = self.name_entry.get()
        try:
            days = float(self.days_entry.get())
            seconds = float(self.seconds_entry.get())
        except ValueError:
            messagebox.showinfo(
                message="Please give me a frequency! Days and seconds must be numbers.")

        try:
            self._services.add_new_task(name, days, seconds)
        except InvalidNameError:
            messagebox.showinfo(message="Please give me a name. Last caharacter can't be '!'")
        except InvalidFrequencyError:
            messagebox.showinfo(message="Days and seconds must be numbers, at least one of them over 0.")

        self.destroy()
        self._initialize()
        self.pack()
