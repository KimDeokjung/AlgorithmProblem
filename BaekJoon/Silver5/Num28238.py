from itertools import combinations
import sys
input = sys.stdin.readline

N = int(input())
inputData = list()
resultNum = 0
resultData = [1, 1, 0, 0, 0]
for x in range(N): inputData.append(list(map(int, input().split())))

for x, y in combinations([0, 1, 2, 3, 4], 2):
    tmp = 0
    for data in inputData:
        if data[x] == data[y] == 1: tmp += 1
    if resultNum < tmp:
        resultNum = tmp
        resultData = [0, 0, 0, 0, 0]
        resultData[x] = 1
        resultData[y] = 1

print(resultNum)
print(*resultData)


