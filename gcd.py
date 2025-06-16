def extended_gcd(a, b):
    old_r, r = a, b
    old_s, s = 1, 0
    old_t, t = 0, 1

    while r != 0:
        quotient = old_r // r
        old_r, r = r, old_r - quotient * r
        old_s, s = s, old_s - quotient * s
        old_t, t = t, old_t - quotient * t

    return old_r, old_s, old_t


# def gcd(a, b):
#     a, b = max(a, b), min(a, b)
#
#     return gcd(b, a - a // b * b)     if b == 0:
#         return a


if __name__ == "__main__":
    print(extended_gcd(34, 35))



