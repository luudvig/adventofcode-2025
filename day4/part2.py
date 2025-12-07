#!/usr/bin/env python3

with open('input') as f:
    accessible, diagram, prev_accessible = set(), tuple([c for c in l] for l in f.read().splitlines()), -1

y_max = len(diagram)
x_max = len(diagram[0])

while (accessible_len := len(accessible)) != prev_accessible:
    prev_accessible = accessible_len

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
                accessible.add((y, x))

    for a in accessible:
        diagram[a[0]][a[1]] = '.'

print(len(accessible))
