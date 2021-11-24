# https://www.acmicpc.net/problem/1018

N,M=map(int,input().split())
resultList = [[0]*M for i in range(N)]
result = -1
nowResult = 0
for x in range(N):
    tmp = input()
    for y in range(len(tmp)):
        if (x+y)%2 == 0 and tmp[y] == "B":resultList[x][y] = 1
        elif (x+y)%2 == 1 and tmp[y] == "W":resultList[x][y] = 1

for x in range(N-7):
    for y in range(M-7):
        for i in range(x, x+8):
            for j in range(y, y+8):
                nowResult += resultList[i][j]
        if result < 0 or result > min(nowResult, 64 - nowResult):
            result = min(nowResult, 64 - nowResult)
        nowResult = 0
print(result)