#!/usr/bin/env python3

with open('example') as f:
    areas, tiles = [], [tuple(map(int, l.split(','))) for l in f.read().splitlines()]

max_x = max(t[0] for t in tiles) + 1
max_y = max(t[1] for t in tiles) + 1
grid = [[False] * max_x for _ in range(max_y)]

def print_grid():
    for y in grid:
        for x in y:
            print(x, end='\t')
        print()

for i, t2 in enumerate(tiles):
    t1 = tiles[i - 1]

    if t1[0] == t2[0]:
        for y in range(min(t1[1], t2[1]), max(t1[1], t2[1]) + 1):
            grid[y][t1[0]] = True
    else:
        for x in range(min(t1[0], t2[0]), max(t1[0], t2[0]) + 1):
            grid[t1[1]][x] = True

print('finished outlines')

for y in range(len(grid)):
    if True not in grid[y]:
        continue
    f_index = grid[y].index(True)
    l_index = len(grid[y]) - 1 - grid[y][::-1].index(True)

    for x in range(f_index + 1, l_index):
        grid[y][x] = True

print('finished grid')
#print_grid()

for i, t1 in enumerate(tiles):
    for t2 in tiles[i + 1:]:
        x = t1[0] - t2[0]
        y = t1[1] - t2[1]

        x = x - 1 if x < 0 else x + 1
        y = y - 1 if y < 0 else y + 1

        a = abs(x * y)
        areas.append([a, t1, t2])

areas.sort(key=lambda t: t[0], reverse=True)
#print(areas[1])

print('finished areas')

for a in areas:
    t1, t2 = a[1], a[2]
    #print(t1, t2)
    for y in range(min(t1[1], t2[1]), max(t1[1], t2[1]) + 1):
        for x in range(min(t1[0], t2[0]), max(t1[0], t2[0]) + 1):
            if not grid[y][x]:
                #print(f'invalid {a}')
                break
        else:
            continue
        break
    else:
        print(f'valid {a}')
        break
