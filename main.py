import random        

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
