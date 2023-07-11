def solution(s, N):
    checkSum = [False for _ in range(10)]
    inputData = []

    for x in range(1, N + 1):
        checkSum[x] = True

    for x in range(len(s) - N + 1):
        flag = True
        tmp = ""

        for y in range(x, x + N):
            nowNum = int(s[y])
            if not checkSum[nowNum]:
                flag = False
                break
            else:
                tmp += s[y]
                checkSum[nowNum] = False

        if flag:
            inputData.append(int(tmp))

        for y in range(1, N + 1):
            checkSum[y] = True
    if len(inputData) == 0:
        return -1
    return max(inputData)

print(solution("12", 2))