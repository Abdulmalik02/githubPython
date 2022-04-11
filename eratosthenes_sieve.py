import math
def erato(n):
    """Input: number (n) that you want to find all prime numer smaller than
    Output: list of all the prime numbers smaller than 'n' """

    #creating a dict of numbers from 2 to n, set to true
    arr = {}
    for i in range(2, n):
        arr[i] = True

    #sorting through numbers to determine which one is prime
    #using the a eratosthenes algorithm
    for i in range(2, math.ceil(math.sqrt(n))):
        if arr[i]:
            for j in range(i**2, n, i):
                arr[j] = False

    primes = [i for i in range(2, n) if arr[i]]
    return primes

print(erato(100))
