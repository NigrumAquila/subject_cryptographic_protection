from math import sqrt 

def power( x, y, p):  
    res = 1
    x = x % p
    while (y > 0):  
        if (y & 1): 
            res = (res * x) % p  

        y = y >> 1 # y = y/2  
        x = (x * x) % p  
    return res  
  
def findPrimefactors(s, n): 
    while (n % 2 == 0) : 
        s.add(2)  
        n = n // 2
    for i in range(3, int(sqrt(n)), 2): 
        while (n % i == 0) : 
            s.add(i)  
            n = n // i  
    if (n > 2) : 
        s.add(n)  

def findPrimitive(n):
    s = set()  
    phi = n - 1
    findPrimefactors(s, phi)  
    for r in range(2, phi + 1):  
        flag = False
        for it in s:  
            if (power(r, phi // it, n) == 1):    
                flag = True
                break
        if (flag == False): 
            return r  
    return -1