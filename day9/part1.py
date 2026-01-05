#!/usr/bin/env python3

with open('input') as f:
    largest, tiles = 0, [tuple(map(int, l.split(','))) for l in f.read().splitlines()]

for i, t1 in enumerate(tiles):
    for t2 in tiles[i + 1:]:
        x = t1[0] - t2[0]
        y = t1[1] - t2[1]

        x = x - 1 if x < 0 else x + 1
        y = y - 1 if y < 0 else y + 1

        area = abs(x * y)

        if area > largest:
            largest = area

print(largest)
