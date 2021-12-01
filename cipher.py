from Crypto.PublicKey import RSA
from Crypto.Cipher import AES
from Crypto import Random

def Enc(key, message):
    iv = Random.new().read(AES.block_size)
    cipher = AES.new(key, AES.MODE_CFB, iv)
    msg = iv + cipher.encrypt(bytes(message, 'utf-8'))
    return msg

def Dec(key, encMessage):
    iv = encMessage[:AES.block_size]
    cipher = AES.new(key, AES.MODE_CFB, iv)
    msg = cipher.decrypt(encMessage[AES.block_size:]).decode('utf-8')
    return msg

def test():
    print(Enc(b'sixteen byte key', "hello"))
    print(Dec(b'sixteen byte key', Enc(b'sixteen byte key', "hello")))

#test()
