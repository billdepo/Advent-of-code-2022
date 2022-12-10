from collections import deque  # stack usage
import numpy as np 

from utilities import write_results

# PART ONE - using stacks

class stack(deque):
    """
    Modification of deque to have more intuitive methods for a stack
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    def top(self):
        return self.__getitem__(-1)
    def push(self, value):
        return self.append(value)
    def is_empty(self):
        return len(self) == 0
    def is_non_empty(self):
        return not self.is_empty()

def find_visible_trees(input_tree_list: list[str]) -> set:
    """
    For a given list, find the indexes that are visible when looking from left to right and store them in forward_stack.
    Equally, find and store the indexes when looking from right to left in backward_stack. 
    """
    tree_list: list[int] = [int(item) for item in input_tree_list]

    forward_stack: stack = stack()
    
    for i in range(len(tree_list)):
        current_item = tree_list[i]

        # populate forward stack 
        if (forward_stack.is_empty()) or (current_item > tree_list[forward_stack.top()]):
            forward_stack.push(i)

    return set(forward_stack)

def add_second_coordinate(trees_set: set, axis_idx, traverse_axis='x'):
    """
    Populate the returned sets from find_visible_trees() function with the second coordinate of the tree on the grid. Coordinates: (n, m), n,m >= 0
    """
    if traverse_axis == 'x':  # add x (row) coordinate
        return {(axis_idx, col_idx) for col_idx in trees_set}
    else: # traverse_axis='y'
        return {(row_idx, axis_idx) for row_idx in trees_set}

def draw(points_set: set, dim, filepath, filename) -> None:
    """
    Takes a set of points with (x, y) coordinates and produces a txt file with star symbol * at the corresponding positions
    Any other point (x, y) not in set is drawn as a space ' ' char
    """
    string = ''
    for i in range(dim):
        for j in range(dim):
            if (i,j) in points_set:
                string += "*"
            else: 
                string += ' '
        string += '\n'
    
    with open((f"{filepath.rstrip('code.py')}{filename}.txt"), 'w') as output_file:
        output_file.write(string)

# file read
with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.read()

# main logic
horizontal_lines = input.split()
vertical_lines = zip(*horizontal_lines)

all_points_set = set()

axis_idx = 0
for horizontal_line, vertical_line in zip(horizontal_lines, vertical_lines):
    # horizontal traverse
    _horizontal_line = [*horizontal_line]
    forward_one_dim_set = find_visible_trees(_horizontal_line)
    backward_one_dim_set = find_visible_trees(_horizontal_line[::-1])
    backward_one_dim_set = {len(_horizontal_line)-1-item for item in backward_one_dim_set}  # fix index since it was in reverse order
    horizontal_one_dim_set = forward_one_dim_set.union(backward_one_dim_set)
    horizontal_two_dim_set = add_second_coordinate(horizontal_one_dim_set, axis_idx=axis_idx)

    # vertical traverse
    downward_one_dim_set = find_visible_trees(vertical_line)
    upward_one_dim_set = find_visible_trees(vertical_line[::-1])
    upward_one_dim_set = {len(vertical_line)-1-item for item in upward_one_dim_set}  # fix index since it was in reverse order
    vertical_one_dim_set = downward_one_dim_set.union(upward_one_dim_set)
    vertical_two_dim_set = add_second_coordinate(vertical_one_dim_set, axis_idx=axis_idx, traverse_axis='y')

    all_points_set = all_points_set.union(horizontal_two_dim_set).union(vertical_two_dim_set)
    axis_idx += 1

trees_visible = len(all_points_set)
part1 = f"The number of trees visible from outside of the grid of size {axis_idx} x {axis_idx} is: {trees_visible}"
draw(all_points_set, axis_idx, __file__, "part1_output_tree")  # output a txt file with a drawing of the visible trees 

# PART 2

def find_scenic_trees(input_tree_list: list[str]) -> list:
    tree_list: list[int] = [int(item) for item in input_tree_list]

    forward_stack: stack = stack()
    scenic_scores = [0 for item in tree_list]

    for i in range(len(tree_list)):
        current_item = tree_list[i]

        # populate forward stack 
        if forward_stack.is_empty():
            scenic_scores[i] = 0
        else:
            if current_item > tree_list[forward_stack.top()]:
                scenic_scores[i] = scenic_scores[i-1] + 1
            else:
                scenic_scores[i] = 1
        
        forward_stack.push(i)

    return scenic_scores

vertical_lines = zip(*horizontal_lines)
idx = 0
scenic_arr_hz = np.zeros((axis_idx, axis_idx))
scenic_arr_vc = np.zeros((axis_idx, axis_idx))

for horizontal_line, vertical_line in zip(horizontal_lines, vertical_lines):
    # horizontal traverse
    _horizontal_line = [*horizontal_line]
    scenic_scores_forward = find_scenic_trees(_horizontal_line)
    scenic_scores_backward = find_scenic_trees(_horizontal_line[::-1])[::-1]
    horizontal_product = [scenic_scores_forward[i] * scenic_scores_backward[i] for i in range(len(scenic_scores_forward))]
    scenic_arr_hz[idx] = horizontal_product

    # vertical traverse
    scenic_scores_downward = find_scenic_trees(vertical_line)
    scenic_scores_upward = find_scenic_trees(vertical_line[::-1])[::-1]
    vertical_product = [scenic_scores_downward[i] * scenic_scores_upward[i] for i in range(len(scenic_scores_downward))]
    scenic_arr_vc[:, idx] = vertical_product

    idx += 1

scenic_scores_array = np.multiply(scenic_arr_hz, scenic_arr_vc).astype(int)
highest_scenic_score = int(np.max(scenic_scores_array))

np.savetxt(f"{__file__.rstrip('code.py')}part2_output_tree.txt", scenic_scores_array, fmt="%d")

part2 = f"The hightest scenic score possible for any tree is {highest_scenic_score}"

# WRITE RESULTS
write_results(__file__, part1, part2)