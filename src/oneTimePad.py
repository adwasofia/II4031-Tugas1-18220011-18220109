import tkinter as tk
from tkinter import *

class ClassOneTimePad():
    def oneTimePadScreen (self, screen):
        global screenOneTimePad
        screen.destroy()
        screenOneTimePad = tk.Tk()
        screenOneTimePad.title("<Title One-time Pad>")
        screenOneTimePad.geometry("1270x690")
        screenOneTimePad.configure(bg="#FFFFFF")

        screenOneTimePad.resizable(False, False)
        screenOneTimePad.mainloop()