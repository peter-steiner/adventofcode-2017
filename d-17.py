#!/user/bin/env python3 -tt
"""
https://adventofcode.com/2017/day/17
"""

import sys
import re

task="d-17"
infile=task + ".input"

steps = 354
buffer = [0]

def solveA():

    global buffer
    dance_floor = []
    target_val = 2017

    i = 0
    index = 0
    while True:
        index = (index + steps)%len(buffer) + 1
        i += 1
        buffer.insert(index , i)
        if i == target_val + 1:
            break

    result = buffer[buffer.index(target_val) + 1]
    print("Next value:", result)

def solveB():

    result = 1337
    print("B:", result)

if __name__ == '__main__':
    print("\n")
    solveA()
    # solveB()

    print("\n************\nFinished: " + task)
    sys.exit(1)
