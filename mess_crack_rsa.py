import rsa
from num_pow import mod_pow


def crack_rsa_message_brute(ciphertext: int, e: int, n: int, max_attempts: int = 10**7):
    iterations = 0
    for m in range(1, max_attempts + 1):
        iterations += 1
        if mod_pow(m, e, n) == ciphertext:
            return m, iterations
    return None, iterations


# def crack_rsa(n, e):
#     factors, m = factorize(n)
#     p, q = factors
#     phi = (p - 1) * (q - 1)
#     d = pow(e, -1, phi)
#     return d

if __name__ == "__main__":
    pub_key, private_key = rsa.generate_keys(10)
    print('Публичный ключ: ' + str(pub_key[0]))
    print('Секреный ключ: ' + str(private_key[0]))
    e, n = pub_key
    mess = int(input('Введите число: '))
    cipr = rsa.rsa_encrypt(mess, pub_key)
    print(cipr)
    print(crack_rsa_message_brute(cipr, e, n))

