from itertools import product


def is_irreducible(polynomial, degree, zn):
    if (polynomial == tuple([0] * (degree - 1) + [1] + [0]) or polynomial == tuple([0] * (degree - 1) + [1] * 2)): return True
    if (not polynomial[-1] or polynomial == tuple([0] * degree + [1])): return False
    return sum(polynomial) % zn != 0;


def polynomial_to_string(polynomial):
    out = ""
    for i, coefficent in enumerate(polynomial):
        if coefficent != 0:
            if coefficent > 1:
                out += "%dx"
            else:
                out += "x" if (i < len(polynomial) - 1) else "1"
            if (len(polynomial) - i - 1 > 1): out += "^%d" % (len(polynomial) - i - 1)
            out += " "
    return out[:-1].replace(" ", " + ")        


def main():
    degree = int(input("Enter degree: "))
    zn = int(input("Enter Zn: "))
    combinations = list(product(range(zn), repeat=degree + 1))[2:]
    print("All Possible Polynomials of Degree %d in Z%d" % (degree, zn))
    for polynomial in combinations:
        if (is_irreducible(polynomial, degree, zn)):
          print("Irreducible: " + polynomial_to_string(polynomial))


if __name__ == "__main__":
    main()