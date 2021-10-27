# https://www.acmicpc.net/problem/1330

a,b=map(int,input().split())
print("<"if a<b else">"if a>b else"==")