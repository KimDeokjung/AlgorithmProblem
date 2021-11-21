#https://www.acmicpc.net/problem/11720

num = int(input())
target = input()
result = 0
for x in range(num):
    result += int(target[x])
print(result)