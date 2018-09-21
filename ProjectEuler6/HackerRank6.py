l=[]
T=int(input())

for i in range(T):
    l.append(int(input()))

for i in range(T):
    n=l[i]
    sum=((n-1)*(n)*(n+1)*(3*n+2))//12
            
    print(sum)
