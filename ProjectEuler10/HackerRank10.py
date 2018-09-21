T=int(input())
l=[]
for i in range(T):
    l.append(int(input()))



n=1000000

prime = [True for i in range(n+1)]
p = 2
while (p * p <= n):
    if (prime[p] == True):
        for i in range(p*p, n+1, p):
            prime[i] = False
    p += 1
    
list=[]
list.append(0)
list.append(0)
sum=0
for p in range(2,n+1):
    if prime[p]:
        sum=sum+p
        list.append(sum)
    else:
        list.append(list[p-1])    
    
    
for i in range(T):
    N=l[i]
    
    print(list[N])    
        

