# https://www.acmicpc.net/problem/2941

Croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

inputData = input()
checkPoint = 0
result = 0

while checkPoint < len(inputData):
    if inputData[checkPoint: checkPoint + 2] in Croatia: checkPoint += 2
    elif inputData[checkPoint: checkPoint + 3] in Croatia: checkPoint += 3
    else: checkPoint += 1
    result += 1

print(result)
