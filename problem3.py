#!/usr/bin/python3.3
big = 600851475143
limit = big
candidates = []
not_prime = []

def eratosthenes2(n):
    multiples = set()
    for i in range(2, n+1):
        if i not in multiples:
            print(i)
            #candidates.append(i)
            multiples.update(range(i*i, n+1, i))

eratosthenes2(big)
