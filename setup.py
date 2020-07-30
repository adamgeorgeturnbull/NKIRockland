import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="nkiRockland",
    version="0.0.1",
    author="Adam Turnbull",
    author_email="adamgturnbull92@gmail.com",
    description="Package for analysing NKI Rockland sample",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/adamgeorgeturnbull/NKIRockland",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)