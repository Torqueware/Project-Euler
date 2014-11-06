#!/usr/bin/python3.3

import math

letter_sum   = 0
number_list  = []
numbers1     = ["", "one", "two", "three", "four", "five", "six", "seven",     \
                "eight", "nine", "ten", "eleven", "twelve", "thirteen",        \
                "fourteen", "fifteen", "sixteen", "seventeen", "eighteen",     \
                "nineteen"]
numbers2     = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy",  \
                "eighty", "ninety"]
numbers3     = ["", "one hundred", "two hundred", "three hundred",             \
                "four hundred", "five hundred", "six hundred",                 \
                "seven hundred", "eight hundred", "nine hundred"]

for i in range(1, 1000):
    number_line = []

    if i < 20:
        number_line.append(numbers1[i])
    elif i < 100:
        number_line.append(numbers2[int(math.floor(i/10))])
        if i%10 > 0:
            number_line.append(numbers1[i%10])
    elif i%100 == 0:
        number_line.append(numbers3[int(i/100)])
    elif i > 100:
        number_line.append(numbers3[int(i/100)])
        number_line.append("and")
        if int(i%100) < 20:
            number_line.append(numbers1[(i%100)])
        else:
            number_line.append(numbers2[int(math.floor((i%100)/10))])
            if i%10 > 0:
                number_line.append(numbers1[i%10])

    number_list.extend(number_line)

number_list.append("one thousand")

for s in number_list:
    for c in s:
        if c != ' ':
            letter_sum += 1

print(letter_sum)

