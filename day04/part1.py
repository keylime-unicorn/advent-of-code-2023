#!/opt/homebrew/bin/python3
# Advent of Code 2023
# Alex Thompson
# Day 04 Part 1

import sys

total_points = 0

for line in sys.stdin:
    line = line.strip().split(": ")
    card = line[1].split(" | ")

    winning = card[0].split()
    selected = card[1].split()

    matches = 0
    for number in winning:
        if number in selected:
            matches += 1

    if matches > 0:
        total_points += 2**(matches-1)
    
print("points: " + str(total_points))