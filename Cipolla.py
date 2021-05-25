import numpy as np

import functions
from Legendre_Jacobi import legendre


def cipolla(n, p):

    # Euler criterion
    l = legendre(n, p)
    if l == 0: # n % p == 0
        return 0
    elif l == -1: # n is not a square in Zp
        return -1

    res = 0
    while res != -1:
        a = np.random.randint(np.ceil(n**0.5), p)
        res = legendre(a**2-n, p)
        if res == 0:
            return a  # a**2 == n (mod p)

    # noinspection PyUnboundLocalVariable
    x = functions.fast_power_sqrt(np.array((a, 1)), (p+1)//2, p)

    return x


print(cipolla(10, 13))
