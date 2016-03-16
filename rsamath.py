from random import seed, randint
from fractions import gcd
from time import time

# Constant K for primality test accuracy
K = 20

# Use current time in milliseconds as random seed
seed(a = int(round(time()) * 1000))

# Determine if a and b are coprime
def coPrime(a, b):
    return gcd(a, b) == 1

# Create a int with l digits
def randInt(l):
    return randint(10**(l - 1), 10**l-1)

# Extended Euclid Algorithm
# https://en.wikibooks.org/wiki/Algorithm_Implementation/Mathematics/Extended_Euclidean_algorithm
def eea(a, b):
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q, r = b//a, b%a
        m, n = x-u*q, y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
    gcd = b
    return gcd, x, y

# Get next prime number of p
def nextPrime(p):
    p = abs(p)
    if (p == 1):
        return 2
    if (p % 2 == 0):
        if isPrime(p + 1, K):
            return p + 1
        else:
            return nextPrime(p + 1)
    elif isPrime(p + 2, K):
        return p + 2
    return nextPrime(p + 2)

# Use Miller-Rabin Primality Test to determine the primality of p
# K signifies the accuracy of the test
# https://www.topcoder.com/community/data-science/data-science-tutorials/primality-testing-non-deterministic-algorithms/
def isPrime(p, k):
    if (p < 2):
        return False
    if (p != 2 and p % 2 == 0):
        return False
    s = p - 1
    while (s % 2 == 0):
        s = s // 2
    for i in range(0, k):
        a = randint(2, p - 1)%(p - 1) + 1
        temp = s
        mod = pow(a, temp, p)
        while (temp != p - 1 and mod !=1 and mod != p-1):
            mod = (mod * mod) % p
            temp = temp * 2
        if (mod != p - 1 and temp % 2 == 0):
            return False
    return True

# Get a random prime number with l digits
def randPrime(l):
    bound = 10**l - 1
    p = randInt(l)
    if isPrime(p, K):
        return p
    else:
        p = nextPrime(p)
        if (p <= bound):
            return p
        else:
            return randPrime(l)
