#!/usr/bin/env python3

with open('input') as f:
    database, ranges = f.read().rstrip().split('\n\n'), set()

for l in database[0].splitlines():
    start, stop = map(int, l.split('-'))
    ranges.add(range(start, stop + 1))

fresh, i = sorted(ranges, key=lambda r: r.start), 0

while i < len(fresh) - 1:
    if fresh[i + 1].start <= fresh[i].stop:
        fresh[i] = range(fresh[i].start, max(fresh[i].stop, fresh[i + 1].stop))
        del fresh[i + 1]
    else:
        i += 1

print(sum(len(f) for f in fresh))
