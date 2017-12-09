#!/user/bin/env python3 -tt
"""
Task:
https://adventofcode.com/2017/day/1
"""

# Imports
import sys
import os

# Global variables
task="d-1"
infile=task + ".input"

def readInput():
    with open('input\\' + infile) as file:
        data = file.read()
    file.close()
    return data

def main():
    numbers = [int(n) for n in readInput()]
    size = len(numbers)
    offset = int(len(numbers)/2)
    nums = numbers + numbers
    print("size: " + str(size) + " offset: " + str(offset) + " nums: " + str(len(nums)))
    numbers_to_sum = []
    index = 0
    for i in nums:
        if index < size:
            a = nums[index]
            b = nums[index+offset]
            if a == b:
                numbers_to_sum.append(a)             
        index += 1

    print("sum: " + str(sum(numbers_to_sum)))
    sys.exit(1)



# Main body
if __name__ == '__main__':
    main()