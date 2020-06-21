from deepl.settings import SUPPORTED_LANGUAGES


def create_abbreviations_dictionary(languages=SUPPORTED_LANGUAGES):
    short_dict = {language["code"].lower(): language["code"] for language in languages}
    verbose_dict = {
        language["language"].lower(): language["code"] for language in languages
    }
    return {**short_dict, **verbose_dict}


def abbreviate_language(language):
    language = language.lower()
    abbreviations = create_abbreviations_dictionary()
    return abbreviations.get(language.lower())


def read_file_lines(path):
    with open(path, "r") as file:
        return "\n".join(file.readlines())
