def abc(application, coast, point, result, target, N):
    nowResult = result
    nowResult += application[point]
    if result >= target:
        return coast[point]
    if point == N - 1:
        return -1
    flag = 10001

    for x in range(point + 1, N):
        tmp = abc(application, coast, x, nowResult, target, N)
        if tmp == -1:
            continue
        flag = min(flag, tmp)

    return flag + coast[point]


N, M = map(int, input().split())
inputDataA = list(map(int, input().split()))
inputDataC = list(map(int, input().split()))
visited = [False for _ in range(N)]
result = 10001

for x in range(N):
    tmp = abc(inputDataA, inputDataC, x, 0, M, N)
    if tmp == -1: continue
    else:
        print(tmp)

        result = min(result, tmp)

print(result)