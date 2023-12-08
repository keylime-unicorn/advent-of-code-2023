#!/opt/homebrew/bin/python3
# Advent of Code 2023
# Alex Thompson
# Day 02 Part 1

import sys

max_red = 12
max_green = 13
max_blue = 14

game_sum = 0
for line in sys.stdin:
    line = line.strip()
    line = line.split(": ")
    gameid = int(line[0][5:])

    game = line[1].split("; ")
    game_impossible = False

    for hand in game: 

        blocks = hand.split(", ")

        for b in blocks:
            b = b.split(" ")
            count = int(b[0])
            color = b[1]

            if color == "red" and count > max_red:
                game_impossible = True
                break
            elif color == "blue" and count > max_blue:
                game_impossible = True
                break
            elif color == "green" and count > max_green:
                game_impossible = True
                break

        if game_impossible:
            break

    if game_impossible == False:
        game_sum += gameid

print("sum: " + str(game_sum))