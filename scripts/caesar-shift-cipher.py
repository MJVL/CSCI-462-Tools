import argparse
from prettytable import PrettyTable


def main():
    parser = argparse.ArgumentParser(description="Implements basic ASCII encryption/decryption through a Ceasar cipher, as well as brute forcing.")
    parser.add_argument("text", help="the plaintext or ciphertext to encrypt or decrypt respectively", type=str)
    parser.add_argument("-k", "--key", help="the shift (if known, no value = brute force)", type=int)
    args = parser.parse_args()

    ascii_start = ord('A') if args.text.isupper() else ord('a')
    if not args.key:
        table = PrettyTable()
        table.field_names = ["Shift", "Text"]
        [table.add_row([i, ''.join(' ' if ord(c) == 32 else chr((ord(c) + i - ascii_start) % 26 + ascii_start) for c in args.text)]) for i in range(26)]
        print(table)
    else:
        print(f"Shifted: {''.join(' ' if ord(c) == 32 else chr((ord(c) + args.key - ascii_start) % 26 + ascii_start) for c in args.text)}")


if __name__ == "__main__":
    main()