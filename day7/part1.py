#!/usr/bin/env python3

with open('input') as f:
    manifold = tuple([c for c in l] for l in f.read().splitlines())

manifold[1][manifold[0].index('S')], split, y = '|', 0, 1

while y < len(manifold) - 1:
    y, x = y + 1, -1

    while x < len(manifold[0]) - 1:
        x += 1

        if manifold[y - 1][x] != '|':
            continue

        match manifold[y][x]:
            case '.':
                manifold[y][x] = '|'
            case '^':
                manifold[y][x - 1] = manifold[y][x + 1] = '|'
                split += 1

print(split)
