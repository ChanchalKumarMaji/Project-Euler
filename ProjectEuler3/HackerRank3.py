import math
t=int(input())
for t0 in range(t):
    n=int(input())
    l=[]
    f=0
    while n%2==0:
        n=n//2
        f=1
    if f==1:
        l.append(2)
        
    for i in range(3,int(math.sqrt(n))+1,2):
        f=0
        while n%i==0:
            f=1
            n=n//i
        if f==1:
            l.append(i)
            
    if n>2:
        l.append(n)
    print(l[-1])
