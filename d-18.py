#!/user/bin/env python3 -tt
"""
https://adventofcode.com/2VALUE17/day/18
"""

import sys
import re

task="d-18"
infile=task + ".input"

with open('input/' + infile) as file:
    input = file.read()
file.close()

register = {}

VALUE = 0
LAST_FREQ = 1

def RepresentsInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False

def snd(cmd):
    r = register[cmd[VALUE]]
    register[cmd[VALUE]] = [r[VALUE], r[VALUE]] 

def set_(cmd):
    r = register[cmd[VALUE]]
    print(cmd, r)
    if RepresentsInt(cmd[1]):
        r[VALUE] = int(cmd[1])
        register[cmd[VALUE]] = [r[VALUE], r[1]] 
        return
    r[VALUE] = register[cmd[1]][VALUE]
    register[cmd[VALUE]] = [r[VALUE], r[1]] 
    return

def add(cmd):
    r = register[cmd[VALUE]]
    if RepresentsInt(cmd[1]):
        r[VALUE] += int(cmd[1])
        register[cmd[VALUE]] = [r[VALUE], r[1]] 
        return
    r[VALUE] += register[cmd[1]][VALUE]
    register[cmd[VALUE]] = [r[VALUE], r[1]] 
    return

def mul(cmd):
    r = register[cmd[VALUE]]
    if RepresentsInt(cmd[1]):
        r[VALUE] *= int(cmd[1])
        register[cmd[VALUE]] = [r[VALUE], r[1]]
        return
    r[VALUE] *= register[cmd[1]][VALUE]
    register[cmd[VALUE]] = [r[VALUE], r[1]] 
    return

def mod(cmd):
    r = register[cmd[VALUE]]
    if RepresentsInt(cmd[1]):
        r[VALUE] = r[VALUE]%int(cmd[1])
        register[cmd[VALUE]] = [r[VALUE], r[1]] 
        return
    r[VALUE] = r[VALUE]%register[cmd[1]][VALUE]
    register[cmd[VALUE]] = [r[VALUE], r[1]] 
    return

def rcv(cmd):
    r = register[cmd[VALUE]]
    if r[VALUE] > 0:
        print("recover", r[1])
        r[VALUE] = r[1]
        register[cmd[VALUE]] = [r[VALUE], r[1]] 
        if r[1] > 0:
            return -1
    return 

def jgz(cmd, cmds, index):
    r = register[cmd[VALUE]]
    if r[VALUE] > 0:
        if RepresentsInt(cmd[1]):
            print(index + int(cmd[1]), index, int(cmd[1]))
            offset = index+int(cmd[1])
            return parseCmd(cmds[offset], cmds, offset)    
        print(index + register[cmd[1]][VALUE], index, register[cmd[1]][VALUE])
        offset = index+register[cmd[1]][VALUE]
        return parseCmd(cmds[offset], cmds, offset)    
    return index+1

def parseCmd(raw_cmd, cmds, index):
    cmds.append(raw_cmd)
    print(raw_cmd)
    #print(raw_cmd.split(" "), raw_cmd.split(" ")[1:][VALUE])
    r = raw_cmd.split(" ")[1]
    if not r in register.keys():
        print("Create registry for", r)
        register[r] = [0, 0]

    if "snd" in raw_cmd:
        snd(raw_cmd.split(" ")[1:])
    if "set" in raw_cmd:
        set_(raw_cmd.split(" ")[1:])
    if "add" in raw_cmd:
        add(raw_cmd.split(" ")[1:])
    if "mul" in raw_cmd:
        mul(raw_cmd.split(" ")[1:])
    if "mod" in raw_cmd:
        mod(raw_cmd.split(" ")[1:])
    if "rcv" in raw_cmd:
        if rcv(raw_cmd.split(" ")[1:]) == -1:
            return -1
    if "jgz" in raw_cmd:
        return jgz(raw_cmd.split(" ")[1:], cmds, index)
    return index+1

def solveA():
    global register
    cmds = []
    raw_cmds = input.split("\n")
    print("Init cmds")
    for raw_cmd in raw_cmds:
        cmds.append(raw_cmd)
        r = raw_cmd.split(" ")[1]
        if not r in register.keys():
            print("Create registry for", r)
            register[r] = [0, 0]
        #print("Register:", register)

    index = 0
    print("Execute:")
    while True:
        print(register)
        index = parseCmd(cmds[index], cmds, index)
        if index == -1:
            break

    print("A:")

def solveB():
    print("B:")

if __name__ == '__main__':
    print("\n")
    solveA()
    solveB()

    print("\n************\nFinished: " + task)
    sys.exit(1)
