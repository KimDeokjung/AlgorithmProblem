N = int(input())
inputData = list()

for _ in range(N):
    inputData.append(input())

if sorted(inputData) == inputData:
    print("INCREASING")
elif sorted(inputData, reverse=True) == inputData:
    print("DECREASING")
else:
    print("NEITHER")