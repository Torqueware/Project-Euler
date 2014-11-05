#!/usr/bin/python3.3

import math

limit = 1000000
longest_chain = 0
longest_chain_length = 0

def collatz(n):
    length= 0

    while n > 1:
        if bool(n & 1): n = (3 * n) + 1
        else: n = int(n/2)
        length += 1

    return length

for i in range(1, limit):
    current_chain_length = collatz(i)

    if longest_chain_length < current_chain_length:
        longest_chain = i
        longest_chain_length = current_chain_length

print("final answer", longest_chain)

