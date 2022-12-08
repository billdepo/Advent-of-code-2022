# Advent of code Year 2022 Day 5 solution
# Author = Vasileios Depastas
# Date = December 2022

from collections import deque
from utilities import write_results

def parse_letter(cursor, line, chars=4):
    letter = line[cursor: cursor + chars]
    return letter


def initialize_stacks(crates_schema: str) -> list[deque]:
    crates_schema_lines: list = crates_schema.splitlines()
    crates_number: int = int(crates_schema_lines[-1].split()[-1])
    crates_schema_lines = crates_schema_lines[:crates_number - 1] # removes last line with numbers
    crates_schema_lines.reverse() # reverse lines order

    cursor: int = 0
    stacks: list[deque()] = [deque() for _ in range(crates_number)]

    for line in crates_schema_lines:
        for i in range(crates_number):
            if i != crates_number-1:
                letter = parse_letter(cursor, line)
                cursor += 4
            else:
                letter = parse_letter(cursor, line, chars=3)
                cursor = 0
            letter = letter.replace('[', '').replace(']', '').strip() # get pure char by removing brackets
            if letter:
                stacks[i].append(letter) # add letter to appropriate stack 

    return stacks

def move_crates(moves: str, stacks: list[deque], part=1) -> str:
    moves = moves.splitlines()

    # move around crates
    for line_moves in moves:
        items = line_moves.split()
        
        # find queue indexes
        move_items = int(items[1])
        remove_queue_idx = int(items[3])-1
        add_queue_idx = int(items[5])-1

        # move crates part 1
        if part == 1:
            for i in range(move_items):
                item = stacks[remove_queue_idx].pop()
                stacks[add_queue_idx].append(item)
        elif part == 2:       
            items_list = []
            for i in range(move_items):
                item = stacks[remove_queue_idx].pop()
                items_list.append(item)
            items_list.reverse()
            for item in items_list:
                stacks[add_queue_idx].append(item)

    stacks_top: str = ""
    for stack in stacks:
        if stack:
            stacks_top = f'{stacks_top}{stack.pop()}'
        else:
            stacks_top = f'{stacks_top} '

    return stacks_top

# PART ONE

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.read()

crates_schema, moves = input.split('\n\n')

init_stacks = initialize_stacks(crates_schema)
stacks_top_p1 = move_crates(moves, [stack.copy() for stack in init_stacks])
part1 = f"Part1: The crates on top of each stack after {len(moves.splitlines())} rearrangement moves are: {stacks_top_p1}"

# PART TWO

stacks_top_p2 = move_crates(moves, [stack.copy() for stack in init_stacks], part=2)
part2 = f"Part2: The crates on top of each stack after {len(moves.splitlines())} rearrangement moves are: {stacks_top_p2}"

# WRITE RESULTS

write_results(__file__, part1, part2)
