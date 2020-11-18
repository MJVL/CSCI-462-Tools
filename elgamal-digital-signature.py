import argparse
from math import gcd


MMI = lambda A, n, s=1, t=0, N=0: (n < 2 and t % N or MMI(n, A % n, t, s - A // n * t, N or n), -1)[n < 1]


def generate_signature(d, p, a, x, ke, show_steps):
    r = pow(a, ke, p)
    s = ((x - d * r) * MMI(ke, p - 1)) % (p - 1)
    if show_steps:
        print(f"\nr = α^kE mod p - 1:\n\t{r} = {a}^{ke} mod {p - 1}")
        print(f"\ns = (x - dr)kE^-1 mod p - 1:\n\t{s} = ({x} - ({d} * {r})) * {MMI(ke, p - 1)} mod {p - 1}\n")
    return r, s


def verify_signature(r, s, p, a, b, x, show_steps):
    t = (b ** r * r ** s) % p
    ax = pow(a, x, p)
    if show_steps:
        print(f"\nt = β^r * r^s mod p:\n\t{t} = {b}^{r} * {r}^{s} mod {p}")
        print(f"\nα^x mod p:\n\t{ax} = {a}^{x} mod {p}")
    print(f"\nVerification (t, α^x) = ({t}, {ax})\n")
    return t == ax

def main():
    parser = argparse.ArgumentParser(description="Walks through the Elgamal Digital Signature process and checks if the signature is valid.")
    parser.add_argument("d", help="the private key, a random integer d ∈ {2, 3, ..., p - 2}", type=int)
    parser.add_argument("p", help="large prime p", type=int)
    parser.add_argument("α", help="primitive root α", type=int)
    parser.add_argument("x", help="message", type=int)
    parser.add_argument("kE", help="random ephemeral key kE ∈ {0, 1, 2,.., p − 2} such that gcd(kE, p − 1) = 1", type=int)
    parser.add_argument("-s", "--show_steps", help="show intermediate calculations", action="store_true")
    args = parser.parse_args()

    d, a, p = args.d, args.α, args.p
    b = pow(a, d, p)
    if args.show_steps:
        print(f"Choose d = {d}\nChoose p = {p}\nChoose α = {a}\n")
        print(f"β = α^d mod p:\n\t{b} = {a}^{d} mod {p}\n")
    print(f"Public Key (p, α, β) = ({p}, {a}, {b})\n")

    x, ke = args.x, args.kE
    if args.show_steps:
        print(f"Choose x = {x}")
        print(f"Choose kE = {ke}")

    r, s = generate_signature(d, p, a, x, ke, args.show_steps)
    print(f"Elgamal Signature (x, (r, s)) = ({x}, ({r}, {s}))")
    print("Valid Signature" if verify_signature(r, s, p, a, b, x, args.show_steps) else "Invalid Signature")


if __name__ == "__main__":
    main()