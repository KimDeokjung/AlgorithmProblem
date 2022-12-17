N, M = map(int, input().split())

ladder = dict()
snake = dict()

for x in range(N):
    start, end = map(int, input().split())
    start -= 1
    end -= 1
    ladder[end] = start


for x in range(M):
    start, end = map(int, input().split())
    start -= 1
    end -= 1
    snake[start] = end

result = [0] * 100

nowLocation = 0
while nowLocation != 99:
    nowLocation += 1
    nowResult = set()
    for x in range(1, 7):
        nowResult.add(result[max([0, nowLocation - x])] + 1)
    if nowLocation in ladder:
        nowResult.add(result[ladder[nowLocation]])
    result[nowLocation] = min(nowResult)

    if nowLocation in snake:
        if result[nowLocation] < result[snake[nowLocation]]:
            result[snake[nowLocation]] = result[nowLocation]
            nowLocation = snake[nowLocation]
        else:
            result[nowLocation] = 100


print(result[99])
