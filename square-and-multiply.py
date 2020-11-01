import argparse


def square_and_multiply(base, power, modulus):
    result = base
    iter_binary = iter('{0:b}'.format(power))
    next(iter_binary)
    for i in iter_binary:
        result **= 2
        if (i == '1'):
            result *= base
        result %= modulus
    return result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("base", help="the base to convert to binary", type=int)
    parser.add_argument("exponent", help="the exponent", type=int)
    parser.add_argument("modulus", help="the modulus", type=int)
    args = parser.parse_args()

    print("{0}^{1} mod {2} = {3}".format(args.base, args.exponent, args.modulus, square_and_multiply(args.base, args.exponent, args.modulus)))


if __name__ == "__main__":
    main()