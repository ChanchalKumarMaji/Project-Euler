

def nod(n):
    t=str(n)
    return len(t)
    
def digits(n):
    t=str(n)
    length=len(t)
    l=[]
    for i in range(length):
        l.append(t[i])
    l.sort()
    return l
    
i=100000    
while True:
    n1=i
    n2=2*i
    n3=3*i
    n4=4*i
    n5=5*i
    n6=6*i
    if nod(n1)==nod(n2) and digits(n1)==digits(n2):
        if nod(n2)==nod(n3) and digits(n2)==digits(n3):
            if nod(n3)==nod(n4) and digits(n3)==digits(n4):
                if nod(n4)==nod(n5) and digits(n4)==digits(n5):
                    if nod(n5)==nod(n6) and digits(n5)==digits(n6):
                        print(i)
                        break             
    i=i+1                        
