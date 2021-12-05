# https://www.acmicpc.net/problem/2751
import sys
input = sys.stdin.readline

num = int(input())
data = list()
for x in range(num):data.append(int(input()))
print(*sorted(data))
