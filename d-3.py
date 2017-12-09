#!/user/bin/env python3 -tt

"""
https://adventofcode.com/2017/day/3
"""

import sys
from libs.ulamspiral_day3 import UlamSpiral
from libs.ulamspiral_modded_day3 import UlamSpiralModded

task="d-3"
infile=task + ".input"

movement = {"U": 0, "D": 0, "L": 0, "R": 0}
deltas = {'U': (-1, 0), 'D': (1, 0), 'R':(0, 1), 'L':(0, -1)}

def findStartingPoint(matrix):
    pos = 0
    while pos < len(matrix):
        try:
            return pos, matrix[pos].index(1)
        except ValueError:
            pass
        pos = pos + 1
    return 0, 0

def printMatrix(matrix):
    rows = len(matrix)
    i = 0
    print("***")
    while i < rows:
        print(*matrix[i])
        i = i + 1
    print("***")

def walk(pos, num, matrix):
    for delta in deltas:
        x, y = pos
        dx, dy = deltas[delta]
        nextPos = x+dx, y+dy
        try:
            nextNum = matrix[x+dx][y+dy]
        except IndexError:
            continue
        # Expected square number
        if nextNum == num + 1:
            movement[delta] = movement[delta] + 1
            return nextPos   

def solve_a():
    square = 277678

    spiral = UlamSpiral(square)
    matrix = spiral.getRows()

    pos = findStartingPoint(matrix)
    numbers = [i+1 for i in range(square)]
    for i in numbers:
        if i < square:
            pos = walk(pos, i, matrix)
        
    dx, dy = movement['U'] - movement['D'], movement['R'] - movement['L']
    steps = abs(dx) + abs(dy)
    print("Solution A: ", steps) 

def findNextInMatrix(square, matrix):
    i = 0
    min = sys.maxsize
    while i < len(matrix):
        for n in matrix[i]:
            if square < n:
                if n < min:
                    min = n
        i += 1
    return min

def solve_b():
    square = 277678

    spiral = UlamSpiralModded(square)
    matrix = spiral.getRows()

    nextSquare = findNextInMatrix(square, matrix)
    print("Solution B: ", nextSquare)

if __name__ == '__main__':
    solve_a()
    solve_b()

    print("Finished executing: " + task)
    sys.exit(1)