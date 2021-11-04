# https://www.acmicpc.net/problem/10797

target = int(input())
num = list(map(int, input().split()))
result = 0

for x in num:
    if x == target:
        result+=1

print(result)