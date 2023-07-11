def solution(maxSize, actions):
    answer = []
    totalAnswer = []
    beforeAction = []
    frontAction = []
    nowPoint = -1
    maxNum = -1

    for action in actions:
        if action == "B":
            if len(beforeAction) == 0: continue
            point = beforeAction.pop(-1)
            if nowPoint != -1:
                frontAction.append(nowPoint)
            nowPoint = point
            answer.append(point)
        elif action == "F":
            if len(frontAction) == 0: continue
            point = frontAction.pop(-1)
            if nowPoint != -1:
                beforeAction.append(nowPoint)
            nowPoint = point
            answer.append(point)
        else:
            frontAction = []
            if nowPoint != -1:
                beforeAction.append(nowPoint)
            point = int(action)
            if len(beforeAction) > 0 and point == beforeAction[-1]:
                beforeAction.pop(-1)
            maxNum = max(point, maxNum)
            nowPoint = int(point)
            answer.append(int(point))

        print(answer)
        print(beforeAction)
        print(frontAction)
        print("-=-=-=-=-=-=")

    flag = [True for _ in range(maxNum + 1)]

    tmp = 0
    for x in answer[::-1]:
        if flag[x]:
            tmp += 1
            totalAnswer.append(str(x))
            flag[x] = False
        if tmp == maxSize:
            break

    return totalAnswer
