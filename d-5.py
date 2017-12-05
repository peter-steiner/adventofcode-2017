#!/user/bin/env python3 -tt

"""
https://adventofcode.com/2017/day/5
"""

import sys

# Global variables
task="d-5"
infile=task + ".input"

movement = {"U": 0, "D": 0}


def readInput():
    with open('input/' + infile) as file:
        data = file.read()
    file.close()
    return data


def solve_a():
    instructions = [int(i) for i in readInput().split('\n')]
 #   print(instructions)

    index = instructions[0]
    iterations = 0
    while index < len(instructions):
        print(index)
        steps = instructions[index]
        instructions[index] = steps + 1;
        index += steps
        iterations +=1

    iterations +=1    
    print("Solution A: ", iterations) 

def solve_b():
    steps = 0

    print("Solution B: ", steps)

if __name__ == '__main__':

    solve_a()
    # solve_b()

    print("Finished executing: " + task)
    sys.exit(1)

#354120 wrong, to low