# def findBeforeAnswer(num):
#     if len(num) % 2 == 1: return num
#     newNum = ""
#
#     for x in range(0, len(num), 2):
#         length = int(num[x])
#         newNum += length * num[x + 1]
#
#     if newNum == num: return num
#     else: return findBeforeAnswer(newNum)
#
# count = 1
# while True:
#     a = input()
#     if a == "0": break
#     print(f"Test {count}: {findBeforeAnswer(a)}")
#     count+=1
#


i=1
z=lambda a,q:a if len(a)%2 or q>99 else z("".join(int(a[x-1])*a[x]for x in range(1,len(a),2)),q+1)
while int(s:=input()):print(f"Test {i}: {z(s,1)}");i+=1
