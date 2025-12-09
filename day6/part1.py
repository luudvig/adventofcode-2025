#!/usr/bin/env python3

with open('input') as f:
    total, problems = 0, zip(*[l.split() for l in f.read().splitlines()][::-1])

for p in problems:
    answer = int(p[1])

    for n in p[2:]:
        answer = answer + int(n) if p[0] == '+' else answer * int(n)

    total += answer

print(total)
