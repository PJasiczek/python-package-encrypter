# python-package-encrypter
> A small Python library implementing a grid/square text cipher (Playfair-style), packaged and versioned as an installable pip package.

## What it does
`encryptText(text, square)` encrypts text using a grid cipher: the letters of a keyword are arranged into a square, and each pair of characters in the input is substituted based on their positions in that grid — the classic Playfair cipher approach.

## Package structure
This repo is set up as a proper installable package rather than a loose script:
* `myPackage/` – the library code (`somePython.encryptText`)
* `setup.py` – package metadata (MIT license, `numpy` dependency)
* `tests/test.py` – a unit test for `encryptText`
* `dist/` – built distributions for versions 0.1–0.3

## Install & use
```
pip install -r requirements.txt
pip install .
```
```python
from myPackage import somePython
somePython.encryptText("abcdefghijklmnoprst", "adaa")
```

## Status
**Archived** — not actively maintained.

Written in 2019 to practice packaging a Python library — `setup.py`, versioning, and a unit test — around a simple cipher algorithm.
