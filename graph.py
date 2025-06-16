import time
from rsa import generate_keys, rsa_encrypt, rsa_decrypt
import random
from one_crack_rsa import crack_rsa
from two_crack_rsa import crack_on_mess
from matplotlib import pyplot as plt


def print_graph(bits_len):
    f_times = []
    m_times = []
    f_iters = []
    m_iters = []
    bit_ = []

    for bits in bits_len:

        public_key, private_key = generate_keys(bits)
        e, n = public_key

        message = 123
        ciphertext = rsa_encrypt(message, public_key)

        print("Факторизация")
        start_time = time.time()
        d, f_iter = crack_rsa(e, n)
        f_time = time.time() - start_time
        f_times.append(f_time)
        f_iters.append(f_iter)
        print(f"Итерации: {f_iter}, Время: {f_time:.4f} сек")

        print("Взлом на сообщении")
        start_time = time.time()
        decode, m_iter = crack_on_mess(e, n, message)
        m_time = time.time() - start_time
        m_times.append(m_time)
        m_iters.append(m_iter)
        print(f"Итерации: {m_iter}, Время: {m_time:.4f} сек")
        bit_.append(bits)

    plt.figure(figsize=(14, 12))

    plt.subplot(2, 1, 1)
    plt.plot(bit_lengths, f_times, 'bo-', label='Факторизация')
    plt.plot(bit_lengths, m_times, 'rs-', label='Перебор сообщений')

    plt.ylabel('Время (секунды)', fontsize=12)
    plt.grid(True)
    plt.legend(fontsize=12)

    plt.subplot(2, 1, 2)
    plt.plot(bit_lengths, f_iters, 'bo-', label='Факторизация')
    plt.plot(bit_lengths, m_iters, 'rs-', label='Перебор сообщений')

    plt.ylabel('Количество итераций', fontsize=12)
    plt.yscale('log')
    plt.grid(True)
    plt.legend(fontsize=12)

    plt.tight_layout()
    filename = 'graph.png'
    plt.savefig(filename, dpi=300)
    plt.show()


if __name__ == "__main__":
    bit_lengths = [i for i in range(4, 15)]
    print_graph(bit_lengths)
