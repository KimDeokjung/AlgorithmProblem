def abc(x1, y1, x2, y2, targetX):
    if x2 - x1 == 0:
        return y1

    tmp = (y2 - y1) / (x2 - x1)
    tmp2 = y1 - tmp * x1

    return targetX * tmp + tmp2

x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())

if x1 > x2: x1, y1, x2, y2 = x2, y2, x1, y1
if x3 > x4: x3, y3, x4, y4 = x4, y4, x3, y3

targetX1 = targetX2 = targetY1 = targetY2 = 0
if x1 > x3: targetX1 = x1
else: targetX1 = x3

if x2 < x4: targetX2 = x2
else: targetX2 = x4

if targetX1 > targetX2:
    print(0)
    exit()

tmp1, tmp2, tmp3, tmp4 = abc(x1, y1, x2, y2, targetX1), abc(x3, y3, x4, y4, targetX1), abc(x1, y1, x2, y2, targetX2), abc(x3, y3, x4, y4, targetX2)
flag1 = tmp1 - tmp2
flag2 = tmp3 - tmp4

if x2 - x1 == 0:
    if min(y1, y2) <= tmp2 <= max(y1, y2) or min(y1, y2) <= tmp4 <= max(y1, y2): print(1)
    else: print(0)
elif x4 - x3 == 0:
    if min(y3, y4) <= tmp1 <= max(y3, y4) or min(y3, y4) <= tmp3 <= max(y3, y4): print(1)
    else: print(0)
elif flag1 * flag2 <= 0:
    print(1)
else:
    print(0)