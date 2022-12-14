from tkinter import ttk, constants, messagebox
from services.services import Services

class TasksView:

    '''Luokka, joka vastaa käyttöliittymän tehtävät näyttävästä näkymästä.'''

    def __init__(self, root, handle_new_task, services: Services):

        '''Luokan konstruktori, joka luo näkymän.
        
        Args:
            root: Ikkuna, johon näkymä avautuu.
            handle_new_task: Add new task -nappulaan liittyvä komento.
            services: Sovelluksen toiminnallisuus.
        '''

        self._root = root
        self._handle_new_task = handle_new_task
        self._frame = None
        self._services = services

        self._initialize()


    def pack(self):

        '''Näyttää kaikki näkymän komponentit ikkunassa.'''

        self._frame.pack(fill=constants.BOTH, padx=10, pady=10)

    
    def destroy(self):

        '''Tuhoaa kaikki näkymän komponentit.'''

        self._frame.destroy()


    def _initialize(self):

        '''Määrittelee ikkunassa näytettävät komponentit.'''

        heading_font = ("courier new", 20)
        
        self._frame = ttk.Frame(master=self._root)
        label = ttk.Label(
            master=self._frame,
            text="Tasks:",
            font=heading_font,
            )
        add_new_task_button = ttk.Button(
            master=self._frame,
            text="Add new task",
            command=self._handle_new_task,
            )

        label.grid(column=0, row=0, padx=5, pady=10)
        self._print_tasks()
        add_new_task_button.grid(column=0, padx=5, pady=10)


    def _print_tasks(self):
        tasks = self._services.get_all_tasks()
        i = 0
        for task in tasks:
            i += 1
            ttk.Label(master=self._frame, text=task
                ).grid(column=0, row=i, padx=5, pady=5)
            ttk.Button(
                master=self._frame,
                text="Clean",
                command=lambda s=task: self._handle_done_button(s),
                ).grid(column=1, row=i)
            ttk.Button(
                master=self._frame,
                text="Info",
                command=lambda s=task: self._handle_info_button(s),
                ).grid(column=2, row=i)
            ttk.Button(
                master=self._frame,
                text="Delete",
                command=lambda s=task: self._handle_delete_button(s)
                ).grid(column=3, row=i)


    def _handle_done_button(self, task):
        task = task.replace(" !", "")
        self._services.mark_done(task)

        self.destroy()
        self._initialize()
        self.pack()


    def _handle_info_button(self, task):
        task = task.replace(" !", "")
        task_info = self._services.show_task(task)

        messagebox.showinfo(message=task_info)


    def _handle_delete_button(self, task):
        task = task.replace(" !", "")
        self._services.delete_task(task)

        self.destroy()
        self._initialize()
        self.pack()
