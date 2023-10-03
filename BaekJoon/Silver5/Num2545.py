T = int(input())
result = list()

for x in range(T):
    input()
    a, b, c, d = map(int, input().split())
    checkSum = a + b + c
    newA = min([a, b, c])
    newC = max([a, b, c])
    newB = checkSum - newA - newC

    tmp = newC - newB
    if tmp >= d:
        newC -= d
    else:
        d -= tmp
        newC = newB
        tmp = newB - newA

        if 2 * tmp >= d:
            tmp2 = d // 2
            tmp3 = d - tmp2
            newB -= tmp2
            newC -= tmp3
        else:
            d -= tmp
            d -= tmp
            newB = newA
            newC = newA
            tmp = d // 3
            d -= tmp
            tmp2 = d // 2
            tmp3 = d - tmp2
            newA -= tmp
            newB -= tmp2
            newC -= tmp3
    result.append(newA * newB * newC)

print(*result)