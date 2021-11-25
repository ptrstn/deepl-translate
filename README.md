[![Python Package](https://github.com/ptrstn/deepl-translate/actions/workflows/python-package.yml/badge.svg)](https://github.com/ptrstn/deepl-translate/actions/workflows/python-package.yml)
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
usage: deepl [-h] [--version] [--formal | --informal] [-t TEXT | -f FILE] source_language target_language

Python client to translate texts using deepl.com

positional arguments:
  source_language       Source language of your text
  target_language       Target language of your desired text

optional arguments:
  -h, --help            show this help message and exit
  --version             show program's version number and exit
  --formal              Use formal tone in translation
  --informal            Use informal tone in translation
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

This will translate the file (```test.txt```) text from Italian (```IT```) into Portuguese (```PT```):

```bash
deepl IT PT --file test.txt
```

#### Example 3

This will translate a Spanish (```ES```) text into Russian (```RU```) in _formal_ tone:

```bash
deepl ES RU --text "¿Cómo te llamas?" --formal
```

```
Как Вас зовут?
```

Note: _informal_ would be "_Как **тебя** зовут?_"

#### Example 4

This will translate a Japanese (```JP```) text into German (```DE```) in _informal_ tone:

```bash
deepl JP DE --text "お元気ですか？" --informal
```

```
Wie geht es dir?
```

Note: _formal_ would be "_Wie geht es **Ihnen**?_"

### Python library

#### Example 1

This will translate a Chinese (```ZH```) text into Dutch (```NL```):

```python
import deepl
deepl.translate(source_language="ZH", target_language="NL", text="你好")
```

```
'Hallo'
```

#### Example 2

This will translate a ```danish``` text into ```german``` in informal tone:

```python
import deepl
deepl.translate(source_language="danish", target_language="german", text="Ring til mig!", formality_tone="informal")
```

```
'Ruf mich an!'
```
