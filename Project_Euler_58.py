def isprime(n):
    f=0
    for i in range(3,n-1,2):
        if n%i==0:
            f=1
            break
             
    if f==1:
        return False
    else:
        return True    


c=0
i=3
while True:
    d=2*(i-1)+1
    n1=i**2
    n2=((i-1)**2)-(i-2)
    n3=((i-1)**2)+1
    n4=(i**2)-(i-1)
    if isprime(n1)==True:
        c=c+1
    if isprime(n2)==True:
        c=c+1
    if isprime(n3)==True:
        c=c+1
    if isprime(n4)==True:
        c=c+1            
    if (c/d)<0.1 :
        break 
    i=i+2
    
print(i)           
