#https://www.acmicpc.net/problem/10989

import sys
input = sys.stdin.readline

N = int(input())
inputData = list()

for x in range(N):inputData.append(int(input()))

print(*sorted(inputData))