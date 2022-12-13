from tkinter import Tk
from ui.ui import UI

def main():

    '''Suorittaa ohjelman'''

    window = Tk()
    window.title("Siivousapuri")
    window.geometry("400x400")

    ui = UI(window)
    ui.start()

    window.mainloop()


if __name__ == "__main__":
    main()
