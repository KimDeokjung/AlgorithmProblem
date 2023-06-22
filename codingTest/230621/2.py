def solution(S):
    checkSum = dict()
    checkSum["A"] = checkSum["B"] = checkSum["N"] = 0
    result = 0

    for x in S:
        if x in ["A", "B", "N"]:
            checkSum[x] += 1

    while checkSum["A"] >= 3 and checkSum["B"] >= 1 and checkSum["N"] >= 2:
        result += 1
        checkSum["A"] -= 3
        checkSum["B"] -= 1
        checkSum["N"] -= 2

    return result

