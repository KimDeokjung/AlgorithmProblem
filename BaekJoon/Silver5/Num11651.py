# https://www.acmicpc.net/problem/11651

N = int(input())
inputData = list()

for x in range(N):
    inputData.append(list(map(int,input().split())))

inputData.sort(key = lambda x:[x[1], x[0]])

for x in inputData:
    print(*x)