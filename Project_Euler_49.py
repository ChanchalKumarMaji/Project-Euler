n=10000
list=[]
def SieveOfEratosthenes(n):
     
    # Create a boolean array "prime[0..n]" and initialize
    #  all entries it as true. A value in prime[i] will
    # finally be false if i is Not a prime, else true.
    prime = [True for i in range(n+1)]
    p = 2
    while (p * p <= n):
         
        # If prime[p] is not changed, then it is a prime
        if (prime[p] == True):
             
            # Update all multiples of p
            for i in range(p * 2, n+1, p):
                prime[i] = False
        p += 1
     
    
    for p in range(2, n+1):
        if prime[p] and p>=1000:
            list.append(p)
SieveOfEratosthenes(n)           
#print(list)

def digits(n):
    d=[]
    d.append(n%10)
    n=n//10
    d.append(n%10)
    n=n//10
    d.append(n%10)
    n=n//10
    d.append(n)
    d.sort()
    return d
    
 
#print(digits(6197))    
final=[]
for p in list:
    final.append(digits(p))
length=len(final)

#visited=[False for i in range(1061)]

for i in range(length):
    k=final[i]
    q=[]
    q.append(list[i])
    c=0
    for j in range(i+1,length):
        t=final[j]
        if k==t:
            c=c+1
            q.append(list[j])
    if c==2 and (q[0]+q[2]==q[1]+q[1]):
        print(q)
                
    










                
#print(final)

