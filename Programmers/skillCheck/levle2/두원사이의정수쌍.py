def solution(r1, r2):
    answer = 0

    totaly = 0
    totalNew = 0

    for x in range(1, r2 + 1):
        y = int((r2 ** 2 - x ** 2) ** .5)
        answer += y + 1
        totaly += y
        if x < r1:
            newY = int((r1 ** 2 - x ** 2) ** .5 - 0.000000001)
            answer -= newY + 1
            totalNew += newY

    return answer * 4
