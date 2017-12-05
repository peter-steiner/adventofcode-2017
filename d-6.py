#!/user/bin/env python3 -tt

"""
https://adventofcode.com/2017/day/6
"""

import sys

# Global variables
task="d-6"
infile=task + ".input"


def readInput():
    with open('input/' + infile) as file:
        input = file.read()
    file.close()
    return input


def solve_a():
    input = readInput()

    print("Solution A: ") 

def solve_b():

    print("Solution B: ")

if __name__ == '__main__':

    solve_a()
    solve_b()

    print("Finished executing: " + task)
    sys.exit(1)
