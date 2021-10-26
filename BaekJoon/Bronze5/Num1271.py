# https://www.acmicpc.net/problem/1271

a,b=map(int,input().split(" "))
print(int(a//b))
print(a-int(a//b)*b)