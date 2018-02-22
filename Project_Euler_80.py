import decimal
N=int(input())
P=int(input())

def sum(n):
    t=str(n)
    l=len(t)
    i=0
    while True:
        if t[i]=='.':
            f=i
            break
        i=i+1
        
    s1=0
    
    for i in range(0,f):
        s1=s1+int(t[i])
        
    for i in range(f+1,P+1):
        s1=s1+int(t[i]) 
        #print(s1,end=" ")
               
    return s1
    
list=[]    
for i in range(1,int(N**0.5)+1):
    list.append(i*i)
    
s=0
for i in range(1,N+1):
    if i in list:
        continue
    d2 = decimal.Decimal(i)
# Add a context with an arbitrary precision of 100
    dot100 = decimal.Context(prec=109)
    n=d2.sqrt(dot100) 
    s=s+sum(n)
    
print(s)    
    
