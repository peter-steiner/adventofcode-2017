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
gen = [65, 8921]

def solveB():

    print("B")

def solveA():
    global gen

    i = 0
    hits = 0
    while i < 40000000:
    # while i < 6:

        gen_a = gen[A] * factor[A] % 2147483647
        gen_b = gen[B] * factor[B] % 2147483647

        bin_list_a = list("{0:b}".format(gen_a))
        len_a = len(bin_list_a)
        bin_list_b = list("{0:b}".format(gen_b))
        len_b = len(bin_list_b)
        # print(gen_a, gen_b)
        # seq_a = "".join(str(i) for i in bin_list_a[len_a-16:len_a])
        # seq_b = "".join(str(i) for i in bin_list_b[len_b-16:len_b])
        seq_a = bin_list_a[len_a-16:len_a]
        seq_b = bin_list_b[len_b-16:len_b]
        for i in range(16):
            if len(seq_a) < 16 or len(seq_b) < 16:
                break
            if seq_a[i] != seq_b[i]:
                break
            if i == 15:
                hits += 1

        # print("*****", len(seq_a))
        # print(seq_a)
        # print(seq_b)
        # if seq_a == seq_b:
            # print("hit at", i)

        gen = [gen_a, gen_b]
        i += 1

    print("A", hits)

if __name__ == '__main__':
    print("\n")
    solveA()
    solveB()

    print("\n************\nFinished: " + task)
    sys.exit(1)
