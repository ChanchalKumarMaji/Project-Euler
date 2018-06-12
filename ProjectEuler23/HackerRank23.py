import math

# Properties of Abundant Numbers
# 1. Every positive multiple greater than 1 of a perfect number is abundant 
# 2. Every positive multiple of an abundant number is abundant.

def check(n):
    s = 0
    for i in range(1, int(math.sqrt(n))+1):
        if n%i == 0:
            if n/i == i:
                s += i
            else:
                s += i
                s += n/i
    s = s-n            
    if n == s:
        return 'P'
    elif n < s:
        return 'A'
    elif n > s:
        return 'D'
                   

# Generating Abundant Numbers less than 28123
def abundant():
    nos = [0 for i in range(28123 + 1)]
    
    for i in range(12, 28123 + 1):
        if nos[i] == 0:
            if check(i) == 'P':
                for j in range(2*i, 28123+1, i):
                    nos[j] = 1
            elif check(i) == 'A':
                for j in range(i, 28123+1, i):
                    nos[i] = 1
                    
    #for i in range(28123+1):
    #    if nos[i] == 1:
    #        print(i, end=" ")
    #print()
    
    return nos

nos = abundant() 

def solve(n):
    global nos
    for i in range(12, 28123+1):
        if nos[i] == 1 and nos[n-i] == 1:
            return True
        if i > n-i:
            return False
        
    

t = int(input())
for t0 in range(t):
    n = int(input())
    if n > 28123:
        print("YES")
    elif solve(n):
        print("YES")
    else:
        print("NO") 
            
