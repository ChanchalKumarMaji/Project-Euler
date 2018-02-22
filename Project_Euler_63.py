    
#N=int(input())  

def digits(n):
    t=str(n)
    return len(t)
              
                
c=0                
for i in range(1,100+1):
    j=1
    while True:
        d=digits(j**i)
        if d==i:
            c=c+1
            #print(i)
        if d>i:
            break    
        j=j+1                
        
print(c) 
