#!/user/bin/env python3 -tt
"""
https://adventofcode.com/2017/day/10
"""

import sys
import re

task="d-10"
infile=task + ".input"

with open('input/' + infile) as file:
    input = file.read()
file.close()

def solveA():
    # input = "3, 4, 1, 5"
    lengths = [int(s.rstrip()) for s in input.split(",")]
    list_size = 256
    hash_arr = list(range(list_size))
    position = 0
    skip = 0

    for length in lengths:
        # cut array
        # pos + length-1
        # reverse array
        hash_size = len(hash_arr)
        # print(hash_arr, length, skip, position)
        circular_arr = hash_arr + hash_arr

        pos_from = position%hash_size
        pos_to = pos_from+length
        sub_list = circular_arr[pos_from:pos_to]
        reversed_sub_list = sub_list[::-1]

        i = 0
        while i < len(reversed_sub_list):
            substitute_pos = (position + i)%hash_size 
            hash_arr[substitute_pos] = reversed_sub_list[i]
            i += 1
        position += (length + skip)%hash_size
        skip += 1

    result = hash_arr[0]*hash_arr[1]

    # print(hash_arr)
    print("Solution A: ", result) 

def solveB():

    print("Solution B: ") 

if __name__ == '__main__':
    solveA()
    # solveB()
    print("Finished executing: " + task)
    sys.exit(1)
