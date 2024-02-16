from tkinter import Tk
from gui import GUI
from converter import convert_to_md

def main():
    root = Tk()
    gui = GUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
