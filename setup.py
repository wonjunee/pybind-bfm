from setuptools import setup

from pybind11.setup_helpers import Pybind11Extension, build_ext
from pybind11 import get_cmake_dir

import sys

__version__ = "0.0.1"

ext_modules = [
    Pybind11Extension("w2",
        ["src/main.cpp"],
        define_macros = [('VERSION_INFO', __version__)],
        ),
]

setup(
    name="w2",
    version=__version__,
    author="Wonjun Lee",
    author_email="wlee@math.ucla.edu",
    description="Python wrapper for the back-and-forth method for optimal transport",
    long_description="",
    ext_modules=ext_modules,
    # extras_require={"test": "pytest"},
    # # Currently, build_ext only provides an optional "highest supported C++
    # # level" feature, but in the future it may provide more features.
#     cmdclass={"build_ext": build_ext},
#     zip_safe=False,
)
