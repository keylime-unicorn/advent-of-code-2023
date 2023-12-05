#!/opt/homebrew/bin/python3
# Advent of Code 2023
# Alex Thompson
# Day 01 Part 2

import sys
import re

values = []
number = "1234567890"
digits = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}

def generate_digits(string):

    occurrences = []

    for n in number:
        for occurrence in list(re.finditer(n, string)):
            t = (occurrence.start(), n)
            occurrences.append(t)

    for d in digits:
        for occurrence in list(re.finditer(d, string)):
            t = (occurrence.start(), digits[d])
            occurrences.append(t)

    return occurrences

for line in sys.stdin:
    line = line.strip()

    indexes = generate_digits(line)
    indexes.sort()
    values.append((int)(indexes[0][1] + indexes[-1][1]))
    
print(sum(values))