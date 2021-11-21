# https://www.acmicpc.net/problem/2579

CheckDir = {}

def CheckMax(num1, list1, list2, resultSum):
    list1Result = num1
    list2Result = 0
    if len(list1) < 3:list1Result += sum(list1)
    elif CheckDir.get(str(list1)) != None: list1Result += CheckDir[str(list1)]
    else:
        list1Result += CheckMax(list1[1],list1[3:],list1[2:],list1[0])
        CheckDir[str(list1)] = list1Result - num1
    if len(list2) < 3:list2Result += sum(list2)
    elif CheckDir.get(str(list2)) != None: list2Result += CheckDir[str(list2)]
    else:
        list2Result += CheckMax(list2[1],list2[3:],list2[2:],list2[0])
        CheckDir[str(list2)] = list2Result
    return max(list1Result, list2Result) + resultSum


num = int(input())
stairs = []
for x in range(num):
    stairs.append(int(input()))
stairs.reverse()
if len(stairs) < 3:print(sum(stairs))
else:print(CheckMax(stairs[1],stairs[3:],stairs[2:], stairs[0]))




