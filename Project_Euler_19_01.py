T=int(input())
list=[]
for i in range(T):
    Y1,M1,D1=map(int,input().split(" "))
    Y2,M2,D2=map(int,input().split(" "))
    if Y1>Y2:
        d=D1
        m=M1
        y=Y1
        Y1=Y2
        M1=M2
        D1=D2
        Y2=y
        M2=m
        D2=d    
    
    if M1==12 and D1!=1:
        Y1=Y1+1
        M1=1
    if D1!=1 and M1!=12:
        M1=M1+1    
    

    c=0 
    for i in range(Y1,Y2+1):
        for j in range(1,12+1):
            
            if j<M1 and i==Y1:
                continue
            
            k,m,y=1,j,i
            m=((m+9)%12)+1
            C=y//100
            
            if m==11 or m==12:
                D=(y-1)%100
            else:
                D=y%100
            f=k+((13*m-1)//5)+D+(D//4)+(C//4)-(2*C) 
            f=f%7
            if f==0:
                c=c+1
                #print(j,end=" ")
                #print(i)
            if i==Y2 and j==M2:
                break    
    list.append(c)            
for i in range(T): 
    print(list[i])
