#!/user/bin/env python3 -tt
"""
https://adventofcode.com/2017/day/11
"""

import sys
import re

task="d-11"
infile=task + ".input"

with open('input/' + infile) as file:
    input = file.read()
file.close()

''' 
ne,ne,ne        #3
ne,ne,sw,sw     #0
ne,ne,s,s       #2
se,sw,se,sw,sw  #3
'''

class Node:
    linked = None

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "Node..."

class Cord:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "" + self.x + ", " + self.y

navigation = {"nw":[-1, 1], "n":[0, 2], "ne":[1, 1], "sw": [-1, 1], "s":[0, -2], "se":[1,-1]}

max_depth = 0

def traverse_hex_grid(depth, cordinate, from_dir):
        cord = Cord(cordinate.x + from_dir.x, cordinate.y + from_dir.y)
        if depth == max_depth:
            return
        for next_dir in navigation:
            (x, y) = next_dir.value()
            traverse_hex_grid(depth + 1, cord, Cord(x, y))

def solveA():
    
    steps = 0
    input = "se,sw,se,sw,sw"
    directions = input.split(",")
    print(directions)
    for dir in directions:
        print(navigation.get(dir))

    print("A: ", steps) 

def solveB():
    steps = 0

    print("B: ", steps)

if __name__ == '__main__':
    solveA()
    solveB()
    print("Finished executing: " + task)
    sys.exit(1)
