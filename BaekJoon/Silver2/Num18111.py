# https://www.acmicpc.net/problem/18111

checkReq = [0]*258
lowNum = highNum = 0
lowBlock = highBlock = 0
result = resultPlace = time = 0
W, H, B = map(int, input().split())
inputData = list()

for x in range(W):
    inputData.append(list(map(int,input().split())))

for x in inputData:
    for y in x:
        checkReq[y] += 1
        if y > 0:
            highNum += 1
            highBlock += y

for x in range(257):
    nowBasket = B + highBlock

    if nowBasket < lowBlock:break

    time += 2 * highBlock
    time += lowBlock

    if result == 0 or result >= time:
        result = time
        resultPlace = x

    highBlock -= highNum
    lowNum += checkReq[x]
    highNum -= checkReq[x + 1]
    lowBlock += lowNum
    time = 0
