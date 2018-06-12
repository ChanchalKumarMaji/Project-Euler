import collections 

N = 5*(10**6) 
cache = [0 for i in range(N+1)]
#d = collections.defaultdict(int)

cache[1] = 1
cache[2] = 2

def isInMemory(n):
    '''
    if n>N:
        if n in d.keys():
            return d[n]
    else:
        return cache[n]
    '''
    if n<=N:
        return cache[n]
    return 0

def putInMemory(n, count):
    '''
    if n>N:
        d[n] = count
    else:
        cache[n] = count 
    '''
    if n<=N:
        cache[n] = count
    
def prepareCache(n):
    k = n
    count = 0
    l = []
    while k!=1:
        val = isInMemory(k) 
        if val == 0:
            l.append(k)
            count += 1
        else:
            break
        if k % 2 == 0:
            k = k//2
        else:
            k = 3*k + 1
          
    #print(l)
    #print(count)
    
    for e in l:
        putInMemory(e, val+count)
        count -= 1
        
    
for i in range(3,N+1):    
    prepareCache(i) 
 
 

#print(cache[:100])

maximum = [0 for i in range(N+1)]

max_val = 0
max_no = 0
for i in range(1, N+1):
    if cache[i]>=max_val:
        maximum[i] = i
        max_val = cache[i]
    else:
        maximum[i] = maximum[i-1]  
        
#print(cache[:30])
#print(maximum[:30])

T = int(input())
for T0 in range(T):
    N = int(input())
    print(maximum[N]) 
