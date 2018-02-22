



c=0 
for i in range(1901,2000+1):
    for j in range(1,12+1):
    
        k,m,y=1,j,i
        m=((m+9)%12)+1
        C=y//100
        D=y%100
        if m==11 or m==12:
            D=D-1
        f=k+((13*m-1)//5)+D+(D//4)+(C//4)-(2*C) 
        f=f%7
        if f==0:
            c=c+1
    
 
print(c) 
