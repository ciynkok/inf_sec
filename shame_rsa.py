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
        is_prime, p_, q_ = check_prime(p)
        if is_prime:
            return p


def generate_keys(bits):
    # if p == 0:
    #     p = generate_prime(bits)
    # if q == 0:
    #     q = generate_prime(bits)

    p = generate_prime(bits)
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
    pub_key, priv_key = generate_keys(32)
    print('Публичный ключ: ' + str(pub_key))
    print('Секреный ключ: ' + str(priv_key))
