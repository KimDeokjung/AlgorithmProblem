import sys
input = sys.stdin.readline
N = int(input())
inputData = list()
for x in range(N): inputData.append(int(input()))

inputData.sort(key = lambda x:-x)
print(*inputData)