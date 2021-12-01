#https://realpython.com/python-sockets/

import socket

HOST = '127.0.0.1'
PORT = 42069
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    m = "Message"
    s.sendall(m.encode())
    data = s.recv(1024)

print('Received', repr(data))
