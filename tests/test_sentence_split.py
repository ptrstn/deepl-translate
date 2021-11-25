from deepl.api import split_into_sentences


def test_split_into_sentences():
    text = (
        "This is a text. This text has words. "
        "The end? The end! I'm not sure... who knows."
    )
    expected_sentences = [
        "This is a text.",
        "This text has words.",
        "The end?",
        "The end!",
        "I'm not sure... who knows.",
    ]

    sentences = split_into_sentences(text)
    assert sentences == expected_sentences
