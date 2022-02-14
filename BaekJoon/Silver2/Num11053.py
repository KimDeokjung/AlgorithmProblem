#https://www.acmicpc.net/problem/11053

N = int(input())
inputData = list(map(int, input().split()))
checksum = [0] * N

for backP in range(N - 1, -1, -1):
    max_increase = 1
    for checkP in range(backP + 1, N):
        if inputData[backP] < inputData[checkP] and max_increase < 1 + checksum[checkP]:
            max_increase = 1 + checksum[checkP]
    checksum[backP] = max_increase

print(max(checksum))
