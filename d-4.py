#!/user/bin/env python3 -tt

"""
https://adventofcode.com/2017/day/4
"""

import sys
import os

# Global variables
task="d-4"
infile=task + ".input"

def readInput():
    with open('input\\' + infile) as file:
        data = file.read()
    file.close()
    return data

def solve_a():

    print("Solution A: " + readInput())  

def solve_b():

    print("Solution B: " + readInput())  


if __name__ == '__main__':
    solve_a()
    solve_b()

    print("Finished executing: " + task)
    sys.exit(1)