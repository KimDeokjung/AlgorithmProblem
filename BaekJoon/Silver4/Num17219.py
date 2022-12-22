import sys
input = sys.stdin.readline

N, M = map(int, input().split())
basket = {}

for x in range(N):
    site, pw = input().split()
    basket[site] = pw

for x in range(M):
    print(basket[input()[:-1]])
