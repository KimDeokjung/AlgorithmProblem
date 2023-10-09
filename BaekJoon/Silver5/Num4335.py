inputData = list()
result = -1
returnData = []

while True:
    num = int(input())
    if num == 0: break
    answer = input()

    if answer == "too high":
        inputData.append((num, True))
    elif answer == "too low":
        inputData.append((num, False))
    else:
        flag = True
        for x, y in inputData:
            if (x > num and y) or (x < num and not y): pass
            else:
                flag = False
                break
        if flag: returnData.append("Stan may be honest")
        else: returnData.append("Stan is dishonest")
        inputData = []

print(*returnData)