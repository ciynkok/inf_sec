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

        print("Crack 1 way")
        start_time = time.time()
        d, f_iter = crack_rsa(e, n)
        f_time = time.time() - start_time
        f_times.append(f_time)
        f_iters.append(f_iter)
        print(f"Iters: {f_iter}, Time: {f_time:.4f} сек")

        print("Crack 2 way")
        start_time = time.time()
        decode, m_iter = crack_on_mess(e, n, message)
        m_time = time.time() - start_time
        m_times.append(m_time)
        m_iters.append(m_iter)
        print(f"Iters: {m_iter}, Time: {m_time:.4f} sec")
        bit_.append(bits)

    plt.figure(figsize=(14, 12))

    plt.subplot(2, 1, 1)
    plt.plot(bit_lengths, f_times, 'bo-', label='Crack 1 way')
    plt.plot(bit_lengths, m_times, 'rs-', label='Crack 2 way')

    plt.ylabel('Time', fontsize=12)
    plt.grid(True)
    plt.legend(fontsize=12)

    plt.subplot(2, 1, 2)
    plt.plot(bit_lengths, f_iters, 'bo-', label='Crack 1 way')
    plt.plot(bit_lengths, m_iters, 'rs-', label='Crack 2 way')

    plt.ylabel('Quantity', fontsize=12)
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
