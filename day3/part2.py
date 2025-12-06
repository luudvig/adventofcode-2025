#!/usr/bin/env python3

with open('input') as f:
    banks, total = ({k: v for k, v in enumerate(l)} for l in f.read().splitlines()), 0

for bank in banks:
    largest, remaining, start = "", 12, 0

    while remaining > 0:
        end = len(bank) - remaining

        bank_slice = {k: v for k, v in bank.items() if start <= k <= end}
        max_index = max(bank_slice, key=bank_slice.get)
        max_digit = bank_slice[max_index]

        largest += max_digit
        start = max_index + 1
        remaining -= 1

    total += int(largest)

print(total)
