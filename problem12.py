#!/usr/bin/python3.3

triangles = [1]
i = 2

while True:
    triangles.append(triangles[i - 2] + i)
    divisors = 0

    for d in range(triangles[i - 2], 1, -1):
        if triangles[i - 2]%d == 0:
            divisors += 1

    print("number ", triangles[i - 2], ". divisors ", divisors)

    if divisors > 499:
        break

    i += 1
