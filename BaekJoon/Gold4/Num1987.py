R, C = map(int, input().split())
inputData = []
checkSum = dict()
result = 0
visited = [False for _ in range(26)]

for x in range(R):
    inputData.append(list(input()))

def abc(point, depth):
    flag = []
    nowResult = depth
    visited[ord(inputData[point[0]][point[1]]) - 65] = True
    if point[0] > 0: flag.append((point[0] - 1, point[1]))
    if point[1] > 0: flag.append((point[0], point[1] - 1))
    if point[0] < R - 1: flag.append((point[0] + 1, point[1]))
    if point[1] < C - 1: flag.append((point[0], point[1] + 1))

    for x, y in flag:
        if visited[ord(inputData[x][y]) - 65]: continue
        nowResult = max(abc([x, y], depth + 1), nowResult)
        visited[ord(inputData[x][y]) - 65] = False

    return nowResult

print(abc([0, 0], 1))

