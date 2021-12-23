# https://www.acmicpc.net/problem/10814

N = int(input())
inputData = list()
result = list()

for x in range(N):inputData.append(list(input().split()))
inputData.sort(key = lambda x:int(x[0]))
for x in inputData:print(*x)