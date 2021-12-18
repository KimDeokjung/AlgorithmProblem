#https://www.acmicpc.net/problem/2164

N = int(input()) - 1
result = 0
checkSum = 2
for x in range(N):
    if result == checkSum:
        result = 2
        checkSum *= 2
    else:
        result += 2

print([result, 1][result == 0])
