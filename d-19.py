#!/user/bin/env python3 -tt
"""
https://adventofcode.com/2VALUE17/day/19
"""

import sys
import re

task="d-19"
infile=task + ".input"

with open('input/' + infile) as file:
    input = file.read()
file.close()

DIAGRAM = []
DIR = "D"
DIR_IND = {'U': "|", 'D': "|", 'R':"-", 'L':"-"}
deltas = {'U': (0, -1), 'D': (0, 1), 'R':(1, 0), 'L':(-1, 0)}
COLLECTED = ""
STEPS = 0

def isChar(char):
    int_val = ord(char.lower())
    return int_val > 96 and int_val < 123
    
# Handle turning point
def try_turn(pos):
    global DIR
    global COLLECTED
    global STEPS

    x, y = pos
    path = DIAGRAM[y][x]
    if path in "+":
        for delta in deltas:
            if DIR in "UD" and delta in "LR":
                dx, dy = deltas.get(delta)
                if y + dy < len(DIAGRAM) and x + dx < len(DIAGRAM[0]):
                    npos = DIAGRAM[y+dy][x+dx]
                    if npos in "-" or isChar(npos):
                        DIR = delta
                        STEPS += 1
                        # print("turn", DIR)
                        if isChar(DIAGRAM[y+dy][x+dx]):
                            COLLECTED += DIAGRAM[y+dy][x+dx]
                        return x+dx, y+dy
            if DIR in "LR" and  delta in "UD":
                dx, dy = deltas.get(delta)
                if y + dy < len(DIAGRAM) and x + dx < len(DIAGRAM[0]):
                    npos = DIAGRAM[y+dy][x+dx]
                    if npos in "|" or isChar(npos):
                        DIR = delta
                        STEPS += 1
                        # print("turn", DIR)
                        if isChar(DIAGRAM[y+dy][x+dx]):
                            COLLECTED += DIAGRAM[y+dy][x+dx]
                        return x+dx, y+dy
    return x, y 

def move(pos):
    global COLLECTED
    global STEPS

    x, y = pos
#    print("stepped on to", DIAGRAM[y][x])
    for delta in deltas:
        if DIR in delta:
            dx, dy = deltas.get(delta)
            pos = [x+dx, y+dy]
            char = DIAGRAM[y][x]

            if char in " ":
                return [x, y]

            # Valid step
            if not -1 in pos and y + dy < len(DIAGRAM) and x + dx < len(DIAGRAM[0]):
                # print(DIAGRAM[y+dy][x+dx])
                #print("move", DIR, "from", [x, y], "to", pos)
                if isChar(DIAGRAM[y+dy][x+dx]):
                    COLLECTED += DIAGRAM[y+dy][x+dx]
                STEPS += 1
                # Turn if possible as next step
                x, y = try_turn(pos)
                pos = [x, y]
    return pos

def solveA():
    rows = input.split("\n")
    for row in rows:
        DIAGRAM.append(list(row))

    print("Bring it on...", len(DIAGRAM), len(DIAGRAM[0]))
    # Starting point
    x = rows[0].index("|")
    pos = [x, 0]
    print("Starting at", pos)

    chars = ""
    for row in rows:
        print(row)
        for c in row:
            if isChar(c):
                chars += c
    i = 0
    while True:
#        print(DIR, pos)
        px, py = pos
        x, y = move(pos)
        if px == x and py == y:
            break        
        pos =[x, y]
        if x < 0 or y < 0:
            break
        
        
    print(COLLECTED, len(COLLECTED), STEPS)

if __name__ == '__main__':
    print("\n")
    solveA()




    print("\n************\nFinished: " + task)
    sys.exit(1)
