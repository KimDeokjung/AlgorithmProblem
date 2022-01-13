#https://www.acmicpc.net/problem/10989

import sys
input = sys.stdin.readline

result = [0] * 10000

N = int(input())

for x in range(N):result[int(input()) -1] += 1

for x in range(10000):
    for y in range(result[x]):
        print(x + 1)

