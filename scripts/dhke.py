def main():
    p = int(input("large prime p"))
    a = int(input("integer α ∈ {2, 3, ..., p - 2}"))
    print(f"Domain Parameters (p, α) = ({p}, {a})")
    
    sec_a = int(input("secret integer a"))
    sec_b = int(input("secret integer b"))
    print(f"Private Keys (a, b) = ({sec_a}, {sec_b})")

    A = pow(a, sec_a, p)
    B = pow(a, sec_b, p)
    print(f"A = α^a mod p\n\t{A} = {a}^{sec_a} mod {p}")
    print(f"B = α^b mod p\n\t{B} = {a}^{sec_b} mod {p}")
    print(f"Public Keys (A, B) = ({A}, {B})")

    session_A = pow(A, sec_b, p)
    session_B = pow(B, sec_a, p)
    session_AB = pow(a, sec_a * sec_b, p)
    print(f"AB = A^b mod p\n\t{session_A} = {A}^{sec_b} mod {p}")
    print(f"AB = B^a mod p\n\t{session_B} = {B}^{sec_a} mod {p}")
    print(f"AB = α^ab mod p\n\t{session_AB} = {a}^({sec_a} * {sec_b}) mod {p}")

    assert session_A == session_B == session_AB, "The joint secret should be the same across calculations."
    print(f"Session Key (AB) = {session_AB}")


if __name__ == "__main__":
    main()