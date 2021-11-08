# https://www.acmicpc.net/problem/13866

friend = list(map(int,input().split()))
allSum = sum(friend)
result = []

for x in range(4):
    for y in range(x+1,4):
        temp = friend[x] + friend[y]
        result.append(abs(allSum - 2*temp))

print(min(result))