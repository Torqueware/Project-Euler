#!/usr/bin/python3.3

limit = 10**999
fibonacci = [1, 1]

while fibonacci[len(fibonacci) - 1] < limit:
    n = fibonacci[len(fibonacci) - 1] + fibonacci[len(fibonacci) - 2]
    fibonacci.append(n)

print(len(fibonacci))

