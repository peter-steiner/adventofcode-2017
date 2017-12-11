#!/user/bin/env python3 -tt
"""
https://adventofcode.com/2017/day/11
"""

import sys
import re

task="d-11"
infile=task + ".input"

with open('input/' + infile) as file:
    input = file.read()
file.close()

''' 
ne,ne,ne        #3
ne,ne,sw,sw     #0
ne,ne,s,s       #2
se,sw,se,sw,sw  #3
 '''
def solveA():
    steps = 0

    print("A: ", steps) 

def solveB():
    steps = 0

    print("B: ", steps)

if __name__ == '__main__':
    solveA()
    solveB()
    print("Finished executing: " + task)
    sys.exit(1)
