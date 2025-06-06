import math
import random
import numpy as np
from matplotlib import pyplot as plt
import rsa
from check_prime import check_prime

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



