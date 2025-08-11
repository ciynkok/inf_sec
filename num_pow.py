import sys
import datetime
from gcd import extended_gcd

sys.set_int_max_str_digits(1000000)


def pow_(base, exponent):
    result = 1
    while exponent > 0:
        if exponent & 1:
            result = (result * base)
        base = (base * base)
        exponent >>= 1
    return result


def mod_pow(base, exponent, modulus):
    if exponent < 0:
        gcd, x, y = extended_gcd(base, modulus)
        base = x % modulus
        return mod_pow(base, -1 * exponent, modulus)
    if modulus == 1:
        return 0
    base = base % modulus
    result = 1
    while exponent > 0:
        if exponent % 2 != 0:
            result = (result * base) % modulus
        base = (base * base) % modulus
        exponent >>= 1
    return result


if __name__ == "__main__":
    print(mod_pow(2, 65536, 65537))

