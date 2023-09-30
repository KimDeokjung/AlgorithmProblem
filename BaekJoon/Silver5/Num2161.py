from collections import deque

N = int(input())
result = list()
inputData = deque()

for x in range(1, N + 1): inputData.append(x)
for x in range(N - 1):
    result.append(inputData.popleft())
    inputData.append(inputData.popleft())
result.append(inputData[0])

print(*result)