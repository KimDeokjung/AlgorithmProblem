#https://www.acmicpc.net/problem/11866

N, K = map(int, input().split())
K -= 1
originalK = K

inputData = list(range(1, N + 1))
result = list()

while len(inputData) > 0:
    K %= N
    result.append(inputData.pop(K))
    N -= 1
    K += originalK

print("<", end = "")
for x in range(len(result) - 1):
    print(result[x], end = ", ")
print(result[-1], end = ">")