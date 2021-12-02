from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5
from Crypto import Random

def Enc(key, message):
    cipher = PKCS1_v1_5.new(key)
    msg = cipher.encrypt(message)
    return msg

def Dec(key, encMessage):
    cipher = PKCS1_v1_5.new(key)
    msg = cipher.decrypt(encMessage, None).decode('utf-8')
    return msg

def test():
    print(Enc(b'sixteen byte key', "hello"))
    print(Dec(b'sixteen byte key', Enc(b'sixteen byte key', "hello")))

#test()
