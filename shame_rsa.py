import random
from check_prime import check_prime
from gcd import extended_gcd
import secrets
from num_pow import mod_pow, pow_
import sys
sys.set_int_max_str_digits(10000000)


def generate_prime(n):
    while True:
        p = secrets.randbits(n)
        p = p | pow_(2, n) | 1
        if check_prime(p):
            return p


def generate_keys(bits, p=0, q=0):
    if p == 0:
        p = generate_prime(bits)
    if q == 0:
        q = generate_prime(bits)

    if not check_prime(p) and not check_prime(q):
        raise ValueError('p или q не являются простыми')

    while p == q:
        q = generate_prime(bits)

    n = p * q
    phi = (p - 1) * (q - 1)

    e = 65537#random.randrange(1, phi)

    gcd, x, y = extended_gcd(e, phi)
    if gcd != 1:
        return generate_keys(bits)

    d = x % phi

    return (e, n), (d, n)


if __name__ == "__main__":
    pub_key, priv_key = generate_keys(30)
    print('Публичный ключ: ' + str(pub_key))
    print('Секреный ключ: ' + str(priv_key))
    e, n = pub_key
    d = priv_key[0]
    cipr = mod_pow(123, e, n)
    print(cipr)
    print(mod_pow(cipr, d, n))
