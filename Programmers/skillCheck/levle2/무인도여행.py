def solution(maps):
    inputData = []
    for x in maps:
        inputData.append(list(x))

    answer = []
    lenX = len(maps)
    lenY = len(maps[0])

    for x in range(lenX):
        for y in range(lenY):
            if inputData[x][y] == "X": continue

            checkSum = [(x, y)]
            result = int(inputData[x][y])
            inputData[x][y] = "X"
            while len(checkSum) != 0:
                i, j = checkSum.pop(0)

                for xFlag, yFlag in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    if -1 < i + xFlag < lenX and -1 < j + yFlag < lenY and inputData[i + xFlag][j + yFlag] != "X":
                        checkSum.append((i + xFlag, j + yFlag))
                        result += int(inputData[i + xFlag][j+yFlag])
                        inputData[i + xFlag][j+yFlag] = "X"

            answer.append(result)
    answer.sort()
    if len(answer) == 0:
        return [-1]
    return answer


maps = ["XXX","XXX","XXX"]
print(solution(maps))