#!/usr/bin/python3.3

import math

big    = 600851475143
limit  = int(math.sqrt(big))
prime = list()
prime = [False] * (limit + 1)

candidates = []
not_prime = []

for x in range(1, int(math.sqrt(limit)) + 1):
    for y in range(1, int(math.sqrt(limit)) + 1):
        n = 4 * x**2 + y**2

        if n <= limit and (n%12 == 1 or n%12 == 5):
            prime[n] = not prime[n]

        n = 3 * x**2 + y**2
        if n <= limit and n%12 == 7:
            prime[n] = not prime[n]

        n = 3 * x**2 - y**2
        if x > y and n <= limit and n%12 == 11:
            prime[n] = not prime[n]

for n in range(5, int(math.sqrt(limit))):
    if prime[n]:
        for k in range(n**2, limit + 1, n**2):
            prime[k] = False

for n in range(5, limit):
    if prime[n] and big%n == 0:
        print(n)
