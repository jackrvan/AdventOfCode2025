#!/usr/bin/python
import sys
import copy

def addToRanges(ranges, _min, _max):
    for i, r in enumerate(ranges):
        if r[0] <= _max and r[1] >= _min:
            newList = copy.deepcopy(ranges)[:i]
            newMin = min(r[0], _min)
            newMax = max(r[1], _max)
            r2 = i+1
            while r2 < len(ranges) and newMax >= ranges[r2][0]:
                newMax = max(newMax, ranges[r2][1])
                r2 += 1
            newList.append([newMin, newMax])
            newList.extend(ranges[r2:])
            return newList
    ranges.append([_min, _max])
    ranges = sorted(ranges, key = lambda r: r[0])
    return ranges

tot = 0
ranges = []
with open(sys.argv[1], 'r') as f:
    for line in f:
        if not line.strip(): continue
        ranges = addToRanges(ranges, int(line.split('-')[0]), int(line.split('-')[1]))
for r in ranges:
    tot += r[1] - r[0] + 1
print(tot)

