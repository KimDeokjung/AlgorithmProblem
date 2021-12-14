#https://www.acmicpc.net/problem/2108

import sys
input = sys.stdin.readline

N = int(input())
inputData = list()
result = list()
for x in range(N):inputData.append(int(input()))

# 평균
result.append(round(sum(inputData) / N))

# 중앙값
inputData.sort()
result.append(inputData[N // 2])

# 최빈값
inputCount = set(inputData)
mode = list()
modeData = -1
for x in inputCount:
    dataCount = inputData.count(x)
    if dataCount > modeData:
        modeData = dataCount
        mode = [x]
    elif dataCount == modeData:
        mode.append(x)
mode.sort()
if len(mode) == 1:result.append(mode[0])
else:result.append(mode[1])

# 범위
result.append(inputData[N - 1] - inputData[0])

print(*result)