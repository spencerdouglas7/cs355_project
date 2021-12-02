#https://realpython.com/python-sockets/

import socket
from sig import *
from cipher import *
from prg import *

HOST = '127.0.0.1'
PORT = 42068
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    key = key_gen()
    pub_key = key.public_key().exportKey('DER') #Export from key object
    s.sendall(pub_key)

    alice_key = s.recv(550)
    alice_key = RSA.importKey(alice_key)
    print("Have Alice's key")

    enc_num = s.recv(512)
    bin_num = Dec(key, enc_num)
    print("Have Alice's nonce")

    num_sig = s.recv(512)
    result = verify(str(enc_num), num_sig, alice_key)
    print("Signature is " + str(result))

    num = crypto_random()
    my_bin_num = bytes(str(num), encoding='utf-8')
    my_enc_num = Enc(alice_key, my_bin_num)
    s.sendall(my_enc_num)

    my_enc_num = str(my_enc_num)
    my_sig = sign(my_enc_num, key)
    s.sendall(my_sig)


    with open('passwords', 'r') as file:
      my_list = file.read()

    print("Done reading file")
    my_hash_my_num = SHA_hash(my_list + str(num), True)

    alice_hash = s.recv(64)
    print("Have Alice's hash")
    alice_hash_sig = s.recv(512)
    hash_sig_result = verify(str(alice_hash), alice_hash_sig, alice_key)
    print("Hash signature is " + str(hash_sig_result))


    my_hash_alice_num = SHA_hash(my_list + bin_num, True)
    my_hash_alice_num = bytes(my_hash_alice_num, encoding='utf-8')
    s.sendall(my_hash_alice_num)

    alice_num_sig = sign(str(my_hash_alice_num), key)
    s.sendall(alice_num_sig)

    if bytes(my_hash_my_num,encoding='utf-8') == alice_hash:
      print("Files are the same")
    else:
      print("I think Alice is a liar")


    exit()


    enc = Enc(key.public_key(),b'Message')
    print(Dec(key, enc))


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
