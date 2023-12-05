a=[]
def z(a,b,c):
    n[a]+=1
    t[b]="*"
    g[c]="_"

while True:
    i=input()
    if i=="#":break
    g,t=i.split()
    n=[t,0,0,0]
    g=list("*"+g+"*")
    t=list("*"+t+"*")
    l=len(g)-1
    for x in range(1,l):
        if g[x]==t[x]:z(1,x,x)
    for x in range(1,l):
        if g[x]==t[x-1]:z(2,x-1,x)
        elif g[x]==t[x+1]:z(2,x+1,x)
    for x in range(1,l):
        for y in range(1,l):
            if g[x]==t[y]:
                z(3,y,x)
                break
    a.append(n)
for x in a:print(x[0] + ": " + str(x[1]) + " black, " + str(x[2]) + " grey, " + str(x[3]) + " white")

