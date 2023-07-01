import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

inputData = []
while True:
    try:
        inputData.append(int(input()))
    except:
        break

def abc(start, end):
    if start == end:
        print(inputData[start])
        return

    left = start + 1
    right = end
    root = inputData[start]

    while left <= right:
        middle = (left + right) // 2

        if inputData[middle] < root:
            left = middle + 1
        else:
            right = middle - 1

    if start + 1 <= left - 1:
        abc(start + 1, left - 1)
    if left <= end:
        abc(left, end)
    print(root)

abc(0, len(inputData) - 1)