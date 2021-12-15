#https://www.acmicpc.net/problem/2108

import sys
input = sys.stdin.readline

N = int(input())
inputData = list()
result = list()
for x in range(N): inputData.append(int(input()))

# 평균
result.append(round(sum(inputData) / N))

# 중앙값
inputData.sort()
result.append(inputData[N // 2])

# 최빈값
modeData = -1
modeCount = 1
mode = list()
for x in range(len(inputData) - 1):
    if inputData[x] == inputData[x + 1]:
        modeCount += 1
    else:
        if modeCount > modeData:
            modeData = modeCount
            mode = [inputData[x]]
        elif modeCount == modeData:
            mode.append(inputData[x])
        modeCount = 1
if modeCount > modeData:
    mode = [inputData[N - 1]]
elif modeCount == modeData:
    mode.append(inputData[N - 1])

if len(mode) == 1:
    result.append(mode[0])
else:
    result.append(mode[1])

# 범위
result.append(inputData[N - 1] - inputData[0])

print(*result)
