from setuptools import setup, find_packages


setup(
    name="CSCI-462-Tools",
    author="Michael Van Leeuwen",
    url="https://github.com/MJVL/CSCI-462-Tools",
    long_description=open("README.md").read(),
    packages=find_packages(),
    install_requires = [
        "prettytable"
    ],
    entry_points = {
        "console_scripts": [
            "square-and-multiply=scripts.square_and_multiply:main",
            "elgamal-digital-signature=scripts.elgamal_digital_signature:main",
            "dsa=scripts.dsa:main",
            "irreducible-polynomials=scripts.irreducible_polynomials:main"
        ]
    }
)