from collections import deque

def solution(x, y, n):
    checkSum = deque()
    checkSum.append((x, 0))
    flag = set()

    while True:
        if len(checkSum) == 0: break
        num, level = checkSum.popleft()

        if num == y: return level

        nowFlag = [num + n, 2 * num, 3 * num]

        for flagNum in nowFlag:
            if flagNum not in flag and flagNum <= y:
                if flagNum == y:
                    return level + 1
                checkSum.append((flagNum, level + 1))
                flag.add(flagNum)
    return -1
