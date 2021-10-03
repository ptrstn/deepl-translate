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


with open(os.path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="deepl-translate",
    version=find_version("deepl", "__init__.py"),
    desription="Python package to translate text using deepl.com",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="http://github.com/ptrstn/deepl-translate",
    author="Peter Stein",
    license="MIT",
    packages=["deepl"],
    install_requires=["requests"],
    entry_points={"console_scripts": ["deepl=deepl.__main__:main"]},
    classifiers=["License :: OSI Approved :: MIT License"],
)
