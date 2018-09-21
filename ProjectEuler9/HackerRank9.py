T=int(input())
list=[]
for i in range(T):
    list.append(int(input()))


for i in range(T):
    n=list[i]
    A=[]
    B=[] 
    C=[]
    max=0
    f=0
    for a in range(1,n//3):
        k1=n*(n-2*a)
        k2=(n-a)*2
        if k1%k2==0:
            f=1
            b=k1//k2
            A.append(a)
            B.append(b)
            C.append(n-a-b)
    if f==1:      
        for j in range(len(A)):
            sum=A[j]*B[j]*C[j]
            if sum>max:
                max=sum
        print(max)        
                
    else:
        print(-1)             
