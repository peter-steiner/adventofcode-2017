#!/user/bin/env python3 -tt
"""
https://adventofcode.com/2017/day/13
"""

import sys
import re

task="d-13.1"
infile=task + ".input"

with open('input/' + infile) as file:
    input = file.read()
file.close()

def parseLayers(raw_firewall):
    ld = {}
    for lay in raw_firewall:
        layer = [int(i) for i in lay.split(": ")]
        ld[layer[0]] = [0 for i in range(layer[1])]
    return ld

def severity(pos, scanner_pos, layer):
    if scanner_pos == 0:
        return pos * len(layer)
    return 0

def scannerPosition(pos, layer):
    p=0
    dir = 1
    for i in range(pos):
        if p + 1 > len(layer) - 1:
            dir *= -1 
        if dir < 0 and p == 0:
            dir *= -1 
        p += dir
    # print(pos, p)
    return p

def solveA():
    raw_firewall = input.split("\n")
    layers_dict = parseLayers(raw_firewall)

    max_depth = max(layers_dict.keys())
    layers = list(range(max_depth+1))
    for layer in layers_dict:
        layers[layer] = layers_dict[layer]

    sum_severity = 0
    for pos in range(max_depth+1):        
        if pos > 0:
            layer = layers_dict.get(pos)
            if layer:
                scanner_pos = scannerPosition(pos, layer)
                sev = severity(pos, scanner_pos, layer)
                sum_severity += sev
    
    print("A", sum_severity)

if __name__ == '__main__':
    print("\n")
    solveA()
    # solveB()

    print("\n************\nFinished: " + task)
    sys.exit(1)
