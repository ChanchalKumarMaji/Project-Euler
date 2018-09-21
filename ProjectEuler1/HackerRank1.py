T=int(input())
list=[] 
for i in range(T):
    list.append(int(input()))
 
for i in range(T):
    n=list[i]-1
    k1=n//3
    k2=n//5
    k3=n//15
    s1=k1*(k1+1)*3//2
    s2=k2*(k2+1)*5//2
    s3=k3*(k3+1)*15//2
    s=s1+s2-s3
    print(s)
