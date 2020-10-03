# CSCI-462-Tools

Collection of miscellaneous scripts written to help for CSCI-462 - RIT's cryptography course.

Most of these scripts are built for convenience, not efficient run times/memory usage, hence the code style won't be pristine.

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