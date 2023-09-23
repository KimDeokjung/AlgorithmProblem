from datetime import datetime, timedelta

a = list(map(int, input().split()))
b = list(map(int, input().split()))

timeA = datetime(a[0], a[1], a[2], 0, 0)
timeB = datetime(b[0], b[1], b[2], 0, 0)
result = timeB - timeA

if (b[0] - a[0] == 1000 and b[1] * 300 + b[2] >= a[1] * 300 + a[2]) or b[0] - a[0] > 1000:
    print("gg")
else:
    print("D-" + str(result.days))
