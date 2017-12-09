#!/user/bin/env python3 -tt

"""
https://adventofcode.com/2017/day/5
"""

import sys

# Global variables
task="d-5"
infile=task + ".input"

def readInput():
    with open('input/' + infile) as file:
        data = file.read()
    file.close()
    return data

def solve_a():
    instructions = [int(i) for i in readInput().split('\n')]

    index = 0
    iterations = 0
    while index < len(instructions):
        steps = instructions[index]
        instructions[index] = steps + 1;
        index += steps
        iterations +=1

    print("Solution A: ", iterations) 

def solve_b():
    steps = 0

    instructions = [int(i) for i in readInput().split('\n')]
    offsets = [0 for i in range(len(instructions))]
    # print(len(offsets), len(instructions))

    index = 0
    steps = 0
    iterations = 0
    while index < len(instructions):
        op = 1
        if instructions[index] >= 3:
            op = -1 

        steps = instructions[index]
        instructions[index] = steps + op
        index += steps
        iterations +=1
        
    print("Solution B:", iterations)

if __name__ == '__main__':
    solve_a()
    solve_b()

    print("Finished executing:", task)
    sys.exit(1)

"""
Solution A:  354121
Solution B:  27283023
"""