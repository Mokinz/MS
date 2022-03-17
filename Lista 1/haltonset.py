import numpy as np

def is_prime(n):
    upper = int(np.sqrt(n))
    modulos = [bool(n % k) for k in range(2, upper+1)]
    if False in modulos:
        return False
    elif modulos:
        return True
    elif n in [2, 3]:
        return True
    return False

def next_prime():
    candidate = 2
    while(True):
        if is_prime(candidate):
            yield candidate
        candidate += 1

def vdc(n, base=2):
    vdc, denom = 0, 1
    while n:
        denom *= base
        n, remainder = divmod(n, base)
        vdc += remainder/float(denom)
    return vdc

def haltonset(length, dim, leap=0, skip=0):
    ind_low = skip
    ind_high = length * (leap + 1) + skip
    primes = next_prime()
    p = [next(primes) for e in range(dim)]
    out = np.zeros((length, dim))
    for d in range(dim):
        out[:, d] = [vdc(i, p[d]) for i in range(ind_low, ind_high, leap+1)]
    return out

#print(haltonset(10000, 350, skip=5, leap=4))
