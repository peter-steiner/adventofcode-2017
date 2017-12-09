#!/user/bin/env python3 -tt
"""
https://adventofcode.com/2017/day/9
"""

import sys
import re

task="d-9"
infile=task + ".input"

with open('input/' + infile) as file:
    input = file.read()
file.close()

def solve():
    groups = 0
    raw_stream = input


    stream = re.sub(r'(\!.)', "", raw_stream)
    # print(stream)
    stream = re.sub(r'(<.*?>)', "", stream)
    
    print(stream)


    print("Solution A: ", groups) 
    print("Solution B: ", groups) 


if __name__ == '__main__':
    solve()
    print("Finished executing: " + task)
    sys.exit(1)
