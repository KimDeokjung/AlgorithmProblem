import math
X, Y = map(int, input().split())

nowZ = 100 * Y // X
if nowZ == 100: print(-1)
else:
    nowZ += 1
    if nowZ == 100:
        print(-1)
    else:
        result = math.ceil(((nowZ * X) - (100 * Y)) / (100 - nowZ))
        print(result)
