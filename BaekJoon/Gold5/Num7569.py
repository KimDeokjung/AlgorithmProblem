M, N, H = map(int, input().split())

inputData = list()
flag = list()
trashCount = 0
totalCount = 0
nowCount = 0
result = 0

for _ in range(H):
    tmp = list()
    for __ in range(N):
        tmp2 = list(map(int, input().split()))
        for index, ___ in enumerate(tmp2):
            if ___ == -1:
                trashCount += 1
            elif ___ == 1:
                nowCount += 1
                flag.append([_, __, index])
        tmp.append(tmp2)

    inputData.append(tmp)

totalCount = M * N * H - trashCount

while totalCount > nowCount:
    tmp = list()

    for s_h, s_n, s_m in flag:
        if s_h - 1 >= 0 and inputData[s_h - 1][s_n][s_m] == 0:
            inputData[s_h - 1][s_n][s_m] = 1
            nowCount += 1
            tmp.append([s_h - 1, s_n, s_m])
        if s_h + 1 < H and inputData[s_h + 1][s_n][s_m] == 0:
            inputData[s_h + 1][s_n][s_m] = 1
            nowCount += 1
            tmp.append([s_h + 1, s_n, s_m])
        if s_n - 1 >= 0 and inputData[s_h][s_n - 1][s_m] == 0:
            inputData[s_h][s_n - 1][s_m] = 1
            nowCount += 1
            tmp.append([s_h, s_n - 1, s_m])
        if s_n + 1 < N and inputData[s_h][s_n + 1][s_m] == 0:
            inputData[s_h][s_n + 1][s_m] = 1
            nowCount += 1
            tmp.append([s_h, s_n + 1, s_m])
        if s_m - 1 >= 0 and inputData[s_h][s_n][s_m - 1] == 0:
            inputData[s_h][s_n][s_m - 1] = 1
            nowCount += 1
            tmp.append([s_h, s_n, s_m - 1])
        if s_m + 1 < M and inputData[s_h][s_n][s_m + 1] == 0:
            inputData[s_h][s_n][s_m + 1] = 1
            nowCount += 1
            tmp.append([s_h, s_n, s_m + 1])

    flag = tmp
    result += 1

    if len(flag) == 0:
        result = -1
        break

print(result)

