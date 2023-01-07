N = int(input())
M = int(input())
S = input()

target = "I"
targetFlag = 0
result = 0

for x in range(len(S)):
    if target == "I" and target == S[x]:
        targetFlag += 1
        target = "O"
    elif target == S[x]:
        target = "I"
    else:
        if x == len(S) - 1:break
        result += max(targetFlag - N, 0)

        if S[x] == "O":
            targetFlag = 0
            target = "I"
        else:
            targetFlag = 1
            target = "O"

result += max(targetFlag - N, 0)
print(result)
