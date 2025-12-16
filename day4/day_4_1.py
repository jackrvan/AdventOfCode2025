#!/usr/bin/python
import sys


def touchingRollsAbove(grid, ri, ci):
    rollsTouching = 0
    if ri == 0:
        return 0
    substr = grid[ri-1][max(ci-1, 0):ci+2]
    return substr.count('@')

def touchingRollsBelow(grid, ri, ci):
    rollsTouching = 0
    if ri == len(grid) - 1:
        return 0
    substr = grid[ri+1][max(ci-1, 0):ci+2]
    return substr.count('@')

def touchingRollRight(grid, ri, ci):
    if ci == len(grid[0]) - 1:
        return 0
    return 1 if grid[ri][ci+1] == '@' else 0

def touchingRollLeft(grid, ri, ci):
    if ci == 0:
        return 0
    return 1 if grid[ri][ci-1] == '@' else 0

grid = []
with open(sys.argv[1], 'r') as f:
    for line in f:
        if not line.strip(): continue
        grid.append(line)
tot = 0
for ri, _ in enumerate(grid):
    for ci, _ in enumerate(grid[ri]):
        if grid[ri][ci] == '.' or not grid[ri][ci].strip(): continue
        total_touching = touchingRollsAbove(grid, ri, ci) + touchingRollsBelow(grid, ri, ci) + touchingRollRight(grid, ri, ci) + touchingRollLeft(grid, ri, ci)
        if total_touching < 4:
            # print(f"grid[{ri}][{ci}] which is {grid[ri][ci]} counts because total touching is {total_touching}")
            tot += 1
print(tot)
