import random


def trial_division(n):
    k = 0
    if n % 2 == 0:
        return 2, n // 2, k
    i = 3
    while i * i <= n:
        if n % i == 0:
            return i, n // i, k
        i += 2
        k += 1
    return n, None, None


def check_prime(n, k=5):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0:
        return False, 2, n // 2

    # p, q, cont = trial_division(n)
    # if p != n:
    #     return False, p, q

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
            return False

    return True


# print(check_prime(667))

