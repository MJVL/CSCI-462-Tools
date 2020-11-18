# private key
d = 67
print(f"Private Key (d) = {d}")

# public key
p = 97
a = 23
b = 15
print(f"Public Key (p, a, b) = ({p}, {a}, {b})")

# message and ephemeral key
x = 17
ke = 49
print(f"Message (x) = {x}")
print(f"Ephemeral Key (ke) = {ke}")

MMI = lambda A, n, s=1, t=0,N =0: (n < 2 and t % N or MMI(n, A % n, t, s - A // n * t, N or n), -1)[n < 1]

r = pow(a, ke, p - 1)
s = ((x - d * r) * MMI(ke, p - 1)) % (p - 1)
print(f"Elgamal Signature (x, (r, s)) = ({x}, ({r}, {s}))")

t = (b ** r * r ** s) % p
a_x = pow(a, x, p)
print(f"Verification (t, a_x) = ({t}, {a_x})")

print("Valid Signature" if t == a_x else "Invalid Signature")