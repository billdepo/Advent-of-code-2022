# Advent of code Year 2022 Day 2 solution
# Author = Vasileios Depastas
# Date = December 2022

# moves mapping below
#          Rock Paper Scissors
# opponent   A    B      C
# player     X    Y      Z
# score for shape selection: X=1, Y=2, Z=3
# score for round outcome:   loss=0, draw=3, win=6

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.read()

shape_score_map = {
    'X': 1,
    'Y': 2,
    'Z': 3
}

round_score_map = {
    'A': {'Z': 0, 'X': 3, 'Y': 6},
    'B': {'X': 0, 'Y': 3, 'Z': 6},
    'C': {'Y': 0, 'Z': 3, 'X': 6}
}

# PART ONE

def find_round_score(op_move, my_move) -> int:
    total_score = 0
    
    # shape selection score
    total_score += shape_score_map[my_move]

    # round outcome
    total_score += round_score_map[op_move][my_move]

    return total_score

lines: list = input.splitlines()  # creates a list of pairs eg ['C Y', 'C X',...]
total_score = 0

for line in lines:
    opponent_move, my_move = line.split(' ')
    singe_game_score = find_round_score(opponent_move, my_move)
    total_score += singe_game_score

part1 = f"The total score after {len(lines)} individual Rock-Paper-Scissors games following strategy 1 is: {total_score}"

# PART TWO

shape_and_round_score_map_part2 = {
    'A': {'X': 3+0, 'Y': 1+3, 'Z': 2+6},
    'B': {'X': 1+0, 'Y': 2+3, 'Z': 3+6},
    'C': {'X': 2+0, 'Y': 3+3, 'Z': 1+6}
}

total_score_part2 = 0
for line in lines:
    opponent_move, my_move = line.split(' ')
    singe_game_score = shape_and_round_score_map_part2[opponent_move][my_move]
    total_score_part2 += singe_game_score

part2 = f"The total score after {len(lines)} individual Rock-Paper-Scissors games following strategy 2 is: {total_score_part2}"

# WRITE RESULTS

with open((__file__.rstrip("code.py")+"output.txt"), 'w') as output_file:
    output_file.writelines(part1)
    output_file.writelines('\n')
    output_file.writelines(part2)

with open((__file__.rstrip("code.py")+"output.txt"), 'r') as output_file:
    content = output_file.read()
    print(content)
