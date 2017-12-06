#!/user/bin/env python3 -tt

"""
https://adventofcode.com/2017/day/6
"""

import sys

# Global variables
task="d-6"
infile=task + ".input"


def readInput():
    with open('input/' + infile) as file:
        input = file.read()
    file.close()
    return input

findAgain = ""

def solve():
    block = [int(i) for i in readInput().split()]
    
    findings = []
    generated = ""
    firstHit = True
    firstFind = ""

    i = 0
    while True:
        i += 1
        redistr = max(block)
        bank = block.index(redistr)
        block[bank] = 0

        items = len(block)
        for k in range(1, redistr + 1):
            next_block_pos = (bank + k)%(items)
            block[next_block_pos] += 1
        generated = "".join([str(i) + "." for i in block])
        if generated in findings:
            if firstHit:
                i = 0
                firstHit = False
                firstFind = generated
                print("A Solved", len(findings), generated) 
            else:
                if generated == firstFind:
                    print("B Solved", i, generated, firstFind)
                    break
        findings.append(generated)
        
            
    print("Solution A: ", i) 

if __name__ == '__main__':

    solve()

    print("Finished executing: " + task)
    sys.exit(1)
