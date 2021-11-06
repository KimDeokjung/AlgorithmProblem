# https://www.acmicpc.net/problem/11282


h, w =map(int, input().split())
smallNum = min(h, w)
bigNum = max(h, w)
result = list()
if bigNum/3 > smallNum:
    result.append(smallNum)
else:
    result.append(bigNum/3)
if smallNum*3/2 > bigNum:
    result.append(bigNum/3)
else:
    result.append(smallNum/2)
print(max(result))
