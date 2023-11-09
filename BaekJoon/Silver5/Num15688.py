import sys
input = sys.stdin.readline

N = int(input())
inputData = list()
for _ in range(N):inputData.append(int(input()))

print(*sorted(inputData))