# setuptools-demo
A sample repository to test setuptools https://github.com/pypa/setuptools

Build the distribution using command
```
python setup.py sdist
```

Should be able to install this module by editing the `requirements.txt` to include the github repository of this package as one of the requirements.
```
-e git+git://github.com/a6kme/setuptools-demo.git@releases#egg=setuptools_demo
```

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

## Version 0.2
This version adds numpy as it's dependency. When we install this package, numpy should be installed with this
