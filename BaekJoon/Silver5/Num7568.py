#https://www.acmicpc.net/problem/7568

N = int(input())
inputData = list()
result = [1] * N

for x in range(N):inputData.append(tuple(map(int,input().split())))

for x in range(len(inputData)):
    for y in range(x + 1, len(inputData)):
        if inputData[x][0] > inputData[y][0] and inputData[x][1] > inputData[y][1]:
            result[y] += 1
        elif inputData[x][0] < inputData[y][0] and inputData[x][1] < inputData[y][1]:
            result[x] += 1

print(*result)