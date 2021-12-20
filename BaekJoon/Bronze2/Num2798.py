#https://www.acmicpc.net/problem/2798

N, target = map(int, input().split())
inputData = list(map(int, input().split()))
result = -1

for i in range(N):
    for j in range(i + 1, N):
        for k in range(j + 1, N):
            blackJ = target - inputData[i] - inputData[j] - inputData[k]
            if result < 0 or (-1 < blackJ < result):
                result = blackJ

print(target - result)

