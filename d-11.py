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

class Cord:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def move(self, dx, dy, dz):
        self.x += dx
        self.y += dy
        self.z += dz

    def __str__(self):
        return "{0}, {1}, {2}".format(self.x, self.y, self.z)

navigation = {"nw":[0, -1, 1], "n":[-1, 0, 1], "ne":[-1, 1, 0], "sw": [1, -1, 0], "s":[1, 0, -1], "se":[0, 1,-1]}

def solveA():
    
    directions = input.split(",")
    max_steps = 0

    cord = Cord(0, 0, 0)
    for dir in directions:
        dist = max(cord.x, cord.y, cord.z)
        if dist > max_steps:
            max_steps = dist

        dx, dy, dz = navigation.get(dir)
        cord.move(dx, dy, dz)
    
    distance = max(cord.x, cord.y, cord.z)
    # print(cord)
    print("A shortest path", distance)
    print("Max steps distance", max_steps)

if __name__ == '__main__':
    print("\n")
    solveA()
    print("\n************\nFinished: " + task)
    sys.exit(1)
