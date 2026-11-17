import sympy

a, b = 1, 1e7
e = 3

euler = lambda p, q: ( p - 1 ) * ( q - 1 )

def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        gcd, x, y = extended_gcd(b % a, a)
        return gcd, y - (b // a) * x, x

p = sympy.randprime(a, b)
q = sympy.randprime(a, b)
phi = euler(p, q)
n = p * q
gcd, x, y = extended_gcd(e, phi)
d = x % phi
k = -y

m = 111111
print(f"Message: {m}")
print(f"Encrypt message:", c := pow(m, e, n))
print(f"Decrypt message: {pow(c, d, n)}")
