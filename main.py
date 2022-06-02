import random
'''
def compuesto(a,n,t,u):
    x = []
    x[0] = (a**u) %n
    if x[0] == 1 or x[0] ==  n-1:
        return False
    
    for i in range(1,t+1):
        x[i] = x[i-1] % n
        if x[i] == n-1:
            return False
    
    return True

def rep( a,  s,  num):
    for i in range (1,s+1):
        if a == num[i]:
            return True
    return False

def miller(n,s):
    t = 0
    u = n-1
    while u %2 == 0:
        u = u/2
        t+= 1
    
    numrand=[]

    for i in range (1,s+1):
        
        while rep(n,numrand,s) :
            a = random.randint(2, n-1) 
            numrand.append(a)

        if compuesto(a,n,t,u):
            return False

    return True
     

print('NUMEROS PRIMOS DE 3 CIFRAS: ')
for i in range(100,1000):
    a = miller(i,5)

    if a:
        print( a + ' ')
'''
        

def EXPMOD(x, y, p):
    res = 1
    x = x % p
    while (y > 0):
        if (y & 1):
            res = (res * x) % p
        y = y>>1
        x = (x * x) % p

    return res

def MILLER_RABIN(d, n):
    a = 2 + random.randint(1, n - 4)
    x = EXPMOD(a, d, n)

    if (x == 1 or x == n - 1):
        return True
    while (d != n - 1):
        x = (x * x) % n 
        d *= 2

        if (x == 1):
            return False
        if (x == n - 1):
            return True

    # Return compuesto
    return False


def esPrimo( n, s):

    if (n <= 1 or n == 4):
        return False
    if (n <= 3):
        return True
    d = n - 1
    while (d % 2 == 0):
        d //= 2
    for i in range(s):
        if (MILLER_RABIN(d, n) == False):
            return False

    return True

s = 5

print("Números primos de 3 cifras: ")
for n in range(100,1000):
    if (esPrimo(n, s)):
        print(n, end=', ')

print()
print("Números primos de 4 cifras: ")
for n in range(1000,10000):
    if (esPrimo(n, s)):
        print(n, end=', ')

print()
print("Números primos de 5 cifras: ")
for n in range(10000,100000):
    if (esPrimo(n, s)):
        print(n, end=', ')