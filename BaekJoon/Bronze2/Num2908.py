#https://www.acmicpc.net/problem/2908

A,B=input().split()
for x in range(2,-1,-1):
    if A[x] < B[x]:print(f'{B[2]}{B[1]}{B[0]}');break
    elif A[x] > B[x]:print(f'{A[2]}{A[1]}{A[0]}');break