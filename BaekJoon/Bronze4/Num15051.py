# https://www.acmicpc.net/problem/15051

a=int(input())
b=int(input())
c=int(input())
print(min(b*2+c*4,min(a*2+c*2,a*4+b*2)))