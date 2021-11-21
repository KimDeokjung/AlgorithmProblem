#https://www.acmicpc.net/problem/2920

a=input()
if(eval(a.replace(" ","<"))):print("ascending")
elif(eval(a.replace(" ",">"))):print("descending")
else:print("mixed")
