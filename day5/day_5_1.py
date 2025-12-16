#!/usr/bin/python
import sys

def isInRange(num, ranges):
    for r in ranges:
        if num >= r[0] and num <= r[1]:
            return True
    return False

empty = False
tot = 0
ranges = []
with open(sys.argv[1], 'r') as f:
    for line in f:
        if not line.strip():
            empty = True
            continue
        if empty:
            if isInRange(int(line), ranges):
                tot += 1
        else:
            ranges.append([int(line.split('-')[0]), int(line.split('-')[1])])
print(tot)

