inputData = [False for _ in range(31)]

for x in range(28):
    inputData[int(input())] = True

for index, x in enumerate(inputData[1:]):
    if not x: print(index + 1)