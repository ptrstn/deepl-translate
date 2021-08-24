from essential_generators import DocumentGenerator

from deepl.api import translate


def test_translate_russian():
    source_language = "RU"
    target_language = "EN"
    text = "Я сошла с ума"
    expected_translation = "I'm out of my mind."
    translation = translate(source_language, target_language, text)
    assert translation == expected_translation


def test_translate_chinese():
    source_language = "ZH"
    target_language = "dutch"
    text = "你好"
    expected_translation = "Hallo!"
    translation = translate(source_language, target_language, text)
    assert translation == expected_translation


def test_translate_sentence():
    text = "Up and down."
    expected_translation = "Op en neer."
    assert translate("EN", "NL", text) == expected_translation


def test_translate_sentences():
    text = (
        "His palms are sweaty, knees weak, arms are heavy. "
        "There's vomit on his sweater already, mom's spaghetti."
    )

    expected_translation = (
        "Seine Handflächen sind schweißnass, die Knie schwach, die Arme sind schwer. "
        "Auf seinem Pullover ist schon Erbrochenes, Mutters Spaghetti."
    )

    assert translate("EN", "DE", text) == expected_translation


def test_translate_generated_paragraph():
    generator = DocumentGenerator()
    text = generator.paragraph()
    translation = translate("EN", "DE", text)
    assert len(translation) > 1
