import time
from rsa import generate_keys, rsa_encrypt, rsa_decrypt
import random
from fact_crack_rsa import crack_rsa_factorization
from mess_crack_rsa import crack_rsa_message_brute
from matplotlib import pyplot as plt

def simulate_rsa_cracking(bit_lengths):
    """Построение графиков и логирование результатов"""
    factor_times = []
    brute_times = []
    factor_iters = []
    brute_iters = []
    brute_bit_lengths = []

    for bits in bit_lengths:
        print(f"\n--- {bits}-битный ключ ---")

        start_time = time.time()
        public_key, private_key = generate_keys(bits)
        e, n = public_key
        keygen_time = time.time() - start_time
        print(f"Сгенерирован ключ: n={n}")
        print(f"Время генерации: {keygen_time:.4f} сек")

        max_message = min(n, 1000)
        message = random.randint(1, max_message)
        ciphertext = rsa_encrypt(message, public_key)
        print(f"Сообщение: {message}, Шифротекст: {ciphertext}")

        print("Запуск факторизации...")
        start_time = time.time()
        p, q, f_iters = crack_rsa_factorization(n)
        factor_time = time.time() - start_time
        factor_times.append(factor_time)
        factor_iters.append(f_iters)
        print(f"Найдены делители: p={p}, q={q}")
        print(f"Итераций: {f_iters}, Время: {factor_time:.4f} сек")

        # 7. ВЗЛОМ МЕТОДОМ ПЕРЕБОРА СООБЩЕНИЙ
        print("Запуск перебора сообщений...")
        start_time = time.time()
        # Для больших ключей используем ограниченный перебор
        max_attempts = min(10 ** 6, n) if bits > 16 else n
        cracked_message, b_iters = crack_rsa_message_brute(
            ciphertext,
            e,
            n,
            max_attempts
        )
        brute_time = time.time() - start_time
        brute_times.append(brute_time)
        brute_iters.append(b_iters)
        brute_bit_lengths.append(bits)
        if cracked_message is not None:
            print(f"Найдено сообщение: {cracked_message}")
        else:
            print("Сообщение не найдено (достигнут лимит попыток)")
        print(f"Итераций: {b_iters}, Время: {brute_time:.4f} сек")

    # Построение графиков
    plt.figure(figsize=(14, 12))

    # 6-7. ГРАФИКИ СРАВНЕНИЯ МЕТОДОВ ВЗЛОМА
    # График времени
    plt.subplot(2, 1, 1)
    plt.plot(bit_lengths, factor_times, 'bo-', label='Факторизация')
    plt.plot(bit_lengths, brute_times, 'rs-', label='Перебор сообщений')

    plt.title('Сравнение времени взлома RSA', fontsize=14)
    plt.xlabel('Размер ключа (бит)', fontsize=12)
    plt.ylabel('Время (секунды)', fontsize=12)
    plt.grid(True)
    plt.legend(fontsize=12)

    for i, bits in enumerate(bit_lengths):
        plt.annotate(
            f"{factor_times[i]:.4f}",
            (bits, factor_times[i]),
            textcoords="offset points",
            xytext=(0, 5),
            ha='center',
            fontsize=9
        )
        plt.annotate(
            f"{brute_times[i]:.4f}",
            (bits, brute_times[i]),
            textcoords="offset points",
            xytext=(0, -15),
            ha='center',
            fontsize=9
        )

    # График итераций
    plt.subplot(2, 1, 2)
    plt.plot(bit_lengths, factor_iters, 'bo-', label='Факторизация')
    plt.plot(bit_lengths, brute_iters, 'rs-', label='Перебор сообщений')

    plt.title('Итерации при взломе RSA', fontsize=14)
    plt.xlabel('Размер ключа (бит)', fontsize=12)
    plt.ylabel('Количество итераций', fontsize=12)
    plt.yscale('log')
    plt.grid(True)
    plt.legend(fontsize=12)

    for i, bits in enumerate(bit_lengths):
        plt.annotate(
            f"{factor_iters[i]}",
            (bits, factor_iters[i]),
            textcoords="offset points",
            xytext=(0, 5),
            ha='center',
            fontsize=9
        )
        plt.annotate(
            f"{brute_iters[i]}",
            (bits, brute_iters[i]),
            textcoords="offset points",
            xytext=(0, -15),
            ha='center',
            fontsize=9
        )

    plt.tight_layout()

    filename = 'rsa_cracking_comparison.png'
    plt.savefig(filename, dpi=300)
    print(f"\nГрафики сохранены в файл '{filename}'")
    plt.show()


if __name__ == "__main__":
    # Размеры ключей для тестирования
    bit_lengths = [i * 4 for i in range(1, 9)]
    simulate_rsa_cracking(bit_lengths)
