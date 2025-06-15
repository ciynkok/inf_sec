import random
import numpy as np


def factorization(n):
    m = []
    i = 2
    p = n
    count_iters = 0
    while i <= np.sqrt(n):
        if p % i == 0:
            k = 0
            while p % i == 0:
                p //= i
                k += 1
            if k != 0:
                m.append((i, k))
        if i == 2:
            i += 1
        else:
            i += 2
        count_iters += 1
    if p != 1:
        m.append((p, 1))
    return m, count_iters


def check_prime(n, k=5, div=False):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0:
        return (False, factorization(n)) if div else False

    d = n - 1
    s = 0
    while d % 2 == 0:
        d //= 2
        s += 1

    for i in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for j in range(s - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return (False, factorization(n)) if div else False

    return True


if __name__ == "__main__":
    print(check_prime(35112342))
    print(factorization(1918691))

