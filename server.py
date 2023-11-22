import socket
import DES.encode_image as des
import AES.encode_image as aes
hostMACAddress = 'f4:8c:50:af:0f:90'# The MAC address of a Bluetooth adapter on the server. The server might have multiple Bluetooth adapters.
port = 4 # 3 is an arbitrary choice. However, it must match the port used by the client.
backlog = 1
size = 2048
s = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
s.bind((hostMACAddress,port))
s.listen(backlog)
cipher_text = bytes()
try:
    client, address = s.accept()
    while 1:
        data = client.recv(size)
        if data and data != bytes("END", encoding="utf-8"):
            cipher_text += data
            client.send(data)
        elif data == bytes("END", encoding="utf-8"):
            break
    print("Type 1/2/3 to choose type of encryption you want to use: ")
    print("1: DES")
    print("2: AES")
    print("3: RC4")
    encrypt_type = int(input("I choose:"))
    if encrypt_type == 1:
        print("Starting decrypt data wwith DES crypto")
        len_arr = int(len(cipher_text)/8)
        image_bin = []
        count = 0
        stop = 0
        for i in range(len_arr):
            arr = ""
            for byte in cipher_text[count:count+8]:
                arr += des.binary(byte)
            count += 8
            image_bin.append(arr)
            stop += 1
        des.decrypt_image(image_bin)
    elif encrypt_type == 2:
        print("Starting decrypt data with AES crypto")
        aes.decrypt_image(cipher_text)
    elif encrypt_type == 3:
        pass
except:	
    print("Closing socket")	
    client.close()
    s.close()