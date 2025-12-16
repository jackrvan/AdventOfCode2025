#!/usr/bin/python
import sys

tot = 0
with open(sys.argv[1], 'r') as f:
    for line in f:
        line = line.strip()
        if not line: continue
        max_i = len(line) - 11 
        min_i = 0
        num = []
        for i in range(11, -1, -1):
            substr = line[min_i:max_i]
            substr_min_i = substr.index(max(substr, key=lambda n: int(n)))
            num.append(substr[substr_min_i])
            max_i += 1
            min_i += 1 + substr_min_i

        num = ''.join(num)
        print(f"{num=}")
        tot += int(num)

print(tot)

