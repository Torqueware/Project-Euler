#!/usr/bin/python3.3

import math
#answer math.factorial(20)
answer   = 2*3*4*5*6*7*11*13*17*19
divisors = [20,19,18,17,16,15,14,13,12,11,10,9,8,7,6,5,4,3,2]

#primes  1  2  3     5     7
#       11    13          17    19

#total   1  2  3  4  5  6  7  8  9 10
#       11 12 13 14 15 16 17 18 19 20
def divisible(n):
    for x in divisors:
        if n%x != 0:
            return False
    return True

for n in range(answer, 0, -1):
    if divisible(n):
        print(n)
        answer = n
