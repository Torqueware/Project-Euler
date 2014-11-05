#!/usr/bin/python3.3

triangles = [1, 3, 6, 10, 15, 21, 28]
i = 8

while True:
    triangles.append(triangles[i - 2] + i)
    divisors = 2

    for d in range(2, triangles[i - 2] - 1):
        f = triangles[i - 2]/d
        if d > f:
            break
        if triangles[i - 2]%d == 0:
            divisors += 1
            if triangles[i - 2]%f == 0:
                divisors += 1

    print("number ", triangles[i - 2], ". divisors ", divisors)

    if divisors > 499:
        break

    i += 1
