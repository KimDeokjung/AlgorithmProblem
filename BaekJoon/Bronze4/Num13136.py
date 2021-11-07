# https://www.acmicpc.net/problem/13136

W,H,L=map(int,input().split())
print(((W-1)//L+1)*((H-1)//L+1))
