
def sumdig(n):
    t=str(n)
    l=len(t)
    s=0
    for i in range(l):
        s=s+int(t[i])
    return s    


final=[]

T=int(input())
for i in range(T):
    n=int(input())
        
    p=sumdig(2**n)         
    final.append(p)
    
for i in range(T):
    print(final[i])
