#!/usr/bin/python3.3

import sys

limit = 2000000
big_prime_sum = 0

for prime in sys.stdin:
    if int(prime) < limit:
        big_prime_sum += int(prime)
    else: break

print(big_prime_sum)
