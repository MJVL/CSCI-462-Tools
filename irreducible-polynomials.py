from itertools import product
import argparse


def is_irreducible(polynomial, degree, zn):
    if (polynomial == tuple([0] * (degree - 1) + [1] + [0]) or polynomial == tuple([0] * (degree - 1) + [1] * 2)): return True
    if (not polynomial[-1]): return False
    return sum(polynomial) % zn != 0;


def polynomial_to_string(polynomial):
    out = ""
    for i, coefficent in enumerate(polynomial):
        if coefficent != 0:
            if coefficent > 1:
                out += "%dx" % coefficent
            else:
                out += "x" if (i < len(polynomial) - 1) else "1"
            if (len(polynomial) - i - 1 > 1): out += "^%d" % (len(polynomial) - i - 1)
            out += " "
    return out[:-1].replace(" ", " + ")        


def main():
    parser = argparse.ArgumentParser(description="Finds all irreducible (and optionally reducible) polynomials up to a specified degree in Z2.")
    parser.add_argument("degree", help="degree to find irreducible polynomials up to", type=int)
    parser.add_argument("-r", "--reducible", help="include reducible polynomials", action="store_true")
    args = parser.parse_args()

    zn = 2 # locked until fixed for larger fields
    combinations = list(product(range(zn), repeat=args.degree + 1))[2:]
    irreducibles, reducibles = [], []

    for polynomial in combinations:
        if (is_irreducible(polynomial, args.degree, zn)):
            irreducibles.append(polynomial_to_string(polynomial))
        else:
            reducibles.append(polynomial_to_string(polynomial))

    print("Polynomials up to Degree %d in Z%d" % (args.degree, zn))
    if args.reducible: print("{0}\nReducible Polynomials\n{0}\n{1}".format("-" * 21, '\n'.join(reducibles)))
    print("{0}\nIrreducible Polynomials\n{0}\n{1}".format("-" * 23, '\n'.join(irreducibles)))


if __name__ == "__main__":
    main()
