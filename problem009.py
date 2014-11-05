#!/usr/bin/python3.3

for a in range(1, 1000):
    for b in range(a, 1000):
        for c in range(b, 1000):
            if a + b + c == 1000 and pow(a, 2) + pow(b, 2) == pow(c, 2):
                print(a*b*c)
