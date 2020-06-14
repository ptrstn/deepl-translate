import codecs
import os
import re

from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))


def read(*parts):
    with codecs.open(os.path.join(here, *parts), "r") as fp:
        return fp.read()


def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


setup(
    name="deeply",
    version=find_version("deeply", "__init__.py"),
    url="http://github.com/ptrstn/deeply",
    author="Peter Stein",
    license="MIT",
    packages=["deeply"],
    install_requires=["requests"],
    entry_points={"console_scripts": ["deeply=deeply.__main__:main"]},
)
