mkdir day{01..25}
touch day{01..25}/part{1..2}.py

echo "#!/opt/homebrew/bin/python3
# Advent of Code 2023
# Alex Thompson
# Day XX Part 1" > part1.py

echo "#!/opt/homebrew/bin/python3
# Advent of Code 2023
# Alex Thompson
# Day XX Part 2" > part2.py 

tee ./day*/part1.py < part1.py
tee ./day*/part2.py < part2.py

echo "*.txt" > .gitignore