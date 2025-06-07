import math
import random
import numpy as np
from matplotlib import pyplot as plt
import shame_rsa
from check_prime import check_prime
from num_pow import mod_pow
import sys
sys.set_int_max_str_digits(1000000)


def crack_rsa_factorization(e, n, m):
    iterations = 0

    small_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
    for p in small_primes:
        iterations += 1
        if n % p == 0:
            return p, n // p, iterations

    root = math.isqrt(n)
    if root * root == n:
        return root, root, iterations

    start = math.isqrt(n)
    for i in range(start, 1, -1):
        iterations += 1
        if n % i == 0:
            return i, n // i, iterations

    return None, None, iterations


if __name__ == "__main__":
    pub_key, private_key = shame_rsa.generate_keys(10)
    print('Публичный ключ: ' + str(pub_key[0]))
    print('Секреный ключ: ' + str(private_key[0]))
    e, n = pub_key
    mess = int(input('Введите число: '))
    p, q, f_iters = crack_rsa_factorization(n)
    phi = (p - 1) * (q - 1)
    d = mod_pow(e, -1, phi)
    print(d)
