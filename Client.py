#https://realpython.com/python-sockets/

import socket
from sig import *
import sys

HOST = '127.0.0.1'
PORT = 42069
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    key = key_gen()
    pub_key = key.public_key().exportKey('DER')
    s.sendall(pub_key)

    m = "Message"
    dif = 1024 - len(m)
    if (dif > 0):
      for i in range(0, dif):
        m += ' '  #Add whitespace padding to end of message
    elif (dif < 0):
      print("Message is too long") #TODO later
    s.sendall(m.encode())

    sig = sign(m.strip(), key) #Strip off whitespace before signing
    s.sendall(sig)
