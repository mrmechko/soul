from setuptools import setup, find_packages
from setuptools.command.install import install as _install

with open("README.MD", "r") as fh:
    long_description = fh.read()

if __name__ == '__main__':
    setup(
        name="thesoulshell",
        version="0.0.3",
        author="Rik Bose",
        author_email="rbose@cs.rochester.edu",
        description="add a little soul to your python",
        long_description=long_description,
        long_description_content_type="text/markdown",
        url="https://github.com/mrmechko/soul",
        packages=find_packages(exclude=["test"]),
        classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)",
            "Operating System :: OS Independent",
        ],
        install_requires=[],
    )
