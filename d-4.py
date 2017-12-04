#!/user/bin/env python3 -tt

"""
https://adventofcode.com/2017/day/4
"""

import sys
import os

# Global variables
task="d-4"
infile=task + ".input"

def readInput():
    with open('input\\' + infile) as file:
        data = file.read()
    file.close()
    return data

def parsePassPhrase(phrase):
    matches = {}
    for s in phrase.split():
        hit = 1
        if s in matches:
            hit += matches[s]
        matches[s] = hit
    # print(matches) 
    return matches

def isValid(matches):
    maxHits = max(list(matches.values()))
    return maxHits < 2

def solve_a():

    # input = "aa bb cc dd ee\naa bb cc dd aa\naa bb cc dd aaa"
    input = readInput()
    passphrases = input.split("\n")

    count = 0
    for phrase in passphrases:
        matches = parsePassPhrase(phrase)
        if isValid(matches):
            count += 1
    
    print("Solution A: ", count)  

def sortAndMatchPhrases(phrase):
    matches = {}
    for s in phrase.split():
        w = "".join(sorted(s))
        hit = 1
        if w in matches:
            hit += matches[w]
        matches[w] = hit
    # print(matches) 
    return matches

def solve_b():
    input =  readInput()
    passphrases = input.split("\n")

    count = 0
    for phrase in passphrases:
        matches = sortAndMatchPhrases(phrase)
        if isValid(matches):
            count += 1
    
    print("Solution B: ", count)  


if __name__ == '__main__':
    solve_a()
    solve_b()

    print("Finished executing: " + task)
    sys.exit(1)