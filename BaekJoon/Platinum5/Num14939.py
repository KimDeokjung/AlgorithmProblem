inputData = []
checkSum = [[0 for _ in range(10)] for __ in range(10)]
for _ in range(10): inputData.append(input())



for x in range(10):
    for y in range(10):
        tmp = [(1, 0), (-1, 0), (0, 1), (0, -1), (0, 0)]

        for tmpx, tmpy in tmp:
            if -1 < x + tmpx < 10 and -1 < y + tmpy < 10:
                if inputData[x + tmpx][y + tmpy] == "O":checkSum[x][y] += 1

for x in checkSum:
    print(x)


