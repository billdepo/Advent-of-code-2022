# Advent of code Year 2022 Day 6 solution
# Author = Vasileios Depastas
# Date = December 2022

from utilities import write_results

def read_char(input: str):
    for c in input:
        yield c

def start_of_packet_marker(input, distinct_chars_number=4) -> int:
    char_generator = read_char(input) # create a char generator

    chars_count: int = 0
    idx: int = -1
    chars_seen = []
    while chars_count < distinct_chars_number:
        current_char: str = next(char_generator)

        if current_char not in chars_seen:
            chars_count += 1
            chars_seen.append(current_char)
        else:
            idx_update = chars_seen.index(current_char)
            chars_seen = chars_seen[idx_update+1: ]
            chars_seen.append(current_char)
            chars_count = len(chars_seen)
        
        idx += 1
    return idx + 1

# PART ONE

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.read()

p1 = start_of_packet_marker(input)
part1 = f'Part1: On the signal comprised of {len(input)} characters, {p1} characters have to be processed before the first start-of-packet marker is detected'

# PART TWO

p2 = start_of_packet_marker(input, 14)
part2 = f'Part2: On the signal comprised of {len(input)} characters, {p2} characters have to be processed before the first start-of-message marker is detected'

# WRITE RESULTS
write_results(__file__, part1, part2)