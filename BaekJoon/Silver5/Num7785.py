import sys
input = sys.stdin.readline

n = int(input())
checkSum = set()

for x in range(n):
    a, b = input().split()
    if b == "enter": checkSum.add(a)
    else: checkSum.remove(a)

result = list(checkSum)
result.sort()
result.reverse()
print(*result)