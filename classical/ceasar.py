
# NOTE: NOT DESIGN FOR VIETNAMESE YET. This code work with alphabet and special character (not alphabet) 
# from 32 to 126 in ascii code. Alphabet in plaintext wil be encrypted by alphabet, special character 
# wil be encrypted by both alphabet and special characters.


def encryption(plain_text, key):
    cipher_text = ""
    for pc in plain_text:
        # Check if the character is lower case
        if pc.islower():
            cc = (ord(pc) - 97)%26 + key
            if cc > 25:
                cc = cc - 25
                cipher_text += chr(96 + cc)
            else:
                cipher_text += chr(97 + cc)
        # check if the character is upper case
        elif pc.isupper():
            cc = (ord(pc) - 65)%26 + key
            if cc > 25:
                cc = cc - 25
                cipher_text += chr(64+cc)
            else:
                cipher_text += chr(65+cc)
        # check if character is not alphabet
        else:
            cc = (ord(pc) - 32)%95 + key
            if cc > 94:
                cc = cc - 94
                cipher_text += chr(31 + cc)
            else:
                cipher_text += chr(32 + cc)

    return {"plain_text": plain_text, "key": key, "cipher_text": cipher_text}


def decryption(key, cipher_text):
    plain_text = ""
    for cc in cipher_text:
        if cc.islower():
            dc = (ord(cc)-97)%26-key
            if dc < 0:
                plain_text += chr(123 + dc)
            else:
                plain_text += chr(97 + dc)
        elif cc.isupper():
            dc = (ord(cc)-65)%26-key
            if dc < 0:
                plain_text += chr(91+dc)
            else:
                plain_text += chr(65+dc)
        else:
            dc = (ord(cc) - 32)%95 - key
            if dc < 0:
                plain_text += chr(127 + dc)
            else:
                plain_text += chr(32 + dc)
    return plain_text

# Let's test our functions
# plain_text = "I love you, Babe!!!"
# enc = encryption(plain_text, 4)
# print(enc)
# key = enc["key"]
# cipher_text = enc["cipher_text"]
# print(decryption(key, cipher_text))
