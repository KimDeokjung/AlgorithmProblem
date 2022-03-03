# https://www.acmicpc.net/problem/10250

N = int(input())
resultList = list()

for x in range(N):
    H, W, many = map(int, input().split())
    result = (many % H) * 100 + many // H + 1
    if many % H == 0:result += H * 100 - 1
    resultList.append(result)

print(*resultList)