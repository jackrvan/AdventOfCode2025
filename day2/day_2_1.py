#!/usr/bin/python
import sys
cache = {}
total = 0
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
    # if num > max_num:
        # return 0
    # if num in cache:
        # return num + do_range(num+1, max_num)
    # else:
        # cache[num] = isDup(num)
        # return cache[num] + do_range(num+1, max_num)
        
def isDup(num):
    strNum = str(num)
    if strNum[:len(strNum)//2] == strNum[len(strNum)//2:]:
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


