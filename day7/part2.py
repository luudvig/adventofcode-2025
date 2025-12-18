#!/usr/bin/env python3

with open('input') as f:
    manifold, timelines_cache, timelines_total = f.read().splitlines(), {}, 0

def step(y, x):
    global timelines_total

    if (y, x) in timelines_cache:
        timelines_total += timelines_cache[(y, x)]
    elif y == len(manifold) - 1:
        timelines_total += 1
    elif manifold[y + 1][x] == '.':
        step(y + 1, x)
    else:
        for dx in (x - 1, x + 1):
            timelines_prev = timelines_total
            step(y + 1, dx)
            timelines_cache[(y + 1, dx)] = timelines_total - timelines_prev

step(1, manifold[0].index('S'))
print(timelines_total)
