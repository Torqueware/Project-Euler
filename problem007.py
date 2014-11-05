#!/usr/bin/python3.3

import sys

i     = 1

for prime in sys.stdin:
    if i > 10000:
        print(prime)
        break
    i += 1
