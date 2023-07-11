def solution(relationships, target, limit):
    checkSum = []
    flag = set()
    inputData = dict()
    result = 0
    newF = 0

    for x, y in relationships:
        if x not in inputData:
            inputData[x] = [y]
        else:
            inputData[x].append(y)
        if y not in inputData:
            inputData[y] = [x]
        else:
            inputData[y].append(x)

        if x == target:
            checkSum.append([y, 1])
        if y == target:
            checkSum.append([x, 1])

    while len(checkSum) != 0:
        friend, depth = checkSum.pop(0)
        print(friend, depth)
        if friend in flag or friend == target: continue

        if depth == 1:
            result += 5
        elif depth <= limit:
            result += 10
            newF += 1
        else:
            continue

        flag.add(friend)
        if depth == limit: continue

        if friend in inputData:
            for x in inputData[friend]:
                if x not in flag:
                    checkSum.append([x, depth + 1])

    return result + newF

print(solution([[1, 2], [2, 3], [2, 6], [3, 4], [4, 5]], 2, 3))