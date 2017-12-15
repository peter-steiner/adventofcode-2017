#!/user/bin/env python3 -tt
"""
https://adventofcode.com/2017/day/15
"""

import sys

task="d-15"
A = 0
B = 1 
factor = [16807, 48271]

def solveA():
    gen = [512, 191]

    i = 0
    hits = 0
    for _ in range(40000000):

        gen_a = gen[A] * factor[A] % 2147483647
        gen_b = gen[B] * factor[B] % 2147483647

        seq_a = list("{0:b}".format(gen_a))[::-1]
        seq_b = list("{0:b}".format(gen_b))[::-1]        
        for n in range(16):
            a = seq_a[n] if n < len(seq_a) else 0 
            b = seq_b[n] if n < len(seq_b) else 0 
            if a != b:
                break
            if n == 15:
                hits += 1

        gen = [gen_a, gen_b]

    print("A", hits)

def solveB():
    gen = [512, 191]
    
    a_sequences = []
    b_sequences = []

    i = 0
    while i < 40000000:
        gen_a = gen[A] * factor[A] % 2147483647
        gen_b = gen[B] * factor[B] % 2147483647
        if gen_a%4 == 0:
            a_sequences.append(gen_a)
        if gen_b%8 == 0:
            b_sequences.append(gen_b)
        i += 1
        gen = [gen_a, gen_b]

    hits = 0
    i = 0
    max_iterations = len(b_sequences) if len(b_sequences) < len(a_sequences) else len(a_sequences)
    while i < max_iterations:
        seq_a = list("{0:b}".format(a_sequences[i]))[::-1]
        seq_b = list("{0:b}".format(b_sequences[i]))[::-1]
        for n in range(16):
            a = seq_a[n] if n < len(seq_a) else 0 
            b = seq_b[n] if n < len(seq_b) else 0 
            if a != b:
                break
            if n == 15:
                hits += 1
        i += 1
    print("B", hits)


if __name__ == '__main__':
    print("\n")
    solveA()
    solveB()

    print("\n************\nFinished: " + task)
    sys.exit(1)
