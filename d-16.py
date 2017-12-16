#!/user/bin/env python3 -tt
"""
https://adventofcode.com/2017/day/16
"""

import sys
import re

task="d-16"
infile=task + ".input"

with open('input/' + infile) as file:
    input = file.read()
file.close()

ascii_base = 97 #a
dance_floor = list(range(16))

def rotate(x, f):
    rf = list(range(len(f)))
    for i in f:
        np = (f.index(i) + x)%(len(f))
        rf[np] = i
    return rf

def spin(x, f):
    # print("r", x, f)
    return rotate(x, f)

def exchange(a, b, f):
    # print("x", a, b, f)
    f[b], f[a] = f[a], f[b]
    return f

def partner(a, b, f):
    # print("p", a, b, f)
    ia = f.index(a)
    ib = f.index(b)
    return exchange(ia, ib, f)

# def testPartner():
#     f = ['a', 'b', 'c', 'd', 'e']
#     print(partner('a', 'e', f))

# def testPartner():
#     f = ['a', 'b', 'c', 'd', 'e']
#     print(partner('a', 'e', f))

def execute(cmd, f):
    if "s" in cmd:
        m = re.search('(\d+)', cmd)
        return spin(int(m.group(1)), f)
    if "x" in cmd:
        m = re.search('(\d+)\/(\d+)', cmd)
        return exchange(int(m.group(1)), int(m.group(2)), f)
    if "p" in cmd:
        m = re.search('(\w)\/(\w)', cmd)
        return partner(m.group(1), m.group(2), f)

def solveA():

    cmds = input.split(",")
    dance_floor = []
    for i in range(16):
        dance_floor.append(chr(ascii_base + i))

    i = 0
    for cmd in cmds:
        dance_floor = execute(cmd, dance_floor)

    df = "".join(s for s in dance_floor)
    print("A:", df)

def solveB():

    print("B:")

if __name__ == '__main__':
    print("\n")
    solveA()
    solveB()

    print("\n************\nFinished: " + task)
    sys.exit(1)
