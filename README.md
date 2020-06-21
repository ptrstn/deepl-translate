[![Build Status](https://travis-ci.com/ptrstn/deepl-translate.svg?branch=master)](https://travis-ci.com/ptrstn/deepl-translate)
[![codecov](https://codecov.io/gh/ptrstn/deepl-translate/branch/master/graph/badge.svg)](https://codecov.io/gh/ptrstn/deepl-translate)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

# DeepL Translate

An unofficial python package to translate text using [DeepL](https://www.deepl.com/).

## Installation

```bash
pip install git+https://github.com/ptrstn/deepl-translate
```

## Usage

### Supported languages

Currently the following languages are supported:

| Abbreviation | Language   | Writing in own language |
|--------------|------------|-------------------------|
| DE           | German     | Deutsch                 |
| EN           | English    | English                 |
| FR           | French     | français                |
| ES           | Spanish    | español                 |
| PT           | Portuguese | português               |
| IT           | Italian    | italiano                |
| NL           | Dutch      | Nederlands              |
| PL           | Polish     | polski                  |
| RU           | Russian    | русский                 |
| JA           | Japanese   | 日本語                   |
| ZH           | Chinese    | 中文                     |

You can either input the abbreviation or the language written in english. 

### Command line tool

#### Help

```bash
deepl --help
```

```
usage: deepl [-h] [--version] [-t TEXT | -f FILE] source_language target_language

Python client to translate texts using deepl.com

positional arguments:
  source_language       Source language of your text
  target_language       Target language of your desired text

optional arguments:
  -h, --help            show this help message and exit
  --version             show program's version number and exit
  -t TEXT, --text TEXT  Text to be translated
  -f FILE, --file FILE  File to be translated
```

#### Example 1

This will translate a Spanish (```ES```) text into Russian (```RU```):

```bash
deepl spanish russian -t "¡Buenos días!"
```

```
Доброе утро!
```

#### Example 2

This will translate a the file (```test.txt```) text from Italian (```IT```) into Portuguese (```PT```):

```bash
deepl IT PT --file test.txt
```

### Python library

#### Example

This will translate a Chinese (```ZH```) text into Dutch (```NL```):

```python
import deepl
deepl.translate(source_language="ZH", target_language="NL", text="你好")
```

```
'Hallo.'
```
