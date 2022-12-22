import sys
input = sys.stdin.readline

N, M = map(int, input().split())

ear = set()
eye = set()

for x in range(N):ear.add(input())
for y in range(M):eye.add(input())

print(len(ear & eye))
for x in sorted(list(ear & eye)):print(x,end="")
