import numpy as np

import functions
import primes


def f(x):
    return x**2 - 1


def pollard_rho(n):

    if primes.is_prime(n):
        return [n]

    x0 = np.random.randint(3, n-2)
    xi = x2i = f(x0)
    i, stage = 1, 2
    d = 1
    tries = 100

    while d == 1:
        while i < stage:
            i += 1
            x2i = f(xi)

        stage *= 2
        d = functions.gcd(n, abs(x2i-xi))

        if i > 1000:
            x0 = np.random.randint(3, n - 2)
            xi = x2i = f(x0)
            i, stage = 1, 2
            d = 1
            tries += 1

        if tries > 10000:
            print(f"Not found: factorisation for {n}")
            return [n]

    print(d)
    return [d] + pollard_rho(n//d)


print(pollard_rho(6453))
