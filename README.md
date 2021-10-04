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
| BG           | Bulgarian  | Български               |
| ZH           | Chinese    | 中文                    |
| CS           | Czech      | Česky                   |
| DA           | Danish     | Dansk                   |
| NL           | Dutch      | Nederlands              |
| EN           | English    | English                 |
| ET           | Estonian   | Eesti                   |
| FI           | Finnish    | Suomi                   |
| FR           | French     | Français                |
| DE           | German     | Deutsch                 |
| EL           | Greek      | Ελληνικά                |
| HU           | Hungarian  | Magyar                  |
| IT           | Italian    | Italiano                |
| JA           | Japanese   | 日本語                  |
| LV           | Latvian    | Latviešu                |
| LT           | Lithuanian | Lietuvių                |
| PL           | Polish     | Polski                  |
| PT           | Portuguese | Português               |
| RO           | Romanian   | Română                  |
| RU           | Russian    | Русский                 |
| SK           | Slovak     | Slovenčina              |
| SL           | Slovenian  | Slovenščina             |
| ES           | Spanish    | Español                 |
| SV           | Swedish    | Svenska                 |

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
