def solution(n, left, right):
    answer = []

    start = left // n
    startAt = left % n

    if startAt <= start:
        key = start
        key += 1
    else:
        key = startAt

    for x in range(left, right + 1):
        if startAt <= start:
            answer.append(key)
        else:
            key += 1
            answer.append(key)

        startAt += 1

        if startAt >= n:
            startAt = 0
            start = key = start + 1
            key += 1

    return answer


for x in range(25):
    print(solution(5, x, 24))
