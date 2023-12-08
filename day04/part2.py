#!/opt/homebrew/bin/python3
# Advent of Code 2023
# Alex Thompson
# Day 04 Part 2

import sys

card_id = 0
card_count = {}

for line in sys.stdin:

    card_id += 1
    if card_id not in card_count:
        card_count[card_id] = 0
    card_count[card_id] += 1

    line = line.strip().split(": ")
    card = line[1].split(" | ")

    winning = card[0].split()
    selected = card[1].split()

    matches = 0
    for number in winning:
        if number in selected:
            matches += 1

    for copy in range(card_count[card_id]):
        for i in range(1, matches+1):
            copy_id = card_id + i
            if copy_id not in card_count:
                card_count[copy_id] = 0
            card_count[copy_id] += 1

print("total cards: " + str(sum(card_count.values())))