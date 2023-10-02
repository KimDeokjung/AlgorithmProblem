T = int(input())
xFlag = [">", "o", "<"]
yFlag = ["v", "o", "^"]
totalResult = []

for _ in range(T):
    input()
    result = 0

    N, M = map(int, input().split())
    inputData = list()
    for x in range(N): inputData.append(list(input()))

    for x in range(N):
        point = 0
        for y in range(M):
            if inputData[x][y] == xFlag[point]: point += 1
            else:
                point = 0
                if inputData[x][y] == xFlag[point]: point += 1

            if point == 3:
                point = 0
                result += 1

    for y in range(M):
        point = 0
        for x in range(N):
            if inputData[x][y] == yFlag[point]:
                point += 1
            else:
                point = 0
                if inputData[x][y] == yFlag[point]: point += 1

            if point == 3:
                point = 0
                result += 1
    totalResult.append(result)

print(*totalResult)