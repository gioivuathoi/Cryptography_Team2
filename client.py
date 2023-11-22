import socket
import math
import DES.encode_image as des
import AES.encode_image as aes
print("Type 1/2/3 to choose type of encryption you want to use: ")
print("1: DES")
print("2: AES")
print("3: RC4")
encrypt_type = int(input("I choose:"))
if encrypt_type == 1:
    print("Start transfer image in DES crypto")
    cipher_text = des.encrypt_image()
    data = ""
    # Combine 64-bit blocks into one block
    for block in cipher_text:
        data += block
    data = des.bitstring_to_bytes(data)
elif encrypt_type == 2:
    print("Start transfer image in AES crypto")
    data = aes.encrypt_image()
elif encrypt_type == 3:
    pass

serverMACAddress = 'f4:8c:50:af:0f:90'
port = 4
s = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
s.connect((serverMACAddress,port))
# Devide data into many 2048-byte packages and transfer them
for i in range(math.ceil(len(data)/2048)):
    start = i*2048
    end = start + 2048
    block = data[start:end]
    s.send(block)
# Send the final signal to annouce finish the transfering
s.send(bytes("END", encoding="utf-8"))
s.close()