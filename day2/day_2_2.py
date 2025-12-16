#!/usr/bin/python
import sys
import re

cache = {}
regex = re.compile('^(\\d+)\\1+$')
def do_range(num, max_num):
    tot = 0
    while num <= max_num:
        if num in cache:
            tot += cache[num]
        else:
            cache[num] = isDup(num)
            tot += cache[num]
        num += 1
    return tot
 
def isDup(num):
    strNum = str(num)
    if regex.fullmatch(strNum):
        # print(f"returning {num} because its dup")
        return num
    # print(f"returning 0 cuz {num}")
    return 0

tot = 0
with open(sys.argv[1], 'r') as f:
    for line in f:
        if not line.strip(): continue
        ranges = line.split(',')
        for r in ranges:
            tot += do_range(int(r.split('-')[0]), int(r.split('-')[1]))
print(tot)


