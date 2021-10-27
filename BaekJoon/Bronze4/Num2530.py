# https://www.acmicpc.net/problem/2530

a,b,c=map(int,input().split())
d=c+int(input())
e=b+d//60
print((a+e//60)%24,e%60,d%60)