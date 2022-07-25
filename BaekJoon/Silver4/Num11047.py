# https://www.acmicpc.net/problem/11047

N, K = map(int, input().split())

coin = list()

for x in range(N):
    inputData = int(input())
    if inputData <= K:coin.append(inputData)

