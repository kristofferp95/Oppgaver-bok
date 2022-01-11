from tkinter import *

class ForegroundColors:
    def __init__(self):
        window = Tk()
        window.title("Set colors")

        self.var = StringVar()
        combobox = OptionMenu(window, self.var, "red", "green", "yellow", "purple", "orange", "blue", command = self.processSelection)
        combobox.pack(fill=BOTH)

        
        window.mainloop()
    
    def processSelection(self):
        return

ForegroundColors()