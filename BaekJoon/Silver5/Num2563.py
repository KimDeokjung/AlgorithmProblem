import sys
input = sys.stdin.readline

N = int(input())
checkSum = set()

for _ in range(N):
    i, j = map(int, input().split())
    for x in range(10):
        for y in range(10):
            checkSum.add(str([i + x, j + y]))

print(len(checkSum))