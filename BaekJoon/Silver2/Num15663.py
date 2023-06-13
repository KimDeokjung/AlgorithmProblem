#
# N, M = map(int, input().split())
#
# inputData = list(map(int, input().split()))
# inputData.sort()
#
# checkSum = set()
#
# def abc(depth, data, checkData, flag):
#     if flag == N-1: return
#
#     if depth + 1 == M:
#         for x in range(flag + 1, N):
#             if checkData * 10 + inputData[x] not in checkSum:
#                 data[depth] = inputData[x]
#                 print(*data)
#                 checkSum.add(checkData * 10 + inputData[x])
#     else:
#         for x in range(flag + 1, N):
#             data[depth] = inputData[x]
#             abc(depth + 1, data, checkData * 10 + inputData[x], x)
#
#
# if M == 1:
#     print(*set(inputData))
# else:
#     data = [0 for _ in range(M)]
#     for x in range(N):
#         data[0] = inputData[x]
#         abc(1, data, inputData[x], x)
#

from itertools import permutations

N, M = map(int, input().split())

inputData = list(map(int, input().split()))
inputData.sort()

checkSum = set()


for i in permutations(inputData, M):
    tmp = str(i)
    if tmp not in checkSum:
        checkSum.add(tmp)
        print(*i)

