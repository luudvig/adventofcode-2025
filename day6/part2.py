#!/usr/bin/env python3

with open('input') as f:
    problem, total, worksheet, x = [], 0, f.read().splitlines(), 0

while x < len(worksheet[0]):
    number, spaces, y = '', True, 0

    while y < len(worksheet):
        match worksheet[y][x]:
            case '+':
                addition = True
            case '*':
                addition = False
            case d if d.isdigit():
                number += d
                spaces = False
        y += 1
    x += 1

    if not spaces:
        problem.append(int(number))

        if x != len(worksheet[0]):
            continue

    answer = problem[0]

    for n in problem[1:]:
        answer = answer + n if addition else answer * n

    problem = []
    total += answer

print(total)
