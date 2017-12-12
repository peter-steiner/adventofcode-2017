#!/user/bin/env python3 -tt
"""
https://adventofcode.com/2017/day/12
"""

import sys
import re

task="d-12"
infile=task + ".input"

with open('input/' + infile) as file:
    input = file.read()
file.close()

def visit(prg, pipes, visited, depth):
    links = pipes.get(prg)
    if prg in visited:
        return 
    visited.append(prg)
    for link in links:
        visit(link, pipes, visited, depth + 1)

def solve():

    raw_pipes = input.split("\n")
    links = [0]

    dict_pipes = {}
    pipes = []
    for p in raw_pipes:
        raw_pipe = p.split("<->")
        links = [int(s) for s in raw_pipe[1].split(",")]
        dict_pipes[int(raw_pipe[0])] = links
        pipes.append(int(raw_pipe[0]))

    visited = []
    visit(0, dict_pipes, visited, 0)

    print("A:", len(visited))

    groups = []
    for p in pipes:
        visited = []
        visit(p, dict_pipes, visited, 0)
        visited.sort()
        group = ",".join(str(i) for i in visited)
        if not group in groups:
            groups.append(group)

    print("B:", len(groups))

if __name__ == '__main__':
    print("\n")
    solve()
    print("\n************\nFinished: " + task)
    sys.exit(1)
