#!/user/bin/env python3 -tt
"""
https://adventofcode.com/2017/day/17
"""

import sys
import re

task="d-17"
infile=task + ".input"

buffer = [0]
steps = 354

def solveA():
    global buffer
    target_val = 2017

    i = 0
    index = 0
    while True:
        i += 1
        index = (index + steps)%i + 1
        buffer.insert(index , i)
        if i == target_val + 1:
            break
    
    index = buffer.index(target_val) + 1 if buffer.index(target_val) + 1 < len(buffer) else 0
    result = buffer[index]
    print("A:", result)

def solveB():
    global buffer
    target_val = 50000000
    
    i = 0
    index = 0
    while True:
        i += 1
        index = (index + steps)%i + 1
        if index < 10 or index < buffer.index(0) + 2:
            buffer.insert(index , i)
        if i == target_val + 1:
            break
        
    find = 0
    index = buffer.index(find) + 1 if buffer.index(find) + 1 < len(buffer) else 0
    result = buffer[index]
    print("B:", result)

if __name__ == '__main__':
    print("\n")
    solveA()
    solveB()

    print("\n************\nFinished: " + task)
    sys.exit(1)
