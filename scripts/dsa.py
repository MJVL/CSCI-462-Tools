import argparse


MMI = lambda A, n, s=1, t=0, N=0: (n < 2 and t % N or MMI(n, A % n, t, s - A // n * t, N or n), -1)[n < 1]


def generate_signature(p, q, a, d, hx, ke, show_steps):
    r = pow(a, ke, p) % q
    s = (hx + d * r) * MMI(ke, q) % q
    if show_steps:
        print(f"\nr = (α^kE mod p) mod q\n\t{r} = ({a}^{ke} mod {p}) mod {q}")
        print(f"\ns = (h(x) + dr)kE^-1 mod q\n\t{s} = ({hx} - ({d} * {r})) * {MMI(ke, q)} mod {q}\n")
    return r, s


def verify_signature(p, q, a, b, hx, r, s, show_steps):
    w = MMI(s, q)
    u1 = w * hx % q
    u2 = w * r % q
    v = (a ** u1 * b ** u2 % p) % q
    ver = r % q
    if show_steps:
        print(f"\nw = s^-1 mod q\n\t{w} = {s}^-1 mod {q}")
        print(f"\nu1 = w * h(x) mod q\n\t{u1} = {w} * {hx} mod {q}")
        print(f"\nu2 = w * r mod q\n\t{u2} = {w} * {r} mod {q}")
        print(f"\nv = (α^u1 * β^u2 mod p) mod q\n\t{v} = ({a}^{u1} * {b}^{u2} mod {p}) mod {q}")
    print(f"\nVerification (v, r % q) = ({v}, {ver})\n")
    return v == ver


def main():
    parser = argparse.ArgumentParser(description="Walks through the Digital Signature Algorithm process and checks if the signature is valid.")
    parser.add_argument("p", help="prime p", type=int)
    parser.add_argument("q", help="divisor of p - 1", type=int)
    parser.add_argument("α", help="element with ord(α) = q", type=int)
    parser.add_argument("d", help="the private key with 0 < d < q", type=int)
    parser.add_argument("h(x)", help="the hash of the message x", type=int)
    parser.add_argument("kE", help="random ephemeral key with 0 < kE < q", type=int)
    parser.add_argument("-s", "--show_steps", help="show intermediate calculations and equations", action="store_true")
    args = parser.parse_args()

    p, q, a, d = args.p, args.q, args.α, args.d
    b = pow(a, d, p)
    if args.show_steps:
        print(f"Choose d = {d}\nChoose p = {p}\nChoose q = {q}\nChoose α = {a}\n")
        print(f"β = α^d mod p:\n\t{b} = {a}^{d} mod {p}\n")
    print(f"Private Key d = {d}\n")
    print(f"Public Key (p, q, α, β) = ({p}, {q}, {a}, {b})\n")
    
    hx, ke = vars(args)["h(x)"], args.kE
    if args.show_steps:
        print(f"Compute h(x) = {hx}")
        print(f"Choose kE = {ke}")

    r, s = generate_signature(p, q, a, d, hx, ke, args.show_steps)
    print(f"DSA Signature (h(x), (r, s)) = ({hx}, ({r}, {s}))")

    print("Valid Signature" if verify_signature(p, q, a, b, hx, r, s, args.show_steps) else "Invalid Signature")


if __name__ == "__main__":
    main()