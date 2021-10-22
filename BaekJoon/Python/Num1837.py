# https://www.acmicpc.net/problem/1837

a,b=map(int,input().split())
while 1:
    b-=1
    if b<0:print("GOOD");break
    if a%b==0:print("BAD",min(b,a/b));break
