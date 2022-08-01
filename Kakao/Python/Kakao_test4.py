import copy
from itertools import combinations

def abc(a, b):
    return len(list(combinations([0] * a, b)))


def solution(q, a):

    answer = -1

    if len(a) == 1:
        target = a[0]
        answer = target ** q - (target - 1) ** q
    else:
        total = 0

        for x in range(len(a)):
            for y in range(len(a) - x):
                lowNum = a[y]
                for z in range(x + 1):
                    if a[y + z] < lowNum:
                        lowNum = a[y + z]
                total += lowNum
                answer = total
        b = copy.deepcopy(a)
        for x in range(len(a)):
            target = -1
            for y in range(len(a)):
                if b[y] != 0 and target == -1:
                    target = y
                elif b[y] != 0 and b[target] > b[y]:
                    target = y
            b[target] = 0
            left = 1
            right = 1
            tmp = 1
            while True:
                if target - tmp < 0:
                    tmp = 1
                    break
                if a[target - tmp] > a[target]:
                    tmp += 1
                    left += 1
                else:
                    tmp = 1
                    break
            while True:
                if target + tmp >= len(a):
                    break
                if a[target + tmp] > a[target]:
                    tmp += 1
                    right += 1
                else:
                    break

            answer = total ** q

            for x in range(q):
                answer -= (total - q + x) ** abc(q, x+1)

    answer %= 998244353
    return answer


print(solution(3, [1, 4, 3, 2]))
