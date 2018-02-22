n=1000000
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
        if prime[p]:
            list.append(p)
SieveOfEratosthenes(n)           


#print(list) 

def truncable(k):
    l=len(str(k))
    for i in range(1,l):
        k1=k%(10**i)
        if k1 not in list:
            return False
        
        k2=k//(10**i)
        if k2 not in list:
            return False
    return True    











length=len(list)
c=0
sum=0

for i in range(4,length):
    p=list[i]
    if truncable(p):
        print(p)
        sum=sum+p
        c=c+1
            
print()    
print(sum)    
    
    
    

