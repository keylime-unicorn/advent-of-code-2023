#!/opt/homebrew/bin/python3
# Advent of Code 2023
# Alex Thompson
# Day 01 Part 1

import sys

values = []
alpha = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

for line in sys.stdin:
    line = line.strip()
    line = line.translate({ord(i): None for i in alpha})
    values.append((int)(line[0] + line[-1]))
    
print(sum(values))