N = int(input())

inputData = []
for x in range(N): inputData.append(input())

a = b = 0

point = 0
for x in range(N):
    for y in range(N):
        if inputData[x][y] == ".": point += 1
        else:
            if point >= 2: a += 1
            point = 0
    if point >= 2: a += 1
    point = 0

point = 0
for x in range(N):
    for y in range(N):
        if inputData[y][x] == ".": point += 1
        else:
            if point >= 2: b += 1
            point = 0
    if point >= 2: b += 1
    point = 0

print(a, b)