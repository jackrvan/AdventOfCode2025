#!/usr/bin/python
import sys

pos = 50
knt = 0
prev_pos = -1
with open(sys.argv[1], 'r') as f:
    for line in f:
        if not line.strip():
            continue
        prev_pos = pos
        direction = line[0]
        amount = int(line[1:])
        knt += amount // 100
        amount %= 100
        if amount == 0: continue
        if direction == 'R':
            pos += amount
            if pos > 99:
                knt += 1
            pos %= 100
        else:
            pos -= amount
            if pos < 0:
                pos = 100 + pos
                if prev_pos != 0:
                    knt += 1
            elif pos == 0 and prev_pos != 0:
                knt += 1
print(knt)
