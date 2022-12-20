N, r, c = map(int, input().split())

leftWidth = upHeight = 0
rightWidth = downHeight = 2 ** N - 1

totalIndex = 2 ** (2 * N)
result = 0

for x in range(N):
    totalIndex //= 4
    middleWidth = (leftWidth + rightWidth) // 2
    middleHeight = (upHeight + downHeight) // 2

    if middleHeight < r:
        result += totalIndex * 2
        upHeight = middleHeight + 1
    else:
        downHeight = middleHeight

    if middleWidth < c:
        result += totalIndex
        leftWidth = middleWidth + 1
    else:
        rightWidth = middleWidth

print(result)
