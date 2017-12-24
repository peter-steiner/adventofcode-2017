#!/user/bin/env python3 -tt
"""
https://adventofcode.com/2VALUE17/day/23
"""

import sys
from libs.queue import Queue
import re

task="d-23"
infile=task + ".input"

with open('input/' + infile) as file:
    input = file.read()
file.close()

COUNT_PRG1 = 0
VALUE = 0
LAST_FREQ = 1
CMDS = []
AQ = []
BQ = []

mul_count = 0

def initCommands():
    global CMDS
    raw_cmds = input.split("\n")
    for raw_cmd in raw_cmds:
        CMDS.append(raw_cmd)

def initRegistry(registry):
    global CMDS
    for raw_cmd in CMDS:
        r = raw_cmd.split(" ")[1]
        if not RepresentsInt(r):
            if not r in registry.keys():
#                print("Add key", r)
                registry[r] = [0, 0]

def RepresentsInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False


def set_(cmd, registry):
    r = registry[cmd[VALUE]]
    if RepresentsInt(cmd[1]):
        r[VALUE] = int(cmd[1])
        registry[cmd[VALUE]] = [r[VALUE], r[1]] 
        return registry
    r[VALUE] = registry[cmd[1]][VALUE]
    registry[cmd[VALUE]] = [r[VALUE], r[1]] 
    return registry

def sub(cmd, registry):
    r = registry[cmd[VALUE]]
    if RepresentsInt(cmd[1]):
        r[VALUE] -= int(cmd[1])
        registry[cmd[VALUE]] = [r[VALUE], r[1]] 
        return registry
    r[VALUE] -= registry[cmd[1]][VALUE]
    registry[cmd[VALUE]] = [r[VALUE], r[1]] 
    return registry

def mul(cmd, registry):
    r = registry[cmd[VALUE]]
    if RepresentsInt(cmd[1]):
        r[VALUE] *= int(cmd[1])
        registry[cmd[VALUE]] = [r[VALUE], r[1]]
        return registry
    r[VALUE] *= registry[cmd[1]][VALUE]
    registry[cmd[VALUE]] = [r[VALUE], r[1]] 
    return registry

def jnz(cmd, cmds, index, registry, id):

    val = 0    
    if RepresentsInt(cmd[VALUE]):
        val = int(cmd[VALUE])
    else:
        val = registry[cmd[VALUE]][0]

    if val != 0:
        if RepresentsInt(cmd[1]):
            offset = index+int(cmd[1])
            return parseCmd(cmds[offset], cmds, offset, registry, id)    
        offset = index+registry[cmd[1]][VALUE]
        return parseCmd(cmds[offset], cmds, offset, registry, id)    
    return index+1, registry

def parseCmd(raw_cmd, cmds, index, registry, id):

    cmds.append(raw_cmd)
    r = raw_cmd.split(" ")[1]
    global mul_count
    # print(raw_cmd)
    if "set" in raw_cmd:
        registry = set_(raw_cmd.split(" ")[1:], registry)
    if "sub" in raw_cmd:
        registry = sub(raw_cmd.split(" ")[1:], registry)
    if "mul" in raw_cmd:
        mul_count += 1
        registry = mul(raw_cmd.split(" ")[1:], registry)
    if "jnz" in raw_cmd:
        return jnz(raw_cmd.split(" ")[1:], cmds, index, registry, id)
    return index+1, registry

def solveA():
    global CMDS
    
    CMDS = []
    registryA = {}
    initCommands()
    initRegistry(registryA)

    max_index = len(CMDS)
    index = 0
    while True:
        index, reg = parseCmd(CMDS[index], CMDS, index, registryA, "A")
        # print(index)
        if index >= max_index:
            break

    print("23 A", mul_count)

if __name__ == '__main__':
    print("\n")
    solveA()

    print("\n************\nFinished: " + task)
    sys.exit(1)
