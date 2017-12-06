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


def solve_a():
    block = [int(i) for i in readInput().split()]
    
    findings = []
    generated = ""

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
        generated = "".join([str(i) for i in block])
        if generated in findings:
            print("MATCH FOUND", generated, findings.index(generated), findings[findings.index(generated)], len(findings)) 
            break
        findings.append(generated)
            
    print("Solution A: ", i) 

def solve_b():

    print("Solution B: ")

if __name__ == '__main__':

    solve_a()
    solve_b()

    print("Finished executing: " + task)
    sys.exit(1)
