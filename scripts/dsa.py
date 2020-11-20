# private key
d = 23
print(f"Private Key (d) = {d}")

# public key
p = 59
q = 29
a = 3
print(f"Public Key (p, q, a) = ({p}, {q}, {a})")

# computed public key
b = pow(a, d, p)
print(f"Computed Public Key (b) = {b}")

# hash
hx = 21
print(f"H(x) = {hx}")

# epehemeral key
ke = 8
print(f"Ephemeral Key (ke) = {ke}")

MMI = lambda A, n, s=1, t=0, N=0: (n < 2 and t % N or MMI(n, A % n, t, s - A // n * t, N or n), -1)[n < 1]

r = pow(a, ke, p) % q
s = (hx + d * r) * MMI(ke, q) % q
print(f"DSA Signature (h(x), (r, s)) = ({hx}, ({r}, {s}))")
print(MMI(ke, q))

w = MMI(s, q)
u1 = w * hx % q
u2 = w * r % q
print(f"w={w}, u1={u1}, u2={u2}")

v = (a ** u1 * b ** u2 % p) % q
ver = r % q
print(f"Verification (v, r % q) = ({v}, {ver})")

print("Valid Signature" if v == ver else "Invalid Signature")