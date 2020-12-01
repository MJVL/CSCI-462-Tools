# CSCI-462-Tools

Collection of miscellaneous scripts written to help for CSCI-462 - RIT's cryptography course.

Most of these scripts are built for convenience, not efficient run times/memory usage, hence the code style won't be pristine.

## Installation

```
sudo python3 setup.py install
```

## Script Glossary
- [square-and-multiply](#square-and-multiply)
  - [Usage](#usage)
  - [Examples](#examples)
- [dhke](#dhke)
    - [Usage](#usage-1)
  - [Examples](#examples-1) 
- [elgamal-digital-signature](#elgamal-digital-signature)
  - [Usage](#usage-2)
  - [Examples](#examples-2)
- [dsa](#dsa)
  - [Usage](#usage-3)
  - [Examples](#examples-3)
- [irreducible-polynomials](#irreducible-polynomials)
  - [Usage](#usage-4)
  - [Example](#example)

## square-and-multiply

### Usage

```
usage: square-and-multiply [-h] [-s] base exponent modulus

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
square-and-multiply 3 197 101

3^197 mod 101 = 15
```

```
square-and-multiply 2 79 101 -s

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

## dhke

### Usage

```
usage: dhke [-h] [-s] p α sec_a sec_b

Walks through the Diffie-Hellman Key Exchange setup process.

positional arguments:
  p                 large prime p
  α                 integer α ∈ {2, 3, ..., p - 2}
  sec_a             secret integer exponent a
  sec_b             secret integer exponent b

optional arguments:
  -h, --help        show this help message and exit
  -s, --show_steps  show intermediate calculations and equations
```

### Examples

```
dhke 306 5 7 17 

Domain Parameters (p, α) = (306, 5)

Private Keys (a, b) = (7, 17)

Public Keys (A, B) = (95, 209)

Session Key (AB) = 299
```

```
dhke 29 2 5 12 -s

Domain Parameters (p, α) = (29, 2)

Private Keys (a, b) = (5, 12)

A = α^a mod p
	3 = 2^5 mod 29

B = α^b mod p
	7 = 2^12 mod 29

Public Keys (A, B) = (3, 7)

AB = A^b mod p
	16 = 3^12 mod 29

AB = B^a mod p
	16 = 7^5 mod 29

AB = α^ab mod p
	16 = 2^(5 * 12) mod 29

Session Key (AB) = 16
```

## elgamal-digital-signature

### Usage

```
usage: elgamal-digital-signature [-h] [-s] d p α x kE

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
elgamal-digital-signature 67 97 23 85 77

Public Key (p, α, β) = (97, 23, 15)

Elgamal Signature (x, (r, s)) = (85, (84, 29))

Verification (t, α^x) = (83, 83)

Valid Signature
```

```
elgamal-digital-signature 12 29 2 26 5 -s

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

## dsa

### Usage

```
usage: dsa [-h] [-s] p q α d hx kE

Walks through the Digital Signature Algorithm process and checks if the
signature is valid.

positional arguments:
  p                 prime p
  q                 divisor of p - 1
  α                 element with ord(α) = q
  d                 the private key with 0 < d < q
  h(x)              the hash of the message x
  kE                random ephemeral key with 0 < kE < q

optional arguments:
  -h, --help        show this help message and exit
  -s, --show_steps  show intermediate calculations and equations
```

### Examples

```
dsa 59 29 3 7 17 25

Public Key (p, q, α, β) = (59, 29, 3, 4)

DSA Signature (h(x), (r, s)) = (17, (22, 8))

Verification (v, r % q) = (22, 22)

Valid Signature
```

```
dsa 59 29 3 7 26 10 -s

Choose d = 7
Choose p = 59
Choose q = 29
Choose α = 3

β = α^d mod p:
	4 = 3^7 mod 59

Public Key (p, q, α, β) = (59, 29, 3, 4)

Compute h(x) = 26
Choose kE = 10

r = (α^kE mod p) mod q
	20 = (3^10 mod 59) mod 29

s = (h(x) + dr)kE^-1 mod q
	5 = (26 - (7 * 20)) * 3 mod 29

DSA Signature (h(x), (r, s)) = (26, (20, 5))

w = s^-1 mod q
	6 = 5^-1 mod 29

u1 = w * h(x) mod q
	11 = 6 * 26 mod 29

u2 = w * r mod q
	4 = 6 * 20 mod 29

v = (α^u1 * β^u2 mod p) mod q
	20 = (3^11 * 4^4 mod 59) mod 29

Verification (v, r % q) = (20, 20)

Valid Signature
```

## irreducible-polynomials

### Usage

```
usage: irreducible-polynomials [-h] [-r] degree

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
irreducible-polynomials 2 -r

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