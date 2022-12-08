# Advent of code Year 2022 Day 3 solution
# Author = Vasileios Depastas
# Date = December 2022

def priority(charset: set) -> int:
    try: 
        char = next(iter(charset))
    except:
        return 0
    if char.lower() == char:  # if char is lowercase
        priority = ord(char) - 96
    else:
        priority = ord(char) - 38
    return priority

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.read()

# PART ONE

lines: list = input.splitlines()  # creates a list of pairs eg ['C Y', 'C X',...]

priorities_total: int = 0

for line in lines:
    chars: int = len(line)  # only even number of chars in input.txt
    first_half, second_half = set(line[:chars//2]), set(line[chars//2:])
    intersection: set = first_half.intersection(second_half)
    priorities_total += priority(intersection)

part1 = f"The sum of priorities for {len(lines)} rucksacks in Part 1 is: {priorities_total}"

# PART TWO

lines = list(set(zip(*[iter(lines)]*3))) # group in group of 3 consecutive items

priorities_total_2 = 0
for line in lines:
    set0, set1, set2 = [set(string) for string in line]
    intersection: set = set0.intersection(set1, set2)
    priorities_total_2 += priority(intersection)

part2 = f"The sum of priorities for {len(lines)} trinities of rucksacks in Part 2 is: {priorities_total_2}"

# WRITE RESULTS

with open((__file__.rstrip("code.py")+"output.txt"), 'w') as output_file:
    output_file.writelines(part1)
    output_file.writelines('\n')
    output_file.writelines(part2)

with open((__file__.rstrip("code.py")+"output.txt"), 'r') as output_file:
    content = output_file.read()
    print(content)
