from tkinter import ttk, constants
from services.services import Services

class TasksView:

    '''Luokka, joka vastaa käyttöliittymän tehtävät näyttävästä näkymästä.'''

    def __init__(self, root, handle_new_task, services: Services):

        '''Luokan konstruktori, joka luo näkymän.
        
        Args:
            root: Ikkuna, johon näkymä avautuu.
            handle_new_task: Add new task -nappulaan liittyvä komento.
        '''

        self._root = root
        self._handle_new_task = handle_new_task
        self._frame = None
        self._services = services

        self._initialize()


    def pack(self):

        '''Näyttää kaikki näkymän komponentit ikkunassa.'''

        self._frame.pack(fill=constants.X)

    
    def destroy(self):

        '''Tuhoaa kaikki näkymän komponentit.'''

        self._frame.destroy()


    def _initialize(self):

        '''Määrittelee ikkunassa näytettävät komponentit.'''

        self._frame = ttk.Frame(master=self._root)
        label = ttk.Label(master=self._frame, text="Tasks:")
        add_new_task_button = ttk.Button(master=self._frame,
                                        text="Add new task",
                                        command=self._handle_new_task)

        label.grid(column=0, row=0)
        self._print_tasks()
        add_new_task_button.grid(column=0)


    def _print_tasks(self):
        tasks = self._services.get_all_tasks()
        i = 0
        for task in tasks:
            i += 1
            task_label = ttk.Label(master=self._frame, text=[task])
            task_button = ttk.Button(master=self._frame, text="Done", command=self._handle_done_button)
            task_label.grid(column=0, row=i)
            task_button.grid(column=1, row=i)


    def _handle_done_button(self, task_button):
        task_row = task_button.grid_info()['row']
