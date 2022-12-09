from services.services import Services
from ui.ui import UI
from tkinter import Tk

def main():

    '''Suorittaa ohjelman'''

    window = Tk()
    window.title("Siivousapuri")

    ui = UI(window)
    ui.start()

    window.mainloop()

    # services = Services()
    # services.print_tasks()

    # while True:

    #     print("Hello! What would you like to do?")
    #     print("To show task list type 1")
    #     print("To add new task type 2")
    #     print("To mark task done type 3")
    #     print("To exit type 4")

    #     command = int(input())

    #     if command == 4:
    #         break

    #     if command == 1:
    #         services.print_tasks()

    #     if command == 2:
    #         name = input("Task name: ")
    #         freq = int(input("Frequency in seconds: "))

    #         services.add_new_task(name, freq)

    #     if command == 3:
    #         name = input("Task name: ")

    #         services.mark_done(name)


if __name__ == "__main__":
    main()
