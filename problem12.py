#!/usr/bin/python3.3

digit_sum = 0
digits = str(2**1000)

for n in digits:
    digit_sum += int(n)

print(digit_sum)
