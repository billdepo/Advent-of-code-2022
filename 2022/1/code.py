# Advent of code Year 2022 Day 1 solution
# Author = Vasileios Depastas
# Date = December 2022

# how many Calories are being carried by the Elf carrying the most Calories

import numpy as np

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.read()

input_list: list[str] = input.split('\n')
calories: np.ndarray = np.array([])

# PART ONE

elf_calories = 0
for calories_entry in input_list:
    try:
        elf_calories += int(calories_entry)  # all numbers except empty string will succeed and be converted to int
    except:  # means we have encountered and empty string
        calories = np.append(calories, elf_calories)
        elf_calories = 0

part1 = f"The max calories carried by an elf are: {int(calories.max())} calories"

# PART TWO

calories = -np.sort(-calories)  # sort in descending order
part2 = f"The 3 elves that carry the maximum calories are carrying in total: {int(calories[:3].sum())} calories"


# WRITE RESULTS

with open((__file__.rstrip("code.py")+"output.txt"), 'w') as output_file:
    output_file.writelines(part1)
    output_file.writelines('\n')
    output_file.writelines(part2)

with open((__file__.rstrip("code.py")+"output.txt"), 'r') as output_file:
    content = output_file.read()
    print(content)