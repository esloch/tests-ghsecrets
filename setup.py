#!/usr/bin/env python

from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()


def read(filename):
    return [req.strip() for req in open(filename).readlines()]


setup(
    name="Testworkflow",
    version="0.1.1",
    author="esloch",
    author_email="es.loch@gmail.com",
    description="Testando os secrets",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/esloch/tests-ghsecrets.git",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GPL V3 License",
        "Operating System :: Linux",
    ],
    python_requires='>=3.7',
    install_requires=read("requirements.txt"),
)
