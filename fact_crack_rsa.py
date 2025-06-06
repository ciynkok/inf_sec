import math
import random
import numpy as np
from matplotlib import pyplot as plt
import rsa
from check_prime import check_prime

# def pollards_rho(n):
#     if n % 2 == 0:
#         return 2
#     if n % 3 == 0:
#         return 3
#     if n % 5 == 0:
#         return 5
#     k = 0
#     while True:
#         c = random.randint(2, n - 1)
#         f = lambda x: (pow(x, 2, n) + c) % n
#         x, y, d = 2, 2, 1
#         while d == 1:
#             x = f(x)
#             y = f(f(y))
#             d = math.gcd(abs(x - y), n)
#             k += 1
#         if d != n:
#             return d, k
#
# def factorize(n):
#     factors = []
#     m = []
#     def _factorize(n):
#         if n == 1:
#             return
#         if check_prime(n):
#             factors.append(n)
#             return
#         d, k = trial_division(n)#pollards_rho(n)
#         m.append(k)
#         _factorize(d)
#         _factorize(n // d)
#     _factorize(n)
#     return sorted(factors), m
#
# def crack_rsa(n, e):
#     factors, m = factorize(n)
#     p, q = factors
#     phi = (p - 1) * (q - 1)
#     d = pow(e, -1, phi)
#     return m[0]
#
# def graph():
#     bits = []
#     iters = []
#
#     for k in range(10, 41):
#         pub_key, private_key = rsa.generate_keys(k)
#         n = pub_key[1]
#         e = pub_key[0]
#         d = crack_rsa(n, e)
#         bits.append(k)
#         iters.append(d)
#
#     bits = np.array(bits)
#     iters = np.array(iters)
#     print(bits, iters)
#     plt.plot(bits, iters)
#     plt.show()
#
# # graph()
# pub_key, private_key = rsa.generate_keys(30)
# n = pub_key[1]
# e = pub_key[0]
# d = crack_rsa(n, e)
# print(f"Взломанный закрытый ключ d: {d}")

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



