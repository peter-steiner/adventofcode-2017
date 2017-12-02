#!/user/bin/env python3 -tt

"""
Task:s
https://adventofcode.com/2017/day/2
"""

import sys
import os

# Global variables
task="d-2"
infile=task + ".input"

def readInput():
    with open('input\\' + infile) as file:
        data = file.read()
    file.close()
    return data

def solve_a():
    sum = 0
    rows = readInput().split("\n")
    for row in rows:
        sequences = [int(s) for s in row.split()]
        diff = max(sequences) - min(sequences)
        sum = sum + diff
    print("Sum: " + str(sum))  

def solve_b():
    sum = 0
    rows = readInput().split("\n")
    for row in rows:
        sequences = [int(s) for s in row.split()]
   
    print("Sum: " + str(sum))  

if __name__ == '__main__':
    solve_a()
    
    print("Finished executing: " + task)
    sys.exit(1)