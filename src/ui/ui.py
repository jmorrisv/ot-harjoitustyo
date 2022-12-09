from tkinter import Tk
from ui.tasks_view import TasksView
from ui.add_new_task_view import AddNewTaskView
from services.services import Services

class UI:

    '''Sovelluksen käyttöliittymästä vastaava luokka.'''

    def __init__(self, root):

        '''Luokan konstruktori.
        
        Args:
            root: Tk()-ikkuna, johon käyttöliittymän näkymät avautuvat.'''

        self._root = root
        self._current_view = None
        self.services = Services()


    def start(self):

        '''Käynnistää sovelluksen.'''

        self._show_tasks_view()

    
    def _clear_window(self):
        if self._current_view:
            self._current_view.destroy()

        self._current_view = None


    def _show_tasks_view(self):

        '''Näyttää tehtävälistanäkymän.'''

        self._current_view = TasksView(self._root, self._handle_add_new_task, self.services)

        self._current_view.pack()


    def _show_add_new_task_view(self):

        '''Näyttää tehtävän lisäys -näkymän.'''

        self._current_view = AddNewTaskView(self._root, self._handle_close, self.services)

        self._current_view.pack()

    
    def _handle_add_new_task(self):

        '''Siirtyy tehtävän lisäys -näkymään.'''

        self._clear_window()
        self._show_add_new_task_view()


    def _handle_close(self):

        '''Tallentaa tehtävän ja siirtyy takaisin tehtävälistanäkymään.'''

        self._clear_window()
        self._show_tasks_view()
