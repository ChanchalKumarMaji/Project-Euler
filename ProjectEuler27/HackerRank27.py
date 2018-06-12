n=100000
def SieveOfEratosthenes(n):
    prime = [True for i in range(n+1)]
    prime[0] = False
    prime[1] = False
    p = 2
    while (p * p <= n):
        if (prime[p] == True):
            for i in range(p * 2, n+1, p):
                prime[i] = False
        p += 1
    return prime    
prime = SieveOfEratosthenes(n)

#print(prime)


N = int(input())


B = []
for i in range(2, N+1):
    if prime[i]:
        B.append(i)
#print(B)

m = 0
res = [0, 0]
for a in range(-N, N+1):
    for b in B:
        if ((1+a+b)%2 == 1) or (a==2 and b!=2) or (a!=2 and b==2):
            n = 0
            c = 0
            while True:
                f = n*n + a*n + b
                f = abs(f)
                if prime[f]:
                    c += 1
                else:
                    if m<c:
                        m = c
                        res[0]=a
                        res[1]=b
                    break
                n += 1    
                    
print(res[0], end=" ")
print(res[1])
