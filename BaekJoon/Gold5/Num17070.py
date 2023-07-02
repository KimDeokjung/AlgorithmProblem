N = int(input())
inputData = []
flag = dict()

for x in range(N):
    inputData.append(list(map(int, input().split())))

def abc(xP, yP, type):
    if xP == yP == N - 1:
        return 1

    checkSum = []
    result = 0

    if type == 1:
        if yP + 1 < N and inputData[xP][yP + 1] == 0:
            checkSum.append((xP, yP + 1, 1))
        if xP + 1 < N and yP + 1 < N and inputData[xP + 1][yP + 1] == 0 and inputData[xP][yP + 1] == 0 and inputData[xP + 1][yP] == 0:
            checkSum.append((xP + 1, yP + 1, 2))
    elif type == 2:
        if xP + 1 < N and inputData[xP + 1][yP] == 0:
            checkSum.append((xP + 1, yP, 3))
        if yP + 1 < N and inputData[xP][yP + 1] == 0:
            checkSum.append((xP, yP + 1, 1))
        if xP + 1 < N and yP + 1 < N and inputData[xP + 1][yP + 1] == 0 and inputData[xP][yP + 1] == 0 and inputData[xP + 1][yP] == 0:
            checkSum.append((xP + 1, yP + 1, 2))
    else:
        if xP + 1 < N and inputData[xP + 1][yP] == 0:
            checkSum.append((xP + 1, yP, 3))
        if xP + 1 < N and yP + 1 < N and inputData[xP + 1][yP + 1] == 0 and inputData[xP][yP + 1] == 0 and inputData[xP + 1][yP] == 0:
            checkSum.append((xP + 1, yP + 1, 2))

    for x, y, t in checkSum:
        if ((x * 1000) + (y * 10) + t) in flag:
            result += flag[(x * 1000) + (y * 10) + t]
        else:
            tmp = abc(x, y, t)
            flag[(x * 1000) + (y * 10) + t] = tmp
            result += tmp

    return result

print(abc(0, 1, 1))
