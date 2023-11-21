from help_function import  *
from enc_dec import  *

def pad(data): 
    return data + b"\x00"*(8-len(data)%8)  
def binary(num):
    bin_num = bin(num)[2:]
    if len(bin_num) < 8:
        bin_num = "0"*(8-len(bin_num)) + bin_num
    return bin_num
def bitstring_to_bytes(s):
    v = int(s, 2)
    b = bytearray()
    while v:
        b.append(v & 0xff)
        v >>= 8
    return b[::-1]

def encrypt_image():

    # Part 1: Get input image and key:
    path = input(r'Enter path of Image : ')
    key = input('Enter Key for encryption of Image : ')
    print('The path of file : ', path)
    print('Key for encryption : ', key)

    # Part 2: Read image in binary mode and
    fin = open(path, 'rb')
    image = fin.read()
    fin.close()

    #Part 3: Padding if image is not diviable to 8 bytes (64 bits)
    if len(image) % 8 != 0:
        image = pad(image)

    # Part 4: Get blocks of 64 bits of image which will be input of DES
    len_arr = int(len(image)/8)
    image_bin = []
    count = 0
    stop = 0
    for i in range(len_arr):
        arr = ""
        for byte in image[count:count+8]:
            arr += binary(byte)
        count += 8
        image_bin.append(arr)
        stop += 1
    
    # Part 5: Create key and encrypt our image 64bit-block by 64bit-block
    rk, rkb = key_generation(key)
    cipher_text = []
    print("Encrypting...")
    print(image_bin[:3])
    for block in image_bin:
        cipher_text.append(encrypt(block,rkb, rk, input_bin= True))
    print("Done encryption!")
    return cipher_text

def decrypt_image(ct, key = None):

    #Part 1: Get key and generate key for decryption
    if key == None:
        key = input('Enter Key for encryption of Image : ')
    print('Key for decryption : ', key)
    pt = []
    plain_text = ""
    rk, rkb = key_generation(key)
    rkb_rev = rkb[::-1]
    rk_rev = rk[::-1]

    #Part 2: Start Decruption
    print("Decrypting...")
    for block in ct:
        pt.append(decrypt(block, rkb_rev, rk_rev,to_hex=False))

    for block in pt:
        plain_text += block
    
#Part 3: Convert bit string to bytes and save the image
    image = bitstring_to_bytes(plain_text)
    print(image[:8])
    fin = open(r"F:\Subjects\Lý thuyết mật mã\encryption\DES\save_image.jpg", 'wb')
#  writing encrypted data in image
    fin.write(image)
    fin.close()
    print("Done decryption!!")
    return plain_text

cipher_text = encrypt_image()
decrypt_image(cipher_text, key = "AABB09182736CCDD")

# print(bitstring_to_bytes("0000000001111000000000000000000011111111110110110000000001000011"))