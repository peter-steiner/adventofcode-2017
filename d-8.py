#!/user/bin/env python3 -tt
"""
https://adventofcode.com/2017/day/8
"""

import sys
import re

task="d-8"
infile=task + ".input"

with open('input/' + infile) as file:
    input = file.read()
file.close()

class Instruction:
    def __init__(self, target, operation, step, conditional_target, operator, condition):
        self.target = target
        self.operation = operation
        self.step = int(step)
        self.conditional_target = conditional_target
        self.operator = operator
        self.condition = int(condition)

    def __str__(self):
        #c : inc : -20 : c : == : 10
        return " : " + self.target + " : " +  self.operation + " : " +  str(self.step) + " : " + self.conditional_target  + " : " +  self.operator + " : " +  str(self.condition)

instruction_match = re.compile(r'(\w+) (inc|dec) (-?\d+) (if) (\w+) (.+) (-?\d+)')
registers = {}

def getRegisterValue(reg):
    return registers[reg]

def jumpInRegister(reg, cmd, jump):
    invert = 1
    if cmd == "dec":
        invert = -1
    registers[reg] += invert * jump 

def initRegister(reg):
    if not reg in registers.keys():
        registers[reg.target] = 0 
        registers[reg.conditional_target] = 0 

def eval_condition(a, condition, b):
    if condition == "==":
        return a == b
    if condition == "!=":
        return a != b
    if condition == "<=":
        return a <= b
    if condition == ">=":
        return a >= b
    if condition == ">":
        return a > b
    if condition == "<":
        return a < b
    print("UNKNOWN CONDITION ", condition)

def operate(instruction):
    a = getRegisterValue(instruction.conditional_target)
    b = instruction.condition
    if eval_condition(a, instruction.operator, b):
        jumpInRegister(instruction.target, instruction.operation, instruction.step)


def solve():
    raw_instructions = [s for s in input.split("\n")]
    
    instructions = []
    for n in raw_instructions:
        matcher = instruction_match.match(n)
        instr = Instruction(matcher.group(1), matcher.group(2), matcher.group(3), matcher.group(5), matcher.group(6), matcher.group(7)) 
        initRegister(instr)
        instructions.append(instr)
    
    maxMemory = 0
    for instr in instructions:
        max_reg = max(registers.values())
        if max_reg > maxMemory:
            maxMemory = max_reg
        operate(instr)    
        
    print("Solution A: ", max(registers.values())) 
    print("Solution B: ", maxMemory) 


if __name__ == '__main__':
    solve()
    print("Finished executing: " + task)
    sys.exit(1)
