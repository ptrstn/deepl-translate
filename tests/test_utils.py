from deepl.utils import abbreviate_language, read_file_lines


def test_abbreviate_language():
    assert "RU" == abbreviate_language("RuSsIaN")
    assert "RU" == abbreviate_language("ru")
    assert "JA" == abbreviate_language("japanese")
    assert "ZH" == abbreviate_language("ZH")
    assert abbreviate_language("wambo") is None


def test_read_file_lines():
    text = read_file_lines("README.md")
    assert "# DeepL Translate" in text
