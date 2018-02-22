n=1000000
list=[]
def SieveOfEratosthenes(n):
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
SieveOfEratosthenes(n)           
#print(list)  

def circular(n):
    t=str(n)
    l=len(t)
    for i in range(l):
        k=t[i:]+t[0:i]
        k=int(k)
        if k not in list:
            return False
    return True
    
c=0
length=len(list)
for i in range(length):
    p=list[i]
    if circular(p):
        print(p)
        c=c+1
        
print(c)
