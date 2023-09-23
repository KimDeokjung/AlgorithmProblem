tmp = 1

x = int(input())
flag = False
while tmp < x:
    x -= tmp
    tmp += 1
    flag = not flag

tmp += 1
if flag:
    j = tmp - x
    i = x
else:
    i = tmp - x
    j = x

print(str(i) + "/" + str(j))
