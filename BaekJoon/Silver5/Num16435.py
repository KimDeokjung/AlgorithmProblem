N, L = map(int, input().split())
inputData = sorted(list(map(int, input().split())))

while True:
    if len(inputData) == 0: break

    if inputData[0] <= L: inputData.pop(0)
    else: break
    L += 1

print(L)

