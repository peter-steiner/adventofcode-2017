#!/user/bin/env python3 -tt
import sys
import os

"""
Task:
https://adventofcode.com/2017/day/2
"""

# Global variables
task="d-2"
infile=task + ".input"

# Class declarations

def readInput():
    with open('input\\' + infile) as f:
        data = f.read()
#        print("This is the output of [" + infile + "]:\n" + data)
    f.close()
    return data

def main():

    data = readInput()

    print("Finished executing: " + task)
    sys.exit(1)

# Main body
if __name__ == '__main__':
    main()