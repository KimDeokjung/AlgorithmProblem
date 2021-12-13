#https://www.acmicpc.net/problem/1978

N = int(input())
inputData = list(map(int, input().split()))
result = list()

for x in inputData:
    if x == 1 or 0:continue
    for y in range(2, int(x**.5) + 1):
        if x % y == 0:break
    else:result.append(x)

print(len(result))

