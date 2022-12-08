# Advent of code Year 2022 Day 7 solution
# Author = Vasileios Depastas
# Date = December 2022

from utilities import write_results

class Tree:
    def __init__(self, name, parent=None, size=0):
        self.parent: Tree | None = parent # parent node. Only root node has self.parent = None
        self.children: list[Tree] = [] # empty for leaf nodes i.e. files
        self.name = name
        # self.type = type # dir or file
        self.size = size # file size, 0 if directory initially
    def add_child(self, node):
        assert isinstance(node, Tree)
        self.children.append(node)
    def add_size(self, size):
        self.size += size
    def children_names(self):
        return [child.name for child in self.children]
    def __repr__(self):
        return f'{self.name}, size={self.size}, children={self.children_names()}'

def command_split(line: str, current_node: Tree):
    splitted_line = line.split()
    match splitted_line:
        case ['$', 'cd', '/']:
            # move to root node
            curr_node = root
        case ['$', 'cd', '..']:
            # move back to parent directory
            curr_node = current_node.parent
        case ['$', 'cd', child]:
            # move into child directory
            # if child not in [_child.name for _child in current_node.children]: # if child not already created
            #     child_node = Tree(child, 'dir', parent=current_node)
            #     current_node.children.append(child_node)
            for node in current_node.children:
                if node.name == child:
                    curr_node = node
        case ["$", 'ls']:
            curr_node = current_node
            # show directories - ignore, no moves to current node
        case ["dir", dir_name]:
            # create children directory
            if dir_name not in [_child.name for _child in current_node.children]:
                child_node = Tree(dir_name, parent=current_node)
                current_node.add_child(child_node)
            curr_node = current_node
        case [filesize, filename]:
            # child_node = Tree(filename, 'file', parent=current_node, size=int(filesize))
            # current_node.add_child(child_node)
            current_node.add_size(int(filesize))
            curr_node = current_node
        case other:
            curr_node = current_node

    return curr_node

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.read()

root = Tree('root')

previous_node: Tree = root
next_node: Tree = root
for line in input.splitlines():
    previous_node = next_node
    next_node = command_split(line, previous_node)

# PART ONE

# DFS Tree traverse using recursion: post order
def add_size_post_order(_root):
    if _root:
        for child_node in _root.children:
            add_size_post_order(child_node)
        if _root.parent:
            _root.parent.size += _root.size

add_size_post_order(root) # sum directories sizes on the tree structure

small_sized_nodes_list = []

def find_small_sized_nodes(_root, node_list, size_limit=100000):
    if _root:
        for child_node in _root.children:
            new_list = find_small_sized_nodes(child_node, node_list)
        if _root.size <= size_limit:
            return node_list.append((_root.name, _root.size))
        return node_list
            
small_nodes_list: list = find_small_sized_nodes(root, small_sized_nodes_list)
sum = sum([size for dir_name, size in small_nodes_list])

part1 = f'Part1: Sum of all directories sizes <= 100000 is: {sum}'

# PART TWO

all_nodes_list = []

def find_all_sized_nodes(_root, a_list, size_limit):
    if _root:
        for child_node in _root.children:
            a_list.append(find_all_sized_nodes(child_node, a_list, size_limit))
        if _root.name == "root":
            return a_list
        if _root.size >= size_limit:
            return((_root.name, _root.size))

TOTAL_SPACE = 70000000
UPDATE_SPACE = 30000000
total_space_used: int = root.size
if TOTAL_SPACE - total_space_used < UPDATE_SPACE:
    nodes_list: list = find_all_sized_nodes(root, [], total_space_used + UPDATE_SPACE - TOTAL_SPACE)

nodes_list = [node for node in nodes_list if node is not None] # remove None elements
nodes_list.sort(key=lambda x:x[1])
node_to_remove = nodes_list[0]
node_name, node_size = node_to_remove

part2 = f'Part2: Directory to be removed is {node_name} and has a total size of: {node_size}'

# WRITE RESULTS
write_results(__file__, part1, part2)