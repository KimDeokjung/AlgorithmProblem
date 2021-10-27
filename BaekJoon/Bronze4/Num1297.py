# https://www.acmicpc.net/problem/1297

a,b,c=map(int,input().split())
d=c*c+b*b
print(int((b*b*a*a/d)**.5),int((c*c*a*a/d)**.5))
