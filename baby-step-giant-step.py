import numpy as np
import functions


def gelfond_shanks(a, b, mod):
    n = mod / functions.gcd(a, mod)  # group order
    m = int(np.ceil(n**0.5))

    # Baby step
    candidates = {}
    for j in range(m):
        a_j = functions.fast_power(a, j, mod)
        candidates[(a_j * b) % mod] = j

    # Giant step
    a_mm = functions.fast_power(a, m, mod)
    y = 1
    for i in range(m+1):
        if y in candidates:
            j = candidates[y]
            return i*m-j
        y = (y * a_mm) % mod
    print("No log found!")


if __name__ == '__main__':
    assert gelfond_shanks(5, 3, 23) == 16
    assert gelfond_shanks(3, 13, 17) == 4
    print("Works")
