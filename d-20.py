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
        return "".join(str(i) for i in self.loc)

    def tick(self):
        acc = self.acc
        # accelrate and calc new position
        for i in range(3):
            self.vel[i] += acc[i] 
            self.loc[i] += self.vel[i]

    def location(self):
        return self.loc

    def trend(self):
        return self.prev_distance - self.distance()

    def distance(self):
        return sum([abs(i) for i in self.loc])

    def __str__(self):
        return "[{0}]:|{1}| loc: {2}, vel: {3}, acc: {4}".format(self.id, self.distance(), self.loc, self.vel, self.acc)

def solveA():
    rows = input.split("\n")
    particles = []

    i = 0
    print(len(rows))
    for row in rows:
        # print(row)
        m = re.findall('(-*\d+,-*\d+,-*\d+)', row, re.DOTALL)
        c, v, a = m
        p = Particle(i, c, v, a)
        particles.append(p)
        i += 1

    print(len(particles))
    points = []
    for p in particles:
        if p.point_as_string() in points:
            particles.remove(p)
        else: 
            points.append(p.point_as_string())
    i = 0
    while i < 1000:
        c = 0
        points = [p.point_as_string() for p in particles]
        for p in particles:
            
            distance = p.distance()
            p.tick()
            trend = p.trend()

        i += 1
        ids = []
        for key, value in points.items():
            if len(value) > 1:
                print(value)
                ids += value 

        for p in particles:
            if p.id in ids:
                particles.remove(p)

    target_particle = None
    min = sys.maxsize
    for p in particles:
        if p.distance() < min:
            min = p.distance()
            target_particle = p            

    print(i, "iterations", len(particles))
    print("Particel min distance", target_particle)

    print("A")

if __name__ == '__main__':
    print("\n")
    solveA()

    print("\n************\nFinished: " + task)
    sys.exit(1)
