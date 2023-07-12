N, K = map(int, input().split())

maxNum = 150000
flag = dict()

result = maxNum
resultNum = 0

checkSum = [(N, 0)]
flag[N] = [1, 0]

if N >= K:
    print(N - K, 1)
else:
    while True:
        point, level = checkSum.pop(0)

        if point == K:
            result = level
            resultNum += 1
        if result < level:
            break

        if point > 0:
            if point - 1 not in flag:
                checkSum.append((point - 1, level + 1))
                flag[point - 1] = [flag[point][0], level]
            else:
                if level == flag[point - 1][1]:
                    flag[point - 1][0] += flag[point][0]
        if point + 1 < maxNum:
            if point + 1 not in flag:
                checkSum.append((point + 1, level + 1))
                flag[point + 1] = [flag[point][0], level]
            else:
                if level == flag[point + 1][1]:
                    flag[point + 1][0] += flag[point][0]
        if point * 2 < maxNum:
            if point * 2 not in flag:
                checkSum.append((point * 2, level + 1))
                flag[point * 2] = [flag[point][0], level]
            else:
                if level == flag[point * 2][1]:
                    flag[point * 2][0] += flag[point][0]
    print(result, flag[K][0])