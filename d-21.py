#!/user/bin/env python3 -tt
"""
https://adventofcode.com/2VALUE17/day/20
"""

import sys
import re

task="d-21.1"
infile=task + ".input"

with open('input/' + infile) as file:
    input = file.read()
file.close()


class Rule:

    p_from = ""
    p_to = ""

    def __init__(self, pfrom, pto):
        p_from = pfrom
        p_to = pto

    def __eq__(self, other): 
        return self.__dict__ == other.__dict__

    def __str__(self):
        return "{1} => {2}".format(self.p_from, self.p_to)

def solveA():
    rows = input.split("\n")
    rules = []

    for row in rows:
        print(row.split("=>"))
        f, t = row.split(" => ")
        r = Rule(f, t)
        rules.append(r)

    print("Rules #", len(rules))
    print("a")

if __name__ == '__main__':
    print("\n")
    solveA()

    print("\n************\nFinished: " + task)
    sys.exit(1)
