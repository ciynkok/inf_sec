import sys
import datetime

sys.set_int_max_str_digits(1000000)

def mod_pow(base: int, exponent: int, modulus: int) -> int:
    """Алгоритм быстрого возведения в степень"""
    if modulus == 1:
        return 0
    base = base % modulus
    result = 1
    while exponent > 0:
        if exponent & 1:
            result = (result * base) % modulus
        base = (base * base) % modulus
        exponent >>= 1
    return result

# print(mod_pow(3, 1000000, 112312))

