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
    iters = 0
    new_me = mod_pow(m, e, n)
    old_me = m
    while new_me != m:
        old_me = new_me
        new_me = mod_pow(new_me, e, n)
        iters += 1

    return old_me, iters


if __name__ == "__main__":
    pub_key, private_key = shame_rsa.generate_keys(15)
    e, n = pub_key
    mess = 123128
    cipr = mod_pow(mess, e, n)
    decode, k = crack_on_mess(e, n, cipr)
    print('Massage: ' + str(mess))
    print('Cipr: ' + str(cipr))
    print('Decrypt: ' + str(decode))
    print('Iters: ' + str(k))
