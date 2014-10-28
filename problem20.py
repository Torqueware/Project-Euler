#!/usr/bin/python3.3

import math

big_number = str(math.factorial(100))
digit_sum = 0

for c in big_number:
    digit_sum += int(c)

print(digit_sum)
