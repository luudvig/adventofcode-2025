#!/usr/bin/env python3

with open('input') as f:
    banks, total = f.read().splitlines(), 0

for bank in banks:
    largest = 0

    for i, b1 in enumerate(bank):
        for b2 in bank[i + 1:]:
            if (joltage := int(b1 + b2)) > largest:
                largest = joltage

    total += largest

print(total)
