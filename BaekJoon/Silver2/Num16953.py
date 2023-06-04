A, B = map(int, input().split())
checkSum = [(A, 1)]
result = -1

while len(checkSum) != 0:
    flag, depth = checkSum.pop(0)

    for x in [flag * 2, flag * 10 + 1]:
        if x == B:
            result = depth + 1
        elif x < B:
            checkSum.append((x, depth + 1))

print(result)