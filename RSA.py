from converter import int2str, str2int
from rsamath import randPrime, coPrime, eea
from rsakey import RSAKey, PublicKey, PrivateKey

def gen(l1, l2):
    p = randPrime(l1 // 2)
    q = randPrime(l1 // 2)
    while (p == q):
        q = randPrime(l1 // 2)
    n = p * q
    temp = (p - 1) * (q - 1)
    e = randPrime(l2)
    while (not coPrime(e, temp)):
        e = randPrime(l2)
    _, d, _ = eea(e, temp)
    while (d < 0):
        d = d + temp
    public = PublicKey(e, n)
    private = PrivateKey(d, n, p, q)
    key = RSAKey(public, private)
    return key

def en():
    m = str2int(input("Please Enter your message:"))
    e = int(input("Please Enter your e:"))
    n = int(input("Please Enter your n:"))
    return pow(m, e, n)

def de():
    m = int(input("Please Enter your message:"))
    d = int(input("Please Enter your d:"))
    n = int(input("Please Enter your n:"))
    return pow(m, d, n)

if __name__ == '__main__':
    f = input("Generate Key => 1\nEncryption => 2\nDecryption => 3\n")
    while (f in ['1', '2', '3']):
        if f == "1":
            l = int(input("Please Enter the length of n: \n"))
            d = int(input("Please Enter the length of e: \n"))
            key = gen(l ,d)
            print ("PublicKey: (%d, %d)" % (key.public.e, key.public.n))
            print ("PrivateKey: (%d, %d)" % (key.private.d, key.private.n))
        elif f == "2":
            print("Encrypted Messages:\n", en())
        elif f == "3":
            print("Decrypted Messages:\n", int2str(str(de())))
        f = input("Generate Key => 1\nEncryption => 2\nDecryption => 3\n")
