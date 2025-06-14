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

    while p == q:
        q = generate_prime(bits)

    n = p * q
    phi = (p - 1) * (q - 1)

    e = random.randrange(1, phi)

    gcd, x, y = extended_gcd(e, phi)
    while gcd != 1:
        e = random.randrange(1, phi)
        gcd, x, y = extended_gcd(e, phi)

    d = x % phi

    return (e, n), (d, n)


if __name__ == "__main__":
    pub_key, priv_key = generate_keys(8)
    print('Публичный ключ: ' + str(pub_key))
    cipr = pow(123, pub_key[0]) % pub_key[1]
    print(mod_pow(cipr, priv_key[0], priv_key[1]))
    print('Секреный ключ: ' + str(priv_key))
