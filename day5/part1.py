#!/usr/bin/env python3

with open('input') as f:
    database, ranges = f.read().rstrip().split('\n\n'), []

for l in database[0].splitlines():
    start, stop = map(int, l.split('-'))
    ranges.append(range(start, stop + 1))

available = map(int, database[1].splitlines())
fresh = tuple(a for a in available if any(a in r for r in ranges))

print(len(fresh))
