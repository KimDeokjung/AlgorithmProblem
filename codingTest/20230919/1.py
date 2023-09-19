def checkRule(data, aCount, bCount):
    lenData = len(data)
    if bCount == 0: return True
    if len(data) == 0: return True
    if aCount == 0: return False

    nowACount = aCount
    nowBCount = bCount

    if data[0] == "a" or data[-1] == "a":
        left = 0
        right = lenData - 1

        for x in range(lenData):
            if data[x] == "a":
                left += 1
                nowACount -= 1
            else:
                break

        for x in range(lenData):
            if data[lenData - x - 1] == "a":
                right -= 1
                nowACount -= 1
            else:
                break
        data = data[left:right + 1]
        return checkRule(data, nowACount, nowBCount)
    else:
        left = 0
        right = lenData - 1
        nowCount = 0
        while True:
            if data[left] == data[right] == "b":
                left += 1
                right -= 1
                nowBCount -= 2
                nowCount += 1
            elif data[left] == data[right] == "a":
                if nowCount == nowACount:
                    data = data[left:right + 1]
                    return checkRule(data, nowACount, nowBCount)
                else:
                    return False
            else:
                return False

def solution(a):
    answer = []

    for x in a:
        aCount = 0
        bCount = 0
        for y in x:
            if y == "a": aCount += 1
            else: bCount += 1
        answer.append(checkRule(x, aCount, bCount))

    return answer
