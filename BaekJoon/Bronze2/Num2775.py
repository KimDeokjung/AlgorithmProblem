#https://www.acmicpc.net/problem/2775

T = int(input())
result = list()

for x in range(T):
    k = int(input())
    n = int(input())

    houseNum = list(range(1, n+1))
    for y in range(k):
        checkRoomNum = 0
        for z in range(n):
            checkRoomNum += houseNum[z]
            houseNum[z] = checkRoomNum
    result.append(houseNum[-1])

print(*result)
