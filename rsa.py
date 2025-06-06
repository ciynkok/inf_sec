import random
import math
from check_prime import check_prime
from gcd import extended_gcd
from num_pow import mod_pow
import secrets
import sys
sys.set_int_max_str_digits(1000000)


def generate_prime(n):
    while True:
        p = secrets.randbits(n)
        p = p | (1 << n - 1) | 1
        if check_prime(p):
            return p

def generate_keys(bits):
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


# def generate_rsa_keys(bit_length):
#     """Построение схемы RSA"""
#     min_val = 2 ** (bit_length // 2 - 1)
#     max_val = 2 ** (bit_length // 2)
#     p = generate_prime(bit_length)
#     q = generate_prime(bit_length)
#
#     # while True:
#     #     p = random.randrange(min_val, max_val)
#     #     if check_prime(p):
#     #         break
#     #
#     # while True:
#     #     q = random.randrange(min_val, max_val)
#     #     if check_prime(q) and p != q:
#     #         break
#
#     n = p * q
#     phi = (p - 1) * (q - 1)
#
#     e = 65537
#     if math.gcd(e, phi) != 1:
#         e = 3
#         while math.gcd(e, phi) != 1:
#             e += 2
#
#     _, d, _ = extended_gcd(e, phi)
#     d = d % phi
#     if d < 0:
#         d += phi
#
#     return (e, n), (d, n)




# def encrypt(pk, plaintext):
#     key, n = pk
#     cipher = []
#     for char in plaintext:
#         cipher.append(mod_pow(ord(char), key) % n)
#     return cipher

def rsa_encrypt(message, public_key):

    e, n = public_key
    return mod_pow(message, e, n)


def rsa_decrypt(ciphertext, private_key):

    d, n = private_key
    return mod_pow(ciphertext, d, n)



# def decrypt(pk, ciphertext):
#     key, n = pk
#     plain = []
#     for char in ciphertext:
#         plain.append(chr(fast_pow(char, key) % n))
#     return ''.join(plain)


# pub_key, private_key = generate_keys(10)
# print('Публичный ключ: ' + str(pub_key[0]))
# print('Секреный ключ: ' + str(private_key[0]))
# in_text = 123
# cipher = rsa_encrypt(in_text, pub_key)
# print(cipher)
# print(rsa_decrypt(cipher, private_key))

