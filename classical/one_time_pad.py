import string
import random
# NOTE: This code work with alphabet and special character from 32 to 126 in ascii code.
# Alphabet in plaintext wil be encrypted by alphabet, special character wil be encrypted by both alphabet
# and special character. Length of keyword equals to plaintext.
def encryption(plain_text):

    cipher_text = ""
    # first, let's create a randome keyword which have the same length with plain text
    length = len(plain_text)
    randomLetters = random.choices(population=string.ascii_letters, k=length)
    # now, we will extract the position of those characters in the keyword
    ids = []
    for letter in randomLetters:
        if letter.islower():
            id = ord(letter) - 97
        elif letter.isupper():
            id = ord(letter) - 65
        ids.append(id)

    # Next, we will create the cipher text based on the keyword
    for id, character in enumerate(plain_text):
        # Check if the character is lower type
        if character.islower():
            key = (ord(character) - 97)%26 + ids[id]
            if key > 25:
                key = key - 25
                cipher_text += chr(96 + key)
            else:
                cipher_text += chr(97 + key)
        # check if the character is upper type
        elif character.isupper():
            key = (ord(character) - 65)%26 + ids[id]
            if key > 25:
                key = key-25
                cipher_text += chr(64+key)
            else:
                cipher_text += chr(65+key)
        # check if the character is special character (not alphabet)
        else:
            key = (ord(character) - 32)%95 + ids[id]
            if key > 94:
                key = key - 94
                cipher_text += chr(31 + key)
            else:
                cipher_text += chr(32 + key)
    return {"plain_text": plain_text, "keyword": randomLetters, "cipher_text": cipher_text}
    # print(cipher_text)
        

def decryption(keyword, cipher_text):
    #From the keyword, we will extract the shift number, which is the position of character in alphabet
    ids = []
    plain_text = ""
    for letter in keyword:
        if letter.islower():
            id = ord(letter) - 97
        elif letter.isupper():
            id = ord(letter) - 65
        ids.append(id)
    for id, character in enumerate(cipher_text):
        if character.islower():
            key = (ord(character) - 97)%26 - ids[id]
            if key < 0:
                plain_text += chr(123 + key)
            else:
                plain_text += chr(97 + key)
        elif character.isupper():
            key = (ord(character) - 65)%26 - ids[id]
            if key < 0:
                plain_text += chr(91+key)
            else:
                plain_text += chr(65+key)
        else:
            key = (ord(character) - 32)%95 - ids[id]
            if key < 0:
                plain_text += chr(127 + key)
            else:
                plain_text += chr(32 + key)
    return plain_text


# Let's test our functions
# plain_text = "I love you, Babe!!!!"
# enc = encryption(plain_text)
# print(enc)
# keyword = enc["keyword"]
# cipher_text = enc["cipher_text"]
# print(decryption(keyword, cipher_text))