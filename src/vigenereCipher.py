import tkinter as tk
from tkinter import *

class ClassVigenereCipher():
    def vigenereCipherScreen (self, screen):
        global screenVigenereCipher
        screen.destroy()
        screenVigenereCipher = tk.Tk()
        screenVigenereCipher.title("<Title Vigenere Cipher>")
        screenVigenereCipher.geometry("1270x690")
        screenVigenereCipher.configure(bg="#FFFFFF")
    
        # Entry box Pesan Teks yang akan Dienkripsi
        global inputPesanTeks
        global pesanTeks
        pesanTeks= StringVar()
        tk.Label(screenVigenereCipher, text= 'Masukkan Pesan Teks:', font= ('Helvetica', 12, 'bold'), bg= '#FFFFFF', fg= 'black').place(x= 300, y= 250, anchor= 'w')
        inputPesanTeks= tk.Entry(screenVigenereCipher, textvariable= pesanTeks, font= ('Helvetica', 12), bg= '#DECBB7', fg= 'black')
        inputPesanTeks.place(x= 635, y= 250, width= 300, height= 30, anchor= 'center')

        # Entry box Key yang akan digunakan untuk Mengenkripsi
        global inputKey
        global key
        key= StringVar()
        tk.Label(screenVigenereCipher, text= 'Masukkan Key:', font= ('Helvetica', 12, 'bold'), bg= '#FFFFFF', fg= 'black').place(x= 300, y= 300, anchor= 'w')
        inputKey= tk.Entry(screenVigenereCipher, textvariable= key, font= ('Helvetica', 12), bg= '#DECBB7', fg= 'black')
        inputKey.place(x= 635, y= 300, width= 300, height= 30, anchor= 'center')

        # Button untuk Melanjutkan ke Proses Enkripsi
        btn= tk.Button(screenVigenereCipher, text= 'Lakukan Enkripsi', font= ('Helvetica', 12, 'bold'), bg= '#DECBB7', width= 20, height= 1, command= self.lakukanEnkripsi)
        btn.place(x= 635, y= 350, anchor= 'center')

        screenVigenereCipher.resizable(False, False)
        screenVigenereCipher.mainloop()
    
    def lakukanEnkripsi (self):
        global encryptedLetter
        global encryptedPesan
        pesan = pesanTeks.get().replace(" ", "")
        kunci = key.get()
        while (len(kunci) < len(pesan)):
            kunci += kunci
        encryptedPesan = ''
        i = 0
        for huruf in pesan:
            encryptedLetter = ((ord(pesan[i])-97) + (ord(kunci[i])-97)) % 26
            encryptedLetter = str(chr(encryptedLetter+97))
            encryptedPesan += encryptedLetter
            i += 1
        tk.Label(screenVigenereCipher, text= 'Hasil Enkripsi:', font= ('Helvetica', 12, 'bold'), bg= '#FFFFFF', fg= 'black').place(x= 300, y= 450, anchor= 'w')
        tk.Label(screenVigenereCipher, text= encryptedPesan.upper(), font= ('Helvetica', 12, 'bold'), bg= '#FFFFFF', fg= 'black').place(x= 635, y= 450, anchor= 'center')
    

