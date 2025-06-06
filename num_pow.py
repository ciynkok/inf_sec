import sys
import datetime

sys.set_int_max_str_digits(1000000)

def fast_pow(a, n):
    t = datetime.datetime.now()
    res = 1
    while n > 0:
        if n % 2 == 0:
            a *= a
            n //= 2
#            print(a, n)
        res *= a
        n = n - 1
            # print(res, a, n)

    # print('Скорость вычисления по быстрому алгоритму: ' + str(datetime.datetime.now() - t))
    return res

def simple_pow(a, n):
    t = datetime.datetime.now()
    res = 1
    for i in range(n):
        res *= a
    # print('Скорость вычисления по линейному алгоритму: ' +
    #       str(datetime.datetime.now() - t))
    return res

fast_pow(97, 100000)
simple_pow(3, 100000)

