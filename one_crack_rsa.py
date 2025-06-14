import math
import random
import numpy as np
from matplotlib import pyplot as plt
import shame_rsa as rsa
from num_pow import mod_pow
from check_prime import check_prime

def factorization(n):
    i = 2
    count_iters = 0
    while i <= np.sqrt(n):
        if n % i == 0:
            return i, n // i, count_iters
        if i == 2:
            i += 1
        else:
            i += 2
        count_iters += 1
    raise ValueError("n is prime")


if __name__ == "__main__":
    pub_key, priv_key = rsa.generate_keys(8)
    e, n = pub_key
    d = priv_key[0]
    p, q, k = factorization(n)
    phi = (p - 1) * (q - 1)
    d1 = mod_pow(e, -1, phi)
    print(d1, d)


