#https://www.acmicpc.net/problem/2869

a,b,c = map(int,input().split())

print(((c - a) // (a - b)) + 1 + ((((c-a) / (a-b))%1 != 0)))
