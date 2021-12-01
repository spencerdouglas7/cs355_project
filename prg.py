import secrets

PRG_LENGTH = 256

def crypto_random():
    return secrets.randbits(PRG_LENGTH)


def crypto_random_test():
    map = {}
    for i in range(1000000):
        val = crypto_random()
        if map.get(val):
            return False
        map.update({val: val})
    return True

print(crypto_random_test())
