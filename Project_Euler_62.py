import sys


list=[]
for i in range(0,100000):
    n=i**3
    t=str(n)
    l=len(t)
    l0=[]
    for j in range(l):
        l0.append(int(t[j]))
    l0.sort()
    list.append(l0)    
   
#print(list)
length=len(list)
for i in range(length):
    c=0
    equal=[]
    equal.append(i)
    for j in range(i+1,length):
        if list[i]==list[j]:
            c=c+1
            equal.append(j)
        if c==4:
            print(equal)
            sys.exit()    
            
                
