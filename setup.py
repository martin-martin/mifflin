import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="mifflin",
    version="0.1.1",
    description="...",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/martin-martin/mifflin",
    author="datamat.in",
    author_email="",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["mifflin"],
    include_package_data=True,
    install_requires=[],
    entry_points={
        "console_scripts": [
            "mifflin=mifflin.__main__:main",
        ]
    },
)
