inputData = list(input())
Xcount = inputData.count("X")
lenInputData = len(inputData)

for x in range(lenInputData - 1):
    if x < lenInputData - 3 and inputData[x] == inputData[x + 1] == inputData[x + 2] == inputData[x + 3] == "X":
        inputData[x] = "A"
        inputData[x + 1] = "A"
        inputData[x + 2] = "A"
        inputData[x + 3] = "A"
        Xcount -= 4
    elif inputData[x] == inputData[x + 1] == "X":
        inputData[x] = "B"
        inputData[x + 1] = "B"
        Xcount -= 2

if Xcount > 0:
    print("-1")
else:
    print("".join(inputData))
