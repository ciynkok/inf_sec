import math
import random
import numpy as np
from matplotlib import pyplot as plt
import shame_rsa as rsa
from num_pow import mod_pow
from check_prime import check_prime


def factorization(n):
    i = 2
    iters = 0
    while i <= np.sqrt(n):
        if n % i == 0:
            return i, n // i, iters
        if i == 2:
            i += 1
        else:
            i += 2
        iters += 1
    raise ValueError("n is prime")


def crack_rsa(e, n):
    p, q, k = factorization(n)
    phi = (p - 1) * (q - 1)
    d = mod_pow(e, -1, phi)
    return d, k


if __name__ == "__main__":
    pub_key, priv_key = rsa.generate_keys(20)
    e, n = pub_key
    d = priv_key[0]
    d1, k = crack_rsa(e, n)
    print('Secret key: ' + str(d))
    print('Decrypted secret key: ' + str(d1))
    print('Iters: ' + str(k))

