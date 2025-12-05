#!/usr/bin/env python3

with open('input') as f:
    invalids, ranges = [], (r.split('-') for r in f.read().rstrip().split(','))

for d in (d for r in ranges for d in range(int(r[0]), int(r[1]) + 1)):
    d_str = str(d)
    d_mid = len(d_str) // 2
    
    if d_str[:d_mid] == d_str[d_mid:]:
        invalids.append(d)

print(sum(invalids))
