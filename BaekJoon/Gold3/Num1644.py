def sosuNum(n):
    tmp = [True for _ in range(n + 1)]
    result = []
    tmp[0] = False
    tmp[1] = False

    for x in range(2, int(n ** .5) + 1):
        if tmp[x]:
            y = 2
            while x * y <= n:
                tmp[x * y] = False
                y += 1

    for index, x in enumerate(tmp):
        if x: result.append(index)
    return result

N = int(input())
checksum = sosuNum(N)
lenChecksum = len(checksum)

left = right = 0
result = flag = 0

while True:
    if N < flag:
        if left >= lenChecksum: break
        flag -= checksum[left]
        left += 1
    elif N > flag:
        if right >= lenChecksum: break
        flag += checksum[right]
        right += 1
    else:
        if left >= lenChecksum: break
        result += 1
        flag -= checksum[left]
        left += 1

print(result)