import Crypto.PublicKey.RSA as RSA
from Crypto import Random
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA256
from Hash import SHA_hash

def key_gen():
  random_gen = Random.new().read
  key = RSA.generate(2048, random_gen)
  return key

def sign(m, key):
  signer = PKCS1_v1_5.new(key)
  hashed_m = SHA_hash(m, False)
  return signer.sign(hashed_m)

def verify(m, sig, public_key):
  verify_sig = PKCS1_v1_5.new(public_key)
  hashed_m = SHA_hash(m, False)
  return verify_sig.verify(hashed_m, sig)

def test():
  m = 'Message'
  key = key_gen()
  sig = sign(m, key)
  m2 = 'Message2'
  sig2 = sign(m2, key)
  print(verify(m, sig, key.public_key()))
  print(verify(m, sig2, key.public_key()))

test()
