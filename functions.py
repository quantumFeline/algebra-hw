# Additional functions for commonly used calculations
import numpy as np
from primes import primes


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def factorisation(n):
    factors = []
    for div in range(2, n+1):
        while n % div == 0:
            factors.append(div)
            n //= div
        if n == 1:
            break
    # print(f"factors of {n}: {factors}")
    return np.array(factors)


def fast_power(base, power, modulo):
    power_bin = "{0:b}".format(power)
    res = 1
    for s in power_bin:
        res = (res ** 2) % modulo
        if s == '1':
            res = (res * base) % modulo
    return res
