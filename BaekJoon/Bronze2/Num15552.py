#https://www.acmicpc.net/problem/11720

import sys
input = sys.stdin.readline

result = list()

T = int(input())
for x in range(T):
    result.append(sum(map(int, input().split())))

print(*result)