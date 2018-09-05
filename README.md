# setuptools-demo
A sample repository to test setuptools https://github.com/pypa/setuptools

## Version 0.1
This version uses a very basic setup.py file to generate the distribution.

```
from setuptools import setup, find_packages
setup(
    name="setuptools_demo",
    version="0.1",
    packages=find_packages(),
)
```
