#base level encryption will upgrade later
'''
TODO:
introduce a random value as an additional key that only the recepient will know after encrypting
therefore it might add an extra layer of protection
'''


def eucalg(a, b):
    # make a the bigger one and b the lesser one
    swapped = False
    if a < b:
        a, b = b, a
        swapped = True
    # ca and cb store current a and b in form of
    # coefficients with initial a and b
    # a' = ca[0] * a + ca[1] * b
    # b' = cb[0] * a + cb[1] * b
    ca = (1, 0)
    cb = (0, 1)
    while b != 0:
        # k denotes how many times number b
        # can be substracted from a
        k = a // b
        # a  <- b
        # b  <- a - b * k
        # ca <- cb
        # cb <- (ca[0] - k * cb[0], ca[1] - k * cb[1])
        a, b, ca, cb = b, a - b * k, cb, (ca[0] - k * cb[0], ca[1] - k * cb[1])
    if swapped:
        return (ca[1], ca[0])
    else:
        return ca


def modpow(b, e, n):
    # find length of e in bits
    tst = 1
    siz = 0
    while e >= tst:
        tst <<= 1
        siz += 1
    siz -= 1
    # calculate the result
    r = 1
    for i in range(siz, -1, -1):
        r = (r * r) % n
        if (e >> i) & 1: r = (r * b) % n
    return r


def keysgen(p, q):
    n = p * q
    lambda_n = (p - 1) * (q - 1)
    e = 35537
    d = eucalg(e, lambda_n)[0]
    if d < 0: d += lambda_n
    # both private and public key must have n stored with them
    return {'priv': (d, n), 'pub': (e, n)}


def numencrypt(m, pub):
    return modpow(m, pub[0], pub[1])


def numdecrypt(m, priv):
    return modpow(m, priv[0], priv[1])


'''
BLUEPRINT:

>>> import RSA_Encryption as rsa
>>> keys = rsa.keysgen(31337, 31357)
>>> keys
{'priv': (720926705, 982634309), 'pub': (35537, 982634309)}
>>> priv = keys['priv']
>>> pub = keys['pub']
>>> msg = 80087
>>> enc = rsa.numencrypt(msg, priv)
>>> enc
34604568
>>> dec = rsa.numdecrypt(enc, pub)
>>> dec
80087
'''