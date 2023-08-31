def solution(plans):
    answer = []
    newPlan = []
    stack = []

    for name, start, playtime in plans:
        h, m = map(int, start.split(":"))
        newPlan.append([name, h * 60 + m, int(playtime)])

    newPlan.sort(key=lambda x:x[1])
    nowName, nowStart, nowPlayTime = newPlan.pop(0)


    for name, start, playtime in newPlan:

        if start - nowStart >= nowPlayTime:
            answer.append(nowName)
            time = start - nowStart
            time -= nowPlayTime

            while len(stack) != 0:
                if stack[0][1] <= time:
                    time -= stack[0][1]
                    x, y = stack.pop(0)
                    answer.append(x)
                else:
                    stack[0][1] -= time
                    break

            nowName, nowStart, nowPlayTime = name, start, playtime
        else:
            stack.insert(0, [nowName, nowPlayTime - start + nowStart])
            nowName, nowStart, nowPlayTime = name, start, playtime

    answer.append(nowName)
    for x, y in stack:
        answer.append(x)

    return answer

