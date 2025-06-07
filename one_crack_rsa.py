import math
import random
import numpy as np
from matplotlib import pyplot as plt
import shame_rsa
from num_pow import mod_pow
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

# def factorize(n):
#     """Факторизация числа n"""
#     factors = []
#     def _factorize(n):
#         if n == 1:
#             return
#         if check_prime(n):
#             factors.append(n)
#             return
#         d, p, k = trial_division(n)
#         _factorize(d)
#         _factorize(n // d)
#     _factorize(n)
#     return sorted(factors)
#
# def crack_rsa(n, e):
#     """Восстановление d из n и e"""
#     factors = factorize(n)
#     if len(factors) != 2:
#         raise ValueError("n не является произведением двух простых чисел!")
#     p, q = factors
#     phi = (p - 1) * (q - 1)
#     d = pow(e, -1, phi)
#     return d


if __name__ == "__main__":
    pub_key, private_key = shame_rsa.generate_keys(10)
    print('Публичный ключ: ' + str(pub_key[0]))
    print('Секреный ключ: ' + str(private_key[0]))
    e, n = pub_key
    p, q, k = trial_division(n)
    phi = (p - 1) * (q - 1)
    # print(check_prime(p), check_prime(q))
    d = mod_pow(e, -1, phi)
    print(d)
    # d = mod_pow(e, -1, phi)

