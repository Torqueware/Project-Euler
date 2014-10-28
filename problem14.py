#!/usr/bin/python3.3

limit = 1000000
longest_chain = 0
longest_chain_length = 0

def chain(sequence):
    n = sequence[len(sequence) - 1]
    if n == 1:
        return sequence
    elif n%2 == 0:
        sequence.append(int(n / 2))
        chain(sequence)
    else:
        sequence.append(3 * n + 1)
        chain(sequence)

def collatz(n):
    new_chain = list()
    new_chain.append(n)

    return(len(chain(new_chain)))

for i in range(1, limit):
    current_chain_length = collatz(i)

    if longest_chain_length < current_chain_length:
        longest_chain = i
        longest_chain_length = current_chain_length

print(longest_chain)

