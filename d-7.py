#!/user/bin/env python3 -tt

"""
https://adventofcode.com/2017/day/7
"""
import sys

# Global variables
task="d-7.1"
infile=task + ".input"

with open('input/' + infile) as file:
    input = file.read()
file.close()

def solve():
    print("Solution A: ", input) 


if __name__ == '__main__':

    solve()

    print("Finished executing: " + task)
    sys.exit(1)
