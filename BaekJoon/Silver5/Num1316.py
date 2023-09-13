N = int(input())
result = 0

for x in range(N):

    checkSum = set()
    beforeData = ""
    check = True
    for y in input():
        if y == beforeData: continue
        else:
            if y in checkSum:
                check = False
            else:
                beforeData = y
                checkSum.add(y)

    if check: result += 1

print(result)