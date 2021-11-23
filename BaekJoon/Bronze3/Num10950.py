#https://www.acmicpc.net/problem/10950

result = []
num = int(input())
for x in range(num):result.append(sum(map(int,input().split())))
print(*result)