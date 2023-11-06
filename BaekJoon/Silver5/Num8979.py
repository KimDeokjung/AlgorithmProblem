N, K = map(int, input().split())
inputData = list()

for _ in range(N): inputData.append(list(map(int, input().split())))

inputData.sort(key = lambda x:-x[3])
inputData.sort(key = lambda x:-x[2])
inputData.sort(key = lambda x:-x[1])

idx = [inputData[i][0] for i in range(N)].index(K)
for i in range(N):
    if inputData[idx][1:] == inputData[i][1:]:
        print(i+1)
        break