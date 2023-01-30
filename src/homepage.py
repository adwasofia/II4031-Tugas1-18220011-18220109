import tkinter as tk
from tkinter import *
from vigenereCipher import ClassVigenereCipher
from extendedVigenereCipher import ClassExtendedVigenereCipher
from playfairCipher import ClassPlayfairCipher
from oneTimePad import ClassOneTimePad

class ClassHomepage():
    def HomepageScreen (self, screen):
        global screenHomepage
        screen.destroy()
        screenHomepage = tk.Tk()
        screenHomepage.title("<Title Homepage>")
        screenHomepage.geometry("1270x690")
        screenHomepage.configure(bg="#FFFFFF")

        vigenereCipherBut = tk.Button(screenHomepage,text="Vigenere Cipher",font=("helvetica",10,"bold"),bg="#DECBB7",command=self.toVigenereCipher).place(x=435,y=270,width=150,height=75)
        extendedVigenereCipherBut = tk.Button(screenHomepage,text="Extended Vigenere Cipher",font=("helvetica",10,"bold"),bg="#DECBB7",command=self.toExtendedVigenereCipher).place(x=685,y=270,width=150,height=75)
        playfairCipherBut = tk.Button(screenHomepage,text="Playfair Cipher",font=("helvetica",10,"bold"),bg="#DECBB7",command=self.toPlayfairCipher).place(x=435,y=400,width=150,height=75)
        oneTimePadBut = tk.Button(screenHomepage,text="One-time Pad",font=("helvetica",10,"bold"),bg="#DECBB7",command=self.toOneTimePad).place(x=685,y=400,width=150,height=75)

        screenHomepage.resizable(False, False)
        screenHomepage.mainloop()

    def toVigenereCipher (self):
        vigenereCipher_var = ClassVigenereCipher()
        vigenereCipher_var.vigenereCipherScreen(screenHomepage)
    
    def toExtendedVigenereCipher (self):
        extendedVigenereCipher_var = ClassExtendedVigenereCipher()
        extendedVigenereCipher_var.extendedVigenereCipherScreen(screenHomepage)
    
    def toPlayfairCipher (self):
        playfairCipher_var = ClassPlayfairCipher()
        playfairCipher_var.playfairCipherScreen(screenHomepage)
    
    def toOneTimePad (self):
        oneTimePad_var = ClassOneTimePad()
        oneTimePad_var.oneTimePadScreen(screenHomepage)
    
        
