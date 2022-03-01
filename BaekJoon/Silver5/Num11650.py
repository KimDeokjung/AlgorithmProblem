# https://www.acmicpc.net/problem/11650

N = int(input())
inputData = list()

for x in range(N):
    inputData.append(list(map(int,input().split())))

inputData.sort(key = lambda x:[x[0], x[1]])

for x in inputData:
    print(*x)