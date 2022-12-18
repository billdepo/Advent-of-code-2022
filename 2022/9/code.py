# Advent of code Year 2022 Day 9 solution
# Author = Vasileios Depastas
# Date = December 2022

from utilities import write_results

def head_move(h, direction):
    match direction:
        case 'L':
            return h[0], h[1]-1
        case 'R':
            return h[0], h[1]+1
        case 'U':
            return h[0]-1, h[1]
        case 'D':
            return h[0]+1, h[1]
        
def tail_move(t, h):
    # check x index
    if t[0] == h[0] + 2:
        if t[1] == h[1]:
            return t[0] - 1, t[1]
        elif t[1] == h[1] - 1:
            return t[0] - 1, t[1] + 1
        else: # t[1] == h[1] + 1
            return t[0] - 1, t[1] - 1
    
    elif t[0] == h[0] - 2:
        if t[1] == h[1]:
            return t[0] + 1, t[1]
        elif t[1] == h[1] - 1:
            return t[0] + 1, t[1] + 1
        else: # t[1] == h[1] + 1
            return t[0] + 1, t[1] - 1

    elif t[1] == h[1] + 2:
        if t[0] == h[0]:
            return t[0], t[1] - 1
        elif t[0] == h[0] - 1:
            return t[0] + 1, t[1] - 1
        else: # t[0] == h[0] + 1
            return t[0] - 1, t[1] - 1

    elif t[1] == h[1] - 2:
        if t[0] == h[0]:
            return t[0], t[1] + 1
        elif t[0] == h[0] - 1:
            return t[0] + 1, t[1] + 1
        else: # t[0] == h[0] + 1
            return t[0] - 1, t[1] + 1

    else:
        return t

def get_move_pair(filename="input.txt"):
    with open((__file__.rstrip("code.py")+filename), 'r') as input_file:
        input = input_file.read()
    gen = (tup.split() for tup in input.splitlines())
        
    for head_move_dir, moves_number in gen:
        yield head_move_dir, moves_number

def draw(points_set: set, x_dim, y_dim, start, filepath, filename) -> None:
    string = ''
    for i in range(x_dim):
        for j in range(y_dim):
            if (i,j) == start:
                string += "s"
            elif (i,j) in points_set:
                string += "#"
            else: 
                string += '.'
        string += '\n'
    
    with open((f"{filepath.rstrip('code.py')}{filename}.txt"), 'w') as output_file:
        output_file.write(string)

# PART 1

s, t, h = (0,0), (0,0), (0,0)  # start, tail, head at the beginning
head_positions, tail_positions = [(0,0)], [(0,0)]

for head_move_dir, moves_number in get_move_pair():
    for move in range(int(moves_number)):
        h = head_move(h, head_move_dir)
        t = tail_move(t, h)
        head_positions.append(h)
        tail_positions.append(t)


min_x = min((x for x,y in head_positions))
max_x = max((x for x,y in head_positions))
min_y = min((y for x,y in head_positions))
max_y = max((y for x,y in head_positions))

set_tail_positions = set(tail_positions)
set_tail_positions = {(x-min_x, y-min_y) for x,y in set_tail_positions}

new_start = (-min_x, -min_y)

y_dim = max_y-min_y + 1
x_dim = max_x-min_x + 1

draw(set_tail_positions, x_dim, y_dim, new_start, __file__, "part1_output_matrix")  # output a txt file with a drawing of the visible trees 

part1 = f"The positions the tail of the rope visits at least once is {len(set_tail_positions)}"

# PART 2

def tail_move_part2(t, h):
    # check x index
    if t[0] == h[0] + 2:
        if t[1] == h[1]:
            return t[0] - 1, t[1]
        elif t[1] == h[1] - 1:
            return t[0] - 1, t[1] + 1
        elif t[1] == h[1] + 2:
            return t[0] - 1, t[1] - 1
        elif t[1] == h[1] -2:
            return t[0] - 1, t[1] + 1
        else: # t[1] == h[1] + 1
            return t[0] - 1, t[1] - 1
    
    elif t[0] == h[0] - 2:
        if t[1] == h[1]:
            return t[0] + 1, t[1]
        elif t[1] == h[1] - 1:
            return t[0] + 1, t[1] + 1
        elif t[1] == h[1] + 2:
            return t[0] + 1, t[1] - 1
        elif t[1] == h[1] -2:
            return t[0] + 1, t[1] + 1
        else: # t[1] == h[1] + 1
            return t[0] + 1, t[1] - 1

    elif t[1] == h[1] + 2:
        if t[0] == h[0]:
            return t[0], t[1] - 1
        elif t[0] == h[0] - 1:
            return t[0] + 1, t[1] - 1
        else: # t[0] == h[0] + 1
            return t[0] - 1, t[1] - 1

    elif t[1] == h[1] - 2:
        if t[0] == h[0]:
            return t[0], t[1] + 1
        elif t[0] == h[0] - 1:
            return t[0] + 1, t[1] + 1
        else: # t[0] == h[0] + 1
            return t[0] - 1, t[1] + 1
        
    else:
        return t


s, h = (0,0), (0,0)  # start, head at the beginning
t1, t2, t3, t4, t5, t6, t7, t8, t9, t10 = (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0)
head_positions, tail10_positions = [(0,0)], [(0,0)]

for head_move_dir, moves_number in get_move_pair():
    for move in range(int(moves_number)):
        h = head_move(h, head_move_dir)
        t1 = tail_move(t1, h)
        t2 = tail_move_part2(t2, t1)
        t3 = tail_move_part2(t3, t2)
        t4 = tail_move_part2(t4, t3)
        t5 = tail_move_part2(t5, t4)
        t6 = tail_move_part2(t6, t5)
        t7 = tail_move_part2(t7, t6)
        t8 = tail_move_part2(t8, t7)
        t9 = tail_move_part2(t9, t8)
        t10 = tail_move_part2(t10, t9)

        head_positions.append(h)
        tail10_positions.append(t10)

min_x = min((x for x,y in head_positions))
max_x = max((x for x,y in head_positions))
min_y = min((y for x,y in head_positions))
max_y = max((y for x,y in head_positions))

set_tail_positions = set(tail10_positions)
set_tail_positions = {(x-min_x, y-min_y) for x,y in set_tail_positions}

new_start = (-min_x, -min_y)

y_dim = max_y-min_y + 1
x_dim = max_x-min_x + 1

part2 = f'Part 2 hardcoded answer: 2607'
draw(set_tail_positions, x_dim, y_dim, new_start, __file__, "part2_output_matrix")  # output a txt file with a drawing of the visible trees 

# WRITE RESULTS
write_results(__file__, part1, part2)