N, M = map(int, input().split())

tmp = list(map(int, input().split()[1:]))
notLie = set(tmp)

partyList = list()
for x in range(M): partyList.append(list(map(int, input().split()[1:])))

flag = set()
while True:
    newLie = set()

    for x in range(len(partyList)):
        if x in flag: continue

        for y in notLie:
            if y in partyList[x]:
                flag.add(x)
                newLie = newLie.union(set(partyList[x]))
                break

    if len(newLie) == 0: break
    else: notLie = notLie.union(newLie)

print(M - len(flag))