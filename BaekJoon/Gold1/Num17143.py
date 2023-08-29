def abc(level, R, C, shark, checkSum, result):
    if level == C: return

    catchr = -1
    catchc = -1
    newBoard = [[0 for _ in range(C)] for __ in range(R)]
    newShark = []
    flag = dict()

    for x in range(R):
        if checkSum[x][level] == 0: continue

        catchr = x
        catchc = level
        break

    if catchr != -1: result[0] += checkSum[catchr][catchc]

    for r, c, s, d, z in shark:
        if r == catchr and c == catchc: continue
        newD = -1

        if d == 1:
            newD = 1
            r = (2 * R - 2) - r
            r %= (2 * R - 2)
            r += s
            r %= (2 * R - 2)

            if r >= R:
                r = (2 * R - 2) - r
            else:
                newD = 2
        elif d == 2:
            newD = 2
            r %= (2 * R - 2)
            r += s
            r %= (2 * R - 2)

            if r >= R:
                r = (2 * R - 2) - r
                newD = 1
        elif d == 3:
            newD = 3
            c %= (2 * C - 2)
            c += s
            c %= (2 * C - 2)

            if c >= C:
                c = (2 * C - 2) - c
                newD = 4
        elif d == 4:
            newD = 4
            c = (2 * C - 2) - c
            c %= (2 * C - 2)
            c += s
            c %= (2 * C - 2)

            if c >= C:
                c = (2 * C - 2) - c
            else:
                newD = 3

        if newBoard[r][c] < z:
            newBoard[r][c] = z
            flag[r * 1000 + c] = [r, c, s, newD, z]

    for x in flag:
        newShark.append(flag[x])

    abc(level + 1, R, C, newShark, newBoard, result)
    return

R, C, M = map(int, input().split())
shark = []
result = [0]
checkSum = [[0 for _ in range(C)] for __ in range(R)]

for x in range(M):
    r, c, s, d, z = map(int, input().split())
    r -= 1
    c -= 1
    if checkSum[r][c] < z:
        checkSum[r][c] = z
        shark.append([r, c, s, d, z])

abc(0, R, C, shark, checkSum, result)

print(*result)