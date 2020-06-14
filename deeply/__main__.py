import argparse

import deeply
from deeply import __version__


def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Python client to translate texts using deepl.com"
    )

    parser.add_argument(
        "--version", action="version", version="%(prog)s {}".format(__version__)
    )

    parser.add_argument("source", help="Source language of your text")

    parser.add_argument("target", help="Target language of your desired text")

    parser.add_argument("text", help="Text to be translated")

    return parser.parse_args()


def main():
    args = parse_arguments()
    source_language = args.source
    target_language = args.target
    text = args.text
    print(deeply.translate(source_language, target_language, text))


if __name__ == "__main__":
    main()
