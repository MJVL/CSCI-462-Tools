from prettytable import PrettyTable
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


def square_and_multiply_table(base, power, modulus):
    table = PrettyTable()
    table.title = "Work for {0}^{1} mod {2} = {3}".format(base, power, modulus, square_and_multiply(base, power, modulus))
    table.field_names = ["Binary Digit", "Work", "Operation", "mod {0}".format(modulus)]
    iter_binary = iter('{0:b}'.format(power))
    table.add_row(["1", base, "N/A", base])
    next(iter_binary)
    result = base
    for i in iter_binary:
        old_result = result
        result = result ** 2 * (1 if i == '0' else base) % modulus
        table.add_row([
            i, 
            "{0}^2{1}".format(old_result, "" if i == '0' else " * {0}".format(base)), 
            "SQ{0}".format("" if i == '0' else " and Mult"), 
            result
        ])
    return table


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("base", help="the base to convert to binary", type=int)
    parser.add_argument("exponent", help="the exponent", type=int)
    parser.add_argument("modulus", help="the modulus", type=int)
    parser.add_argument("-s", "--show-steps", help="show each step in the algorithm", action="store_true")
    args = parser.parse_args()

    if not args.show_steps:
        print("{0}^{1} mod {2} = {3}".format(args.base, args.exponent, args.modulus, square_and_multiply(args.base, args.exponent, args.modulus)))
    else:
        print(square_and_multiply_table(args.base, args.exponent, args.modulus))


if __name__ == "__main__":
    main()
