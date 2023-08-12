import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

def abc(checkSum, visited, num, result):
    if visited[num]: return
    visited[num] = True

    if checkSum[num] == 0:
        result.append(num)
        return
    else:
        for x in checkSum[num]:
            if visited[x]: continue
            abc(checkSum, visited, x, result)
        result.append(num)

N, M = map(int, input().split())
checkSum = [[] for _ in range(N + 1)]
visited = [False for _ in range(N + 1)]
result = []

for x in range(M):
    A, B = map(int, input().split())
    checkSum[B].append(A)

for x in range(1, N + 1):
    if visited[x]: continue
    abc(checkSum, visited, x, result)

print(*result)