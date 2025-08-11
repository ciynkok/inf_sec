# def extended_gcd(a, b):
#     old_r, r = a, b
#     old_x, x = 1, 0
#     old_y, y = 0, 1
#
#     while r != 0:
#         quotient = old_r // r
#         old_r, r = r, old_r - quotient * r
#         old_x, x = x, old_x - quotient * x
#         old_y, y = y, old_y - quotient * y
#
#     return old_r, old_x, old_y


def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    gcd, x1, y1 = extended_gcd(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return gcd, x, y


# def gcd(a, b):
#     a, b = max(a, b), min(a, b)
#
#     return gcd(b, a - a // b * b)     if b == 0:
#         return a


if __name__ == "__main__":
    print(extended_gcd(78, 99))



