#https://www.acmicpc.net/problem/2439

N=int(input())
for x in range(N):print(("*"*-~x).rjust(N))