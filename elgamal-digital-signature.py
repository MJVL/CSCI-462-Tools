import argparse
from math import gcd


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("private_key", help="random integer d ∈ {2, 3, ..., p - 2}", type=int)
    parser.add_argument("p", help="large prime p", type=int)
    parser.add_argument("α", help="primitive root α", type=int)
    parser.add_argument("x", help="message", type=int)
    parser.add_argument("kE", help="random ephemeral key kE ∈ {0,1,2,..., p − 2} such that gcd(kE, p − 1) = 1", type=int)
    parser.add_argument("-v", "--verbose", help="show intermediate calculations", action="store_true")
    args = parser.parse_args()

    d = args.private_key
    print(f"Private Key (d) = {d}")

    p = args.p
    a = args.α
    b = pow(a, d, p)
    #print(f"β = α^d mod p")
    print(f"Public Key (p, α, β) = ({p}, {a}, {b})")

    # message and ephemeral key
    x = args.x
    ke = args.kE
    print(f"Message (x) = {x}")
    print(f"Ephemeral Key (kE) = {ke}")

    MMI = lambda A, n, s=1, t=0, N=0: (n < 2 and t % N or MMI(n, A % n, t, s - A // n * t, N or n), -1)[n < 1]

    r = pow(a, ke, p - 1)
    s = ((x - d * r) * MMI(ke, p - 1)) % (p - 1)
    print(f"Elgamal Signature (x, (r, s)) = ({x}, ({r}, {s}))")

    t = (b ** r * r ** s) % p
    a_x = pow(a, x, p)
    print(f"Verification (t, a_x) = ({t}, {a_x})")

    print("Valid Signature" if t == a_x else "Invalid Signature")


if __name__ == "__main__":
    main()