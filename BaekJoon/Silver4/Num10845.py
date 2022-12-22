#https://www.acmicpc.net/problem/10845

import sys
input = sys.stdin.readline

N = int(input())
stack = list()
result = list()

for x in range(N):
    inputData = list(input().split())
    if inputData[0] == 'push':
        stack.append(inputData[1])
    elif inputData[0] == 'pop':
        if len(stack) == 0: result.append('-1')
        else: result.append(stack.pop(0))
    elif inputData[0] == 'size':
        result.append(len(stack))
    elif inputData[0] == 'empty':
        if len(stack) == 0: result.append('1')
        else: result.append('0')
    elif inputData[0] == 'front':
        if len(stack) == 0: result.append('-1')
        else: result.append(stack[0])
    elif inputData[0] == 'back':
        if len(stack) == 0: result.append('-1')
        else: result.append(stack[-1])

print(*result)