#!/user/bin/env python3 -tt
"""
https://adventofcode.com/2017/day/14
"""

import sys
import re
from libs.knot_hash import Knot_hash
from time import sleep

task="d-14.1"
infile=task + ".input"


def text_to_bits(my_hexdata):
    scale = 16 ## equals to hexadecimal
    num_of_bits = 4
    return bin(int(my_hexdata, scale))[2:].zfill(num_of_bits)

def solveA():
    base = "vbqugkhl"

    knot_hash = Knot_hash()
    sum = 0
    for row in range(128):
        knot_h = knot_hash.generate(base + "-" + str(row))
        row_parts = []
        row = ""
        for v in list(knot_h):
            row_parts.append(text_to_bits(v))
        row += "".join(str(b) for b in row_parts)
        sum += row.count("1")

    print("A:", sum)

def allocate_group(m, row, kol):
    max_ind = len(m)-1
    if row < 0 or row > max_ind or kol < 0 or kol > max_ind:
        return 
    if m[row][kol] == 'X' or m[row][kol] == '0':
        return
    if m[row][kol] == '1':
        m[row][kol] = 'X'
    allocate_group(m, row, kol+1) # right
    allocate_group(m, row+1, kol) # down
    allocate_group(m, row-1, kol) # up
    allocate_group(m, row, kol-1) # left
    
def solveB():

    base = "vbqugkhl"

    knot_hash = Knot_hash()
    matrix = []
    for i in range(128):
        knot_h = knot_hash.generate(base + "-" + str(i))
        row_parts = []
        for v in list(knot_h):
            row_parts.append(text_to_bits(v))
        row = "".join(str(b) for b in row_parts)
        matrix.append(list(row))

    sum_group = 0
    row = 0
    while row < len(matrix):
        kol = 0
        while kol < len(matrix[row]):
            if matrix[row][kol] == '1':
                sum_group += 1
                allocate_group(matrix, row, kol) 
            kol += 1
        row += 1    

    print("B:", sum_group)

if __name__ == '__main__':
    print("\n")
    solveA()
    solveB()

    print("\n************\nFinished: " + task)
    sys.exit(1)
