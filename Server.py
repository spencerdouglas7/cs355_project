#https://realpython.com/python-sockets/
import socket
from sig import *
from cipher import *
from prg import *

HOST = '127.0.0.1'
PORT = 42068


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        bob_key = conn.recv(550) #public key is length 550
        bob_key = RSA.importKey(bob_key)
        print("have Bob's key")

        key = key_gen()
        pub_key = key.public_key().exportKey('DER')
        conn.sendall(pub_key)

        num = crypto_random()
        bin_num = bytes(str(num), encoding='utf-8')
        enc_num = Enc(bob_key, bin_num)
        conn.sendall(enc_num)

        enc_num = str(enc_num)
        sig = sign(enc_num, key)
        conn.sendall(sig)

        bob_enc_num = conn.recv(512)
        bob_bin_num = Dec(key, bob_enc_num)
        print("Have Bob's nonce")

        bob_sig = conn.recv(512)
        result = verify(str(bob_enc_num), bob_sig, bob_key)
        print("Signature is " + str(result))

        with open('passwords', 'r') as file:
          my_list = file.read()

        print("Done reading file")

        my_hash = SHA_hash(my_list + bob_bin_num, True)
        my_hash = bytes(my_hash, encoding='utf-8')
        conn.sendall(my_hash)

        hash_sig = sign(str(my_hash), key)
        conn.sendall(hash_sig)

        my_hash_my_num = SHA_hash(my_list + str(num), True)
        bob_hash_my_num = conn.recv(64)
        print("Have Bob's hash")


        bob_hash_sig = conn.recv(512)
        bob_hash_sig_result = verify(str(bob_hash_my_num), bob_hash_sig, bob_key)
        print("Bob's hash signature is " + str(bob_hash_sig_result))



        if bytes(my_hash_my_num, encoding='utf-8') == bob_hash_my_num:
          print("Files are the same")
        else:
          print("I think Bob is a liar")

        exit()
