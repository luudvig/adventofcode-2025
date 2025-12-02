#!/usr/bin/env python3

with open('input') as f:
    dial, rotations, total = 50, f.read().splitlines(), 0

for r in rotations:
    if r[0] == 'L' and dial == 0:
        total -= 1

    dial = dial - int(r[1:]) if r[0] == 'L' else dial + int(r[1:])

    while dial < 0:
        dial = 100 + dial
        total += 1
    while dial > 99:
        dial = dial - 100
        total += 1

    if r[0] == 'L' and dial == 0:
        total += 1

print(total)
