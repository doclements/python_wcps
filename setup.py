#!/usr/bin/env python
"""python WCPS project"""
from setuptools import find_packages, setup

setup(name = 'pywcps',
    version = '0.1',
    description = "Python WCPS access module.",
    long_description = "A module for accessing data through the OGC standard WCPS.",
    platforms = ["Linux"],
    author="Oliver Clements",
    author_email="olcl@pml.ac.uk",
    url="git remote add origin https://github.com/doclements/python_wcps",
    license = "MIT",
    packages=find_packages()
    )
