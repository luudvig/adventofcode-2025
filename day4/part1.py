#!/usr/bin/env python3

with open('input') as f:
    accessible, diagram = 0, f.read().splitlines()

y_max = len(diagram)
x_max = len(diagram[0])

for y in range(y_max):
    for x in range(x_max):
        if diagram[y][x] != '@':
            continue

        adjacent = 0

        for dy, dx in ((y-1, x-1), (y-1, x), (y-1, x+1), (y, x-1), (y, x+1), (y+1, x-1), (y+1, x), (y+1, x+1)):
            if not -1 < dy < y_max or not -1 < dx < x_max or diagram[dy][dx] != '@':
                continue

            adjacent += 1

            if adjacent > 3:
                break
        else:
            accessible += 1

print(accessible)
