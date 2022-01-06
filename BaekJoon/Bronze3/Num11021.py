# https://www.acmicpc.net/problem/11021

N = int(input())
result = list()

for x in range(1, N + 1):
    result.append(f'Case #{x}: {sum(map(int,input().split()))}')

print(*result)

