import tkinter as tk
from tkinter import *

def createKey(key):
    array_key = []
    for character in key:
        if character.isalpha() not in array_key and character != 'J':
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

key = input()
text = input()
print(encryptPlayfair(key, text))
