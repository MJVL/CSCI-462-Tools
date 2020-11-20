import argparse


MMI = lambda A, n, s=1, t=0, N=0: (n < 2 and t % N or MMI(n, A % n, t, s - A // n * t, N or n), -1)[n < 1]


def main():
    parser = argparse.ArgumentParser(description="Walks through the Elgamal Digital Signature process and checks if the signature is valid.")
    parser.add_argument("p", help="prime p", type=int)
    parser.add_argument("q", help="divisor of p - 1", type=int)
    parser.add_argument("α", help="element with ord(α) = q", type=int)
    parser.add_argument("d", help="the private key with 0 < d < q", type=int)
    parser.add_argument("h(x)", help="the hash of the message x", type=int, metavar="h")
    parser.add_argument("kE", help="random ephemeral key with 0 < kE < q", type=int)
    parser.add_argument("-s", "--show_steps", help="show intermediate calculations and equations", action="store_true")
    args = parser.parse_args()

    p, q, a, d = args.p, args.q, args.α, args.d
    b = pow(a, d, p)
    if args.show_steps:
        print(f"Choose d = {d}, Choose p = {p}\nChoose q = {q}\nChoose α = {a}\n")
        print(f"β = α^d mod p:\n\t{b} = {a}^{d} mod {p}\n")
    print(f"Public Key (p, q, α, β) = ({p}, {q}, {a}, {b})\n")
    
    hx, ke = vars(args)["h(x)"], args.kE
    if args.show_steps:
        print(f"Compute h(x) = {hx}")
        print(f"Choose kE = {ke}")

    r = pow(a, ke, p) % q
    s = (hx + d * r) * MMI(ke, q) % q
    print(f"DSA Signature (h(x), (r, s)) = ({hx}, ({r}, {s}))")

    w = MMI(s, q)
    u1 = w * hx % q
    u2 = w * r % q
    print(f"w={w}, u1={u1}, u2={u2}")

    v = (a ** u1 * b ** u2 % p) % q
    ver = r % q
    print(f"Verification (v, r % q) = ({v}, {ver})")

    print("Valid Signature" if v == ver else "Invalid Signature")



if __name__ == "__main__":
    main()