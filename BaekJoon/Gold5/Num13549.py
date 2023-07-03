N, K = map(int, input().split())
checkSum = dict()
result = [100001]

def abc(point, round):
    print(point, round)
    flag = []
    nowResult = []
    if point == K: return round

    flag.append((point + 1, round + 1))
    flag.append((point - 1, round + 1))
    flag.append((point * 2, round))

    for p, r in flag:
        if p < 0 or abs(p - point) > (result[0] - round):
            continue
        if p in checkSum:
            nowResult.append(checkSum[p] + r)
        else:
            tmp = abc(p, r)
            nowResult.append(tmp)
            checkSum[p] = tmp - r

    return min(nowResult)

print(abc(N, 1))