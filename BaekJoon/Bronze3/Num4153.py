#https://www.acmicpc.net/problem/4153

result = list()
while True:
    inputData = list(map(int, input().split()))
    if sum(inputData) == 0:
        break
    inputData.sort()
    if inputData[0] ** 2 + inputData[1] ** 2 == inputData[2] ** 2:result.append("right")
    else:result.append("wrong")
print(*result)