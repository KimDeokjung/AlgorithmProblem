import heapq
import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    maxHeap = []
    minHeap = []
    totalNum = 0
    count = int(input())
    flag = [False for _ in range(count)]

    for x in range(count):
        f, n = input().split()
        n = int(n)

        if f == "I":
            heapq.heappush(minHeap, (n, x))
            heapq.heappush(maxHeap, (-n, x))
            flag[x] = True
            totalNum += 1
        elif n == 1 and totalNum > 0:
            while True:
                popData = heapq.heappop(maxHeap)
                if flag[popData[1]]:
                    flag[popData[1]] = False
                    break
            totalNum -= 1
            if totalNum == 0: maxHeap = []
        elif n == -1 and totalNum > 0:
            while True:
                popData = heapq.heappop(minHeap)
                if flag[popData[1]]:
                    flag[popData[1]] = False
                    break
            totalNum -= 1
            if totalNum == 0: minHeap = []

    if totalNum == 0: print("EMPTY")
    else:
        while not flag[maxHeap[0][1]]:
            heapq.heappop(maxHeap)
        while not flag[minHeap[0][1]]:
            heapq.heappop(minHeap)

        print(-maxHeap[0][0], minHeap[0][0])