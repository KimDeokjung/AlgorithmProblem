def solution(k, tangerine):
    answer = 0

    checkSum = dict()
    for x in tangerine:
        if x not in checkSum:
            checkSum[x] = 1
        else:
            checkSum[x] += 1

    flag = []
    for x in checkSum:
        flag.append((x, checkSum[x]))

    flag.sort(key=lambda x: -x[1])

    for x in flag:
        answer += 1
        k -= x[1]
        if k <= 0: break

    return answer

