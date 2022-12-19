from tkinter import Tk
from ui.ui import UI

def main():

    '''Suorittaa ohjelman.'''

    window = Tk()
    window.title("Siivousapuri")
    window.geometry("500x500")

    u_i = UI(window)
    u_i.start()

    window.mainloop()


if __name__ == "__main__":
    main()
