# https://en.wikipedia.org/wiki/Factorial_number_system

def solve(n):
    l = []
    i = 1
    while n != 0:
        rem = n%i 
        l.append(rem)
        n = n//i
        i += 1
    
    return l[::-1]

chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm']
t = int(input())
for t0 in range(t):
    n = int(input())
    n = n - 1
    l = solve(n)
    res = []
    i = 13 - len(l) - 1
    
    #for i in range(13-len(l)):
    #    res.append(chars[i])
    
    res = res + chars[:i+1]
    
    char = chars[i+1:]
    for e in l:
        res.append(char[e])
        char.remove(char[e]) 
    ans = ''.join(res)
    
    print(ans) 
    
