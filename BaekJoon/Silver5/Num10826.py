a = 0
b = 1

n = int(input())

if n == 1: print(0)
elif n == 2: print(1)

for x in range(n - 1):
    c = b
    b = a + b
    a = c
print(b)