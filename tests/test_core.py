import deeply


def test_translate_russian():
    language_from = "RU"
    language_to = "EN"
    text = "Я сошла с ума"
    expected_translation = "I'm out of my mind."
    translation = deeply.translate(
        source_language=language_from, target_language=language_to, text=text
    )
    assert translation == expected_translation


def test_translate_chinese():
    language_from = "ZH"
    language_to = "dutch"
    text = "你好"
    expected_translation = "Hallo."
    translation = deeply.translate(
        source_language=language_from, target_language=language_to, text=text
    )
    assert translation == expected_translation
