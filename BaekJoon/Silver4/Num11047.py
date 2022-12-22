# https://www.acmicpc.net/problem/11047

N, K = map(int, input().split())

coin = list()
result = 0

for x in range(N):coin.insert(0, int(input()))

for x in coin:
    result += K // x
    K %= x

print(result)