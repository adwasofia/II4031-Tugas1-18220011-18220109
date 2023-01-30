import tkinter as tk
from tkinter import *

class ClassPlayfairCipher():
    def playfairCipherScreen (self, screen):
        global screenPlayfairCipher
        screen.destroy()
        screenPlayfairCipher = tk.Tk()
        screenPlayfairCipher.title("<Title Playfair Cipher>")
        screenPlayfairCipher.geometry("1270x690")
        screenPlayfairCipher.configure(bg="#FFFFFF")

        screenPlayfairCipher.resizable(False, False)
        screenPlayfairCipher.mainloop()