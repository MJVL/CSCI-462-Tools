# CSCI-462-Tools

Collection of miscellaneous scripts written to help for CSCI-462 - RIT's cryptography course.

Most of these scripts are built for convenience, not efficient run times/memory usage, hence the code style won't be pristine.

## square-and-multiply

### Usage

```
usage: square-and-multiply.py [-h] [-s] base exponent modulus

positional arguments:
  base              the base to convert to binary
  exponent          the exponent
  modulus           the modulus

optional arguments:
  -h, --help        show this help message and exit
  -s, --show-steps  show each step in the algorithm
```

### Example

```
python3 .\square-and-multiply.py 3 197 101

3^197 mod 101 = 15

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

## irreducible-polynomials

### Usage

```
usage: irreducible-polynomials.py [-h] [-r] degree

positional arguments:
  degree           Degree to find irreducible polynomials up to

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