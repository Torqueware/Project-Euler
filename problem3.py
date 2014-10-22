#!/usr/bin/python3.3
big = 600851475143
limit = big
candidates = []
not_prime = []

for i in range(3, limit, 2):
    if big%i == 0: candidates.append(i)
for n in candidates:
    for i in range(3, n, 2):
        if n%i == 0:
            not_prime.append(n)
            break
print("Candidates")
for n in candidates:
    prime = true
    for i in not_prime:
        if n == i: prime = false
    if prime: print(n)
