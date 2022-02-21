#https://www.acmicpc.net/status?user_id=ejrwnd1103&problem_id=15729&from_mine=1

N = int(input())

inputData = list(map(int, input().split()))

result = [0] * N
count = 0

for x in range(N):
    if result[x] != inputData[x]:
        count += 1
        result[x] = (result[x] + 1) % 2
        result[(x + 1) % N] = (result[(x + 1) % N] + 1) % 2
        result[(x + 2) % N] = (result[(x + 2) % N] + 1) % 2

print(count)