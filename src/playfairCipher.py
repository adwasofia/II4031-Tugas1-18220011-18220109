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

        tk.Label(screenPlayfairCipher, text= "Playfair Cipher", font= ("Helvetica", 14, "bold"), bg= "#FFFFFF", fg= "black").place(x= 635, y= 150, anchor= "center")

        def backHome():
            from homepage import ClassHomepage
            ClassHomepage().HomepageScreen(screenPlayfairCipher)
        def lakukanEnkripsi():
            self.lakukanCipher(TRUE)
        def lakukanDekripsi():
            self.lakukanCipher(FALSE)

        # Entry box pesan yang akan dienkripsi atau didekripsi
        global inputPesanTeks
        global pesanTeks
        pesanTeks= StringVar()
        tk.Label(screenPlayfairCipher, text= "Masukkan Pesan Teks:", font= ("Helvetica", 12, "bold"), bg= "#FFFFFF", fg= "black").place(x= 300, y= 250, anchor= "w")
        inputPesanTeks= tk.Entry(screenPlayfairCipher, textvariable= pesanTeks, font= ("Helvetica", 12), bg= "#DECBB7", fg= "black")
        inputPesanTeks.place(x= 500, y= 250, width= 470, height= 30, anchor= "w")

        # Entry box key untuk enkripsi/dekripsi
        global inputKey
        global key
        key= StringVar()
        tk.Label(screenPlayfairCipher, text= "Masukkan Key:", font= ("Helvetica", 12, "bold"), bg= "#FFFFFF", fg= "black").place(x= 300, y= 300, anchor= "w")
        inputKey= tk.Entry(screenPlayfairCipher, textvariable= key, font= ("Helvetica", 12), bg= "#DECBB7", fg= "black")
        inputKey.place(x= 500, y= 300, width= 470, height= 30, anchor= "w")

        # Button untuk melakukan enkripsi
        btn= tk.Button(screenPlayfairCipher, text= "Lakukan Enkripsi", font= ("Helvetica", 12, "bold"), bg= "#DECBB7", width= 20, height= 1, command= lakukanEnkripsi)
        btn.place(x= 625, y= 400, anchor= "e")

        # Button untuk melakukan dekripsi
        btn= tk.Button(screenPlayfairCipher, text= "Lakukan Dekripsi", font= ("Helvetica", 12, "bold"), bg= "#DECBB7", width= 20, height= 1, command= lakukanDekripsi)
        btn.place(x= 645, y= 400, anchor= "w")

        # Button tambahan
        btnhome= tk.Button(screenPlayfairCipher, text= "Home", font= ("Helvetica", 12, "bold"), bg= "#DECBB7", width= 20, height= 1, command= backHome)
        btnhome.place(x= 300, y= 150, anchor= "w", width=100)
        btnrefresh= tk.Button(screenPlayfairCipher, text= "Refresh", font= ("Helvetica", 12, "bold"), bg= "#DECBB7", width= 20, height= 1, command= self.refreshPage)
        btnrefresh.place(x= 970, y= 150, anchor= "e",width=100)

        screenPlayfairCipher.resizable(False, False)
        screenPlayfairCipher.mainloop()

    # Fungsi cipher
    def lakukanCipher(self, status):
        def createKey(key):
            array_key = []
            for character in key:
                if character.isalpha() not in array_key and character != "J":
                    array_key.append(character)
                for i in range(26):
                    if chr(i + 65) != "J" and chr(i + 65) not in array_key:
                        array_key.append(chr(i + 65))
            
            key_bujursangkar = [[array_key[i*5+j] for j in range(5)] for i in range(5)]
            return key_bujursangkar

        def getCharacter(character, key_bujursangkar):
            for i in range(len(key_bujursangkar)):
                for j in range(len(key_bujursangkar[i])):
                    if key_bujursangkar[i][j] == character:
                        return i,j

        def makeBigram(text):
            text = "".join([char for char in text if char.isalpha()])
            text = text.replace("J", "I")
            text_bigram = []
            char_bigram = ""
            for i in range(len(text)):
                if text[i] == char_bigram:
                    char_bigram += "X"
                    text_bigram.append(char_bigram)
                    char_bigram = text[i]
                else:
                    char_bigram += text[i]
                
                if len(char_bigram) == 2:
                    text_bigram.append(char_bigram)
                    char_bigram = ""
                elif (i == len(text) - 1) and (len(char_bigram) == 1):
                    char_bigram += "X"
                    text_bigram.append(char_bigram)
            return text_bigram

        def doPlayfairCipher(text_bigram, status, key_bujursangkar):
            baris_1, kolom_1 = getCharacter(text_bigram[0], key_bujursangkar)
            baris_2, kolom_2 = getCharacter(text_bigram[1], key_bujursangkar)

            hasil = ""

            if baris_1 == baris_2:
                if status:
                    hasil += (key_bujursangkar[baris_1][(kolom_1 + 1) % len(key_bujursangkar[baris_1])])
                    hasil += (key_bujursangkar[baris_2][(kolom_2 + 1) % len(key_bujursangkar[baris_2])])
                else:
                    hasil += (key_bujursangkar[baris_1][(kolom_1 - 1) % len(key_bujursangkar[baris_1])])
                    hasil += (key_bujursangkar[baris_2][(kolom_2 - 1) % len(key_bujursangkar[baris_2])])

            elif kolom_1 == kolom_2:
                if status:
                    hasil += (key_bujursangkar[(baris_1 + 1) % len(key_bujursangkar)][kolom_1])
                    hasil += (key_bujursangkar[(baris_2 + 1) % len(key_bujursangkar)][kolom_2])
                else:
                    hasil += (key_bujursangkar[(baris_1 - 1) % len(key_bujursangkar)][kolom_1])
                    hasil += (key_bujursangkar[(baris_2 - 1) % len(key_bujursangkar)][kolom_2])

            else:
                hasil += (key_bujursangkar[baris_1][kolom_2] + key_bujursangkar[baris_2][kolom_1])

            return hasil

        def encryptPlayfair(key, text):
            plain_text = makeBigram(text.upper())
            key_bujursangkar = createKey(key.upper())
            cipher_text = ""

            for bigram in plain_text:
                cipher_text += doPlayfairCipher(bigram, True, key_bujursangkar)
            return cipher_text

        def decryptPlayfair(key, text):
            cipher_text = makeBigram(text.upper())
            key_bujursangkar = createKey(key.upper())
            plain_text = ""

            for bigram in cipher_text:
                plain_text += doPlayfairCipher(bigram, False, key_bujursangkar)
            return plain_text

        pesan = pesanTeks.get()
        kunci = key.get()

        # Melakukan enkripsi atau dekripsi
        hasil = ""
        if status:
            hasil = encryptPlayfair(kunci, pesan)
        else:
            hasil = decryptPlayfair(kunci, pesan)
        
        # Menampilkan hasil
        tk.Label(screenPlayfairCipher, text= hasil.upper(), font= ("Helvetica", 12, "bold"), bg= "#FFFFFF", fg= "black").place(x= 500, y= 350, anchor= "w")

    def refreshPage(self):
        self.playfairCipherScreen(screenPlayfairCipher)
