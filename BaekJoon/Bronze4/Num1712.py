# https://www.acmicpc.net/problem/1712

a,b,c=map(int,input().split())
d=c-b
print(a//d+1 if d>0 else -1)
