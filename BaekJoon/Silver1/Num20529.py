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
        flag = 0
        flag += checkSum[a] * checkSum[b] * checkMbti(a, b)
        flag += checkSum[c] * checkSum[b] * checkMbti(c, b)
        flag += checkSum[a] * checkSum[c] * checkMbti(a, c)
        if result > flag: result = flag

    if result == 1000000: result = 0
    totalResult.append(result)

print(*totalResult)