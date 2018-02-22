

def iteration(n):
    if n%2==0:
        return n//2
    else:
        return 3*n+1
        
max=0        
for i in range(1,1000000):
    n=i
    c=0
    while True:
        n=iteration(n)
        c=c+1
        if n==1:
            if max<c:
                max=c
                p=i
            break
            
print(p)
print(max)            
                    
