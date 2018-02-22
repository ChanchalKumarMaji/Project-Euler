n=100000
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

length=len(list)
def primeFactorization(n):
    f=1
    for i in range(length):
        p=list[i]
        c=0
        while n%p==0:
            c=c+1
            n=n//p
        f=f*(c+1)
        if n==1:
            return f        
    
    
i=1
while True:
    n=(i*(i+1))//2
    if primeFactorization(n)>500:
        print(n)
        break

    i+=1
    
    
