#!/user/bin/env python3 -tt
"""
https://adventofcode.com/2VALUE17/day/20
"""

import sys
import re

task="d-20"
infile=task + ".input"

with open('input/' + infile) as file:
    input = file.read()
file.close()


class Particle:
    id = None
    vel = []
    acc = []
    loc = []
    prev_distance = 0

    def __init__(self, id_, loc_, vel_, acc_):
        self.id = id_
        self.loc = [int(i) for i in loc_.split(",")]
        self.vel = [int(i) for i in vel_.split(",")]
        self.acc = [int(i) for i in acc_.split(",")]
        self.prev_distance = self.distance()

    def point_as_string(self):
        return ",".join(str(i) for i in self.loc)

    def tick(self):
        acc = self.acc
        for i in range(3):
            self.vel[i] += self.acc[i] 
            self.loc[i] += self.vel[i]

    def location(self):
        return self.loc

    def trend(self):
        return self.prev_distance - self.distance()

    def distance(self):
        return sum([abs(i) for i in self.loc])

    def __eq__(self, other): 
        return self.__dict__ == other.__dict__

    def __str__(self):
        return "[{0}]:|{1}| loc: {2}, vel: {3}, acc: {4}".format(self.id, self.distance(), self.loc, self.vel, self.acc)

def removeDuplicates(particles):
    points = {}
    for p in particles:
        if p.point_as_string() in points.keys():
            points[p.point_as_string()] += 1
        else: 
            points[p.point_as_string()] = 1

    i = 0
    toRemove = []
    for p in particles:
        if p.point_as_string() in points.keys() and points[p.point_as_string()] > 1:
            toRemove.append(p)
            i += 1

    for r in toRemove:
        particles.remove(r)    
    return particles

def solveA():
    rows = input.split("\n")
    particles = []

    i = 0
    print(len(rows))
    for row in rows:
        m = re.findall('(-*\d+,-*\d+,-*\d+)', row, re.DOTALL)
        c, v, a = m
        p = Particle(i, c, v, a)
        particles.append(p)
        i += 1

    particles = removeDuplicates(particles)
    print("patricles #", len(particles))

    i = 0
    while i < 10000:
        for p in particles:
            p.tick()
        particles = removeDuplicates(particles)
        i += 1

    target_particle = None
    min = sys.maxsize
    for p in particles:
        if p.distance() < min:
            min = p.distance()
            target_particle = p            

    print(i, "iterations", len(particles))
    print("Particel min distance", target_particle)

if __name__ == '__main__':
    print("\n")
    solveA()

    print("\n************\nFinished: " + task)
    sys.exit(1)
