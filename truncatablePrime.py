# Primality testing as taken from http://rosettacode.org/wiki/Miller-Rabin_primality_test#Python
# Not proven for very large primes, but probably (?) right?
# TODO: try better set from http://miller-rabin.appspot.com/
from itertools import chain

def _try_composite(a, d, n, s):
    if pow(a, d, n) == 1:
        return False
    for i in range(s):
        if pow(a, 2**i * d, n) == n-1:
            return False
    return True # n  is definitely composite
 
def is_prime(n, _precision_for_huge_n=16):
    if n in _known_primes or n in (0, 1):
        return True
    if any((n % p) == 0 for p in _known_primes):
        return False
    d, s = n - 1, 0
    while not d % 2:
        d, s = d >> 1, s + 1
    # Returns exact according to http://primes.utm.edu/prove/prove2_3.html
    if n < 1373653: 
        return not any(_try_composite(a, d, n, s) for a in (2, 3))
    if n < 25326001: 
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5))
    if n < 118670087467: 
        if n == 3215031751: 
            return False
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7))
    if n < 2152302898747: 
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7, 11))
    if n < 3474749660383: 
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7, 11, 13))
    if n < 341550071728321: 
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7, 11, 13, 17))
    # otherwise
    return not any(_try_composite(a, d, n, s) 
                   for a in _known_primes[:_precision_for_huge_n])
 
_known_primes = [2, 3]
_known_primes += [x for x in range(5, 1000, 2) if is_prime(x)]


def rtrunc_primes():
    """Generate a set of all right-truncatable primes"""
    rprimes = [[2, 3, 5, 7]]      # Seed with 1-digit primes
    rdigits = [1, 3, 7, 9]      # Only possible digits after first digit

    n = 2
    while rprimes[n-2]:         # Continue as long as we have found a prime in the previous n
        nprimes = [p for base in rprimes[n-2] for p in [10*base+d for d in rdigits ] if is_prime (p)]
        rprimes.append(nprimes)
        n += 1
    return {p for p in chain.from_iterable(rprimes)}

def ltrunc_primes():
    """Generate a set of all left-truncatable primes"""
    lprimes = [[2, 3, 5, 7]]      # Seed with 1-digit primes
    ldigits = range(1,10)      # Only possible digits after first digit

    n = 2
    factor = 1
    while lprimes[n-2]:         # Continue as long as we have found a prime in the previous n
        factor *= 10            # We need to stick the digits to the front, so mult with factor
        nprimes = [p for base in lprimes[n-2] for p in [base + l * factor for l in ldigits] if is_prime(p)]
        lprimes.append(nprimes)
        n += 1
    return {p for p in chain.from_iterable(lprimes)}


rtrunc_primes = rtrunc_primes()
ltrunc_primes = ltrunc_primes()

tprimes = sorted(list(rtrunc_primes & ltrunc_primes))

print "Truncatable primes: ", tprimes
print "Sum minus 1-digit primes: ", sum(tprimes[4:])
print "Number of truncatable primes: ", len(tprimes)
