N, M = map(int, input().split())

inputN = list(map(int, input().split()))
inputN += list(map(int, input().split()))

print(*sorted(inputN))