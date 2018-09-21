def reverse(n):
    t=str(n)
    r=''
    length=len(t)
    for i in range(length):
        r=t[i]+r
    return int(r)    

N=[]
T=int(input())
for i in range(T):
    n=int(input())
    N.append(n)
    
    
palin=[]    

for i in range(100,1000):
    for j in range(100,1000):
        n=i*j
        if reverse(n)==n:
            palin.append(n)

palin.sort()
length=len(palin)

for i in range(T):
    n=N[i]
    for j in range(length):
        if palin[j]>=n:
            print(palin[j-1])
            break 
