# https://www.acmicpc.net/problem/10162

A, B, C = 300, 60, 10
target = int(input())
if target%A%B%C == 0:
    print(target//A, target%A//B, target%A%B//C)
else:print(-1)
