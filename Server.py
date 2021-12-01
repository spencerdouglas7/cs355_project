#https://realpython.com/python-sockets/
import socket
from sig import *

HOST = '127.0.0.1'
PORT = 42069


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        key = conn.recv(294) #public key is size 327
        key = RSA.importKey(key)
        print("have key")
        print(key.exportKey('PEM'))

        m = conn.recv(1024)
        m = m.decode()
        print("have message")
        m = m.strip()
        print(m)

        sig = conn.recv(256)
        print("Have sig")
        print("Signature is ", end='')
        print(verify(m, sig, key))

        while True:
            data = conn.recv(2048)
            if not data:
                break
            #print(data.decode())
