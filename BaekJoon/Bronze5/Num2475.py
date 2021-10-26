# https://www.acmicpc.net/problem/2475

a=list(map(int,input().split()))
b=0
for x in a:b+=x*x
print(b%10)