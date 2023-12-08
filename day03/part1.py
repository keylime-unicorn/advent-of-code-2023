#!/opt/homebrew/bin/python3
# Advent of Code 2023
# Alex Thompson
# Day 03 Part 1

import sys
import re

numbers = "1234567890"
delim = "."
special = ".^$*+?"
symbols = set()

engine = []
parts = []

for line in sys.stdin:
    line = line.strip()
    for l in line:
        if l != delim and l not in numbers:
            symbols.add(l)
    engine.append(line)
    
max_x = len(engine)
max_y = len(engine[0])

for x, row in enumerate(engine):

    #print(row)

    for symbol in symbols:
            
        if symbol in special:
            indexes = [m.start() for m in re.finditer("\\" + symbol, row)] 
        else:
            indexes = [m.start() for m in re.finditer(symbol, row)]    

        #print(symbol, indexes)

        for y in indexes:

            # N (x-1, y)
            if x > 0 and engine[x-1][y] in numbers:

                from_left = ""
                to_right = ""

                if y > 0:
                    from_left = engine[x-1][:y].split(delim)[-1]
                if y < max_y:
                    to_right = engine[x-1][y+1:].split(delim)[0]

                parts.append(from_left + engine[x-1][y] + to_right)

            else:

                # NW (x-1, y-1) 
                if x > 0 and y > 0 and engine[x-1][y-1] in numbers: 
                    from_left = engine[x-1][:y].split(delim)[-1]
                    parts.append(from_left)

                # NE (x-1, y+1)
                if x > 0 and y < max_y and engine[x-1][y+1] in numbers:
                    to_right = engine[x-1][y+1:].split(delim)[0]
                    parts.append(to_right)

            # E (x, y+1) 
            if y < max_y and engine[x][y+1] in numbers:
                to_right = engine[x][y+1:].split(delim)[0]
                parts.append(to_right)

            # W (x, y-1)
            if y > 0 and engine[x][y-1] in numbers:
                from_left = engine[x][:y].split(delim)[-1]
                parts.append(from_left)

            # S (x+1, y)
            if x < max_x and engine[x+1][y] in numbers:

                from_left = ""
                to_right = ""

                if y > 0:
                    from_left = engine[x+1][:y].split(delim)[-1]
                if y < max_y:
                    to_right = engine[x+1][y+1:].split(delim)[0]

                parts.append(from_left + engine[x+1][y] + to_right)

            else:

                # SW (x+1, y-1)
                if x < max_x and y > 0 and engine[x+1][y-1] in numbers:
                    from_left = engine[x+1][:y].split(delim)[-1]
                    parts.append(from_left)

                # SE (x+1, y+1)
                if x < max_x and y < max_y and engine[x+1][y+1] in numbers:
                    to_right = engine[x+1][y+1:].split(delim)[0]
                    parts.append(to_right)

parts = [int(p) for p in parts]
print("sum: " + str(sum(parts)))