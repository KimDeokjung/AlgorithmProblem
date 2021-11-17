#https://www.acmicpc.net/problem/1546

input()
S=list(map(int,input().split()))
print(sum(S)/max(S)*100/len(S))
