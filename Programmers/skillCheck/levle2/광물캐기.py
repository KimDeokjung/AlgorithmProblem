def abc(point, picks, minerals):
    if picks == 0: return 0
    originPick = picks
    result = 9999

    stone = picks % 10
    picks //= 10
    iron = picks % 10
    picks //= 10
    dia = picks % 10

    if stone != 0:
        tmp = 0
        for x in minerals[point: point + 5]:
            if x == "stone":
                tmp += 1
            elif x == "iron":
                tmp += 5
            else:
                tmp += 25
        if point + 5 < len(minerals):
            tmp += abc(point + 5, originPick - 1, minerals)
        result = min(tmp, result)

    if iron != 0:
        tmp = 0
        for x in minerals[point: point + 5]:
            if x == "stone":
                tmp += 1
            elif x == "iron":
                tmp += 1
            else:
                tmp += 5
        if point + 5 < len(minerals):
            tmp += abc(point + 5, originPick - 10, minerals)
        result = min(tmp, result)

    if dia != 0:
        tmp = 0
        for x in minerals[point: point + 5]:
            tmp += 1
        if point + 5 < len(minerals):
            tmp += abc(point + 5, originPick - 100, minerals)
        result = min(tmp, result)

    return result

def solution(picks, minerals):
    answer = 0
    tmp = picks[0] * 100 + picks[1] * 10 + picks[2]

    answer = abc(0, tmp, minerals)

    return answer


print(solution([1,3,1], ["diamond", "diamond", "diamond", "iron", "iron", "diamond", "iron", "stone"]))

