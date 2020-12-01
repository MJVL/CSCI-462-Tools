import argparse


def main():
    parser = argparse.ArgumentParser(description="Walks through the Diffie-Hellman Key Exchange setup process.")
    parser.add_argument("p", help="large prime p", type=int)
    parser.add_argument("α", help="integer α ∈ {2, 3, ..., p - 2", type=int)
    parser.add_argument("sec_a", help="secret integer exponent a", type=int)
    parser.add_argument("sec_b", help="secret integer exponent b", type=int)
    parser.add_argument("-s", "--show_steps", help="show intermediate calculations and equations", action="store_true")
    args = parser.parse_args()

    p, a, sec_a, sec_b = args.p, args.α, args.sec_a, args.sec_b
    print(f"Domain Parameters (p, α) = ({p}, {a})\n")
    print(f"Private Keys (a, b) = ({sec_a}, {sec_b})\n")

    A = pow(a, sec_a, p)
    B = pow(a, sec_b, p)
    if args.show_steps:
        print(f"A = α^a mod p\n\t{A} = {a}^{sec_a} mod {p}\n")
        print(f"B = α^b mod p\n\t{B} = {a}^{sec_b} mod {p}\n")
    print(f"Public Keys (A, B) = ({A}, {B})\n")

    session_A = pow(A, sec_b, p)
    session_B = pow(B, sec_a, p)
    session_AB = pow(a, sec_a * sec_b, p)
    if args.show_steps:
        print(f"AB = A^b mod p\n\t{session_A} = {A}^{sec_b} mod {p}\n")
        print(f"AB = B^a mod p\n\t{session_B} = {B}^{sec_a} mod {p}\n")
        print(f"AB = α^ab mod p\n\t{session_AB} = {a}^({sec_a} * {sec_b}) mod {p}\n")
    assert session_A == session_B == session_AB, "The joint secret should be the same across calculations."
    print(f"Session Key (AB) = {session_AB}")


if __name__ == "__main__":
    main()