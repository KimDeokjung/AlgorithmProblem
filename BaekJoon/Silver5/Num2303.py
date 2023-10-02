from itertools import combinations

N = int(input())
result = [0, 0]
for _ in range(N):
    tmp = 0
    for x in combinations(list(map(int, input().split())), 3):
        nowTmp = sum(x)
        nowTmp %= 10
        tmp = max(nowTmp, tmp)
    if result[1] <= tmp:
        result = [_ + 1, tmp]

print(result[0])