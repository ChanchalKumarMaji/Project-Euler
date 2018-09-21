T=int(input())
list=[]
for i in range(T):
    list.append(int(input()))
    
for i in range(T):
    n=list[i]
    ef1=0
    ef2=2
    sum=ef1+ef2
    while ef2<=n:
        ef3=4*ef2 + ef1
        if ef3>n:
            break
        ef1=ef2
        ef2=ef3
        sum=sum+ef2    
    print(sum)
