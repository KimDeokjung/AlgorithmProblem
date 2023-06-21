from itertools import combinations

T = int(input())
mbti = ['ISTJ', 'ISFJ', 'INFJ', 'INTJ', 'ISTP', 'ISFP', 'INFP', 'INTP', 'ESTP', 'ESFP', 'ENFP', 'ENTP', 'ESTJ', 'ESFJ', 'ENFJ', 'ENTJ']
totalResult = []

def checkMbti(a, b):
    check = 0

    for x in range(4):
        if a[x] != b[x]: check += 1

    return check

for x in range(T):
    checkSum = dict()
    inputData = set()
    result = 1000000

    for x in mbti:
        checkSum[x] = 0

    N = int(input())
    for x in input().split():
        checkSum[x] += 1
        inputData.add(x)

    for a, b, c in combinations(inputData, 3):
        flagA = flagB = flagC = 0

        if checkSum[a] >= 3:
            flagA = 0
        elif checkSum[a] == 2:
            flagA = min([2 * checkMbti(a, b), 2 * checkMbti(a, c)])
        else:
            flagA += checkMbti(a, b)
            flagA += checkMbti(c, b)
            flagA += checkMbti(a, c)

        if checkSum[b] >= 3:
            flagB = 0
        elif checkSum[b] == 2:
            flagB = min([2 * checkMbti(a, b), 2 * checkMbti(b, c)])
        else:
            flagB += checkMbti(a, b)
            flagB += checkMbti(c, b)
            flagB += checkMbti(a, c)

        if checkSum[c] >= 3:
            flagC = 0
        elif checkSum[c] == 2:
            flagC = min([2 * checkMbti(a, c), 2 * checkMbti(b, c)])
        else:
            flagC += checkMbti(a, b)
            flagC += checkMbti(c, b)
            flagC += checkMbti(a, c)

        flag = min([flagA, flagB, flagC])
        if result > flag: result = flag

    if len(inputData) == 2:
        a = inputData.pop()
        b = inputData.pop()

        flag = 2 * checkMbti(a, b)
        if result > flag: result = flag

    if result == 1000000: result = 0
    totalResult.append(result)

print(*totalResult)