l = [True for i in range(1000+1)] 
p = 2
while p*p<=1000:
    if l[p]:
        for i in range(p*2, 1000+1, p):
            l[i] = False
    p += 1
primes = [0]    
for i in range(2,1000+1):
    if l[i]:
        primes.append(i)
        
#print(primes)

dp = [[0 for j in range(1000+1)] for i in range(len(primes))]

for i in range(len(primes)):
    dp[i][0] = 1
    
for i in range(1, len(primes)):
    for j in range(1, 1000+1):
        if (j-primes[i])>=0:
            dp[i][j] = dp[i-1][j] + dp[i][j-primes[i]] 
        else:
            dp[i][j] = dp[i-1][j] 
                                     
#print(dp)

T = int(input())
for T0 in range(T):
    N = int(input())
    count = 0
    for e in l[2:N+1]:
        if e:
            count += 1
    
            
    print(dp[count][N])


