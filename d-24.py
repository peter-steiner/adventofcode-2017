#!/user/bin/env python3 -tt
"""
https://adventofcode.com/2017/day/24
"""

import sys
import copy

task="d-24"
infile=task + ".input"

with open('input/' + infile) as file:
    input = file.read()
file.close()

max = 0
visited_max = 0

def visit(port, pipes, pipe_dict, visited, depth):
    global max
    global visited_max
    for pipe in pipe_dict.keys():
        val = pipe_dict[pipe][:]
        if port in val:
            val.remove(port)
            link = val[0]
            if not pipe in visited:
                vc = copy.copy(visited)
                vc.append(pipe)
                visit(link, pipes, pipe_dict.copy(), vc, depth + 1)
    sum = 0
    for v in visited:
        pipe = pipe_dict[v]
        sum += pipe[0] + pipe[1]

    if len(visited) > visited_max:
        max = 0
        visited_max = len(visited)
    if len(visited) >= visited_max:
        if sum > max:
            max = sum       

def solve():

    global max
    raw_pipes = input.split("\n")
    links = [0]

    dict_pipes = {}
    pipes = []
    for p in raw_pipes:
        raw_pipe = p.split("/")
        links = [int(raw_pipe[0]), int(raw_pipe[1])]
        dict_pipes[p] = links
        pipes.append(int(raw_pipe[0]))

    visit(0, dict_pipes.keys(), dict_pipes, [], 0)

    print("A:", max)

if __name__ == '__main__':
    print("\n")
    solve()
    print("\n************\nFinished: " + task)
    sys.exit(1)
