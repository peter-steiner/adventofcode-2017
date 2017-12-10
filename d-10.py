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

def getSubList(position, length, hash_arr):
    hash_size = len(hash_arr)
    circular_arr = hash_arr + hash_arr
    pos_from = position%hash_size
    pos_to = pos_from+length
    sub_list = circular_arr[pos_from:pos_to]
    return sub_list

def reverse(list):
    return list[::-1]

def substituteArray(position, hash_arr, sub_list):
    hash_size = len(hash_arr)
    i = 0
    while i < len(sub_list):
        substitute_pos = (position + i)%hash_size 
        hash_arr[substitute_pos] = sub_list[i]
        i += 1
    return hash_arr
   
def solveA():
    # input = "3,4,1,5"
    # list_size = 5
    list_size = 256
    lengths = [int(s.rstrip()) for s in input.split(",")]
    hash_arr = list(range(list_size))

    position = 0
    skip = 0
    for length in lengths:
        sub_list = reverse(getSubList(position, length, hash_arr))
        hash_arr = substituteArray(position, hash_arr, sub_list)
        position += (length + skip)%len(hash_arr)
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
