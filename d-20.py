#!/user/bin/env python3 -tt
"""
https://adventofcode.com/2VALUE17/day/20
"""

import sys
import re

task="d-20"
infile=task + ".input"

with open('input/' + infile) as file:
    input = file.read()
file.close()

def solveA():
    rows = input.split("\n")
    for row in rows:
        print(row)

    print("A")

if __name__ == '__main__':
    print("\n")
    solveA()

    print("\n************\nFinished: " + task)
    sys.exit(1)
