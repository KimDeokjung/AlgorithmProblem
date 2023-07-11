inputData = input()
bomb = input()
bombLen = len(bomb)

checkSum = dict()
result = []
flag = -1

for index, x in enumerate(inputData):
    result.append(x)

    if x == bomb[0]:
        if bombLen == 1:
            result.pop(-1)
            continue
        flag += 1
        checkSum[flag] = 1
    elif flag == -1:
        continue
    else:
        if bomb[checkSum[flag]] == x:
            checkSum[flag] += 1
            if checkSum[flag] == bombLen:
                for x in range(bombLen):
                    result.pop(-1)
                flag -= 1
        else:
            flag = -1

if len(result) == 0:
    print("FRULA")
else:
    for x in result:
        print(x, end="")
