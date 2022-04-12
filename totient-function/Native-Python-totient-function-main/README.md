# Native-Python-totient-function
Reasonably optimized version of Euler's phi in pure Python.

I built a simple recursion on the identities
* phi(p^k) = p^k - p^(k-1)
* phi(mn) = phi(m) phi(n) gcd(m, n) / phi(gcd(m, n))
  
No prime sieve, just trial division, so there is definitely room for improvement here.
