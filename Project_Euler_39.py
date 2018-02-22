

max=0


for p in range(3,1000):
    
    items=[]
    for a in range(1,p//2):
        num=p*(p-(2*a))
        den=2*(p-a)
        
        if num%den==0:
            b=num//den
            c=p-a-b
            l=[]
            l.append(a)
            l.append(b)
            l.append(c)
            l.sort()
            if l not in items:
                items.append(l)

    k=len(items)
    if max<k:
        max=k
        n=p
        

print(n)                    
                    
                 
