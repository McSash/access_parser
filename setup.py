import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="access_parser_c",
    version="0.0.5",
    author="Sascha Saumer",
    author_email="s.saumer@hotmail.de",
    description="Access database (*.mdb, *.accdb) parser",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/McSash/access_parser_c",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
          'construct',
          'tabulate',
      ],
)
