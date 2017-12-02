#!/user/bin/env python3 -tt
import sys
import os

"""
Task:s
https://adventofcode.com/2017/day/2
"""

# Global variables
task="d-2"
infile=task + ".input"

# Class declarations

def readInput():
    with open('input\\' + infile) as file:
        data = file.read()
    file.close()
    return data

def main():
    sum = 0
    rows = readInput().split("\n")
    for row in rows:
        sequences = [int(s) for s in row.split()]
        min_ = min(sequences)
        max_ = max(sequences)
        diff = max_ - min_
        #print( str(max_) + "-" + str(min_) + "=" + str(diff))
        sum = sum + diff

    print("Sum: " + str(sum))  
    print("Finished executing: " + task)
    sys.exit(1)

# Main body
if __name__ == '__main__':
    main()