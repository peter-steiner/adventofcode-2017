#!/user/bin/env python3 -tt
"""
https://adventofcode.com/2017/day/14
"""

import sys
import re
from libs.knot_hash import Knot_hash

task="d-14.1"
infile=task + ".input"


def text_to_bits(my_hexdata):
    scale = 16 ## equals to hexadecimal
    num_of_bits = 4
    return bin(int(my_hexdata, scale))[2:].zfill(num_of_bits)

input = "vbqugkhl"

def solveB():

    print("B")

def solveA():
    base = "vbqugkhl"

    knot_hash = Knot_hash()
    rows = []
    for i in range(128):
        knot_h = knot_hash.generate(base + "-" + str(i))
#        print(base + "-" + str(i))
        row_parts = []
        row_bin = []
        for v in list(knot_h):
            row_parts.append(text_to_bits(v))
#        print(row_parts)
        rows.append("".join(str(b) for b in row_parts))

    sum = 0
    for r in rows:
        sum += r.count("1")
    print("A:", sum)

if __name__ == '__main__':
    print("\n")
    solveA()
    solveB()

    print("\n************\nFinished: " + task)
    sys.exit(1)
