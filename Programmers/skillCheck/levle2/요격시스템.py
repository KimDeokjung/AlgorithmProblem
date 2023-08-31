def solution(targets):
    targets.sort(key=lambda x:x[0])
    result = 0
    flag = 0
    lenTarget = len(targets)

    for x in range(lenTarget):
        if flag > 0:
            flag -= 1
            continue

        y, z = targets[x]
        flag = 1
        while x + flag < lenTarget:
            if z > targets[x + flag][0]:
                z = min(z, targets[x + flag][1])
                flag += 1
            else:
                flag -= 1
                break
        result += 1
    return result

