import random
from check_prime import check_prime
from gcd import extended_gcd
from num_pow import fast_pow
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


print(generate_keys())
def encrypt(pk, plaintext):
    key, n = pk
    cipher = []
    for char in plaintext:
        cipher.append(fast_pow(ord(char), key) % n)
    return cipher

def rsa_encrypt(message, public_key) -> int:

    e, n = public_key
    return fast_pow(message, e) % n


def rsa_decrypt(ciphertext, private_key) -> int:

    d, n = private_key
    return fast_pow(ciphertext, d) % n



def decrypt(pk, ciphertext):
    key, n = pk
    plain = []
    for char in ciphertext:
        plain.append(chr(fast_pow(char, key) % n))
    return ''.join(plain)


# pub_key, private_key = generate_keys(10)
# print('Публичный ключ: ' + str(pub_key[0]))
# print('Секреный ключ: ' + str(private_key[0]))
# in_text = input('Введите текст для шифрования: ')
# cipher = encrypt(pub_key, in_text)
# print(cipher)
# print(decrypt(private_key, cipher))

