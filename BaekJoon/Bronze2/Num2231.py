#https://www.acmicpc.net/problem/2231

inputData = int(input())

for x in range(inputData):
    data = x
    result = 0

    result += x
    while x != 0:
        result += x % 10
        x //= 10
    if result == inputData:
        print(data)
        break
else:print(0)

