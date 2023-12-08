#!/opt/homebrew/bin/python3
# Advent of Code 2023
# Alex Thompson
# Day 02 Part 2

import sys

powers_sum = 0
for line in sys.stdin:
    line = line.strip()
    line = line.split(": ")
    game = line[1].split("; ")

    max_red = 0
    max_blue = 0
    max_green = 0
    for hand in game: 

        blocks = hand.split(", ")

        for b in blocks:
            b = b.split(" ")
            count = int(b[0])
            color = b[1]

            if color == "red" and count > max_red:
                max_red = count
            elif color == "blue" and count > max_blue:
                max_blue = count
            elif color == "green" and count > max_green:
                max_green = count

    game_power = max_red * max_green * max_blue
    powers_sum += game_power

print("total power: " + str(powers_sum))