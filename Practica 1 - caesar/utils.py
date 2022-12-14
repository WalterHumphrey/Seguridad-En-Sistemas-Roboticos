#!/usr/bin/env python3

alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
sh_alphabet = {}

# New alphabet shifting from key
def dictionary(key):
    for i in range(0,26):
        letter = alphabet[i]
        sh_alphabet[letter] = alphabet[(i+key)%26]
    return sh_alphabet

# Encrypts with new alphabet
def caesar_encrypt(text,key):
    cipher = ''
    dictionary(key)
    for letter in text:
        if letter in sh_alphabet:
            letter = sh_alphabet[letter]
            cipher = cipher + letter
        elif letter == ' ' or letter == '\n':
            cipher = cipher + ' '
        else:
            cipher = cipher + ''
    return cipher