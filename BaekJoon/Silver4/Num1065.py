#https://www.acmicpc.net/problem/1065

N = int(input())
case = [111, 123, 135, 147, 159, 210, 222, 234, 246, 258, 321, 333, 345, 357, 369, 420, 432, 444, 456, 468, 531, 543, 555, 567, 579, 630, 642, 654, 666, 678, 741, 753, 765, 777, 789, 840, 852, 864, 876, 888, 951, 963, 975, 987, 999]
result = 0

if N < 100:print(N)
else:
    result += 99

    for x in case:
        if N >= x:
            result += 1

    print(result)


