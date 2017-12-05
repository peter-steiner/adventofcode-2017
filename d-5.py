#!/user/bin/env python3 -tt

"""
https://adventofcode.com/2017/day/5
"""

import sys

# Global variables
task="d-5.1"
infile=task + ".input"

movement = {"U": 0, "D": 0}
visited = {}

def readInput():
    with open('input\\' + infile) as file:
        data = file.read()
    file.close()
    return data

def jump(loc, steps, instructions):
    if loc in visited:
        visited[loc] += 1
    else:
        visited[loc] 
    print("step to ", visited[steps])
    return instructions[visited[steps]]


def solve_a():
    steps = 0
    instructions = [int(i) for i in readInput().split('\n')]

    jump_ = instructions[0]
    loc = 0
    i = 0
    while i < 1:
        print(jump_, " ", loc)
        if loc > len(instructions):
            i = 1 
        steps += 1
        jump_ = instructions[loc]
        loc += jump_
        instructions[loc] += 1
        print(jump_)
        

    print(instructions)

    print("Solution A: ", steps) 

def solve_b():
    steps = 0

    print("Solution B: ", steps)

if __name__ == '__main__':

    solve_a()
    # solve_b()

    print("Finished executing: " + task)
    sys.exit(1)

