import pytest
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
    expected_translation = "Hallo"
    translation = translate(source_language, target_language, text)
    assert expected_translation in translation


def test_translate_greek_romanian():
    source_language = "gReEk"
    target_language = "ro"
    text = "Γεια σας"
    expected_translation = "bună ziua"
    translation = translate(source_language, target_language, text)
    assert expected_translation in translation.lower()


def test_translate_sentence():
    text = "Up and down."
    expected_translation = "Op en neer."
    assert translate("EN", "NL", text) == expected_translation


def test_translate_sentences():
    text = (
        "His palms are sweaty, knees weak, arms are heavy. "
        "There's vomit on his sweater already, mom's spaghetti."
    )

    translation = translate("EN", "DE", text)
    assert "Handfläche" in translation
    assert "Pullover" in translation
    assert "Spaghetti" in translation


def test_translate_generated_paragraph():
    generator = DocumentGenerator()
    text = generator.paragraph()
    translation = translate("EN", "DE", text)
    assert len(translation) > 1


def test_formal_german_translation():
    text = "What's your name?"
    expected_translations = ["Wie ist Ihr Name?", "Wie heißen Sie?"]
    translation = translate("EN", "DE", text, formality_tone="formal")
    assert translation in expected_translations


def test_informal_german_translation():
    text = "What's your name?"
    expected_translations = ["Wie ist dein Name?", "Wie heißt du?"]
    translation = translate("EN", "DE", text, formality_tone="informal")
    assert translation in expected_translations


def test_invalid_formal_tone():
    with pytest.raises(ValueError):
        translate("EN", "DE", "ABC", formality_tone="politically incorrect")
