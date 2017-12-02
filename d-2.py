#!/user/bin/env python3 -tt

"""
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
    print("Solution A: " + str(sum))  

def solve_b():
    sum = 0
    rows = readInput().split("\n")
    for row in rows:
        sequences = sorted([int(s) for s in row.split()])
        sum = sum + findEven(0, sequences)

    print("Solution B: " + str(sum))  

def findEven(index, numbers):
    divider = numbers[index]
    result_arr = [n for n in numbers if n != divider and n % divider == 0]
    if result_arr:
        return result_arr[0] // divider 
    if index == len(numbers) - 1:
        return 0
    return findEven(index+1, numbers)

if __name__ == '__main__':

    solve_a()
    solve_b()

    print("Finished executing: " + task)
    sys.exit(1)