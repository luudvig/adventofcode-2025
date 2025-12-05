#!/usr/bin/env python3

with open('input') as f:
    invalids, ranges = [], (r.split('-') for r in f.read().rstrip().split(','))

for d in (d for r in ranges for d in range(int(r[0]), int(r[1]) + 1)):
    d_str = str(d)
    d_len = len(d_str)
    d_mid = d_len // 2 + 1

    while d_mid > 1:
        d_mid -= 1

        if d_len % d_mid != 0:
            continue
        elif len(set(d_str[i:i + d_mid] for i in range(0, d_len, d_mid))) == 1:
            invalids.append(d)
            break

print(sum(invalids))
