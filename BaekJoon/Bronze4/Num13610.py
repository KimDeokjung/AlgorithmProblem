# https://www.acmicpc.net/problem/13610

a,b = map(int,input().split())
result = 1
while 1:
    if result * b - result * a >= b:
        break
    result+=1
print(result)