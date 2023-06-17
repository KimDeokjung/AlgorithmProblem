leftConfig = dict()
rightConfig = dict()

for _ in range(int(input())):
    root, left, right = input().split()

    if left != ".": leftConfig[root] = left
    if right != ".": rightConfig[root] = right

def abc(data):
    print(data, end="")
    if data in leftConfig: abc(leftConfig[data])
    if data in rightConfig: abc(rightConfig[data])

def bcd(data):
    if data in leftConfig: bcd(leftConfig[data])
    print(data, end="")
    if data in rightConfig: bcd(rightConfig[data])

def cde(data):
    if data in leftConfig: cde(leftConfig[data])
    if data in rightConfig: cde(rightConfig[data])
    print(data, end="")

abc("A")
print()
bcd("A")
print()
cde("A")
