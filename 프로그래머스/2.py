def solution(n, horizontal):
    answer = [[0 for col in range(n)] for row in range(n)]

    point = 1
    for x in range(n):
        if x % 2 == horizontal:
            col = 0
            row = x
            for y in range(2 * x + 1):
                answer[col][row] = point
                point += 1
                if y >= x:row -= 1
                else: col += 1
        else:
            col = x
            row = 0
            for y in range(2 * x + 1):
                answer[col][row] = point
                point += 1
                if y >= x:col -= 1
                else: row += 1
    return answer


