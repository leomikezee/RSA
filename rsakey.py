class PublicKey:
    def __init__(self, e, n):
        self.e = e
        self.n = n

class PrivateKey:
    def __init__(self, d, n, p, q):
        self.d = d
        self.n = n
        self.p = p
        self.q = q

class RSAKey:
    def __init__(self, public, private):
        self.public = public
        self.private = private
