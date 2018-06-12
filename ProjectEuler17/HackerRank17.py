d = {0: "Zero",
     1: "One",
     2: "Two",
     3: "Three",
     4: "Four",
     5: "Five",
     6: "Six",
     7: "Seven",
     8: "Eight",
     9: "Nine",
     10: "Ten",
     11: "Eleven",
     12: "Twelve",
     13: "Thirteen",
     14: "Fourteen",
     15: "Fifteen",
     16: "Sixteen",
     17: "Seventeen",
     18: "Eighteen",
     19: "Nineteen",
     20: "Twenty",
     30: "Thirty",
     40: "Forty",
     50: "Fifty",
     60: "Sixty",
     70: "Seventy",
     80: "Eighty",
     90: "Ninety",
     1000: "Thousand",
     1000000: "Million",
     1000000000: "Billion",
     1000000000000: "Trillion"
    }        

#print(d)

def noToWord(s):
    res = ""
    #if s == "0" or s == "00" or s == "000":
    #    return res
    if s[0]=="0" and s[1]=="0" and s[2]=="0":
        s=""
    elif s[0]=="0" and s[1]=="0":
        s=s[2:]
    elif s[0]=="0":
        s=s[1:] 
    
    
    if len(s)==1:
        d0 = int(s[0])
        res = d[d0]  
    elif len(s)==2:
        d0 = int(s[1])
        d1 = int(s[0])
        if int(s)>19:
            res = (d[d1*10] + " " + d[d0]) if d0!=0 else d[d1*10]
        else:
            res = d[int(s)]
            
    elif len(s)==3:
        d0 = int(s[2])
        d1 = int(s[1])
        d2 = int(s[0])
        if int(s[1:])>19:
            if d1!=0 and d0!=0:
                res = d[d2] + " " + "Hundred" + " " +d[d1*10] + " " + d[d0]
            #elif d1==0 and d0!=0:
            #    res = d[d2] + " " + "Hundred" + " " + d[d0]
            elif d1!=0 and d0==0:
                res = d[d2] + " " + "Hundred" + " " +d[d1*10]
            #elif d1==0 and d0==0:
            #    res = d[d2] + " " + "Hundred"
        else:
            if d1!=0 and d0!=0:
                res = d[d2] + " " + "Hundred" + " " +d[int(s[1:])] 
            elif d1==0 and d0!=0:
                res = d[d2] + " " + "Hundred" + " " +d[int(s[2:])] 
            elif d1!=0 and d0==0:
                res = d[d2] + " " + "Hundred" + " " +d[int(s[1:])]
            elif d1==0 and d0==0:
                res = d[d2] + " " + "Hundred"
            
            
    return res    
        

T = int(input())
for T0 in range(T):
    s = input() 
    
    if s=="0":
        print(d[0])
        continue
        
    l = []
    if len(s)%3 == 0:
        for i in range(len(s),0,-3):
            l.append(s[i-3:i])
        l = l[::-1]
    else:
        k = len(s)//3
        l.append(s[0:len(s)-k*3])
        for i in range(len(s)-k*3, len(s), 3):
            l.append(s[i:i+3]) 
    #print(l)
    res = ""
    c = len(l[0])
    for e in l:
        #print(noToWord(e))
        k = 10**(len(s) - c)
        c += 3
        t = d[k] if k>=1000 else ""
        #print(t)
        if noToWord(e) != "":
            res = (res + noToWord(e) + " " + t +" ")
        
    print(res)    
    
