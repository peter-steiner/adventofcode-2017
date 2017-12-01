#!/user/bin/env python3 -tt
"""
Module documentation.
"""

# Imports
import sys
import os

# Global variables
task="d-1"
infile=task + ".input"

# Class declarations

# Function declarations

def readInput():
    with open('input\\' + infile) as f:
        data = f.read()
#        data="123123"
#        print("This is the output of [" + infile + "]:\n" + data)
    f.close()
    return data

def main():

    data = readInput()
    numbers = [int(n) for n in data]
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
#            print(str(a) + str(b) + "--index: " + str(index) + " " + str(size))
            if a == b:
#                print("Adding: " + str(a) + " " + str(b))
                numbers_to_sum.append(a)             
        index = index+1

    print("sum: " + str(sum(numbers_to_sum)))
    print("Finished executing: " + task)
    sys.exit(1)



# Main body
if __name__ == '__main__':
    main()