import heapq
import sys
input = sys.stdin.readline

N, E = map(int, input().split())
inputData = [[-1 for _ in range(N + 1)] for __ in range(N + 1)]

for x in range(E):
    go, end, value = map(int, input().split())
    inputData[go][end] = inputData[end][go] = value

pointOne, pointTwo = map(int, input().split())

def abc(a, b, c):
    flag = [-1 for _ in range(N + 1)]
    checkSum = list()
    tmp = 0

    for x in range(1, N + 1):
        if inputData[a][x] == -1: continue
        heapq.heappush(checkSum, (inputData[a][x], x))

    while tmp != N:
        if len(checkSum) == 0:
            break
        length, point = heapq.heappop(checkSum)

        if flag[point] == -1:
            tmp += 1
            flag[point] = length
        elif flag[point] > length:
            flag[point] = length
        else:
            continue

        for x in range(1, N + 1):
            if inputData[point][x] == -1: continue
            heapq.heappush(checkSum, (inputData[point][x] + length, x))

    return [flag[b], flag[c]]

if min(pointOne, pointTwo) == 1 and max(pointOne, pointTwo) == N:
    tmp1 = abc(1, N, N)
    print(tmp1[0])
elif min(pointOne, pointTwo) == 1:
    pointThree = pointTwo + pointOne - 1
    tmp1 = abc(1, pointThree, pointThree)
    tmp2 = abc(pointThree, N, N)
    if tmp1[0] == -1 or tmp2[0] == -1:
        print(-1)
    else:
        print(tmp1[0] + tmp2[0])
elif max(pointOne, pointTwo) == N:
    pointThree = pointTwo + pointOne - N
    tmp1 = abc(1, pointThree, pointThree)
    tmp2 = abc(pointThree, N, N)
    if tmp1[0] == -1 or tmp2[0] == -1:
        print(-1)
    else:
        print(tmp1[0] + tmp2[0])
else:
    tmp1 = abc(1, pointOne, pointTwo)
    tmp2 = abc(pointOne, pointTwo, N)
    tmp3 = abc(pointTwo, pointOne, N)

    result1 = result2 = 0
    if tmp1[0] == -1 or tmp2[0] == -1 or tmp3[1] == -1:
        result1 = -1
    else:
        result1 = tmp1[0] + tmp2[0] + tmp3[1]
    if tmp1[1] == -1 or tmp2[1] == -1 or tmp3[0] == -1:
        result2 = -1
    else:
        result2 = tmp1[1] + tmp2[1] + tmp3[0]

    if result1 == result2 == -1:
        print(-1)
    elif result1 == -1:
        print(result2)
    elif result2 == -1:
        print(result1)
    else:
        print(min(result1, result2))
