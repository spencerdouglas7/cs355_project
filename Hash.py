from Crypto.Hash import SHA256

# @author Spencer Douglas
# Given a @param string, @return the SHA-256 hash of the respective string, or None if a string is not provided.
def SHA_hash(string, printable):
    if string is None or type(string) is not str:
        return
    h = SHA256.new()
    #convert to bytes for hash
    bytedata = bytes(string, 'utf-8')
    h.update(bytedata)
    if printable:
      return h.hexdigest()
    else:
      return h
def SHA_hash_test():
    print(SHA_hash('Hello'))
    print(SHA_hash('Hello'))
    print(SHA_hash(None))
    print(SHA_hash({}))
    print(SHA_hash('Zoo Wee Mama'))


#SHA_hash_test()
