#https://www.acmicpc.net/problem/15700
N, M = map(int, input().split())

result = 0

result += (N // 2) * M + (N % 2) * (M // 2)

print(result)
