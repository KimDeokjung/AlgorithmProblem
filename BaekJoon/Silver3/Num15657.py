import itertools

N, M = map(int, input().split())

inputData = list(map(int, input().split()))
inputData.sort()


for x in itertools.product(inputData, repeat = M):
    print(*x)