#!/usr/bin/python
import sys

tot = 0
with open(sys.argv[1], 'r') as f:
    for line in f:
        line = line.strip()
        if not line: continue
        # print(f"{line=}")
        # print(line[:len(line)-2])
        index_largest = line.index(max(line[:len(line)-1], key=lambda n: int(n)))
        # print(f"{index_largest=}")
        
        index_largest_after_largest = line.index((max(line[index_largest+1:], key=lambda n: int(n))))
        num = int(line[index_largest])*10 + int(line[index_largest_after_largest])
        print(f"{num=}")
        tot += num

print(tot)

