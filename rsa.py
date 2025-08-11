import random
import math
from check_prime import check_prime
from gcd import extended_gcd
from num_pow import mod_pow
import secrets
from shame_rsa import generate_keys
import sys
sys.set_int_max_str_digits(1000000)


# def generate_prime(n):
#     while True:
#         p = secrets.randbits(n)
#         p = p | (1 << n - 1) | 1
#         if check_prime(p):
#             return p
#
#
# def generate_keys(bits, p=None, q=None):
#     if p is None:
#         p = generate_prime(bits)
#     elif not check_prime(p):
#         return
#     if q is None:
#         q = generate_prime(bits)
#     elif not check_prime(q):
#         return
#
#     while p == q:
#         q = generate_prime(bits)
#     n = p * q
#     phi = (p - 1) * (q - 1)
#
#     e = random.randrange(1, phi)
#
#     gcd, x, y = extended_gcd(e, phi)
#     while gcd != 1:
#         e = random.randrange(1, phi)
#         gcd, x, y = extended_gcd(e, phi)
#
#     d = x % phi
#
#     return (e, n), (d, n)


def rsa_encrypt(message, public_key):
    e, n = public_key
    return mod_pow(message, e, n)


def encrypt(plaintext, public_key):
    key, n = public_key
    cipher = [mod_pow(ord(char), key, n) for char in plaintext]
    return cipher


def decrypt(ciphertext, private_key):
    key, n = private_key
    plain = [chr(mod_pow(char, key, n)) for char in ciphertext]
    return ''.join(plain)


def rsa_decrypt(ciphertext, private_key):
    d, n = private_key
    return mod_pow(ciphertext, d, n)


if __name__ == "__main__":
    pub_key, priv_key = generate_keys(10)
    in_text = input('Enter text: ')
    cipher = encrypt(in_text, pub_key)
    print(cipher)
    print(decrypt(cipher, priv_key))

