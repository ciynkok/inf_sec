import math
import random
import numpy as np
from matplotlib import pyplot as plt
import rsa
from check_prime import check_prime


def trial_division(n):
    k = 0
    if n % 2 == 0:
        return 2
    i = 3
    while i * i <= n:
        if n % i == 0:
            return i, n // i, k
        i += 2
        k += 1
    return n, None, None


def crack_rsa_factorization(n):
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


# pub_key, private_key = rsa.generate_keys(10)
# print('Публичный ключ: ' + str(pub_key[0]))
# print('Секреный ключ: ' + str(private_key[0]))
# e, n = pub_key
# p, q, k = trial_division(n)
# # q = n // p
# # p, q, f_iters = crack_rsa_factorization(n)
# phi = (p - 1) * (q - 1)
# d = pow(e, -1, phi)
# print(d)

