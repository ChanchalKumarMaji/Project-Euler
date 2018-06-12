def solve(n):
    l = []
    i = 1
    while n != 0:
        rem = n%i 
        l.append(rem)
        n = n//i
        i += 1
    
    return l[::-1]

chars = [str(i) for i in range(10)]

n = 1000000
n = n - 1
l = solve(n)
res = []
i = 10 - len(l) - 1
        
res = res + chars[:i+1]
    
char = chars[i+1:]
for e in l:
    res.append(char[e])
    char.remove(char[e]) 
ans = ''.join(res)
    
print(ans) 
