import tkinter as tk
from vigenereCipher import ClassVigenereCipher


class ClassHomepage():
    def HomepageScreen (self, screen):
        global screenHomepage
        screen.destroy()
        screenHomepage = tk.Tk()
        screenHomepage.title("<Title Homepage>")
        screenHomepage.geometry("1270x690")
        screenHomepage.configure(bg="#FFFFFF")

        vigenereCipherBut = tk.Button(screenHomepage,text="Vigenere Cipher",font=("helvetica",10,"bold"),bg="#DECBB7",command=self.toVigenereCipher).place(x=560,y=270,width=150,height=75)

        screenHomepage.resizable(False, False)
        screenHomepage.mainloop()
    
    def toVigenereCipher (self):
        vigenereCipher_var = ClassVigenereCipher()
        vigenereCipher_var.vigenereCipherScreen(screenHomepage)

    #def toExtendedVigenereCipher (self):
        
    #def toPlayfairCipher (self):
        
    #def toOneTimePad (self):
        
