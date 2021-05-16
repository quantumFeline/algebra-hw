import numpy as np
import functions
import primes
from tqdm import tqdm


def miller_rabin_test(n, tries=10):
    if n == 1:
        return False

    d = n-1
    s = 0
    while d % 2 == 0:
        d //= 2
        s += 1

    for _ in range(tries):
        a = np.random.randint(-1e9, 1e9)
        # print(f"Trying {a}")
        a_d = functions.fast_power(a, d, n)
        a_2rd = a_d

        r = 0
        while r < s:
            if a_2rd == n - 1:
                exists_r = True
                break
            r += 1
            a_2rd = (a_2rd ** 2) % n
        else:
            exists_r = False

        if a_d != 1 and not exists_r:
            return False  # Not a prime
    return True  # The number has passed all test


print(miller_rabin_test(6873))

for i in tqdm(range(1, 10000)):
    if miller_rabin_test(i) and i not in primes.primes:
        print(f"False positive: {i}")
