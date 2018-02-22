N,K=map(int,input().split(" "))
list=[]
def reverse(n):
    t=str(n)
    r=''
    length=len(t)
    for i in range(length):
        r=t[i]+r
    r=int(r)
    if r==n:
        return True
    return False        
    
for i in range(1,1000000+1):
    if reverse(i):
        list.append(i)    
        
#print(list) 
 
def reverse(string):
    string = "".join(reversed(string))
    return string 





def binary(n):
    b=''
    while n!=0:
        t=str(n%K)
        b=t+b
        n=n//K
    if b==reverse(b):
        return True
    return False 
         
      
sum=0
for p in list:
    if p<N:
        if binary(p):
            #print(p)
            sum=sum+p
        
print(sum)   








     
           
