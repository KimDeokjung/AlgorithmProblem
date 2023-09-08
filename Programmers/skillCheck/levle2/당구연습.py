def solution(m, n, startX, startY, balls):
    answer = []

    for x, y in balls:
        tmp = []
        result = []
        if startX < x or startY != y:
            point = (y - startY) * startX / (x + startX) + startY
            tmp.append((0, point))
        if startX > x or startY != y:
            point = (y - startY) * (m - startX) / (2*m - x - startX) + startY
            tmp.append((m, point))
        if startY < y or startX != x:
            point = (x - startX) * startY / (startY + y) + startX
            tmp.append((point, 0))
        if startY > y or startX != x:
            point = (x - startX) * (n - startY) / (2*n - y - startY) + startX
            tmp.append((point, n))

        if (startX ** 2 + startY ** 2) < (x ** 2 + y ** 2) and (startY * x / startX) == y: tmp.append((0, 0))
        if (startX ** 2 + (n - startY) ** 2) < (x ** 2 + (n - y) ** 2) and ((n - startY) * x / startX) == (y - n): tmp.append((0, n))
        if ((m - startX) ** 2 + startY ** 2) < ((m - x) ** 2 + y ** 2) and (startY * (m - x) / (m - startX)) == y: tmp.append((m, 0))
        if ((m - startX) ** 2 + (n - startY) ** 2) < ((m - x) ** 2 + (n - y) ** 2) and ((n - startY) * (x - m) / (m - startX)) == (y - n): tmp.append((m, n))

        print(tmp)

        for i, j in tmp:
            a = (abs(i - startX) ** 2 + abs(j - startY) ** 2) ** .5
            b = (abs(i - x) ** 2 + abs(j - y) ** 2) ** .5
            result.append(round((a + b) ** 2))
        answer.append(min(result))

    return answer
