import sympy, base64

def rsa(msg, mode='enc', keys=None):
    if keys is None:
        p, q = sympy.randprime(1, 10000), sympy.randprime(1, 10000)
        n, phi = p * q, (p - 1) * (q - 1)0
        e, d = 3, pow(3, -1, phi)
        keys = ((e, n), (d, n))

    (e, n), (d, n) = keys

    if mode == 'enc':
        return ".".join(base64.b64encode(pow(ord(c), e, n).to_bytes(8, 'big')).decode() for c in msg)
    else:
        return "".join(chr(pow(int.from_bytes(base64.b64decode(b), 'big'), d, n)) for b in msg.split("."))

message = "HELLO"

pub, priv = None, None
encrypted = rsa(message, 'enc', (pub, priv))
pub, priv = rsa(None, keys=(pub, priv))[0], rsa(None, keys=(pub, priv))[1]
decrypted = rsa(encrypted, 'dec', (pub, priv))

print(f"Message: {message}")
print(f"Encrypted: {encrypted}")
print(f"Decrypted: {decrypted}")
