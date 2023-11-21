import socket
from DES.encode_image import decrypt_image, binary

hostMACAddress = 'f4:8c:50:af:0f:90'# The MAC address of a Bluetooth adapter on the server. The server might have multiple Bluetooth adapters.
port = 4 # 3 is an arbitrary choice. However, it must match the port used by the client.
backlog = 1
size = 2048
s = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
s.bind((hostMACAddress,port))
s.listen(backlog)
cipher_text = bytearray()
try:
    client, address = s.accept()
    while 1:
        data = client.recv(size)
        if data and data != bytes("END", encoding="utf-8"):
            cipher_text += data
            client.send(data)
        elif data == bytes("END", encoding="utf-8"):
            break
    len_arr = int(len(cipher_text)/8)
    image_bin = []
    count = 0
    stop = 0
    for i in range(len_arr):
        arr = ""
        for byte in cipher_text[count:count+8]:
            arr += binary(byte)
        count += 8
        image_bin.append(arr)
        stop += 1
    decrypt_image(image_bin)
except:	
    print("Closing socket")	
    client.close()
    s.close()