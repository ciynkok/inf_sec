import math
import random
import numpy as np
from matplotlib import pyplot as plt
import shame_rsa
from check_prime import check_prime
from num_pow import mod_pow, pow_
import sys
sys.set_int_max_str_digits(1000000)


def crack_on_mess(e, n, m):
    new_me = mod_pow(m, e, n)
    old_me = m
    while new_me != m:
        old_me = new_me
        new_me = mod_pow(new_me, e, n)

    return old_me


if __name__ == "__main__":
    pub_key, private_key = shame_rsa.generate_keys(10)
    print('Публичный ключ: ' + str(pub_key[0]))
    print('Секреный ключ: ' + str(private_key[0]))
    e, n = pub_key
    mess = 123123
    cipr = mod_pow(mess, e, n)
    print(crack_on_mess(e, n, cipr))
