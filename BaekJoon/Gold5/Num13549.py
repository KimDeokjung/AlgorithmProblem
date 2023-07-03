N, K = map(int, input().split())
checkSum = [[] for _ in range(150000)]
checkSum[0].append(N)
visited = set()
visited.add(N)
nowStep = 0
result = 130000
flag = True

while flag:
    for x in checkSum[nowStep]:
        tmp = x
        while tmp < 130000:
            if tmp == K or tmp * 2 == K:
                result = min(result, nowStep)
                flag = False
            elif tmp - 1 == K or tmp + 1 == K:
                result = min(result, nowStep + 1)
                flag = False
            visited.add(tmp)
            if tmp + 1 not in visited and tmp + 1 < K + (K // 2):
                visited.add(tmp + 1)
                checkSum[nowStep + 1].append(tmp + 1)
            if tmp - 1 not in visited and tmp - 1 >= 0:
                visited.add(tmp - 1)
                checkSum[nowStep + 1].append(tmp - 1)
            tmp *= 2
            if tmp == 0: break
    nowStep += 1

print(result)