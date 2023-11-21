import socket
import math
from DES.encode_image import encrypt_image, bitstring_to_bytes

print("Start transfer image in DES crypto")
cipher_text = encrypt_image()
data = ""
for block in cipher_text:
    data += block
data = bitstring_to_bytes(data)
serverMACAddress = 'f4:8c:50:af:0f:90'
port = 4
s = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
s.connect((serverMACAddress,port))
for i in range(math.ceil(len(data)/2048)):
    start = i*2048
    end = start + 2048
    block = data[start:end]
    s.send(block)
s.send(bytes("END", encoding="utf-8"))
s.close()