import tkinter as tk
from tkinter import *

class ClassExtendedVigenereCipher():
    def extendedVigenereCipherScreen (self, screen):
        global screenExtendedVigenereCipher
        screen.destroy()
        screenExtendedVigenereCipher = tk.Tk()
        screenExtendedVigenereCipher.title("<Title Extended Vigenere Cipher>")
        screenExtendedVigenereCipher.geometry("1270x690")
        screenExtendedVigenereCipher.configure(bg="#FFFFFF")
    
        # Entry box Pesan Teks yang akan Dienkripsi
        global inputPesanTeks
        global pesanTeks
        pesanTeks= StringVar()
        tk.Label(screenExtendedVigenereCipher, text= 'Masukkan Pesan Teks:', font= ('Helvetica', 12, 'bold'), bg= '#FFFFFF', fg= 'black').place(x= 300, y= 250, anchor= 'w')
        inputPesanTeks= tk.Entry(screenExtendedVigenereCipher, textvariable= pesanTeks, font= ('Helvetica', 12), bg= '#DECBB7', fg= 'black')
        inputPesanTeks.place(x= 635, y= 250, width= 300, height= 30, anchor= 'center')

        # Entry box Key yang akan digunakan untuk Mengenkripsi
        global inputKey
        global key
        key= StringVar()
        tk.Label(screenExtendedVigenereCipher, text= 'Masukkan Key:', font= ('Helvetica', 12, 'bold'), bg= '#FFFFFF', fg= 'black').place(x= 300, y= 300, anchor= 'w')
        inputKey= tk.Entry(screenExtendedVigenereCipher, textvariable= key, font= ('Helvetica', 12), bg= '#DECBB7', fg= 'black')
        inputKey.place(x= 635, y= 300, width= 300, height= 30, anchor= 'center')

        # Button untuk Melanjutkan ke Proses Enkripsi
        btn= tk.Button(screenExtendedVigenereCipher, text= 'Lakukan Enkripsi', font= ('Helvetica', 12, 'bold'), bg= '#DECBB7', width= 20, height= 1, command= self.lakukanEnkripsiExtendedVigenere)
        btn.place(x= 635, y= 350, anchor= 'center')

        screenExtendedVigenereCipher.resizable(False, False)
        screenExtendedVigenereCipher.mainloop()
    
    def lakukanEnkripsiExtendedVigenere (self):
        global encryptedLetter
        global encryptedPesan
        pesan = pesanTeks.get().replace(" ", "")
        kunci = key.get()
        while (len(kunci) < len(pesan)):
            kunci += kunci
        encryptedPesan = ''
        i = 0
        for huruf in pesan:
            encryptedLetter = (ord(pesan[i]) + ord(kunci[i])) % 256
            encryptedLetter = str(chr(encryptedLetter))
            encryptedPesan += encryptedLetter
            i += 1
        tk.Label(screenExtendedVigenereCipher, text= 'Hasil Enkripsi:', font= ('Helvetica', 12, 'bold'), bg= '#FFFFFF', fg= 'black').place(x= 300, y= 450, anchor= 'w')
        tk.Label(screenExtendedVigenereCipher, text= encryptedPesan.upper(), font= ('Helvetica', 12, 'bold'), bg= '#FFFFFF', fg= 'black').place(x= 635, y= 450, anchor= 'center')