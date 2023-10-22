import heapq
import sys
input = sys.stdin.readline

N = int(input())
result = []

for x in range(7):
    heapq.heappush(result, -float(input()))

for x in range(N - 7):
    tmp = float(input())
    if -result[0] > tmp:
        heapq.heappop(result)
        heapq.heappush(result, -tmp)

result.sort(key=lambda x:-x)
for x in result:
    print("{:.3f}".format(-x))
