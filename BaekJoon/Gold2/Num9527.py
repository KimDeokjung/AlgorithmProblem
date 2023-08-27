def a(b):
    c=2;d=0
    while c<b*2:d+=(b//c*(c//2))+max(b%c-(c//2),0);c*=2
    return d
e,f=map(int,input().split())
print(a(f+1)-a(e))
