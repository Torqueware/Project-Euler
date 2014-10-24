#!/usr/bin/python3.3

answer = 0

def isPalindrome(string):
    for i in range(0, int(len(string)/2)):
        if string[i] != string[len(string) - i - 1]:
            return False
    return True

for i in range(999, 99, -1):
    for j in range(i, 99, -1):
        if isPalindrome(str(i * j)) and i * j > answer:
            answer = i * j

print(answer)
