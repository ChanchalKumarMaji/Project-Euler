n=10000
list=[]
cycles=[]
prime = [True for i in range(n+1)]
p = 2
while (p * p <= n):
    if (prime[p] == True):
        for i in range(p * 2, n+1, p):
            prime[i] = False
    p += 1
     
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
            return c
        

for p in range(2, n+1):
    if prime[p]:
        k=cycle(p)
        cycles.append(k)
        list.append(p)
          
#print(list)            

length=len(list)

T=int(input())
for i in range(T):
    n=int(input())
    max=0
    for i in range(length):
        p=list[i]
        if p<n:
            if max<cycles[i]:
                max=cycles[i]
                f=p
        else:
            break
            
    print(f)        
