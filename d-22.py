#!/user/bin/env python3 -tt
"""
https://adventofcode.com/2017/day/22
"""

import sys
import copy

task="d-22"
infile=task + ".input"

with open('input/' + infile) as file:
    input = file.read()
file.close()


def solve():
    
    lines = input.split("\n")
    print("A:", lines)

if __name__ == '__main__':
    print("\n")
    solve()
    print("\n************\nFinished: " + task)
    sys.exit(1)
