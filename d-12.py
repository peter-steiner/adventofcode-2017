#!/user/bin/env python3 -tt
"""
https://adventofcode.com/2017/day/12
"""

import sys
import re

task="d-12.1"
infile=task + ".input"

with open('input/' + infile) as file:
    input = file.read()
file.close()


class Pipe():
    def __init__(self, link_, links_):
        self.link = link_
        self.links = links_

    def __str__(self):
        return "{0} <-> {1}".format(self.link, self.links) 

def printPipes(pipes):
    for pipe in pipes:
        print(pipe)

def solve():

    raw_pipes = input.split("\n")
    links = [0]

    dict_pipes = {}
    pipes = []
    for p in raw_pipes:
        raw_pipe = p.split("<->")
        links = [int(s) for s in raw_pipe[1].split(",")]
        links.sort()
        print(links)
        for l in links:
            pipe = Pipe(int(raw_pipe[0]), l)
            pipes.append(pipe)
            pipe_reverse = Pipe(l, int(raw_pipe[0]))
            pipes.append(pipe_reverse)
 
        # pipe = Pipe(int(raw_pipe[0]), links[0])
        pipes.append(pipe)
        # print(pipe)

    pipes.sort(key=lambda p: p.link, reverse=False)
    # printPipes(pipes)

    piped_programs = set()
    piped_programs.add(0)
    for pipe in pipes:
        if pipe.link in piped_programs or pipe.links in piped_programs:
            print("....")
            piped_programs.add(pipe.link)
            piped_programs.add(pipe.links)

        # #  and not pipe.links in links
        # if pipe.link in links:
        #     links.append(pipe.links)

    programs = list(piped_programs)
    # for link in programs:
    #     print(link)

    print("A: ", len(programs))
    # print("B")

if __name__ == '__main__':
    print("\n")
    solve()
    print("\n************\nFinished: " + task)
    sys.exit(1)
