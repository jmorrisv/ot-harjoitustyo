from tkinter import ttk, constants, messagebox
from services.services import Services, InvalidFrequencyError, InvalidNameError

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
        heading_font = ("courier new", 20)

        self._frame = ttk.Frame(master=self._root)
        label = ttk.Label(master=self._frame, text="New task", font=heading_font)

        name_label = ttk.Label(master=self._frame, text="Name")
        self.name_entry = ttk.Entry(master=self._frame)

        frequency_label = ttk.Label(master=self._frame, text="Frequency")
        months_label = ttk.Label(master=self._frame, text="months")
        self.months_entry = ttk.Entry(master=self._frame)
        weeks_label = ttk.Label(master=self._frame, text="weeks")
        self.weeks_entry = ttk.Entry(master=self._frame)
        days_label = ttk.Label(master=self._frame, text="days")
        self.days_entry = ttk.Entry(master=self._frame)
        seconds_label = ttk.Label(master=self._frame, text="seconds")
        self.seconds_entry = ttk.Entry(master=self._frame)

        save_button = ttk.Button(master=self._frame, text="Save", command=self._handle_save_button_click)
        close_button = ttk.Button(master=self._frame, text="Close", command=self._handle_close)

        label.grid(column=0, row=0, columnspan=2, padx=5, pady=10)
        name_label.grid(column=0, row=1, padx=1, pady=15)
        self.name_entry.grid(column=1, row=1, padx=1, pady=10)

        frequency_label.grid(column=0, row=2, columnspan=2, padx=5, pady=5)
        
        self.months_entry.grid(column=0, row=3, padx=5, pady=10)
        self.weeks_entry.grid(column=1, row=3, padx=5, pady=10)
        months_label.grid(column=0, row=4, padx=5, pady=1)
        weeks_label.grid(column=1, row=4, padx=5, pady=1)
        
        self.days_entry.grid(column=0, row=5, padx=5, pady=10)
        self.seconds_entry.grid(column=1, row=5, padx=5, pady=10)
        days_label.grid(column=0, row=6, padx=5, pady=1)
        seconds_label.grid(column=1, row=6, padx=5, pady=1)

        save_button.grid(column=0, row=7, columnspan=4, padx=5)
        close_button.grid(column=0, row=8, columnspan=4, padx=5)


    def _handle_save_button_click(self):
        
        name = self.name_entry.get()
        try:
            months = float(self.months_entry.get())
            weeks = float(self.weeks_entry.get())
            days = float(self.days_entry.get())
            seconds = float(self.seconds_entry.get())
        except ValueError:
            messagebox.showinfo(
                message="Please give me a frequency! Values must be numbers.")
            return

        try:
            self._services.add_new_task(name, months, weeks, days, seconds)
        except InvalidNameError:
            messagebox.showinfo(
            message='''Please give your task a name. Check that it's not already on the list. Also note that the last character can't be "!"''')
        except InvalidFrequencyError:
            messagebox.showinfo(
                message="Frequency values must be numbers, at least one of them over 0.")

        self.destroy()
        self._initialize()
        self.pack()
