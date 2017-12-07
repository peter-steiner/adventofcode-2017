#!/user/bin/env python3 -tt

"""
https://adventofcode.com/2017/day/7
"""
import sys
import re

# Global variables
task="d-7.1"
infile=task + ".input"

with open('input/' + infile) as file:
    input = file.read()
file.close()

class Node:
    def __init__(self, name, weight, linked):
        self.name = name
        self.weight = weight
        self.linked = linked

def solve():
    listOfnodes = [s.rstrip() for s in input.split("\n")]
    prog = re.compile(r'(\w+) \((\d+)\)')
    allLinked = []
    nodes = []
    for n in listOfnodes:
        pmn = prog.match(n)
        np = Node(pmn.group(1), pmn.group(2), []) 
        links = n.split("->")
        if len(links) > 1:
            np.linked = links[1].split(",")        

        nodes.append(np)
        print(np.name, ":", np.weight, ":", np.linked)
        allLinked.append(np.linked)

    print(allLinked)
    print(":".join(allLinked))
    base = ""
    for n in nodes:
        if len(n.linked) > 1 and not n.name in ":".join(allLinked):
            print("Should happen once", n.name)
            base = n.name 

    print("Solution A: ", base) 


if __name__ == '__main__':

    solve()

    print("Finished executing: " + task)
    sys.exit(1)
