#https://www.acmicpc.net/problem/2577

R=1
for x in range(3):R*=int(input())
for x in range(10):print(str(R).count(str(x)))


