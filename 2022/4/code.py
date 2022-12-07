# Advent of code Year 2022 Day 4 solution
# Author = ?
# Date = December 2022

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.read()


# PART ONE

def is_subset(range1: str, range2: str) -> bool:
    r1_start, r1_end = [int(string) for string in range1.split('-')]
    r2_start, r2_end = [int(string) for string in range2.split('-')]
    
    if (r1_start <= r2_start and r1_end >= r2_end) or (r2_start <= r1_start and r2_end >= r1_end): # if one set completely includes the other one
        return True
    
    return False # else case

subsets_count: int = 0

lines: list = input.splitlines()  # creates a list of items
for line in lines:
    range1, range2 = line.split(',')
    subsets_count += is_subset(range1, range2)

part1 = f"The number of assignment pairs out of {len(lines)} pairs where one range fully contains the other is: {subsets_count}"

# PART TWO

def overlap(range1: str, range2: str) -> bool:
    r1_start, r1_end = [int(string) for string in range1.split('-')]
    r2_start, r2_end = [int(string) for string in range2.split('-')]
    
    if (r1_start <= r2_end <= r1_end) or (r1_start <= r2_start <= r1_end) or (r2_start <= r1_end <= r2_end) or (r2_start <= r1_start <= r2_end):
        print(f'{range1} {range2} : True')
        return True

    print(f'{range1} {range2} : False')
    
    return False # else case

overlaps_count: int = 0

lines: list = input.splitlines()  # creates a list of items
for line in lines:
    range1, range2 = line.split(',')
    overlaps_count += overlap(range1, range2)

part2 = f"The number of assignment pairs out of {len(lines)} pairs where one range fully overlaps with the other is: {overlaps_count}"

# WRITE RESULTS

with open((__file__.rstrip("code.py")+"output.txt"), 'w') as output_file:
    output_file.writelines(part1)
    output_file.writelines('\n')
    output_file.writelines(part2)

with open((__file__.rstrip("code.py")+"output.txt"), 'r') as output_file:
    content = output_file.read()
    print(content)
