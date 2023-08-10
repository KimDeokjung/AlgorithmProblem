import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

def abc(inputData, checkSum, N, level, fisrtData, lastData):
    tmp = 99999999
    if level == N - 2:
        for index, color in enumerate(inputData[level]):
            if index == lastData or index == fisrtData: continue
            tmp = min(tmp, color)
        return tmp
    else:
        for index, color in enumerate(inputData[level]):
            if index == lastData: continue

            if level * 100 + index * 10 + fisrtData in checkSum:
                tmp = min(tmp, checkSum[level * 100 + index * 10 + fisrtData] + color)
            else:
                newColor = abc(inputData, checkSum, N, level + 1, fisrtData, index)
                tmp = min(tmp, newColor + color)
                checkSum[level * 100 + index * 10 + fisrtData] = newColor
        return tmp


N = int(input())

inputData = []
checkSum = dict()
first = list(map(int, input().split()))
for x in range(N - 1):
    inputData.append(list(map(int, input().split())))

r = abc(inputData, checkSum, N, 0, 0, 0) + first[0]
g = abc(inputData, checkSum, N, 0, 1, 1) + first[1]
b = abc(inputData, checkSum, N, 0, 2, 2) + first[2]

print(min(r, g, b))