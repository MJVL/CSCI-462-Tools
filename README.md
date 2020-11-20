# CSCI-462-Tools

Collection of miscellaneous scripts written to help for CSCI-462 - RIT's cryptography course.

Most of these scripts are built for convenience, not efficient run times/memory usage, hence the code style won't be pristine.

## Installation

```
pip3 install -r requirements.txt
```

## Script Glossary
- [square-and-multiply](#square-and-multiply)
  - [Usage](#usage)
  - [Examples](#examples)
- [elgamal-digital-signature](#elgamal-digital-signature)
  - [Usage](#usage-1)
  - [Examples](#examples-1)
- [irreducible-polynomials](#irreducible-polynomials)
  - [Usage](#usage-2)
  - [Example](#example)

## square-and-multiply

### Usage

```
usage: square-and-multiply.py [-h] [-s] base exponent modulus

Implementation of the square-and-multiply algorithm, a fast method of modular
exponentiation.

positional arguments:
  base              the base to convert to binary
  exponent          the exponent
  modulus           the modulus

optional arguments:
  -h, --help        show this help message and exit
  -s, --show-steps  show each step in the algorithm
```

### Examples

```
python3 .\square-and-multiply.py 3 197 101

3^197 mod 101 = 15
```

```
python3 .\square-and-multiply.py 2 79 101 -s
+-------------------------------------------------+
|            Work for 2^79 mod 101 = 42           |
+--------------+----------+-------------+---------+
| Binary Digit |   Work   |  Operation  | mod 101 |
+--------------+----------+-------------+---------+
|      1       |    2     |     N/A     |    2    |
|      0       |   2^2    |      SQ     |    4    |
|      0       |   4^2    |      SQ     |    16   |
|      1       | 16^2 * 2 | SQ and Mult |    7    |
|      1       | 7^2 * 2  | SQ and Mult |    98   |
|      1       | 98^2 * 2 | SQ and Mult |    18   |
|      1       | 18^2 * 2 | SQ and Mult |    42   |
+--------------+----------+-------------+---------+
```

## elgamal-digital-signature

### Usage

```
usage: elgamal-digital-signature.py [-h] [-s] d p α x kE

Walks through the Elgamal Digital Signature process and checks if the
signature is valid.

positional arguments:
  d                 the private key, a random integer d ∈ {2, 3, ..., p - 2}
  p                 large prime p
  α                 primitive root α
  x                 message
  kE                random ephemeral key kE ∈ {0, 1, 2,.., p − 2} such that
                    gcd(kE, p − 1) = 1

optional arguments:
  -h, --help        show this help message and exit
  -s, --show_steps  show intermediate calculations and equations
```

### Examples

```
python3 elgamal-digital-signature.py 67 97 23 85 77

Public Key (p, α, β) = (97, 23, 15)

Elgamal Signature (x, (r, s)) = (85, (84, 29))

Verification (t, α^x) = (83, 83)

Valid Signature
```

```
python3 elgamal-digital-signature.py 12 29 2 26 5 -s

Choose d = 12
Choose p = 29
Choose α = 2

β = α^d mod p:
	7 = 2^12 mod 29

Public Key (p, α, β) = (29, 2, 7)

Choose x = 26
Choose kE = 5

r = α^kE mod p - 1:
	3 = 2^5 mod 28

s = (x - dr)kE^-1 mod p - 1:
	26 = (26 - (12 * 3)) * 17 mod 28

Elgamal Signature (x, (r, s)) = (26, (3, 26))

t = β^r * r^s mod p:
	22 = 7^3 * 3^26 mod 29

α^x mod p:
	22 = 2^26 mod 29

Verification (t, α^x) = (22, 22)

Valid Signature
```

## irreducible-polynomials

### Usage

```
usage: irreducible-polynomials.py [-h] [-r] degree

Finds all irreducible (and optionally reducible) polynomials up to a specified
degree in Z2.

positional arguments:
  degree           degree to find irreducible polynomials up to

optional arguments:
  -h, --help       show this help message and exit
  -r, --reducible  include reducible polynomials
```

### Example

```
python3 .\irreducible-polynomials.py 2 -r

Polynomials up to Degree 2 in Z2
---------------------
Reducible Polynomials
---------------------
x^2
x^2 + 1
x^2 + x
-----------------------
Irreducible Polynomials
-----------------------
x
x + 1
x^2 + x + 1
```