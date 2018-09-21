T=int(input())
l=[]
digit=[]
K=[]
max=0
for i in range(T):
    dig,kd=map(int,input().split())
    l.append(input())
    digit.append(dig)
    K.append(kd)


for i in range(T):
    n=l[i]
    max=0
    d=digit[i]
    k=K[i]
    for j in range(d-k+1):
        t=1
        
        for p in range(j,k+j):
            t=t*(int(n[p]))
        if t>max:
            max=t
        
    print(max)
    
 
