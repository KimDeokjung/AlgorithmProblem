inputData = input()
checkSum = input()
lenCheckSum = len(checkSum)
result = 0

while True:
    if checkSum in inputData:
        inputData = inputData[:inputData.index(checkSum)] + "!" * lenCheckSum + inputData[inputData.index(checkSum) + lenCheckSum:]
        result += 1
    else:
        break

print(result)

