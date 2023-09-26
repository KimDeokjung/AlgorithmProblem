S = list(input())
beforeData = "."
oneNum = 0
zeroNum = 0
for x in S:
    if x != beforeData:
        if x == "0":
            zeroNum += 1
        else:
            oneNum += 1
        beforeData = x

print(min(oneNum, zeroNum))