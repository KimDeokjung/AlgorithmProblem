# https://www.acmicpc.net/problem/1676

N = int(input())

result = 0
for x in range(1, N+1):
    if x % 125 == 0: result += 3
    elif x % 25 == 0:result += 2
    elif x % 5 == 0:result += 1

print(result)