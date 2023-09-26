N, M = map(int, input().split())
inputData = [[0 for _ in range(100)] for __ in range(100)]
result = 0

for x in range(N):
    x1, y1, x2, y2 = map(int, input().split())

    for i in range(x1 - 1, x2):
        for j in range(y1 - 1, y2):
            inputData[i][j] += 1
            if inputData[i][j] == M + 1:
                result += 1

print(result)