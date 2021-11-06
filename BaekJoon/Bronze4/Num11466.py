# https://www.acmicpc.net/problem/11466

h, w =map(int, input().split())
smallNum = min(h, w)
bigNum = max(h, w)
result = list()
if bigNum/3 < smallNum:
    result.append(bigNum/3)
else:
    result.append(smallNum)

result.append(smallNum/2)

print(max(result))

