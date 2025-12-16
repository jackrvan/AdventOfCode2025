#!/usr/bin/python

pos = 50
knt = 0
with open('day_1_input.txt', 'r') as f:
    for line in f:
        if not line.strip():
            continue
        print(f"{pos=}")
        direction = line[0]
        amount = int(line[1:])
        while amount > 99:
            amount -= 100
        if direction == 'R':
            pos += amount
            pos %= 100
        else:
            pos -= amount
            if pos < 0:
                pos = 100 + pos
        if pos == 0:
            knt += 1
print(knt)
