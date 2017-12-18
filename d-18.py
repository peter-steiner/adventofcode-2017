#!/user/bin/env python3 -tt
"""
https://adventofcode.com/2017/day/18
"""

import sys
import re

task="d-18.1"
infile=task + ".input"

with open('input\\' + infile) as file:
    input = file.read()
file.close()

def RepresentsInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False

def snd(cmd, register):
    reg = register[cmd[0]]
    reg[1] = reg[0]

def set_(cmd, register):
    reg = register[cmd[0]]
    if RepresentsInt(cmd[1]):
        reg[0] = int(cmd[1])
        return
    reg[0] = register[cmd[1]][0]
    
def add(cmd, register):
    reg = register[cmd[0]]
    if RepresentsInt(cmd[1]):
        reg[0] += int(cmd[1])
        return
    reg[0] += register[cmd[1]][0]
    
def mul(cmd, register):
    reg = register[cmd[0]]
    if RepresentsInt(cmd[1]):
        reg[0] *= int(cmd[1])
        return
    reg[0] *= register[cmd[1]][0]

def mod(cmd, register):
    reg = register[cmd[0]]
    if RepresentsInt(cmd[1]):
        reg[0] = reg[0]%int(cmd[1])
        return
    reg[0] *= register[cmd[1]][0]

def rcv(cmd, register):
    reg = register[cmd[0]]
    print("recover", reg)
    if reg[1] > 0:
        print("recover")
        reg[0] = reg[1]

def jgz(cmd, cmds, register):
    reg = register[cmd[0]]
    if reg[1] > 0:
        print(len(cmds), -1, int(cmd[1]), len(cmds))
        parseCmd(cmds[len(cmds)-1+int(cmd[1])], cmds, register)    

def parseCmd(raw_cmd, cmds, register):
    cmds.append(raw_cmd)
    # print(raw_cmd.split(" "), raw_cmd.split(" ")[1])
    reg = raw_cmd.split(" ")[1]
    if not reg in register.keys():
        register[reg] = [0, 0]

    if "snd" in raw_cmd:
        snd(raw_cmd.split(" ")[1:], register)
    if "set" in raw_cmd:
        snd(raw_cmd.split(" ")[1:], register)
    if "add" in raw_cmd:
        add(raw_cmd.split(" ")[1:], register)
    if "mul" in raw_cmd:
        mul(raw_cmd.split(" ")[1:], register)
    if "mod" in raw_cmd:
        mod(raw_cmd.split(" ")[1:], register)
    if "rcv" in raw_cmd:
        rcv(raw_cmd.split(" ")[1:], register)
    if "jgz" in raw_cmd:
        jgz(raw_cmd.split(" ")[1:], cmds, register)

def solveA():

    register = {}
    cmds = []
    raw_cmds = input.split("\n")
    for raw_cmd in raw_cmds:
        parseCmd(raw_cmd, cmds, register)
        # print(register)

    print("A:")

def solveB():
    print("B:")

if __name__ == '__main__':
    print("\n")
    solveA()
    solveB()

    print("\n************\nFinished: " + task)
    sys.exit(1)
