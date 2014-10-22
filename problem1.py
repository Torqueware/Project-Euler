#!/usr/bin/python3.3
ans = 0
threes = []

for i in range(1, 1000):
    if i%3 == 0 and i%5 == 0:
        threes.append(i)
    elif i%3 == 0:
        threes.append(i)
    elif i%5 == 0:
        threes.append(i)

print(sum(threes))
