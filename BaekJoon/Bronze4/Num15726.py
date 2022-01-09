# https://www.acmicpc.net/problem/15726

inputData = list(map(int, input().split()))

print(int([inputData[0] * inputData[1] / inputData[2], inputData[0] / inputData[1] * inputData[2]][inputData[2] > inputData[1]]))
