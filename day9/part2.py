#!/usr/bin/env python3

from itertools import combinations, pairwise

__author__ = "https://www.reddit.com/r/adventofcode/comments/1phywvn/comment/nt2m7fx/"

with open('input') as f:
    largest, red = 0, [tuple(map(int, l.split(','))) for l in f.read().splitlines()]

green = list(pairwise(red + [red[0]]))

for (x, y), (u, v) in combinations(red, 2):
    if x > u:
        x, u = u, x
    if y > v:
        y, v = v, y

    area = (u - x + 1) * (v - y + 1)

    if area > largest:
        for (p, q), (r, s) in green:
            if p > r:
                p, r = r, p
            if q > s:
                q, s = s, q

            if p < u and q < v and r > x and s > y:
                break
        else:
            largest = area

print(largest)
