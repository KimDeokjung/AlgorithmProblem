def solution(merchantNames):
    answer = []
    totalAnswer = []
    hardSet = ["&", "(", ")", ".", ",", "-"]

    for merchantName in merchantNames:
        if len(answer) == 0:
            flag = False
            for x in merchantName:
                if x in hardSet:
                    flag = True
                    break
            answer.append([merchantName, flag])
            continue
        masterFlag = True

        for x in range(len(answer)):
            flag = True
            beforeHardFlag = False
            hardFlag = False
            lenFlag = min(len(answer[x][0]), len(merchantName))
            flagX = flagMerchant = 0

            while flagX != lenFlag and flagMerchant != lenFlag:
                if merchantName[flagMerchant] in hardSet:
                    hardFlag = True
                    flagMerchant += 1
                    continue
                if answer[x][0][flagX] in hardSet:
                    beforeHardFlag = True
                    flagX += 1
                    continue
                if merchantName[flagMerchant] == " ":
                    flagMerchant += 1
                    continue
                if answer[x][0][flagX] == " ":
                    flagX += 1
                    continue

                if answer[x][0][flagX] != merchantName[flagMerchant]:
                    flag = False
                    break
                flagX += 1
                flagMerchant += 1

            for y in range(flagX, lenFlag):
                if answer[x][0][y] in hardSet: beforeHardFlag = True
            for y in range(flagMerchant, lenFlag):
                if merchantName[y] in hardSet: hardFlag = True

            if flag:
                masterFlag = False
                if hardFlag and not beforeHardFlag:
                    answer[x][0] = merchantName
                    answer[x][1] = True
                    break

                if len(merchantName) > len(answer[x][0]):
                    answer[x][0] = merchantName
                    break

        if masterFlag:
            flag = False
            for x in merchantName:
                if x in hardSet:
                    flag = True
                    break

            answer.append([merchantName, flag])


    for x in range(len(answer)):
        flag = False
        maxLen = 0
        point = 0
        for y in range(len(answer)):
            if flag == False and answer[y][1] == True:
                point = y
                flag = True
                maxLen = len(answer[y][0])
            elif flag == True and answer[y][1] == True and maxLen < len(answer[y][0]):
                maxLen = len(answer[y][0])
                point = y
            elif flag == False and answer[y][1] == False and maxLen < len(answer[y][0]):
                maxLen = len(answer[y][0])
                point = y
        totalAnswer.append(answer[point][0])
        answer[point][0] = ""
        answer[point][1] = False

    return totalAnswer

print(solution(["비 비","비비 "]))