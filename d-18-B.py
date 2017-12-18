#!/user/bin/env python3 -tt
"""
https://adventofcode.com/2VALUE17/day/18
"""

import sys
from libs.queue import Queue
import re

#

task="d-18"
#task="d-18-B.1"
infile=task + ".input"

with open('input/' + infile) as file:
    input = file.read()
file.close()

A_WAITING = False
B_WAITING = False

QUEUE = {"A":Queue(), "B":Queue()}

COUNT_PRG1 = 0

VALUE = 0
LAST_FREQ = 1
CMDS = []
AQ = []
BQ = []

def initCommands():
    raw_cmds = input.split("\n")
    for raw_cmd in raw_cmds:
        CMDS.append(raw_cmd)

def initRegistry(registry):
    for raw_cmd in CMDS:
        r = raw_cmd.split(" ")[1]
        if not r in registry.keys():
            registry[r] = [0, 0]

def RepresentsInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False

def snd(cmd, registry, id):
    global COUNT_PRG1
    print(cmd)
    val = 0
    if RepresentsInt(cmd[0]):
        val = cmd[0]
    else:
        val = registry[cmd[VALUE]][0]
    if "A" in id:   
        #print("Add to queue", "B", QUEUE.get("B").show())
        q = QUEUE.get("B")
        q.push(val)
        QUEUE["B"] = q
    if "B" in id:
        COUNT_PRG1 += 1
        #print("Add to queue", "A", QUEUE.get("A").show())
        q = QUEUE.get("A")
        q.push(val)
        QUEUE["A"] = q

def rcv(cmd, index, registry, id):
    global A_WAITING
    global B_WAITING
   # print("Read from queue", id, QUEUE.get(id).show())
    r = registry[cmd[VALUE]]
    q = Queue()
    val = 0
    if "A" in id:
        q = QUEUE.get("A")
        if q.isEmpty():
            print("Queue is empty")
            A_WAITING = True
            return index, registry
        val = q.pop()
        QUEUE["A"] = q
        A_WAITING = False
    if "B" in id:
        q = QUEUE.get("B")
        if q.isEmpty():
            print("Queue is empty")
            B_WAITING = True
            return index, registry
        val = q.pop()
        QUEUE["B"] = q
        B_WAITING = False
    print(r, cmd[VALUE], val)
    registry[cmd[VALUE]] = [val, 0]
    return index + 1, registry


def set_(cmd, registry):
    r = registry[cmd[VALUE]]
    if RepresentsInt(cmd[1]):
        r[VALUE] = int(cmd[1])
        registry[cmd[VALUE]] = [r[VALUE], r[1]] 
        return registry
    r[VALUE] = registry[cmd[1]][VALUE]
    registry[cmd[VALUE]] = [r[VALUE], r[1]] 
    return registry

def add(cmd, registry):
    r = registry[cmd[VALUE]]
    if RepresentsInt(cmd[1]):
        r[VALUE] += int(cmd[1])
        registry[cmd[VALUE]] = [r[VALUE], r[1]] 
        return registry
    r[VALUE] += registry[cmd[1]][VALUE]
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

def mod(cmd, registry):
    r = registry[cmd[VALUE]]
    if RepresentsInt(cmd[1]):
        r[VALUE] = r[VALUE]%int(cmd[1])
        registry[cmd[VALUE]] = [r[VALUE], r[1]] 
        return registry
    r[VALUE] = r[VALUE]%registry[cmd[1]][VALUE]
    registry[cmd[VALUE]] = [r[VALUE], r[1]] 
    return registry

def jgz(cmd, cmds, index, registry, id):
    r = registry[cmd[VALUE]]
    print(r[VALUE])
    if r[VALUE] > 0:
        if RepresentsInt(cmd[1]):
            offset = index+int(cmd[1])
            return parseCmd(cmds[offset], cmds, offset, registry, id)    
        offset = index+registry[cmd[1]][VALUE]
        return parseCmd(cmds[offset], cmds, offset, registry, id)    
    return index+1, registry

def parseCmd(raw_cmd, cmds, index, registry, id):
    cmds.append(raw_cmd)
    r = raw_cmd.split(" ")[1]
    if not r in registry.keys():
        print("Create registry for", r)
        registry[r] = [0, 0]
    if "snd" in raw_cmd:
        snd(raw_cmd.split(" ")[1:], registry, id)
    if "set" in raw_cmd:
        registry = set_(raw_cmd.split(" ")[1:], registry)
    if "add" in raw_cmd:
        registry = add(raw_cmd.split(" ")[1:], registry)
    if "mul" in raw_cmd:
        registry = mul(raw_cmd.split(" ")[1:], registry)
    if "mod" in raw_cmd:
        registry = mod(raw_cmd.split(" ")[1:], registry)
    if "rcv" in raw_cmd:
        return rcv(raw_cmd.split(" ")[1:], index, registry, id)
    if "jgz" in raw_cmd:
        return jgz(raw_cmd.split(" ")[1:], cmds, index, registry, id)
    return index+1, registry

def solveB():
    global registry
    global CMDS
    registryA = {}
    registryB = {}
    CMDS = []
    queue = {"A":Queue(), "B":Queue()}

    initCommands()
    initRegistry(registryA)
    initRegistry(registryB)


    indexA = 0
    indexB = 0
    i = 0
    print("Execute:")
    while True:
        indexA, registryA = parseCmd(CMDS[indexA], CMDS, indexA, registryA, "A")
        indexB, registryB  = parseCmd(CMDS[indexB], CMDS, indexB, registryB, "B")
        i += 1
#        if i == 8:
#            break
        #print(A_WAITING, B_WAITING)
        if A_WAITING and B_WAITING:
            break

    print("B:", COUNT_PRG1)

if __name__ == '__main__':
    print("\n")
    solveB()

    print("\n************\nFinished: " + task)
    sys.exit(1)
