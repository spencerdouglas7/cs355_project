from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto import Random

def Enc(key, message):
    cipher = PKCS1_OAEP.new(key)
    msg = cipher.encrypt(message)
    return msg

def Dec(key, encMessage):
    cipher = PKCS1_OAEP.new(key)
    msg = cipher.decrypt(encMessage).decode('utf-8')
    return msg

def test():
    print(Enc(b'sixteen byte key', "hello"))
    print(Dec(b'sixteen byte key', Enc(b'sixteen byte key', "hello")))

#test()
