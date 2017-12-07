#!/user/bin/env python3 -tt

"""
https://adventofcode.com/2017/day/7
"""
import sys
import re

# Global variables
task="d-7"
infile=task + ".input"

with open('input/' + infile) as file:
    input = file.read()
file.close()

class Node:
    parent = None

    def __init__(self, name, weight, linked):
        self.name = name
        self.weight = weight
        self.linked = linked

def solve():
    raw_node_list = [s.rstrip() for s in input.split("\n")]
    regex = re.compile(r'(\w+) \((\d+)\)')

    nodes = []
    linked_node_names = []
    for n in raw_node_list:
        pmn = regex.match(n)
        np = Node(pmn.group(1), pmn.group(2), []) 
        links = n.split("->")
        if len(links) > 1:
            np.linked = links[1].split(",")        
        nodes.append(np)
#        print(np.name, ":", np.weight, ":", np.linked)
        for link in np.linked:
            linked_node_names.append(link)

    base = ""
    for node in nodes:
        if len(node.linked) > 1 and not node.name in ":".join(linked_node_names):
            print("Master node found", node.name)
            base = node.name

    print("Solution A: ", base) 


if __name__ == '__main__':

    solve()

    print("Finished executing: " + task)
    sys.exit(1)
