#!/user/bin/env python3 -tt
"""
https://adventofcode.com/2017/day/9
"""
from libs.stack import Stack
import sys
import re

task="d-9"
infile=task + ".input"

with open('input/' + infile) as file:
    input = file.read()
file.close()

lvl_score = []
lvl_stack = Stack()

def solveA():
    groups = 0
    raw_stream = input
    # raw_stream = "{{<!!>},{<!!>},{<!!>},{<!!>}}"


    stream = re.sub(r'(\!.)', "", raw_stream)
    stream = re.sub(r'(<.*?>)', "", stream)
    stream = re.sub(r'(,)', "", stream)

    sa = list(stream)
    p = 0
    while p < len(sa):
        char = sa[p]
        p += 1

        lvl = lvl_stack.size()
        if char == '{':
            lvl_stack.push('{')                        
        if char == '}':
            lvl_stack.pop()
            lvl_score.append(lvl)

    result = sum(lvl_score)

    print("Solution A: ", result) 

def solveB():
    groups = 0
    raw_stream = input
    # raw_stream = "{{<!!>},{<!!>},{<!!>},{<!!>}}"

    stream = re.sub(r'(\!.)', "", raw_stream)
    stream = re.sub(r'(<.*?>)', "", stream)

    print("Solution B: ") 


if __name__ == '__main__':
    solveA()
    print("Finished executing: " + task)
    sys.exit(1)
