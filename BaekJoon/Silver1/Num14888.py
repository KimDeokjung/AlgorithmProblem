def abc(total, inputData, level, flag, N):
    nowFlag = []
    for x in range(4):
        if flag[x] == 0: continue

        tmp = 0
        if x == 0: tmp = total + inputData[level]
        elif x == 1: tmp = total - inputData[level]
        elif x == 2: tmp = total * inputData[level]
        else:
            if (total < 0 and inputData[level] > 0) or (total > 0 and inputData[level] < 0):
                tmp = abs(total) // abs(inputData[level])
                tmp *= -1
            else:
                tmp = abs(total) // abs(inputData[level])

        nowFlag.append((tmp, x))

    if level == N-1:
        nowResult = [max(nowFlag), min(nowFlag)]
        return nowResult


    nowResult = [[], []]
    for x, y in nowFlag:
        flag[y] -= 1
        tmp = abc(x, inputData, level + 1, flag, N)
        nowResult[0].append(tmp[0])
        nowResult[1].append(tmp[1])
        flag[y] += 1

    return [max(nowResult[0]), min(nowResult[1])]

N = int(input())
inputData = list(map(int, input().split()))
flag = list(map(int, input().split()))

for x, y in abc(inputData[0], inputData, 1, flag, N):
    print(x)
