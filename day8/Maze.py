from collections import defaultdict
import math
from functools import reduce


# prepare input
f = open("input.txt","r")
data = f.read()
seq, nodes = data.split("\n\n")
N = len(seq)
nodes = nodes.split("\n")
maze = defaultdict(list)
for node in nodes:
    node, neighbor = node.split(" = ")
    neighbor = neighbor[1:-1].split(", ")
    maze[node] = neighbor



def part_1():

    # transverse graph and calculate steps
    curr_node = 'AAA'
    steps = 0

    while curr_node != "ZZZ":
        if seq[steps%N] == "R":
            curr_node = maze[curr_node][1]
        else:
            curr_node = maze[curr_node][0]

        steps +=1

    return steps

print(f'result part 1 : {part_1()}')

def part_2():
    # idefntify all starting points
    curr_nodes = []
    for node in maze.keys():
        if node[-1] == "A":
            curr_nodes.append(node)


    # store required step for each starting node
    super_step = []
    for node in curr_nodes:
        curr_node = node
        steps = 0
        while curr_node[-1] != "Z":
            if seq[steps % N] == "R":
                curr_node = maze[curr_node][1]
            else:
                curr_node = maze[curr_node][0]

            steps += 1
        super_step.append(steps)

    # answer is lcm of each step
    return reduce(math.lcm,super_step)




print(f'result part 2 : {part_2()}')


