def solution(S, C):
    result = 0
    checkSum = []
    tmp = []
    flag = "?"

    for x in range(len(S)):
        if S[x] == flag:
            tmp.append(C[x])
        else:
            if len(tmp) > 0: checkSum.append(tmp)
            tmp = [C[x]]
            flag = S[x]

    if len(tmp) > 0: checkSum.append(tmp)

    for x in checkSum:
        result += sum(x)
        result -= max(x)

    return result

