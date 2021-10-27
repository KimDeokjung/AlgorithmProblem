# https://www.acmicpc.net/problem/2525

a,b=map(int,input().split())
c=b+int(input())
print((a+c//60)%24,c%60)