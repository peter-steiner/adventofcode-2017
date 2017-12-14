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

def test_text_tobit():
    bin_ = text_to_bits("0")
    print("test 0", bin_)
    bin_ = text_to_bits("1")
    print("test 1", bin_)
    bin_ = text_to_bits("e")
    print("test e", bin_)
    bin_ = text_to_bits("f")
    print("test f", bin_)

def solveA():
    input = "a0c2017..."

    knot_hash = Knot_hash()
    knot_h = knot_hash.generate(input)
    for v in list(knot_h):
        bin_ = text_to_bits(v)
        print(bin_)

    print("a knot", knot_h)
    # print("a", "asbit", row, len(row))

if __name__ == '__main__':
    print("\n")
    solveA()
    solveB()

    test_text_tobit()

    print("\n************\nFinished: " + task)
    sys.exit(1)
