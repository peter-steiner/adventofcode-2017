#!/user/bin/env python3 -tt
"""
https://adventofcode.com/2017/day/15
"""

import sys
import re

task="d-15"
infile=task + ".input"

A = 0
B = 1 
factor = [16807, 48271]
gen = [512, 191]
# gen = [65, 8921]

def solveB():
    i = 0
    while True:
        i += 1
        l = list("{0:b}".format(i))
        if len(l) == 17:
            print(i, l)
            break
    print("B")

def solveA():
    global gen

    i = 0
    hits = 0
    while i < 40000000:
    # while i < 6:
        if i%1000000 == 0:
            print("Progress: ", i)

        gen_a = gen[A] * factor[A] % 2147483647
        gen_b = gen[B] * factor[B] % 2147483647

        bin_list_a = list("{0:b}".format(gen_a))
        len_a = len(bin_list_a)
        bin_list_b = list("{0:b}".format(gen_b))
        len_b = len(bin_list_b)

        seq_a = bin_list_a[::-1]
        seq_b = bin_list_b[::-1]
        for n in range(16):
            a = seq_a[n] if n < len(seq_a) else 0 
            b = seq_b[n] if n < len(seq_b) else 0 
            if a != b:
                break
            if n == 15:
                hits += 1

        # print("*****", len(seq_a))
        # print(seq_a)
        # print(seq_b)

        i += 1
        gen = [gen_a, gen_b]

    print("A", hits)

if __name__ == '__main__':
    print("\n")
    solveA()
    # solveB()

    print("\n************\nFinished: " + task)
    sys.exit(1)
