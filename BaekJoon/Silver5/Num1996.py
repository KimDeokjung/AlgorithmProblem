N = int(input())
inputData = list()
result = [[0 for _ in range(N)] for _ in range(N)]
for _ in range(N): inputData.append(input())

flag = [(-1, 1), (0, 1), (1, 1), (1, 0), (-1, 0), (-1, -1), (0, -1), (1, -1)]
for x in range(N):
    for y in range(N):
        if inputData[x][y] != ".":
            result[x][y] = "*"
        else:
            tmp = 0
            for i, j in flag:
                nowX = x + i
                nowY = y + j
                if 0 <= nowX < N and 0 <= nowY < N and inputData[nowX][nowY] != ".":
                    tmp += int(inputData[nowX][nowY])
            if tmp > 9:
                result[x][y] = "M"
            else:
                result[x][y] = str(tmp)

for x in result:
    print("".join(x))