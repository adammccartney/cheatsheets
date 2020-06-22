#!/usr/bin/env python
import setuptools

install_requires = ["abjad"]

keywords = [
    "abjad",
    "music composition",
    "music notation",
    "formalized score control",
    "lilypond",
]

if __name__ == "__main__":
    setuptools.setup(
        name="mccartney",
        version = "0.0",
        author="Adam McCartney",
        author_email="adam@mur.at",
        install_requires=install_requires,
        keywords=", ".join(keywords),
        packages=setuptools.find_packages(),
        platforms="Any",
        url="https://github.com/adammccartney/mccartney",
)
