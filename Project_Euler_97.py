


n=7830457
digits=[]
t=n
length=0
while t!=0:
    d=t%10
    digits.append(d)
    t=t//10
    length +=1 
   
#print(digits)
#print(length)

list1=[]

c=0
for i in range(length):
    p=(10**c)    
    list1.append(p)
    c+=1
    
#print(list1)

list2=[]

for i in range(length):
    p=(2**list1[i])%10000000000    
    list2.append(p)
    
#print(list2)    

list3=[]

for i in range(length):
    p=(list2[i]**digits[i])%10000000000    
    list3.append(p)
    
#print(list3)    

pro=list3[0]
for i in range(1,length):
    pro=(pro*list3[i])%10000000000
  
#print(pro)

pro=(pro*28433)%10000000000

print(pro)


    




