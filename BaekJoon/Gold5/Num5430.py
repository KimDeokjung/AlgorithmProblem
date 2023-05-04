# import sys
# input = sys.stdin.readline

T = int(input())
totalResult = list()
for _ in range(T):
    p = input()
    n = int(input())
    tmp = input()[1:-1].split(",")
    inputData = list(map(int,tmp)) if tmp[0] != "" else []
    start = 0
    end = n - 1
    isReverse = 0
    error = False
    for x in p:
        if x == "R":
            start, end = end, start
            isReverse = (isReverse + 1) % 2
        else:
            if (not isReverse and start > end) or (isReverse and start < end):
                totalResult.append("error")
                error = True
                break

            if isReverse:
                start -= 1
            else:
                start += 1

    if error:continue

    if isReverse:
        start = n - start - 1
        end = n - end
        inputData.reverse()
    else:
        end += 1

    totalResult.append(inputData[start : end])

for x in totalResult:
    print(str(x).replace(" ", ""))

