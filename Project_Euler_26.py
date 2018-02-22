n=10000
list=[]

prime = [True for i in range(n+1)]
p = 2
while (p * p <= n):
    if (prime[p] == True):
        for i in range(p * 2, n+1, p):
            prime[i] = False
    p += 1
     
    
for p in range(2, n+1):
    if prime[p]:
        list.append(p)
          
#print(list)            


def cycle(n):
    c=0
    r=(1%n)*10
    if r==0:
        return 0
    while True:
        r=(r%n)*10
        c=c+1
        if r==0:
            return 0
    
        if r==10:
            break
        
    return c
final=[]
T=int(input())
for i in range(T):
    n=int(input())
    max=0
    for p in list:
        if p<n:
            if max<cycle(p):
                max=cycle(p)
                f=p
        else:
            final.append(f)
            break
            
for i in range(T):                         
    print(final[i])    
    
