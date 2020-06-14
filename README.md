[![Build Status](https://travis-ci.com/ptrstn/deeply.svg?branch=master)](https://travis-ci.com/ptrstn/deeply)
[![codecov](https://codecov.io/gh/ptrstn/deeply/branch/master/graph/badge.svg)](https://codecov.io/gh/ptrstn/deeply)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

# Deeply

A python package to translate text using [DeepL](https://www.deepl.com/).

## Installation

```bash
pip install --user git+https://github.com/ptrstn/deeply
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
deeply --help
```

```
usage: deeply [-h] [--version] source target text

Python client to translate texts using deepl.com

positional arguments:
  source      Source language of your text
  target      Target language of your desired text
  text        Text to be translated

optional arguments:
  -h, --help  show this help message and exit
  --version   show program's version number and exit
```

#### Example

This will translate a Spanish (```ES```) text into Russian (```RU```):

```bash
deeply spanish russian "¡Buenos días!"
```

```
Доброе утро!
```

### Python library

#### Example

This will translate a Chinese (```ZH```) text into Dutch (```NL```):

```python
import deeply
deeply.translate(source_language="ZH", target_language="NL", text="你好")
```

```
'Hallo.'
```
