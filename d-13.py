#!/user/bin/env python3 -tt
"""
https://adventofcode.com/2017/day/13
"""

import sys
import re

task="d-13"
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
    # print(pos, scanner_pos)
    if scanner_pos == 0:
        return pos * len(layer)
    return 0

def severityB(pos, scanner_pos, layer):
    # print(pos, scanner_pos)
    if scanner_pos == 0:
        return len(layer)
    return 0

def scannerPositionForLayer(pos, layer):
    p=0
    last_index = len(layer)-1
    steps = pos % (last_index*2)
    dir = 1
    for i in range(steps):
        if p + 1 > last_index:
            dir *= -1
        p += dir
    return p

def solveB():
    raw_firewall = input.split("\n")
    layers_dict = parseLayers(raw_firewall)

    max_depth = max(layers_dict.keys())
    layers = list(range(max_depth+1))
    for layer in layers_dict:
        layers[layer] = layers_dict[layer]

    delay = 0
    while True:
        # if delay%10000 == 0:
        #     print("Progress", delay)
        sum_severity = 0
        for pos in range(max_depth+1):        
            scan_count = pos + delay
            layer = layers_dict.get(pos)
            if layer:
                scanner_pos = scannerPositionForLayer(scan_count, layer)
                sev = severityB(pos, scanner_pos, layer)
                sum_severity += sev
                if sev > 0:
                    break
        if sum_severity == 0:
            print("severity:", delay, sum_severity)
            break
        delay += 1
    
    print("B", delay, sum_severity)

def solveA():
    raw_firewall = input.split("\n")
    layers_dict = parseLayers(raw_firewall)

    max_depth = max(layers_dict.keys())
    layers = list(range(max_depth+1))
    for layer in layers_dict:
        layers[layer] = layers_dict[layer]

    sum_severity = 0
    for pos in range(max_depth+1):        
        scan_count = pos
        if pos > 0:
            layer = layers_dict.get(pos)
            if layer:
                scanner_pos = scannerPositionForLayer(scan_count, layer)
                sev = severity(pos, scanner_pos, layer)
                sum_severity += sev
    
    print("A", sum_severity)

if __name__ == '__main__':
    print("\n")
    solveA()
    solveB()

    print("\n************\nFinished: " + task)
    sys.exit(1)
