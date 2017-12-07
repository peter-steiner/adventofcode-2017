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
    children = None
    weight_sum = 0

    def __init__(self, name, weight, linked):
        self.name = name
        self.weight = int(weight)
        self.weight_sum += self.weight
        self.linked = linked
        self.children = []

    def __str__(self):
        children_str = " ".join(self.linked)
        parent_name = self.parent.name if self.parent else "KING"
        return "" + self.name + " : " +  parent_name + ":" + str(self.weight)  + " : " + children_str #+ ":||||:" + " ".join([n.name for n in self.children])

nodeTree = []
def traverseTree(node, deep):

    if len(nodeTree) <= deep:
        nodeTree.append([])

    nodeTree[deep].append(node)
    if not node.children:
        return
    for child in node.children:
        traverseTree(child, deep+1)

def detectUnstable(node, deep):
    weights = []

    for n in node.children:
        if n.weight_sum not in weights:
            weights.append(n.weight_sum)

    for n in node.children:
        if len(weights) > 1 and max(weights) == n.weight_sum:
            print("found unstable for: ", n.name, " in: ", weights)
            diff = max(weights) - min(weights)
            new_weight = n.weight - diff
            print("[", deep, "]New weight:", new_weight,  " for: ", n, " diff: ", diff)

    for n in node.children:
        if len(nodeTree) > deep + 1:
            detectUnstable(n, deep +1)


def buildTree(parent, nodes):
    if not parent.linked:
        return parent
    for link_str in parent.linked:
        for node in nodes:
            #Find matching node
            if link_str == node.name:
                node.parent = parent
                parent.children.append(node)
                child = buildTree(node, nodes)
                parent.weight_sum += child.weight_sum

    return parent

def printNodes(nodes):
    print("Print all nodes")
    for node in nodes:
        print(node)


def solve():
    raw_node_list = [s.rstrip() for s in input.split("\n")]
    regex = re.compile(r'(\w+) \((\d+)\)')

    master_node = None
    nodes = []
    all_linked_node_names = []
    for n in raw_node_list:
        pmn = regex.match(n)
        np = Node(pmn.group(1).rstrip(), pmn.group(2).rstrip(), [])
        links = n.split("->")
        if len(links) > 1:
            np.linked = [s.strip() for s in links[1].split(",")]
        if np:
            nodes.append(np)
        for link in np.linked:
            all_linked_node_names.append(link)

    for node in nodes:
        if len(node.linked) > 1 and not node.name in ":".join(all_linked_node_names):
            master_node = node

    buildTree(master_node, nodes)
    traverseTree(master_node, 0)

#    for row in nodeTree:
#        nodes = ""
#        for node in row:
#            parent = node.parent.name if node.parent  else "KING"
#            nodes += "[" + parent + "]" + node.name + ":" + str(node.weight_sum)
#        print(nodes)

#    for weights in weightTree:
#        if len(weights) > 1:
#            print(":".join([str(s) for s in weights]))

    print("Detect unstable:")
    detectUnstable(master_node, 0)

if __name__ == '__main__':

    solve()

    print("Finished executing: " + task)
    sys.exit(1)
