from sys import argv
from math import sqrt, gcd

def phi(mn):
	if mn > 2:
		divisor = 2
		r = mn - 1

		limit = int(sqrt(mn) + 1)

		while divisor < limit:
			if not mn % divisor:
				k = mn // divisor
				prime_power = divisor
				prev_prime_power = 1

				while not k % divisor:
					k //= divisor
					prev_prime_power, prime_power = prime_power, prime_power * divisor

				r = prime_power - prev_prime_power

				if k > 1:
					if k > 2:
						r *= phi(k)
					d = gcd(prime_power, k)
					if d > 1:
						r *= d
						r //= phi(d)
						
				break

			divisor += 1 + divisor % 2
	else:
		r = 1

	return r

for arg in argv[1:]:
	a = int(arg)

	print("phi({}) = {}".format(a, phi(a)))
