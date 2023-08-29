import sys
sys.setrecursionlimit(50000)

def up(level, N, inputData):
    result = 0
    newData = [[0 for _ in range(N)] for __ in range(N)]

    for x in range(N):
        tmp = []
        flag = -1
        for y in range(N):
            if inputData[y][x] == 0: continue
            if flag == -1:
                flag = inputData[y][x]
                tmp.append(flag)
            else:
                if flag == inputData[y][x]:
                    tmp[-1] *= 2
                    flag = -1
                else:
                    flag = inputData[y][x]
                    tmp.append(flag)

        for index, y in enumerate(tmp):
            newData[index][x] = y

    if level == 5:
        result = 0
        for x in range(N):
            result = max(result, max(newData[x]))
    else:
        result = max(up(level + 1, N, newData), down(level + 1, N, newData), left(level + 1, N, newData), right(level + 1, N, newData))

    return result

def down(level, N, inputData):
    result = 0
    newData = [[0 for _ in range(N)] for __ in range(N)]

    for x in range(N):
        tmp = []
        flag = -1
        for y in range(N - 1, -1, -1):
            if inputData[y][x] == 0: continue
            if flag == -1:
                flag = inputData[y][x]
                tmp.append(flag)
            else:
                if flag == inputData[y][x]:
                    tmp[-1] *= 2
                    flag = -1
                else:
                    flag = inputData[y][x]
                    tmp.append(flag)

        for index, y in enumerate(tmp):
            newData[N - index - 1][x] = y

    if level == 5:
        result = 0
        for x in range(N):
            result = max(result, max(newData[x]))
    else:
        result = max(up(level + 1, N, newData), down(level + 1, N, newData), left(level + 1, N, newData), right(level + 1, N, newData))

    return result

def left(level, N, inputData):
    result = 0
    newData = [[0 for _ in range(N)] for __ in range(N)]

    for x in range(N):
        tmp = []
        flag = -1
        for y in range(N):
            if inputData[x][y] == 0: continue
            if flag == -1:
                flag = inputData[x][y]
                tmp.append(flag)
            else:
                if flag == inputData[x][y]:
                    tmp[-1] *= 2
                    flag = -1
                else:
                    flag = inputData[x][y]
                    tmp.append(flag)

        for index, y in enumerate(tmp):
            newData[x][index] = y

    if level == 5:
        result = 0
        for x in range(N):
            result = max(result, max(newData[x]))
    else:
        result = max(up(level + 1, N, newData), down(level + 1, N, newData), left(level + 1, N, newData), right(level + 1, N, newData))

    return result

def right(level, N, inputData):
    result = 0
    newData = [[0 for _ in range(N)] for __ in range(N)]

    for x in range(N):
        tmp = []
        flag = -1
        for y in range(N - 1, -1, -1):
            if inputData[x][y] == 0: continue
            if flag == -1:
                flag = inputData[x][y]
                tmp.append(flag)
            else:
                if flag == inputData[x][y]:
                    tmp[-1] *= 2
                    flag = -1
                else:
                    flag = inputData[x][y]
                    tmp.append(flag)

        for index, y in enumerate(tmp):
            newData[x][N - index - 1] = y

    if level == 5:
        result = 0
        for x in range(N):
            result = max(result, max(newData[x]))
    else:
        result = max(up(level + 1, N, newData), down(level + 1, N, newData), left(level + 1, N, newData), right(level + 1, N, newData))

    return result


N = int(input())
inputData = list()
for x in range(N): inputData.append(list(map(int, input().split())))

print(max(up(1, N, inputData), down(1, N, inputData), left(1, N, inputData), right(1, N, inputData)))

