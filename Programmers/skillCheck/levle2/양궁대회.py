def abc(level, info, n, use, nowScore, path, flag):
    if level == 10:
        tmp = flag[use] + path
        return (nowScore, tmp)

    result = []

    if info[level] > 0:
        tmp = path
        tmp = "A" + tmp
        result.append((abc(level + 1, info, n, use, nowScore - 10 + level, tmp, flag)))
    else:
        tmp = path
        tmp = "A" + tmp
        result.append((abc(level + 1, info, n, use, nowScore, tmp, flag)))

    if info[level] + 1 <= use:
        if info[level] > 0:
            tmp = path
            tmp = flag[info[level]] + tmp
            result.append(abc(level + 1, info, n, use - info[level], nowScore - 10 + level, tmp, flag))
        tmp = path
        tmp = flag[info[level] + 1] + tmp
        result.append(abc(level + 1, info, n, use - 1 - info[level], nowScore + 10 - level, tmp, flag))

    return max(result)

def solution(n, info):
    answer = []
    flag = {}
    flag[0] = "A"
    flag[1] = "B"
    flag[2] = "C"
    flag[3] = "D"
    flag[4] = "E"
    flag[5] = "F"
    flag[6] = "G"
    flag[7] = "H"
    flag[8] = "I"
    flag[9] = "J"
    flag[10] = "K"
    flag[11] = "L"
    flag[12] = "M"
    reverseFlag = {}
    reverseFlag["A"] = 0
    reverseFlag["B"] = 1
    reverseFlag["C"] = 2
    reverseFlag["D"] = 3
    reverseFlag["E"] = 4
    reverseFlag["F"] = 5
    reverseFlag["G"] = 6
    reverseFlag["H"] = 7
    reverseFlag["I"] = 8
    reverseFlag["J"] = 9
    reverseFlag["K"] = 10
    reverseFlag["L"] = 11
    reverseFlag["M"] = 12

    result = abc(0, info, n, n, 0, "", flag)
    if result[0] > 1:
        tmp = []
        for x in result[1][::-1]:
            tmp.append(reverseFlag[x])
        return tmp
    else:
        return [-1]

n = 9
info = [0, 0, 1, 2, 0, 1, 1, 1, 1, 1, 1]
print(solution(n, info))
