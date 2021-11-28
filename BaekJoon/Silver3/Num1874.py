# https://www.acDmicpc.net/problem/1874

num = int(input())
inputData = list()
stack = list()
result = list()
for _ in range(num):inputData.append(int(input()))

target = 1
for x in range(num*2):
    if len(stack) == 0:
        stack.insert(0,target)
        target += 1
        result.append("+")
    else:
        if stack[0] == inputData[0]:
            inputData.pop(0)
            stack.pop(0)
            result.append("-")
        else:
            stack.insert(0, target)
            target += 1
            result.append("+")

if len(stack) == 0:print(*result)
else:print("NO")
