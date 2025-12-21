#!/usr/bin/env python3

with open('input') as f:
    boxes, distances = [tuple(map(int, l.split(','))) for l in f.read().splitlines()], []

for i, b1 in enumerate(boxes):
    for b2 in boxes[i + 1:]:
        d = ((b1[0] - b2[0]) ** 2 + (b1[1] - b2[1]) ** 2 + (b1[2] - b2[2]) ** 2) ** 0.5
        distances.append([d, b1, b2])

distances.sort(key=lambda d: d[0])
circuits, circuits_index = [], {}

for d in distances:
    if (b1_index := circuits_index.get(d[1])) is not None and (b2_index := circuits_index.get(d[2])) is not None:
        if b1_index == b2_index:
            continue

        b2_circuit = circuits.pop(b2_index)
        circuits.insert(b2_index, [])
        circuits[b1_index].extend(b2_circuit)

        for b in b2_circuit:
            circuits_index[b] = b1_index
    elif (b1_index := circuits_index.get(d[1])) is not None:
        circuits[b1_index].append(d[2])
        circuits_index[d[2]] = b1_index
    elif (b2_index := circuits_index.get(d[2])) is not None:
        circuits[b2_index].append(d[1])
        circuits_index[d[1]] = b2_index
    else:
        circuits.append([d[1], d[2]])
        circuits_index[d[1]] = circuits_index[d[2]] = len(circuits) - 1

    if len(circuits) > 1 and len(set(circuits_index.values())) == 1:
        print(d[1][0] * d[2][0])
        break
