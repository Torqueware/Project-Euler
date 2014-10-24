#!/usr/bin/python3.3

import math

SumSquare = 0
SquareSum = 0

for n in range(1, 101):
    SumSquare += pow(n, 2)
print(SumSquare)
for n in range(1, 101):
    SquareSum += n
SquareSum = pow(SquareSum, 2)
print(SquareSum)
print(SquareSum-SumSquare)


