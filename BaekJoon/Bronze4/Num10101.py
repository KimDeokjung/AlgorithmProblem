# https://www.acmicpc.net/problem/10101

angle = []
for _ in range(3):angle.append(int(input()))
sorted(angle)
if(sum(angle)!=180):print('Error')
elif(angle[2]==60):print('Equilateral')
elif(len(set(angle).union()))==2:print('Isosceles')
else:print('Scalene')