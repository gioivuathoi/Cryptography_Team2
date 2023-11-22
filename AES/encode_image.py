from AES.AES import AES, encrypt, decrypt

def encrypt_image():
    # Part 1: Get input image and key:
    path = input(r'Enter path of Image : ')
    key = input('Enter Key for encryption of Image: ')
    print('The path of file : ', path)
    print('Key for encryption : ', key)

    # Part 2: Read image in binary mode and
    fin = open(path, 'rb')
    image = fin.read()
    fin.close()
    
    # Part 3: Create key and encrypt our image, the function encrypt_cbc will automatically pad the image
    # and divide it into 16-byte blocks,then encrypt each block and combine them into one cipher text
    print("Encrypting...")
    print(image[:10])
    cipher_text = encrypt(key, image)
    print("Done encryption!")
    return cipher_text

def decrypt_image(ct, key = None):
    # Part 1: Get key and generate key for decryption
    if key == None:
        key = input('Enter Key for encryption of Image: ')
    print('Key for decryption : ', key)
    # Part 2: Start Decryption
    image = decrypt(key, ct)
    # Part 3: Save the image
    print(image[:8])
    fin = open(r"save_image.jpg", 'wb')
    fin.write(image)
    fin.close()
    print("Done decryption!!")

# cipher_text = encrypt_image()
# decrypt_image(cipher_text)