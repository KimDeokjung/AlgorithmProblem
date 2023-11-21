w, h = map(int, input().split())
result = [0, 0]
N = int(input())

flagX = [0, h]
flagY = [0, w]

for x in range(N):
    tmp, data = map(int, input().split())
    if tmp == 0: flagX.append(data)
    else: flagY.append(data)

flagX.sort()
flagY.sort()

for x in range(len(flagX) - 1):
    result[0] = max(result[0], flagX[x + 1] - flagX[x])

for x in range(len(flagY) - 1):
    result[1] = max(result[1], flagY[x + 1] - flagY[x])

print(result[0] * result[1])
