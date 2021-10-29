# https://www.acmicpc.net/problem/4299

a,b=map(int,input().split())
c=a+b
if c%2==1 or c//2>a or c<0:print(-1)
else:print(c//2,a-c//2)
