result = list()

while True:
    T = int(input())
    if T == 0: break

    inputData = list()
    for x in range(T): inputData.append(input())

    tmp = set()
    for x in range(2 * T - 1):
        a, b = input().split()
        if a in tmp: tmp.remove(a)
        else: tmp.add(a)
    a = int(tmp.pop()) - 1
    result.append(inputData[a])

for x in range(len(result)):
    print(str(x + 1) + " " + result[x])
