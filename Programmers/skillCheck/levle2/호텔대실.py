import heapq

def solution(book_time):
    inputData = []
    point = 0
    roomNum = 0
    sideRoom = 0
    flag = set()
    for start, end in book_time:
        startTmp = start.split(":")
        endTmp = end.split(":")
        heapq.heappush(inputData, (60 * int(endTmp[0]) + int(endTmp[1]), point))
        heapq.heappush(inputData, (60 * int(startTmp[0]) + int(startTmp[1]), point))
        point += 1

    while len(inputData) != 0:
        time, num = heapq.heappop(inputData)
        if num == -1:
            sideRoom += 1
        elif num in flag:
            heapq.heappush(inputData, (time + 10, -1))
        else:
            if sideRoom > 0:
                sideRoom -= 1
            else:
                roomNum += 1
            flag.add(num)

    return roomNum


book_time = [["10:20", "12:30"], ["10:20", "12:30"], ["10:20", "12:30"]]
print(solution(book_time))
