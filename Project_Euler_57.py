N=int(input())

def digits(n):
    t=str(n)
    d=len(t)
    return d
num=3
den=2
#list1=[]
#list2=[]
c=0
for i in range(N-1):
    n=den
    den=num+den
    num=den+n
    #list1.append(num)
    #list2.append(den)
    dn=digits(num)
    dd=digits(den)
    if dn>dd:
        print(i+2)
#print(list1)
#print(list2)    

